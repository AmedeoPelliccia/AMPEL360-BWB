# LC-11_0010-05 — Planform Layout

**UTCS Node:** LC-11_0010-05  
**Document Type:** Technical Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Aerodynamics Team

---

## 1. Purpose

This document provides detailed planform layout specifications for the AMPEL360 BWB Q100, including wing geometry, control surface arrangement, and propulsion integration from a top-view perspective.

---

## 2. Overall Planform Strategy

### 2.1 Design Philosophy

The Q100 planform is optimized for:
- **Transonic cruise efficiency:** Minimize wave drag at M = 0.72-0.75
- **Span loading:** Elliptical lift distribution for minimum induced drag
- **Distributed propulsion integration:** 8 nacelles along trailing edge
- **Airport compatibility:** Wingspan < 52 m (ICAO Code C)
- **Stability and control:** Adequate moment arms for pitch and yaw control

### 2.2 Key Planform Features

1. **Highly swept centerbody** (45° LE) for transonic performance
2. **Moderate sweep outer wing** (32° LE) for structural efficiency
3. **Blended transition** eliminates junction drag
4. **Straight trailing edge** simplifies control surface actuation
5. **Winglet vertical stabilizers** provide yaw control and reduce effective span

---

## 3. Planform Dimensions Summary

| Parameter | Symbol | Value | Units | Notes |
|-----------|--------|-------|-------|-------|
| Wingspan | b | 45.0 | m | Tip to tip |
| Reference area | Sref | 295.0 | m² | Total planform area |
| Aspect ratio | AR | 6.86 | — | b²/Sref |
| Mean aerodynamic chord | MAC | 6.9 | m | Calculated from area distribution |
| MAC leading edge position | XMAC | 13.0 | m | From nose (X = 0) |
| Centerbody width (max) | — | 18.0 | m | At widest point |
| Root chord (centerline) | Croot | 12.5 | m | Maximum chord |
| Tip chord | Ctip | 2.8 | m | Wingtip chord |
| Taper ratio | λ | 0.35 | — | Effective Ctip/Croot |

---

## 4. Spanwise Geometry Breakdown

### 4.1 Centerbody Section (0% - 40% semi-span)

**Purpose:** Primary lifting body, cabin and cargo containment, hydrogen storage

| Parameter | Value | Notes |
|-----------|-------|-------|
| Spanwise extent | 0 - 9.0 m (each side from centerline) | |
| Leading edge sweep | 45° | Optimized for M = 0.72 cruise |
| Trailing edge | Straight (0° sweep) | Simplifies flap/fan integration |
| Chord at BL 0 (centerline) | 12.5 m | Maximum depth for cabin height |
| Chord at BL 9.0 m | 8.0 m | Transition to outer wing |
| Area (both sides) | ~180 m² | ~61% of total planform |

**Key Features:**
- Houses entire pressurized cabin (16 m length)
- Hydrogen storage tanks aft of cabin
- Thick airfoil sections (15-18% t/c) for internal volume
- Leading edge slats for high-lift (18 m span)
- Trailing edge flaps between propulsion nacelles (10 m span)

---

### 4.2 Transition/Blend Section (40% - 55% semi-span)

**Purpose:** Smooth aerodynamic transition from centerbody to outer wing

| Parameter | Value | Notes |
|-----------|-------|-------|
| Spanwise extent | 9.0 - 12.4 m (from centerline) | |
| Leading edge sweep | 38-42° (variable) | Smooth curve from 45° to 32° |
| Chord at BL 9.0 m | 8.0 m | Start of blend |
| Chord at BL 12.4 m | 6.5 m | End of blend |
| Area (both sides) | ~48 m² | ~16% of total planform |

**Key Features:**
- Smoothly faired contours (no sharp discontinuities)
- Thickness ratio decreases from 12% to 10% t/c
- Distributed propulsion nacelles continue (nacelles 5-6)
- Structural wing carry-through below cabin floor

---

### 4.3 Outer Wing Section (55% - 100% semi-span)

**Purpose:** Efficient span loading, fuel storage (if needed), aileron control

