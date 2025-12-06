# LC-11_0000-28 — Assumptions Register

**UTCS Node:** LC-11_0000-28  
**Document Type:** Assumptions Database  
**Status:** Living Document  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Systems Engineering Team

---

## 1. Purpose

This register catalogs all assumptions made during Q100 concept development, enabling tracking, validation, and risk assessment.

---

## 2. Assumption Format

Each assumption includes:
- **Assumption ID:** Unique identifier (ASM-YYYY-NNN)
- **Category:** Technology, Performance, Cost, Schedule, Regulatory, Market
- **Description:** Clear statement of the assumption
- **Confidence:** Low / Medium / High
- **Impact if wrong:** Low / Medium / High
- **Validation plan:** How assumption will be validated
- **Status:** Active / Validated / Invalidated

---

## 3. Technology Assumptions

### ASM-2025-001: Fuel Cell Power Density
- **Category:** Technology
- **Assumption:** PEM fuel cells will achieve 1.2 kW/kg by 2027
- **Confidence:** Medium
- **Impact if wrong:** High (affects MTOW, range)
- **Validation:** Supplier engagement, technology roadmaps
- **Status:** Active

### ASM-2025-002: Battery Energy Density
- **Category:** Technology
- **Assumption:** Green-E batteries achieve 400 Wh/kg by 2027
- **Confidence:** High
- **Impact if wrong:** Medium (battery weight, but not critical path)
- **Validation:** Green-E product roadmap
- **Status:** Validated (current technology)

### ASM-2025-003: BWB Aerodynamic Efficiency
- **Category:** Performance
- **Assumption:** L/D = 21 achievable at M 0.72 cruise
- **Confidence:** Medium
- **Impact if wrong:** High (range, fuel consumption)
- **Validation:** CFD analysis, wind tunnel testing
- **Status:** Active (CFD preliminary)

---

## 4. Regulatory Assumptions

### ASM-2025-010: Hydrogen Aircraft Certification
- **Category:** Regulatory
- **Assumption:** EASA/FAA H₂ special conditions available by 2026
- **Confidence:** Medium
- **Impact if wrong:** High (schedule delay)
- **Validation:** Regulatory engagement, industry forums
- **Status:** Active

### ASM-2025-011: AI Flight Control Certification
- **Category:** Regulatory
- **Assumption:** Hybrid AI augmentation certifiable under existing framework
- **Confidence:** Low
- **Impact if wrong:** Very High (major redesign or schedule delay)
- **Validation:** EASA/FAA consultation, white papers
- **Status:** Active (high priority validation)

---

## 5. Infrastructure Assumptions

### ASM-2025-020: Hydrogen Availability
- **Category:** Market
- **Assumption:** Green H₂ available at key airports by 2030
- **Confidence:** Medium
- **Impact if wrong:** High (market viability)
- **Validation:** Airport H₂ infrastructure roadmaps
- **Status:** Active

---

## 6. Cost and Schedule Assumptions

### ASM-2025-030: Development Cost
- **Category:** Cost
- **Assumption:** $4.0B program cost achievable for Baseline A
- **Confidence:** Medium
- **Impact if wrong:** Medium (funding, business case)
- **Validation:** Detailed cost estimating, vendor quotes
- **Status:** Active

### ASM-2025-031: Entry Into Service
- **Category:** Schedule
- **Assumption:** 2032 EIS achievable with 2027 technology freeze
- **Confidence:** Medium (70%)
- **Impact if wrong:** High (market timing, competition)
- **Validation:** Detailed schedule analysis, risk assessment
- **Status:** Active

---

## 7. Assumption Tracking

### 7.1 High-Priority Validation

| Assumption ID | Description | Priority | Target Validation Date |
|---------------|-------------|----------|------------------------|
| ASM-2025-011 | AI certification path | Very High | Q2 2026 |
| ASM-2025-001 | FC power density | High | Q1 2026 |
| ASM-2025-003 | BWB L/D | High | Q2 2026 (wind tunnel) |
| ASM-2025-020 | H₂ infrastructure | High | Q3 2026 |

### 7.2 Assumptions by Category

| Category | Total | Validated | Active | Invalidated |
|----------|-------|-----------|--------|-------------|
| Technology | 5 | 1 | 4 | 0 |
| Performance | 3 | 0 | 3 | 0 |
| Regulatory | 2 | 0 | 2 | 0 |
| Market | 2 | 0 | 2 | 0 |
| Cost | 1 | 0 | 1 | 0 |
| Schedule | 1 | 0 | 1 | 0 |
| **Total** | **14** | **1** | **13** | **0** |

---

## 8. Change Log

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-12-05 | Initial assumptions register |

---

**© 2025 AMPEL360. All rights reserved.**
