#!/usr/bin/env python3
"""
ATA Resolver for AMPEL360-BWB-EXLC UTCS-ID System
=================================================

Resolves ATAIDX (2/4/6/8 digit codes) to ATADESC (UPPER_SNAKE_CASE descriptors)
for deterministic UTCS-ID generation.

Usage:
    CLI:    python ata_resolver.py 952021
            python ata_resolver.py --validate 21
            python ata_resolver.py --list-systems
            python ata_resolver.py --by-axis T_TECHNOLOGY
            python ata_resolver.py --by-lc LC1
    
    Module: 
        from ata_resolver import ATAResolver
        resolver = ATAResolver()
        result = resolver.resolve("952021")
        print(result.atadesc)  # NEURAL_NETWORKS_NN_ECS_NN_ECS_CABIN_TEMP

Part of the OPT-IN Framework Standard v2.0
AMPEL360-BWB-EXLC — eXtended LifeCycle, eXCeLLenCe by design
"""

import yaml
import sys
import os
import argparse
import json
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any, Union
from dataclasses import dataclass, field, asdict
from enum import Enum


# =============================================================================
# ENUMS AND DATA CLASSES
# =============================================================================

class ATAResolutionLevel(Enum):
    """Resolution granularity levels"""
    SYSTEM = 2      # 2-digit: ATA system
    SECTION = 4     # 4-digit: ATA section
    SUBJECT = 6     # 6-digit: ATA subject
    EXTENDED = 8    # 8-digit: Extended chapters (100+)


class OPTINAxis(Enum):
    """OPT-IN Framework axes"""
    O_ORGANIZATION = "O"
    P_PROGRAM = "P"
    T_TECHNOLOGY = "T"
    I_INFRASTRUCTURE = "I"
    N_NEURAL_NETWORKS = "N"


class LCStage(Enum):
    """Lifecycle stages"""
    LC1 = "LC1"  # Development
    LC2 = "LC2"  # Manufacturing
    LC3 = "LC3"  # Operations


