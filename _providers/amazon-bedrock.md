---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Bedrock Agentic Access
  operation_count: 12
  slug: amazon-bedrock-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 8
apis:
- description: The Amazon Bedrock Agent API provides operations for managing and configuring autonomous AI agents, knowledge bases for RAG, data sources, and ingestion jobs. Authentication uses AWS Signature Version
  name: Amazon Bedrock Agent API
  slug: amazon-bedrock-agent-api
- description: The Amazon Bedrock Agent Runtime API provides operations for invoking Bedrock agents and retrieving content from knowledge bases for RAG applications. Authentication uses AWS Signature Version 4 (SigV
  name: Amazon Bedrock Agent Runtime API
  slug: amazon-bedrock-agent-runtime-api
- description: Operations for multi-turn conversations with models.
  name: Amazon Bedrock Converse API
  slug: amazon-bedrock-converse-api
- description: Operations for listing custom models.
  name: Amazon Bedrock Custom Models API
  slug: amazon-bedrock-custom-models-api
- description: Operations for listing and describing foundation models.
  name: Amazon Bedrock Foundation Models API
  slug: amazon-bedrock-foundation-models-api
- description: Operations for invoking models and running inference.
  name: Amazon Bedrock Inference API
  slug: amazon-bedrock-inference-api
- description: Operations for creating and managing model customization jobs.
  name: Amazon Bedrock Model Customization API
  slug: amazon-bedrock-model-customization-api
- description: Operations for managing provisioned model throughput.
  name: Amazon Bedrock Provisioned Throughput API
  slug: amazon-bedrock-provisioned-throughput-api
artifact_total: 38
collections:
- collection_type: postman
  name: Amazon Bedrock Converse API
  slug: postman-amazon-bedrock-converse-api
- collection_type: postman
  name: Amazon Bedrock Converse Custom Models API
  slug: postman-amazon-bedrock-custom-models-api
- collection_type: postman
  name: Amazon Bedrock Converse Foundation Models API
  slug: postman-amazon-bedrock-foundation-models-api
- collection_type: postman
  name: Amazon Bedrock Converse Inference API
  slug: postman-amazon-bedrock-inference-api
- collection_type: postman
  name: Amazon Bedrock Converse Model Customization API
  slug: postman-amazon-bedrock-model-customization-api
- collection_type: postman
  name: Amazon Bedrock Converse Provisioned Throughput API
  slug: postman-amazon-bedrock-provisioned-throughput-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Bedrock Converse API
  slug: open-amazon-bedrock-converse-api
- collection_type: open
  name: Amazon Bedrock Converse Custom Models API
  slug: open-amazon-bedrock-custom-models-api
- collection_type: open
  name: Amazon Bedrock Converse Foundation Models API
  slug: open-amazon-bedrock-foundation-models-api
- collection_type: open
  name: Amazon Bedrock Converse Inference API
  slug: open-amazon-bedrock-inference-api
- collection_type: open
  name: Amazon Bedrock Converse Model Customization API
  slug: open-amazon-bedrock-model-customization-api
- collection_type: open
  name: Amazon Bedrock Converse Provisioned Throughput API
  slug: open-amazon-bedrock-provisioned-throughput-api
- collection_type: open
  name: Amazon Bedrock Runtime API
  slug: open-amazon-bedrock-runtime
- collection_type: open
  name: Amazon Bedrock API
  slug: open-amazon-bedrock
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-bedrock/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-bedrock-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-bedrock-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-bedrock-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-bedrock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/bedrock/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/bedrock/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/bedrock/pricing/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/bedrock/
- group: start
  title: ''
  type: Login
  url: https://console.aws.amazon.com/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/bedrock/faqs/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/bedrock/getting-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
created: '2026-05-11'
description: Amazon Bedrock is a fully managed AWS service that makes high-performing foundation models from leading AI companies available through a unified API for building generative AI applications. It supports text and image generation, conversational AI, model customization and fine-tuning, retrieval-augmented generation (RAG) via knowledge bases, autonomous agents, guardrails for responsible AI, and provisioned throughput for production workloads. The Bedrock APIs are AWS regional service endpoints accessed over HTTPS using AWS Signature Version 4 (SigV4) authentication, typically via the AWS SDKs.
examples:
- key_count: 2
  name: Converse Example
  slug: converse-example
- key_count: 2
  name: Create Knowledge Base Example
  slug: create-knowledge-base-example
- key_count: 2
  name: Invoke Model Example
  slug: invoke-model-example
finops:
- name: Amazon Bedrock Finops
  service_category: API
  slug: amazon-bedrock-finops
graphqls:
- description: Amazon Bedrock is a fully managed AWS service for accessing foundation models from AI21 Labs, Anthropic, Cohere, Meta, Mistral AI, and Stability AI. The API covers model invocation, streaming, agents,
  name: Amazon Bedrock GraphQL API
  slug: amazon-bedrock-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-bedrock.png
json_schemas:
- name: Amazon Bedrock Foundation Model
  property_count: 10
  slug: amazon-bedrock-model
json_structures:
- name: Bedrock Resource Structure
  property_count: 0
  slug: bedrock-resource-structure
jsonld:
- class_count: 20
  name: Amazon Bedrock Context
  property_count: 8
  slug: amazon-bedrock-context
layout: provider
modified: '2026-05-19'
name: Amazon Bedrock
nav: Providers
network: true
overview: 'Amazon Bedrock publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Converse API, Custom Models API, Foundation Models API, and 3 more. Tagged areas include AI, Foundation Models, Generative AI, LLM, and Machine Learning.


  The Amazon Bedrock catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Amazon Bedrock''s developer surface includes documentation, pricing, signup flow, developer portal, developer console, support, engineering blog, and 13 more developer resources.'
plans:
- name: Amazon Bedrock Plans Pricing
  plan_count: 1
  slug: amazon-bedrock-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 2
  name: Amazon Bedrock Rate Limits
  slug: amazon-bedrock-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Bedrock API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-bedrock-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.8
  delta: -5.9
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 9.8
    contract_quality: 67.0
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 39.5
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-bedrock/refs/heads/main/screenshots/amazon-bedrock-2026-06-20T171613.png
security:
- kind: domain-security
  name: Amazon Bedrock Domain Security
  slug: amazon-bedrock-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Bedrock Vulnerability Disclosure
  slug: amazon-bedrock-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Bedrock Trust Center
  slug: amazon-bedrock-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-bedrock
tags:
- AI
- Foundation Models
- Generative AI
- LLM
- Machine Learning
- RAG
- Agents
- Responsible AI
website: https://aws.amazon.com/bedrock/
---
