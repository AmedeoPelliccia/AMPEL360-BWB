# LC-1.4 Design Engineering — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-1.4 Design Engineering.

---

## Primary Audiences

| Role                              | Description                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------|
| **System Owners**                 | Domain leads responsible for their systems' design                          |
| **Mechanical/Structural Design**  | Leads airframe, structures, and mechanical systems design                   |
| **Electrical/Avionics**           | Leads electrical systems, avionics, and power distribution design           |
| **Propulsion/Energy**             | Leads hydrogen, electric propulsion, and energy systems design              |
| **ATA Domain Leads**              | Chapter-level design authority per ATA specification                        |

---

## Artefacts & Roles

### Preliminary Design

| Artefact            | Responsible (R) | Accountable (A) | Consulted (C)    | Informed (I) |
|---------------------|-----------------|-----------------|------------------|--------------|
| Preliminary design  | Domain Owner    | Chief Engineer  | SysEng, Safety   | Program      |

**Description:** Initial design concepts and layouts for all aircraft systems and structures.

**Key Activities:**
- Define system architecture and topology
- Establish preliminary sizing and layout
- Identify critical design drivers
- Validate against requirements (LC-1.3)
- Coordinate with safety analysis (LC-1.2)

---

### Detailed CAD Models

| Artefact             | Responsible (R) | Accountable (A) | Consulted (C)    | Informed (I) |
|----------------------|-----------------|-----------------|------------------|--------------|
| Detailed CAD models  | Design Office   | Domain Lead     | Manufacturing    | All          |

**Description:** 3D parametric models of all aircraft components, assemblies, and systems.

**Key Activities:**
- Create master geometry (Catia, NX, SolidWorks)
- Maintain design baselines and configurations
- Generate assembly models and exploded views
- Coordinate with manufacturing for DFM (Design for Manufacturing)
- Generate 2D engineering drawings

---

### Design Schematics

| Artefact          | Responsible (R) | Accountable (A) | Consulted (C)        | Informed (I) |
|-------------------|-----------------|-----------------|----------------------|--------------|
| Design Schematics | Design Office   | Domain Lead     | Avionics/Systems     | V&V          |

**Description:** Electrical schematics, hydraulic diagrams, control logic, and system diagrams.

**Key Activities:**
- Electrical wiring diagrams (EWIS)
- Hydraulic and pneumatic schematics
- Control system logic diagrams
- Data bus architectures (AFDX, A429, CAN, NN-bus)
- Software architecture diagrams

---

### ATA-Mapped Design Documents

| Artefact                     | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|------------------------------|-----------------|-----------------|---------------|--------------|
| ATA-mapped design documents  | Domain Owner    | ATA Lead        | SysEng        | CAB          |

**Description:** Design documentation organized by ATA chapter for consistency with industry standards.

**Key Activities:**
- Organize design per ATA 100 specification
- Cross-reference with iSpec 2200
- Maintain ATA-level design baselines
- Support certification by ATA chapter

---

## Information Architecture (IA)

### Folder Structure
```
LC-1.4_Detailed_Design/
├── RACI_MATRIX.md (this file)
├── README.md
├── Preliminary_Design/
│   ├── System_Architecture_Diagrams/
│   ├── Concept_Layouts/
│   └── Sizing_Studies/
├── CAD_Models/
│   ├── Master_Geometry/
│   │   ├── BWB_Fuselage_V*.catpart
│   │   ├── Wing_Assembly_V*.catproduct
│   │   └── [Other major assemblies...]
│   ├── Subsystems_by_ATA/
│   │   ├── ATA_21_Air_Conditioning/
│   │   ├── ATA_27_Flight_Controls/
│   │   ├── ATA_28H_Hydrogen_System/
│   │   ├── ATA_80_Electric_Propulsion/
│   │   ├── ATA_85_Green_E_Battery/
│   │   ├── ATA_95_NN_Systems/
│   │   └── [Other ATA chapters...]
│   └── 2D_Drawings/
├── Schematics/
│   ├── Electrical_Diagrams/
│   ├── Hydraulic_Pneumatic_Diagrams/
│   ├── Control_Logic_Diagrams/
│   └── Data_Bus_Architecture/
└── ATA_Design_Documentation/
    ├── ATA_21_Design_Description_V*.pdf
    ├── ATA_27_Design_Description_V*.pdf
    ├── ATA_28H_Design_Description_V*.pdf
    └── [Other ATA chapters...]
```

### UTCS Naming Convention
- **Format:** `LC-14_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-14_27-FLIGHT-CONTROLS_PRELIM-DESIGN_V1R0.pdf`
- **Example:** `LC-14_28H-HYDROGEN_CAD-TANK-ASSY_V2R1.catproduct`
- **Example:** `LC-14_95-NN-SYSTEMS_SCHEMATIC-NN-FCS_V1R0.pdf`

---

## Governance & Approval

### Review Cycles
- **Weekly:** Design reviews within each domain team
- **Bi-weekly:** Cross-functional design coordination meetings
- **Monthly:** CAB reviews major design decisions
- **Milestone:** CE approves design baselines (PDR, CDR)

### Decision Authority
- **Chief Engineer:** Approves aircraft-level design and major trade-offs
- **Domain Leads:** Approve subsystem design within their ATA chapters
- **CAB:** Reviews and approves cross-system design decisions

### Design Reviews
- **Conceptual Design Review (CoDR):** Validate concept feasibility
- **Preliminary Design Review (PDR):** Validate preliminary design meets requirements
- **Critical Design Review (CDR):** Validate detailed design ready for manufacturing
- **Test Readiness Review (TRR):** Validate design ready for prototype build

---

## Integration Points

### Upstream (Inputs)
- **LC-1.1:** Concept baselines and configuration
- **LC-1.2:** Safety-driven design constraints
- **LC-1.3:** Detailed system requirements

### Downstream (Outputs)
- **LC-1.5 Interfaces:** Design defines interface requirements
- **LC-1.6 Analysis:** CAD models used for FEM, CFD analysis
- **LC-1.7 V&V:** Design forms verification baseline
- **LC-2.1 Prototyping:** CAD models drive manufacturing

### Lateral (Parallel)
- **MBSE:** SysML models synchronized with CAD
- **UTCS:** Design elements uniquely identified
- **GenCCC:** Design validation against requirements

---

## Design Best Practices

### CAD Modeling Standards
1. **Parametric:** Use parameters for key dimensions
2. **Modular:** Design for assembly and maintenance
3. **Version Control:** Maintain design baselines in PLM system
4. **Manufacturability:** Design for Manufacturing (DFM)
5. **Maintainability:** Design for Maintenance (DFM)

### Hydrogen-Electric Specific Design
- **Hydrogen Systems (ATA 28H):** Cryogenic tank integration, leak detection
- **Electric Propulsion (ATA 80):** Motor placement, cooling, redundancy
- **Green-E Battery (ATA 85):** Thermal management, crash protection
- **AI/NN Systems (ATA 95):** Computing hardware placement, cooling, EMI protection

### BWB-Specific Design
- Center-of-gravity management for blended configuration
- Structural loads distribution in lifting body
- Cabin layout in non-traditional fuselage
- Novel manufacturing and assembly processes

---

## Key Principles

1. **Requirements-Driven:** All design decisions traced to requirements
2. **Multidisciplinary:** Integrated design across all systems
3. **Model-Based:** CAD as single source of truth
4. **Certification-Ready:** Design compliant with CS-25/FAR Part 25
5. **Sustainable:** Circularity and end-of-life considered in design

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Chief Engineer
