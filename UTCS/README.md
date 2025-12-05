# UTCS — Unified Traceability Code Standard

## Overview

The UTCS (Unified Traceability Code Standard) provides a comprehensive identification and traceability framework for all artefacts throughout the AMPEL360 BWB aircraft lifecycle.

## Purpose

UTCS ensures:
- **Machine readability** for automated systems (CI/CD, GenCCC, CAOS, DPP)
- **Human readability** for engineering, certification, and operations teams
- **Deterministic derivation** from structured taxonomies (ATA, LC stages)
- **Long-term traceability** across the entire aircraft lifecycle
- **Global uniqueness** for all artefacts

## Documentation

### Core Specifications

- **[UTCS-ID Specification v1.0](./UTCS-ID_Specification_v1.0.md)** - The unified identifier format for all lifecycle artefacts
- **[ATA_MAP.yaml](./ATA_MAP.yaml)** - Official ATA dictionary for automatic ATADESC generation
- **[ata_resolver.py](./ata_resolver.py)** - Python resolver for ATA code validation and ATADESC generation

## UTCS-ID Format

All AMPEL360 artefacts use a unified identifier format:

```
LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_VxRy
```

### Components

- **LC-{STAGE}{SUBSTAGE}**: Lifecycle stage and substage (e.g., LC-16 = Development, Engineering Analysis)
- **{ATAIDX}**: 2-, 4-, or 6-digit ATA iSpec 2200 code
- **{ATADESC}**: Automatically derived human-readable ATA description
- **{FUNC}**: Functional descriptor (CFD, FEM, NNMODEL, etc.)
- **VxRy**: Version and revision (e.g., V1R3)

### Examples

```
LC-16_572301-WINGS_SLATS_FLAP_WELL_ENV_CFD_V1R3
LC-17_953021-NEURAL_NETWORKS_NN_ECS_NN_ECS_CABIN_TEMP_NNMODEL_V2R0
LC-32_210501-AIR_CONDITIONING_ECS_SENSOR_MROPROC_V1R0
```

## Integration

UTCS integrates with:

- **LC Framework**: All three lifecycle pillars (Development, Manufacturing, Series Operations)
- **OPT-IN**: Organization, Program, Technical, Infrastructure, Neural Networks axes
- **GenCCC**: Generative Configuration & Compliance Checking
- **CAOS**: Computer Aided Operations & Services
- **DPP**: Digital Product Passport
- **V&V Lake**: Verification & Validation data repository

## Lifecycle Stages

### LC-1 Development (Stages 11-17)
- 11: Research & Concept Development
- 12: Safety Analysis & Preliminary Risk
- 13: Requirements Engineering
- 14: Detailed Design
- 15: Interfaces & Constituency Assemblies
- 16: Engineering Analysis & Integration
- 17: Verification & Validation

### LC-2 Manufacturing (Stages 21-24)
- 21: Prototype Manufacturing
- 22: Test Campaign & Certification
- 23: Final Assembly Line & Production
- 24: Production Quality & Conformity

### LC-3 Series Operations (Stages 31-34)
- 31: Configuration & Change Management
- 32: MRO (Maintenance, Repair, Overhaul)
- 33: Customer Support & Services
- 34: PNR, Spares & Circular Economy

## ATA Integration

UTCS leverages the ATA iSpec 2200 taxonomy for system classification:

- **2-digit**: System level (e.g., 57 = Wings, 21 = Air Conditioning)
- **4-digit**: Section/Subsection (e.g., 5723 = Slats)
- **6-digit**: Subject/Sub-subsystem (e.g., 572301 = Flap Well Envelope)

Special AMPEL360 ATA chapters:
- **ATA 28H**: Hydrogen Storage and Distribution
- **ATA 85**: Green-E Battery Energy Storage
- **ATA 95**: AI/NN Orchestration Systems (NN-ECS, NN-FCS, NN-IMA)

## Compliance

All AMPEL360 artefacts must comply with UTCS-ID format for:
- Release documentation
- Model artefacts
- Safety-critical components
- Neural Network deliverables (ATA 95)
- Infrastructure components (ATA 02 / CAOS)

