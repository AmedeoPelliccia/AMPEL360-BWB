# LC-11_0010-22 — ECS and Cabin Integration

**UTCS Node:** LC-11_0010-22  
**Document Type:** Systems Integration  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Environmental Control Systems Team

---

## 1. Purpose

Defines Environmental Control System (ECS) integration with the BWB cabin and overall aircraft systems.

---

## 2. ECS Architecture

### 2.1 System Functions

- **Pressurization:** Maintain cabin altitude < 8,000 ft
- **Temperature control:** 18-26°C cabin temperature range
- **Ventilation:** Fresh air supply, 20 cfm per occupant
- **Humidity:** Passive humidification from fuel cell water vapor
- **Air quality:** HEPA filtration, CO₂ management

### 2.2 Integration with Propulsion

- **Heat source:** Fuel cell waste heat provides cabin heating
- **Cooling:** Vapor cycle air conditioning, integrated thermal management
- **Water:** Fuel cell water vapor collected for humidity and potable water

---

## 3. Cabin Pressurization

### 3.1 Pressure Vessel

- **Design pressure differential:** 9.0 psi (620 mbar)
- **Cabin altitude (cruise):** 6,500 ft at FL390
- **Pressure control:** Modulating outflow valves (2× redundant)

### 3.2 Structural Considerations

- **Non-circular cross-section:** BWB centerbody optimized for combined aero + pressure loads
- **Reinforcement:** Frames, stringers, and vertical pillars
- **Sealing:** Advanced seals at doors, windows, penetrations

---

## 4. Temperature Control

### 4.1 Heating

- **Primary:** Fuel cell waste heat (3,000 kW available @ cruise)
- **Distribution:** Ducted hot air from FC heat exchangers
- **Zoning:** Multi-zone control (cockpit, forward cabin, aft cabin)

### 4.2 Cooling

- **System:** Vapor cycle air conditioning (2× packs)
- **Capacity:** 50 kW cooling (each pack)
- **Heat rejection:** Ram air heat exchangers

---

## 5. Air Distribution

- **Supply:** Overhead distribution along cabin ceiling
- **Return:** Floor-level return grilles
- **Flow rate:** 20 cfm per person (ASHRAE standard)
- **Recirculation:** 50% recirculation with HEPA filtration

---

## 6. Emergency Systems

- **Oxygen:** Chemical oxygen generators for passengers, gaseous O₂ for crew
- **Fire suppression:** Halon replacement (clean agents) in cargo and systems bays
- **Smoke detection:** Dual-loop smoke detectors throughout cabin

---

## 7. References

- [LC-11_0010-06 — Cabin Layout Concept](./LC-11_0010-06_Cabin_Layout_Concept.md)
- [LC-11_0010-11 — Energy Sizing](./LC-11_0010-11_Energy_Sizing_Prelim.md)

---

**© 2025 AMPEL360. All rights reserved.**
