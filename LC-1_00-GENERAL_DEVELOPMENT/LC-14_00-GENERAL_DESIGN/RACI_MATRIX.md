# LC-14 Design Engineering — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-14 Design Engineering.

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
- Validate against requirements (LC-13)
- Coordinate with safety analysis (LC-12)

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
LC-14_00-GENERAL_DESIGN/
├── RACI_MATRIX.md (this file)
├── README.md
├── Preliminary_Design/
│   ├── LC-14_00-GENERAL_SYSTEM-ARCHITECTURE-DIAGRAMS_V*.md
│   ├── LC-14_00-GENERAL_CONCEPT-LAYOUTS_V*.md
│   └── LC-14_00-GENERAL_SIZING-STUDIES_V*.csv
├── CAD_Models/
│   ├── Master_Geometry/
│   │   ├── LC-14_5100-FUSELAGE_BWB-FUSELAGE_V*.catpart
│   │   ├── LC-14_5700-WINGS_WING-ASSEMBLY_V*.catproduct
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
│   ├── LC-14_2400-ELECTRICAL-POWER_ELECTRICAL-DIAGRAMS_V*.md
│   ├── LC-14_2900-HYDRAULIC-POWER_HYD-PNEUMATIC-DIAGRAMS_V*.md
│   ├── LC-14_2700-FLIGHT-CONTROLS_CONTROL-LOGIC-DIAGRAMS_V*.md
│   └── LC-14_4200-IMA_DATA-BUS-ARCHITECTURE_V*.md
└── ATA_Design_Documentation/
    ├── LC-14_2100-AIR-CONDITIONING_DESIGN-DESCRIPTION_V*.md
    ├── LC-14_2700-FLIGHT-CONTROLS_DESIGN-DESCRIPTION_V*.md
    ├── LC-14_2800-HYDROGEN_DESIGN-DESCRIPTION_V*.md
    └── [Other ATA chapters...]
```

### UTCS Naming Convention
- **Format:** <span style="color:#0066cc">`LC-14`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** <span style="color:#0066cc">`LC-14`</span>`_`<span style="color:#cc6600">`27`</span>`-`<span style="color:#666666">`FLIGHT-CONTROLS`</span>`_`<span style="color:#009900">`PRELIM-DESIGN`</span>`_`<span style="color:#990099">`V1R0`</span>`.md`
- **Example:** <span style="color:#0066cc">`LC-14`</span>`_`<span style="color:#cc6600">`2800`</span>`-`<span style="color:#666666">`HYDROGEN`</span>`_`<span style="color:#009900">`CAD-TANK-ASSY`</span>`_`<span style="color:#990099">`V2R1`</span>`.catproduct`
- **Example:** <span style="color:#0066cc">`LC-14`</span>`_`<span style="color:#cc6600">`9500`</span>`-`<span style="color:#666666">`NN-SYSTEMS`</span>`_`<span style="color:#009900">`SCHEMATIC-NN-FCS`</span>`_`<span style="color:#990099">`V1R0`</span>`.md`

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
- **LC-11:** Concept baselines and configuration
- **LC-12:** Safety-driven design constraints
- **LC-13:** Detailed system requirements

### Downstream (Outputs)
- **LC-15 Interfaces:** Design defines interface requirements
- **LC-16 Analysis:** CAD models used for FEM, CFD analysis
- **LC-17 V&V:** Design forms verification baseline
- **LC-21 Prototyping:** CAD models drive manufacturing

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
