# LC-11_0000-06 — Cabin Layout Concept

**UTCS Node:** LC-11_0000-06  
**Document Type:** Interior Configuration Specification  
**Status:** Draft  
**Version:** 1.0  
**Date:** 2025-12-05  
**Owner:** Cabin & Product Design Team

---

## 1. Purpose

This document defines the cabin layout concept for the AMPEL360 BWB Q100, addressing the unique challenges and opportunities of the non-cylindrical pressure vessel configuration.

---

## 2. Cabin Overview

### 2.1 Key Parameters

| Parameter | Value | Units | Notes |
|-----------|-------|-------|-------|
| Cabin length (interior) | 16.0 | m | Usable passenger area |
| Maximum cabin width | 16.5 | m | Interior dimension |
| Cabin height (ceiling) | 2.85 | m | At crown, typical for single-aisle |
| Floor area (total) | ~220 | m² | Includes aisles, galleys, lavatories |
| Passenger capacity | 100-120 | pax | Configuration dependent |
| Seat pitch (economy) | 30-32 | inches | Standard comfort |
| Seat pitch (premium) | 36-38 | inches | Enhanced comfort |

### 2.2 Design Challenges

1. **Non-circular cross-section:** BWB cabin is wide and relatively low height
2. **Emergency egress:** Wide cabin requires more exits than conventional aircraft
3. **Structural pillars:** Support columns required for pressure vessel strength
4. **Window constraints:** Limited or no side windows in centerbody region
5. **CG management:** Passenger distribution affects weight and balance

---

## 3. Baseline Configuration: 2-3-2 Economy (100 seats)

### 3.1 Seating Arrangement

**Layout:** Triple aisle, 2-3-2 seating
- **Left outer section:** 2 seats (A, B)
- **Left center section:** 3 seats (C, D, E)
- **Right center section:** 3 seats (F, G, H)
- **Right outer section:** 2 seats (J, K)

**Total seats per row:** 10  
**Number of rows:** 10 (economy)  
**Total economy seats:** 100

### 3.2 Cabin Zones

| Zone | Rows | Seats | Width (m) | Notes |
|------|------|-------|-----------|-------|
| Cockpit | — | 2 | — | Forward, separate from cabin |
| Entry vestibule | — | — | 16.5 | Forward cabin entry |
| Economy (forward) | 1-5 | 50 | 16.5 | Full width |
| Galley/Lavatory (mid) | — | — | 16.5 | Service area |
| Economy (aft) | 6-10 | 50 | 16.5 | Full width |
| Aft galley/service | — | — | 14.0 | Narrowing centerbody |

### 3.3 Cross-Section View (Typical)

```
         [Overhead bins]     [Overhead bins]     [Overhead bins]
    ___________________________________________________________
   /  |  A  B  | Aisle | C  D  E | Aisle | F  G  H | Aisle | J  K  |  \
  |   |--------|-------|---------|-------|---------|-------|--------|   |
  |   |   2    |  1.2m |    3    |  1.2m |    3    |  1.2m |   2    |   |
  |___|________|_______|_________|_______|_________|_______|________|___|

         <-------- 16.5 m interior width -------->
```

**Dimensions:**
- Seat width (economy): 18 inches (46 cm)
- Aisle width: 1.2 m (each of 3 aisles)
- Seat pitch: 31 inches (79 cm)
- Ceiling height: 2.85 m (at crown)

---

## 4. Alternative Configuration: 2-4-2 High-Density (120 seats)

### 4.1 Seating Arrangement

**Layout:** Dual aisle, 2-4-2 seating
- **Left section:** 2 seats (A, B)
- **Center section:** 4 seats (C, D, E, F)
- **Right section:** 2 seats (G, H)

**Total seats per row:** 8  
**Number of rows:** 15  
**Total seats:** 120

### 4.2 Comparison

| Configuration | Seats/Row | Rows | Total Seats | Aisles | Egress Rating |
|---------------|-----------|------|-------------|--------|---------------|
| 2-3-2 (Baseline) | 10 | 10 | 100 | 3 | Excellent |
| 2-4-2 (High-density) | 8 | 15 | 120 | 2 | Good |

