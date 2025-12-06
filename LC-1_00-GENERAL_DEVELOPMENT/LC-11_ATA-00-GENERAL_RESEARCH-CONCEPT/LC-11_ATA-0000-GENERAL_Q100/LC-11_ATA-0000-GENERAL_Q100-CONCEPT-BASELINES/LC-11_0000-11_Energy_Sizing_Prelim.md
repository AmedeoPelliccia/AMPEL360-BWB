# LC-11_0000-11 — Energy Sizing Preliminary

**UTCS Node:** LC-11_0000-11  
**Document Type:** Energy System Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Energy Systems & Propulsion Team

---

## 1. Purpose

This document defines the preliminary energy sizing for the AMPEL360 BWB Q100, including hydrogen fuel capacity, battery energy storage, fuel cell power requirements, and integrated energy management strategy.

---

## 2. Energy System Architecture

### 2.1 Hybrid Energy Configuration

**Primary Energy Source:** Hydrogen (H₂) via fuel cells  
**Secondary Energy Source:** Green-E lithium-ion batteries  
**Architecture Type:** Series hybrid (fuel cell → electricity → motors)

```
[H₂ Tanks] → [Fuel Cell] → [DC Bus] → [Inverters] → [Motors/Fans]
                              ↑  ↓
                          [Battery Pack]
```

### 2.2 Power Split Strategy

| Flight Phase | Fuel Cell Power | Battery Power | Total Power | Notes |
|--------------|-----------------|---------------|-------------|-------|
| **Ground/Taxi** | 200 kW | 0 kW | 200 kW | APU-like operation |
| **Takeoff** | 4,000 kW | 5,000 kW | 9,000 kW | Maximum combined power |
| **Climb** | 4,000 kW | 2,000 kW | 6,000 kW | Battery assists FC |
| **Cruise** | 3,000 kW | 0 kW | 3,000 kW | FC only, battery recharge |
| **Descent** | 500 kW | 0 kW | 500 kW | Idle power |
| **Approach/Land** | 2,000 kW | 0 kW | 2,000 kW | Go-around capability |

---

## 3. Hydrogen Energy System

### 3.1 Hydrogen Fuel Requirements

**Design Mission Energy:**

| Mission Segment | Duration (min) | Power (kW) | Energy (MJ) | H₂ Fuel (kg) |
|-----------------|----------------|------------|-------------|--------------|
| Taxi out | 10 | 200 | 120 | 2 |
| Takeoff | 2 | 7,000 | 840 | 14 |
| Climb | 23 | 5,000 | 6,900 | 115 |
| Cruise | 191 | 3,000 | 34,380 | 573 |
| Descent | 30 | 500 | 900 | 15 |
| Approach/Land | 10 | 1,000 | 600 | 10 |
| Taxi in | 10 | 200 | 120 | 2 |
| **Mission Total** | **276** | **—** | **43,860** | **731** |
| **Reserve (200nm+30min)** | 90 | 2,500 | 13,500 | 225 |
| **Contingency (5%)** | — | — | 2,868 | 48 |
| **Total H₂ Required** | **366** | **—** | **60,228** | **1,004** |

**Fuel Cell Efficiency:** 50% (cruise), 45% (high power)  
**H₂ LHV:** 120 MJ/kg

**Total Hydrogen Fuel Load:** 
- Mission + reserves: 1,004 kg
- Trapped/unusable: 100 kg (10%)
- **Total H₂ capacity: 1,100 kg** (conservative estimate)

**Note:** Baseline A design carries 2,500 kg H₂ total capacity for extended range missions up to 2,000 nm.

### 3.2 Hydrogen Storage System

**Storage Technology:** Compressed Gaseous Hydrogen (GH₂), Type IV COPV tanks

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Storage pressure** | 350 | bar | 5,075 psi |
| **Storage temperature** | Ambient | °C | No cryogenic cooling |
| **Tank configuration** | Multiple tanks | — | 6-8 tanks distributed |
| **Total H₂ capacity** | 2,500 | kg | Maximum usable |
| **Tank volume (total)** | ~40 | m³ | @ 350 bar, 23.7 kg/m³ |
| **Gravimetric efficiency** | 5.5% | % | H₂ mass / (H₂ + tank mass) |
| **Tank system mass** | 2,800 | kg | COPV tanks + fittings |