@dataclass
class ATAResolution:
    """Result of ATA code resolution"""
    ataidx: str
    atadesc: str
    level: ATAResolutionLevel
    system_code: str
    system_name: str
    section_code: Optional[str] = None
    section_name: Optional[str] = None
    subject_code: Optional[str] = None
    subject_name: Optional[str] = None
    optin_axis: Optional[str] = None
    lc_stages: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    description: str = ""
    is_ampel360_extended: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation"""
        d = asdict(self)
        # Convert Enum to string for JSON serialization
        d['level'] = self.level.name
        return d
    
    def to_json(self) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=2)


@dataclass
class ValidationResult:
    """Result of ATA code validation"""
    is_valid: bool
    ataidx: str
    message: str
    resolution: Optional[ATAResolution] = None


# =============================================================================
# ATA RESOLVER
# =============================================================================

class ATAResolver:
    """
    Resolves ATA codes to descriptive names using ATA_MAP.yaml
    
    Supports hierarchical resolution:
    - 2-digit: System level (e.g., 57 → WINGS)
    - 4-digit: Section level (e.g., 5723 → WINGS_SLATS)
    - 6-digit: Subject level (e.g., 572301 → WINGS_SLATS_FLAP_WELL_ENV)
    """
    
    def __init__(self, ata_map_path: Optional[Path] = None):
        """
        Initialize resolver with ATA dictionary
        
        Args:
            ata_map_path: Path to ATA_MAP.yaml file. If None, searches in default locations.
        """
        self.ata_map_path = ata_map_path or self._find_ata_map()
        self.ata_map = self._load_ata_map()
        self.systems = self.ata_map.get('systems', {})
        self.sections = self.ata_map.get('sections', {})
        self.subjects = self.ata_map.get('subjects', {})
        self.meta = self.ata_map.get('meta', {})
    
    def _find_ata_map(self) -> Path:
        """Find ATA_MAP.yaml in default locations"""
        # Try current directory
        current_dir = Path.cwd()
        candidates = [
            current_dir / 'ATA_MAP.yaml',
            current_dir / 'UTCS' / 'ATA_MAP.yaml',
            Path(__file__).parent / 'ATA_MAP.yaml',
        ]
        
        for candidate in candidates:
            if candidate.exists():
                return candidate
        
        raise FileNotFoundError(
            "ATA_MAP.yaml not found. Please provide path explicitly or "
            "ensure file is in current directory or UTCS/ subdirectory."
        )
    
    def _load_ata_map(self) -> Dict[str, Any]:
        """Load and parse ATA_MAP.yaml"""
        try:
            with open(self.ata_map_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except Exception as e:
            raise RuntimeError(f"Failed to load ATA_MAP.yaml: {e}")
    
    def resolve(self, ataidx: str) -> ATAResolution:
        """
        Resolve ATA code to descriptive name
        
        Args:
            ataidx: ATA code (2, 4, 6, or 8 digits, may include letters like 28H)
        
        Returns:
            ATAResolution with hierarchical descriptors
        
        Raises:
            ValueError: If code format is invalid
        """
        # Clean and validate input
        ataidx = str(ataidx).strip().upper()
        
        # Determine resolution level
        level = self._determine_level(ataidx)
        
        # Extract components
        system_code = self._extract_system_code(ataidx)
        section_code = self._extract_section_code(ataidx) if len(ataidx) >= 4 else None
        subject_code = ataidx if len(ataidx) >= 6 else None
        
        # Resolve system
        system_info = self.systems.get(system_code, {})
        if not system_info:
            return self._create_fallback_resolution(ataidx, level)
        
        system_name = system_info.get('name', f'UNKNOWN_SYSTEM_{system_code}')
        
        # Build ATADESC
        atadesc_parts = [system_name]
        section_name = None
        subject_name = None
        
        # Resolve section if applicable
        if section_code and len(ataidx) >= 4:
            section_info = self.sections.get(section_code, {})
            if section_info:
                section_name = section_info.get('name', f'UNKNOWN_SECTION_{section_code}')
                atadesc_parts.append(section_name)
            else:
                atadesc_parts.append(f'UNKNOWN_SECTION_{section_code[2:]}')
        
        # Resolve subject if applicable
        if subject_code and len(ataidx) >= 6:
            subject_info = self.subjects.get(subject_code, {})
            if subject_info:
                subject_name = subject_info.get('name', f'UNKNOWN_SUBJECT_{subject_code}')
                atadesc_parts.append(subject_name)
            else:
                atadesc_parts.append(f'UNKNOWN_SUBJECT_{subject_code[4:]}')
        
        # Join parts with underscore
        atadesc = '_'.join(atadesc_parts)
        
        # Check if AMPEL360 extended
        is_extended = system_code in ['28H', '85', '95'] or 'AMPEL360' in system_info.get('tags', [])
        
        return ATAResolution(
            ataidx=ataidx,
            atadesc=atadesc,
            level=level,
            system_code=system_code,
            system_name=system_name,
            section_code=section_code,
            section_name=section_name,
            subject_code=subject_code,
            subject_name=subject_name,
            optin_axis=system_info.get('optin_axis'),
            lc_stages=system_info.get('lc_stages', []),
            tags=system_info.get('tags', []),
            description=system_info.get('description', ''),
            is_ampel360_extended=is_extended
        )
    
    def _determine_level(self, ataidx: str) -> ATAResolutionLevel:
        """Determine resolution level from code length"""
        # Remove letters for length check
        numeric_part = ''.join(c for c in ataidx if c.isdigit())
        length = len(ataidx)
        
        if length <= 2 or (length == 3 and ataidx[2].isalpha()):  # e.g., "28H"
            return ATAResolutionLevel.SYSTEM
        elif length == 4:
            return ATAResolutionLevel.SECTION
        elif length == 6:
            return ATAResolutionLevel.SUBJECT
        else:
            return ATAResolutionLevel.EXTENDED
    
    def _extract_system_code(self, ataidx: str) -> str:
        """Extract 2-digit system code (may include letter like 28H)"""
        if len(ataidx) >= 3 and ataidx[2].isalpha():
            return ataidx[:3]  # e.g., "28H"
        return ataidx[:2]
    
    def _extract_section_code(self, ataidx: str) -> Optional[str]:
        """Extract 4-digit section code"""
        if len(ataidx) < 4:
            return None
        
        # Handle special cases like 28H
        if len(ataidx) >= 3 and ataidx[2].isalpha():
            if len(ataidx) >= 5:
                return ataidx[:5]  # e.g., "28H01"
            return None
        
        return ataidx[:4]
    
    def _create_fallback_resolution(self, ataidx: str, level: ATAResolutionLevel) -> ATAResolution:
        """Create fallback resolution for unknown codes"""
        system_code = self._extract_system_code(ataidx)
        
        return ATAResolution(
            ataidx=ataidx,
            atadesc=f'UNKNOWN_ATA_{ataidx}',
            level=level,
            system_code=system_code,
            system_name=f'UNKNOWN_SYSTEM_{system_code}',
            description='Unknown ATA code - not found in dictionary'
        )
    
    def validate(self, ataidx: str) -> ValidationResult:
        """
        Validate ATA code existence in dictionary
        
        Args:
            ataidx: ATA code to validate
        
        Returns:
            ValidationResult with validation status
        """
        try:
            resolution = self.resolve(ataidx)
            
            is_valid = not resolution.atadesc.startswith('UNKNOWN_ATA_')
            
            if is_valid:
                message = f"Valid ATA code: {ataidx} → {resolution.atadesc}"
            else:
                message = f"Invalid ATA code: {ataidx} not found in dictionary"
            
            return ValidationResult(
                is_valid=is_valid,
                ataidx=ataidx,
                message=message,
                resolution=resolution
            )
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                ataidx=ataidx,
                message=f"Validation error: {str(e)}"
            )
    
    def list_systems(self, optin_axis: Optional[str] = None, 
                    lc_stage: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all available systems with optional filtering
        
        Args:
            optin_axis: Filter by OPT-IN axis (e.g., 'T_TECHNOLOGY')
            lc_stage: Filter by LC stage (e.g., 'LC1')
        
        Returns:
            List of system definitions
        """
        systems_list = []
        
        for code, info in self.systems.items():
            # Apply filters
            if optin_axis and info.get('optin_axis') != optin_axis:
                continue
            
            if lc_stage and lc_stage not in info.get('lc_stages', []):
                continue
            
            systems_list.append({
                'code': code,
                'name': info.get('name'),
                'optin_axis': info.get('optin_axis'),
                'lc_stages': info.get('lc_stages', []),
                'tags': info.get('tags', []),
                'description': info.get('description', '')
            })
        
        return sorted(systems_list, key=lambda x: x['code'])
    
    def list_sections(self, system_code: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all available sections with optional system filter
        
        Args:
            system_code: Filter by system code (e.g., '57')
        
        Returns:
            List of section definitions
        """
        sections_list = []
        
        for code, info in self.sections.items():
            # Apply system filter
            if system_code:
                parent = info.get('parent', '')
                if parent != system_code:
                    continue
            
            sections_list.append({
                'code': code,
                'name': info.get('name'),
                'parent': info.get('parent'),
                'description': info.get('description', '')
            })
        
        return sorted(sections_list, key=lambda x: x['code'])
    
    def list_subjects(self, section_code: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List all available subjects with optional section filter
        
        Args:
            section_code: Filter by section code (e.g., '5723')
        
        Returns:
            List of subject definitions
        """
        subjects_list = []
        
        for code, info in self.subjects.items():
            # Apply section filter
            if section_code:
                parent = info.get('parent', '')
                if parent != section_code:
                    continue
            
            subjects_list.append({
                'code': code,
                'name': info.get('name'),
                'parent': info.get('parent'),
                'description': info.get('description', '')
            })
        
        return sorted(subjects_list, key=lambda x: x['code'])
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get ATA_MAP metadata"""
        return self.meta


# =============================================================================
# CLI INTERFACE
# =============================================================================

def create_parser() -> argparse.ArgumentParser:
    """Create CLI argument parser"""
    parser = argparse.ArgumentParser(
        description='ATA Resolver for AMPEL360-BWB-EXLC UTCS-ID System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Resolve ATA codes:
    %(prog)s 57
    %(prog)s 5723
    %(prog)s 572301
    %(prog)s 28H
    %(prog)s 95
  
  Validate codes:
    %(prog)s --validate 21
    %(prog)s --validate 9502
  
  List systems:
    %(prog)s --list-systems
    %(prog)s --by-axis T_TECHNOLOGY
    %(prog)s --by-lc LC1
  
  List sections/subjects:
    %(prog)s --list-sections
    %(prog)s --list-sections --system 57
    %(prog)s --list-subjects --section 5723
  
  Output formats:
    %(prog)s 572301 --format json
    %(prog)s --list-systems --format yaml
        """
    )
    
    # Positional argument for resolution
    parser.add_argument(
        'ataidx',
        nargs='?',
        help='ATA code to resolve (2, 4, or 6 digits)'
    )
    
    # Actions
    parser.add_argument(
        '--validate',
        metavar='CODE',
        help='Validate ATA code existence'
    )
    
    parser.add_argument(
        '--list-systems',
        action='store_true',
        help='List all available ATA systems'
    )
    
    parser.add_argument(
        '--list-sections',
        action='store_true',
        help='List all available sections'
    )
    
    parser.add_argument(
        '--list-subjects',
        action='store_true',
        help='List all available subjects'
    )
    
    # Filters
    parser.add_argument(
        '--by-axis',
        metavar='AXIS',
        help='Filter by OPT-IN axis (e.g., T_TECHNOLOGY)'
    )
    
    parser.add_argument(
        '--by-lc',
        metavar='STAGE',
        help='Filter by LC stage (LC1, LC2, or LC3)'
    )
    
    parser.add_argument(
        '--system',
        metavar='CODE',
        help='Filter sections by system code'
    )
    
    parser.add_argument(
        '--section',
        metavar='CODE',
        help='Filter subjects by section code'
    )
    
    # Output options
    parser.add_argument(
        '--format',
        choices=['text', 'json', 'yaml'],
        default='text',
        help='Output format (default: text)'
    )
    
    parser.add_argument(
        '--ata-map',
        type=Path,
        help='Path to ATA_MAP.yaml file'
    )
    
    parser.add_argument(
        '--metadata',
        action='store_true',
        help='Show ATA_MAP metadata'
    )
    
    return parser


