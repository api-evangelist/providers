---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 45.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Amazon Augmented Ai Agentic Access
  operation_count: 5
  slug: amazon-augmented-ai-agentic-access
  summary_line: 5 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Operations for creating and managing human review loops
  name: Amazon Augmented AI Human Loops API
  slug: amazon-augmented-ai-human-loops-api
artifact_total: 70
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-augmented-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-augmented-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-augmented-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-augmented-ai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-augmented-ai-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-augmented-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-augmented-ai-well-known.yml
created: '2026-03-16'
description: Amazon Augmented AI (Amazon A2I) is a machine learning service that makes it easy to build the workflows required for human review of ML predictions. Amazon A2I brings human review to all developers, removing the undifferentiated heavy lifting associated with building human review systems or managing large numbers of human reviewers.
examples:
- key_count: 3
  name: A2I Data Attributes Example
  slug: a2i-data-attributes-example
- key_count: 3
  name: A2I Delete Human Loop Response Example
  slug: a2i-delete-human-loop-response-example
- key_count: 3
  name: A2I Describe Human Loop Response Example
  slug: a2i-describe-human-loop-response-example
- key_count: 3
  name: A2I Human Loop Activation Results Example
  slug: a2i-human-loop-activation-results-example
- key_count: 3
  name: A2I Human Loop Input Example
  slug: a2i-human-loop-input-example
- key_count: 3
  name: A2I Human Loop Output Example
  slug: a2i-human-loop-output-example
- key_count: 3
  name: A2I Human Loop Summary Example
  slug: a2i-human-loop-summary-example
- key_count: 3
  name: A2I List Human Loops Response Example
  slug: a2i-list-human-loops-response-example
- key_count: 3
  name: A2I Start Human Loop Request Example
  slug: a2i-start-human-loop-request-example
- key_count: 3
  name: A2I Start Human Loop Response Example
  slug: a2i-start-human-loop-response-example
- key_count: 3
  name: A2I Stop Human Loop Request Example
  slug: a2i-stop-human-loop-request-example
- key_count: 3
  name: A2I Stop Human Loop Response Example
  slug: a2i-stop-human-loop-response-example
features:
- Human review integration for Amazon Rekognition and Amazon Textract
- Custom flow definitions for any ML use case
- Built-in worker task templates for common review tasks
- Integration with Amazon SageMaker Ground Truth for workforce management
- Private, vendor, and Amazon Mechanical Turk workforce support
- Automatic routing based on ML confidence scores
- Audit trail with evidence of human review decisions
- Scalable workforce management across thousands of reviewers
- Pre-built UI templates for image and text review tasks
- Compliance support with PII content classifiers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-augmented-ai.png
integrations:
- Amazon SageMaker
- Amazon Rekognition
- Amazon Textract
- Amazon S3
- Amazon SageMaker Ground Truth
- Amazon Mechanical Turk
- AWS IAM
- Amazon CloudWatch
- AWS Lambda
- Amazon SNS
json_schemas:
- name: DataAttributes
  property_count: 0
  slug: a2i-data-attributes
- name: DeleteHumanLoopResponse
  property_count: 0
  slug: a2i-delete-human-loop-response
- name: DescribeHumanLoopResponse
  property_count: 0
  slug: a2i-describe-human-loop-response
- name: HumanLoopActivationResults
  property_count: 0
  slug: a2i-human-loop-activation-results
- name: HumanLoopInput
  property_count: 0
  slug: a2i-human-loop-input
- name: HumanLoopOutput
  property_count: 0
  slug: a2i-human-loop-output
- name: HumanLoopSummary
  property_count: 0
  slug: a2i-human-loop-summary
- name: ListHumanLoopsResponse
  property_count: 0
  slug: a2i-list-human-loops-response
- name: StartHumanLoopRequest
  property_count: 0
  slug: a2i-start-human-loop-request
- name: StartHumanLoopResponse
  property_count: 0
  slug: a2i-start-human-loop-response
- name: StopHumanLoopRequest
  property_count: 0
  slug: a2i-stop-human-loop-request
- name: StopHumanLoopResponse
  property_count: 0
  slug: a2i-stop-human-loop-response
json_structures:
- name: A2I Data Attributes Structure
  property_count: 0
  slug: a2i-data-attributes-structure
- name: A2I Delete Human Loop Response Structure
  property_count: 0
  slug: a2i-delete-human-loop-response-structure
- name: A2I Describe Human Loop Response Structure
  property_count: 0
  slug: a2i-describe-human-loop-response-structure
- name: A2I Human Loop Activation Results Structure
  property_count: 0
  slug: a2i-human-loop-activation-results-structure
- name: A2I Human Loop Input Structure
  property_count: 0
  slug: a2i-human-loop-input-structure
- name: A2I Human Loop Output Structure
  property_count: 0
  slug: a2i-human-loop-output-structure
- name: A2I Human Loop Summary Structure
  property_count: 0
  slug: a2i-human-loop-summary-structure
- name: A2I List Human Loops Response Structure
  property_count: 0
  slug: a2i-list-human-loops-response-structure
- name: A2I Start Human Loop Request Structure
  property_count: 0
  slug: a2i-start-human-loop-request-structure
- name: A2I Start Human Loop Response Structure
  property_count: 0
  slug: a2i-start-human-loop-response-structure
- name: A2I Stop Human Loop Request Structure
  property_count: 0
  slug: a2i-stop-human-loop-request-structure
- name: A2I Stop Human Loop Response Structure
  property_count: 0
  slug: a2i-stop-human-loop-response-structure
jsonld:
- class_count: 4
  name: Amazon Augmented Ai Context
  property_count: 0
  slug: amazon-augmented-ai-context
layout: provider
modified: '2026-06-20'
name: Amazon Augmented AI
nav: Providers
network: true
overview: 'Amazon Augmented AI publishes 1 API on the [APIs.io](https://apis.io/) network: Human Loops API. Tagged areas include Amazon Augmented AI, Human In The Loop, Machine Learning, and AI Review.


  The Amazon Augmented AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Augmented AI''s developer surface includes authentication and 6 more developer resources.'
random_paper: 56
rules:
- name: Amazon Augmented AI API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-augmented-ai-jsonschema-spectral-rules
- name: Amazon Augmented AI API Rules
  rule_count: 18
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 11
  slug: amazon-augmented-ai-spectral-rules
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 73.5
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 37.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-augmented-ai/refs/heads/main/screenshots/amazon-augmented-ai-2026-07-25T195931.png
security:
- kind: authentication
  name: Amazon Augmented Ai Authentication
  slug: amazon-augmented-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Augmented Ai Domain Security
  slug: amazon-augmented-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Augmented Ai Vulnerability Disclosure
  slug: amazon-augmented-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-augmented-ai
tags:
- Amazon Augmented AI
- Human In The Loop
- Machine Learning
- AI Review
use_cases:
- Review low-confidence document text extraction results
- Validate image classification predictions before deployment
- Moderate user-generated content with human reviewers
- Ensure accuracy of medical record processing
- Verify identity document data extraction results
- Build training datasets with human-verified labels
---
