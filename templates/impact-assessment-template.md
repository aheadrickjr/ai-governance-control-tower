# AI Risk and Impact Assessment Template

## Purpose

This template is used to evaluate the risk, impact, control requirements, and approval path for an AI-enabled use case after initial intake.

The goal is to determine whether the use case can proceed safely, what controls are required, who must approve it, and what monitoring must exist after deployment.

---

## 1. Assessment Summary

### Use Case Name

[Enter use case name]

### Assessment Date

[YYYY-MM-DD]

### Assessment Owner

[Enter person, role, or team responsible for assessment]

### Business Owner

[Enter accountable business owner]

### Technology Owner

[Enter technology owner]

### Current Stage

- [ ] Idea
- [ ] Prototype
- [ ] Pilot
- [ ] Pre-production
- [ ] Production
- [ ] Existing system under review

---

## 2. Use Case Classification

### AI Capability Type

Select all that apply:

- [ ] Generative AI
- [ ] Predictive model
- [ ] Classification
- [ ] Recommendation
- [ ] Document extraction
- [ ] Search / retrieval
- [ ] Conversational assistant
- [ ] Image / video analysis
- [ ] Speech / audio processing
- [ ] Workflow automation
- [ ] Decision support
- [ ] Other: [Describe]

### Business Criticality

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Mission-critical

### User Population

Select all that apply:

- [ ] Internal employees only
- [ ] Contractors / third parties
- [ ] Customers
- [ ] Prospects
- [ ] Vendors
- [ ] Regulators / auditors
- [ ] Public users

### Decision Impact

- [ ] Informational only
- [ ] Assists human decision-making
- [ ] Recommends action
- [ ] Triggers workflow
- [ ] Makes or materially influences decisions
- [ ] Unknown / requires clarification

---

## 3. Data Impact Assessment

### Data Sources

[List data sources used by the AI system]

### Data Classification

Select all that apply:

- [ ] Public
- [ ] Internal
- [ ] Confidential
- [ ] Restricted
- [ ] Regulated
- [ ] Personal data
- [ ] Sensitive personal data
- [ ] Financial data
- [ ] Health data
- [ ] Customer data
- [ ] Employee data
- [ ] Proprietary business data

### Data Lineage Status

- [ ] Fully documented
- [ ] Partially documented
- [ ] Not documented
- [ ] Unknown

### Data Quality Status

- [ ] Known and acceptable
- [ ] Known issues exist
- [ ] Not assessed
- [ ] Unknown

### Data Risks

Select all that apply:

- [ ] Incomplete data
- [ ] Inaccurate data
- [ ] Stale data
- [ ] Biased or unrepresentative data
- [ ] Unclear data ownership
- [ ] Unknown lineage
- [ ] Sensitive data exposure
- [ ] Inappropriate secondary use
- [ ] Data retention concern
- [ ] Data residency concern
- [ ] Third-party data concern

### Data Risk Notes

[Describe data-related risks, assumptions, and required follow-up]

---

## 4. Model / System Impact Assessment

### AI System Purpose

[Describe what the AI system is intended to do]

### Expected Outputs

[Describe generated outputs, recommendations, classifications, predictions, summaries, or actions]

### Output Use

- [ ] Reference only
- [ ] Drafting support
- [ ] Summarization support
- [ ] Recommendation support
- [ ] Operational workflow support
- [ ] Customer-facing response
- [ ] Regulatory or compliance support
- [ ] Decision support
- [ ] Other: [Describe]

### Known Limitations

[Describe known limitations, uncertainty, false positive/false negative concerns, hallucination risk, or explainability gaps]

### Model / System Risks

Select all that apply:

- [ ] Inaccurate output
- [ ] Hallucination
- [ ] Bias or unfair treatment
- [ ] Poor explainability
- [ ] Overconfidence in output
- [ ] Lack of reproducibility
- [ ] Prompt injection
- [ ] Data leakage through prompts
- [ ] Inappropriate recommendations
- [ ] Model drift
- [ ] Performance degradation
- [ ] Vendor dependency
- [ ] Insufficient testing

