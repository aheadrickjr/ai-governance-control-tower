@'
# AWS Cost Control

## Purpose

This document defines the AWS cost control setup for the AI Governance Control Tower sprint.

The goal is to prevent unexpected AWS spend while building portfolio artifacts, testing AWS services, and studying for AWS AI Practitioner / AIF-C01.

---

## Current Cost Control Status

| Control | Status | Notes |
|---|---|---|
| AWS Budget | Complete | Monthly budget created |
| Cost Explorer | Complete | Enabled and available for daily cost review |
| Billing / Budget Alerts | Complete | Budget alerts configured |
| Daily Cost Check | Active Rule | Check AWS cost during build activity |

---

## Budget Configuration

| Setting | Value |
|---|---|
| Budget Type | Cost budget |
| Budget Period | Monthly |
| Budget Amount | $50 |
| Scope | All AWS services |
| Alerting | Budget alerts configured |
| Review Cadence | Daily during AWS build activity |

---

## Budget Rationale

The monthly AWS budget is initially set at $50 because the current month includes residual cost from two servers that were active earlier in the month.

This budget should be reviewed next month and adjusted downward if the AI Governance Control Tower build does not require persistent infrastructure.

---

## Cost Explorer Usage

Cost Explorer has been enabled and will be used to review:

| Review Area | Purpose |
|---|---|
| Month-to-date cost | Confirm current AWS spend |
| Forecasted monthly cost | Identify projected overspend |
| Cost by service | Show which AWS services are generating charges |
| Daily cost trend | Detect sudden usage spikes |
| Free tier usage | Identify where charges may begin |

---

## Sprint Spending Rules

During the 28-Day AI Governance Control Tower sprint:

- Do not leave experimental services running unnecessarily.
- Prefer documentation, templates, and static artifacts before paid infrastructure.
- Use AWS Free Tier where possible.
- Avoid high-cost AI, analytics, or compute workloads unless explicitly planned.
- Review Cost Explorer daily during AWS build activity.
- Stop and document any unexpected charge before continuing.

---

## Day 2 Completion Evidence

| Evidence | Status |
|---|---|
| AWS Budget created | Complete |
| Budget alerts configured | Complete |
| Cost Explorer enabled | Complete |
| Daily cost check rule established | Complete |
| COST_CONTROL.md created | Complete |

---

## Cost Governance Principle

Cloud cost control is part of AI governance.

An AI use case is not production-ready if the organization cannot identify who owns the cost, what services generate spend, what thresholds trigger review, and who responds when usage exceeds expectations.
'@ | Set-Content -Path .\docs\COST_CONTROL.md -Encoding UTF8