# LC-11_0000-04 — Geometry Definition

**UTCS Node:** LC-11_0000-04  
**Document Type:** Technical Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Aerodynamics & Structures Team

---

## 1. Purpose

This document defines the preliminary external geometry and key dimensional parameters for the AMPEL360 BWB Q100 aircraft. It establishes the geometric baseline for aerodynamic analysis, structural design, and systems integration.

---

## 2. Overall Dimensions

### 2.1 Principal Dimensions (Baseline A - Conservative)

| Parameter | Value | Units | Status | Notes |
|-----------|-------|-------|--------|-------|
| **Overall Length** | 32.5 | m | Preliminary | Nose to tail extremity |
| **Overall Wingspan** | 45.0 | m | Preliminary | Tip to tip |
| **Overall Height** | 8.2 | m | Preliminary | Ground to highest point (tail) |
| **Reference Wing Area (Sref)** | 295 | m² | Preliminary | Including centerbody |
| **Aspect Ratio** | 6.86 | — | Preliminary | b²/Sref |
| **Mean Aerodynamic Chord (MAC)** | 6.9 | m | Preliminary | Reference for CG location |

### 2.2 Dimensional Comparison

| Aircraft | Wingspan (m) | Length (m) | Wing Area (m²) | Aspect Ratio |
|----------|--------------|------------|----------------|--------------|
| **Q100 Baseline A** | **45.0** | **32.5** | **295** | **6.86** |
| A320neo | 35.8 | 37.6 | 122.6 | 10.4 |
| B787-8 | 60.1 | 56.7 | 325 | 11.1 |
| Flying-V (concept) | 65.0 | 17.0 | ~350 | ~12 |

*Note: Q100 optimizes for distributed propulsion integration and BWB efficiency*

---

## 3. Planform Geometry

### 3.1 Overall Planform Shape

The BWB planform consists of three integrated regions:
1. **Centerbody:** Central lifting body containing cabin, cargo, and hydrogen storage
2. **Outer Wing Panels:** Outboard wing sections for additional lift and control surfaces
3. **Blended Transition:** Smooth fairing between centerbody and outer wings

### 3.2 Planform Parameters

| Region | Parameter | Value | Notes |
|--------|-----------|-------|-------|
| **Centerbody** | Width | 18.0 m | At maximum beam location |
| | Chord (root) | 12.5 m | Centerline chord |
| | Chord (mid) | 8.0 m | At centerbody/wing blend |
| | Sweep (LE) | 45° | Leading edge sweep |
| **Outer Wing** | Root chord | 8.0 m | At blend line |
| | Tip chord | 2.8 m | Wingtip chord |
| | Sweep (LE) | 32° | Outer panel leading edge |
| | Span (each side) | 13.5 m | From blend to tip |
| **Overall** | Taper ratio | 0.35 | Tip/root (effective) |

### 3.3 Leading Edge Sweep Distribution

- **Centerbody LE:** 45° (optimized for transonic drag)
- **Transition region:** 38-42° (smoothly faired)
- **Outer wing LE:** 32° (structural efficiency and control surface sizing)

### 3.4 Trailing Edge

- **Straight trailing edge** from centerline to ~75% semi-span
- **Forward sweep** outboard for:
  - Distributed propulsion nacelle integration
  - Control surface effectiveness
  - Wingtip vortex management

---

## 4. Sectional Geometry

### 4.1 Airfoil Sections

The BWB uses custom-designed airfoil sections optimized for:
- Transonic cruise efficiency (M = 0.72-0.75)
- Pressure recovery for boundary layer ingestion (BLI)
- Internal volume for cabin and systems

| Station | Location (% semi-span) | Thickness/Chord (t/c) | Camber | Function |
|---------|------------------------|----------------------|--------|----------|
| **Centerline** | 0% | 18% | High (4-5%) | Cabin containment, lift |
| **Centerbody mid** | 20% | 15% | Medium (3%) | Cabin + cargo |
| **Blend** | 40% | 12% | Medium (2.5%) | Transition to wing |
| **Mid outer wing** | 65% | 10% | Low (1.5%) | Cruise lift, fuel tanks |
| **Wingtip** | 100% | 8% | Low (1%) | Drag reduction, control |

### 4.2 Airfoil Characteristics

- **Type:** NASA/Boeing BWB custom sections (NLF-like characteristics)
- **Cruise CL:** 0.45-0.50 (at design mission)
- **Buffet margin:** > 0.15 ΔCL at cruise
- **Max thickness location:** 30-35% chord (forward for structural depth)

### 4.3 Twist Distribution

