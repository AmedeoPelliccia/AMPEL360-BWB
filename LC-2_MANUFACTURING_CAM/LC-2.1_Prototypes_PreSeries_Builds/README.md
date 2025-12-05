# LC-2.1 Prototypes / Pre-Series Builds

## Purpose
Develop and validate manufacturing processes, tooling, and assembly procedures through prototype and pre-series aircraft builds.

## Scope

This phase encompasses the transition from engineering design to manufacturable hardware, including:

- **Manufacturing Drawings:** Detailed 2D drawings with GD&T and manufacturing notes
- **CAM Toolpaths:** CNC programs for machining and automated composite layup
- **Composite Layups:** Detailed ply schedules and manufacturing instructions
- **Jig and Tooling Design:** Assembly fixtures, molds, and manufacturing aids
- **Assembly Instructions:** Step-by-step work instructions with ergonomics considerations
- **Inspection Documentation:** Quality control plans and conformity records

## Key Activities

### 1. Manufacturing Engineering

#### Drawing Release
- Conversion of 3D CAD models to 2D manufacturing drawings
- GD&T (Geometric Dimensioning and Tolerancing) application
- Manufacturing notes and special process callouts
- Material specifications and finish requirements
- Bill of Materials (BOM) finalization
- Drawing approval and release workflow

#### CAM Programming
- **CNC Machining:**
  - 3-axis, 4-axis, 5-axis toolpath generation
  - Tool selection and cutting parameters
  - Fixture and work-holding design
  - Program simulation and verification
  - Post-processing for specific machine controllers

- **Composite Manufacturing:**
  - Automated Fiber Placement (AFP) programs
  - Automated Tape Laying (ATL) paths
  - Laser projection templates for hand layup
  - Cure cycle parameters and monitoring

### 2. Tooling & Fixture Design

#### Assembly Jigs
- Determinant Assembly (DETA) principles
- Drill jigs and templates
- Assembly fixtures for major joins
- Alignment and leveling systems
- Ergonomic considerations for workers

#### Composite Tooling
- Layup molds (male and female)
- Vacuum bagging consumables
- Autoclave-compatible materials
- Core splice fixtures
- Mandrels for hollow structures

#### Machining Fixtures
- Multi-operation work-holding
- Modular fixturing systems
- Soft jaws and custom clamps
- Tombstones for multi-part setups

#### Inspection Fixtures
- CMM fixtures and probes
- Go/No-Go gauges
- Shadow boards for hardware
- Calibration standards

### 3. Composite Manufacturing

#### Ply Schedule Development
- Material selection (carbon fiber, glass fiber, aramid)
- Resin system selection (epoxy, BMI, PEKK)
- Ply orientation sequences
- Core material specification (honeycomb, foam)
- Ply drop-off and termination details
- Co-curing and co-bonding strategies

#### Layup Procedures
- Material storage and handling (freezer, thaw time)
- Surface preparation and cleaning
- Ply cutting templates (manual or CNC)
- Debulking cycles
- Vacuum bagging techniques
- Autoclave or oven cure cycles
- Post-cure inspection (ultrasonic C-scan)

#### Quality Assurance
- Incoming material inspection
- In-process inspections (FOD, ply gaps, wrinkles)
- Cured part inspection (dimensional, NDT)
- First Article Inspection (FAI) per AS9102
- Material certifications and traceability

### 4. Prototype Build Strategy

#### Build Philosophy
- **Engineering Prototypes:** Validate design and interfaces
- **Manufacturing Prototypes:** Validate processes and tooling
- **Pre-Series Aircraft:** Full representative build for certification

#### Build Sequence
1. **Sub-assemblies:** Wings, center body sections, tail (if applicable)
2. **Major Assembly:** Wing-to-body join, systems installation
3. **Final Assembly:** Doors, windows, landing gear, engines/motors
4. **Systems Integration:** Electrical, hydraulic, environmental, avionics
5. **Ground Testing:** Power-on, systems functional tests
6. **Flight Test Preparation:** Instrumentation, pre-flight inspections

### 5. Assembly Instructions & Work Orders

#### Work Instruction Development
- Step-by-step assembly procedures
- Visual aids (photos, 3D illustrations)
- Torque specifications for fasteners
- Sealant and adhesive application
- Cleanliness and FOD prevention
- Safety precautions and PPE requirements

#### Ergonomics Assessment
- Task analysis for repetitive motions
- Lifting and handling assessments
- Accessibility for assembly and inspection
- Workstation design and tooling aids
- Fatigue reduction strategies

