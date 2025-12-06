# LC-11_0000-03 — Concept Evolution Log

**UTCS Node:** LC-11_0000-03  
**Document Type:** Decision History  
**Status:** Living Document  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** AMPEL360 Architecture Board

---

## 1. Purpose

This document tracks the evolution of the AMPEL360 BWB Q100 concept from initial ideation through baseline freeze. It provides a chronological record of major design decisions, rationale changes, and lessons learned to support future decision-making and maintain institutional knowledge.

---

## 2. Evolution Timeline

### 2.1 Phase 0: Initial Ideation (Q4 2024)

#### Concept Genesis
- **Date:** October 2024
- **Event:** AMPEL360 program initiation workshop
- **Participants:** Architecture Board, Chief Engineer, Strategic Partners
- **Outcome:** Decision to pursue BWB configuration for next-generation sustainable aircraft

#### Key Insights
- Market analysis identified 100-150 seat regional/short-haul segment as optimal entry point
- Hydrogen propulsion selected as primary energy source due to zero CO₂ emissions
- AI integration identified as enabling technology for BWB flight control challenges

#### Initial Assumptions
- **Range target:** 1,500 nm with full passenger load
- **Technology readiness:** 2030-2032 entry into service feasible
- **Regulatory environment:** EASA/FAA hydrogen certification framework under development

---

### 2.2 Phase 1: Configuration Studies (Q4 2024 - Q1 2025)

#### Entry: November 2024

**Activity:** Parametric BWB configuration studies  
**Lead:** Aerodynamics & Structures Team

**Configurations Evaluated:**
1. Pure flying wing (no distinct fuselage)
2. Hybrid BWB (partial blending)
3. Full BWB with integrated centerbody
4. Conventional tube-and-wing with H₂ pods

**Key Findings:**
- Pure flying wing cabin layout impractical for passenger egress
- Full BWB offers optimal balance of efficiency and cabin viability
- Conventional configuration incompatible with large hydrogen tank integration

**Decision:** **Adopt full BWB configuration (Option 3)**  
**Rationale:** 30-40% efficiency gain, optimal H₂ integration, manageable cabin complexity  
**Approver:** Chief Engineer  
**Date:** December 15, 2024

---

#### Entry: January 2025

**Activity:** Propulsion architecture trade study  
**Lead:** Propulsion & Energy Team

**Options Evaluated:**
1. Battery-electric only
2. Hydrogen fuel cell electric
3. Hydrogen combustion turbines
4. Hybrid H₂ fuel cell + battery
5. Hybrid H₂ turbine + fuel cell

**Key Findings:**
- Battery-only: Range limited to ~400 nm (insufficient)
- H₂ fuel cell: 1,500 nm achievable but requires peak power solution
- H₂ turbines: Higher power density but lower efficiency, NOx emissions
- Hybrid FC+Battery: Optimal balance of range, efficiency, and peak power

**Decision:** **Adopt H₂ fuel cell + battery hybrid (Option 4)**  
**Rationale:** Zero CO₂, 1,500+ nm range, batteries provide takeoff power  
**Approver:** Architecture Board  
**Date:** January 20, 2025

---

### 2.3 Phase 2: Preliminary Sizing (Q1 - Q2 2025)

#### Entry: February 2025

**Activity:** Initial sizing loop iteration  
**Lead:** Flight Sciences & Performance Team

**Inputs:**
- Mission: 1,500 nm, 100 passengers, ICAO reserves
- L/D estimate: 20-22 (cruise)
- Fuel cell system: 1.2 kW/kg (2027 projection)
- Battery: 350 Wh/kg (Green-E baseline)

**Results (Iteration 1):**
- MTOW: ~68,000 kg
- Hydrogen mass: 2,200 kg (GH₂ at 350 bar)
- Wingspan: 42 m
- **Issue:** Wing loading resulted in excessive structural weight

**Action:** Increase wingspan to 45 m, iterate structural layout

---

#### Entry: March 2025

**Activity:** Refined sizing with structural optimization  
**Lead:** Structures Team

**Changes:**
- Wingspan increased to 45 m (aspect ratio ~6.5)
- CFRP primary structure weight model refined
- Hydrogen tank arrangement optimized for CG management

**Results (Iteration 2):**
- MTOW: ~64,000 kg
- Hydrogen mass: 2,000 kg
- Empty weight: ~38,000 kg
- **Assessment:** Within feasibility envelope, proceed to baseline definition

**Decision:** **Freeze preliminary sizing for Baseline A**  
**Approver:** Chief Engineer  
**Date:** March 30, 2025

---

### 2.4 Phase 3: Propulsion Distribution (Q2 2025)

#### Entry: April 2025

**Activity:** Distributed propulsion architecture study  
**Lead:** Propulsion Integration Team

