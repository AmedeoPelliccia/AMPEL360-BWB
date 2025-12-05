#!/usr/bin/env python3
"""
UTCS-ID Validation Report Generator
====================================

Generates comprehensive validation reports for CI/CD pipeline

Part of AMPEL360-BWB-EXLC CI/CD pipeline
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import os


def load_validation_report(report_path: Path) -> dict:
    """Load validation report JSON"""
    if not report_path.exists():
        print(f"Warning: Report file not found at {report_path}")
        return None
    
    with open(report_path, 'r') as f:
        return json.load(f)


def generate_markdown_report(report: dict, output_path: Path):
    """Generate markdown validation report"""
    lines = [
        "# UTCS-ID Validation Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}",
        f"**Repository:** {os.getenv('GITHUB_REPOSITORY', 'local')}",
        f"**Branch:** {os.getenv('GITHUB_REF_NAME', 'local')}",
        f"**Commit:** {os.getenv('GITHUB_SHA', 'local')[:7]}",
        "",
        "---",
        "",
        "## Summary",
        "",
        f"- **Total files scanned:** {report['summary']['total_files']}",
        f"- **Files checked:** {report['summary']['checked_files']}",
        f"- **Files skipped:** {report['summary']['skipped_files']}",
        f"- **Valid UTCS-ID files:** {report['summary']['valid_files']} ✅",
        f"- **Invalid files:** {report['summary']['invalid_files']} ❌",
        f"- **Warnings:** {report['summary']['warnings']} ⚠️",
        "",
    ]
    
    # Errors section
    if report['errors']:
        lines.extend([
            "## ❌ Errors",
            "",
            "The following files have UTCS-ID format errors:",
            "",
        ])
        
        for error in report['errors']:
            lines.append(f"### `{error['file']}`")
            lines.append(f"**Error:** {error['message']}")
            lines.append("")
    
    # Warnings section
    if report['warnings']:
        lines.extend([
            "## ⚠️ Warnings",
            "",
            "The following files could benefit from UTCS-ID naming:",
            "",
        ])
        
        # Group warnings by directory
        warnings_by_dir = {}
        for warning in report['warnings']:
            dir_name = str(Path(warning['file']).parent)
            if dir_name not in warnings_by_dir:
                warnings_by_dir[dir_name] = []
            warnings_by_dir[dir_name].append(warning)
        
        for dir_name in sorted(warnings_by_dir.keys()):
            lines.append(f"### Directory: `{dir_name}`")
            for warning in warnings_by_dir[dir_name]:
                filename = Path(warning['file']).name
                lines.append(f"- `{filename}`")
            lines.append("")
    
    # Valid files section
    if report['valid_files']:
        lines.extend([
            "## ✅ Valid UTCS-ID Files",
            "",
            f"Found {len(report['valid_files'])} files with valid UTCS-ID format:",
            "",
        ])
        
        for filepath in sorted(report['valid_files']):
            lines.append(f"- `{filepath}`")
        lines.append("")
    
    # UTCS-ID format reference
    lines.extend([
        "---",
        "",
        "## UTCS-ID Format Reference",
        "",
        "Valid UTCS-ID format:",
        "",
        "```",
        "LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_VxRy",
        "```",
        "",
        "**Components:**",
        "",
        "- `STAGE`: Lifecycle stage (1=Development, 2=Manufacturing, 3=Operations)",
        "- `SUBSTAGE`: Sub-phase code (11-17, 21-24, 31-34)",
        "- `ATAIDX`: ATA code (2, 4, or 6 digits)",
        "- `ATADESC`: Descriptive name (UPPER_SNAKE_CASE)",
        "- `FUNC`: Functional descriptor (3-12 chars)",
        "- `VxRy`: Version and revision",
        "",
        "**Examples:**",
        "",
        "```",
        "LC-16_572301-WINGS_SLATS_FLAP_WELL_ENV_CFD_V1R3.pdf",
        "LC-17_950201-NEURAL_NETWORKS_NN_ECS_NN_ECS_CABIN_TEMP_NNMODEL_V2R0.py",
        "LC-32_210501-AIR_CONDITIONING_ECS_SENSOR_MROPROC_V1R0.md",
        "```",
        "",
        "**Documentation:**",
        "",
        "- [UTCS-ID Specification](../../UTCS/UTCS-ID_Specification_v1.0.md)",
        "- [ATA Dictionary](../../UTCS/ATA_MAP.yaml)",
        "- [ATA Resolver](../../UTCS/ata_resolver.py)",
        "",
    ])
    
    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"Markdown report saved to: {output_path}")


def print_console_summary(report: dict):
    """Print summary to console"""
    print("=" * 80)
    print("VALIDATION REPORT SUMMARY")
    print("=" * 80)
    print()
    
    summary = report['summary']
    
    # Overall status
    if summary['invalid_files'] == 0:
        print("✅ VALIDATION PASSED")
        print(f"   {summary['valid_files']} files have valid UTCS-ID format")
    else:
        print("❌ VALIDATION FAILED")
        print(f"   {summary['invalid_files']} files have UTCS-ID format errors")
    
    print()
    
    # Statistics
    print("📊 Statistics:")
    print(f"   Total files:     {summary['total_files']}")
    print(f"   Checked:         {summary['checked_files']}")
    print(f"   Valid:           {summary['valid_files']} ✅")
    print(f"   Invalid:         {summary['invalid_files']} ❌")
    print(f"   Warnings:        {summary['warnings']} ⚠️")
    print(f"   Skipped:         {summary['skipped_files']}")
    print()
    
    # Top errors
    if report['errors']:
        print("❌ Top Errors:")
        for error in report['errors'][:5]:
            print(f"   • {error['file']}")
            print(f"     {error['message']}")
        
        if len(report['errors']) > 5:
            print(f"   ... and {len(report['errors']) - 5} more")
        print()
    
    # Recommendations
    if summary['warnings'] > 0:
        print("💡 Recommendations:")
        print(f"   {summary['warnings']} files could benefit from UTCS-ID naming")
        print("   Consider renaming for better traceability")
        print()
    
    print("=" * 80)


def main():
    """Main entry point"""
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Load validation report
    report_path = repo_root / '.github' / 'reports' / 'utcs-validation.json'
    report = load_validation_report(report_path)
    
    if not report:
        print("No validation report found. Run validation first.")
        sys.exit(1)
    
    # Generate markdown report
    md_report_path = repo_root / '.github' / 'reports' / 'utcs-validation-report.md'
    generate_markdown_report(report, md_report_path)
    
    # Print console summary
    print_console_summary(report)
    
    # Exit with appropriate code
    sys.exit(0 if report['summary']['invalid_files'] == 0 else 1)


if __name__ == '__main__':
    main()
