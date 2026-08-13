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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Data Fusion Agentic Access
  operation_count: 9
  slug: google-cloud-data-fusion-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 3
apis:
- description: Operations for managing Data Fusion instances
  name: Google Cloud Data Fusion Instances API
  slug: google-cloud-data-fusion-instances-api
- description: Available locations for Data Fusion
  name: Google Cloud Data Fusion Locations API
  slug: google-cloud-data-fusion-locations-api
- description: Long-running operation management
  name: Google Cloud Data Fusion Operations API
  slug: google-cloud-data-fusion-operations-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Cloud Data Fusion Instances API
  slug: postman-google-cloud-data-fusion-instances-api
- collection_type: postman
  name: Google Cloud Data Fusion Instances Locations API
  slug: postman-google-cloud-data-fusion-locations-api
- collection_type: postman
  name: Google Cloud Data Fusion Instances Operations API
  slug: postman-google-cloud-data-fusion-operations-api
- collection_type: open
  name: Google Cloud Data Fusion API
  slug: open-google-cloud-data-fusion
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-data-fusion/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-data-fusion-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-data-fusion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-data-fusion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-data-fusion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-data-fusion-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/data-fusion
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/data-fusion/docs/quickstarts
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/data-fusion/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/data-fusion/docs/concepts/iam
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/data-fusion/pricing
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
  url: https://cloud.google.com/data-fusion/docs/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-data-fusion-context.jsonld
created: '2026-03-13'
description: Google Cloud Data Fusion is a fully managed, cloud-native data integration service that helps users build and manage ETL/ELT data pipelines. It provides a visual point-and-click interface for building data transformation pipelines, powered by the open-source CDAP framework.
finops:
- name: Google Cloud Data Fusion Finops
  service_category: API
  slug: google-cloud-data-fusion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-data-fusion.png
json_schemas:
- name: Google Cloud Data Fusion Instance
  property_count: 17
  slug: google-cloud-data-fusion-instance
jsonld:
- class_count: 14
  name: Google Cloud Data Fusion Context
  property_count: 1
  slug: google-cloud-data-fusion-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Data Fusion
nav: Providers
network: true
overview: 'Google Cloud Data Fusion publishes 3 APIs on the [APIs.io](https://apis.io/) network: Instances API, Locations API, and Operations API. Tagged areas include Data Integration, Data Pipelines, ETL, and Google Cloud.


  The Google Cloud Data Fusion catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Data Fusion''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 11 more developer resources.'
plans:
- name: Google Cloud Data Fusion Plans Pricing
  plan_count: 3
  slug: google-cloud-data-fusion-plans-pricing
random_paper: 97
rate_limits:
- limit_count: 5
  name: Google Cloud Data Fusion Rate Limits
  slug: google-cloud-data-fusion-rate-limits
rules:
- name: Google Cloud Data Fusion API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-data-fusion-jsonschema-spectral-rules
scopes:
- name: Google Cloud Data Fusion Scopes
  scope_count: 1
  slug: google-cloud-data-fusion-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.8
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 47.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-data-fusion/refs/heads/main/screenshots/google-cloud-data-fusion-2026-06-20T182058.png
security:
- kind: authentication
  name: Google Cloud Data Fusion Authentication
  slug: google-cloud-data-fusion-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Data Fusion Domain Security
  slug: google-cloud-data-fusion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Data Fusion Vulnerability Disclosure
  slug: google-cloud-data-fusion-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-data-fusion
tags:
- Data Integration
- Data Pipelines
- ETL
- Google Cloud
website: https://cloud.google.com/data-fusion
---