#### Digital Work Instructions
- Tablet-based or AR (Augmented Reality) instructions
- Real-time feedback and quality gates
- Automated data capture (torque, time, worker ID)
- Integration with MES (Manufacturing Execution System)

### 6. Inspection & Conformity

#### Inspection Planning
- Inspection points in the build sequence
- Critical characteristics identification
- Inspection methods and tools
- Sample size and frequency
- Hold points for authority inspections

#### Conformity Inspections
- **Type A Inspection:** First article, major changes
- **Type B Inspection:** In-process sampling
- **Type C Inspection:** Final aircraft conformity

#### Non-Destructive Testing (NDT)
- Ultrasonic testing (UT) for composites and bonds
- X-ray for internal structure and fasteners
- Eddy current for surface cracks
- Thermography for delamination detection
- Laser shearography for composite defects

#### Dimensional Inspection
- Coordinate Measuring Machine (CMM)
- Laser trackers for large assemblies
- Photogrammetry for complex surfaces
- Manual measurements with calipers and micrometers

### 7. Lessons Learned & Process Refinement

#### Build Issues Tracking
- Non-conformance reports (NCR)
- Root cause analysis
- Corrective and preventive actions (CAPA)
- Engineering change requests (ECR)

#### Process Improvements
- Build time reduction initiatives
- Quality improvement projects
- Tooling modifications
- Work instruction updates
- Supplier feedback and collaboration

## Deliverables

- Manufacturing drawings and specifications
- CAM programs (CNC, AFP, ATL)
- Composite layup schedules
- Tooling and fixture designs
- Assembly work instructions
- Quality control plans
- Inspection reports and conformity records
- First Article Inspection (FAI) reports
- Prototype build reports
- Lessons learned documentation
- Manufacturing Readiness Level (MRL) assessment

## Tools & Methods

### CAD/CAM Software
- **Catia V5/V6:** Manufacturing preparation
- **Siemens NX CAM:** Advanced CAM programming
- **Mastercam:** CNC programming
- **CGTech VERICUT:** Machining simulation
- **Fibersim:** Composite design and manufacturing

### Manufacturing Execution
- **SAP MES:** Work order management
- **Dassault DELMIA:** Digital manufacturing
- **Siemens Tecnomatix:** Manufacturing planning
- **Plataine:** Composite manufacturing optimization

### Quality Management
- **ETQ Reliance:** Quality management system
- **Discus:** Aerospace quality software
- **SAP QM:** Quality module
- **Minitab:** Statistical analysis

### Inspection Equipment
- **Hexagon CMMs:** Coordinate measuring
- **FARO Laser Trackers:** Large-part measurement
- **GOM ATOS:** Optical 3D scanning
- **Olympus NDT Equipment:** Ultrasonic and X-ray

## Integration

- **From LC-1.4:** Engineering design and CAD models
- **From LC-1.5:** Interface definitions and assembly sequence
- **From LC-1.7:** Design validation and test results
- **To LC-2.2:** Test articles for ground and flight testing
- **To LC-2.3:** Validated processes for production
- **OPT-IN I-axis:** Manufacturing infrastructure
- **UTCS:** Configuration and serial number management
- **GenCCC:** Automated work instruction generation

## Standards & References

- **AS9100:** Aerospace Quality Management
- **AS9102:** First Article Inspection
- **AS9103:** Variation Management of Key Characteristics
- **NADCAP:** Special Process Accreditation (composites, NDT, heat treat, etc.)
- **MIL-HDBK-17:** Composite Materials Handbook
- **NIAR (National Institute for Aviation Research):** Composite standards
- **SAE Aerospace Standards:** Material and process specifications

## Hydrogen-Electric Specific Considerations

### Hydrogen System Manufacturing
- Cryogenic tank fabrication (Type III/IV pressure vessels)
- Hydrogen valve and regulator assembly
- Leak-tight welding and brazing
- Pressure testing and certification
- Safety system integration

### Electric Propulsion Manufacturing
- Electric motor assembly and balancing
- Power electronics manufacturing (inverters, converters)
- High-voltage cable harness assembly
- Battery pack assembly (Green-E)
- Thermal management system integration

### BWB Unique Manufacturing
- Large-area composite panel manufacturing
- Novel structural joint designs
- Cabin pressure vessel integration
- Wing-body blend transitions
- Distributed propulsion installation

## Risk Management

- Manufacturing risk assessment (FMEA)
- Tooling and equipment procurement lead times
- Skilled labor availability and training
- Material availability and long-lead items
- Build schedule contingency planning
- Cost escalation mitigation
