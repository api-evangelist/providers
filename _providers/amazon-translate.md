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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Amazon Translate Agentic Access
  operation_count: 4
  slug: amazon-translate-agentic-access
  summary_line: 4 operations · 4 acting
api_count: 3
apis:
- description: The Batch Translation API from Amazon Translate — 2 operation(s) for batch translation.
  name: Amazon Translate Batch Translation API
  slug: amazon-translate-batch-translation-api
- description: The Terminology API from Amazon Translate — 1 operation(s) for terminology.
  name: Amazon Translate Terminology API
  slug: amazon-translate-terminology-api
- description: The Translation API from Amazon Translate — 1 operation(s) for translation.
  name: Amazon Translate Translation API
  slug: amazon-translate-translation-api
artifact_total: 30
collections:
- collection_type: postman
  name: Amazon Translate Batch Translation API
  slug: postman-amazon-translate-batch-translation-api
- collection_type: postman
  name: Amazon Translate Batch Translation Terminology API
  slug: postman-amazon-translate-terminology-api
- collection_type: postman
  name: Amazon Translate Batch Translation API
  slug: postman-amazon-translate-translation-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Translate Batch Translation API
  slug: open-amazon-translate-batch-translation-api
- collection_type: open
  name: Amazon Translate Batch Translation Terminology API
  slug: open-amazon-translate-terminology-api
- collection_type: open
  name: Amazon Translate Batch Translation API
  slug: open-amazon-translate-translation-api
- collection_type: open
  name: Amazon Translate API
  slug: open-amazon-translate
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-translate/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-translate-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-translate-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-translate-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-translate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-translate-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/translate/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/translate/
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
  url: https://console.aws.amazon.com/translate/
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
  url: https://stackoverflow.com/questions/tagged/amazon-translate
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-translate/refs/heads/main/rules/amazon-translate-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-translate/refs/heads/main/vocabulary/amazon-translate-vocabulary.yaml
created: '2024-01-15'
description: Amazon Translate is a neural machine translation service that delivers fast, high-quality, affordable, and customizable language translation for applications and content.
examples:
- key_count: 2
  name: Amazon Translate Example
  slug: amazon-translate-example
features:
- description: Automate operational tasks with Amazon Translate.
  name: Automation
- description: Programmatic access to Amazon Translate resources.
  name: API Access
finops:
- name: Amazon Translate Finops
  service_category: API
  slug: amazon-translate-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Translate Translation Job
  property_count: 12
  slug: amazon-translate-job
- name: Tag
  property_count: 2
  slug: amazon-translate-tag
json_structures:
- name: Amazon Translate Job Structure
  property_count: 0
  slug: amazon-translate-job-structure
- name: Amazon Translate Tag Structure
  property_count: 0
  slug: amazon-translate-tag-structure
jsonld:
- class_count: 7
  name: Amazon Translate Context
  property_count: 5
  slug: amazon-translate-context
layout: provider
modified: '2026-05-19'
name: Amazon Translate
nav: Providers
network: true
overview: 'Amazon Translate publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Translation API, Terminology API, and Translation API. Tagged areas include Language Processing, Localization, Machine Translation, NLP, and Translation.


  The Amazon Translate catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Translate''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 17 more developer resources.'
plans:
- name: Amazon Translate Plans Pricing
  plan_count: 3
  slug: amazon-translate-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Amazon Translate Rate Limits
  slug: amazon-translate-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Amazon Translate API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-translate-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Amazon Translate API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: amazon-translate-spectral-rules
score:
  band: strong
  composite: 59.0
  delta: 8.7
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 76.2
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-translate/refs/heads/main/screenshots/amazon-translate-2026-06-20T171839.png
security:
- kind: authentication
  name: Amazon Translate Authentication
  slug: amazon-translate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Translate Domain Security
  slug: amazon-translate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Translate Vulnerability Disclosure
  slug: amazon-translate-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Translate Trust Center
  slug: amazon-translate-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-translate
tags:
- Language Processing
- Localization
- Machine Translation
- NLP
- Translation
use_cases:
- description: Use Amazon Translate to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/translate/
---
