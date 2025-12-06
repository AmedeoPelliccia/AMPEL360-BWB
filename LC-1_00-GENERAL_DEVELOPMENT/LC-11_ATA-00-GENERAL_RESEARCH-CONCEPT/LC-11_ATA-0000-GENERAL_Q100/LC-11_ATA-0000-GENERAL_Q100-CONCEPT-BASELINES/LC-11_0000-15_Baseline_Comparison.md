# LC-11_0000-15 — Baseline Comparison

**UTCS Node:** LC-11_0000-15  
**Document Type:** Trade Study Analysis  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Architecture Board

---

## 1. Purpose

This document provides a comprehensive comparison of Baselines A, B, and C to support configuration selection and technology roadmap planning.

---

## 2. Summary Comparison Table

| Parameter | Baseline A | Baseline B | Baseline C | Units |
|-----------|------------|------------|------------|-------|
| **Technology Maturity (TRL freeze)** | 2027 | 2029 | 2031 | — |
| **Risk Level** | Low-Medium | Medium | High | — |
| **MTOW** | 65,000 | 62,000 | 59,000 | kg |
| **OEW** | 38,000 | 36,000 | 34,000 | kg |
| **Payload** | 12,000 | 12,000 | 12,000 | kg |
| **Fuel capacity** | 2,500 | 2,300 | 2,100 | kg H₂ |
| **Design range** | 1,500 | 1,650 | 1,800 | nm |
| **Cruise L/D** | 21.0 | 21.5 | 22.0 | — |
| **FC power** | 4,000 | 4,000 | 4,000 | kW |
| **FC power density** | 1.2 | 1.5 | 1.8 | kW/kg |
| **FC system mass** | 3,333 | 2,667 | 2,222 | kg |
| **Battery capacity** | 1,000 | 1,000 | 1,000 | kWh |
| **Battery density** | 400 | 400 | 450 | Wh/kg |
| **Battery mass** | 2,500 | 2,500 | 2,222 | kg |
| **H₂ storage** | GH₂ 350 bar | GH₂ 700/LH₂ | LH₂ | — |
| **H₂ tank mass** | 2,800 | 2,200 | 1,800 | kg |
| **EIS target** | 2032 | 2033 | 2035 | — |
| **Development cost** | $4.0B | $4.2B | $4.5B | USD |
| **Unit cost (est.)** | $85M | $82M | $80M | USD |

---

## 3. Technology Delta Analysis

### 3.1 Fuel Cell Systems

**Baseline A → B:**
- Power density: +25% (1.2 → 1.5 kW/kg)
- Mass savings: -666 kg
- Technology path: Automotive heavy-duty scaling

**Baseline B → C:**
- Power density: +20% (1.5 → 1.8 kW/kg)
- Mass savings: -445 kg
- Technology path: Aerospace-optimized design

### 3.2 Hydrogen Storage

**Baseline A:**
- 350 bar GH₂, proven COPV technology
- Tank mass: 2,800 kg, Volume: 40 m³

**Baseline B:**
- 700 bar GH₂ or early LH₂ option
- Tank mass: 2,200 kg, Volume: 20-25 m³

**Baseline C:**
- LH₂ baseline, cryogenic mature
- Tank mass: 1,800 kg, Volume: 13.5 m³

---

## 4. Performance Comparison

### 4.1 Mission Capability

| Mission Type | Baseline A | Baseline B | Baseline C |
|--------------|------------|------------|------------|
| **Max payload, 500 nm** | 14,000 kg | 14,000 kg | 14,000 kg |
| **Design (12 tons), range** | 1,500 nm | 1,650 nm | 1,800 nm |
| **Max range (reduced pax)** | 2,000 nm | 2,200 nm | 2,400 nm |

### 4.2 Efficiency Metrics

| Metric | Baseline A | Baseline B | Baseline C |
|--------|------------|------------|------------|
| **Energy/pax-km** | 0.43 MJ | 0.40 MJ | 0.38 MJ |
| **vs. A320neo** | -33% | -38% | -41% |
| **DOC reduction** | -20% | -23% | -25% |

---

## 5. Risk Comparison

### 5.1 Technical Risk

| Risk Area | Baseline A | Baseline B | Baseline C |
|-----------|------------|------------|------------|
| **Fuel cell maturity** | Medium | Medium | High |
| **H₂ storage** | Low-Med | Medium | High |
| **Battery technology** | Low | Low | Medium |
| **AI certification** | High | Medium | Medium |
| **Overall technical risk** | **Medium** | **Medium** | **High** |

### 5.2 Schedule Risk

| Parameter | Baseline A | Baseline B | Baseline C |
|-----------|------------|------------|------------|
| **Tech freeze** | 2027 | 2029 | 2031 |
| **First flight** | 2029 | 2031 | 2033 |
| **EIS** | 2032 | 2033 | 2035 |
| **Schedule confidence** | 70% | 60% | 40% |

---

## 6. Cost Comparison

### 6.1 Development Costs

- **Baseline A:** $4.0B (baseline)
- **Baseline B:** $4.2B (+5%, technology maturation costs)
- **Baseline C:** $4.5B (+12.5%, high-risk technology)

### 6.2 Unit Production Costs

- **Baseline A:** $85M (100th aircraft)
- **Baseline B:** $82M (-3.5%, weight savings)
- **Baseline C:** $80M (-6%, cryogenic complexity offset by weight)

---

## 7. Market Analysis

### 7.1 Airline Acceptance

| Factor | Baseline A | Baseline B | Baseline C |
|--------|------------|------------|------------|
| **Technology risk perception** | Acceptable | Acceptable | Concerning |
| **H₂ infrastructure readiness** | 2030 OK | 2033 OK | 2035 uncertain |
| **Performance advantage** | Good | Better | Best |
| **Cost competitiveness** | Good | Better | Best |

### 7.2 Competitive Position

All baselines outperform conventional aircraft (A320neo) on:
- Operating costs: 20-25% reduction
- Emissions: 100% reduction (green H₂)
- Noise: 50% reduction

---

## 8. Recommendation

**Primary Baseline:** **Baseline A**

**Rationale:**
1. **Lowest programmatic risk:** Technology maturity aligned with 2027 freeze
2. **Achievable schedule:** 2032 EIS credible
3. **Market timing:** H₂ infrastructure available at key airports by 2030
4. **Technology hedge:** Baseline B as fallback if FC technology advances faster

**Secondary Option:** **Baseline B** (monitor for PDR decision point)

**Not Recommended:** **Baseline C** (too high risk for initial program)

---

## 9. Decision Points

| Milestone | Decision | Criteria |
|-----------|----------|----------|
| **MCR-1 (Q2 2026)** | Confirm Baseline A | No major technical roadblocks |
| **PDR (Q4 2026)** | Baseline A vs. B | FC power density achievement |
| **CDR (Q4 2027)** | Final baseline freeze | All technologies at TRL 7+ |

---

## 10. References

- [LC-11_0000-12 — Baseline A Definition](./LC-11_0000-12_BaselineA_Definition.md)
- [LC-11_0000-13 — Baseline B Definition](./LC-11_0000-13_BaselineB_Definition.md)
- [LC-11_0000-14 — Baseline C Definition](./LC-11_0000-14_BaselineC_Definition.md)

---

**© 2025 AMPEL360. All rights reserved.**
