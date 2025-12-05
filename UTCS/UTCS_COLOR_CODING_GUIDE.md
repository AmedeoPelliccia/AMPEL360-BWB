# UTCS Color Coding Guide

**Visual Differentiation of LC ID and ATA ID Components**

**Document ID:** UTCS-COLOR-01  
**Version:** 1.0  
**Status:** RELEASE  
**Date:** December 2025

---

## Purpose

This guide defines the color coding scheme for UTCS-LC identifiers to provide visual distinction between different components, making it easier for engineers, operators, and automated systems to parse and understand lifecycle artefact identifiers.

---

## Color Scheme

### Component Colors

| Component | Color | Hex Code | Purpose |
|-----------|-------|----------|---------|
| **LC ID** | <span style="color:#0066cc">**Blue**</span> | `#0066cc` | Lifecycle stage identification (LC-11, LC-22, etc.) |
| **ATA ID** | <span style="color:#cc6600">**Orange**</span> | `#cc6600` | ATA chapter identification (00, 27, 28H, 95, etc.) |
| **ATA DESC** | <span style="color:#666666">**Gray**</span> | `#666666` | ATA description text |
| **FUNC** | <span style="color:#009900">**Green**</span> | `#009900` | Functional descriptor |
| **Version** | <span style="color:#990099">**Purple**</span> | `#990099` | Version and revision (V1R0, etc.) |

---

## HTML Formatting Examples

### Basic Format
```html
<span style="color:#0066cc">LC-11</span>_<span style="color:#cc6600">00</span>-<span style="color:#666666">GENERAL</span>_<span style="color:#009900">CONCEPT-BASELINE</span>_<span style="color:#990099">V1R0</span>.md
```

**Renders as:**
<span style="color:#0066cc">LC-11</span>_<span style="color:#cc6600">00</span>-<span style="color:#666666">GENERAL</span>_<span style="color:#009900">CONCEPT-BASELINE</span>_<span style="color:#990099">V1R0</span>.md

### Advanced Examples

#### Development Stage - CFD Analysis
```html
<span style="color:#0066cc">LC-16</span>_<span style="color:#cc6600">5700</span>-<span style="color:#666666">WINGS</span>_<span style="color:#009900">CFD-CRUISE</span>_<span style="color:#990099">V2R1</span>.dat
```
<span style="color:#0066cc">LC-16</span>_<span style="color:#cc6600">5700</span>-<span style="color:#666666">WINGS</span>_<span style="color:#009900">CFD-CRUISE</span>_<span style="color:#990099">V2R1</span>.dat

#### Hydrogen System Design
```html
<span style="color:#0066cc">LC-14</span>_<span style="color:#cc6600">2800</span>-<span style="color:#666666">HYDROGEN</span>_<span style="color:#009900">CAD-TANK-ASSY</span>_<span style="color:#990099">V3R2</span>.catproduct
```
<span style="color:#0066cc">LC-14</span>_<span style="color:#cc6600">2800</span>-<span style="color:#666666">HYDROGEN</span>_<span style="color:#009900">CAD-TANK-ASSY</span>_<span style="color:#990099">V3R2</span>.catproduct

#### NN Systems Verification
```html
<span style="color:#0066cc">LC-17</span>_<span style="color:#cc6600">9500</span>-<span style="color:#666666">NN-SYSTEMS</span>_<span style="color:#009900">TEST-PLAN-NN-FCS</span>_<span style="color:#990099">V1R0</span>.md
```
<span style="color:#0066cc">LC-17</span>_<span style="color:#cc6600">9500</span>-<span style="color:#666666">NN-SYSTEMS</span>_<span style="color:#009900">TEST-PLAN-NN-FCS</span>_<span style="color:#990099">V1R0</span>.md

#### Manufacturing - Test Report
```html
<span style="color:#0066cc">LC-22</span>_<span style="color:#cc6600">00</span>-<span style="color:#666666">GENERAL</span>_<span style="color:#009900">FLIGHT-TEST-REPORT</span>_<span style="color:#990099">V1R0</span>.md
```
<span style="color:#0066cc">LC-22</span>_<span style="color:#cc6600">00</span>-<span style="color:#666666">GENERAL</span>_<span style="color:#009900">FLIGHT-TEST-REPORT</span>_<span style="color:#990099">V1R0</span>.md

#### Operations - MRO Procedure
```html
<span style="color:#0066cc">LC-32</span>_<span style="color:#cc6600">2100</span>-<span style="color:#666666">AIR-CONDITIONING</span>_<span style="color:#009900">MROPROC-ECS-SENSOR</span>_<span style="color:#990099">V1R0</span>.md
```
<span style="color:#0066cc">LC-32</span>_<span style="color:#cc6600">2100</span>-<span style="color:#666666">AIR-CONDITIONING</span>_<span style="color:#009900">MROPROC-ECS-SENSOR</span>_<span style="color:#990099">V1R0</span>.md

#### Circularity - Digital Product Passport
```html
<span style="color:#0066cc">LC-34</span>_<span style="color:#cc6600">8500</span>-<span style="color:#666666">GREEN-E-BATTERY</span>_<span style="color:#009900">DPP-BATTERY-PACK-001</span>_<span style="color:#990099">V1R0</span>.json
```
<span style="color:#0066cc">LC-34</span>_<span style="color:#cc6600">8500</span>-<span style="color:#666666">GREEN-E-BATTERY</span>_<span style="color:#009900">DPP-BATTERY-PACK-001</span>_<span style="color:#990099">V1R0</span>.json

---

## Markdown Badge Style (Alternative)

For systems that don't support HTML color tags, use badge-style formatting:

