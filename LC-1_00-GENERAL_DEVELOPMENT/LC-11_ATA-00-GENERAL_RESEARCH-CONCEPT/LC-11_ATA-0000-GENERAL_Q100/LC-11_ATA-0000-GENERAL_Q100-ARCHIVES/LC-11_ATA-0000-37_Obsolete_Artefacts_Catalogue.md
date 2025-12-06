# LC-11_ATA-0000-37 Obsolete Artefacts Catalogue

## Purpose

Flat catalogue of obsolete Q100 concept artefacts, documenting what was superseded, when, why, and what replaced it. This provides full traceability for configuration management and decision provenance.

## Catalogue Format

Each entry follows the pattern:
```
Old Path → New Path (or "Deprecated")
Archive Date: YYYY-MM-DD
Reason: Brief explanation
Status: Superseded | Obsolete | Merged | Deprecated
```

---

## Obsolete Artefacts

### Concept Baselines

**Entry 001:**
```
Old: LC-11_0010-12_BaselineA_Definition.md (V1R0)
New: LC-11_0010-12_BaselineA_Definition.md (V1R1)
Archive Date: TBD
Reason: Updated with aerodynamic refinement results
Status: Superseded
```

**Entry 002:**
```
Old: LC-11_0010-13_BaselineB_Definition.md (V1R0)
New: Merged into Baseline C
Archive Date: TBD
Reason: Baseline B and C consolidated after trade study
Status: Merged
```

---

### Parametric Studies

**Entry 003:**
```
Old: LC-11_PARAM-Wing_Sweep_V1R0.md
New: LC-11_PARAM-Wing_Sweep_V2R0.md
Archive Date: TBD
Reason: Updated model with improved aerodynamic analysis
Status: Superseded
```

**Entry 004:**
```
Old: LC-11_PARAM-Tank_Sizing_Initial.md
New: Incorporated into LC-11_0010-11_Energy_Sizing_Prelim.md
Archive Date: TBD
Reason: Results integrated into baseline document
Status: Merged
```

---

### Trade Studies

**Entry 005:**
```
Old: LC-11_TRADE-Propulsion_Options_V1R0.md
New: LC-11_TRADE-Propulsion_Options_V2R0.md
Archive Date: TBD
Reason: Additional option evaluated, evaluation criteria updated
Status: Superseded
```

**Entry 006:**
```
Old: LC-11_TRADE-Control_Surfaces_Prelim.md
New: Deprecated
Archive Date: TBD
Reason: Concept direction changed, control strategy revised
Status: Obsolete
```

---

### Constraints and Envelopes

**Entry 007:**
```
Old: LC-11_CONSTR-Takeoff_V1R0.md
New: LC-11_CONSTR-Takeoff_V2R0.md
Archive Date: TBD
Reason: Updated with refined mass and aerodynamics
Status: Superseded
```

**Entry 008:**
```
Old: LC-11_CONSTR-CG_Envelope_Prelim.md
New: LC-11_CONSTR-CG_Envelope_Final.md
Archive Date: TBD
Reason: Detailed analysis completed, preliminary replaced
Status: Superseded
```

---

### Seed Requirements

**Entry 009:**
```
Old: LC-11_REQSEED-Airframe_V1R0.md
New: Transitioned to LC-13 formal requirements
Archive Date: TBD
Reason: Seed requirements incorporated into formal spec
Status: Superseded (transitioned to formal requirements)
```

**Entry 010:**
```
Old: LC-11_REQSEED-Propulsion_Initial.md
New: Deprecated
Archive Date: TBD
Reason: Propulsion architecture changed, requirements re-baselined
Status: Obsolete
```

---

### Risk Research

**Entry 011:**
```
Old: LC-11_RISK-H2_Leak_V1R0.md
New: Transitioned to Programme Risk Register
Archive Date: TBD
Reason: Risk accepted into formal risk management process
Status: Superseded (transitioned to formal risk register)
```

**Entry 012:**
```
Old: LC-11_RISK-Manufacturing_Complexity_Prelim.md
New: LC-11_RISK-Manufacturing_Complexity_V2R0.md
Archive Date: TBD
Reason: Additional manufacturing feasibility study completed
Status: Superseded
```

---

### Reviews and Decisions

**Entry 013:**
```
Old: LC-11_REVIEW-MCR0_Draft_Minutes.md
New: LC-11_REVIEW-MCR0_Final_Minutes.md
Archive Date: TBD
Reason: Final minutes approved and released
Status: Superseded
```

**Entry 014:**
```
Old: LC-11_REVIEW-Internal_Aero_Review_2025-01.md
New: Archived (review complete)
Archive Date: TBD
Reason: Review completed, actions closed
Status: Archived
```

---

### Miscellaneous Artefacts

**Entry 015:**
```
Old: LC-11_0010-XX_Preliminary_Sketch.svg
New: LC-11_0010-04_Geometry_Definition.md (formal definition)
Archive Date: TBD
Reason: Informal sketch replaced by formal geometry definition
Status: Superseded
```

**Entry 016:**
```
Old: LC-11_TEMP-Analysis_Sandbox.md
New: Deprecated
Archive Date: TBD
Reason: Temporary working document, results incorporated elsewhere
Status: Obsolete
```

---

## Usage Notes

### For Configuration Management
- All obsolete artefacts remain accessible for audit purposes
- Version control history preserved
- Archive packages may contain copies for offline access

### For Traceability
- Each entry maintains link to replacement or destination
- Decision rationale documented
- Timeline of changes preserved

### For Governance
- Obsolete artefacts reviewed quarterly
- Archive catalogue updated as part of baseline freezes
- CAB oversight for major artefact deprecation

---

## Archive Storage

**Physical/Digital Archive:**
- Obsolete versions stored in ASSETS/ subdirectory
- Tagged in version control system
- Backup copies in programme document management system

**Retention Policy:**
- Obsolete artefacts retained for full programme lifecycle
- Extended retention for certification and compliance evidence
- Disposal only after programme closure and regulatory periods

---

## Related Documents

- **Change History Summary:** LC-11_ATA-0000-38_Change_History_Summary.md
- **Concept Evolution Log:** LC-11_0010-03_Concept_Evolution_Log.md
- **Archives Overview:** LC-11_ATA-0000-29_Archives_Overview.md

---

**Document Control:**
- **UTCS-ID:** LC-11_ATA-0000-37
- **Version:** 1.0
- **Status:** Active
- **Last Updated:** 2025-12-06
- **Next Review:** Quarterly or at baseline freeze
