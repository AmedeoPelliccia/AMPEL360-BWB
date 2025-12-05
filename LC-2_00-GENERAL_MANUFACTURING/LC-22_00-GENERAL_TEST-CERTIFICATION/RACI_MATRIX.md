# LC-22 Test Campaign & Certification — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-22 Test Campaign & Certification.

---

## Primary Audiences

| Role                          | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| **Test Engineering**          | Leads ground and systems test campaigns                                     |
| **Flight Test**               | Leads flight test program and certification flights                         |
| **Ground Test**               | Executes ground-based structural and systems testing                        |
| **Certification Authorities** | EASA, FAA, or other regulatory bodies witnessing and approving tests        |

---

## Artefacts & Roles

### Ground Tests

| Artefact      | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|---------------|-----------------|-----------------|---------------|--------------|
| Ground tests  | Test Eng        | CE              | Safety        | Authorities  |

**Description:** Static, fatigue, systems, and environmental qualification testing.

**Key Activities:**
- Static strength tests
- Fatigue and damage tolerance tests
- Systems integration tests
- Environmental qualification (DO-160)
- Witness and documentation

---

### Flight Test Cards

| Artefact          | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-------------------|-----------------|-----------------|---------------|--------------|
| Flight test cards | Flight Test     | CE              | V&V           | Program      |

**Description:** Detailed flight test procedures for certification and performance validation.

**Key Activities:**
- Test point definition
- Safety procedures
- Data requirements
- Success criteria
- Pilot briefings

---

### Certification Evidence

| Artefact             | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I) |
|----------------------|-----------------|-----------------|----------------|--------------|
| Certification evidence| Certification   | CE              | Safety, SysEng | Authorities  |

**Description:** Complete certification package demonstrating compliance with type certification basis.

**Key Activities:**
- Test reports compilation
- Compliance demonstration
- Type Certificate application
- Authority coordination
- Certification review responses

---

### Conformity Documentation

| Artefact                 | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I) |
|--------------------------|-----------------|-----------------|----------------|--------------|
| Conformity documentation | Quality         | Manufacturing   | Certification  | Program      |

**Description:** Documentation demonstrating aircraft conforms to type design.

**Key Activities:**
- Conformity inspections (A, B, C)
- As-built documentation
- Deviation disposition
- Airworthiness sign-off

---

## Information Architecture (IA)

### Folder Structure
```
LC-22_00-GENERAL_TEST-CERTIFICATION/
├── RACI_MATRIX.md (this file)
├── README.md
├── Ground_Tests/
│   ├── LC-22_5700-WINGS_TEST-REPORT-STATIC_V*R*.pdf
│   ├── LC-22_5100-FUSELAGE_TEST-REPORT-FATIGUE_V*R*.pdf
│   ├── LC-22_2800-HYDROGEN_TEST-REPORT-PRESSURE_V*R*.pdf
│   └── LC-22_00-GENERAL_DO160-QUALIFICATION_V*R*.pdf
├── Flight_Test/
│   ├── LC-22_00-GENERAL_FLIGHT-TEST-PLAN_V*R*.pdf
│   ├── Flight_Test_Cards/
│   ├── Flight_Test_Reports/
│   └── Flight_Test_Data/
├── Certification_Evidence/
│   ├── LC-22_00-GENERAL_TYPE-CERT-APPLICATION_V*R*.pdf
│   ├── LC-22_00-GENERAL_COMPLIANCE-MATRIX_V*R*.xlsx
│   ├── Authority_Correspondence/
│   └── Certification_Review_Responses/
└── Conformity/
    ├── LC-22_00-GENERAL_CONFORMITY-INSP-A_V*R*.pdf
    ├── LC-22_00-GENERAL_CONFORMITY-INSP-B_V*R*.pdf
    ├── LC-22_00-GENERAL_CONFORMITY-INSP-C_V*R*.pdf
    └── As_Built_Documentation/
```

### UTCS Naming Convention
- **Format:** `LC-22_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-22_5700-WINGS_TEST-REPORT-STATIC_V1R0.pdf`
- **Example:** `LC-22_00-GENERAL_FLIGHT-TEST-CARD-001_V1R0.pdf`
- **Example:** `LC-22_00-GENERAL_TYPE-CERT-APPLICATION_V2R1.pdf`

---

## Integration Points

### Upstream (Inputs)
- **LC-17 V&V:** Test plans and acceptance criteria
- **LC-21 Prototyping:** Test articles and prototype aircraft
- **LC-12 Safety:** Safety requirements and evidence needs

### Downstream (Outputs)
- **LC-23 FAL:** Production approval based on certification
- **LC-32 MRO:** Test data for maintenance planning
- **Operators:** Certified aircraft ready for service

---

## Key Principles

1. **Safety First:** No test compromises safety of personnel or aircraft
2. **Objective Evidence:** All tests produce quantifiable results
3. **Traceability:** Test results trace to requirements
4. **Authority Coordination:** Regular engagement with certification authorities
5. **Data Quality:** Rigorous data acquisition and validation

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Test & Certification
