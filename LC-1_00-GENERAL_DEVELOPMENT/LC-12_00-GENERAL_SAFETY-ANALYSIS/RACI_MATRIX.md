# LC-1.2 Safety Analysis (ARP4761) — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-1.2 Safety Analysis.

---

## Primary Audiences

| Role                              | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| **Systems Safety Office**         | Leads all safety analysis activities and maintains hazard logs              |
| **Certification Authorities**     | EASA, FAA, or other regulatory bodies reviewing safety case                 |
| **System Owners**                 | Domain leads responsible for their systems' safety compliance               |
| **Risk & Compliance**             | Oversees risk management and regulatory compliance activities               |

---

## Artefacts & Roles

### FHA (Functional Hazard Assessment)

| Artefact                            | Responsible (R) | Accountable (A) | Consulted (C)     | Informed (I)    |
|-------------------------------------|-----------------|-----------------|-------------------|-----------------|
| FHA (Functional Hazard Assessment)  | Safety          | CE/CAB          | Systems Leads     | Certification   |

**Description:** Identifies and classifies failure conditions and their effects at the aircraft and system functional level.

**Key Activities:**
- Identify aircraft-level and system-level functions
- Determine failure conditions and effects
- Classify severity (Catastrophic, Hazardous, Major, Minor, No Safety Effect)
- Assign qualitative probability targets
- Define safety objectives

---

### PSSA (Preliminary System Safety Assessment)

| Artefact                                    | Responsible (R) | Accountable (A) | Consulted (C)            | Informed (I) |
|---------------------------------------------|-----------------|-----------------|--------------------------|--------------|
| PSSA (Preliminary System Safety Assessment) | Safety          | CE/CAB          | Systems, Architecture    | Program      |

**Description:** Architecture-level safety analysis validating that the preliminary design can meet safety objectives.

**Key Activities:**
- Evaluate preliminary architecture against FHA requirements
- Allocate safety requirements to systems
- Common cause analysis (CCA)
- Zonal Safety Analysis (ZSA)
- Particular Risk Analysis (PRA)

---

### SSA (System Safety Assessment)

| Artefact                       | Responsible (R) | Accountable (A) | Consulted (C)   | Informed (I) |
|--------------------------------|-----------------|-----------------|-----------------|--------------|
| SSA (System Safety Assessment) | Safety          | Authorities     | Systems & V&V   | Program      |

**Description:** Final safety validation demonstrating compliance with all safety requirements and objectives.

**Key Activities:**
- Validate design implementation meets safety objectives
- Review test evidence and V&V results
- Confirm DAL compliance (DO-178C, DO-254)
- Final hazard log closure
- Certification package preparation

---

### DAL Allocation Matrix

| Artefact              | Responsible (R)  | Accountable (A) | Consulted (C)   | Informed (I)       |
|-----------------------|------------------|-----------------|-----------------|---------------------|
| DAL Allocation matrix | Systems + Safety | CE              | Certification   | All engineering     |

**Description:** Development Assurance Level (DAL) assignment for software and hardware components per DO-178C/DO-254.

**Key Activities:**
- Assign DAL (Level A through E) based on failure condition severity
- Define independence and partitioning requirements
- Document rationale and traceability
- Review with certification authorities

---

## Information Architecture (IA)

### Folder Structure
```
LC-1.2_Safety_Analysis_ARP4761/
├── RACI_MATRIX.md (this file)
├── README.md
├── FHA_Functional_Hazard_Assessment/
│   ├── Aircraft_Level_FHA_V*.pdf
│   ├── System_Level_FHA_*.pdf
│   └── Failure_Conditions_Database.xlsx
├── PSSA_Preliminary_System_Safety_Assessment/
│   ├── PSSA_Report_V*.pdf
│   ├── FTA_Fault_Trees/
│   ├── FMEA_Analysis/
│   └── Common_Cause_Analysis/
├── SSA_System_Safety_Assessment/
│   ├── SSA_Report_V*.pdf
│   ├── Safety_Validation_Evidence/
│   └── Certification_Evidence_Package/
├── DAL_Allocation/
│   ├── DAL_Matrix_V*.xlsx
│   ├── Software_DAL_Assignment_*.pdf
│   └── Hardware_DAL_Assignment_*.pdf
└── Hazard_Logs/
    ├── Master_Hazard_Log.xlsx
    └── Hazard_Status_Reports/
```

### UTCS Naming Convention
- **Format:** `LC-1.2_{ATA-IDX}-{ATA-DESC}_{FUNCTION}_V{x}R{y}`
- **Example:** `LC-1.2_00-GENERAL_FHA-AIRCRAFT-LEVEL_V1R0.pdf`
- **Example:** `LC-1.2_22-AUTOFLIGHT_PSSA-FCS-SAFETY_V2R1.pdf`
- **Example:** `LC-1.2_95-NN-SYSTEMS_DAL-MATRIX-NN-FCS_V1R0.xlsx`

---

## Governance & Approval

### Review Cycles
- **Bi-weekly:** Safety team reviews hazard log status
- **Monthly:** CAB reviews safety analysis progress
- **Milestone:** CE and Authorities approve major safety deliverables (FHA, PSSA, SSA)

### Decision Authority
- **Chief Engineer:** Approves safety requirements and architectures
- **Certification Authorities:** Final acceptance of safety case
- **Safety Office:** Day-to-day safety analysis execution

### Traceability
- Hazards tracked in UTCS with unique IDs
- Safety requirements traced to design elements
- GenCCC validates safety requirement coverage
- CGen generates consistent safety documentation

---

## Integration Points

### Upstream (Inputs)
- **LC-1.1:** Concept-level hazard identification
- **Market Requirements:** Operational safety expectations
- **Regulatory:** CS-25, FAR Part 25 safety requirements

### Downstream (Outputs)
- **LC-1.3 Requirements Engineering:** Safety-derived requirements
- **LC-1.4 Detailed Design:** Safety constraints on architecture
- **LC-1.7 V&V:** Safety test requirements and evidence collection
- **LC-2.2 Certification:** Safety case and compliance demonstration

### Lateral (Parallel)
- **MBSE:** Safety models and architectures
- **OPT-IN (N axis):** AI/NN safety assurance
- **GenCCC:** Automated safety requirement validation

---

## Hydrogen-Electric & AI/NN Specific Safety

### Novel Safety Considerations
1. **Hydrogen Systems (ATA 28H):**
   - Cryogenic hazards (cold burns, embrittlement)
   - Leak detection and containment
   - Fire and explosion risks
   - Ventilation and purging requirements

2. **Electric Propulsion (ATA 80):**
   - High-voltage electrical safety
   - Battery thermal runaway (Green-E)
   - Motor failure modes and effects
   - Power distribution redundancy

3. **AI/NN Systems (ATA 95):**
   - NN-FCS (Flight Control) safety assurance
   - NN-ECS (Environmental Control) reliability
   - NN-IMA (Integrated Modular Avionics) partitioning
   - Learning and adaptation safety boundaries

4. **BWB Configuration:**
   - Novel evacuation requirements
   - Structural integrity of blended surfaces
   - Center-of-gravity management
   - Maintenance access safety

---

## Key Principles

1. **Safety First:** No compromise on safety for performance or cost
2. **Compliance-Ready:** All analysis aligned with ARP4761 and regulatory standards
3. **Traceability:** Complete chain from hazard to mitigation to verification
4. **Continuous Improvement:** Hazard log updated throughout development lifecycle
5. **Independence:** Safety analysis independent from design and V&V execution

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Systems Safety Office
