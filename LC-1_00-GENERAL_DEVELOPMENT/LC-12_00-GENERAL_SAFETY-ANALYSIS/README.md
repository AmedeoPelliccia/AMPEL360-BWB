# LC-1.2 Safety Analysis (ARP4761 / System Safety)

## Purpose
Conduct comprehensive safety assessment activities in accordance with ARP4761 guidelines to ensure the AMPEL360 BWB aircraft meets certification safety requirements.

## Scope

This phase implements the systematic safety assessment process required for civil aircraft certification, including:

- **FHA (Functional Hazard Assessment):** Identification of hazards and failure conditions
- **PSSA (Preliminary System Safety Assessment):** Architecture-level safety analysis
- **SSA (System Safety Assessment):** Detailed safety validation
- **Preliminary Hazard Logs:** Documentation of identified hazards
- **Failure Conditions Classification:** Severity and probability assessment
- **Safety-Driven Architectural Constraints:** Design requirements from safety analysis
- **DAL Allocation:** Development Assurance Level assignment per DO-178C/DO-254
- **Independence Requirements:** Segregation and partitioning requirements

## Key Activities

### 1. Functional Hazard Assessment (FHA)
- Identify aircraft and system functions
- Determine failure conditions and effects
- Classify failure condition severity (Catastrophic, Hazardous, Major, Minor, No Safety Effect)
- Define safety objectives

### 2. Preliminary System Safety Assessment (PSSA)
- Preliminary architecture evaluation
- Allocation of safety requirements
- Identification of common cause analysis needs
- Preliminary zonal safety analysis
- Particular risks assessment

### 3. Safety Requirements Allocation
- DAL assignment (Level A through E)
- Independence and segregation requirements
- Redundancy and dissimilarity requirements
- Built-in test and monitoring requirements

### 4. Hazard Log Management
- Centralized hazard tracking
- Status monitoring and closure
- Traceability to design mitigations
- Review and approval workflow

### 5. Common Cause Analysis
- Common Mode Failures (CMF)
- Zonal Safety Analysis (ZSA)
- Particular Risk Analysis (PRA)
- Software/Hardware interaction hazards

### 6. Safety Integration
- Integration with system architecture (LC-1.4)
- Safety requirements flow-down (LC-1.3)
- V&V planning alignment (LC-1.7)
- Certification liaison activities

## Deliverables

- Functional Hazard Assessment (FHA) Report
- Preliminary System Safety Assessment (PSSA) Report
- System Safety Assessment (SSA) Report
- Safety Requirements Specification
- Hazard Log Database
- DAL Assignment Matrix
- Common Cause Analysis Reports
- Safety Case Documentation

## Tools & Methods

- **FTA:** Fault Tree Analysis
- **FMEA/FMECA:** Failure Modes and Effects (Criticality) Analysis
- **ETA:** Event Tree Analysis
- **CCA:** Common Cause Analysis
- **Markov Models:** Reliability and availability analysis
- **Safety Management Tools:** DOORS, Jama, Cameo Safety

## Integration

- **Requirements Engineering (LC-1.3):** Safety requirements flow to system requirements
- **Detailed Design (LC-1.4):** Architecture must comply with safety constraints
- **V&V (LC-1.7):** Safety evidence collection and certification
- **OPT-IN:** Safety governance and neural network (N) safety assurance
- **UTCS:** Traceability of safety artifacts
- **GenCCC:** Automated safety requirement validation

## Standards & References

- **ARP4761:** Guidelines and Methods for Conducting the Safety Assessment Process
- **ARP4754A:** Guidelines for Development of Civil Aircraft and Systems
- **DO-178C:** Software Considerations in Airborne Systems and Equipment Certification
- **DO-254:** Design Assurance Guidance for Airborne Electronic Hardware
- **CS-25/FAR Part 25:** Airworthiness Standards: Transport Category Airplanes
- **CAST-32A:** Multi-core Processor Safety Guidance
- **ARINC 653:** Avionics Application Software Standard Interface

## Hydrogen-Electric Specific Considerations

- Hydrogen storage and distribution hazards
- Electric propulsion safety (ATA 80)
- Battery safety and thermal runaway (Green-E)
- AI/NN system safety assurance (ATA 95)
- Novel BWB structural safety considerations
