# AI Governance Control Tower Workflow

## Purpose

This diagram shows the first version of the AI Governance Control Tower workflow.

The goal is to show how an AI-enabled use case moves from business intake through review, risk assessment, control mapping, approval, monitoring, and escalation.

## High-Level Workflow

```mermaid
flowchart TD
    A[Business Unit Submits AI Use Case] --> B[AI Use Case Intake]
    B --> C[Stakeholder & Ownership Review]
    C --> D[Data & Privacy Review]
    D --> E[AWS AI Service Mapping]
    E --> F[Risk & Impact Assessment]
    F --> G[Control Checklist]
    G --> H{Approval Decision}

    H -->|Approved| I[Implementation Oversight]
    H -->|Needs Changes| J[Remediation / Clarification]
    H -->|Rejected| K[Stop / Archive Use Case]

    J --> B

    I --> L[Monitoring & Escalation Model]
    L --> M{Issue Detected?}

    M -->|No| N[Continue Monitoring]
    M -->|Yes| O[Escalate / Pause / Kill Switch]

    O --> P[Governance Review Board]
    P --> Q[Decision Log]