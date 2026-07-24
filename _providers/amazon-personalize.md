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
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Amazon Personalize Agentic Access
  operation_count: 1
  slug: amazon-personalize-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Operations for managing datasets and dataset groups
  name: Amazon Personalize Datasets API
  slug: amazon-personalize-datasets-api
arazzos:
- description: Create an empty Amazon Personalize dataset group for organizing training datasets.
  name: Amazon Personalize Create a Dataset Group
  slug: amazon-personalize-create-dataset-group-workflow
artifact_total: 31
collections:
- collection_type: postman
  name: Amazon Personalize API
  slug: postman-amazon-personalize
- collection_type: open
  name: Amazon Personalize API
  slug: open-amazon-personalize
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-personalize-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-personalize-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-personalize-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-personalize-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-personalize-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-personalize/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-personalize-create-dataset-group-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/category/artificial-intelligence/amazon-personalize/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/personalize/
- group: docs
  title: ''
  type: CLI Reference
  url: https://docs.aws.amazon.com/cli/latest/reference/personalize/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: Service Status
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/personalize/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/personalize/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/personalize/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/personalize/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/personalize/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-personalize
- group: build
  title: ''
  type: Code Examples
  url: https://docs.aws.amazon.com/code-library/latest/ug/personalize_code_examples.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-personalize-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-personalize-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-personalize-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-personalize-openapi-context.jsonld
- group: docs
  title: Amazon Personalize
  type: JSONSchema
  url: json-schema/amazon-personalize-schema.json
- group: docs
  title: Openapi Campaign
  type: JSONSchema
  url: json-schema/openapi-campaign-schema.json
- group: docs
  title: Openapi Create Dataset Group Request
  type: JSONSchema
  url: json-schema/openapi-create-dataset-group-request-schema.json
- group: docs
  title: Openapi Dataset Group
  type: JSONSchema
  url: json-schema/openapi-dataset-group-schema.json
- group: docs
  title: Openapi Solution
  type: JSONSchema
  url: json-schema/openapi-solution-schema.json
created: '2024-01-15'
description: Amazon Personalize is a fully managed machine learning service that enables developers to create individualized recommendations for customers using their applications.
examples:
- key_count: 12
  name: Amazon Personalize Example
  slug: amazon-personalize-example
- key_count: 5
  name: Openapi Campaign Example
  slug: openapi-campaign-example
- key_count: 2
  name: Openapi Create Dataset Group Request Example
  slug: openapi-create-dataset-group-request-example
- key_count: 5
  name: Openapi Dataset Group Example
  slug: openapi-dataset-group-example
- key_count: 5
  name: Openapi Solution Example
  slug: openapi-solution-example
finops:
- name: Amazon Personalize Finops
  service_category: API
  slug: amazon-personalize-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Amazon Personalize Dataset Group Definition
  property_count: 12
  slug: amazon-personalize
- name: Campaign
  property_count: 5
  slug: openapi-campaign
- name: CreateDatasetGroupRequest
  property_count: 2
  slug: openapi-create-dataset-group-request
- name: DatasetGroup
  property_count: 5
  slug: openapi-dataset-group
- name: Solution
  property_count: 5
  slug: openapi-solution
json_structures:
- name: Amazon Personalize Structure
  property_count: 12
  slug: amazon-personalize-structure
- name: Openapi Campaign Structure
  property_count: 5
  slug: openapi-campaign-structure
- name: Openapi Create Dataset Group Request Structure
  property_count: 2
  slug: openapi-create-dataset-group-request-structure
- name: Openapi Dataset Group Structure
  property_count: 5
  slug: openapi-dataset-group-structure
- name: Openapi Solution Structure
  property_count: 5
  slug: openapi-solution-structure
jsonld:
- class_count: 0
  name: Amazon Personalize Context
  property_count: 5
  slug: amazon-personalize-context
- class_count: 4
  name: Amazon Personalize Openapi Context
  property_count: 10
  slug: amazon-personalize-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon Personalize
nav: Providers
network: true
overview: 'Amazon Personalize publishes 1 API on the [APIs.io](https://apis.io/) network: Datasets API. Tagged areas include AI, Customer Experience, Machine Learning, ML, and Personalization.


  The Amazon Personalize catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Amazon Personalize''s developer surface includes authentication, engineering blog, support, developer console, documentation, pricing, getting-started guide, and 27 more developer resources.'
plans:
- name: Amazon Personalize Plans Pricing
  plan_count: 3
  slug: amazon-personalize-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Personalize Rate Limits
  slug: amazon-personalize-rate-limits
rules:
- name: Amazon Personalize API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amazon-personalize-jsonschema-spectral-rules
- name: Amazon Personalize API Rules
  rule_count: 25
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 13
  slug: amazon-personalize-spectral-rules
score:
  band: strong
  composite: 65.0
  delta: 0.0
  facets:
    commercial_clarity: 86.8
    contract_quality: 67.3
    developer_ergonomics: 54.3
    discoverability: 47.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 65.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-personalize/refs/heads/main/screenshots/amazon-personalize-2026-06-20T171758.png
security:
- kind: authentication
  name: Amazon Personalize Authentication
  slug: amazon-personalize-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Personalize Domain Security
  slug: amazon-personalize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Personalize Vulnerability Disclosure
  slug: amazon-personalize-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Personalize Trust Center
  slug: amazon-personalize-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-personalize
tags:
- AI
- Customer Experience
- Machine Learning
- ML
- Personalization
- Recommendations
website: https://aws.amazon.com/personalize/
---
