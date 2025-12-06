# LC-11_0000-10 — Performance Assumptions

**UTCS Node:** LC-11_0000-10  
**Document Type:** Performance Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Flight Sciences & Performance Team

---

## 1. Purpose

This document defines the aerodynamic, propulsive, and performance assumptions used for sizing and analysis of the AMPEL360 BWB Q100 Baseline A configuration.

---

## 2. Aerodynamic Performance

### 2.1 Lift-to-Drag Ratio (L/D)

| Condition | L/D | CL | Notes |
|-----------|-----|-----|-------|
| **Cruise (M=0.72, FL390)** | 21.0 | 0.48 | Design point |
| **Loiter (M=0.50, FL250)** | 23.5 | 0.65 | Reserve hold |
| **Climb (M=0.74, FL200)** | 18.0 | 0.55 | Average climb |
| **Approach (M=0.30, clean)** | 16.0 | 1.10 | Pre-landing |

**Comparison:**
- A320neo cruise L/D: ~18-19 (tube-and-wing)
- Q100 cruise L/D: ~21 (+11% improvement from BWB efficiency)

### 2.2 Drag Breakdown (Cruise Condition)

| Drag Component | CD | % Total Drag | Notes |
|----------------|-----|--------------|-------|
| **Zero-Lift Drag (CD0)** | 0.0160 | 70% | Skin friction + form drag |
| - Skin friction | 0.0120 | 52% | Wetted area = 706 m² |
| - Form drag | 0.0025 | 11% | Nacelles, excrescences |
| - Interference drag | 0.0015 | 7% | Minimal (integrated BWB) |
| **Induced Drag (CDi)** | 0.0069 | 30% | Lift-dependent |
| **Total Drag (CDtotal)** | 0.0229 | 100% | At CL = 0.48 |

**Span Efficiency:** e = 0.88 (excellent for BWB, near-elliptical loading)

### 2.3 Maximum Lift Coefficients

| Configuration | CLmax | Notes |
|---------------|-------|-------|
| **Clean (cruise)** | 1.20 | No flaps/slats |
| **Flaps 20° (takeoff)** | 1.85 | LE slats + TE flaps 20° |
| **Flaps 30° (approach)** | 2.15 | LE slats + TE flaps 30° |
| **Flaps 40° (landing)** | 2.40 | LE slats + TE flaps 40° |

**Stall Margin:** Operate at < 80% CLmax for buffet-free flight

### 2.4 Drag Polar (Parabolic Approximation)

**Cruise:**  
CD = CD0 + k × CL²  
CD = 0.0160 + 0.0298 × CL²

Where: k = 1 / (π × AR × e) = 1 / (π × 6.86 × 0.88) = 0.0298

**High-Lift (Flaps 40°):**  
CD = 0.080 + 0.0350 × CL²  
(Higher CD0 due to flap deflection and slot gaps)

---

## 3. Propulsion Performance

### 3.1 Fuel Cell System

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Rated power (continuous)** | 3,000 | kW | Cruise power |
| **Maximum power (short-term)** | 4,000 | kW | Climb, 10 min limit |
| **Power density** | 1.2 | kW/kg | System-level (Baseline A) |
| **Efficiency (cruise)** | 50% | % | Electrical / H₂ LHV |
| **Efficiency (peak power)** | 45% | % | Lower at high power |

**Fuel Consumption Rate (Cruise):**  
H₂ flow = 3,000 kW / (0.50 × 120 MJ/kg) = 3,000 / 60,000 = 0.05 kg/s = 180 kg/h

### 3.2 Electric Motor / Propeller

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Number of motors** | 8 | — | Distributed propulsion |
| **Power per motor (cruise)** | 375 | kW | 3,000 kW / 8 |
| **Power per motor (max)** | 625 | kW | 5,000 kW / 8 (with battery) |
| **Motor efficiency** | 96% | % | Electric motor |
| **Fan/propeller efficiency** | 88% | % | Includes BLI benefit |
| **Overall propulsive efficiency** | 84.5% | % | 0.96 × 0.88 |

**Thrust per Fan (Cruise, M=0.72, FL390):**  
Power = 375 kW  
Thrust = Power / (V × η) = 375,000 / (220 m/s × 0.845) ≈ 2,020 N per fan  
Total thrust (8 fans) = 16,160 N ≈ 16.2 kN

### 3.3 Battery System

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Capacity** | 1,000 | kWh | Green-E lithium-ion |
| **Peak power output** | 5,000 | kW | 10-minute duration |
| **Discharge rate** | 5C | — | 1,000 kWh in 12 min |
| **Charge rate (ground)** | 2C | — | 30-minute recharge |
| **Depth of discharge (normal)** | 80% | % | Extend battery life |
| **Round-trip efficiency** | 92% | % | Charge/discharge losses |

