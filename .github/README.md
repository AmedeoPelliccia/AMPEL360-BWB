# AMPEL360 CI/CD Workflows

This directory contains GitHub Actions workflows and scripts for automated validation and quality assurance of the AMPEL360-BWB-EXLC repository.

## Workflows

### 1. UTCS-ID Validation (`workflows/utcs-id-validation.yml`)

Validates UTCS-ID compliance for files in the repository.

**Triggers:**
- Push to `main`, `develop`, `feature/**`, `release/**` branches
- Pull requests to `main` and `develop` branches

**Jobs:**

#### `validate-utcs-ids`
Validates filenames against UTCS-ID specification:
- Checks ATA_MAP.yaml validity
- Tests ATA resolver functionality
- Validates UTCS-ID compliant filenames
- Generates validation reports
- Uploads validation artifacts

#### `check-ata-dictionary`
Verifies ATA dictionary completeness:
- Reports system/section/subject statistics
- Lists AMPEL360 extended systems
- Validates dictionary structure

#### `lint-python`
Lints Python code:
- Runs flake8 static analysis
- Validates Python syntax
- Checks code quality

## Scripts

### `scripts/validate_utcs_filenames.py`

Python script that scans the repository for UTCS-ID compliant filenames.

**Features:**
- Validates UTCS-ID format: `LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_VxRy`
- Validates LC stage and substage ranges
- Detects partial UTCS-ID attempts
- Generates detailed validation reports
- Configurable file extensions and skip patterns

**Usage:**
```bash
python .github/scripts/validate_utcs_filenames.py
```

**Output:**
- Console summary with statistics
- JSON report: `.github/reports/utcs-validation.json`

### `scripts/generate_validation_report.py`

Generates comprehensive validation reports from validation results.

**Features:**
- Creates markdown validation report
- Groups errors and warnings
- Provides UTCS-ID format reference
- Includes usage examples

**Usage:**
```bash
python .github/scripts/generate_validation_report.py
```

**Output:**
- Console summary
- Markdown report: `.github/reports/utcs-validation-report.md`

## Validation Rules

### UTCS-ID Format

Valid filenames must follow the pattern:

```
LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_VxRy.{ext}
```

**Components:**
- **STAGE**: `1` (Development), `2` (Manufacturing), `3` (Operations)
- **SUBSTAGE**: 
  - LC-1: 11-17 (7 development phases)
  - LC-2: 21-24 (4 manufacturing phases)
  - LC-3: 31-34 (4 operations phases)
- **ATAIDX**: 2/4/6-digit ATA code (e.g., `57`, `5723`, `572301`)
- **ATADESC**: UPPER_SNAKE_CASE descriptor from ATA dictionary
- **FUNC**: 3-12 character functional descriptor (UPPER_SNAKE_CASE)
- **VxRy**: Version (x) and Revision (y) numbers

**Examples:**
```
LC-16_572301-WINGS_SLATS_FLAP_WELL_ENV_CFD_V1R3.md
LC-17_950201-NEURAL_NETWORKS_NN_ECS_NN_ECS_CABIN_TEMP_NNMODEL_V2R0.py
LC-32_210501-AIR_CONDITIONING_ECS_SENSOR_MROPROC_V1R0.md
```

### Checked File Extensions

The validator checks files with these extensions:
- **Documents**: `.md`, `.md`, `.docx`, `.csv`
- **CAD**: `.cad`, `.step`, `.iges`, `.stl`
- **Code**: `.py`, `.c`, `.cpp`, `.h`, `.hpp`
- **Data**: `.json`, `.yaml`, `.yml`, `.xml`
- **Analysis**: `.fea`, `.cfd`, `.fem`
- **Archives**: `.zip`, `.tar`, `.gz`

### Skipped Files

The following are excluded from validation:
- **Directories**: `.git`, `.github`, `node_modules`, `__pycache__`, etc.
- **Standard files**: `README.md`, `LICENSE`, configuration files
- **UTCS core files**: `ATA_MAP.yaml`, `ata_resolver.py`, specifications

## Reports

Validation reports are saved in `.github/reports/`:

- `utcs-validation.json` - Detailed JSON report
- `utcs-validation-report.md` - Human-readable markdown report

Reports are uploaded as GitHub Actions artifacts with 30-day retention.

## Integration

### Local Testing

Test validation locally before committing:

```bash
# Validate filenames
python .github/scripts/validate_utcs_filenames.py

# Generate report
python .github/scripts/generate_validation_report.py

# View report
cat .github/reports/utcs-validation-report.md
```

### CI/CD Pipeline

The workflow runs automatically on:
- Every push to main branches
- Every pull request
- Manual workflow dispatch

### Status Badges

Add to README.md:

```markdown
[![UTCS-ID Validation](https://github.com/AmedeoPelliccia/AMPEL360-BWB/actions/workflows/utcs-id-validation.yml/badge.svg)](https://github.com/AmedeoPelliccia/AMPEL360-BWB/actions/workflows/utcs-id-validation.yml)
```

## Customization

### Modify Checked Extensions

Edit `CHECKED_EXTENSIONS` in `validate_utcs_filenames.py`:

```python
CHECKED_EXTENSIONS = {
    '.md', '.md', '.docx',  # Add your extensions
}
```

### Add Skip Patterns

Edit `SKIP_FILES` or `SKIP_DIRS` in `validate_utcs_filenames.py`:

```python
SKIP_FILES = {
    'README.md',
    'your-file.md',  # Add files to skip
}
```

### Adjust Validation Strictness

Modify validation logic in `validate_utcs_filename()` function to adjust rules.

## Troubleshooting

### Validation Fails

1. Check error messages in CI logs
2. Review `.github/reports/utcs-validation-report.md`
3. Use ATA resolver to verify codes:
   ```bash
   python UTCS/ata_resolver.py --validate YOUR_ATA_CODE
   ```

### Python Dependencies

Workflow installs:
- `pyyaml` - YAML parsing
- `flake8` - Python linting
- `pylint` - Code analysis

### Permissions

Ensure workflows have necessary permissions in repository settings:
- **Actions**: Read and write
- **Contents**: Read

## References

- [UTCS-ID Specification](../UTCS/UTCS-ID_Specification_v1.0.md)
- [ATA Dictionary](../UTCS/ATA_MAP.yaml)
- [ATA Resolver](../UTCS/ata_resolver.py)
- [LC Framework](../AMPEL360_LC_FRAMEWORK.md)

## Support

For issues or questions:
1. Check validation reports in `.github/reports/`
2. Review UTCS-ID specification
3. Test with ATA resolver
4. Open GitHub issue with validation output
