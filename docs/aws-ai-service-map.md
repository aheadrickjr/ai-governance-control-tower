# AWS AI Service Map

## Purpose

This document maps common AWS AI and cloud services to AI governance review questions.

The purpose is not to recommend a service automatically. The purpose is to help a reviewer understand which AWS services may support a use case, what each service is generally used for, and what governance considerations should be reviewed before approval.

AWS describes its machine learning service portfolio as including pre-trained services for common AI-powered use cases, while services such as Amazon Bedrock and Amazon SageMaker support more customized generative AI and machine learning scenarios. :contentReference[oaicite:0]{index=0}

---

## Service Mapping Objective

The AWS AI service map helps answer:

1. Which AWS AI or cloud services may apply to the use case?
2. What business capability does the service support?
3. What data does the service require?
4. What outputs does the service produce?
5. What governance risks are introduced?
6. What controls are required before deployment?
7. What monitoring is required after launch?

---

## How to Use This Map

Use this document after initial AI use-case intake and before final approval.

Recommended flow:

```text
AI Use Case Intake
     |
     v
Risk and Impact Assessment
     |
     v
AWS AI Service Mapping
     |
     v
Control Checklist
     |
     v
Approval Decision
     |
     v
Monitoring and Escalation