**Usage Profile:**
- **Takeoff:** 5,000 kW for 2 minutes (167 kWh, 17% capacity)
- **Climb:** 4,000 kW for 8 minutes (533 kWh, 53% capacity)
- **Cruise:** 0 kW (fuel cell only)
- **Descent/Landing:** 0 kW (regenerative braking potential, not baselined)

---

## 4. Takeoff Performance

### 4.1 Takeoff Assumptions

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Takeoff weight** | 65,000 | kg | MTOW (Baseline A) |
| **Thrust (all engines)** | 80 | kN | 8 fans @ 10 kN each (static, SL) |
| **Thrust (one engine out)** | 70 | kN | 7 fans operative |
| **CLmax (takeoff, flaps 20°)** | 1.85 | — | LE slats + TE flaps |
| **Takeoff speed (V2)** | 80 | m/s | 155 KIAS |
| **Field length (all engines)** | 1,800 | m | ISA, sea level |
| **Field length (OEI, FAR25)** | 2,000 | m | One engine inoperative case |

### 4.2 Takeoff Segments (CS-25)

1. **Ground roll:** Accelerate to VR (rotation speed) ≈ 75 m/s
2. **Rotation:** 3° pitch rate, 2 seconds to VLO (liftoff speed) ≈ 78 m/s
3. **Airborne:** Climb to 35 ft screen height at V2 = 80 m/s
4. **Climb gradient (OEI):** > 2.4% (CS-25 §25.121) → Achieved: 3.0%

---

## 5. Climb Performance

### 5.1 Climb Assumptions

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Climb power (fuel cell)** | 4,000 | kW | Maximum continuous |
| **Climb power (battery assist)** | 2,000 | kW | 8-minute duration |
| **Total climb power** | 6,000 | kW | FC + battery |
| **Climb speed** | M 0.74 | — | 250 KIAS / M0.74 transition |
| **Climb gradient (all engines)** | 18% | — | At sea level, MTOW |
| **Climb gradient (OEI)** | 3.0% | — | At 35 ft, MTOW (exceeds CS-25) |

### 5.2 Time to Climb

| Altitude Segment | Time (min) | Distance (nm) | Fuel (kg H₂) |
|------------------|------------|---------------|--------------|
| **SL → FL100** | 4 | 15 | 15 |
| **FL100 → FL200** | 5 | 20 | 20 |
| **FL200 → FL300** | 6 | 25 | 25 |
| **FL300 → FL390** | 8 | 35 | 35 |
| **Total (SL → FL390)** | 23 | 95 | 95 |

**Average Climb Rate:** 2,500 ft/min (initial), reducing to 500 ft/min (near ceiling)

---

## 6. Cruise Performance

### 6.1 Cruise Assumptions

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Cruise altitude** | FL390 | — | 39,000 ft (optimum) |
| **Cruise Mach** | 0.72 | — | M 0.70-0.75 operational range |
| **Cruise TAS** | 220 | m/s | 428 KTAS at FL390 |
| **Cruise lift coefficient** | 0.48 | — | Near L/Dmax |
| **Cruise L/D** | 21.0 | — | Aerodynamic efficiency |
| **Cruise thrust required** | 15.2 | kN | Drag × 1.0 (no wind) |
| **Cruise power required** | 3,340 | kW | Thrust × velocity / η |
| **Fuel cell power output** | 3,000 | kW | 90% of rated continuous |

### 6.2 Specific Range

**Specific Range (SR):** Distance per unit fuel  
SR = (V / SFC) × (L / D)

Where:
- V = 220 m/s (cruise speed)
- SFC = Specific fuel consumption = 1 / (η × LHV) = 1 / (0.50 × 120 MJ/kg) = 1/60 kg/MJ
- L/D = 21

SR = (220 / (1/60)) × 21 = 220 × 60 × 21 = 277,200 m/kg = 277 km/kg H₂  
SR = 149.7 nm/kg H₂

**Cruise Fuel Flow:** 0.05 kg/s = 180 kg/h H₂

---

## 7. Descent and Landing Performance

### 7.1 Descent

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Descent rate (typical)** | 2,000 | ft/min | Passenger comfort |
| **Descent speed** | M 0.72 / 250 KIAS | — | Transition at FL200 |
| **Descent power** | 500 | kW | Idle power, drag management |
| **Descent fuel** | Minimal | — | ~20 kg H₂ (30 min descent) |

### 7.2 Landing

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Landing weight (typical)** | 57,000 | kg | After 1,500 nm mission |
| **Landing speed (Vref)** | 70 | m/s | 136 KIAS (flaps 40°) |
| **Landing field length** | 1,600 | m | CS-25, sea level, dry runway |
| **Approach speed (Vapp)** | 75 | m/s | Vref + 5 kt (wind correction) |
| **Touchdown rate** | < 6 | ft/s | Target sink rate |

