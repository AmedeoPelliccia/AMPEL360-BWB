# LC-1.4 Detailed Design

## Purpose
Develop comprehensive 3D models, system architectures, and detailed design documentation that fully define the AMPEL360 BWB aircraft for manufacturing and certification.

## Scope

This phase translates requirements into detailed, manufacturable designs, including:

- **CAD Models:** 3D parametric models in Catia, NX, or BlenderCAD
- **Systems Architecture:** Logical and physical architecture models (MBSE)
- **ATA Chapter Breakdown:** Design organization by ATA chapters
- **2D/3D/Parametric Baselines:** Master geometry and configuration control
- **Bill of Materials (BOM):** Complete parts lists with metadata
- **OPT-IN Folder Structure:** Organized design artifacts

## Key Activities

### 1. CAD Development
- **Master Geometry:** BWB outer mold line (OML) and inner mold line (IML)
- **Structural Design:** Primary structure, frames, longerons, skin panels
- **Systems Integration:** Routing of hydraulics, electrical, environmental control
- **Hydrogen Systems:** Storage tanks, distribution, safety systems
- **Propulsion Integration:** Electric motor mounts, nacelle design
- **Cabin Design:** Seating, monuments, galleys, lavatories
- **Landing Gear:** Main and nose gear integration

### 2. Model-Based Systems Engineering (MBSE)
- **System Architecture:** SysML models for all major systems
- **Functional Architecture:** Operational modes and states
- **Physical Architecture:** Component allocation and interfaces
- **Behavioral Models:** State machines and sequence diagrams
- **Requirements Allocation:** Linking requirements to design elements

### 3. ATA Chapter Design Organization

#### Airframe Systems (ATA 20-49)
- ATA 21: Air Conditioning
- ATA 22: Auto Flight (AI/NN Enhanced)
- ATA 23: Communications
- ATA 24: Electrical Power
- ATA 25: Equipment/Furnishings
- ATA 26: Fire Protection
- ATA 27: Flight Controls (Fly-by-Wire)
- ATA 28: Fuel (Hydrogen)
- ATA 29: Hydraulic Power
- ATA 30: Ice and Rain Protection
- ATA 32: Landing Gear
- ATA 33: Lights
- ATA 34: Navigation
- ATA 36: Pneumatic

#### Structures (ATA 50-57)
- ATA 51: Structures - General
- ATA 52: Doors
- ATA 53: Fuselage (BWB Center Body)
- ATA 54: Nacelles/Pylons
- ATA 55: Stabilizers (If applicable)
- ATA 56: Windows
- ATA 57: Wings (Blended Wing)

#### Propulsion (ATA 70-80)
- ATA 71: Power Plant (Electric Motors)
- ATA 72: Engine (Turbine/Fuel Cell if hybrid)
- ATA 73: Engine Fuel and Control
- ATA 74: Ignition
- ATA 75: Air
- ATA 76: Engine Controls
- ATA 77: Engine Indicating
- ATA 78: Exhaust
- ATA 79: Oil
- ATA 80: Starting (Electric Propulsion)

#### Custom Systems
- **ATA 85:** Green-E Battery Energy Storage
- **ATA 95:** AI/NN Orchestration Systems (NN-ECS, NN-FCS, NN-IMA)
- **ATA 28H:** Hydrogen Storage and Distribution
- **ATA 85-30:** Circularity Infrastructure (ANCHORS)

### 4. Bill of Materials (BOM)
- Top-level aircraft BOM
- System-level BOMs (per ATA)
- Assembly BOMs
- Part-level details with metadata
- Material specifications
- Supplier information
- UTCS identifiers for all parts

### 5. Design Documentation
- Detail drawings (2D manufacturing drawings)
- 3D model annotations
- Design rationale documentation
- Trade study results
- Material and process specifications
- Surface finish and treatment requirements
- Tolerance analysis and GD&T

### 6. Digital Mock-Up (DMU)
- Assembly sequence validation
- Interference checking
- Maintainability analysis
- Human factors and ergonomics
- Serviceability and access studies

## Deliverables

- Master 3D CAD models (Catia, NX, BlenderCAD)
- 2D manufacturing drawings
- System architecture models (SysML)
- Complete BOM with metadata
- Design specifications per ATA chapter
- Interface Control Documents (preliminary)
- Digital mock-up studies
- Design review packages
- OPT-IN organized design repository

## Tools & Methods

### CAD Tools
- **Catia V5/V6:** Aerospace-grade parametric modeling
- **Siemens NX:** Advanced surfacing and analysis
- **BlenderCAD:** Open-source alternative for conceptual design
- **CREO:** Parametric design alternative

### MBSE Tools
- **Cameo Systems Modeler:** SysML modeling
- **CATIA Magic:** Model-based architecture
- **Rhapsody:** System modeling and simulation

### PLM/PDM
- **Teamcenter:** Product lifecycle management
- **Windchill:** Product data management
- **3DEXPERIENCE Platform:** Collaborative design environment

### Analysis Integration
- Link to LC-1.6 for FEM/CFD analysis
- Automated model export for simulation
- Design optimization loops

## Integration

- **From LC-1.3:** Requirements drive design decisions
- **From LC-1.2:** Safety constraints embedded in design
- **To LC-1.5:** Interface definitions and ICDs
- **To LC-1.6:** Models for engineering analysis
- **To LC-2.1:** Manufacturing drawings and tooling design
- **OPT-IN:** Design artifact organization
- **UTCS:** Version control and configuration management
- **GenCCC:** Automated design validation and checking

## Design Standards

- **ATA iSpec 2200:** Design data organization
- **ISO 1101:** Geometric dimensioning and tolerancing
- **MIL-STD-31000A:** Technical data packages
- **AS9100:** Quality management for aerospace
- **EN 9100:** European aerospace quality standard

## Configuration Management

- Design baselines and change control
- Release management
- Effectivity tracking
- Variant management for different aircraft configurations
- UTCS-based version control

## BWB-Specific Design Considerations

- **Aerodynamic Integration:** Seamless blending of wing and fuselage
- **Structural Efficiency:** Load paths in unconventional geometry
- **Cabin Pressurization:** Wide-body pressure vessel design
- **Center of Gravity:** Hydrogen fuel consumption effects
- **Emergency Egress:** Passenger evacuation in BWB configuration
- **Manufacturing Breaks:** Structural joints and assembly strategy