def format_output(data: Any, format_type: str) -> str:
    """Format output based on specified format"""
    if format_type == 'json':
        if isinstance(data, ATAResolution):
            return data.to_json()
        return json.dumps(data, indent=2)
    elif format_type == 'yaml':
        return yaml.dump(data, default_flow_style=False, sort_keys=False)
    else:  # text
        if isinstance(data, ATAResolution):
            lines = [
                f"ATAIDX:      {data.ataidx}",
                f"ATADESC:     {data.atadesc}",
                f"Level:       {data.level.name}",
                f"System:      [{data.system_code}] {data.system_name}",
            ]
            if data.section_name:
                lines.append(f"Section:     [{data.section_code}] {data.section_name}")
            if data.subject_name:
                lines.append(f"Subject:     [{data.subject_code}] {data.subject_name}")
            if data.optin_axis:
                lines.append(f"OPT-IN Axis: {data.optin_axis}")
            if data.lc_stages:
                lines.append(f"LC Stages:   {', '.join(data.lc_stages)}")
            if data.tags:
                lines.append(f"Tags:        {', '.join(data.tags)}")
            if data.description:
                lines.append(f"Description: {data.description}")
            if data.is_ampel360_extended:
                lines.append(f"AMPEL360:    Extended system")
            return '\n'.join(lines)
        elif isinstance(data, list):
            lines = []
            for item in data:
                if isinstance(item, dict):
                    code = item.get('code', '')
                    name = item.get('name', '')
                    desc = item.get('description', '')
                    lines.append(f"[{code}] {name}")
                    if desc:
                        lines.append(f"  {desc}")
            return '\n'.join(lines)
        else:
            return str(data)


def main():
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        # Initialize resolver
        resolver = ATAResolver(ata_map_path=args.ata_map)
        
        # Show metadata
        if args.metadata:
            data = resolver.get_metadata()
            print(format_output(data, args.format))
            return 0
        
        # List systems
        if args.list_systems:
            systems = resolver.list_systems(
                optin_axis=args.by_axis,
                lc_stage=args.by_lc
            )
            print(format_output(systems, args.format))
            return 0
        
        # List sections
        if args.list_sections:
            sections = resolver.list_sections(system_code=args.system)
            print(format_output(sections, args.format))
            return 0
        
        # List subjects
        if args.list_subjects:
            subjects = resolver.list_subjects(section_code=args.section)
            print(format_output(subjects, args.format))
            return 0
        
        # Validate code
        if args.validate:
            result = resolver.validate(args.validate)
            print(result.message)
            if result.resolution and args.format != 'text':
                print(format_output(result.resolution, args.format))
            return 0 if result.is_valid else 1
        
        # Resolve code
        if args.ataidx:
            resolution = resolver.resolve(args.ataidx)
            print(format_output(resolution, args.format))
            return 0
        
        # No action specified
        parser.print_help()
        return 1
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