## ATA Dictionary

### [ATA_MAP.yaml](./ATA_MAP.yaml)

The ATA_MAP.yaml provides the official dictionary for automatic ATADESC generation. It includes:

- **70+ Standard ATA Chapters** (00-80): Complete coverage of traditional aircraft systems
- **AMPEL360 Extended Chapters**: Custom systems for hydrogen, battery, and AI/NN
  - ATA 28H: Hydrogen storage and distribution
  - ATA 85: Green-E battery energy storage
  - ATA 85-30: ANCHORS circularity framework
  - ATA 95: AI/NN orchestration systems
- **OPT-IN Axis Mapping**: Each system tagged with O/P/T/I/N classification
- **LC Stage Tags**: Applicability across Development, Manufacturing, Operations
- **Hierarchical Structure**: Systems (2-digit), Sections (4-digit), Subjects (6-digit)

The dictionary ensures deterministic, machine-readable, and human-friendly identifier generation for all lifecycle artefacts.

## Python Resolver

### [ata_resolver.py](./ata_resolver.py)

The Python resolver provides both CLI and programmatic access to ATA code resolution and validation.

**Features:**
- Resolve 2/4/6-digit ATA codes to ATADESC descriptors
- Validate ATA codes against the dictionary
- List systems filtered by OPT-IN axis or LC stage
- List sections and subjects hierarchically
- Support for AMPEL360 extended systems (28H, 85, 95)
- Multiple output formats (text, JSON, YAML)

**CLI Usage:**
```bash
# Resolve ATA codes
python ata_resolver.py 57                    # → WINGS
python ata_resolver.py 5723                  # → WINGS_SLATS
python ata_resolver.py 572301                # → WINGS_SLATS_FLAP_WELL_ENV

# Validate codes
python ata_resolver.py --validate 21         # Check if code exists

# List systems
python ata_resolver.py --list-systems        # All systems
python ata_resolver.py --by-axis T_TECHNOLOGY # Filter by OPT-IN axis
python ata_resolver.py --by-lc LC1           # Filter by lifecycle stage

# Output formats
python ata_resolver.py 85 --format json      # JSON output
```

**Programmatic Usage:**
```python
from ata_resolver import ATAResolver

resolver = ATAResolver()
result = resolver.resolve("572301")
print(result.atadesc)  # WINGS_SLATS_FLAP_WELL_ENV
```

## GitHub Actions CI/CD

### Automated Validation

The repository includes GitHub Actions workflows for automated UTCS-ID validation:

**Workflow:** `.github/workflows/utcs-id-validation.yml`

**Features:**
- Validates ATA_MAP.yaml structure
- Tests ATA resolver functionality
- Scans repository for UTCS-ID compliant filenames
- Generates validation reports
- Checks Python code quality
- Uploads validation artifacts

**Validation Scripts:**
- `.github/scripts/validate_utcs_filenames.py` - Filename validator
- `.github/scripts/generate_validation_report.py` - Report generator

**Triggers:**
- Every push to main/develop branches
- Every pull request
- Manual workflow dispatch

**Reports:**
- JSON report: `.github/reports/utcs-validation.json`
- Markdown report: `.github/reports/utcs-validation-report.md`

See [.github/README.md](../.github/README.md) for detailed CI/CD documentation.

## Implementation Tools

Implementation artifacts:
1. ✅ **ATA_MAP.yaml** - Official ATA dictionary (implemented)
2. ✅ **Python resolver (ata_resolver.py)** - Tool to enforce/validate IDs automatically (implemented)
3. ✅ **GitHub Actions** - CI rules for automated validation (implemented)

## References

- [AMPEL360 LC Framework](../AMPEL360_LC_FRAMEWORK.md)
- [ATA iSpec 2200 Documentation Standard](https://www.ataebiz.org/)
- [OPT-IN Framework](../README.md)

## Status

**Current Version**: 1.0  
**Status**: RELEASE  
**Owner**: AMPEL360 / OPT-IN Governance
