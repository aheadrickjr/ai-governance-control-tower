@'
# Resource Map

## Purpose

This document maps the core resources, services, repositories, documents, and environments used for the 28-Day AI Governance Control Tower sprint.

The goal is to keep the project organized, auditable, and easy to continue without losing context.

---

## Sprint Project

| Item | Value |
|---|---|
| Project Name | AI Governance Control Tower |
| Sprint Folder | 28Day_AIGovernance |
| GitHub Repository | ai-governance-control-tower |
| Primary Company Context | Globe & Anchor Digital Media Solutions |
| Primary Learning Track | AWS AI Practitioner / AIF-C01 |
| Supporting Governance Track | AI Governance / AIGP concepts |
| Sprint Goal | Build a practical AI governance portfolio project with working artifacts and AWS-aware controls |

---

## Repository Structure

| Path | Purpose |
|---|---|
| README.md | Public project overview |
| PROJECT_STORY.md | Narrative and purpose of the project |
| SPRINT_CHARTER.md | Sprint goals, boundaries, and execution rules |
| DEFINITION_OF_DONE.md | Completion criteria |
| docs/ | Governance and cloud documentation |
| templates/ | Reusable intake, assessment, and governance templates |
| examples/ | Sample completed governance reviews |
| notes/ | Study and sprint notes |
| src/ | Future automation or application code |

---

## Current Day 2 Artifacts

| Artifact | Purpose | Status |
|---|---|---|
| docs/ai-use-case-intake.md | Documents the AI use case intake process | Complete |
| docs/risk-impact-assessment.md | Defines risk and impact review approach | Complete |
| docs/aws-ai-service-map.md | Maps AWS AI services to governance concerns | Complete |
| templates/intake-form-template.md | Reusable intake template | Complete |
| templates/impact-assessment-template.md | Reusable impact assessment template | Complete |
| docs/RESOURCE_MAP.md | Maps project resources and sprint assets | Complete |
| docs/COST_CONTROL.md | Defines AWS cost controls and budget monitoring | Complete |

---

## AWS Resource Categories

| Category | AWS Service / Tool | Governance Relevance |
|---|---|---|
| Account Cost Visibility | AWS Billing and Cost Management | Tracks account spend and billing exposure |
| Budget Control | AWS Budgets | Sets budget thresholds and alerts |
| Cost Analysis | AWS Cost Explorer | Reviews actual and forecasted spend |
| Billing Alerts | AWS Budgets / Billing Preferences | Enables billing-related monitoring and alerting |
| AI Services | Amazon Bedrock, SageMaker, Comprehend, Textract, Transcribe, Rekognition, Q Business | AI use case and service mapping |
| Security and Access | IAM | Access control and least privilege |
| Logging and Monitoring | CloudWatch, CloudTrail | Auditability and operational evidence |
| Storage | S3 | Data storage, classification, retention, and access control |
| Serverless Compute | Lambda | Lightweight workflow automation |
| Governance Metadata | AWS Glue Data Catalog | Data cataloging and metadata management |

---

## External Learning and Reference Sources

| Resource | Purpose |
|---|---|
| ExamPro AIF-C01 Course | AWS AI Practitioner study path |
| AWS Documentation | Primary source for AWS service behavior |
| AWS Skill Builder / Exam Guide | Certification scope validation |
| LinkedIn Learning Practice Exams | Practice exam reinforcement |
| Project GitHub Repository | Portfolio proof of execution |
| NotebookLM | Optional resource repository and study assistant |

---

## Governance Resource Principle

Every project artifact should support one of four outcomes:

1. Clarify the AI use case.
2. Identify data, risk, ownership, and controls.
3. Map the use case to AWS services and operating requirements.
4. Produce evidence that the use case was reviewed, approved, monitored, or escalated.
'@ | Set-Content -Path .\docs\RESOURCE_MAP.md -Encoding UTF8