# AI Governance Control Tower

## Purpose

AI Governance Control Tower is a practical portfolio and consulting project that demonstrates how AI governance can be turned into executable artifacts, review workflows, risk controls, and AWS AI service mappings.

This project is being built as part of a certification-to-portfolio sprint that combines:

- AWS AI Practitioner / AIF-C01 preparation
- AIGP / AI Governance Professional preparation
- AI data governance consulting positioning
- GitHub-ready proof of execution
- Globe & Anchor Digital Media Solutions service development

The goal is not to create a theoretical AI ethics document. The goal is to create a working project package that shows how an organization could intake, evaluate, govern, approve, monitor, and escalate AI-enabled use cases.

---

## Project Story

Organizations are adopting AI faster than their governance, risk, data, compliance, and operations teams can manage it.

Common failure patterns include:

- AI use cases launched without business ownership
- No stakeholder review
- Unclear model or system purpose
- Weak data lineage and data quality visibility
- No AI impact assessment
- No documented approval path
- No assigned operational owner
- No monitoring or escalation process
- No kill-switch or pause criteria
- Overreliance on AI output without human accountability

This project addresses that gap by creating a structured AI governance foundation.

---

## Target Audience

This project is designed for:

- Hiring managers evaluating AI governance and data architecture capability
- Consulting clients considering AI adoption
- Financial services and healthcare organizations
- SMBs introducing AI tools
- Internal Globe & Anchor Digital Media Solutions service development
- Recruiters looking for evidence beyond certification badges

---

## First Use Case

### AI Use Case Governance Intake and Review

A business unit wants to introduce an AI-enabled solution into the organization.

Before approval, the organization must document:

- Business purpose
- System scope
- Stakeholders
- Data involved
- AWS AI/cloud services involved
- Risk level
- Human oversight
- Approval requirements
- Monitoring expectations
- Escalation and shutdown process

This first use case is broad enough to demonstrate AI governance maturity but narrow enough to build quickly.

---

## Repository Structure

```text
ai-governance-control-tower/
├── README.md
├── PROJECT_STORY.md
├── DEFINITION_OF_DONE.md
├── SPRINT_CHARTER.md
├── docs/
│   ├── ai-use-case-intake.md
│   ├── stakeholder-raci.md
│   ├── risk-impact-assessment.md
│   ├── control-checklist.md
│   ├── monitoring-escalation-model.md
│   └── aws-ai-service-map.md
├── templates/
│   ├── intake-form-template.md
│   ├── impact-assessment-template.md
│   ├── control-register-template.csv
│   └── decision-log-template.md
├── examples/
│   └── sample-ai-use-case-review.md
├── src/
│   └── placeholder.md
└── notes/
    ├── aif-c01-study-notes.md
    └── aigp-study-notes.md

---
#######################################################
###               Week 1 Sprint Status              ###
#######################################################

Week 1 of the AI Governance Control Tower sprint established the foundation for the project, including the project story, AWS resource mapping, cost controls, AI service architecture framing, repository structure, sample governance data, and AIF-C01 weak-area tracking.

| Day | Focus | Framework Step | Daily Task | Daily Deliverable |
|---:|---|---|---|---|
| 1 | Goal | Goal | Write sprint charter and AIF-C01 completion contract | `PROJECT_STORY.md` + Definition of Done |
| 2 | Research | Research | Build resource map; enable AWS Budgets / Cost Explorer / Billing alerts | `RESOURCE_MAP.md` + `COST_CONTROL.md` |
| 3 | Priming | Priming | Skim AIF-C01 domains; draw S3-Lambda-DynamoDB-CloudWatch architecture | AIF domain map + architecture v1 |
| 4 | Priming | Priming | Create GitHub repo structure and project README skeleton | Public repo initialized |
| 5 | Priming | Priming | Choose business domain and define sample files | Sample data files + schema notes |
| 6 | Priming/Gate | Gate | Take AIF-C01 baseline quiz and document weak areas | Baseline score + weak-area list |
| 7 | Package | Implementation | Publish Week 1 notes and LinkedIn build post draft | `README.md` v1 + LinkedIn Post 1 |
##
######################################################
###          Week 1 Completion Summary             ###
######################################################
##
By the end of Week 1, this project had moved from concept to a visible portfolio foundation.

Completed work includes:

- Project purpose and story defined
- Sprint charter and completion expectations documented
- AWS resource and cost-control artifacts created
- Initial AWS AI/cloud architecture mapped
- Public GitHub repository initialized
- Business domain selected
- Sample data files and schema notes created
- AIF-C01 baseline quiz completed
- Weak areas documented for targeted review
- Root `README.md` updated as the project landing page
- LinkedIn build-in-public post drafted

### Current Project Position

The AI Governance Control Tower is now positioned as a practical governance architecture project, not just a certification study exercise.

The project demonstrates how AI governance can be translated into visible artifacts, operating controls, review workflows, AWS service mapping, and portfolio-ready documentation.

Next sprint focus:

- Refine AI use case intake workflow
- Expand risk and control artifacts
- Continue AIF-C01 study against documented weak areas
- Add hands-on AWS/DataHub/Glue-aligned governance evidence where practical
- Prepare additional LinkedIn build updates tied to actual repository progress
---

## Governance Framework Direction

This project will progressively align to practical governance themes drawn from:

- AI risk management
- Responsible AI review
- Data governance and lineage
- Human oversight
- Model/service monitoring
- Cloud AI service governance
- Auditability and operational accountability

The first version focuses on building usable governance artifacts before expanding into automation, dashboards, and control monitoring.

---

## Sprint Build Philosophy

This project follows a certification-to-portfolio sprint model.

Each sprint day should produce at least one visible artifact, improvement, commit, or documented learning that can support:

- GitHub portfolio credibility
- LinkedIn content
- Interview talking points
- Consulting service development
- AI governance architecture maturity
--
#############################################
###     Day 8 Validator Checkpoint        ###
#############################################

Day 8 established the first working validator foundation for the AI Governance Control Tower sprint.

### Files Added

```text
data/sample_controls.csv
data/sample_neg_controls.csv
src/validator.py
src/row_validator.py
##
#############################################
###       Regulatory Domain Anchor        ###
#############################################
##

The first regulatory domain anchor for this project is small business lending governance, using CFPB Section 1071 / DF1071-related documentation as source material.

This gives the AI Governance Control Tower a real-world governance context involving:

- Small business lending data collection
- Regulatory reporting considerations
- Data quality and completeness expectations
- Applicant / business demographic data handling
- Governance review and control requirements
- Documentation and auditability expectations

The purpose is not to reproduce regulatory guidance, but to use the Section 1071 / DF1071 domain as a practical scenario for demonstrating AI governance, data governance, intake review, risk assessment, control mapping, and monitoring.

Supporting source documents and summaries are stored under `docs/`.

Current supporting artifacts include:

| Artifact | Purpose |
|---|---|
| `docs/cfbp_smb_lending_github.md` | Project-facing summary / notes for small business lending governance |
| `docs/cfpb_sbl_executive-summary.pdf` | CFPB small business lending executive summary reference |
| `docs/cfpb_sbl_sample-data-collection-form.pdf` | CFPB sample data collection form reference |
| `docs/regsDF1071.pdf` | DF1071 / Section 1071 regulatory reference material |