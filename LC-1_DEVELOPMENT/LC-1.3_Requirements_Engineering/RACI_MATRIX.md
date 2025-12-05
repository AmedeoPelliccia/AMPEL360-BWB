# LC-1.3 Requirements Engineering — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-1.3 Requirements Engineering.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Systems Engineering**       | Leads requirements definition, allocation, and traceability                 |
| **MBSE Team**                 | Maintains model-based requirements and architecture models                  |
| **V&V & Certification**       | Ensures requirements are verifiable and certification-compliant             |
| **Architecture Board**        | Reviews and approves system-level requirements                              |

---

## Artefacts & Roles

### SRD (System Requirements Document)

| Artefact                           | Responsible (R) | Accountable (A) | Consulted (C)         | Informed (I) |
|------------------------------------|-----------------|-----------------|------------------------|--------------|
| SRD (System Requirements Document) | SysEng          | CE              | Architecture, Safety   | All systems  |

**Description:** Comprehensive specification of all system-level requirements for the AMPEL360 BWB aircraft.

**Key Activities:**
- Define functional requirements
- Define performance requirements
- Define interface requirements
- Define environmental requirements
- Define safety requirements (from LC-1.2)
- Define certification requirements

---

### Subsystem Requirements

| Artefact                | Responsible (R)      | Accountable (A) | Consulted (C) | Informed (I) |
|-------------------------|----------------------|-----------------|---------------|--------------|
| Subsystem requirements  | SysEng Subdomain     | CE              | Owners        | V&V          |

**Description:** Detailed requirements allocated to each subsystem and ATA chapter.

**Key Activities:**
- Allocate aircraft requirements to subsystems
- Define subsystem functional requirements
- Define subsystem interface requirements
- Ensure completeness and consistency
- Validate against safety requirements

---

### ICD Requirements Section

| Artefact                | Responsible (R) | Accountable (A) | Consulted (C)                | Informed (I) |
|-------------------------|-----------------|-----------------|------------------------------|--------------|
| ICD requirement section | SysEng          | CE              | Interfaces / Architecture    | All          |

**Description:** Requirements specifically related to interfaces between systems, assemblies, and external entities.

**Key Activities:**
- Define mechanical interface requirements
- Define electrical interface requirements
- Define data interface requirements (AFDX, A429, CAN, NN-bus)
- Define software interface requirements
- Coordinate with LC-1.5 ICD development

---

### Traceability Matrix

| Artefact             | Responsible (R) | Accountable (A) | Consulted (C)                 | Informed (I) |
|----------------------|-----------------|-----------------|-------------------------------|--------------|
| Traceability matrix  | SysEng          | V&V             | Certification, Safety         | Program      |

**Description:** Complete mapping of requirements to design, verification, and certification evidence.

**Key Activities:**
- Map stakeholder needs to requirements
- Map requirements to design elements
- Map requirements to verification methods
- Map requirements to certification basis
- Maintain bidirectional traceability

---

## Information Architecture (IA)

### Folder Structure
```
LC-1.3_Requirements_Engineering/
├── RACI_MATRIX.md (this file)
├── README.md
├── SRD_System_Requirements_Document/
│   ├── AMPEL360_SRD_V*.pdf
│   ├── Functional_Requirements/
│   ├── Performance_Requirements/
│   ├── Interface_Requirements/
│   └── Safety_Requirements/
├── Subsystem_Requirements/
│   ├── ATA_21_Air_Conditioning_Requirements_V*.pdf
│   ├── ATA_22_Autoflight_Requirements_V*.pdf
│   ├── ATA_27_Flight_Controls_Requirements_V*.pdf
│   ├── ATA_28H_Hydrogen_System_Requirements_V*.pdf
│   ├── ATA_80_Electric_Propulsion_Requirements_V*.pdf
│   ├── ATA_85_Green_E_Battery_Requirements_V*.pdf
│   ├── ATA_95_NN_Systems_Requirements_V*.pdf
│   └── [Other ATA chapters...]
├── ICD_Interface_Requirements/
│   ├── Mechanical_Interface_Requirements_V*.pdf
│   ├── Electrical_Interface_Requirements_V*.pdf
│   ├── Data_Interface_Requirements_V*.pdf
│   └── Software_Interface_Requirements_V*.pdf
└── Traceability/
    ├── Requirements_Traceability_Matrix.xlsx
    ├── Verification_Matrix.xlsx
    ├── Certification_Traceability.xlsx
    └── GenCCC_Traceability_Reports/
```

### UTCS Naming Convention
- **Format:** `LC-1.3_{ATA-IDX}-{ATA-DESC}_{FUNCTION}_V{x}R{y}`
- **Example:** `LC-1.3_00-GENERAL_SRD-AIRCRAFT-LEVEL_V1R0.pdf`
- **Example:** `LC-1.3_28H-HYDROGEN_SUBSYS-REQUIREMENTS_V2R1.pdf`
- **Example:** `LC-1.3_95-NN-SYSTEMS_NN-FCS-REQUIREMENTS_V1R0.pdf`

---

## Governance & Approval

### Review Cycles
- **Weekly:** Systems engineering reviews requirement updates
- **Bi-weekly:** CAB reviews system-level requirements changes
- **Monthly:** V&V reviews verification and traceability status
- **Milestone:** CE approves requirements baseline freeze

### Decision Authority
- **Chief Engineer:** Final approval of system requirements baseline
- **Systems Engineering:** Day-to-day requirements management
- **CAB:** Approval of requirements changes after baseline

### Traceability
- All requirements uniquely identified in UTCS format
- GenCCC automatically validates traceability and completeness
- CGen generates consistent requirements documents
- MBSE models synchronized with requirements database

---

## Integration Points

### Upstream (Inputs)
- **LC-1.1:** Concept-level requirements and constraints
- **LC-1.2:** Safety-derived requirements
- **Market Requirements:** Customer and operational needs
- **Certification Basis:** CS-25, FAR Part 25, DO-178C, DO-254

### Downstream (Outputs)
- **LC-1.4 Detailed Design:** Requirements guide design decisions
- **LC-1.5 Interfaces:** Interface requirements define ICDs
- **LC-1.6 Analysis:** Requirements validate analysis models
- **LC-1.7 V&V:** Requirements define verification criteria
- **LC-2.2 Certification:** Requirements form certification basis

### Lateral (Parallel)
- **MBSE:** Requirements models and SysML architecture
- **GenCCC:** Automated requirements validation
- **UTCS:** Requirements identity and version management

---

## Requirements Engineering Best Practices

### Requirement Quality Attributes
1. **Complete:** All necessary information provided
2. **Consistent:** No conflicts with other requirements
3. **Unambiguous:** Single interpretation possible
4. **Verifiable:** Can be verified by inspection, analysis, demonstration, or test
5. **Traceable:** Linked to source and downstream artefacts
6. **Feasible:** Technically and economically achievable
7. **Necessary:** Aligned with mission and safety needs

### Requirements Types
- **Functional:** What the system shall do
- **Performance:** How well the system shall perform
- **Interface:** How the system shall interact
- **Environmental:** Conditions the system shall withstand
- **Safety:** Hazard mitigation and reliability targets
- **Certification:** Regulatory compliance mandates

---

## Key Principles

1. **Requirements-Driven Development:** All design decisions traced to requirements
2. **Bidirectional Traceability:** Complete chain from needs to verification
3. **Configuration Management:** Rigorous control of requirements baseline
4. **MBSE Integration:** Model-based requirements for consistency
5. **Verification Focus:** All requirements must be verifiable

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Systems Engineering
