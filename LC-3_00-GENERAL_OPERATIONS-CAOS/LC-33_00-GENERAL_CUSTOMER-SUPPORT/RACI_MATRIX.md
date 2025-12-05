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
│   ├── LC-33_00-GENERAL_SB-*_V*R*.md
│   └── SB_Index/
└── Fleet_Reports/
    ├── LC-33_00-GENERAL_FLEET-REPORT-MONTHLY_V*R*.md
    └── Operational_Statistics/
```

### UTCS Naming Convention
- **Format:** <span style="color:#0066cc">`LC-33`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** <span style="color:#0066cc">`LC-33`</span>`_`<span style="color:#cc6600">`2700`</span>`-`<span style="color:#666666">`FLIGHT-CONTROLS`</span>`_`<span style="color:#009900">`IETP-FCS-MAINTENANCE`</span>`_`<span style="color:#990099">`V1R0`</span>`.xml`
- **Example:** `LC-33_00-GENERAL_SB-2025-001_V1R0.md`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Customer Support
