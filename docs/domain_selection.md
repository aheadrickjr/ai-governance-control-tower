# Domain Selection: AI Governance Control Tower for Commercial Credit Modernization

## Sprint Context

This project is part of a 28-day AI Governance Control Tower sprint. The purpose of the project is to build a practical portfolio artifact that demonstrates AI governance, data governance, risk classification, regulatory awareness, human review, and audit evidence for an enterprise banking modernization scenario.

The selected business domain is intentionally narrow enough to build in a 28-day sprint, but broad enough to demonstrate real-world governance concerns that matter to banks, fintechs, lenders, leasing companies, and consulting organizations.

---

## Selected Business Domain

**Commercial Credit & Leasing Origination**

The project focuses on AI-assisted intake, underwriting support, data classification, governance review, and audit evidence for commercial credit and leasing workflows.

This domain includes:

- Commercial loans
- Commercial real estate loans
- Equipment finance
- Commercial leases
- Asset-based lending
- Small business lending where DF1071 / Section 1071 may apply
- Borrower and guarantor onboarding
- Collateral and asset review
- Financial statement intake
- Human review before credit decisions

---

## Project Name

**AI Governance Control Tower for Commercial Credit Modernization**

---

## Primary Workflow

The primary workflow is:

> AI-assisted commercial loan and lease intake, underwriting support, data classification, governance review, and audit evidence.

The control tower is designed to answer a practical governance question:

> Before a financial institution uses AI in commercial credit or leasing, what must be classified, reviewed, controlled, approved, and documented?

---

## Why This Domain Was Selected

Commercial credit and leasing origination was selected because it provides a strong intersection of:

- AI governance
- Data governance
- Commercial banking modernization
- Credit risk
- Regulatory reporting
- Sensitive borrower and guarantor data
- Document-heavy intake workflows
- Human decision controls
- Cloud data platform governance

This domain also aligns well with enterprise modernization initiatives such as governed data platforms, cloud migration, Snowflake-style data products, financial crime monitoring, and AI-assisted operational workflows.

---

## In-Scope Products and Processes

The following product and workflow areas are in scope:

| Area | Description |
|---|---|
| Commercial Term Loans | Business-purpose loans requiring borrower, guarantor, financial, collateral, and approval data |
| CRE Loans | Commercial real estate loans involving property, rent roll, appraisal, borrower, and guarantor information |
| Equipment Finance | Credit products secured by equipment or business assets |
| Commercial Leases | Lease origination and underwriting workflows similar to commercial credit intake |
| Asset-Based Lending | Lending workflows using receivables, inventory, or other business assets as collateral |
| Small Business Lending | Included where DF1071 / Section 1071 data collection or reporting may apply |
| Borrower Onboarding | Intake of business identity, ownership, financial condition, and compliance data |
| Guarantor Review | Intake and classification of guarantor information, including PII |
| Collateral Review | Review of property, equipment, assets, or pledged collateral |
| Underwriting Support | AI-assisted summarization and classification, with human decision authority retained |
| Audit Evidence | Documented evidence of reviews, approvals, risk classification, and control decisions |

---

## Explicitly Out of Scope

The project intentionally excludes consumer and residential mortgage workflows.

The following are out of scope:

- Residential mortgage origination
- Consumer mortgage lending
- NMLS licensing workflows
- SAFE Act loan originator controls
- HELOC / consumer home equity lending
- Personal credit decisioning
- Fully automated credit approvals
- AI systems making final lending decisions without human review

This boundary is important. The project is focused on commercial credit and leasing modernization, not consumer mortgage compliance.

---

## Governance Problems Addressed

The control tower is designed to address the following governance problems:

1. **AI Use-Case Intake**
   - What AI capability is being proposed?
   - Who owns the use case?
   - What business process does it support?
   - Is AI being used for summarization, classification, recommendation, or decisioning?

2. **Risk Classification**
   - Is the use case low, medium, or high risk?
   - Could the output influence a credit decision?
   - Is human review required?
   - Is there potential customer, borrower, guarantor, or regulatory impact?