**Tank Arrangement:**
- Located in aft centerbody (behind cabin pressure bulkhead)
- Multiple tanks enable CG management via selective fueling/consumption
- Safety separation: > 1.0 m from cabin pressure vessel
- Ventilation: Dedicated H₂ detection and venting system

### 3.3 Alternative: Liquid Hydrogen (LH₂)

**Future Option (Baseline C):**

| Parameter | GH₂ (350 bar) | LH₂ (Cryogenic) | Advantage |
|-----------|---------------|-----------------|-----------|
| Storage density | 23.7 kg/m³ | 70.8 kg/m³ | LH₂: 3× denser |
| Storage volume | 40 m³ | 13.5 m³ | LH₂: ~70% less volume |
| Tank mass | 2,800 kg | 1,800 kg | LH₂: ~35% lighter |
| Complexity | Low | High (cryogenic) | GH₂: simpler |
| Boil-off | None | 1-3%/day | GH₂: no losses |

**Decision:** GH₂ for Baseline A (lower risk), LH₂ option for Baseline C (technology maturation)

---

## 4. Fuel Cell System Sizing

### 4.1 Power Requirements

**Peak Power:** 4,000 kW (continuous max, climb/go-around)  
**Cruise Power:** 3,000 kW (typical cruise at FL390, M0.72)  
**Design Point:** 4,000 kW continuous (enables margin)

### 4.2 Fuel Cell Specifications

**Technology:** PEM (Proton Exchange Membrane) Fuel Cell

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Rated power (continuous)** | 4,000 | kW | Maximum continuous |
| **Power density** | 1.2 | kW/kg | System-level (Baseline A) |
| **Fuel cell system mass** | 3,333 | kg | Stacks + BoP + cooling |
| **Efficiency (nominal)** | 50% | % | @ 3,000 kW output |
| **Efficiency (peak)** | 45% | % | @ 4,000 kW output |
| **Operating temperature** | 80 | °C | PEM typical |
| **Coolant** | Water-glycol | — | Liquid cooling |

**Fuel Cell Stack:**
- Modular design: 10-20 stacks in series/parallel
- Individual stack power: 200-400 kW
- Redundancy: N+1 configuration (can lose 1 stack and continue safe flight)

### 4.3 Balance of Plant (BoP)

| Component | Mass (kg) | Power (kW) | Function |
|-----------|-----------|------------|----------|
| **Air compressors** | 400 | 200 | Cathode air supply |
| **Hydrogen pumps/regulators** | 200 | 50 | Anode H₂ supply |
| **Cooling system** | 500 | 100 | Thermal management |
| **Humidifiers** | 150 | 20 | Membrane hydration |
| **Power conditioning** | 250 | — | DC-DC converters |
| **Control electronics** | 100 | 10 | System monitoring |
| **Plumbing and structure** | 400 | — | Manifolds, mounts |
| **Total BoP** | 2,000 | 380 | ~60% of FC system mass |

---

## 5. Battery Energy Storage

### 5.1 Battery Requirements

**Primary Functions:**
1. **Peak power assist:** Takeoff and climb (high transient power)
2. **Emergency power:** Fuel cell failure backup
3. **Power quality:** Smooth transients, voltage stability

### 5.2 Battery Specifications

**Technology:** Green-E Lithium-Ion (recycled materials)

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Energy capacity** | 1,000 | kWh | 3,600 MJ |
| **Energy density** | 400 | Wh/kg | Cell-level (Baseline A) |
| **Battery pack mass** | 2,500 | kg | Cells + BMS + enclosure |
| **Peak power output** | 5,000 | kW | 5C discharge rate |
| **Nominal voltage** | 800 | VDC | High-voltage DC bus |
| **Depth of discharge (normal)** | 80% | % | Extend cycle life |
| **Cycle life** | 2,000 | cycles | @ 80% DoD |

### 5.3 Battery Usage Profile (Design Mission)

| Flight Phase | Energy (kWh) | DoD (%) | Notes |
|--------------|--------------|---------|-------|
| **Pre-flight (ground)** | -50 | — | Recharge from previous flight |
| **Takeoff** | -167 | 17% | 5,000 kW × 2 min |
| **Climb** | -533 | 53% | 4,000 kW × 8 min (avg) |
| **Cruise (recharge)** | +300 | -30% | Excess FC power to battery |
| **Approach/Land** | 0 | 0% | FC only |
| **End of mission** | — | 40% | 400 kWh remaining (reserve) |