**Landing Distance Breakdown:**
1. **Airborne (50 ft → touchdown):** 600 m
2. **Ground roll (braking):** 1,000 m
3. **Total landing distance:** 1,600 m

---

## 8. Range-Payload Performance

### 8.1 Design Mission (1,500 nm)

| Mission Segment | Fuel (kg H₂) | Distance (nm) | Time (min) |
|-----------------|--------------|---------------|------------|
| **Taxi out** | 5 | — | 10 |
| **Takeoff** | 10 | — | 2 |
| **Climb (SL → FL390)** | 95 | 95 | 23 |
| **Cruise (FL390)** | 1,375 | 1,405 | 191 |
| **Descent** | 20 | — | 30 |
| **Approach/Land** | 5 | — | 10 |
| **Taxi in** | 10 | — | 10 |
| **Subtotal (Mission)** | **1,520** | **1,500** | **276** |
| **Reserve (200 nm + 30 min)** | 400 | 200 | 60 |
| **Total Fuel** | **1,920** | **1,700** | **336** |

**Payload:** 12,000 kg (100 pax + baggage)  
**Takeoff Weight:** 65,000 kg (38,000 OEW + 12,000 payload + 15,000 fuel)

### 8.2 Range-Payload Curve

| Range (nm) | Payload (kg) | Fuel (kg H₂) | MTOW (kg) | Notes |
|------------|--------------|--------------|-----------|-------|
| 500 | 14,000 | 750 | 52,750 | Short-haul, max payload |
| 1,000 | 13,000 | 1,200 | 52,200 | Regional optimum |
| **1,500** | **12,000** | **2,000** | **52,000** | **Design point** |
| 1,800 | 10,000 | 2,300 | 50,300 | Reduced payload |
| 2,000 | 8,500 | 2,500 | 49,000 | Maximum ferry range |

**Trade-off:** Range vs. payload constrained by MTOW (65,000 kg) and MZFW (52,000 kg).

---

## 9. Environmental Performance

### 9.1 Emissions

**Operational Emissions (Cruise):**
- **CO₂:** 0 kg (hydrogen combustion produces only H₂O)
- **NOx:** 0 kg (fuel cells do not produce nitrogen oxides)
- **Particulates:** 0 kg (no combustion byproducts)
- **Water vapor:** ~18 kg H₂O per kg H₂ consumed

**Lifecycle Emissions:**
- Dependent on hydrogen production method (green H₂ target: 0 gCO₂/MJ)

### 9.2 Noise

| Condition | Noise Level (EPNdB) | Location | Notes |
|-----------|---------------------|----------|-------|
| **Takeoff** | 85 | Sideline (450 m) | Distributed propulsion benefit |
| **Approach** | 90 | 2,000 m from threshold | Upper surface fans shielded |
| **Flyover** | 88 | 6,500 m from brake release | |

**Target:** Chapter 14 cumulative < 265 EPNdB (−10 dB below Chapter 4 baseline)

---

## 10. Sensitivity Analysis

### 10.1 Key Sensitivities

| Parameter | Variation | Range Impact | Notes |
|-----------|-----------|--------------|-------|
| **L/D (cruise)** | ±5% | ±140 nm | Aerodynamic efficiency |
| **Fuel cell efficiency** | ±5% | ±150 nm | Propulsion efficiency |
| **OEW** | ±1,000 kg | ±100 nm | Weight growth |
| **Cruise altitude** | ±2,000 ft | ±50 nm | Altitude optimization |
| **Cruise Mach** | ±0.02 | ±30 nm | Speed vs. efficiency trade |

---

## 11. Performance Margins

| Performance Parameter | Requirement | Achieved | Margin |
|-----------------------|-------------|----------|--------|
| **Takeoff field length** | < 2,000 m | 1,800 m | +200 m |
| **Landing field length** | < 1,800 m | 1,600 m | +200 m |
| **Climb gradient (OEI)** | > 2.4% | 3.0% | +0.6% |
| **Range (design mission)** | 1,500 nm | 1,560 nm | +60 nm |
| **Service ceiling** | > FL350 | FL410 | +6,000 ft |

---

## 12. References

- [LC-11_0000-08 — Mission and Payload Assumptions](./LC-11_0000-08_Mission_Payload_Assumptions.md)
- [LC-11_0000-09 — Preliminary Mass Breakdown](./LC-11_0000-09_PMB0_Preliminary_Mass_Breakdown.md)
- [LC-11_0000-11 — Energy Sizing Preliminary](./LC-11_0000-11_Energy_Sizing_Prelim.md)

---

## 13. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Flight Sciences & Performance Team | Initial performance assumptions |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Flight Sciences, Propulsion, All Engineering Teams
- **Next Review:** Q1 2026
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
