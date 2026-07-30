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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Google Cloud Bigtable Agentic Access
  operation_count: 10
  slug: google-cloud-bigtable-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 3
apis:
- description: Operations on Bigtable clusters within instances
  name: Google Cloud Bigtable Clusters API
  slug: google-cloud-bigtable-clusters-api
- description: Operations on Bigtable instances
  name: Google Cloud Bigtable Instances API
  slug: google-cloud-bigtable-instances-api
- description: Operations on Bigtable tables
  name: Google Cloud Bigtable Tables API
  slug: google-cloud-bigtable-tables-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters API
  slug: postman-google-cloud-bigtable-clusters-api
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters Instances API
  slug: postman-google-cloud-bigtable-instances-api
- collection_type: postman
  name: Google Cloud Bigtable Admin Clusters Tables API
  slug: postman-google-cloud-bigtable-tables-api
- collection_type: open
  name: Google Cloud Bigtable Admin API
  slug: open-cloud-bigtable
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-bigtable/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-bigtable-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-bigtable-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-bigtable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-bigtable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-bigtable-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/bigtable
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/bigtable/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/bigtable/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/bigtable/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/bigtable/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/bigtable/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-bigtable-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/bigtable-release-notes.xml
created: '2026-03-13'
description: Google Cloud Bigtable is a fully managed, scalable NoSQL database service designed for large analytical and operational workloads. It offers consistent sub-10ms latency and seamless scalability, making it ideal for time-series data, IoT, ad tech, fintech, and machine learning applications. Bigtable integrates with popular big data tools like Hadoop, Dataflow, and Dataproc.
finops:
- name: Google Cloud Bigtable Finops
  service_category: API
  slug: google-cloud-bigtable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-bigtable.png
json_schemas:
- name: Google Cloud Bigtable Instance
  property_count: 7
  slug: instance
jsonld:
- class_count: 16
  name: Google Cloud Bigtable Context
  property_count: 0
  slug: google-cloud-bigtable-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Bigtable
nav: Providers
network: true
overview: 'Google Cloud Bigtable publishes 3 APIs on the [APIs.io](https://apis.io/) network: Clusters API, Instances API, and Tables API. Tagged areas include Bigtable, Database, Google Cloud, NoSQL, and Wide Column.


  The Google Cloud Bigtable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Bigtable''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Bigtable Plans Pricing
  plan_count: 3
  slug: google-cloud-bigtable-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Google Cloud Bigtable Rate Limits
  slug: google-cloud-bigtable-rate-limits
rules:
- name: Google Cloud Bigtable API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: google-cloud-bigtable-jsonschema-spectral-rules
scopes:
- name: Google Cloud Bigtable Scopes
  scope_count: 3
  slug: google-cloud-bigtable-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 63.0
  delta: -3.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 70.3
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/screenshots/google-cloud-bigtable-2026-06-20T182046.png
security:
- kind: authentication
  name: Google Cloud Bigtable Authentication
  slug: google-cloud-bigtable-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Bigtable Domain Security
  slug: google-cloud-bigtable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Bigtable Vulnerability Disclosure
  slug: google-cloud-bigtable-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-bigtable
tags:
- Bigtable
- Database
- Google Cloud
- NoSQL
- Wide Column
website: https://cloud.google.com/bigtable
---
