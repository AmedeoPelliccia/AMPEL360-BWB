# UTCS-LC Naming Rules

**Universal Traceability & Configuration System — Lifecycle Naming Convention**

**Document ID:** UTCS-LC-NR-01  
**Version:** 1.0  
**Status:** RELEASE  
**Owner:** AMPEL360 / OPT-IN Governance  
**Date:** December 2025

---

## 1. Purpose

This document defines the comprehensive naming rules for all directories, files, and artefacts within the AMPEL360 lifecycle framework, ensuring:

* **Deterministic Naming:** Machine and human-readable identifiers
* **Lifecycle Traceability:** Clear mapping to LC stages and substages
* **ATA Alignment:** Integration with ATA iSpec 2200 classification
* **Version Control:** Built-in versioning for configuration management
* **Automation-Ready:** Compatible with GenCCC, CAOS, and DPP systems
* **Visual Differentiation:** Color coding to distinguish LC ID from ATA ID components (see [Color Coding Guide](./UTCS_COLOR_CODING_GUIDE.md))

---

## 2. Scope

### Applies To:
- All directories in the lifecycle framework
- All documents, models, code, and data files
- All artefacts in GenCCC, CAOS, and V&V systems
- All Digital Product Passport (DPP) entries

### Does Not Apply To:
- Runtime system identifiers
- Vendor proprietary file names (internal to vendor packages)
- Temporary working files in `/tmp`
- External certification authority reference numbers

---

## 3. Core Naming Format

### 3.1 Complete UTCS-LC Format

```
LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}.{ext}
```

### 3.2 Directory Format (No Version)

For organizational directories (folders), version numbers are omitted:

```
LC-{STAGE}{SUBSTAGE}_{ATAIDX}-{ATADESC}_{FUNC}
```

---

## 4. Component Definitions

### 4.1 LC Stage Codes

| Code | Stage | Description |
|------|-------|-------------|
| **1** | Development | Concept through V&V |
| **2** | Manufacturing | Prototyping through production |
| **3** | Operations | CAOS, MRO, support, circularity |

### 4.2 Substage Codes

#### Development (Stage 1)
| Code | Substage | Description |
|------|----------|-------------|
| **11** | Research & Concept | Initial ideation and trade studies |
| **12** | Safety Analysis | FHA, PSSA, SSA per ARP4761 |
| **13** | Requirements | System and subsystem requirements |
| **14** | Design | CAD, schematics, architecture |
| **15** | Interfaces | ICDs, assemblies, bus architecture |
| **16** | Analysis | CFD, FEM, performance, integration |
| **17** | Verification | Test plans, V&V, certification prep |

#### Manufacturing (Stage 2)
| Code | Substage | Description |
|------|----------|-------------|
| **21** | Prototyping | Prototype builds and manufacturing prep |
| **22** | Test & Certification | Ground/flight test, certification evidence |
| **23** | FAL & Production | Final assembly line and production planning |
| **24** | Supply Chain | Supplier management, industrialization |

#### Operations (Stage 3)
| Code | Substage | Description |
|------|----------|-------------|
| **31** | Configuration | Change management, baselines |
| **32** | MRO | Maintenance, repair, overhaul |
| **33** | Customer Support | IETP, training, service bulletins |
| **34** | Spares & Circularity | PNR, spares, material recovery |

### 4.3 ATA Index (ATAIDX)

The ATAIDX follows ATA iSpec 2200 hierarchical numbering:

- **2 digits:** System level (e.g., `57` = Wings, `28` = Fuel/Hydrogen)
- **4 digits:** Section level (e.g., `5723` = Wing Slats)
- **6 digits:** Subject level (e.g., `572301` = Slat Well Envelope)
- **Special:** `00` = General/Aircraft-level (not specific to one ATA chapter)

**Examples:**
- `00` → General/Aircraft-level
- `27` → Flight Controls
- `2700` → Flight Controls System
- `270010` → Flight Control Computer

### 4.4 ATA Description (ATADESC)

ATADESC is **automatically derived** from ATAIDX using the ATA_MAP.yaml dictionary.