Spanwise twist optimizes lift distribution and minimizes induced drag:

| Station | Geometric Twist (°) | Notes |
|---------|---------------------|-------|
| Centerline | +3.0° | High lift centerbody |
| 25% semi-span | +1.5° | Smooth transition |
| 50% semi-span | 0° | Reference (no twist) |
| 75% semi-span | -1.0° | Reduce tip loading |
| Wingtip | -2.5° | Washout for stall characteristics |

*Total washout: 5.5° (centerline to tip)*

---

## 5. Fuselage/Centerbody Geometry

### 5.1 Centerbody Dimensions

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| Maximum width | 18.0 | m | At widest cabin section |
| Maximum height | 5.5 | m | At cabin crown |
| Length (pressurized) | 22.0 | m | Cabin + cockpit |
| Cabin floor area | ~220 | m² | Usable cabin space |

### 5.2 Cross-Sectional Shape

The centerbody cross-section is a **non-circular pressure vessel** optimized for:
- Aerodynamic efficiency (integrated with wing profile)
- Structural efficiency (elliptical/rectangular with rounded corners)
- Cabin layout flexibility (wide, low-height cross-section)

**Typical Cabin Cross-Section (mid-cabin):**
- Width: 16.5 m (interior)
- Height: 2.85 m (ceiling height)
- Floor width: 14.0 m (between seat tracks)
- Shape: Rounded rectangle approximating ellipse

### 5.3 Nose Geometry

- **Type:** Smooth, low-drag nose fairing
- **Length:** 4.5 m (nose tip to pressure bulkhead)
- **Cockpit windows:** Conventional layout adapted to BWB contour
- **Weather radar:** Nose-mounted (X-band, 24-inch antenna)

### 5.4 Tail/Aft Geometry

- **Aft body:** Smooth taper to trailing edge
- **Tail cone:** Integrated with aft pressure bulkhead
- **Auxiliary Power Unit (APU):** Aft centerbody location

---

## 6. Control Surfaces

### 6.1 Primary Flight Controls

| Surface | Location | Span | Chord (% local) | Function |
|---------|----------|------|-----------------|----------|
| **Elevons** | Trailing edge, outer wing | 11.0 m (each) | 25% | Pitch + roll |
| **Spoilers/Speedbrakes** | Upper surface, outer wing | 8.0 m (each) | 20% | Lift dump, roll assist |
| **Rudders** | Vertical stabilizers | 3.5 m (each) | 30% | Yaw control |

### 6.2 High-Lift Devices

| Device | Location | Span | Deployment | Notes |
|--------|----------|------|------------|-------|
| **Leading Edge Slats** | Centerbody + inner wing | 18.0 m | 25° / 30° | Two-position |
| **Trailing Edge Flaps** | Inboard TE (between fans) | 10.0 m | 20° / 30° / 40° | Three-position |

*Note: Distributed propulsion reduces reliance on mechanical high-lift (thrust vectoring possible)*

### 6.3 Vertical Stabilizers

- **Configuration:** Twin vertical stabilizers (winglets)
- **Location:** Outer wing tips, canted outward 15°
- **Height:** 4.5 m (above local wing surface)
- **Purpose:** Yaw stability and control, reduce span (airport gate compatibility)

---

## 7. Propulsion Integration

### 7.1 Distributed Propulsion Layout

- **Number of nacelles:** 8 (Baseline A)
- **Location:** Trailing edge, upper surface
- **Spanwise distribution:** Evenly spaced from centerline to 80% semi-span
- **Spacing:** ~4.5 m between adjacent nacelle centerlines

### 7.2 Nacelle Geometry (Preliminary)

| Parameter | Value | Units |
|-----------|-------|-------|
| Fan diameter | 1.2 | m |
| Nacelle length | 1.8 | m |
| Inlet lip radius | 0.05 | m |
| Nozzle area ratio | 1.05 | — |

### 7.3 Boundary Layer Ingestion (BLI)

- **Inlet location:** ~10 cm above local trailing edge surface
- **BLI fraction:** 40-50% of nacelle mass flow from boundary layer
- **Distortion tolerance:** Electric fan design accommodates non-uniform inflow

---

## 8. Internal Arrangement (Preliminary)

### 8.1 Cabin Zone

- **Location:** Forward centerbody
- **Length:** 16.0 m
- **Capacity:** 100-120 passengers (configuration dependent)
- **Aisle arrangement:** Dual aisles (2-3-2 or 2-4-2 seating)

### 8.2 Hydrogen Storage Zone

