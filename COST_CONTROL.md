# COST_CONTROL.md

## AI Governance Control Tower — AWS Cost Control Gate

### Purpose

This document defines the AWS cost-control guardrails for the AI Governance Control Tower sprint.

The goal is to prevent accidental cloud spend while still allowing controlled experimentation with AWS services such as S3, IAM, Bedrock, and supporting governance artifacts.

This file acts as the Day 15 Cost Gate.

---

## Cost Gate Status

**Status:** Approved for controlled AWS experimentation  
**Scope:** Low-cost / free-tier-aware services only  
**Default rule:** If cost impact is unclear, stop and verify before creating the resource.

---

## Operating Rules

### 1. No Root User for Build Work

The AWS root user must not be used for day-to-day build activity.

Root user use is limited to:

- Account-level billing setup
- MFA/security recovery
- Tasks that explicitly require root access

All normal build work must use a dedicated IAM user.

---

## IAM Naming Standard

### IAM Group

Use:

```text
gad-admins