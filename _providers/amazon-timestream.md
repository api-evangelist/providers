---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Amazon Timestream Agentic Access
  operation_count: 7
  slug: amazon-timestream-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 4
apis:
- description: Operations for managing Timestream databases.
  name: Amazon Timestream Databases API
  slug: amazon-timestream-databases-api
- description: Operations for querying time series data.
  name: Amazon Timestream Query API
  slug: amazon-timestream-query-api
- description: Operations for managing Timestream tables.
  name: Amazon Timestream Tables API
  slug: amazon-timestream-tables-api
- description: Operations for writing time series data.
  name: Amazon Timestream Write API
  slug: amazon-timestream-write-api
artifact_total: 21
collections:
- collection_type: open
  name: Amazon Timestream
  slug: open-amazon-timestream
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-timestream-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-timestream-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-timestream-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-timestream-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/timestream/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/timestream/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/timestream/
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
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/amazon-timestream/refs/heads/main/rules/amazon-timestream-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/amazon-timestream/refs/heads/main/vocabulary/amazon-timestream-vocabulary.yaml
created: '2024-01-15'
description: Amazon Timestream is a fast, scalable, and serverless time series database service designed for IoT and operational applications. It makes it easy to store and analyze trillions of events per day at a fraction of the cost of relational databases, with built-in time series analytics functions and automatic data lifecycle management.
examples:
- key_count: 2
  name: Amazon Timestream Example
  slug: amazon-timestream-example
features:
- description: Automate operational tasks with Amazon Timestream.
  name: Automation
- description: Programmatic access to Amazon Timestream resources.
  name: API Access
finops:
- name: Amazon Timestream Finops
  service_category: API
  slug: amazon-timestream-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Database
  property_count: 6
  slug: amazon-timestream-database
json_structures:
- name: Amazon Timestream Database Structure
  property_count: 0
  slug: amazon-timestream-database-structure
jsonld:
- class_count: 0
  name: Amazon Timestream Context
  property_count: 6
  slug: amazon-timestream-context
layout: provider
modified: '2026-05-19'
name: Amazon Timestream
nav: Providers
network: true
overview: 'Amazon Timestream publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Databases API, Query API, Tables API, and 1 more. Tagged areas include Database, Iot, and Time Series.


  The Amazon Timestream catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Timestream''s developer surface includes developer portal, documentation, support, developer console, signup flow, and 13 more developer resources.'
plans:
- name: Amazon Timestream Plans Pricing
  plan_count: 3
  slug: amazon-timestream-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Amazon Timestream Rate Limits
  slug: amazon-timestream-rate-limits
rules:
- name: Amazon Timestream API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-timestream-jsonschema-spectral-rules
- name: Amazon Timestream API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: amazon-timestream-spectral-rules
score:
  band: strong
  composite: 61.3
  delta: 3.3
  facets:
    commercial_clarity: 81.6
    contract_quality: 53.1
    developer_ergonomics: 28.3
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 58.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-timestream/refs/heads/main/screenshots/amazon-timestream-2026-06-20T171834.png
security:
- kind: domain-security
  name: Amazon Timestream Domain Security
  slug: amazon-timestream-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Timestream Vulnerability Disclosure
  slug: amazon-timestream-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Timestream Trust Center
  slug: amazon-timestream-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-timestream
tags:
- Database
- Iot
- Time Series
use_cases:
- description: Use Amazon Timestream to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/timestream/
---
