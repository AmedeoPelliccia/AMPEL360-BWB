#!/usr/bin/env python3
"""
UTCS-ID Filename Validator for GitHub Actions
==============================================

Validates that files follow UTCS-ID naming convention:
    LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_VxRy

Part of AMPEL360-BWB-EXLC CI/CD pipeline
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import json

# UTCS-ID pattern based on specification
UTCS_ID_PATTERN = re.compile(
    r'^LC-(?P<stage>[123])(?P<substage>\d{1,2})_'
    r'(?P<ataidx>\d{2,6}[A-Z]?(-\d{2})?)-(?P<atadesc>[A-Z_]+)_'
    r'(?P<func>[A-Z0-9_]{3,12})_'
    r'V(?P<version>\d+)R(?P<revision>\d+)'
    r'(?P<ext>\.[a-zA-Z0-9]+)?$'
)

# Relaxed pattern for partial matches (for reporting)
PARTIAL_PATTERN = re.compile(r'LC-\d')

# File extensions that should be checked
CHECKED_EXTENSIONS = {
    '.md', '.pdf', '.docx', '.xlsx',
    '.cad', '.step', '.iges', '.stl',
    '.py', '.c', '.cpp', '.h', '.hpp',
    '.json', '.yaml', '.yml', '.xml',
    '.fea', '.cfd', '.fem',
    '.zip', '.tar', '.gz'
}

# Directories to skip
SKIP_DIRS = {
    '.git', '.github', 'node_modules', '__pycache__', 
    '.venv', 'venv', 'build', 'dist', '.pytest_cache'
}

# Files to always skip
SKIP_FILES = {
    'README.md', 'LICENSE', 'CONTRIBUTING.md', 'CHANGELOG.md',
    '.gitignore', '.gitattributes', 'requirements.txt',
    'setup.py', 'setup.cfg', 'pyproject.toml',
    'package.json', 'package-lock.json',
    'ATA_MAP.yaml', 'ata_resolver.py',
    'UTCS-ID_Specification_v1.0.md',
    'AMPEL360_LC_FRAMEWORK.md'
}


class ValidationResult:
    """Result of filename validation"""
    
    def __init__(self):
        self.total_files = 0
        self.checked_files = 0
        self.skipped_files = 0
        self.valid_files = 0
        self.invalid_files = 0
        self.errors: List[Tuple[str, str]] = []
        self.warnings: List[Tuple[str, str]] = []
        self.valid_paths: List[str] = []
    
    def add_error(self, filepath: str, message: str):
        """Add validation error"""
        self.errors.append((filepath, message))
        self.invalid_files += 1
    
    def add_warning(self, filepath: str, message: str):
        """Add validation warning"""
        self.warnings.append((filepath, message))
    
    def add_valid(self, filepath: str):
        """Mark file as valid"""
        self.valid_paths.append(filepath)
        self.valid_files += 1
    
    def print_summary(self):
        """Print validation summary"""
        print("=" * 80)
        print("UTCS-ID FILENAME VALIDATION SUMMARY")
        print("=" * 80)
        print(f"Total files scanned:     {self.total_files}")
        print(f"Files checked:           {self.checked_files}")
        print(f"Files skipped:           {self.skipped_files}")
        print(f"Valid UTCS-ID files:     {self.valid_files}")
        print(f"Invalid files:           {self.invalid_files}")
        print(f"Warnings:                {len(self.warnings)}")
        print()
        
        if self.errors:
            print("❌ ERRORS:")
            for filepath, message in self.errors:
                print(f"  {filepath}")
                print(f"    → {message}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS:")
            for filepath, message in self.warnings:
                print(f"  {filepath}")
                print(f"    → {message}")
            print()
        
        if self.valid_files > 0:
            print(f"✅ {self.valid_files} files have valid UTCS-ID format")
        
        print("=" * 80)
        
        # Exit code based on errors (warnings are informational)
        return 0 if len(self.errors) == 0 else 1


def should_skip_file(filepath: Path) -> bool:
    """Check if file should be skipped"""
    # Skip by filename
    if filepath.name in SKIP_FILES:
        return True
    
    # Skip by directory
    for part in filepath.parts:
        if part in SKIP_DIRS:
            return True
    
    # Skip hidden files
    if filepath.name.startswith('.'):
        return True
    
    return False


def should_check_file(filepath: Path) -> bool:
    """Check if file extension should be validated"""
    return filepath.suffix.lower() in CHECKED_EXTENSIONS


def validate_utcs_filename(filename: str) -> Tuple[bool, Optional[str], Optional[dict]]:
    """
    Validate filename against UTCS-ID pattern
    
    Returns:
        (is_valid, error_message, parsed_components)
    """
    # Remove extension for validation
    name_without_ext = filename
    ext = ''
    if '.' in filename:
        name_without_ext, ext = filename.rsplit('.', 1)
        ext = '.' + ext
    
    # Try to match UTCS-ID pattern
    match = UTCS_ID_PATTERN.match(filename)
    
    if match:
        components = match.groupdict()
        
        # Validate LC stage
        stage = components['stage']
        substage = components['substage']
        if stage not in ['1', '2', '3']:
            return False, f"Invalid LC stage: {stage}", None
        
        # Validate substage ranges
        substage_int = int(substage)
        if stage == '1' and not (11 <= substage_int <= 17):
            return False, f"Invalid LC-1 substage: {substage}", None
        elif stage == '2' and not (21 <= substage_int <= 24):
            return False, f"Invalid LC-2 substage: {substage}", None
        elif stage == '3' and not (31 <= substage_int <= 34):
            return False, f"Invalid LC-3 substage: {substage}", None
        
        return True, None, components
    
    # Check if it looks like an attempt at UTCS-ID
    if PARTIAL_PATTERN.search(filename):
        return False, "Filename appears to attempt UTCS-ID format but is invalid", None
    
    # Not a UTCS-ID file (no error)
    return False, None, None


def scan_repository(repo_path: Path) -> ValidationResult:
    """Scan repository for UTCS-ID compliant files"""
    result = ValidationResult()
    
    print(f"Scanning repository: {repo_path}")
    print(f"Checking files with extensions: {', '.join(sorted(CHECKED_EXTENSIONS))}")
    print()
    
    for root, dirs, files in os.walk(repo_path):
        # Remove skip directories from search
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        
        for filename in files:
            filepath = Path(root) / filename
            rel_path = filepath.relative_to(repo_path)
            
            result.total_files += 1
            
            # Skip files that shouldn't be checked
            if should_skip_file(rel_path):
                result.skipped_files += 1
                continue
            
            # Only check files with relevant extensions
            if not should_check_file(filepath):
                result.skipped_files += 1
                continue
            
            result.checked_files += 1
            
            # Validate filename
            is_valid, error, components = validate_utcs_filename(filename)
            
            if is_valid:
                result.add_valid(str(rel_path))
            elif error:
                # This is an error - file tried to use UTCS-ID but failed
                result.add_error(str(rel_path), error)
            else:
                # This is just informational - file doesn't use UTCS-ID
                result.add_warning(
                    str(rel_path),
                    "File does not use UTCS-ID format (consider renaming for traceability)"
                )
    
    return result


def save_report(result: ValidationResult, output_path: Path):
    """Save validation report as JSON"""
    report = {
        'summary': {
            'total_files': result.total_files,
            'checked_files': result.checked_files,
            'skipped_files': result.skipped_files,
            'valid_files': result.valid_files,
            'invalid_files': result.invalid_files,
            'warnings': len(result.warnings)
        },
        'errors': [{'file': f, 'message': m} for f, m in result.errors],
        'warnings': [{'file': f, 'message': m} for f, m in result.warnings],
        'valid_files': result.valid_paths
    }
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"Report saved to: {output_path}")


def main():
    """Main entry point"""
    # Get repository root (assuming script is in .github/scripts)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    print("UTCS-ID Filename Validator")
    print("=" * 80)
    print()
    
    # Scan repository
    result = scan_repository(repo_root)
    
    # Save report
    report_path = repo_root / '.github' / 'reports' / 'utcs-validation.json'
    save_report(result, report_path)
    
    # Print summary
    exit_code = result.print_summary()
    
    # Note: We're lenient - warnings don't cause failure
    # Only actual UTCS-ID format errors cause failure
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
