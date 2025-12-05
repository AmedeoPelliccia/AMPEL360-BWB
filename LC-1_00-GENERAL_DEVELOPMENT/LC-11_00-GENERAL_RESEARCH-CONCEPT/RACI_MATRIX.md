# LC-1.1 Research & Concept Development — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-1.1 Research & Concept Development.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Chief Engineer (CE)**       | Overall technical authority and decision-maker for the program              |
| **Architecture Board (CAB)**  | Reviews and approves architectural decisions and trade studies              |
| **Research & Innovation**     | Leads exploratory research and novel technology assessment                  |
| **Flight Sciences**           | Responsible for flight physics, performance, and mission analysis           |
| **Aerodynamics & Structures** | Leads aerodynamic configuration and structural conceptual design            |

---

## Artefacts & Roles

### Concept Baselines

| Artefact              | Responsible (R)      | Accountable (A) | Consulted (C)               | Informed (I)      |
|-----------------------|----------------------|-----------------|------------------------------|-------------------|
| Concept baselines     | Architecture         | CE              | Aerodynamics, Structures     | Program Mngt      |

**Description:** High-level aircraft configuration baselines establishing the overall BWB architecture, propulsion integration, and major system boundaries.

**Key Activities:**
- Define BWB configuration parameters
- Hydrogen propulsion system integration
- AI/NN orchestration architecture concept
- Circularity touchpoints identification

---

### Trade Studies

| Artefact        | Responsible (R)      | Accountable (A) | Consulted (C)                | Informed (I)      |
|-----------------|----------------------|-----------------|------------------------------|-------------------|
| Trade studies   | Aerodynamics / R&T   | CE              | Safety, Propulsion, MBSE     | Stakeholders      |

**Description:** Analytical studies comparing alternative architectural, propulsion, and systems configurations to inform design decisions.

**Key Activities:**
- Configuration trade studies (BWB variants)
- Propulsion architecture trades (hydrogen/electric mix)
- Systems architecture alternatives
- Technology readiness assessments

---

### High-Level Configurations

| Artefact                   | Responsible (R) | Accountable (A) | Consulted (C)              | Informed (I) |
|----------------------------|-----------------|-----------------|----------------------------|--------------|
| High-level configurations  | Architecture    | CAB             | Flight Sciences, Loads     | Program      |

**Description:** Preliminary aircraft geometry, major systems layout, and integration concepts.

**Key Activities:**
- Overall vehicle dimensions and proportions
- Major component placement (wing, fuselage, empennage)
- Propulsion system integration
- Cabin and cargo layout concepts

---

### Mission & Performance Envelopes

| Artefact                        | Responsible (R)  | Accountable (A) | Consulted (C)          | Informed (I) |
|---------------------------------|------------------|-----------------|------------------------|--------------|
| Mission & performance envelopes | Flight Sciences  | CE              | Propulsion, Energy     | Program      |

**Description:** Definition of operational requirements, flight profiles, range, payload, and performance targets.

**Key Activities:**
- Mission profile definition (range, altitude, speed)
- Payload-range diagram
- Climb, cruise, descent profiles
- Energy and hydrogen consumption estimates
- Environmental performance targets

---

## Information Architecture (IA)

### Folder Structure
```
LC-11_00-GENERAL_RESEARCH-CONCEPT/
├── RACI_MATRIX.md (this file)
├── README.md
├── Concept_Baselines/
│   ├── LC-11_00-GENERAL_BWB-CONFIG_V*.md
│   ├── LC-11_7100-POWERPLANT_PROPULSION-INTEGRATION_V*.md
│   └── LC-11_00-GENERAL_SYSTEMS-ARCHITECTURE_V*.md
├── Trade_Studies/
│   ├── LC-11_00-GENERAL_CONFIG-TRADES_V*.md
│   ├── LC-11_7100-POWERPLANT_PROPULSION-TRADES_V*.md
│   └── LC-11_00-GENERAL_TECH-ASSESSMENT_V*.md
├── High_Level_Configurations/
│   ├── LC-11_5100-FUSELAGE_VEHICLE-GEOMETRY_V*.md
│   ├── LC-11_00-GENERAL_MAJOR-SYSTEMS-LAYOUT_V*.md
│   └── LC-11_00-GENERAL_INTEGRATION-CONCEPTS_V*.md
└── Mission_Performance_Envelopes/
    ├── LC-11_00-GENERAL_MISSION-PROFILES_V*.md
    ├── LC-11_00-GENERAL_PERFORMANCE-REQUIREMENTS_V*.md
    └── LC-11_2800-HYDROGEN_ENERGY-ANALYSIS_V*.md
```

### UTCS Naming Convention
All artefacts in this stage follow the UTCS-LC naming standard:
- **Format:** <span style="color:#0066cc">`LC-11`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** <span style="color:#0066cc">`LC-11`</span>`_`<span style="color:#cc6600">`00`</span>`-`<span style="color:#666666">`GENERAL`</span>`_`<span style="color:#009900">`CONCEPT-BASELINE`</span>`_`<span style="color:#990099">`V1R0`</span>`.md`
- **Example:** <span style="color:#0066cc">`LC-11`</span>`_`<span style="color:#cc6600">`00`</span>`-`<span style="color:#666666">`GENERAL`</span>`_`<span style="color:#009900">`TRADE-STUDY-BWB`</span>`_`<span style="color:#990099">`V2R1`</span>`.md`

See [UTCS-LC Naming Rules](../../UTCS/UTCS-LC_NAMING_RULES.md) for complete specification.

---

## Governance & Approval

### Review Cycles
- **Weekly:** Architecture Board reviews concept evolution
- **Monthly:** Program management informed of progress
- **Milestone:** CE approval required for baseline freeze

### Decision Authority
- **Chief Engineer:** Final approval of concept baseline
- **CAB:** Approval of major trade study results
- **Program Management:** Informed consent for resource allocation

### Traceability
- All concept decisions tracked in UTCS with unique IDs
- GenCCC automatically validates traceability to program requirements
- CGen generates consistent documentation across all concept artefacts

---

## Integration Points

### Upstream (Inputs)
- Market requirements and customer needs
- Technology roadmaps and maturity assessments
- Regulatory and certification landscape
- Sustainability and environmental targets

### Downstream (Outputs)
- **LC-1.2 Safety Analysis:** Concept-level hazard identification
- **LC-1.3 Requirements Engineering:** Derived requirements from concept
- **LC-1.4 Detailed Design:** Frozen concept baseline for detailed design
- **LC-1.6 Engineering Analysis:** Initial sizing for analysis models

### Lateral (Parallel)
- **OPT-IN Framework:** Concept artifacts feed Organization and Program axes
- **MBSE:** Architecture models synchronized with concept evolution
- **GenCCC:** Requirements capture and traceability setup

---

## Key Principles

1. **Early Exploration:** Maximize design space exploration before committing to detailed design
2. **Data-Driven Decisions:** All trades backed by analytical evidence and stakeholder input
3. **Sustainability First:** Environmental impact considered from concept phase
4. **Safety Integration:** Preliminary hazards identified and addressed in concept
5. **Digital Thread:** All concept artefacts uniquely identified and traceable via UTCS

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Architecture Board
