# LC-34 PNR, Spares & Circular Material Economy — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-34 PNR, Spares & Circularity.

---

## Primary Audiences

| Role                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Spares Logistics**        | Manages spare parts inventory and distribution                              |
| **Material Circularity**    | Implements circular economy and material recovery programs                  |
| **Cost Engineering**        | Analyzes lifecycle costs and optimization opportunities                     |
| **Operators**               | End-users consuming spare parts and services                                |

---

## Artefacts & Roles

### Spare Parts Catalogue

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| Spare parts catalogue | Spares          | Customer Support| Engineering   | Operators    |

**Description:** Comprehensive catalogue of spare parts with part numbers, descriptions, and ordering information.

---

### Circularity Loops

| Artefact          | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I)  |
|-------------------|-----------------|-----------------|----------------|---------------|
| Circularity loops | Circularity Eng | CE              | Manufacturing  | Certification |

**Description:** Material recovery, recycling, and second-life programs for aircraft components.

---

### Tracking / DPP (Digital Product Passport)

| Artefact        | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I) |
|-----------------|-----------------|-----------------|----------------|--------------|
| Tracking / DPP  | Circularity Eng | Program         | Supply chain   | Authorities  |

**Description:** Digital Product Passports tracking material provenance, lifecycle, and circularity.

---

## Information Architecture (IA)

### Folder Structure
```
LC-34_00-GENERAL_SPARES-CIRCULARITY/
├── RACI_MATRIX.md (this file)
├── README.md
├── Spares_Catalogue/
│   ├── LC-34_00-GENERAL_SPARES-CATALOGUE-MASTER_V*R*.xlsx
│   ├── Part_Number_Registry/
│   └── Provisioning_Data/
├── Circularity/
│   ├── LC-34_00-GENERAL_CIRCULARITY-PROGRAM_V*R*.pdf
│   ├── Material_Recovery_Procedures/
│   ├── Battery_Second_Life/
│   └── Recycling_Programs/
└── Digital_Product_Passports/
    ├── LC-34_8500-GREEN-E-BATTERY_DPP-PACK-001_V*R*.json
    ├── LC-34_5700-WINGS_DPP-COMPOSITE-PANEL-001_V*R*.json
    └── DPP_Tracking_Database/
```

### UTCS Naming Convention
- **Format:** `LC-34_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-34_00-GENERAL_SPARES-CATALOGUE-MASTER_V1R0.xlsx`
- **Example:** `LC-34_8500-GREEN-E-BATTERY_DPP-BATTERY-PACK-001_V1R0.json`
- **Example:** `LC-34_00-GENERAL_CIRCULARITY-PROGRAM_V1R0.pdf`

---

## Novel Circularity Considerations

### Green-E Battery (ATA 85)
- Battery state-of-health monitoring
- Second-life applications (grid storage)
- Recycling and material recovery
- DPP tracking throughout lifecycle

### Hydrogen Systems (ATA 28H)
- Tank recertification and lifecycle extension
- Material recovery from cryogenic systems
- CO₂ capture and utilization

### Composite Structures
- Composite recycling technologies
- Carbon fiber recovery and reuse
- End-of-life disassembly procedures

---

## Key Principles

1. **Circular by Design:** Circularity considered from design phase
2. **Traceability:** Complete material provenance via DPP
3. **Sustainability:** Maximize material recovery and reuse
4. **Value Retention:** Extend component life and extract maximum value
5. **Regulatory Compliance:** Align with EU DPP and sustainability regulations

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Circularity & Spares Management
