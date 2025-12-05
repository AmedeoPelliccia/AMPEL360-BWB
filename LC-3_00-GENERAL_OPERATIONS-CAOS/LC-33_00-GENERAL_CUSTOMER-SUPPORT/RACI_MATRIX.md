# LC-33 Customer Care & Support Services — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-33 Customer Care & Support Services.

---

## Primary Audiences

| Role                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **IETP Team**             | Develops and maintains Interactive Electronic Technical Publications        |
| **Training**              | Provides operator and maintainer training programs                          |
| **Operations Support**    | Provides technical support to airline operations                            |
| **Customer Engineering**  | Liaison between customers and engineering                                   |

---

## Artefacts & Roles

### IETP Content (S1000D)

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| IETP content (S1000D) | Tech Pubs       | Customer Support| Engineering   | Operators    |

**Description:** Interactive technical documentation compliant with S1000D standard.

---

### Service Bulletins

| Artefact          | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-------------------|-----------------|-----------------|---------------|--------------|
| Service Bulletins | Customer Support| CE              | Safety        | Authorities  |

**Description:** Service bulletins communicating important technical information and modifications.

---

### Fleet Service Reports

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| Fleet service reports | Support         | CE              | Ops           | Program      |

**Description:** Regular reports on fleet operational status and technical issues.

---

## Information Architecture (IA)

### Folder Structure
```
LC-33_00-GENERAL_CUSTOMER-SUPPORT/
├── RACI_MATRIX.md (this file)
├── README.md
├── IETP/
│   ├── LC-33_00-GENERAL_IETP-MASTER-INDEX_V*R*.xml
│   ├── LC-33_2700-FLIGHT-CONTROLS_IETP-FCS-MAINT_V*R*.xml
│   └── S1000D_Data_Modules/
├── Service_Bulletins/
│   ├── LC-33_00-GENERAL_SB-*_V*R*.pdf
│   └── SB_Index/
└── Fleet_Reports/
    ├── LC-33_00-GENERAL_FLEET-REPORT-MONTHLY_V*R*.pdf
    └── Operational_Statistics/
```

### UTCS Naming Convention
- **Format:** `LC-33_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-33_2700-FLIGHT-CONTROLS_IETP-FCS-MAINTENANCE_V1R0.xml`
- **Example:** `LC-33_00-GENERAL_SB-2025-001_V1R0.pdf`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Customer Support
