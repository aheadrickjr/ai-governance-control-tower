# AIF Domain Map + Architecture v1

## Purpose

This document maps a simple AWS serverless intake architecture to AIF-C01 learning domains.

## Architecture v1

```text
AI Use Case Intake / Upload
        |
        v
Amazon S3
        |
        v
AWS Lambda
        |
        v
Amazon DynamoDB
        |
        v
Amazon CloudWatch

#####

## Phase 2: AIF-C01 Domain Mapping

| AIF-C01 Domain | What It Means | Architecture Connection | Notes |
|---|---|---|---|
| Fundamentals of AI and ML | Understand basic AI/ML concepts, model types, training vs inference, and data’s role in AI systems. | S3 can store source data, documents, or evidence used by downstream AI workflows. | Data quality and context matter before any AI service is introduced. |
| Fundamentals of Generative AI | Understand foundation models, prompts, embeddings, inference, and generative AI use cases. | This architecture can later add Amazon Bedrock after the intake layer. | Current v1 does not include Bedrock yet. |
| Applications of Foundation Models | Understand how FMs are selected, evaluated, integrated, and used in business workflows. | Lambda could call Bedrock or another AI service after validating an intake event. | This becomes the future AI processing layer. |
| Guidelines for Responsible AI | Understand fairness, explainability, privacy, security, transparency, and governance. | DynamoDB can store risk flags, approval status, reviewer notes, and audit metadata. | This connects directly to AI governance control tower concepts. |
| Security, Compliance, and Governance for AI Solutions | Understand access controls, monitoring, data protection, and governance mechanisms. | IAM controls access; CloudWatch monitors execution; DynamoDB stores traceability. | This is the strongest governance connection in v1. |