### Model / System Risk Notes

[Describe model/system-related risks and concerns]

---

## 5. Stakeholder Impact Assessment

### Affected Stakeholders

Select all that apply:

- [ ] Employees
- [ ] Customers
- [ ] Applicants
- [ ] Patients
- [ ] Borrowers
- [ ] Vendors
- [ ] Business partners
- [ ] Regulators
- [ ] Auditors
- [ ] Public users
- [ ] Other: [Describe]

### Potential Stakeholder Harm

Select all that apply:

- [ ] Incorrect information
- [ ] Delayed service
- [ ] Unfair treatment
- [ ] Privacy exposure
- [ ] Financial harm
- [ ] Health or safety concern
- [ ] Denial or reduction of service
- [ ] Reputational harm
- [ ] Regulatory issue
- [ ] Loss of trust
- [ ] Other: [Describe]

### Stakeholder Impact Level

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical
- [ ] Unknown

### Stakeholder Impact Notes

[Describe stakeholder impact and required safeguards]

---

## 6. Legal, Regulatory, and Compliance Impact

### Relevant Compliance Areas

Select all that apply:

- [ ] Privacy
- [ ] Security
- [ ] Consumer protection
- [ ] Fair lending / fair treatment
- [ ] Employment
- [ ] Healthcare
- [ ] Financial services
- [ ] Records retention
- [ ] Auditability
- [ ] Contractual obligations
- [ ] Intellectual property
- [ ] Cross-border data transfer
- [ ] Other: [Describe]

### Required Legal / Compliance Review

- [ ] Yes
- [ ] No
- [ ] Unknown

### Regulatory Risk Level

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical
- [ ] Unknown

### Compliance Notes

[Describe compliance concerns, required reviews, or open questions]

---

## 7. Security and Privacy Impact

### Access Control Requirements

[Describe who can access the system, data, prompts, outputs, logs, and admin functions]

### Privacy Considerations

[Describe personal data, sensitive data, consent, notice, minimization, retention, or data subject concerns]

### Security Risks

Select all that apply:

- [ ] Unauthorized access
- [ ] Excessive permissions
- [ ] Data leakage
- [ ] Prompt injection
- [ ] Insecure storage
- [ ] Insecure API access
- [ ] Weak logging
- [ ] Third-party exposure
- [ ] Credential exposure
- [ ] Misconfigured cloud service
- [ ] Lack of encryption
- [ ] Lack of monitoring

### Security / Privacy Risk Level

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical
- [ ] Unknown

### Security / Privacy Notes

[Describe required controls and follow-up actions]

---

## 8. Human Oversight Assessment

### Human Oversight Model

- [ ] Human reviews every output before use
- [ ] Human reviews exceptions only
- [ ] Human can override output
- [ ] Human approves before external communication
- [ ] Human monitors after the fact
- [ ] No human review currently planned
- [ ] Unknown

### Human Accountability Owner

[Enter role or team accountable for use of AI output]

### Override Process

[Describe how a human can override, correct, reject, or escalate AI output]

### Oversight Risk

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical
- [ ] Unknown

### Human Oversight Notes

[Describe gaps, concerns, or required oversight controls]

---

## 9. AWS AI / Cloud Service Impact

### Candidate AWS Services

Select all that apply:

- [ ] Amazon Bedrock
- [ ] Amazon Q
- [ ] Amazon SageMaker
- [ ] Amazon Comprehend
- [ ] Amazon Textract
- [ ] Amazon Transcribe
- [ ] Amazon Polly
- [ ] Amazon Rekognition
- [ ] Amazon Lex
- [ ] Amazon Kendra
- [ ] AWS Lambda
- [ ] Amazon S3
- [ ] Amazon CloudWatch
- [ ] AWS CloudTrail
- [ ] AWS IAM
- [ ] AWS KMS
- [ ] Other: [Describe]

