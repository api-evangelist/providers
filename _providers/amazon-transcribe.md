---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Transcribe Agentic Access
  operation_count: 5
  slug: amazon-transcribe-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 2
apis:
- description: The Transcription Jobs API from Amazon Transcribe — 4 operation(s) for transcription jobs.
  name: Amazon Transcribe Transcription Jobs API
  slug: amazon-transcribe-transcription-jobs-api
- description: The Vocabularies API from Amazon Transcribe — 1 operation(s) for vocabularies.
  name: Amazon Transcribe Vocabularies API
  slug: amazon-transcribe-vocabularies-api
artifact_total: 26
collections:
- collection_type: postman
  name: Amazon Transcribe Transcription Jobs API
  slug: postman-amazon-transcribe-transcription-jobs-api
- collection_type: postman
  name: Amazon Transcribe Transcription Jobs Vocabularies API
  slug: postman-amazon-transcribe-vocabularies-api
- collection_type: open
  name: Amazon Transcribe API
  slug: open-amazon-transcribe
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-transcribe/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-transcribe-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-transcribe-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-transcribe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-transcribe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-transcribe-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/transcribe/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/transcribe/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/transcribe/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-transcribe
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transcribe/refs/heads/main/rules/amazon-transcribe-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-transcribe/refs/heads/main/vocabulary/amazon-transcribe-vocabulary.yaml
created: '2024-01-15'
description: Amazon Transcribe is a speech-to-text service that uses machine learning models to convert audio to text, supporting real-time streaming and batch transcription with automatic speech recognition (ASR).
examples:
- key_count: 2
  name: Amazon Transcribe Example
  slug: amazon-transcribe-example
features:
- description: Automate operational tasks with Amazon Transcribe.
  name: Automation
- description: Programmatic access to Amazon Transcribe resources.
  name: API Access
finops:
- name: Amazon Transcribe Finops
  service_category: API
  slug: amazon-transcribe-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Transcribe Transcription Job
  property_count: 13
  slug: amazon-transcribe-job
- name: Tag
  property_count: 2
  slug: amazon-transcribe-tag
- name: TranscriptionJob
  property_count: 8
  slug: amazon-transcribe-transcription-job
json_structures:
- name: Amazon Transcribe Job Structure
  property_count: 0
  slug: amazon-transcribe-job-structure
- name: Amazon Transcribe Tag Structure
  property_count: 0
  slug: amazon-transcribe-tag-structure
- name: Amazon Transcribe Transcription Job Structure
  property_count: 0
  slug: amazon-transcribe-transcription-job-structure
jsonld:
- class_count: 7
  name: Amazon Transcribe Context
  property_count: 5
  slug: amazon-transcribe-context
layout: provider
modified: '2026-05-19'
name: Amazon Transcribe
nav: Providers
network: true
overview: 'Amazon Transcribe publishes 2 APIs on the [APIs.io](https://apis.io/) network: Transcription Jobs API and Vocabularies API. Tagged areas include Audio Processing, Machine Learning, Speech Recognition, Speech-To-Text, and Transcription.


  The Amazon Transcribe catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Transcribe''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 17 more developer resources.'
plans:
- name: Amazon Transcribe Plans Pricing
  plan_count: 3
  slug: amazon-transcribe-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Amazon Transcribe Rate Limits
  slug: amazon-transcribe-rate-limits
rules:
- name: Amazon Transcribe API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-transcribe-jsonschema-spectral-rules
- name: Amazon Transcribe API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 9
  slug: amazon-transcribe-spectral-rules
score:
  band: exemplar
  composite: 66.4
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 72.9
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-transcribe/refs/heads/main/screenshots/amazon-transcribe-2026-06-20T171840.png
security:
- kind: authentication
  name: Amazon Transcribe Authentication
  slug: amazon-transcribe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Transcribe Domain Security
  slug: amazon-transcribe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Transcribe Vulnerability Disclosure
  slug: amazon-transcribe-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Transcribe Trust Center
  slug: amazon-transcribe-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-transcribe
tags:
- Audio Processing
- Machine Learning
- Speech Recognition
- Speech-To-Text
- Transcription
use_cases:
- description: Use Amazon Transcribe to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/transcribe/
---
