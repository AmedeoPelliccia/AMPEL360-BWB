# LC-15 Interfaces & Constituency Assemblies — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-15 Interfaces & Constituency Assemblies.

---

## Primary Audiences

| Role                                      | Description                                                                 |
|-------------------------------------------|-----------------------------------------------------------------------------|
| **Integration Engineering**               | Leads interface definition and integration planning                         |
| **MBSE Team**                             | Maintains interface models and digital architecture                         |
| **Avionics/Power/Mechanical System Leads**| Domain experts defining interfaces for their systems                        |

---

## Artefacts & Roles

### ICD (Interface Control Document)

| Artefact                             | Responsible (R) | Accountable (A) | Consulted (C)        | Informed (I) |
|--------------------------------------|-----------------|-----------------|----------------------|--------------|
| ICD (Interface Control Document)     | Integration     | CE              | All system owners    | V&V          |

**Description:** Comprehensive specification of all mechanical, electrical, software, and data interfaces.

**Key Activities:**
- Define mechanical mounting interfaces
- Define electrical connectors and pin assignments
- Define data bus protocols and message formats
- Define software APIs and service interfaces
- Coordinate interface compatibility across systems

---

### Assembly Tree

| Artefact      | Responsible (R) | Accountable (A) | Consulted (C)   | Informed (I) |
|---------------|-----------------|-----------------|-----------------|--------------|
| Assembly tree | Integration     | Domain Lead     | Manufacturing   | Program      |

**Description:** Hierarchical breakdown of aircraft structure and system assemblies showing constituency.

**Key Activities:**
- Define assembly hierarchy (aircraft → major assemblies → subassemblies → parts)
- Establish assembly sequences and dependencies
- Coordinate with manufacturing planning (LC-2.3)
- Maintain Bill of Materials (BOM) structure

---

### Port/Bus Architecture (A429, AFDX, CAN, NN-bus)

| Artefact                                        | Responsible (R)     | Accountable (A) | Consulted (C) | Informed (I) |
|-------------------------------------------------|---------------------|-----------------|---------------|--------------|
| Port/bus architecture (A429, AFDX, CAN, NN-bus) | Avionics & AI Core  | CE              | Systems       | Safety       |

**Description:** Data communication architecture including legacy and novel AI/NN buses.

**Key Activities:**
- Define AFDX (Avionics Full-Duplex Switched Ethernet) network topology
- Define ARINC 429 bus allocation
- Define CAN bus architecture for vehicle systems
- Define NN-bus for AI/NN system communication (ATA 95)
- Bandwidth allocation and latency analysis

---

### Installation Rules

| Artefact           | Responsible (R) | Accountable (A) | Consulted (C)              | Informed (I)  |
|--------------------|-----------------|-----------------|----------------------------|---------------|
| Installation rules | Integration     | Domain Lead     | Manufacturing, MRO         | Certification |

**Description:** Standards and procedures for installing, connecting, and integrating aircraft systems.

**Key Activities:**
- Define torque specifications for fasteners
- Define wire routing and EWIS installation rules
- Define fluid line installation standards
- Define clearance and tolerance requirements
- Define accessibility for maintenance

---

## Information Architecture (IA)

### Folder Structure
```
LC-15_00-GENERAL_INTERFACES/
├── RACI_MATRIX.md (this file)
├── README.md
├── ICD_Interface_Control_Documents/
│   ├── Mechanical_Interfaces/
│   │   ├── Structural_Attach_Points_ICD_V*.pdf
│   │   ├── Fastener_Standards_ICD_V*.pdf
│   │   └── Mounting_Interfaces_ICD_V*.pdf
│   ├── Electrical_Interfaces/
│   │   ├── Power_Distribution_ICD_V*.pdf
│   │   ├── Connector_Standards_ICD_V*.pdf
│   │   └── Wire_Harness_ICD_V*.pdf
│   ├── Data_Interfaces/
│   │   ├── AFDX_Network_ICD_V*.pdf
│   │   ├── ARINC_429_ICD_V*.pdf
│   │   ├── CAN_Bus_ICD_V*.pdf
│   │   └── NN_Bus_ICD_V*.pdf
│   └── Software_Interfaces/
│       ├── API_Specifications_V*.pdf
│       └── Service_Interfaces_V*.pdf
├── Assembly_Trees/
│   ├── Aircraft_Assembly_Breakdown_V*.pdf
│   ├── BOM_Structure_V*.xlsx
│   └── Assembly_Sequence_Plans/
├── Bus_Architecture/
│   ├── AFDX_Topology_V*.pdf
│   ├── ARINC_429_Bus_Allocation_V*.pdf
│   ├── CAN_Bus_Architecture_V*.pdf
│   ├── NN_Bus_Specification_V*.pdf
│   └── Network_Bandwidth_Analysis/
└── Installation_Rules/
    ├── Installation_Standards_Manual_V*.pdf
    ├── Torque_Specifications/
    ├── Wire_Routing_Standards/
    └── Maintenance_Access_Requirements/
```

