# LC-11_0010-08 — Mission and Payload Assumptions

**UTCS Node:** LC-11_0010-08  
**Document Type:** Design Requirements  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Flight Sciences & Performance Team

---

## 1. Purpose

This document defines the mission profiles and payload assumptions for the AMPEL360 BWB Q100 concept, establishing the foundation for performance sizing and analysis.

---

## 2. Design Mission

### 2.1 Primary Mission Profile

**Mission Type:** Regional/Short-haul passenger transport

| Phase | Description | Distance/Time | Altitude | Speed |
|-------|-------------|---------------|----------|-------|
| **Taxi Out** | Ground operations | 10 min | Ground | — |
| **Takeoff** | Runway departure | 2,000 m | SL to 1,500 ft | V2+10 kt |
| **Climb** | Ascent to cruise | — | 1,500 ft → FL390 | 250 KIAS / M 0.74 |
| **Cruise** | Constant altitude | 1,500 nm | FL390 | M 0.72 |
| **Descent** | Descent to approach | — | FL390 → 1,500 ft | M 0.72 / 250 KIAS |
| **Approach/Land** | Landing sequence | 20 nm | 1,500 ft → Ground | 180-140 KIAS |
| **Taxi In** | Ground operations | 10 min | Ground | — |
| **Reserve** | Diversion + hold | 200 nm + 30 min | FL250 | M 0.70 |

**Total Design Range:** 1,500 nm (cruise) + 200 nm (reserve) = 1,700 nm fuel capacity

### 2.2 Mission Assumptions

- **Takeoff field length:** 2,000 m (6,562 ft) at MTOW, ISA, sea level
- **Landing field length:** 1,800 m (5,905 ft) at MLW, ISA, sea level
- **Cruise altitude:** FL390 (39,000 ft) optimum
- **Cruise Mach:** 0.72 (target), range 0.70-0.75
- **Reserves:** ICAO Annex 6 (200 nm diversion + 30 min hold at 1,500 ft)

---

## 3. Payload Assumptions

### 3.1 Passenger Payload

**Design Passenger Capacity:** 100 passengers (2-3-2 configuration)

| Item | Value | Units | Notes |
|------|-------|-------|-------|
| Passenger count | 100 | pax | Standard configuration |
| Passenger weight (avg) | 95 | kg/pax | Including carry-on (EASA std) |
| **Total passenger weight** | **9,500** | **kg** | |

**Alternative Configuration:** 120 passengers (2-4-2 high-density)
- Total passenger weight: 120 × 95 = 11,400 kg

### 3.2 Baggage Payload

**Checked Baggage:**
- **Weight per passenger:** 20 kg (standard allowance)
- **Total checked baggage (100 pax):** 2,000 kg
- **Volume:** ~25 m³ (underbelly cargo hold)

**Carry-On Baggage:**
- **Weight per passenger:** 10 kg (included in 95 kg passenger weight)
- **Total carry-on (100 pax):** 1,000 kg (stowed in overhead bins)

### 3.3 Cargo Payload

**Additional Cargo Capacity:**
- **Volume available:** ~10 m³ (after baggage)
- **Maximum additional cargo:** 500-1,000 kg (density dependent)

### 3.4 Total Payload (Design Mission)

| Payload Component | Weight (kg) | Notes |
|-------------------|-------------|-------|
| Passengers (100 × 95 kg) | 9,500 | Including carry-on |
| Checked baggage (100 × 20 kg) | 2,000 | In cargo hold |
| Additional cargo | 500 | Optional revenue cargo |
| **Total Payload** | **12,000** | **Design payload** |

---

## 4. Alternative Mission Profiles

### 4.1 Short-Haul Mission (500 nm)

**Use Case:** Regional shuttle, high-frequency operations

- **Cruise range:** 500 nm
- **Payload:** 120 pax (high-density) = 11,400 kg
- **Reduced fuel:** ~50% of design fuel load
- **Advantage:** Higher payload fraction, faster turnaround

### 4.2 Maximum Range Mission (2,000 nm)

**Use Case:** Transcontinental, premium routes

- **Cruise range:** 1,800 nm + 200 nm reserve = 2,000 nm total
- **Payload:** 85 pax (reduced for max range)
- **Full fuel load:** Maximum H₂ capacity