**Generation Rules:**
1. Look up system code (first 2 digits)
2. If 4+ digits, append section description
3. If 6 digits, append subject description
4. Join with underscores
5. Convert to uppercase
6. Replace spaces with hyphens

**Examples:**
- `00` → `GENERAL`
- `27` → `FLIGHT-CONTROLS`
- `2700` → `FLIGHT-CONTROLS-SYSTEM`
- `2800` → `FUEL` (or `HYDROGEN` for novel systems)
- `9500` → `NN-SYSTEMS` (novel AI/NN chapter)

**Novel ATA Chapters:**
- `28H` → `HYDROGEN` (hydrogen-specific subsystems; 'H' suffix distinguishes from conventional fuel systems in ATA 28)
- `80` → `ELECTRIC-PROPULSION` (new chapter for distributed electric propulsion)
- `85` → `GREEN-E-BATTERY` (new chapter for battery energy storage systems)
- `95` → `NN-SYSTEMS` (new chapter for AI/Neural Network systems)

### 4.5 Functional Descriptor (FUNC)

Short code indicating artefact purpose or type.

**Rules:**
- 3-20 characters
- Uppercase letters, numbers, hyphens
- No spaces or special characters
- Must be descriptive and consistent

**Common FUNC Codes:**

| FUNC | Description |
|------|-------------|
| **CONCEPT** | Conceptual design document |
| **TRADE-STUDY** | Trade study analysis |
| **FHA** | Functional Hazard Assessment |
| **PSSA** | Preliminary System Safety Assessment |
| **SSA** | System Safety Assessment |
| **SRD** | System Requirements Document |
| **CAD** | CAD model or drawing |
| **SCHEMATIC** | Electrical or system schematic |
| **ICD** | Interface Control Document |
| **CFD** | Computational Fluid Dynamics analysis |
| **FEM** | Finite Element Model |
| **NNMODEL** | Neural Network model |
| **TEST-PLAN** | Verification test plan |
| **VNVREP** | Verification and Validation Report |
| **CERT-EVIDENCE** | Certification evidence package |
| **PROTOTYPE** | Prototype build documentation |
| **TEST-REPORT** | Test campaign report |
| **FAL-PLAN** | Final Assembly Line plan |
| **BOM** | Bill of Materials |
| **CONFIG-BASELINE** | Configuration baseline |
| **MROPROC** | MRO procedure |
| **IETP** | Interactive Electronic Technical Publication |
| **SERVICE-BULLETIN** | Service bulletin |
| **DPP** | Digital Product Passport |

### 4.6 Version (V) and Revision (R)

**Format:** `V{x}R{y}`

- **Version (x):** Major baseline changes (breaking changes, major redesign)
- **Revision (y):** Minor updates (corrections, clarifications, non-breaking changes)

**Rules:**
- Both x and y are integers starting from 0
- First release is `V1R0` (not V0R0)
- Revisions increment: V1R0 → V1R1 → V1R2 ...
- Versions increment: V1Ry → V2R0

**Examples:**
- `V1R0` → First release
- `V1R3` → Third revision of first version
- `V2R0` → Second major version
- `V2R1` → First revision of second version

### 4.7 File Extension (.ext)

Standard file extensions based on artefact type:

| Extension | Type |
|-----------|------|
| `.md` | Markdown documentation |
| `.md` | PDF documents |
| `.docx` | Word documents |
| `.csv` | Excel spreadsheets |
| `.catpart` | CATIA part file |
| `.catproduct` | CATIA assembly |
| `.sldprt` | SolidWorks part |
| `.sldasm` | SolidWorks assembly |
| `.nas` | Nastran FEM file |
| `.dat` | CFD data file |
| `.slx` | Simulink model |
| `.py` | Python script |
| `.json` | JSON data |
| `.yaml` | YAML configuration |
| `.xml` | XML data (IETP, S1000D) |

---

## 5. Naming Examples

**Color Coding:** See [UTCS Color Coding Guide](./UTCS_COLOR_CODING_GUIDE.md) for visual differentiation between components:
- <span style="color:#0066cc">LC ID (Blue)</span>
- <span style="color:#cc6600">ATA ID (Orange)</span>
- <span style="color:#666666">ATA DESC (Gray)</span>
- <span style="color:#009900">FUNC (Green)</span>
- <span style="color:#990099">Version (Purple)</span>