**Net Battery Discharge (Mission):** 400 kWh (40% DoD)  
**Post-mission recharge (ground):** 30-minute fast charge (2C rate)

### 5.4 Battery Thermal Management

**Cooling Requirements:**
- Heat generation (discharge): ~250 kW peak (5% losses at 5,000 kW)
- Cooling method: Liquid cooling (water-glycol), integrated with FC cooling
- Operating temperature range: 20-40°C (optimal)

---

## 6. Electrical System Architecture

### 6.1 High-Voltage DC Bus

**Voltage Level:** 800 VDC (nominal)  
**Voltage Range:** 650-900 VDC (operating envelope)

**Advantages:**
- Lower conductor weight vs. 400V (50% current reduction)
- Higher efficiency (lower I²R losses)
- Compatibility with automotive technology (800V EV trend)

### 6.2 Power Distribution

| Bus Section | Power (kW) | Voltage (VDC) | Loads |
|-------------|------------|---------------|-------|
| **Main HVDC Bus** | 9,000 | 800 | Motor inverters (8×) |
| **Essential HVDC Bus** | 500 | 800 | Emergency (2 motors min) |
| **Avionics Bus** | 50 | 28 | Flight control, avionics |
| **Cabin Services Bus** | 100 | 115 VAC | Galley, IFE, lighting |

### 6.3 Motor Inverters

**Configuration:** 8 independent motor inverters (1 per fan)

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| **Power per inverter (cruise)** | 375 | kW | 3,000 kW / 8 |
| **Power per inverter (max)** | 1,125 | kW | Peak (5 sec duration) |
| **Efficiency** | 98% | % | SiC (Silicon Carbide) MOSFETs |
| **Mass per inverter** | 75 | kg | Power electronics + cooling |
| **Total inverter mass** | 600 | kg | 8 inverters |

---

## 7. Energy Management Strategy

### 7.1 Operating Modes

**Mode 1: Takeoff (High Power)**
- Fuel cell: 4,000 kW (100% rated)
- Battery: 5,000 kW (5C discharge)
- Total: 9,000 kW
- Duration: 2 minutes

**Mode 2: Climb (Moderate Power)**
- Fuel cell: 4,000 kW (100% rated)
- Battery: 2,000 kW (2C discharge)
- Total: 6,000 kW
- Duration: 20 minutes

**Mode 3: Cruise (Efficient)**
- Fuel cell: 3,000 kW (75% rated, optimal efficiency)
- Battery: 0 kW (recharge at 300 kW if available FC capacity)
- Total: 3,000 kW
- Duration: 3+ hours

**Mode 4: Emergency (Fuel Cell Failure)**
- Fuel cell: 0 kW (failure scenario)
- Battery: 2,000 kW (sustain flight, land at nearest airport)
- Duration: 30 minutes (enough to divert and land)

### 7.2 AI-Optimized Energy Management

**Neural Network Controller:**
- Real-time optimization of FC/battery power split
- Predictive energy demand based on flight phase, weather, ATC
- Battery state-of-charge (SoC) management for longevity
- Thermal management coordination (FC + battery + motors)

**Benefits:**
- 3-5% energy efficiency improvement vs. rule-based control
- Extended battery life (optimal charge/discharge profiles)
- Improved system reliability (predictive failure detection)

---

## 8. Thermal Management

### 8.1 Heat Rejection Requirements

| Component | Power (kW) | Efficiency (%) | Waste Heat (kW) | Notes |
|-----------|------------|----------------|-----------------|-------|
| **Fuel cell (cruise)** | 3,000 | 50% | 3,000 | Major heat source |
| **Fuel cell (peak)** | 4,000 | 45% | 4,889 | Climb/takeoff |
| **Battery (discharge)** | 5,000 | 95% | 250 | Peak discharge |
| **Motors (8×)** | 3,000 | 96% | 120 | Motor losses |
| **Inverters (8×)** | 3,000 | 98% | 60 | Power electronics |
| **Total (peak)** | — | — | **~5,300** | Maximum heat load |

### 8.2 Cooling System Architecture

**Cooling Fluid:** Water-glycol (50/50 mix)  
**Heat Exchangers:** Ram air heat exchangers (wing leading edge, fuselage)

