# LC-11_0010-21 — Propulsion Integration

**UTCS Node:** LC-11_0010-21  
**Document Type:** Integration Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Propulsion Integration Team

---

## 1. Purpose

Defines the integration of the distributed electric propulsion system into the BWB Q100 airframe.

---

## 2. Propulsion System Overview

### 2.1 Configuration

- **Type:** Distributed electric propulsion
- **Number of units:** 8 electric motor/fan assemblies
- **Location:** Trailing edge, upper surface (BLI configuration)
- **Power source:** Hydrogen fuel cell + battery hybrid

### 2.2 Unit Specifications

| Parameter | Value | Units |
|-----------|-------|-------|
| Motor power (cruise) | 375 | kW |
| Motor power (max) | 625 | kW |
| Fan diameter | 1.2 | m |
| Nacelle length | 1.8 | m |
| Unit weight | 150 | kg |

---

## 3. Installation Details

### 3.1 Spanwise Distribution

- Nacelles positioned at BL ±6m, ±9m, ±12m, ±15m (from centerline)
- Spacing: 3.0 m between adjacent nacelle centerlines
- Height: Inlet lip ~0.1 m above local trailing edge

### 3.2 Structural Integration

- **Mounting:** Steel/titanium pylon structure attached to wing rear spar
- **Load paths:** Motor thrust and gyroscopic loads to wing structure
- **Access:** Quick-disconnect mounts for maintenance/replacement

### 3.3 Electrical Integration

- **Power distribution:** 800 VDC cables from centerbody
- **Inverters:** Co-located with motors in nacelles
- **Control:** Dual-redundant digital control via CAN bus

---

## 4. Aerodynamic Integration

### 4.1 Boundary Layer Ingestion (BLI)

- **Benefit:** 5-8% propulsive efficiency improvement
- **Inlet design:** D-shaped, short inlet for boundary layer capture
- **Distortion:** Electric fan design accommodates non-uniform inflow

### 4.2 Acoustic Considerations

- **Fan noise:** Upper surface installation shields ground
- **Tip speed:** Limited to M_tip < 0.8 for noise reduction
- **Treatment:** Acoustic liners in inlet and exhaust

---

## 5. Thermal Management

- **Motor cooling:** Liquid cooling (water-glycol) integrated with FC system
- **Heat rejection:** Local heat exchangers or centerbody routing
- **Thermal protection:** Fire-resistant barriers, temperature sensors

---

## 6. Safety and Redundancy

- **Failure modes:** Any single motor failure, safe flight continues
- **Asymmetric thrust:** Differential thrust compensation via flight control
- **Fire protection:** Detection and suppression in each nacelle

---

## 7. References

- [LC-11_0010-05 — Planform Layout](./LC-11_0010-05_Planform_Layout.md)
- [LC-11_0010-11 — Energy Sizing](./LC-11_0010-11_Energy_Sizing_Prelim.md)

---

**© 2025 AMPEL360. All rights reserved.**