### 5.1 Development Stage Examples

```
# Concept-level trade study
LC-11_ATA-0000-GENERAL_TRADE-STUDY-BWB-CONFIG_V1R0.md
```
<span style="color:#0066cc">**LC-11**</span>_<span style="color:#cc6600">**ATA-0000**</span>-<span style="color:#666666">**GENERAL**</span>_<span style="color:#009900">**TRADE-STUDY-BWB-CONFIG**</span>_<span style="color:#990099">**V1R0**</span>.md

```
# Safety analysis for flight controls
LC-12_27-FLIGHT-CONTROLS_FHA-FCS_V1R0.md
LC-12_27-FLIGHT-CONTROLS_PSSA-FCS_V1R1.md

# System requirements document
LC-13_00-GENERAL_SRD-AIRCRAFT-LEVEL_V2R0.md
LC-13_2800-HYDROGEN_SUBSYS-REQUIREMENTS_V1R0.md

# CAD model for hydrogen tank
LC-14_2800-HYDROGEN_CAD-TANK-ASSY_V3R2.catproduct

# Interface control document for AFDX
LC-15_42-IMA_ICD-AFDX-NETWORK_V1R0.md

# CFD analysis for wing
LC-16_5700-WINGS_CFD-CRUISE_V2R1.dat

# Verification test plan for NN systems
LC-17_9500-NN-SYSTEMS_TEST-PLAN-NN-FCS_V1R0.md
```

### 5.2 Manufacturing Stage Examples

```
# Prototype build instructions
LC-21_5700-WINGS_PROTOTYPE-BUILD-INSTR_V1R0.md

# Flight test report
LC-22_00-GENERAL_FLIGHT-TEST-REPORT_V1R0.md

# Final assembly line plan
LC-23_00-GENERAL_FAL-PLAN-STATION-3_V2R0.md

# Supplier technical package
LC-24_8000-ELECTRIC-PROPULSION_SUPPLIER-PKG-MOTOR_V1R0.md
```

### 5.3 Operations Stage Examples

```
# Configuration baseline
LC-31_00-GENERAL_CONFIG-BASELINE-AC001_V5R2.md

# MRO procedure
LC-32_2100-AIR-CONDITIONING_MROPROC-ECS-SENSOR_V1R0.md

# IETP module
LC-33_2700-FLIGHT-CONTROLS_IETP-FCS-MAINTENANCE_V1R0.xml

# Digital Product Passport
LC-34_8500-GREEN-E-BATTERY_DPP-BATTERY-PACK-001_V1R0.json
```

### 5.4 Directory Structure Examples

```
# Top-level LC directories (no version)
LC-1_00-GENERAL_DEVELOPMENT/
LC-2_00-GENERAL_MANUFACTURING/
LC-3_00-GENERAL_OPERATIONS-CAOS/

# Substage directories (no version)
LC-1_00-GENERAL_DEVELOPMENT/
├── LC-11_ATA-00-GENERAL_RESEARCH-CONCEPT/
├── LC-12_00-GENERAL_SAFETY-ANALYSIS/
├── LC-13_00-GENERAL_REQUIREMENTS/
├── LC-14_00-GENERAL_DESIGN/
├── LC-15_00-GENERAL_INTERFACES/
├── LC-16_00-GENERAL_ANALYSIS/
└── LC-17_00-GENERAL_VERIFICATION/

# ATA-specific subdirectories (no version)
LC-14_00-GENERAL_DESIGN/
├── LC-14_2700-FLIGHT-CONTROLS_CAD/
├── LC-14_2800-HYDROGEN_CAD/
├── LC-14_8000-ELECTRIC-PROPULSION_CAD/
└── LC-14_9500-NN-SYSTEMS_CAD/
```

---

## 6. Formal Rules

### Rule 1: Mandatory Format
All AMPEL360 artefacts **MUST** use the UTCS-LC format.

