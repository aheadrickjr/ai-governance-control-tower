# Schema Notes: Commercial Credit AI Governance Control Tower

## Purpose

These sample files define the first structured data layer for the AI Governance Control Tower for Commercial Credit Modernization.

The files are intentionally lightweight. They are designed to support a portfolio sprint, not to represent a full production banking data model.

The goal is to demonstrate how AI governance, data governance, regulatory awareness, control mapping, human review, and audit evidence can be represented in a practical data structure.

---

## Files Created

| File | Purpose |
|---|---|
| `data/sample_ai_use_cases.csv` | Defines proposed AI use cases for commercial credit and leasing workflows |
| `data/sample_data_sources.csv` | Defines source systems and data stores used by the AI governance process |
| `data/sample_regulatory_controls.csv` | Defines governance controls mapped to regulatory, risk, data, and AI concerns |
| `data/sample_governance_decisions.csv` | Captures review outcomes, required controls, pilot status, and evidence notes |

---

## `sample_ai_use_cases.csv`

This file acts as the AI use-case intake register.

Key fields:

| Field | Meaning |
|---|---|
| `use_case_id` | Unique identifier for each proposed AI use case |
| `use_case_name` | Plain-English name of the use case |
| `business_domain` | Business domain covered by the control tower |
| `product_type` | Commercial credit or leasing product area |
| `ai_capability` | Type of AI assistance being proposed |
| `business_owner` | Business group accountable for the process |
| `system_owner` | Technology or platform owner |
| `risk_level` | Initial risk tier |
| `human_review_required` | Whether a human must review the AI output |
| `credit_decision_impact` | Whether the use case may influence a credit decision |
| `df1071_applicable` | Whether Section 1071 / DF1071 may apply |
| `aml_kyc_relevance` | Whether AML or KYC concerns are relevant |
| `data_sensitivity` | Sensitivity of the data used |
| `approval_status` | Current governance review status |
| `notes` | Additional explanation |

---

## `sample_data_sources.csv`

This file acts as the data-source register.

Key fields:

| Field | Meaning |
|---|---|
| `source_id` | Unique identifier for each source |
| `source_name` | Name of the system, dataset, or repository |
| `source_type` | Type of source system |
| `business_domain` | Business domain associated with the source |
| `product_area` | Product or process area supported |
| `system_owner` | Technology owner |
| `data_owner` | Business or governance owner |
| `contains_pii` | Whether the source contains personally identifiable information |
| `contains_financial_data` | Whether the source contains financial data |
| `contains_regulatory_data` | Whether the source contains regulatory reporting or compliance data |
| `contains_collateral_data` | Whether the source contains collateral or asset data |
| `data_sensitivity` | Overall sensitivity level |
| `source_trust_level` | Initial trust rating for governance purposes |
| `governance_notes` | Explanation of governance concerns |

---

## `sample_regulatory_controls.csv`

This file maps governance controls to risk, regulatory, and operational concerns.

Key fields:

| Field | Meaning |
|---|---|
| `control_id` | Unique identifier for the control |
| `control_name` | Name of the governance control |
| `control_domain` | Governance area such as AI governance, data governance, credit risk, or compliance |
| `applicable_product_area` | Product area where the control applies |
| `regulatory_driver` | Policy, regulation, or governance driver |
| `risk_addressed` | Risk the control is intended to address |
| `control_type` | Preventive, detective, or corrective |
| `human_review_required` | Whether human review is part of the control |
| `evidence_required` | Evidence needed to prove the control operated |
| `control_owner` | Group responsible for the control |
| `notes` | Additional explanation |

---

## `sample_governance_decisions.csv`

This file records governance review outcomes.

Key fields:

| Field | Meaning |
|---|---|
| `decision_id` | Unique identifier for the decision |
| `use_case_id` | Related AI use case |
| `review_date` | Date of review |
| `review_status` | Governance decision status |
| `risk_level` | Risk level assigned during review |
| `required_controls` | Control IDs required before pilot or production use |
| `approved_for_pilot` | Whether the use case may proceed to controlled pilot |
| `approved_for_production` | Whether the use case may be used in production |
| `decision_owner` | Group accountable for the decision |
| `decision_notes` | Explanation of the decision |
| `next_review_date` | Date for follow-up review |

---

## Design Boundary

This sample model focuses on commercial credit and leasing.

In scope:

- Commercial loans
- CRE loans
- Equipment finance
- Commercial leases
- Asset-based lending
- Small business lending where DF1071 / Section 1071 may apply
- Borrower and guarantor review
- Collateral and asset review
- AI-assisted underwriting support
- Snowflake-style governed data platform patterns

Out of scope:

- Residential mortgage origination
- Consumer mortgage lending
- NMLS licensing workflows
- SAFE Act loan originator controls
- HELOC or consumer home equity lending
- Fully automated credit decisions

---

## Governance Principle

AI may assist the process, but AI does not own the decision.

The control tower assumes that final underwriting, approval, denial, pricing, exception handling, AML disposition, and regulatory sign-off remain human-owned.