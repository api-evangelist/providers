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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Spanner Agentic Access
  operation_count: 10
  slug: google-cloud-spanner-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 3
apis:
- description: Operations on Spanner databases
  name: Google Cloud Spanner Databases API
  slug: google-cloud-spanner-databases-api
- description: Operations on Spanner instances
  name: Google Cloud Spanner Instances API
  slug: google-cloud-spanner-instances-api
- description: Operations on database sessions
  name: Google Cloud Spanner Sessions API
  slug: google-cloud-spanner-sessions-api
artifact_total: 22
collections:
- collection_type: postman
  name: Google Cloud Spanner Databases API
  slug: postman-google-cloud-spanner-databases-api
- collection_type: postman
  name: Google Cloud Spanner Databases Instances API
  slug: postman-google-cloud-spanner-instances-api
- collection_type: postman
  name: Google Cloud Spanner Databases Sessions API
  slug: postman-google-cloud-spanner-sessions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Spanner API
  slug: open-cloud-spanner
- collection_type: open
  name: Google Cloud Spanner Databases API
  slug: open-google-cloud-spanner-databases-api
- collection_type: open
  name: Google Cloud Spanner Databases Instances API
  slug: open-google-cloud-spanner-instances-api
- collection_type: open
  name: Google Cloud Spanner Databases Sessions API
  slug: open-google-cloud-spanner-sessions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-spanner/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-spanner-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-spanner-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-spanner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-spanner-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-spanner-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/spanner
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/spanner/docs/getting-started/rest
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/spanner/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/spanner/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/spanner/pricing
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
  url: https://cloud.google.com/spanner/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-spanner-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/spanner-release-notes.xml
created: '2026-03-13'
description: Google Cloud Spanner is a fully managed, mission-critical relational database service that offers transactional consistency at global scale, automatic synchronous replication, and schemas with SQL support. It combines the benefits of relational database structure with non-relational horizontal scale, providing up to 99.999% availability.
finops:
- name: Google Cloud Spanner Finops
  service_category: API
  slug: google-cloud-spanner-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-spanner.png
json_schemas:
- name: Google Cloud Spanner Instance
  property_count: 10
  slug: instance
jsonld:
- class_count: 16
  name: Google Cloud Spanner Context
  property_count: 0
  slug: google-cloud-spanner-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Spanner
nav: Providers
network: true
overview: 'Google Cloud Spanner publishes 3 APIs on the [APIs.io](https://apis.io/) network: Databases API, Instances API, and Sessions API. Tagged areas include Database, Distributed, Google Cloud, Relational, and SQL.


  The Google Cloud Spanner catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Spanner''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Spanner Plans Pricing
  plan_count: 3
  slug: google-cloud-spanner-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Google Cloud Spanner Rate Limits
  slug: google-cloud-spanner-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Spanner API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-spanner-jsonschema-spectral-rules
scopes:
- name: Google Cloud Spanner Scopes
  scope_count: 3
  slug: google-cloud-spanner-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 66.4
    developer_ergonomics: 54.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-spanner/refs/heads/main/screenshots/google-cloud-spanner-2026-06-20T182136.png
security:
- kind: authentication
  name: Google Cloud Spanner Authentication
  slug: google-cloud-spanner-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Spanner Domain Security
  slug: google-cloud-spanner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Spanner Vulnerability Disclosure
  slug: google-cloud-spanner-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-spanner
tags:
- Database
- Distributed
- Google Cloud
- Relational
- SQL
website: https://cloud.google.com/spanner
---