3. **Data Source Classification**
   - What data sources are used?
   - Do they contain PII, financial data, collateral data, or regulatory data?
   - Who owns the data?
   - Is the data suitable for the AI use case?

4. **Regulatory and Control Mapping**
   - Does DF1071 / Section 1071 apply?
   - Are fair lending or ECOA-related concerns present?
   - Is AML / KYC / beneficial ownership screening relevant?
   - Is audit evidence required before production use?

5. **Human Review**
   - Who reviews the AI output?
   - What decisions must remain human-owned?
   - What evidence proves review occurred?

6. **Audit Evidence**
   - What was reviewed?
   - Who approved it?
   - What controls were applied?
   - What risks were accepted or mitigated?

---

## AI Usage Boundary

The project assumes AI may assist with:

- Document summarization
- Intake completeness review
- Data classification
- Risk signal identification
- Regulatory applicability prompts
- Drafting review notes
- Routing items for human review

The project does **not** assume AI is allowed to make final credit decisions.

Final underwriting, approval, denial, pricing, and exception decisions remain human-owned.

---

## Sample Use Cases

| Use Case ID | Use Case Name | Product Area | Risk Level | Notes |
|---|---|---|---|---|
| UC-001 | CRE Loan Intake Document Summarization | Commercial Real Estate Lending | High | AI summarizes borrower, property, appraisal, and financial documents for underwriter review |
| UC-002 | Equipment Lease Underwriting Package Review | Commercial Leasing | Medium/High | AI reviews lease package completeness and flags missing documents |
| UC-003 | DF1071 Small Business Lending Data Validation | Regulatory Reporting | High | AI-assisted validation of required small business lending data fields |
| UC-004 | Borrower and Guarantor Data Classification | Data Governance | High | Classification of PII, beneficial ownership, financial data, and sensitive credit data |
| UC-005 | Snowflake Credit Data Product Classification | Data Platform Governance | Medium | Governance of commercial credit data products used by analytics or AI workflows |
| UC-006 | AML / FCCM Screening Summary Support | Financial Crime Compliance | High | AI summarizes screening or alert context for compliance review, without making final decisions |

---

## Platform Layer

The project includes a Snowflake-style governed data platform layer.

This platform layer represents the governed data foundation beneath the AI workflow.

Example governed data products may include:

- Borrower profile data
- Guarantor profile data
- Commercial loan application data
- Lease application data
- Collateral and asset data
- Financial statement data
- DF1071 reporting data
- AML / KYC screening data
- AI governance decision evidence

The purpose of this layer is to demonstrate that AI governance is not separate from data governance. The AI control process depends on trusted data sources, clear ownership, classification, lineage, and evidence.

---

## Initial Data Artifacts

The Day 5 sample data artifacts will include:

| File | Purpose |
|---|---|
| `data/sample_ai_use_cases.csv` | Defines AI use cases, business owners, product areas, risk levels, and review requirements |
| `data/sample_data_sources.csv` | Defines data sources, data classifications, ownership, and sensitivity |
| `data/sample_regulatory_controls.csv` | Maps governance controls to DF1071, fair lending, AML/KYC, data privacy, and audit evidence concerns |
| `data/sample_governance_decisions.csv` | Captures review decisions, required controls, approval status, and evidence notes |
| `docs/schema_notes.md` | Explains each sample file and field definition |

---

## Decision Summary

The selected domain is:

**Commercial Credit & Leasing Origination**

The selected project is:

**AI Governance Control Tower for Commercial Credit Modernization**

The selected first workflow is:

**AI-assisted commercial loan and lease intake with governance review and audit evidence.**

Residential mortgage and consumer lending workflows are excluded to keep the sprint focused, reduce unnecessary regulatory complexity, and preserve a clear commercial banking modernization narrative.

This domain was selected because it provides the strongest combination of hiring-market relevance, AI governance depth, data governance depth, financial services alignment, and practical portfolio value.