### AWS Service Fit

[Describe why these AWS services are appropriate or not appropriate]

### AWS Governance Considerations

Select all that apply:

- [ ] IAM roles and least privilege
- [ ] Encryption
- [ ] Logging
- [ ] Monitoring
- [ ] Cost controls
- [ ] Data residency
- [ ] Data retention
- [ ] Model access restrictions
- [ ] Approved model/provider selection
- [ ] Guardrails
- [ ] Audit trail
- [ ] Incident response
- [ ] Other: [Describe]

### AWS Service Risk Notes

[Describe AWS-specific concerns and required safeguards]

---

## 10. Control Assessment

### Required Controls

Select all that apply:

- [ ] Business owner approval
- [ ] Data owner approval
- [ ] Technology owner approval
- [ ] Legal review
- [ ] Compliance review
- [ ] Security review
- [ ] Privacy review
- [ ] Human-in-the-loop review
- [ ] Output validation
- [ ] Testing and acceptance criteria
- [ ] Bias/fairness review
- [ ] Data quality review
- [ ] Access control
- [ ] Logging and audit trail
- [ ] Monitoring dashboard
- [ ] Incident response process
- [ ] Escalation path
- [ ] Kill-switch / pause process
- [ ] Periodic reassessment

### Control Gaps

[List missing or weak controls]

### Required Remediation

[List actions required before approval or launch]

---

## 11. Risk Rating

### Overall Risk Rating

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical

### Risk Rating Rationale

[Explain why this risk rating was selected]

### Residual Risk After Controls

- [ ] Low
- [ ] Medium
- [ ] High
- [ ] Critical
- [ ] Unknown

### Residual Risk Owner

[Enter person, role, or committee accepting residual risk]

---

## 12. Approval Recommendation

### Assessment Recommendation

- [ ] Approve to proceed
- [ ] Approve with conditions
- [ ] Require remediation before proceeding
- [ ] Require additional review
- [ ] Reject
- [ ] Defer

### Conditions for Approval

[List required conditions]

### Required Reviewers

- [ ] Business owner
- [ ] Technology owner
- [ ] Data owner
- [ ] Security
- [ ] Privacy
- [ ] Legal
- [ ] Compliance
- [ ] Risk
- [ ] Audit
- [ ] AI governance committee
- [ ] Other: [Describe]

### Final Decision Owner

[Enter role or committee]

---

## 13. Monitoring and Reassessment

### Monitoring Requirements

Select all that apply:

- [ ] Output accuracy review
- [ ] User feedback review
- [ ] Incident tracking
- [ ] Bias/fairness monitoring
- [ ] Security monitoring
- [ ] Privacy monitoring
- [ ] Cost monitoring
- [ ] Usage monitoring
- [ ] Model/system performance monitoring
- [ ] Periodic control review
- [ ] Other: [Describe]

### Reassessment Frequency

- [ ] Monthly
- [ ] Quarterly
- [ ] Semi-annually
- [ ] Annually
- [ ] Upon material change
- [ ] Upon incident
- [ ] Other: [Describe]

### Escalation Triggers

Select all that apply:

- [ ] Harmful or incorrect output
- [ ] Regulatory concern
- [ ] Security event
- [ ] Privacy event
- [ ] Customer complaint
- [ ] Bias/fairness concern
- [ ] Unexpected system behavior
- [ ] Significant cost increase
- [ ] Vendor/model change
- [ ] Data source change
- [ ] Business process change
- [ ] Other: [Describe]

### Pause / Kill-Switch Criteria

[Describe when the system should be paused, disabled, rolled back, or escalated]

---

## 14. Assessment Decision Log

| Date | Decision | Owner | Notes |
|---|---|---|---|
| YYYY-MM-DD | [Decision] | [Owner] | [Notes] |

---

## 15. Open Issues

| Issue | Owner | Due Date | Status |
|---|---|---|---|
| [Issue] | [Owner] | [YYYY-MM-DD] | [Open/In Progress/Closed] |