| Parameter | Value | Notes |
|-----------|-------|-------|
| Spanwise extent | 12.4 - 22.5 m (from centerline) | |
| Leading edge sweep | 32° | Optimized for structure and control |
| Trailing edge sweep | -5° (forward) | Improves tip control authority |
| Chord at BL 12.4 m | 6.5 m | Blend station |
| Chord at BL 22.5 m (tip) | 2.8 m | Wingtip |
| Area (both sides) | ~67 m² | ~23% of total planform |
| Taper ratio (outer wing) | 0.43 | Local taper (6.5m / 2.8m) |

**Key Features:**
- Reduced thickness (8-10% t/c) for transonic efficiency
- Winglet-mounted vertical stabilizers at tips
- Elevon control surfaces (11 m span each side)
- Spoilers/speed brakes on upper surface (8 m span)
- Optional fuel tanks (backup SAF or additional battery)

---

## 5. Leading Edge Definition

### 5.1 Leading Edge Sweep Distribution

The leading edge sweep varies continuously to optimize aerodynamic and structural performance:

| Buttline Station (m) | Local LE Sweep (°) | Section |
|----------------------|---------------------|---------|
| 0.0 (centerline) | 45° | Centerbody |
| 4.5 | 45° | Centerbody |
| 9.0 | 45° | Centerbody edge |
| 10.5 | 42° | Transition |
| 12.4 | 38° | Blend end |
| 15.0 | 34° | Outer wing |
| 22.5 | 32° | Wingtip |

### 5.2 Leading Edge Devices

**Leading Edge Slats:**
- **Span:** BL 0 to BL 9.0 m (both sides) = 18.0 m total
- **Chord:** 12% of local chord
- **Deployment angles:** 0° (retracted), 25° (approach), 30° (landing)
- **Gap:** 2-3% chord when deployed
- **Purpose:** Increase CLmax, delay stall, improve low-speed handling

**Fixed Leading Edge:**
- **Span:** BL 9.0 to BL 22.5 m (outer wing)
- **Profile:** Smooth contour optimized for cruise
- **Droop:** None (natural airfoil shape)

---

## 6. Trailing Edge Definition

### 6.1 Trailing Edge Geometry

The trailing edge is predominantly straight with slight forward sweep outboard:

| Buttline Station (m) | Trailing Edge Sweep (°) | Notes |
|----------------------|-------------------------|-------|
| 0.0 - 16.0 | 0° (straight) | Centerbody + inner wing |
| 16.0 - 22.5 | -5° (forward sweep) | Outer wing, improves aileron authority |

### 6.2 Trailing Edge Devices

**Trailing Edge Flaps:**
- **Location:** Inboard centerbody (between propulsion nacelles)
- **Span:** BL 2.0 to BL 7.0 m (both sides) = 10.0 m total
- **Chord:** 28% of local chord
- **Type:** Single-slotted Fowler flaps
- **Deployment angles:** 0° (retracted), 20° (takeoff), 30° (approach), 40° (landing)
- **Purpose:** High-lift for takeoff and landing

**Elevons (Combined Elevator + Aileron):**
- **Location:** Outer wing trailing edge
- **Span:** BL 11.5 to BL 22.5 m (each side) = 11.0 m per side
- **Chord:** 25% of local chord
- **Deflection range:** ±25° (symmetric for pitch, differential for roll)
- **Actuation:** Dual hydraulic + electric backup

**Spoilers/Speed Brakes:**
- **Location:** Upper surface, outer wing
- **Span:** BL 14.0 to BL 22.0 m (each side) = 8.0 m per side
- **Chord:** 20% of local chord
- **Deployment:** 0° (retracted) to 60° (full deployment)
- **Purpose:** Lift dump (landing), roll assist, speed brake (flight)

---

## 7. Propulsion Integration Layout

### 7.1 Distributed Nacelle Placement

**Configuration:** 8 nacelles along trailing edge (upper surface)

| Nacelle # | Buttline (m) | X-position (m) | Notes |
|-----------|--------------|----------------|-------|
| 1 (left) | -15.0 | 24.0 | Outboard |
| 2 (left) | -12.0 | 24.2 | |
| 3 (left) | -9.0 | 24.5 | |
| 4 (left) | -6.0 | 24.8 | |
| 5 (right) | +6.0 | 24.8 | |
| 6 (right) | +9.0 | 24.5 | |
| 7 (right) | +12.0 | 24.2 | |
| 8 (right) | +15.0 | 24.0 | Outboard |