**Configurations Evaluated:**
1. Two large fans (underwing pods)
2. Four fans (spanwise distribution)
3. Six fans (trailing edge, upper surface)
4. Eight fans (trailing edge, upper surface)
5. Twelve fans (trailing edge, upper surface)

**Key Trade Factors:**
- Redundancy and safety (more fans = better fail-safe)
- Aerodynamic efficiency (BLI benefits)
- Electrical system complexity
- Weight and maintenance considerations

**CFD Results:**
- BLI efficiency gains: 5-8% with trailing edge upper surface placement
- Six fans: Minimum configuration for fail-safe single-engine-out
- Eight fans: Optimal balance of efficiency, redundancy, weight

**Decision:** **Adopt 8-fan distributed propulsion baseline**  
**Rationale:** Safety redundancy + BLI efficiency + manageable complexity  
**Approver:** Architecture Board  
**Date:** April 25, 2025

---

#### Entry: May 2025

**Activity:** AI flight control architecture definition  
**Lead:** Avionics & Control Laws Team

**Approach:**
- Hybrid AI + conventional control architecture
- Neural network adaptive augmentation of baseline control laws
- Multi-layer safety architecture with monitoring and fallback

**Key Decisions:**
1. AI augments (not replaces) conventional flight control laws
2. Three-layer architecture: Conventional → AI Augmentation → AI Monitoring
3. Extensive simulation and test validation required before certification

**Outcome:** AI integration plan approved with certification roadmap  
**Approver:** Chief Engineer, pending regulatory consultation  
**Date:** May 15, 2025

---

### 2.5 Phase 4: System Integration (Q3 2025)

#### Entry: July 2025

**Activity:** Hydrogen storage architecture definition  
**Lead:** Energy Systems & Safety Team

**Storage Options Evaluated:**
1. Compressed GH₂ (350 bar) - multiple COPV tanks
2. Compressed GH₂ (700 bar) - fewer, heavier tanks
3. Liquid H₂ (LH₂) cryogenic tanks
4. Hybrid GH₂ + LH₂

**Trade Analysis:**
- 350 bar GH₂: Mature technology, higher volume
- 700 bar GH₂: Lower volume, higher tank weight, safety concerns
- LH₂: Minimum volume, cryogenic complexity, boil-off management
- Hybrid: Complexity outweighs benefits

**Decision:** **Baseline: 350 bar GH₂ with LH₂ as future upgrade path**  
**Rationale:** Lower risk for first aircraft, volume acceptable in BWB centerbody  
**Approver:** Architecture Board  
**Date:** July 10, 2025

---

#### Entry: August 2025

**Activity:** Thermal management system architecture  
**Lead:** Environmental Control Systems (ECS) Team

**Challenge:** Integrated cooling for:
- Fuel cell stacks (~50% waste heat)
- Electric motors and power electronics
- Battery thermal management
- Cabin ECS

**Solution:** Unified thermal management system with:
- Liquid cooling loops (water-glycol)
- Ram air heat exchangers
- Fuel-cooled oil coolers (H₂ pre-heating)
- Vapor cycle cabin conditioning

**Outcome:** Integrated TMS architecture defined  
**Date:** August 20, 2025

---

### 2.6 Phase 5: Baseline Definition (Q3 - Q4 2025)

#### Entry: September 2025

**Activity:** Three-baseline strategy definition  
**Lead:** Architecture Board

**Baseline Strategy:**
- **Baseline A:** Conservative assumptions, proven technologies (2027-2028 TRL)
- **Baseline B:** Moderate assumptions, near-term advances (2028-2029 TRL)
- **Baseline C:** Aggressive assumptions, optimistic technology (2029-2030 TRL)

**Purpose:** Bracket uncertainty range, support risk assessment and decision-making

**Outcome:** Baseline comparison framework established  
**Date:** September 5, 2025

---

#### Entry: October 2025

**Activity:** Baseline A definition freeze  
**Status:** **COMPLETE**

**Baseline A Characteristics:**
- Fuel cell: 1.2 kW/kg (conservative)
- Battery: 350 Wh/kg (current Green-E)
- GH₂ storage: 350 bar COPV
- 8 distributed fans
- MTOW: ~65,000 kg

**Approval:** Architecture Board and Chief Engineer  
**Date:** October 15, 2025

---

#### Entry: November 2025

**Activity:** Baseline B and C definition  
**Status:** **COMPLETE**

**Baseline B:** Moderate technology improvements
- Fuel cell: 1.5 kW/kg
- Battery: 400 Wh/kg
- Possible LH₂ storage
- MTOW: ~62,000 kg

**Baseline C:** Aggressive technology assumptions
- Fuel cell: 1.8 kW/kg
- Battery: 450 Wh/kg
- LH₂ storage baseline
- Advanced AI control (full authority)
- MTOW: ~59,000 kg