- **Location:** Aft centerbody (behind cabin pressure bulkhead)
- **Volume available:** ~40 m³
- **Configuration:** Multiple COPV tanks (350 bar)
- **Safety separation:** Minimum 1.0 m from cabin pressure boundary

### 8.3 Cargo Zone

- **Location:** Below cabin floor, centerbody
- **Volume:** ~25 m³ (≈ 3 LD3 containers equivalent)
- **Access:** Belly cargo doors (port and starboard)

### 8.4 Systems Bays

- **Main equipment bay:** Forward lower centerbody (avionics, ECS)
- **APU bay:** Aft centerbody
- **Electrical equipment:** Distributed along centerbody/wing structure

---

## 9. Reference Axes and Datums

### 9.1 Coordinate System

- **Origin:** Nose tip at waterline zero
- **X-axis:** Positive aft (along fuselage reference line - FRL)
- **Y-axis:** Positive right (looking forward)
- **Z-axis:** Positive up

### 9.2 Key Reference Stations

| Feature | X-Station (m) | Notes |
|---------|---------------|-------|
| Nose tip | 0.0 | Origin |
| Cockpit windscreen | 3.5 | |
| Front pressure bulkhead | 4.5 | |
| Forward cabin door | 6.0 | |
| Wing MAC leading edge | 13.0 | Aerodynamic reference |
| Wing MAC 25% | 14.7 | CG reference location |
| Aft cabin door | 20.0 | |
| Aft pressure bulkhead | 22.0 | |
| Trailing edge (centerline) | 25.5 | |
| Tail extremity | 32.5 | |

### 9.3 Waterline and Buttline References

- **Waterline Zero (WL 0):** Ground contact plane (landing gear compressed)
- **Buttline Zero (BL 0):** Aircraft centerline
- **Cabin floor:** WL 2.5 m (approximate)

---

## 10. Mass Properties (Preliminary)

### 10.1 Center of Gravity Envelope

| Condition | X-CG (% MAC) | Z-CG (m WL) | Notes |
|-----------|--------------|-------------|-------|
| Most Forward | 15% | 3.2 | Empty + crew, full H₂ |
| Most Aft | 35% | 3.5 | MTOW, aft cargo loaded |
| Cruise (typical) | 25% | 3.4 | Mid-mission |

### 10.2 Moment of Inertia (Preliminary Estimates)

| Axis | Value | Units |
|------|-------|-------|
| Ixx (roll) | 1.2 × 10⁶ | kg·m² |
| Iyy (pitch) | 2.8 × 10⁶ | kg·m² |
| Izz (yaw) | 3.5 × 10⁶ | kg·m² |

---

## 11. Design Constraints

### 11.1 Airport Compatibility

- **Wingspan:** 45 m < ICAO Code C limit (52 m) → No special gate requirements
- **Tail height:** 8.2 m < standard hangar clearance (12-15 m)
- **Turning radius:** Compatible with standard taxiways

### 11.2 Structural Design Loads

- **Limit load factor:** +2.5g / -1.0g (normal operation)
- **Ultimate load factor:** +3.75g / -1.5g (1.5× safety factor)
- **Gust loads:** CS-25 §25.341 (25 ft/s at VC, 50 ft/s at VB)

### 11.3 Ground Clearance

- **Wingtip:** > 0.5 m (gear compressed, maximum bank angle)
- **Tail strike angle:** > 12° (rotation at takeoff)
- **Engine inlet:** > 0.4 m (FOD protection)

---

## 12. Future Refinements

The following geometric aspects require further definition:

1. **Detailed airfoil design:** CFD optimization for cruise and off-design conditions
2. **Landing gear integration:** Main gear location and stowage volume
3. **Door and emergency exit locations:** Cabin layout driven
4. **Nacelle integration details:** Inlet shaping, exhaust mixing, acoustic treatment
5. **Control surface hinge lines:** Actuation system sizing
6. **Inspection and maintenance access panels:** Producibility and maintainability

---

## 13. References

- [LC-11_0000-01 — Concept Overview](./LC-11_0000-01_Concept_Overview.md)
- [LC-11_0000-05 — Planform Layout](./LC-11_0000-05_Planform_Layout.md)
- [LC-11_0000-06 — Cabin Layout Concept](./LC-11_0000-06_Cabin_Layout_Concept.md)
- [LC-11_0000-20 — Airframe Integration](./LC-11_0000-20_Airframe_Integration.md)

---

## 14. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Aerodynamics & Structures Team | Initial geometry definition (Baseline A) |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Aerodynamics, Structures, Systems Integration Teams
- **Next Review:** Q1 2026 (post-wind tunnel test)
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