### Rule 2: No Spaces
File and directory names **MUST NOT** contain spaces. Use hyphens instead.

### Rule 3: Uppercase Descriptors
ATADESC and FUNC **MUST** be uppercase.

### Rule 4: Delimiter Usage
- Underscore `_` separates major components
- Hyphen `-` used within components and to separate ATAIDX from ATADESC

### Rule 5: Version Required for Files
All files **MUST** include version suffix `V{x}R{y}`.

### Rule 6: No Version for Directories
Directories **MUST NOT** include version suffix.

### Rule 7: ATA Derivation
ATADESC **MUST** be automatically derived from ATAIDX using ATA_MAP.yaml.

### Rule 8: Uniqueness
No two artefacts may share the same UTCS-LC identifier.

### Rule 9: Immutability
Once assigned, the base UTCS-LC ID (excluding version) cannot change.

### Rule 10: Character Length
Recommended maximum 200 characters for complete file name including extension.

---

## 7. Validation & Tools

### 7.1 UTCS Parser
The `ata_resolver.py` tool validates and generates UTCS-LC identifiers:

```bash
python3 utcs/ata_resolver.py --ataidx 2700 --func TEST-PLAN --stage 17
# Output: LC-17_2700-FLIGHT-CONTROLS-SYSTEM_TEST-PLAN
```

### 7.2 GenCCC Validation
GenCCC automatically validates all artefact names against UTCS-LC rules during CI/CD.

### 7.3 CAOS Integration
CAOS parses UTCS-LC identifiers to:
- Extract lifecycle stage and ATA classification
- Build traceability graphs
- Support DPP lineage tracking

---

## 8. Best Practices

### 8.1 Naming Consistency
- Use consistent FUNC codes across similar artefacts
- Follow established patterns in existing directories
- Consult ATA_MAP.yaml for correct ATADESC

### 8.2 Version Management
- Increment revisions for minor updates
- Increment versions for major baseline changes
- Document version history in artefact metadata

### 8.3 Directory Organization
- Group artefacts by substage, then by ATA chapter
- Use README.md in each directory to explain contents
- Include RACI_MATRIX.md to define roles and responsibilities

### 8.4 Novel Systems
- For novel ATA chapters (28H, 80, 85, 95), ensure ATA_MAP.yaml is updated
- Coordinate with Systems Engineering for new FUNC codes
- Update this document with new examples as needed

---

## 9. Exceptions & Special Cases

### 9.1 Multi-ATA Artefacts
For artefacts spanning multiple ATA chapters, use:
- `00-GENERAL` for aircraft-level
- Primary ATA if one system is dominant
- Create multiple artefact versions if needed

### 9.2 Legacy Files
Legacy files being migrated:
1. Rename to UTCS-LC format
2. Update all references
3. Document old name in metadata
4. Use revision 0 to indicate migration

### 9.3 External Vendor Files
Vendor-supplied files:
- Place in vendor-specific subdirectory
- Create UTCS-LC wrapper document referencing vendor file
- Maintain vendor's original file name internally

---

## 10. Compliance & Enforcement

### Required For:
- All release documentation
- All certification artefacts
- All safety-critical components (DAL A-C)
- All NN system deliverables (ATA 95)
- All DPP entries

### Enforced By:
- GenCCC CI/CD pipeline
- Pre-commit hooks
- Code review checklist
- Configuration management audits

### Waiver Process:
Exceptions require:
1. Written justification
2. Chief Engineer approval
3. Documentation in exception log
4. Review at next CAB meeting

---

## 11. References

1. [UTCS-ID Specification v1.0](./UTCS-ID_Specification_v1.0.md)
2. [ATA iSpec 2200](./ATA_MAP.yaml) — ATA chapter definitions
3. [AMPEL360 LC Framework](../AMPEL360_LC_FRAMEWORK.md)
4. GenCCC Standard — Cross-Contextual Consistency Engine
5. CAOS Specification — Computer Aided Operations & Services
6. Digital Product Passport (DPP) Standard

---

## 12. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| V1R0 | 2025-12-05 | AMPEL360 | Initial release with complete UTCS-LC rules |

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Systems Engineering & Configuration Management
