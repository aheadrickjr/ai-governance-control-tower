# AI Governance Controls

## Purpose

This document defines starter governance controls for responsible AI, data security, privacy, compliance, and operational oversight.

These controls are intended to support the AI Governance Control Tower sprint by translating responsible AI concepts into practical controls, evidence requirements, ownership, and review cadence.

## Control Framework

Each control includes:

- Control ID
- Control Name
- Risk Addressed
- Control Objective
- Control Description
- Evidence Required
- Control Owner
- Review Frequency
- Related AI / AWS Concept

## Starter Controls

| Control ID | Control Name | Risk Addressed | Control Objective | Evidence Required | Owner | Frequency |
|---|---|---|---|---|---|---|
| AIGC-001 | AI Use Case Intake Review | AI tools used without business, risk, or compliance visibility | Ensure AI use cases are documented before approval or deployment | Intake form, approval record, risk classification | AI Governance Lead | Per use case |
| AIGC-002 | Data Classification for AI Inputs | Sensitive or regulated data used improperly in AI workflows | Ensure data used in AI systems is classified before use | Data classification record, source inventory | Data Owner / Steward | Per dataset |
| AIGC-003 | Privacy Review for AI Workflows | Personal or confidential data exposed to AI tools | Confirm privacy requirements before AI processing | Privacy review checklist, PII/PHI assessment | Privacy / Compliance | Per workflow |
| AIGC-004 | Human Review for High-Risk Outputs | AI output used without human validation | Require human-in-the-loop review for high-impact decisions | Review log, exception notes, approval record | Business Owner | Per decision/process |
| AIGC-005 | AI Output Validation | Inaccurate, hallucinated, or misleading AI output used operationally | Validate AI-generated outputs before business use | Test cases, validation notes, defect log | Process Owner | Ongoing |
| AIGC-006 | Access Control for AI Systems | Unauthorized users access sensitive AI tools, prompts, or outputs | Restrict AI access based on role and business need | Access list, IAM/group membership, review record | System Owner | Quarterly |
| AIGC-007 | Prompt and Output Logging | No audit trail for AI interactions | Maintain traceability for prompts, responses, and decisions | Prompt logs, output logs, audit records | Platform Owner | Ongoing |
| AIGC-008 | Bias and Fairness Review | AI decisions create unfair or discriminatory outcomes | Review high-risk AI use cases for bias and disparate impact | Fairness checklist, test results, mitigation notes | AI Governance Lead | Per high-risk use case |
| AIGC-009 | Model / Tool Approval Register | Unapproved AI tools enter business use | Maintain inventory of approved AI tools and models | Approved tool register, vendor assessment | Governance / Security | Monthly |
| AIGC-010 | Incident Escalation for AI Failures | AI errors, privacy issues, or security events are not escalated | Define escalation path for AI-related incidents | Incident ticket, escalation record, remediation plan | Risk / Security / Governance | Per incident |

## How These Controls Support Client Readiness

These controls help an organization demonstrate that AI adoption is not unmanaged experimentation.

They create evidence that the organization has considered:

- Responsible AI usage
- Data privacy
- Data security
- Human oversight
- Output validation
- Auditability
- Ownership
- Compliance readiness
- Risk escalation

## Sprint Notes

This is a starter control set for Day 9. It will be expanded later as the AI Governance Control Tower matures.