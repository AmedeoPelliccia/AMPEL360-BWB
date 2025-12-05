# LC-23 FAL & Production Planning — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-23 Final Assembly Line & Production Planning.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Industrial Engineering**    | Plans and optimizes FAL layout, takt time, and production flow              |
| **Production Planning**       | Schedules production, manages capacity, and coordinates resources           |
| **Tooling & Process**         | Designs and maintains production tooling and processes                      |
| **Supply Chain**              | Coordinates material flow and supplier deliveries                           |

---

## Artefacts & Roles

### BOM (Bill of Materials)

| Artefact | Responsible (R)  | Accountable (A)     | Consulted (C) | Informed (I) |
|----------|------------------|---------------------|---------------|--------------|
| BOM      | Industrial Eng   | Production Director | Design        | Program      |

**Description:** Complete hierarchical listing of all parts, assemblies, and materials required for aircraft production.

---

### Routings

| Artefact  | Responsible (R)       | Accountable (A)     | Consulted (C) | Informed (I) |
|-----------|-----------------------|---------------------|---------------|--------------|
| Routings  | Manufacturing Process | Production Director | Tooling       | FAL          |

**Description:** Detailed manufacturing process steps, sequence, and work center assignments.

---

### Tooling Plans

| Artefact      | Responsible (R) | Accountable (A)     | Consulted (C)  | Informed (I) |
|---------------|-----------------|---------------------|----------------|--------------|
| Tooling plans | Tooling         | Production Director | Manufacturing  | Safety       |

**Description:** Specifications for jigs, fixtures, and tooling required for production.

---

### FAL Station Documentation

| Artefact                  | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|---------------------------|-----------------|-----------------|---------------|--------------|
| FAL station documentation | FAL             | Industrial Eng  | Safety        | Program      |

**Description:** Work instructions, safety procedures, and quality checkpoints for each FAL station.

---

## Information Architecture (IA)

### Folder Structure
```
LC-23_00-GENERAL_FAL-PRODUCTION/
├── RACI_MATRIX.md (this file)
├── README.md
├── BOM/
│   ├── LC-23_00-GENERAL_BOM-MASTER_V*R*.xlsx
│   ├── LC-23_00-GENERAL_BOM-BY-ATA_V*R*.xlsx
│   └── Part_Specifications/
├── Routings/
│   ├── LC-23_00-GENERAL_ROUTING-MASTER_V*R*.xlsx
│   ├── Station_Process_Sheets/
│   └── Work_Instructions/
├── Tooling/
│   ├── LC-23_00-GENERAL_TOOLING-PLAN_V*R*.pdf
│   ├── Jig_Designs/
│   └── Fixture_Specifications/
└── FAL_Stations/
    ├── LC-23_00-GENERAL_FAL-LAYOUT_V*R*.pdf
    ├── Station_01_Documentation/
    ├── Station_02_Documentation/
    └── [Additional stations...]
```

### UTCS Naming Convention
- **Format:** `LC-23_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-23_00-GENERAL_BOM-MASTER_V1R0.xlsx`
- **Example:** `LC-23_00-GENERAL_FAL-LAYOUT_V2R1.pdf`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Industrial Engineering
