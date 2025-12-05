# LC-24 Supply Chain & Industrialisation — RACI Matrix

## Purpose
This document defines the **Responsible, Accountable, Consulted, and Informed (RACI)** roles for all artefacts and activities within LC-24 Supply Chain & Industrialisation.

---

## Primary Audiences

| Role                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| **Supply Chain**            | Manages supplier relationships, contracts, and material flow                |
| **Procurement**             | Handles purchasing, negotiations, and supplier qualification                |
| **Quality**                 | Ensures supplier quality and performs audits                                |
| **Production Engineering**  | Coordinates industrialization and supplier technical requirements           |

---

## Artefacts & Roles

### Supplier Technical Packages

| Artefact                    | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------------|-----------------|-----------------|---------------|--------------|
| Supplier technical packages | Supply Chain    | Production      | Engineering   | Quality      |

**Description:** Technical specifications, drawings, and requirements packages provided to suppliers.

---

### Procurement Specifications

| Artefact              | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|-----------------------|-----------------|-----------------|---------------|--------------|
| Procurement specs     | Supply Chain    | Production      | Design        | Legal        |

**Description:** Contractual and technical specifications for procured parts and materials.

---

### Industrial Readiness

| Artefact             | Responsible (R) | Accountable (A) | Consulted (C)  | Informed (I) |
|----------------------|-----------------|-----------------|----------------|--------------|
| Industrial readiness | Production      | CE              | Supply chain   | Program      |

**Description:** Assessment of supplier and production system readiness for serial production.

---

## Information Architecture (IA)

### Folder Structure
```
LC-24_00-GENERAL_SUPPLY-CHAIN/
├── RACI_MATRIX.md (this file)
├── README.md
├── Supplier_Packages/
│   ├── LC-24_5700-WINGS_SUPPLIER-PKG-COMPOSITE_V*R*.pdf
│   ├── LC-24_2800-HYDROGEN_SUPPLIER-PKG-TANKS_V*R*.pdf
│   └── LC-24_8000-ELECTRIC-PROPULSION_SUPPLIER-PKG-MOTORS_V*R*.pdf
├── Procurement/
│   ├── LC-24_00-GENERAL_PROCUREMENT-SPEC-MASTER_V*R*.pdf
│   ├── Contracts/
│   └── Supplier_Qualifications/
└── Industrialization/
    ├── LC-24_00-GENERAL_INDUSTRIAL-READINESS-ASSESSMENT_V*R*.pdf
    ├── Supplier_Audits/
    └── Production_Capacity_Analysis/
```

### UTCS Naming Convention
- **Format:** `LC-24_{ATAIDX}-{ATADESC}_{FUNC}_V{x}R{y}`
- **Example:** `LC-24_8000-ELECTRIC-PROPULSION_SUPPLIER-PKG-MOTOR_V1R0.pdf`

---

**Document Control:**
- **Version:** 1.0
- **Date:** December 2025
- **Status:** Released
- **Owner:** AMPEL360 Supply Chain Management
