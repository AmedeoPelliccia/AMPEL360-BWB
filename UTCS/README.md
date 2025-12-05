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

## Implementation Tools

Recommended implementation artifacts:
1. **ATA_MAP.yaml** - Official ATA dictionary for automatic ATADESC generation
2. **Python resolver** - Tool to enforce/validate IDs automatically
3. **GitHub Actions** - CI rules to check all filenames via GenCCC

## References

- [AMPEL360 LC Framework](../AMPEL360_LC_FRAMEWORK.md)
- [ATA iSpec 2200 Documentation Standard](https://www.ataebiz.org/)
- [OPT-IN Framework](../README.md)

## Status

**Current Version**: 1.0  
**Status**: RELEASE  
**Owner**: AMPEL360 / OPT-IN Governance