**Trade-off:** 2-3-2 provides superior passenger experience (3 aisles, shorter walk to exit) but lower density.

---

## 5. Emergency Egress

### 5.1 Exit Requirements

Per CS-25 §25.807, emergency exits must enable full evacuation within 90 seconds.

**Exit Configuration (Baseline):**
- **Type A exits (forward):** 2 (port and starboard) — 110 pax capacity each
- **Type III exits (overwing):** 4 (2 port, 2 starboard) — 35 pax capacity each
- **Type A exits (aft):** 2 (port and starboard) — 110 pax capacity each

**Total exit capacity:** 2×110 + 4×35 + 2×110 = 580 pax  
**Required for 120 pax:** 120 pax (factor of 4.8× margin)

### 5.2 Evacuation Strategy

- **Wide cabin advantage:** Multiple aisles enable parallel evacuation flows
- **Exit spacing:** Meets CS-25 §25.813 (minimum distance between exits)
- **Slide deployment:** Dual-lane slides from Type A exits (2 passengers simultaneously)
- **Structural pillars:** Positioned to not obstruct evacuation paths

### 5.3 Cabin Crew

- **Minimum crew:** 4 flight attendants (FAR 121.391, 1 per 50 pax)
- **Typical crew:** 6 flight attendants (enhanced service)
- **Crew stations:** Forward, mid-cabin (×2), aft

---

## 6. Structural Considerations

### 6.1 Pressure Vessel Design

The BWB cabin is a **non-circular pressure vessel**, requiring:
- **Frames and stringers:** Longitudinal and circumferential reinforcement
- **Pillars/Columns:** Vertical supports to react pressure loads (not required in cylindrical fuselage)

**Pillar Arrangement:**
- **Number:** 8-12 structural columns distributed through cabin
- **Location:** Between seat sections (minimize intrusion)
- **Spacing:** ~4-5 m longitudinally, ~6-8 m laterally
- **Diameter:** ~20-30 cm (CFRP composite)
- **Aesthetic treatment:** Pillars integrated into cabin design (may become design feature)

### 6.2 Floor Structure

- **Cargo floor (lower):** Supports baggage containers and systems
- **Cabin floor:** Passenger seating, aisles
- **Floor beams:** Span laterally between fuselage sides
- **Seat tracks:** Longitudinal rails for seat attachment and CG adjustment

---

## 7. Amenities and Services

### 7.1 Galley Configuration

**Forward Galley:**
- **Location:** Front of cabin, adjacent to entry doors
- **Size:** Compact, 2-3 m²
- **Equipment:** Beverage maker, storage

**Mid-Cabin Galley (Main):**
- **Location:** Between row 5 and row 6
- **Size:** Full-service, 6-8 m²
- **Equipment:** Ovens, beverage makers, refrigeration, storage
- **Width:** Full cabin width (16.5 m) — opportunity for large service area

**Aft Galley:**
- **Location:** Aft cabin
- **Size:** 2-3 m²
- **Equipment:** Supplemental service station

### 7.2 Lavatories

**Quantity:** 4-6 lavatories (typical for 100-120 pax)

**Locations:**
- Forward: 2 lavatories (adjacent to forward galley)
- Mid-cabin: 2-4 lavatories (near mid-galley)
- Aft: Optional 2 lavatories

**Size:** Standard (1.2 m² each) with accessible lavatory option (2.5 m²)

### 7.3 Overhead Bins and Storage

- **Volume per passenger:** 0.12 m³ (typical regional/short-haul)
- **Total overhead bin volume:** 12-14 m³
- **Configuration:** Continuous overhead bins above each seat section
- **Additional storage:** Coat closets near entry doors

---

## 8. Passenger Experience Enhancements

### 8.1 Windows and Natural Light

**Challenge:** BWB centerbody has limited opportunity for conventional side windows.

**Solutions:**
1. **Virtual windows:** High-resolution displays showing exterior cameras (real-time)
2. **Skylights/roof windows:** Possible in low-stress regions (forward/aft)
3. **Ambient lighting:** LED mood lighting to enhance perceived spaciousness