### 4.3 Cargo Mission

**Use Case:** All-cargo freighter variant

- **Payload:** 12,000-15,000 kg cargo (pallets/containers)
- **Range:** 1,200-1,500 nm (cargo-dependent)
- **Configuration:** Seats removed, cargo handling system installed

---

## 5. Operational Envelope

### 5.1 Altitude Envelope

| Condition | Altitude | Notes |
|-----------|----------|-------|
| Maximum operating altitude | FL410 (41,000 ft) | Certified ceiling |
| Optimum cruise altitude | FL390 (39,000 ft) | Best range |
| Service ceiling (one engine out) | FL250 (25,000 ft) | Safety requirement |
| Minimum safe altitude | Per ATC/terrain | Regulatory |

### 5.2 Speed Envelope

| Speed | Value | Notes |
|-------|-------|-------|
| VMO (Max operating speed) | 350 KIAS | Below 10,000 ft |
| MMO (Max operating Mach) | M 0.80 | High-altitude limit |
| Cruise speed (typical) | M 0.72 | Optimum efficiency |
| Design cruise speed range | M 0.70 - 0.75 | Operational flexibility |
| Approach speed (Vref) | 140-150 KIAS | Configuration dependent |

### 5.3 Weight Envelope

| Weight Category | Value (kg) | Notes |
|-----------------|------------|-------|
| MTOW (Max Takeoff Weight) | 65,000 | Baseline A (preliminary) |
| MLW (Max Landing Weight) | 57,000 | ~88% MTOW |
| MZFW (Max Zero Fuel Weight) | 52,000 | Structure + payload limit |
| OEW (Operating Empty Weight) | 38,000 | Estimated (Baseline A) |

---

## 6. Environmental Conditions

### 6.1 Atmospheric Conditions

**Standard Design Conditions:**
- **ISA (International Standard Atmosphere):** 15°C at sea level
- **ISA +10°C:** Hot day performance
- **ISA -10°C:** Cold day performance (better)

**Altitude Performance:**
- **Cruise density altitude:** FL390 (39,000 ft) ISA
- **Cruise temperature:** -56.5°C (ISA at FL390)

### 6.2 Airport Conditions

**Runway Requirements:**
- **Length:** 2,000 m (takeoff), 1,800 m (landing) minimum
- **Surface:** Paved (concrete or asphalt)
- **Width:** 45 m (ICAO Code C standard)
- **Pavement strength:** PCN 60 or greater

**Wind Conditions:**
- **Crosswind limit:** 35 knots (demonstrated)
- **Tailwind limit:** 15 knots (takeoff/landing)

---

## 7. Fuel/Energy Assumptions

### 7.1 Hydrogen Fuel

**Fuel Type:** Compressed gaseous hydrogen (GH₂) at 350 bar (Baseline A)

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| Design mission fuel | 2,000 | kg H₂ | 1,500 nm cruise + reserves |
| Reserve fuel | 400 | kg H₂ | 200 nm diversion + 30 min hold |
| Total fuel capacity | 2,500 | kg H₂ | Maximum usable |
| Hydrogen LHV | 120 | MJ/kg | Lower heating value |
| Total energy (max fuel) | 300,000 | MJ | 83,333 kWh equivalent |

**Alternate Fuel (Future):**
- Liquid hydrogen (LH₂): Higher volumetric density, requires cryogenic storage

### 7.2 Battery (Green-E)

**Battery Function:** Peak power (takeoff/climb), emergency backup

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| Battery capacity | 1,000 | kWh | Green-E lithium-ion |
| Battery weight | 2,500 | kg | 400 Wh/kg (Baseline A) |
| Peak power output | 5,000 | kW | 10C discharge (10 minutes) |
| Recharge time (ground) | 30 | minutes | 2C charge rate |

### 7.3 Fuel Cell System

**System Type:** PEM (Proton Exchange Membrane) fuel cell

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| Fuel cell power (cruise) | 3,000 | kW | Continuous rated power |
| Fuel cell power (max) | 4,000 | kW | Short-term peak (climb) |
| Power density | 1.2 | kW/kg | System-level (Baseline A) |
| Fuel cell system weight | 3,333 | kg | Includes stacks, BoP, cooling |
| Efficiency (cruise) | 50% | % | Electrical output / H₂ LHV |