```markdown
![LC-11](https://img.shields.io/badge/LC-11-0066cc)
![00](https://img.shields.io/badge/ATA-00-cc6600)
![GENERAL](https://img.shields.io/badge/-GENERAL-666666)
![CONCEPT](https://img.shields.io/badge/FUNC-CONCEPT--BASELINE-009900)
![V1R0](https://img.shields.io/badge/VER-V1R0-990099)
```

**Renders as:**

![LC-11](https://img.shields.io/badge/LC-11-0066cc) _ ![00](https://img.shields.io/badge/ATA-00-cc6600) - ![GENERAL](https://img.shields.io/badge/-GENERAL-666666) _ ![CONCEPT](https://img.shields.io/badge/FUNC-CONCEPT--BASELINE-009900) _ ![V1R0](https://img.shields.io/badge/VER-V1R0-990099)

---

## Code Syntax Highlighting

For code blocks and technical documentation, use syntax highlighting:

````markdown
```yaml
# Example UTCS identifier with color annotations
identifier:
  lc_stage: "LC-16"      # Blue: Lifecycle stage (Analysis)
  ata_index: "5700"      # Orange: ATA chapter (Wings)
  ata_desc: "WINGS"      # Gray: Description
  function: "CFD-CRUISE" # Green: Functional descriptor
  version: "V2R1"        # Purple: Version/Revision
  
full_id: "LC-16_5700-WINGS_CFD-CRUISE_V2R1.dat"
```
````

---

## Application Guidelines

### Documentation
- Use HTML color tags in markdown documentation
- Use badges in README files and summary documents
- Use syntax highlighting in technical specifications

### Presentations
- Use color-coded text in slides
- Maintain consistent color scheme across all materials
- Provide legend on first slide using UTCS identifiers

### Software Tools
- Implement color coding in file browsers and explorers
- Use colors in search results and listings
- Apply colors in visualization dashboards

### Printed Materials
- Ensure colors are distinguishable in grayscale
- Use bold/italic as fallback for color-blind accessibility
- Test print outputs before mass production

---

## Accessibility Considerations

### Color-Blind Friendly
- **Blue (#0066cc):** Distinguishable by most color-blind types
- **Orange (#cc6600):** High contrast with blue
- **Use patterns:** Combine with bold, italic, or underline when needed

### High Contrast Mode
- All colors have sufficient contrast ratio (4.5:1 minimum)
- Fallback to bold text when colors unavailable

### Screen Readers
- HTML color tags don't affect screen reader functionality
- Ensure proper semantic markup for accessibility

---

## Implementation Checklist

- [ ] Update documentation templates with color coding
- [ ] Configure GenCCC to output colored identifiers
- [ ] Update CAOS dashboard with color-coded UTCS IDs
- [ ] Train teams on color scheme meaning
- [ ] Verify color rendering in all documentation systems
- [ ] Test accessibility compliance
- [ ] Update style guide for presentations

---

## Examples by Lifecycle Stage

### LC-1 Development (Blue)
- <span style="color:#0066cc">LC-11</span>: Research & Concept
- <span style="color:#0066cc">LC-12</span>: Safety Analysis
- <span style="color:#0066cc">LC-13</span>: Requirements
- <span style="color:#0066cc">LC-14</span>: Design
- <span style="color:#0066cc">LC-15</span>: Interfaces
- <span style="color:#0066cc">LC-16</span>: Analysis
- <span style="color:#0066cc">LC-17</span>: Verification

### LC-2 Manufacturing (Blue)
- <span style="color:#0066cc">LC-21</span>: Prototyping
- <span style="color:#0066cc">LC-22</span>: Test & Certification
- <span style="color:#0066cc">LC-23</span>: FAL & Production
- <span style="color:#0066cc">LC-24</span>: Supply Chain

### LC-3 Operations (Blue)
- <span style="color:#0066cc">LC-31</span>: Configuration
- <span style="color:#0066cc">LC-32</span>: MRO
- <span style="color:#0066cc">LC-33</span>: Customer Support
- <span style="color:#0066cc">LC-34</span>: Spares & Circularity

### Key ATA Chapters (Orange)
- <span style="color:#cc6600">00</span>: General
- <span style="color:#cc6600">27</span>: Flight Controls
- <span style="color:#cc6600">28</span>/<span style="color:#cc6600">28H</span>: Fuel/Hydrogen
- <span style="color:#cc6600">42</span>: Integrated Modular Avionics
- <span style="color:#cc6600">57</span>: Wings
- <span style="color:#cc6600">80</span>: Electric Propulsion
- <span style="color:#cc6600">85</span>: Green-E Battery
- <span style="color:#cc6600">95</span>: NN Systems

---

## Complete Formatted Example

### Full UTCS Identifier with All Colors

<span style="color:#0066cc">**LC-16**</span>_<span style="color:#cc6600">**5700**</span>-<span style="color:#666666">**WINGS**</span>_<span style="color:#009900">**CFD-CRUISE**</span>_<span style="color:#990099">**V2R1**</span>**.dat**

**Component Breakdown:**
- <span style="color:#0066cc">**LC-16**</span> → Lifecycle Stage: Development - Analysis
- <span style="color:#cc6600">**5700**</span> → ATA Index: 57 (Wings) + 00 (System level)
- <span style="color:#666666">**WINGS**</span> → ATA Description: Wings system
- <span style="color:#009900">**CFD-CRUISE**</span> → Function: CFD analysis for cruise condition
- <span style="color:#990099">**V2R1**</span> → Version: 2, Revision: 1
- **.dat** → File extension: Data file

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 UTCS Governance
