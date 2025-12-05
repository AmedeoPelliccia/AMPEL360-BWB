# LC-32 MRO (Maintenance, Repair, Overhaul) — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-32 MRO.

---

## Primary Audiences

| Role                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **MRO Services**          | Provides maintenance, repair, and overhaul services                         |
| **Customer Support**      | Supports operators with technical assistance                                |
| **Reliability**           | Analyzes fleet reliability and recommends improvements                      |
| **Operations**            | End-users performing day-to-day maintenance                                 |

---

## Artefacts & Roles

### Task Cards

| Artefact    | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-------------|-----------------|-----------------|---------------|--------------|
| Task cards  | MRO             | Customer Support| Design        | Ops          |

**Description:** Detailed maintenance task instructions for scheduled and unscheduled maintenance.

---

### Troubleshooting Trees

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| Troubleshooting trees | Customer Support| CE              | Design        | Airlines     |

**Description:** Diagnostic procedures for fault isolation and troubleshooting.

---

### Reliability Data

| Artefact         | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|------------------|-----------------|-----------------|---------------|--------------|
| Reliability data | Reliability     | CE              | MRO           | Authorities  |

**Description:** Fleet reliability statistics, trends, and improvement recommendations.

---

## Information Architecture (IA)

### Folder Structure
```
LC-32_00-GENERAL_MRO/
├── RACI_MATRIX.md (this file)
├── README.md
├── Task_Cards/
│   ├── LC-32_2100-AIR-CONDITIONING_TASK-CARD-ECS_V*R*.pdf
│   ├── LC-32_2700-FLIGHT-CONTROLS_TASK-CARD-FCS_V*R*.pdf
│   └── LC-32_2800-HYDROGEN_TASK-CARD-H2-SYSTEM_V*R*.pdf
├── Troubleshooting/
│   ├── LC-32_00-GENERAL_TROUBLESHOOTING-MASTER_V*R*.pdf
│   ├── Fault_Isolation_Procedures/
│   └── Diagnostic_Tools/
└── Reliability/
    ├── LC-32_00-GENERAL_RELIABILITY-REPORT-MONTHLY_V*R*.pdf
    ├── Fleet_Statistics/
    └── Improvement_Recommendations/
```

### UTCS Naming Convention
- **Format:** <span style="color:#0066cc">`LC-32`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** <span style="color:#0066cc">`LC-32`</span>`_`<span style="color:#cc6600">`2100`</span>`-`<span style="color:#666666">`AIR-CONDITIONING`</span>`_`<span style="color:#009900">`MROPROC-ECS-SENSOR`</span>`_`<span style="color:#990099">`V1R0`</span>`.pdf`
- **Example:** <span style="color:#0066cc">`LC-32`</span>`_`<span style="color:#cc6600">`00`</span>`-`<span style="color:#666666">`GENERAL`</span>`_`<span style="color:#009900">`RELIABILITY-REPORT`</span>`_`<span style="color:#990099">`V1R0`</span>`.pdf`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 MRO Services
