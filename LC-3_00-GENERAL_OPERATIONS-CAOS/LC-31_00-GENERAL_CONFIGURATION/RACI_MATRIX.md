# LC-31 Configuration & Change Management — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-31 Configuration & Change Management.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Configuration Management**  | Maintains configuration baselines and controls changes                      |
| **Engineering**               | Evaluates technical impact of changes                                       |
| **Certification**             | Assesses airworthiness impact of changes                                    |
| **MRO**                       | Implements changes in operational fleet                                     |

---

## Artefacts & Roles

### Configuration Baselines

| Artefact                | Responsible (R) | Accountable (A) | Consulted (C)                  | Informed (I) |
|-------------------------|-----------------|-----------------|--------------------------------|--------------|
| Configuration baselines | ConfigMngt      | CE              | Certification, Engineering     | Program      |

**Description:** Formal definition of aircraft configuration at specific points in lifecycle.

---

### ECOs / Change Requests

| Artefact               | Responsible (R) | Accountable (A) | Consulted (C)            | Informed (I)      |
|------------------------|-----------------|-----------------|--------------------------|-------------------|
| ECOs / Change Requests | Engineering     | CE              | Manufacturing, MRO       | Customer Services |

**Description:** Engineering Change Orders documenting modifications to baseline configuration.

---

### Approval Trails

| Artefact        | Responsible (R) | Accountable (A) | Consulted (C)   | Informed (I) |
|-----------------|-----------------|-----------------|-----------------|--------------|
| Approval trails | ConfigMngt      | CE              | Certification   | All          |

**Description:** Complete audit trail of change approvals and implementations.

---

## Information Architecture (IA)

### Folder Structure
```
LC-31_00-GENERAL_CONFIGURATION/
├── RACI_MATRIX.md (this file)
├── README.md
├── Configuration_Baselines/
│   ├── LC-31_00-GENERAL_CONFIG-BASELINE-PROTO_V*R*.pdf
│   ├── LC-31_00-GENERAL_CONFIG-BASELINE-PROD_V*R*.pdf
│   └── LC-31_00-GENERAL_CONFIG-BASELINE-FLEET_V*R*.pdf
├── Change_Requests/
│   ├── ECO_Database.xlsx
│   ├── LC-31_00-GENERAL_ECO-*_V*R*.pdf
│   └── Change_Impact_Assessments/
└── Approval_Documentation/
    ├── LC-31_00-GENERAL_APPROVAL-LOG_V*R*.xlsx
    └── Authority_Approvals/
```

### UTCS Naming Convention
- **Format:** `LC-31_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-31_00-GENERAL_CONFIG-BASELINE-PROD_V5R2.pdf`
- **Example:** `LC-31_2700-FLIGHT-CONTROLS_ECO-12345_V1R0.pdf`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Configuration Management