---

## 8. Performance Targets

### 8.1 Range-Payload Capability

**Design Point:** 1,500 nm with 12,000 kg payload

**Range-Payload Curve (Preliminary):**

| Range (nm) | Payload (kg) | Notes |
|------------|--------------|-------|
| 500 | 14,000 | Max structural payload (high-density) |
| 1,000 | 13,000 | Short-haul optimum |
| 1,500 | 12,000 | **Design mission** |
| 1,800 | 10,000 | Reduced payload for range |
| 2,000 | 8,500 | Maximum ferry range |

### 8.2 Efficiency Targets

**Energy per Passenger-Kilometer:**
- **Target:** 0.45 MJ/pax-km (30% better than A320neo baseline ~0.64 MJ/pax-km)
- **Equivalent (conventional fuel):** ~35% reduction in fuel burn per pax-km

**Block Fuel (Design Mission, 1,500 nm):**
- **Hydrogen:** 2,000 kg
- **Energy:** 240,000 MJ (67,000 kWh)
- **Per passenger:** 2,400 MJ/pax (100 pax)
- **Per pax-km:** 0.43 MJ/pax-km (meets target)

---

## 9. Operational Assumptions

### 9.1 Daily Utilization

**Target:** 8-10 flight hours per day (regional shuttle operations)

**Typical Day:**
- Morning: 2 rotations (4 flights), 4 flight hours
- Afternoon: 2 rotations (4 flights), 4 flight hours
- Evening: 1 rotation (2 flights), 2 flight hours
- **Total:** 5 rotations (10 flights), 10 flight hours

**Ground Time:**
- Turnaround: 30-45 minutes (standard gate)
- Overnight maintenance: 6-8 hours

### 9.2 Route Structure

**Primary Route Types:**
- Regional hub-to-hub: 500-800 nm (high frequency)
- Transcontinental short-haul: 1,000-1,500 nm (medium frequency)
- Island/coastal routes: 300-1,000 nm (environmental priority)

**Example Routes (Europe):**
- London - Paris: 215 nm
- Frankfurt - Rome: 600 nm
- Madrid - Berlin: 950 nm
- London - Athens: 1,500 nm (design mission)

---

## 10. Certification Basis

### 10.1 Airworthiness Standards

- **CS-25 / FAR Part 25:** Large aircraft certification
- **EASA Special Condition:** Hydrogen-powered aircraft (expected 2026)
- **FAA Policy:** Equivalent safety findings for H₂ propulsion

### 10.2 Performance Requirements

**CS-25 Key Requirements:**
- §25.105: Takeoff (all-engines, one-engine-out)
- §25.111: Takeoff path
- §25.121: Climb (various configurations)
- §25.125: Landing
- §25.143: Controllability and maneuverability
- §25.1309: Equipment and systems (fail-safe)

---

## 11. Assumptions Register

| Assumption | Value | Confidence | Risk | Validation Plan |
|------------|-------|------------|------|-----------------|
| Fuel cell power density | 1.2 kW/kg | Medium | Medium | Supplier engagement, tech roadmap |
| Battery energy density | 400 Wh/kg | High | Low | Green-E validated |
| L/D (cruise) | 21 | Medium | Medium | CFD validation, wind tunnel |
| Hydrogen availability | Yes (2030) | Medium | High | Infrastructure roadmap |
| Passenger acceptance | Positive | Low | High | Market surveys, public outreach |

---

## 12. References

- [LC-11_0010-01 — Concept Overview](./LC-11_0010-01_Concept_Overview.md)
- [LC-11_0010-09 — Preliminary Mass Breakdown](./LC-11_0010-09_PMB0_Preliminary_Mass_Breakdown.md)
- [LC-11_0010-10 — Performance Assumptions](./LC-11_0010-10_Performance_Assumptions.md)
- [LC-11_0010-11 — Energy Sizing Preliminary](./LC-11_0010-11_Energy_Sizing_Prelim.md)

---

## 13. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Flight Sciences & Performance Team | Initial mission and payload assumptions |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Flight Sciences, Propulsion, Systems Engineering Teams
- **Next Review:** Q1 2026
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
