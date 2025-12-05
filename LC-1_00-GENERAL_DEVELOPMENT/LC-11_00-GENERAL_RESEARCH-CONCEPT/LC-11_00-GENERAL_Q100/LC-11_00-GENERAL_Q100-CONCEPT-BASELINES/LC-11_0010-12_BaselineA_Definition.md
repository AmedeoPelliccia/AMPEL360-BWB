# LC-11_0010-12 — Baseline A Definition

**UTCS Node:** LC-11_0010-12  
**Document Type:** Baseline Configuration  
**Status:** Frozen  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Architecture Board

---

## 1. Purpose

This document defines Baseline A, the conservative technology configuration for the AMPEL360 BWB Q100, based on 2027-2028 technology readiness levels (TRL 6-7).

---

## 2. Baseline A Overview

**Philosophy:** Conservative assumptions using proven or near-term technologies to minimize programmatic risk.

**Target Entry Into Service:** 2030-2032  
**Technology Freeze Date:** 2027  
**Risk Posture:** Low-Medium

---

## 3. Key Parameters Summary

| Parameter | Value | Units | Confidence |
|-----------|-------|-------|------------|
| **MTOW** | 65,000 | kg | High |
| **OEW** | 38,000 | kg | Medium |
| **Payload** | 12,000 | kg | High |
| **Fuel capacity (H₂)** | 2,500 | kg | High |
| **Range (design)** | 1,500 | nm | High |
| **Cruise L/D** | 21.0 | — | Medium |
| **Fuel cell power density** | 1.2 | kW/kg | Medium |
| **Battery energy density** | 400 | Wh/kg | High |

---

## 4. Configuration Details

### 4.1 Airframe

- **Wingspan:** 45.0 m
- **Wing area:** 295 m²
- **Aspect ratio:** 6.86
- **Structure:** CFRP primary structure, OOA manufacturing
- **Cabin:** 2-3-2 seating, 100 pax nominal

### 4.2 Propulsion

- **Fuel cells:** PEM, 4,000 kW, 1.2 kW/kg
- **Motors:** 8× electric motors, 500 kW each
- **Battery:** 1,000 kWh Green-E Li-ion, 400 Wh/kg
- **H₂ storage:** GH₂ at 350 bar, Type IV COPV tanks

### 4.3 Systems

- **Flight control:** Hybrid AI-augmented + conventional
- **Electrical:** 800 VDC high-voltage DC architecture
- **Thermal management:** Integrated FC/battery/motor cooling

---

## 5. Technology Maturity Assessment

| Technology Area | TRL (2025) | TRL (2027) | Risk | Notes |
|-----------------|------------|------------|------|-------|
| **BWB aerodynamics** | 4-5 | 6 | Medium | Wind tunnel validation needed |
| **CFRP structure** | 7-8 | 8 | Low | Boeing 787 heritage |
| **Fuel cell (1.2 kW/kg)** | 5 | 6-7 | Medium | Automotive FC scaling |
| **Battery (400 Wh/kg)** | 7 | 8 | Low | Current EV technology |
| **GH₂ storage (350 bar)** | 6 | 7 | Low-Medium | Automotive H₂ tanks |
| **Distributed propulsion** | 4 | 6 | Medium | Flight test validation needed |
| **AI flight control** | 3-4 | 5-6 | High | Certification challenge |

---

## 6. Performance Capability

### 6.1 Design Mission

- **Range:** 1,500 nm + 200 nm reserves
- **Payload:** 100 pax + baggage (12,000 kg)
- **Cruise:** M 0.72 at FL390
- **Takeoff field:** 2,000 m (ISA, SL)
- **Landing field:** 1,800 m (ISA, SL)

### 6.2 Alternative Missions

| Mission Type | Range (nm) | Payload (kg) | Notes |
|--------------|------------|--------------|-------|
| Short-haul | 500 | 14,000 | High-density (120 pax) |
| Design point | 1,500 | 12,000 | 100 pax standard |
| Extended range | 2,000 | 8,500 | Reduced payload |

---

## 7. Cost and Schedule

### 7.1 Development Cost (Estimated)

- **Non-recurring engineering:** $2.5B (2025 dollars)
- **Tooling and facilities:** $800M
- **Flight test program:** $400M
- **Certification:** $300M
- **Total program cost:** ~$4B

### 7.2 Unit Cost (Target)

- **Flyaway cost (initial):** $85M (100th aircraft)
- **Operating cost:** 20% lower than A320neo (DOC per seat-mile)

### 7.3 Development Schedule

- **Concept freeze:** Q4 2025 ✓
- **PDR:** Q4 2026
- **CDR:** Q4 2027
- **First flight:** 2029
- **Certification:** 2031
- **EIS:** 2032

---

## 8. Risk Areas

### 8.1 Technical Risks

1. **Fuel cell power density:** May not achieve 1.2 kW/kg by 2027
   - Mitigation: Baseline B with 1.5 kW/kg as backup
2. **AI certification:** Regulatory framework unclear
   - Mitigation: Hybrid architecture (AI augmentation, not replacement)
3. **BWB cabin egress:** Wide cabin evacuation demonstration
   - Mitigation: Early mockup testing and certification authority engagement

### 8.2 External Dependencies

1. **Hydrogen infrastructure:** Airport H₂ availability by 2030
2. **Regulatory framework:** EASA/FAA H₂ aircraft special conditions
3. **Supply chain:** Fuel cell and battery suppliers scaling production

---

## 9. Comparison to Baseline B and C

| Parameter | Baseline A | Baseline B | Baseline C |
|-----------|------------|------------|------------|
| **TRL basis** | 2027 | 2029 | 2031 |
| **Risk** | Low-Med | Medium | High |
| **MTOW** | 65,000 kg | 62,000 kg | 59,000 kg |
| **FC power density** | 1.2 kW/kg | 1.5 kW/kg | 1.8 kW/kg |
| **H₂ storage** | GH₂ 350 bar | GH₂ 700 / LH₂ | LH₂ |
| **EIS target** | 2032 | 2033 | 2035 |

**Recommendation:** Proceed with Baseline A for program launch, monitor technology maturation for potential Baseline B transition at PDR.

---

## 10. Approval and Freeze

**Baseline A Freeze:** October 15, 2025  
**Approved By:** Chief Engineer, Architecture Board  
**Status:** Frozen for preliminary design phase

**Change Control:** Any changes to Baseline A require Architecture Board approval and formal change request process.

---

## 11. References

- [LC-11_0010-01 — Concept Overview](./LC-11_0010-01_Concept_Overview.md)
- [LC-11_0010-09 — Preliminary Mass Breakdown](./LC-11_0010-09_PMB0_Preliminary_Mass_Breakdown.md)
- [LC-11_0010-15 — Baseline Comparison](./LC-11_0010-15_Baseline_Comparison.md)

---

**Document Control:**  
**Status:** FROZEN  
**Distribution:** All Engineering Teams, Program Management, Executive Leadership  
**Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