### 7.2 Nacelle Geometry

- **Fan diameter:** 1.2 m
- **Nacelle length:** 1.8 m
- **Spacing:** 3.0 m between adjacent nacelles (center-to-center)
- **Height above surface:** ~0.1 m (inlet lip to local TE)
- **Cant angle:** 0° (aligned with freestream at cruise)

### 7.3 Boundary Layer Ingestion (BLI)

- **Inlet location:** Positioned to ingest low-momentum wake from BWB centerbody
- **BLI benefit:** 5-8% reduction in propulsive power required
- **Distortion tolerance:** Electric fan design accommodates non-uniform inlet flow
- **Inlet design:** Short, D-shaped inlet optimized for low drag and good pressure recovery

---

## 8. Control Surface Layout

### 8.1 Primary Flight Control Surfaces

**Pitch Control:**
- **Elevons (symmetric deflection):** ±25° combined
- **Control power:** ~0.025 / deg (preliminary)
- **Redundancy:** Dual hydraulic actuators per surface

**Roll Control:**
- **Elevons (differential deflection):** ±25° per side
- **Spoilers (differential deployment):** 0-60° per side
- **Control power:** Roll rate > 30°/sec at cruise

**Yaw Control:**
- **Twin rudders (winglet vertical stabilizers):** ±30°
- **Differential thrust:** Propulsion yaw assist (±5% thrust per side)

### 8.2 Secondary Flight Controls

**High-Lift:**
- **Leading edge slats:** 0° / 25° / 30°
- **Trailing edge flaps:** 0° / 20° / 30° / 40°
- **Increased CLmax:** From 1.2 (clean) to 2.4 (full flaps)

**Drag Modulation:**
- **Spoilers/speed brakes:** 0-60° deployment
- **Drag increment:** ΔCD ≈ 0.08 at full deployment

---

## 9. Vertical Stabilizers (Winglets)

### 9.1 Configuration

- **Type:** Split winglet-mounted vertical stabilizers
- **Quantity:** 2 (one per wingtip)
- **Purpose:** Yaw stability and control, induced drag reduction

### 9.2 Geometry

| Parameter | Value | Units |
|-----------|-------|-------|
| Height (above wing) | 4.5 | m |
| Root chord | 3.0 | m |
| Tip chord | 1.2 | m |
| Sweep (LE) | 35° | |
| Cant angle | 15° (outward) | |
| Area (each) | 9.5 | m² |

### 9.3 Rudder

- **Span:** 3.5 m (75% of stabilizer height)
- **Chord:** 30% of local stabilizer chord
- **Deflection:** ±30°
- **Purpose:** Yaw control, crosswind landing correction

---

## 10. Area Distribution

### 10.1 Spanwise Lift Distribution (Design Condition)

Target lift distribution approximates elliptical for minimum induced drag:

| Spanwise Station (% semi-span) | Local Lift Coefficient (Cl) | Notes |
|--------------------------------|------------------------------|-------|
| 0% (centerline) | 0.52 | High lift centerbody |
| 20% | 0.55 | Peak loading region |
| 40% (blend) | 0.50 | |
| 60% | 0.42 | Outer wing |
| 80% | 0.28 | Reduced loading outboard |
| 100% (tip) | 0.10 | Low tip loading |

**Effective Span Efficiency:** e ≈ 0.88 (excellent for non-elliptical planform)

### 10.2 Wetted Area Breakdown

| Component | Wetted Area (m²) | % of Total |
|-----------|------------------|------------|
| Upper surface | 298 | 42% |
| Lower surface | 295 | 42% |
| Nacelles (8×) | 38 | 5% |
| Vertical stabilizers | 40 | 6% |
| Misc. (fairings, etc.) | 35 | 5% |
| **Total** | **706** | **100%** |

**Wetted Area Ratio:** Swet / Sref = 706 / 295 = 2.39 (favorable for BWB)

---

## 11. Structural Layout (Planform View)

### 11.1 Primary Structure

**Wing Box:**
- **Front spar:** ~15% chord location
- **Rear spar:** ~65% chord location
- **Ribs:** Spanwise spacing ~0.8-1.2 m
- **Stringers:** Longitudinal (spanwise), ~0.3 m spacing

