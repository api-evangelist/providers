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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Timestream Agentic Access
  operation_count: 7
  slug: amazon-timestream-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Timestream databases.
  name: Amazon Timestream Databases API
  slug: amazon-timestream-databases-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: Operations for querying time series data.
  name: Amazon Timestream Query API
  slug: amazon-timestream-query-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Timestream tables.
  name: Amazon Timestream Tables API
  slug: amazon-timestream-tables-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: Operations for writing time series data.
  name: Amazon Timestream Write API
  slug: amazon-timestream-write-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: The Timestream Batch Load Task API from Amazon Timestream — 3 operation(s) for timestream batch load task.
  name: Amazon Timestream Timestream Batch Load Task API
  slug: amazon-timestream-batch-load-task-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: The Timestream Operations API from Amazon Timestream — 8 operation(s) for timestream operations.
  name: Amazon Timestream Timestream Operations API
  slug: amazon-timestream-operations-api
- baseURL: https://ingest.timestream.amazonaws.com
  baseurl_source: declared
  description: The Timestream Scheduled Query API from Amazon Timestream — 6 operation(s) for timestream scheduled query.
  name: Amazon Timestream Timestream Scheduled Query API
  slug: amazon-timestream-scheduled-query-api
artifact_total: 32
collections:
- collection_type: postman
  name: Amazon Timestream Databases API
  slug: postman-amazon-timestream-databases-api
- collection_type: postman
  name: Amazon Timestream Databases Query API
  slug: postman-amazon-timestream-query-api
- collection_type: postman
  name: Amazon Timestream Databases Tables API
  slug: postman-amazon-timestream-tables-api
- collection_type: postman
  name: Amazon Timestream Databases Write API
  slug: postman-amazon-timestream-write-api
- collection_type: open
  name: Amazon Timestream Databases API
  slug: open-amazon-timestream-databases-api
- collection_type: open
  name: Amazon Timestream Databases Query API
  slug: open-amazon-timestream-query-api
- collection_type: open
  name: Amazon Timestream Databases Tables API
  slug: open-amazon-timestream-tables-api
- collection_type: open
  name: Amazon Timestream Databases Write API
  slug: open-amazon-timestream-write-api
- collection_type: open
  name: Amazon Timestream
  slug: open-amazon-timestream
common:
- group: commercial
  href: https://artifacts.apis.io/amazon-timestream/plans/amazon-timestream-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amazon-timestream-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/amazon-timestream/rate-limits/amazon-timestream-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/amazon-timestream-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/amazon-timestream/finops/amazon-timestream-finops.yml
  title: ''
  type: FinOps
  url: finops/amazon-timestream-finops.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-timestream/overview
- group: agent
  href: https://artifacts.apis.io/amazon-timestream/agentic-access/amazon-timestream-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-timestream-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/amazon-timestream/security/amazon-timestream-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/amazon-timestream-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/amazon-timestream/security/amazon-timestream-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-timestream-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-timestream/security/amazon-timestream-domain-security.yml
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
- has_sources: true
  method: derived
  name: Amazon Timestream Finops
  primary_unit: gb-month
  service_category: ''
  slug: amazon-timestream-finops
  template: false
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
overview: 'Amazon Timestream publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Databases API, Query API, Tables API, and 4 more. Tagged areas include Database, IoT, and Time Series.


  The Amazon Timestream catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Timestream''s developer surface includes developer portal, documentation, support, developer console, signup flow, and 17 more developer resources.'
plans:
- name: Amazon Timestream Plans Pricing
  plan_count: 15
  slug: amazon-timestream-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Amazon Timestream Rate Limits
  slug: amazon-timestream-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Amazon Timestream — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: amazon-timestream-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Amazon Timestream API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 8
  slug: amazon-timestream-spectral-rules
score:
  band: strong
  composite: 58.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 64.0
    catalog_earned_first_party: 12.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.6
  facets:
    access_clarity: 92.1
    contract_governance: 27.3
    contract_quality: 55.0
    developer_ergonomics: 44.0
    discoverability: 64.3
    operational_transparency: 39.5
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 85.7
      derived: 0
      marker_coverage: 42.9
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amazon-timestream/amazon-timestream-2026-06-20T171834.png
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
- IoT
- Time Series
use_cases:
- description: Use Amazon Timestream to manage and automate cloud operations.
  name: Cloud Operations
website: https://aws.amazon.com/timestream/
---