| Cooling Loop | Components Cooled | Flow Rate (L/min) | ΔT (°C) |
|--------------|-------------------|-------------------|---------|
| **Loop 1 (High Temp)** | Fuel cell stacks | 600 | 20°C rise |
| **Loop 2 (Low Temp)** | Battery, motors, inverters | 300 | 15°C rise |
| **Loop 3 (Cabin ECS)** | Cabin conditioning | 200 | Variable |

**Heat Rejection Strategy:**
- **Cruise (cold ambient):** Passive heat rejection sufficient
- **Ground (hot day):** Active cooling via ground power or APU

---

## 9. Refueling and Recharging

### 9.1 Hydrogen Refueling

**Refueling Time:** 15-20 minutes (1,500-2,500 kg H₂)  
**Refueling Pressure:** 350 bar (from 450 bar ground supply)  
**Refueling Rate:** ~100-150 kg/min (parallel fill, multiple tanks)

**Ground Equipment:**
- Hydrogen refueling truck or hydrant system
- Safety zone: 50 m exclusion (no ignition sources)
- Automated coupling with leak detection

### 9.2 Battery Recharging

**Recharge Time:** 30 minutes (fast charge, 2C rate)  
**Recharge Power:** 2,000 kW (ground charger)  
**Recharge Energy:** 800 kWh (80% SoC restoration)

**Ground Equipment:**
- High-power DC fast charger (CCS or custom connector)
- Battery thermal management during charge (cooling)

---

## 10. Safety and Redundancy

### 10.1 Energy System Redundancy

**Fuel Cell:**
- N+1 stack redundancy (can lose 1 stack, continue safe operation)
- Dual control systems (primary + backup)

**Battery:**
- Multi-module design (isolate failed modules)
- Fused at cell and module level
- Thermal runaway containment (fire-resistant barriers)

**Electrical Distribution:**
- Dual bus architecture (main + essential)
- Bus tie breakers for isolation
- Emergency power from battery (30 min reserve)

### 10.2 Failure Modes

| Failure | Impact | Mitigation | Outcome |
|---------|--------|------------|---------|
| **1 fuel cell stack failure** | -400 kW | Battery compensates | Safe flight continues |
| **Total fuel cell failure** | No FC power | Battery emergency mode | 30 min to land |
| **Battery failure** | No peak power | Reduced performance | Takeoff rejected or degraded climb |
| **1 motor failure** | -375 kW | 7 motors sufficient | Safe flight continues |
| **2 motors failure (same side)** | Asymmetric thrust | Yaw control + differential thrust | Land ASAP |

---

## 11. Technology Roadmap

### 11.1 Baseline Progression

| Parameter | Baseline A (2027) | Baseline B (2029) | Baseline C (2031) |
|-----------|-------------------|-------------------|-------------------|
| **Fuel cell power density** | 1.2 kW/kg | 1.5 kW/kg | 1.8 kW/kg |
| **Fuel cell efficiency** | 50% | 52% | 55% |
| **Battery energy density** | 400 Wh/kg | 400 Wh/kg | 450 Wh/kg |
| **H₂ storage** | GH₂ 350 bar | GH₂ 700 bar or LH₂ | LH₂ |
| **Total system mass** | 8,833 kg | 7,500 kg | 6,500 kg |

### 11.2 Enabling Technologies

1. **Fuel Cells:** Automotive and heavy-duty truck development (2025-2030)
2. **Batteries:** EV industry driving density improvements (400+ Wh/kg by 2027)
3. **H₂ Storage:** Aerospace-grade COPV maturation, LH₂ for aviation (NASA/ESA programs)
4. **Power Electronics:** SiC technology scaling (higher voltage, efficiency)

---

## 12. References

- [LC-11_0000-08 — Mission and Payload Assumptions](./LC-11_0000-08_Mission_Payload_Assumptions.md)
- [LC-11_0000-09 — Preliminary Mass Breakdown](./LC-11_0000-09_PMB0_Preliminary_Mass_Breakdown.md)
- [LC-11_0000-10 — Performance Assumptions](./LC-11_0000-10_Performance_Assumptions.md)
- [LC-11_0000-21 — Propulsion Integration](./LC-11_0000-21_Propulsion_Integration.md)

---

## 13. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Energy Systems & Propulsion Team | Initial energy sizing |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Propulsion, Energy Systems, Electrical, All Engineering Teams
- **Next Review:** Q1 2026
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