### UTCS Naming Convention
- **Format:** <span style="color:#0066cc">`LC-15`</span>`_`<span style="color:#cc6600">`{ATAIDX}`</span>`-`<span style="color:#666666">`{ATADESC}`</span>`_`<span style="color:#009900">`{FUNC}`</span>`_`<span style="color:#990099">`V{x}R{y}`</span>
- **Example:** <span style="color:#0066cc">`LC-15`</span>`_`<span style="color:#cc6600">`42`</span>`-`<span style="color:#666666">`IMA`</span>`_`<span style="color:#009900">`ICD-AFDX-NETWORK`</span>`_`<span style="color:#990099">`V1R0`</span>`.pdf`
- **Example:** <span style="color:#0066cc">`LC-15`</span>`_`<span style="color:#cc6600">`00`</span>`-`<span style="color:#666666">`GENERAL`</span>`_`<span style="color:#009900">`ASSEMBLY-TREE-AIRCRAFT`</span>`_`<span style="color:#990099">`V2R1`</span>`.xlsx`
- **Example:** <span style="color:#0066cc">`LC-15`</span>`_`<span style="color:#cc6600">`95`</span>`-`<span style="color:#666666">`NN-SYSTEMS`</span>`_`<span style="color:#009900">`ICD-NN-BUS`</span>`_`<span style="color:#990099">`V1R0`</span>`.pdf`

---

## Governance & Approval

### Review Cycles
- **Weekly:** Integration team coordinates interface definitions
- **Bi-weekly:** System owners review interface compatibility
- **Monthly:** CAB reviews interface architecture
- **Milestone:** CE approves ICD baselines

### Decision Authority
- **Chief Engineer:** Approves aircraft-level interface architecture
- **Integration Lead:** Day-to-day interface coordination
- **System Owners:** Approve interfaces for their systems

### Interface Control Board (ICB)
- Reviews all interface changes
- Assesses impact on connected systems
- Approves interface baseline updates
- Coordinates with configuration management (LC-3.1)

---

## Integration Points

### Upstream (Inputs)
- **LC-13:** Requirements define interface needs
- **LC-14:** Design defines physical and logical interfaces

### Downstream (Outputs)
- **LC-16 Analysis:** Interface models for integrated simulations
- **LC-17 V&V:** Interface testing and validation
- **LC-21 Prototyping:** Installation rules guide assembly
- **LC-32 MRO:** Installation rules guide maintenance

### Lateral (Parallel)
- **MBSE:** Interface models in SysML
- **UTCS:** Interfaces uniquely identified and versioned
- **GenCCC:** Interface validation and consistency checking

---

## Interface Types

### Mechanical Interfaces
- Structural attach points and load paths
- Fastener types, sizes, and torque specifications
- Clearances and tolerances
- Accessibility for assembly and maintenance

### Electrical Interfaces
- Power distribution (28V DC, 230V AC, 540V DC for electric propulsion)
- Connector types and pin assignments (D-sub, MIL-DTL, etc.)
- Wire gauge and insulation standards
- Grounding and bonding requirements

### Data Interfaces
- **AFDX:** High-speed avionics network (100 Mbps, dual redundant)
- **ARINC 429:** Legacy avionics data bus
- **CAN:** Controller Area Network for vehicle systems
- **NN-bus:** Neural network communication bus (novel for ATA 95)

### Software Interfaces
- API specifications for software components
- Service-oriented architecture (SOA) interfaces
- Operating system interfaces (ARINC 653 for IMA)
- AI/NN model interfaces

---

## Novel Interface Considerations

### Hydrogen Systems (ATA 28H)
- Cryogenic fluid interfaces with thermal insulation
- Leak detection sensor interfaces
- Pressure and temperature monitoring
- Safety shutoff valve interfaces

### Electric Propulsion (ATA 80)
- High-voltage power distribution (540V DC, 800V DC)
- Motor controller interfaces
- Inverter and converter connections
- Battery management system (BMS) interfaces

### AI/NN Systems (ATA 95)
- NN-bus protocol and message formats
- Real-time data streaming interfaces
- Model update and versioning interfaces
- Safety monitoring and override interfaces

---

## Key Principles

1. **Standardization:** Use industry-standard interfaces where possible
2. **Modularity:** Enable plug-and-play assembly and replacement
3. **Traceability:** All interfaces uniquely identified and version controlled
4. **Compatibility:** Ensure electrical, mechanical, and logical compatibility
5. **Maintainability:** Design interfaces for ease of assembly and disassembly

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Integration Engineering