### 8.2 Interior Design Concept

- **Open, spacious feel:** Wide cabin creates unique sense of space
- **Structural pillars as design feature:** Artistic treatments, lighting integration
- **Premium materials:** Sustainable, recyclable materials (circular economy)
- **Enhanced IFE:** In-flight entertainment on seatback screens or personal devices

### 8.3 Noise and Vibration

- **Advantages:** Upper-surface propulsion shields cabin from fan noise
- **Acoustic treatment:** Advanced insulation and damping materials
- **Target:** Cabin noise < 75 dB (cruise), competitive with conventional aircraft

---

## 9. Cabin Configuration Flexibility

### 9.1 Modular Seat Installation

- **Seat track system:** Allows reconfiguration for different missions
- **Quick-change capability:** Convert between economy and premium layouts (12-24 hours)
- **Mission profiles:**
  - **Regional high-density:** 120 economy seats (2-4-2 layout)
  - **Premium regional:** 100 seats (2-3-2 layout, enhanced pitch)
  - **Hybrid:** 20 premium + 80 economy = 100 total
  - **Corporate/VIP:** 40-60 seats, large premium seating

### 9.2 Cargo/Passenger Variants

- **Combi configuration:** Forward cabin for passengers, aft for cargo (pallets/containers)
- **All-cargo freighter:** Remove seats, install cargo handling system
- **Quick-change:** Palletized seats and monuments for rapid conversion

---

## 10. Accessibility and Universal Design

### 10.1 Wheelchair Accessibility

- **Aisle width:** 1.2 m aisles accommodate wheelchair passage
- **Accessible lavatory:** Minimum 1 accessible lavatory (2.5 m²)
- **Boarding:** Level entry from jetway (no steps)

### 10.2 Passenger Assistance

- **Seating:** Designated seating for passengers requiring assistance
- **Service animal accommodation:** Space for service animals
- **Onboard wheelchair:** Stowed in closet near accessible lavatory

---

## 11. Weight and CG Management

### 11.1 Passenger Weight Distribution

- **Reference passenger weight:** 95 kg (including carry-on)
- **Total passenger weight (100 pax):** 9,500 kg
- **CG impact:** Longitudinal passenger distribution managed via seat assignment

### 11.2 CG Control Strategy

**Challenge:** Wide cabin allows large lateral CG shifts (left/right passenger imbalance).

**Solutions:**
1. **Symmetric loading procedures:** Balance passengers left/right during boarding
2. **Fuel transfer:** Active fuel management to trim CG (if multiple tank zones)
3. **Cargo placement:** Strategic cargo loading to counterbalance passengers

---

## 12. Future Enhancements

1. **Advanced IFE:** AR/VR entertainment systems
2. **Biometric boarding:** Facial recognition for seamless entry
3. **Wellness features:** Circadian lighting, enhanced air quality (H₂ fuel cell humidification)
4. **Modular monuments:** Quick-change galleys and lavatories for operational flexibility
5. **Hydrogen safety education:** Passenger communication on safety and sustainability

---

## 13. References

- [LC-11_0000-04 — Geometry Definition](./LC-11_0000-04_Geometry_Definition.md)
- [LC-11_0000-07 — Crew and Passenger Flow Concept](./LC-11_0000-07_Crew_Pax_Flow_Concept.md)
- [LC-11_0000-09 — Preliminary Mass Breakdown](./LC-11_0000-09_PMB0_Preliminary_Mass_Breakdown.md)
- CS-25 §25.807 — Emergency Exits
- CS-25 §25.813 — Emergency Exit Access

---

## 14. Change Log

| Version | Date | Author | Description |
|---------|------|--------|-------------|
| 1.0 | 2025-12-05 | Cabin & Product Design Team | Initial cabin layout concept |

---

**Document Control:**
- **Classification:** Internal Use
- **Distribution:** Cabin Design, Certification, Operations, Marketing Teams
- **Next Review:** Q1 2026 (post-mockup evaluation)
- **Approver:** Chief Engineer

---

**© 2025 AMPEL360. All rights reserved.**
