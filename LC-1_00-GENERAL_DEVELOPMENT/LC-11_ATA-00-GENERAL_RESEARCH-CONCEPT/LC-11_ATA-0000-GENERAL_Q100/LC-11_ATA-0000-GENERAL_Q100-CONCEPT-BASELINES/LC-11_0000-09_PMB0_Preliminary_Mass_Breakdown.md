# LC-11_0000-09 — PMB0 Preliminary Mass Breakdown

**UTCS Node:** LC-11_0000-09  
**Document Type:** Mass Budget  
**Status:** Draft  
**Version:** 1.0 (PMB0 - First Estimate)  
**Date:** 2025-12-05  
**Owner:** Weights & Balance Team

---

## 1. Purpose

This document provides the preliminary mass breakdown (PMB0) for the AMPEL360 BWB Q100 Baseline A configuration, establishing the foundational weight budget for design and performance analysis.

---

## 2. Mass Summary (Baseline A)

| Category | Mass (kg) | % OEW | % MTOW | Notes |
|----------|-----------|-------|--------|-------|
| **Operating Empty Weight (OEW)** | **38,000** | **100%** | **58.5%** | Aircraft ready for ops |
| **Payload** | **12,000** | **31.6%** | **18.5%** | 100 pax + baggage |
| **Fuel (Hydrogen + Battery)** | **15,000** | **39.5%** | **23.1%** | Mission + reserves |
| **Maximum Takeoff Weight (MTOW)** | **65,000** | **171%** | **100%** | Design limit |

---

## 3. Operating Empty Weight (OEW) Breakdown

### 3.1 Structure (15,200 kg, 40.0% OEW)

| Component | Mass (kg) | Method | Notes |
|-----------|-----------|--------|-------|
| **Wing Structure** | 8,500 | Parametric | CFRP primary structure |
| - Wing box (spars, ribs, skins) | 6,000 | | Integrated BWB planform |
| - Control surfaces (elevons, flaps) | 1,200 | | Including actuators |
| - Winglets / vertical stabilizers | 800 | | Including rudders |
| - Secondary structure | 500 | | Fairings, access panels |
| **Fuselage/Centerbody** | 4,500 | Parametric | Non-circular pressure vessel |
| - Pressure shell | 3,000 | | CFRP frames, stringers |
| - Floor structure | 800 | | Cabin + cargo floors |
| - Doors and hatches | 400 | | 6 passenger doors + cargo |
| - Interior structure | 300 | | Partitions, ceiling |
| **Landing Gear** | 1,800 | Mass fraction | 2.8% MTOW |
| - Nose gear | 400 | | Steerable, dual-wheel |
| - Main gear (2 units) | 1,400 | | Dual-bogie, 4 wheels total |
| **Engine/Nacelle Structure** | 400 | Unit weight | 8 nacelles @ 50 kg each |

### 3.2 Propulsion (8,833 kg, 23.2% OEW)

| Component | Mass (kg) | Method | Notes |
|-----------|-----------|--------|-------|
| **Fuel Cell System** | 3,333 | Power/density | 4,000 kW / 1.2 kW/kg |
| - Fuel cell stacks | 2,000 | | PEM stacks |
| - Balance of plant (BoP) | 1,000 | | Pumps, compressors, valves |
| - Thermal management | 333 | | Cooling loops, heat exchangers |
| **Electric Motors (8 units)** | 800 | Unit weight | 100 kg each (500 kW) |
| **Power Electronics** | 600 | | Inverters, controllers (8 units) |
| **Electrical Distribution** | 1,600 | System weight | High-voltage DC cables, bus bars |
| **Propellers/Fans (8 units)** | 400 | Unit weight | 50 kg each (1.2 m diameter) |
| **Battery System (Green-E)** | 2,500 | Energy/density | 1,000 kWh / 400 Wh/kg |
| - Battery cells | 2,100 | | Lithium-ion cells |
| - Battery management system (BMS) | 200 | | Monitoring, cooling |
| - Battery enclosure | 200 | | Fire suppression, mounts |
| **Exhaust/Intake** | 100 | Estimate | Minimal (electric propulsion) |

### 3.3 Hydrogen Storage (3,500 kg, 9.2% OEW)

| Component | Mass (kg) | Method | Notes |
|-----------|-----------|--------|-------|
| **Hydrogen Tanks (COPV)** | 2,800 | Gravimetric | 350 bar, multiple tanks |
| - Tank shells | 2,400 | | Carbon-fiber overwrapped |
| - Tank fittings and valves | 400 | | Fill/vent connections |
| **Fuel System** | 700 | Estimate | Plumbing, distribution |
| - Piping and manifolds | 300 | | Stainless steel/composite |
| - Pumps and regulators | 150 | | Pressure management |
| - Sensors and monitoring | 100 | | Leak detection, level |
| - Fire suppression system | 150 | | Inerting, detection, extinguishers |