**Approval:** Architecture Board  
**Date:** November 20, 2025

---

### 2.7 Phase 6: Current Status (Q4 2025)

#### Entry: December 2025

**Activity:** Baseline comparison and selection preparation  
**Status:** **IN PROGRESS**

**Current Activities:**
- Detailed trade study analysis (Baseline A vs. B vs. C)
- Risk assessment for each baseline
- Technology maturation roadmap validation
- Regulatory consultation on certification approach

**Next Milestone:** Mission Concept Review (MCR-1) - Planned Q2 2026

**Open Questions:**
- Final baseline selection criteria
- Supplier engagement timeline
- Infrastructure availability assumptions
- Certification timeline and requirements

---

## 3. Key Design Drivers Evolution

### 3.1 Initial Drivers (Q4 2024)

1. Zero operational CO₂ emissions
2. 1,500 nm range capability
3. 100-120 passenger capacity
4. Aerodynamic efficiency

### 3.2 Current Drivers (Q4 2025)

1. **Environmental:** Zero CO₂, 50% noise reduction, lifecycle sustainability
2. **Performance:** 1,500 nm range, 30% efficiency improvement vs. A320neo
3. **Safety:** Exceed CS-25/FAR-25 with novel propulsion/control
4. **Economic:** 20% DOC reduction, competitive acquisition cost
5. **Certifiability:** Technology maturity aligned with 2030-2032 entry into service
6. **Manufacturability:** Scalable composite production, modular design

### 3.3 Driver Priority Changes

| Driver | Initial Priority | Current Priority | Change Rationale |
|--------|------------------|------------------|------------------|
| Environmental | High | **Very High** | Market demand and regulatory pressure increased |
| Certifiability | Medium | **High** | Novel propulsion/AI complexity recognized |
| Manufacturability | Medium | **High** | Production scale-up identified as critical path |
| Cost | High | **High** | Maintained as key competitive factor |

---

## 4. Lessons Learned

### 4.1 Technical Insights

1. **BWB cabin layout:** More complex than initially assumed; requires early mockup validation
2. **Hydrogen safety:** Multi-layer safety architecture essential for certification acceptance
3. **AI certification:** Regulatory framework development slower than anticipated; hybrid approach necessary
4. **Distributed propulsion:** Electrical distribution system weight significant driver; high-voltage DC critical
5. **Thermal integration:** Unified thermal management system enables significant weight savings

### 4.2 Process Insights

1. **Early supplier engagement:** Critical for technology maturity validation (especially fuel cells)
2. **Regulatory dialogue:** Continuous EASA/FAA consultation prevents late-stage surprises
3. **Multi-baseline strategy:** Effective for managing technology risk and uncertainty
4. **Digital thread:** UTCS naming and traceability investment pays off in configuration management
5. **Cross-functional collaboration:** Weekly Architecture Board reviews accelerate decision-making

### 4.3 Risk Management

1. **Technology risk:** Fuel cell power density and durability remain on critical path
2. **Certification risk:** AI flight control certification timeline uncertain
3. **Infrastructure risk:** Hydrogen airport availability key external dependency
4. **Manufacturing risk:** Large composite panel production requires capital investment
5. **Market risk:** Airline acceptance of novel configuration requires early engagement

---

## 5. Deferred Decisions

The following decisions have been deferred pending further study or external inputs:

| Decision | Reason for Deferral | Target Date |
|----------|---------------------|-------------|
| Final baseline selection (A/B/C) | Awaiting detailed trade study results | Q1 2026 |
| LH₂ vs. GH₂ storage final choice | Supplier maturity assessment in progress | Q2 2026 |
| Number of distributed fans (8 vs. 10) | CFD validation and redundancy analysis | Q1 2026 |
| AI authority level (augmentation vs. full) | Regulatory framework clarity | Q3 2026 |
| Cabin configuration (2-3-2 vs. 2-4-2) | Mockup evaluation and egress analysis | Q2 2026 |
| Battery chemistry (Li-ion vs. solid-state) | Technology maturation timeline | Q4 2026 |

---

## 6. Document References

- [LC-11_0000-01 — Concept Overview](./LC-11_0000-01_Concept_Overview.md)
- [LC-11_0000-02 — Architecture Rationale](./LC-11_0000-02_Architecture_Rationale.md)
- [LC-11_0000-12 — Baseline A Definition](./LC-11_0000-12_BaselineA_Definition.md)
- [LC-11_0000-27 — Concept Decision Log](./LC-11_0000-27_Concept_Decision_Log.md)

---

## 7. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Architecture Board | Initial concept evolution log through Q4 2025 |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Architecture Board, Program Management, All Technical Leads
- **Next Review:** Monthly updates through MCR-1
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
