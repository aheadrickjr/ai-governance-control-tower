# Risk and Impact Assessment

## Purpose

This document defines the risk and impact assessment process for AI use cases in the AI Governance Control Tower project.

The assessment process evaluates whether an AI-enabled use case can proceed safely, what risks must be controlled, what approvals are required, and what monitoring must exist after launch.

The goal is not to eliminate all risk. The goal is to make risk visible, assign ownership, document controls, and confirm whether the remaining risk is acceptable.

---

## Assessment Objective

The risk and impact assessment answers the following questions:

1. What could go wrong?
2. Who or what could be impacted?
3. What data, systems, users, and decisions are involved?
4. What controls are required?
5. Who must review and approve the use case?
6. Who accepts residual risk?
7. What must be monitored after launch?
8. When should the AI system be paused, escalated, or shut down?

---

## When Assessment Is Required

A risk and impact assessment is required when an AI use case:

- Moves beyond idea stage
- Uses confidential, regulated, or sensitive data
- Affects customers, employees, borrowers, patients, applicants, vendors, or public users
- Supports or influences decisions
- Produces customer-facing or operational outputs
- Uses generative AI, prediction, classification, recommendation, document extraction, or automated summarization
- Connects to business-critical systems
- Introduces legal, regulatory, security, privacy, fairness, or reputational risk
- Moves from prototype to pilot or production
- Is already in use but was never formally reviewed

---

## Assessment Inputs

The assessment should use information from:

- AI use-case intake
- Business owner interview
- Technology owner input
- Data owner input
- Security review
- Privacy review
- Compliance/legal review
- AWS AI service mapping
- Architecture notes
- Data lineage documentation
- Existing risk/control registers
- User impact analysis

---

## Assessment Flow

```text
Completed Intake
     |
     v
Risk and Impact Assessment
     |
     v
Data Impact Review
     |
     v
Model/System Impact Review
     |
     v
Stakeholder Impact Review
     |
     v
Security, Privacy, Legal, and Compliance Review
     |
     v
Control Assessment
     |
     v
Residual Risk Rating
     |
     v
Approval Recommendation
     |
     v
Monitoring and Reassessment Plan