# LC-21 Prototyping — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-21 Prototyping.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Manufacturing Engineering** | Leads prototype manufacturing planning and execution                        |
| **Tooling**                   | Responsible for jigs, fixtures, and tooling design                          |
| **Prototype Shop**            | Executes prototype builds and assembly                                      |

---

## Artefacts & Roles

### Prototype Build Instructions

| Artefact                      | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I) |
|-------------------------------|-----------------|-----------------|----------------|--------------|
| Prototype build instructions  | Manufacturing   | Production Lead | Design, QA     | Program      |

**Description:** Detailed instructions for building prototype aircraft or major assemblies.

**Key Activities:**
- Manufacturing process planning
- Assembly sequence definition
- Tooling and fixture requirements
- Quality inspection points
- Build documentation

---

### Prototype Configuration

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| Prototype configuration| Manufacturing   | CE              | Production    | V&V          |

**Description:** Configuration baseline for prototype aircraft including deviations from production design.

**Key Activities:**
- As-built configuration documentation
- Deviation tracking and approval
- UTCS identity assignment
- Configuration freeze for test

---

### Prototype Physical Test Artefacts

| Artefact                          | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I)  |
|-----------------------------------|-----------------|-----------------|---------------|---------------|
| Prototype physical test artefacts | Manufacturing   | QA              | V&V           | Certification |

**Description:** Physical test articles and specimens for structural, systems, and certification testing.

**Key Activities:**
- Test article fabrication
- Witness coupons and specimens
- Instrumentation installation
- Quality acceptance
- Delivery to test facilities

---

## Information Architecture (IA)

### Folder Structure
```
LC-21_00-GENERAL_PROTOTYPING/
├── RACI_MATRIX.md (this file)
├── README.md
├── Build_Instructions/
│   ├── LC-21_5100-FUSELAGE_BUILD-INSTR-PROTO1_V*R*.md
│   ├── LC-21_5700-WINGS_BUILD-INSTR-PROTO1_V*R*.md
│   └── LC-21_2800-HYDROGEN_BUILD-INSTR-TANK_V*R*.md
├── Configuration_Baselines/
│   ├── LC-21_00-GENERAL_PROTO1-CONFIG-BASELINE_V*R*.md
│   ├── LC-21_00-GENERAL_PROTO1-DEVIATION-LOG_V*R*.csv
│   └── As_Built_Documentation/
└── Test_Articles/
    ├── LC-21_5700-WINGS_TEST-ARTICLE-STATIC_V*R*.md
    ├── LC-21_5100-FUSELAGE_TEST-ARTICLE-FATIGUE_V*R*.md
    └── LC-21_2800-HYDROGEN_TEST-ARTICLE-PRESSURE_V*R*.md
```

### UTCS Naming Convention
- **Format:** <span style="color:#0066cc">`LC-21`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** `LC-21_5100-FUSELAGE_BUILD-INSTR-PROTO1_V1R0.md`
- **Example:** `LC-21_00-GENERAL_PROTO1-CONFIG-BASELINE_V1R2.md`

---

## Integration Points

### Upstream (Inputs)
- **LC-14 Design:** CAD models and engineering drawings
- **LC-15 Interfaces:** Assembly instructions and ICDs
- **LC-17 V&V:** Test requirements for prototype

### Downstream (Outputs)
- **LC-22 Test Campaign:** Prototype aircraft for testing
- **LC-23 FAL:** Lessons learned for production planning
- **LC-17 V&V:** Test evidence from prototype builds

---

## Key Principles

1. **Design Fidelity:** Prototype represents production design intent
2. **Lessons Learned:** Capture manufacturing insights for production
3. **Quality Focus:** Prototype quality supports valid test results
4. **Configuration Control:** Rigorous tracking of prototype configuration
5. **Safety First:** Prototype safety for personnel and test programs

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Manufacturing Engineering