**Centerbody Structure:**
- **Pressure bulkhead (forward):** X = 4.5 m
- **Pressure bulkhead (aft):** X = 22.0 m
- **Floor beams:** Support cabin and cargo floor
- **Keel beam:** Central longitudinal member for load distribution

### 11.2 Hard Points

- **Main landing gear:** X ≈ 15.0 m, Y ≈ ±5.5 m
- **Nose landing gear:** X ≈ 5.0 m, Y = 0 m
- **Propulsion nacelle mounts:** 8 locations along trailing edge
- **Fuel cell installation:** Centerbody aft section
- **Hydrogen tank mounts:** Centerbody aft, multiple tanks

---

## 12. Design Drivers and Trade-Offs

### 12.1 Sweep Selection

**Centerbody (45° LE sweep):**
- **Benefit:** Delayed drag divergence at M = 0.72-0.75
- **Trade-off:** Structural weight (swept wing less efficient)
- **Justification:** Transonic performance critical for mission range/speed

**Outer wing (32° LE sweep):**
- **Benefit:** Structural efficiency, lower weight
- **Trade-off:** Slightly earlier drag rise than 45°
- **Justification:** Outer wing operates at lower local lift coefficient (less critical)

### 12.2 Aspect Ratio (AR = 6.86)

**Trade-offs:**
- **Higher AR:** Lower induced drag, better L/D → longer range
- **Lower AR:** Lower structural weight, easier gust load management
- **Selected AR = 6.86:** Balance of efficiency and weight

**Comparison:**
- Conventional airliners: AR = 9-11 (tube-and-wing benefits from fuselage contribution)
- BWB concepts: AR = 6-8 (entire planform contributes lift)

### 12.3 Wingtip Devices

**Winglet vertical stabilizers (selected) vs. alternatives:**

| Option | Drag Benefit | Weight | Yaw Control |
|--------|--------------|--------|-------------|
| No winglet | Baseline | Baseline | Requires large tail |
| Blended winglet | -3% induced drag | +150 kg | No yaw control |
| Split-tip winglet | -4% induced drag | +200 kg | No yaw control |
| **Winglet vertical stabilizer** | **-4% induced drag** | **+250 kg** | **Yes (integrated)** |

**Justification:** Integrating yaw control into winglets eliminates separate tail (net weight savings ~400 kg).

---

## 13. Computational Analysis

### 13.1 CFD Validation Status

| Analysis Type | Status | Tool | Key Result |
|---------------|--------|------|------------|
| Cruise drag polar | Complete | ANSYS Fluent | L/D = 21.2 @ M=0.72, CL=0.48 |
| High-lift (flaps) | Complete | OpenFOAM | CLmax = 2.35 @ M=0.2 |
| Propulsion integration | In progress | STAR-CCM+ | BLI benefit: 6.5% (preliminary) |
| Stability derivatives | Complete | AVL + CFD | Stable with control augmentation |

### 13.2 Wind Tunnel Testing

**Planned Tests:**
- **Model scale:** 1:20 (2.25 m span model)
- **Facility:** TBD (likely NASA Ames or European partner)
- **Test objectives:**
  - Validate CFD drag predictions
  - Measure high-lift performance
  - Assess propulsion integration (powered model)
  - Stability and control derivatives

---

## 14. Future Refinements

1. **Inlet shaping optimization:** Further CFD to minimize BLI inlet distortion
2. **Control surface sizing:** May require adjustment post-flight dynamics analysis
3. **Winglet vertical stabilizer cant angle:** Optimize for drag vs. yaw authority
4. **Nacelle spacing:** Trade study on 6 vs. 8 vs. 10 fans
5. **High-lift system:** Potential for thrust-assisted lift in lieu of larger flaps

---

## 15. References

- [LC-11_0010-04 — Geometry Definition](./LC-11_0010-04_Geometry_Definition.md)
- [LC-11_0010-06 — Cabin Layout Concept](./LC-11_0010-06_Cabin_Layout_Concept.md)
- [LC-11_0010-21 — Propulsion Integration](./LC-11_0010-21_Propulsion_Integration.md)

---

## 16. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Aerodynamics Team | Initial planform layout definition |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Aerodynamics, Structures, Propulsion Teams
- **Next Review:** Q1 2026 (post-CFD validation)
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