### 3.4 Systems (6,800 kg, 17.9% OEW)

| System | Mass (kg) | Notes |
|--------|-----------|-------|
| **Flight Control System** | 900 | Fly-by-wire, AI-augmented |
| - Actuators (control surfaces) | 500 | Hydraulic + electric backup |
| - Flight control computers | 200 | Redundant AI processors |
| - Sensors (air data, IMU, GPS) | 200 | |
| **Avionics** | 800 | Communication, navigation, displays |
| - Cockpit displays and controls | 300 | Dual pilot stations |
| - Radios and transponders | 200 | VHF, HF, SATCOM |
| - Navigation aids | 200 | ILS, GPS, INS |
| - AI systems | 100 | Neural network processors |
| **Electrical System** | 1,500 | Power generation, distribution |
| - Generators (fuel cell integrated) | 0 | Included in propulsion |
| - APU (auxiliary power unit) | 400 | Ground ops, emergency backup |
| - Batteries (ship's power, 24V/28V) | 200 | Non-propulsion electrical |
| - Wiring and distribution | 900 | Cables, circuit breakers |
| **Hydraulics** | 400 | Backup for flight controls |
| - Hydraulic pumps | 100 | Electric-driven |
| - Reservoirs and accumulators | 100 | |
| - Plumbing | 200 | Lines, valves |
| **Environmental Control System (ECS)** | 1,800 | Cabin pressurization, air conditioning |
| - Air conditioning packs | 600 | Vapor cycle, integrated with FC cooling |
| - Cabin pressure control | 300 | Outflow valves, controllers |
| - Ventilation and ducting | 500 | Distribution to cabin |
| - Oxygen system | 200 | Emergency passenger + crew |
| - Waste system (lavatories) | 200 | Tanks, plumbing |
| **Anti-Ice / De-Ice** | 500 | Wing and engine inlet protection |
| **APU and Ground Equipment** | 600 | Auxiliary power unit, tow fittings |
| **Miscellaneous Systems** | 300 | Fire detection/suppression, lighting |

### 3.5 Furnishings & Equipment (3,667 kg, 9.6% OEW)

| Component | Mass (kg) | Notes |
|-----------|-----------|-------|
| **Seats (100 pax)** | 1,200 | 12 kg/seat (economy) |
| **Cabin Interior** | 1,500 | Panels, overhead bins, partitions |
| - Sidewall panels and ceiling | 600 | Lightweight composites |
| - Overhead bins | 400 | Stowage for carry-ons |
| - Lavatories (4 units) | 300 | Modules @ 75 kg each |
| - Galleys and carts | 200 | Service equipment |
| **Cargo Handling Equipment** | 200 | Nets, tie-downs |
| **Emergency Equipment** | 300 | Life rafts, slides, ELT |
| **Cockpit Equipment** | 150 | Seats, controls |
| **Passenger Service Items** | 317 | IFE, blankets, magazines |

---

## 4. Payload Breakdown (12,000 kg)

| Item | Mass (kg) | Notes |
|------|-----------|-------|
| **Passengers (100 pax)** | 9,500 | 95 kg/pax (including carry-on) |
| **Checked Baggage** | 2,000 | 20 kg/pax |
| **Additional Cargo** | 500 | Revenue cargo (optional) |
| **Total Payload** | 12,000 | |

---

## 5. Fuel/Energy Breakdown (15,000 kg)

| Item | Mass (kg) | Energy (MJ) | Notes |
|------|-----------|-------------|-------|
| **Hydrogen (usable)** | 2,000 | 240,000 | Design mission fuel |
| **Hydrogen (reserves)** | 400 | 48,000 | 200 nm diversion + 30 min |
| **Hydrogen (trapped/unusable)** | 100 | 12,000 | Tank residuals |
| **Battery (Green-E)** | 2,500 | 3,600 | 1,000 kWh = 3,600 MJ |
| **Total Fuel/Energy** | 15,000 | 303,600 | |

**Note:** Battery weight is included in Propulsion section (OEW), but energy content counted here for mission analysis.

---

## 6. Weight Budget Summary

### 6.1 Design Weights

| Weight Category | Mass (kg) | Definition |
|-----------------|-----------|------------|
| **Manufacturer's Empty Weight (MEW)** | 36,200 | Structure + propulsion + systems |
| **Operating Items** | 1,800 | Crew, catering, potable water |
| **Operating Empty Weight (OEW)** | 38,000 | MEW + operating items |
| **Payload** | 12,000 | Passengers + baggage + cargo |
| **Zero Fuel Weight (ZFW)** | 50,000 | OEW + payload |
| **Fuel (Mission + Reserves)** | 15,000 | H₂ + battery energy |
| **Takeoff Weight** | 65,000 | ZFW + fuel |
| **Maximum Takeoff Weight (MTOW)** | 65,000 | Structural limit |
| **Maximum Landing Weight (MLW)** | 57,000 | ~88% MTOW |
| **Maximum Zero Fuel Weight (MZFW)** | 52,000 | Structural limit |

### 6.2 Mass Fractions

| Fraction | Value | Notes |
|----------|-------|-------|
| **OEW / MTOW** | 0.585 | Competitive with conventional |
| **Payload / MTOW** | 0.185 | Typical for regional aircraft |
| **Fuel / MTOW** | 0.231 | H₂ + battery |

---

## 7. Center of Gravity (CG) Envelope

### 7.1 CG Locations (Preliminary)

| Condition | X-CG (% MAC) | Mass (kg) | Notes |
|-----------|--------------|-----------|-------|
| **OEW** | 26% | 38,000 | Empty, no payload/fuel |
| **Forward CG (critical)** | 15% | 65,000 | Full H₂ forward, light pax aft |
| **Aft CG (critical)** | 35% | 65,000 | Light H₂, heavy pax aft |
| **Design cruise CG** | 25% | 58,000 | Mid-mission, typical loading |

**CG Range:** 15% to 35% MAC (20% range)  
**Target Cruise CG:** 25% MAC (optimal for trim and stability)

### 7.2 CG Management Strategy

- **Hydrogen tank distribution:** Multiple tanks enable CG control via selective fueling
- **Passenger seating:** Load planning to balance left/right and forward/aft
- **Cargo placement:** Strategic loading to fine-tune CG

---

## 8. Comparison to Baseline B and C

| Parameter | Baseline A | Baseline B | Baseline C | Units |
|-----------|------------|------------|------------|-------|
| **MTOW** | 65,000 | 62,000 | 59,000 | kg |
| **OEW** | 38,000 | 36,000 | 34,000 | kg |
| **Fuel cell system** | 3,333 | 2,667 | 2,222 | kg |
| **Fuel cell power density** | 1.2 | 1.5 | 1.8 | kW/kg |
| **Battery system** | 2,500 | 2,500 | 2,000 | kg |
| **Battery energy density** | 400 | 400 | 450 | Wh/kg |
| **H₂ fuel (mission)** | 2,000 | 1,900 | 1,800 | kg |

**Key Driver:** Fuel cell power density improvement (Baseline A → B → C) reduces system weight and enables MTOW reduction.

---

## 9. Uncertainty and Margin

### 9.1 Mass Growth Allowances

| Component | Baseline Mass (kg) | Growth Allowance (%) | Margin (kg) |
|-----------|--------------------|----------------------|-------------|
| Structure | 15,200 | 10% | 1,520 |
| Propulsion | 8,833 | 15% | 1,325 |
| H₂ storage | 3,500 | 10% | 350 |
| Systems | 6,800 | 12% | 816 |
| Furnishings | 3,667 | 5% | 183 |
| **Total** | **38,000** | **~12%** | **4,194** |

**Mass Margin (PMB0):** +4,194 kg (~11% of OEW)  
**MTOW with margin:** 69,194 kg

**Strategy:** Maintain 10-15% margin through preliminary design, reduce to 5% by CDR.

### 9.2 Confidence Levels

| Weight Group | Confidence | Basis |
|--------------|------------|-------|
| Structure | Medium | Parametric models, BWB experience limited |
| Propulsion (fuel cell) | Low | Technology maturity, supplier data pending |
| Propulsion (motors, batteries) | High | Established automotive/aerospace data |
| H₂ storage | Medium | COPV technology mature, integration new |
| Systems | High | Conventional systems, well-understood |
| Furnishings | High | Standard equipment |

---

## 10. Mass Reduction Opportunities

1. **Advanced composites:** Out-of-autoclave (OOA) processes reduce manufacturing defects, thinner laminates
2. **Fuel cell technology maturation:** 1.5+ kW/kg by 2028 saves ~700 kg (Baseline A → B)
3. **Electrical system optimization:** High-voltage DC (800V+) reduces cable weight ~200 kg
4. **Integrated thermal management:** Combined ECS + fuel cell cooling saves ~300 kg
5. **Additive manufacturing:** 3D-printed brackets, fittings reduce weight ~100 kg

**Total potential savings:** ~1,300 kg (3.4% OEW reduction)

---

## 11. References

- [LC-11_0000-08 — Mission and Payload Assumptions](./LC-11_0000-08_Mission_Payload_Assumptions.md)
- [LC-11_0000-10 — Performance Assumptions](./LC-11_0000-10_Performance_Assumptions.md)
- [LC-11_0000-12 — Baseline A Definition](./LC-11_0000-12_BaselineA_Definition.md)

---

## 12. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| PMB0 v1.0 | 2025-12-05 | Weights & Balance Team | Initial preliminary mass breakdown |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** All Engineering Teams, Program Management
- **Next Review:** Q1 2026 (PMB1 after detailed design iteration)
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
