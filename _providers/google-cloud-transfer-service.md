---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Transfer Service Agentic Access
  operation_count: 8
  slug: google-cloud-transfer-service-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://storagetransfer.googleapis.com
  baseurl_source: declared
  description: Operations for managing transfer jobs
  name: Google Cloud Transfer Service TransferJobs API
  slug: google-cloud-transfer-service-transferjobs-api
- baseURL: https://storagetransfer.googleapis.com
  baseurl_source: declared
  description: Operations for monitoring transfer operations
  name: Google Cloud Transfer Service TransferOperations API
  slug: google-cloud-transfer-service-transferoperations-api
- baseURL: https://storagetransfer.googleapis.com
  baseurl_source: declared
  description: Operations for managing on-premises transfer agent pools
  name: Google Cloud Transfer Service Agent Pools API
  slug: google-cloud-transfer-service-agent-pools-api
artifact_total: 18
collections:
- collection_type: open
  name: Google Cloud Transfer Service Google Storage Transfer AgentPools API
  slug: open-google-cloud-transfer-service-agentpools-api
- collection_type: open
  name: Google Cloud Transfer Service Google Storage Transfer AgentPools TransferJobs API
  slug: open-google-cloud-transfer-service-transferjobs-api
- collection_type: open
  name: Google Cloud Transfer Service Google Storage Transfer AgentPools TransferOperations API
  slug: open-google-cloud-transfer-service-transferoperations-api
- collection_type: open
  name: Google Cloud Transfer Service Google Storage Transfer API
  slug: open-storage-transfer-api
common:
- group: commercial
  href: https://artifacts.apis.io/google-cloud-transfer-service/plans/google-cloud-transfer-service-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-cloud-transfer-service-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-cloud-transfer-service/rate-limits/google-cloud-transfer-service-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-cloud-transfer-service-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/google-cloud-transfer-service/finops/google-cloud-transfer-service-finops.yml
  title: ''
  type: FinOps
  url: finops/google-cloud-transfer-service-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.google.com/
- group: agent
  href: https://artifacts.apis.io/google-cloud-transfer-service/agentic-access/google-cloud-transfer-service-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-transfer-service-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-transfer-service/security/google-cloud-transfer-service-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-transfer-service-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-transfer-service/security/google-cloud-transfer-service-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-cloud-transfer-service-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-transfer-service/authentication/google-cloud-transfer-service-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-cloud-transfer-service-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-cloud-transfer-service/scopes/google-cloud-transfer-service-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-transfer-service-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/storage-transfer/docs/create-transfers
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/storage-transfer/pricing
- group: design
  href: https://artifacts.apis.io/google-cloud-transfer-service/json-ld/google-cloud-transfer-service-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-transfer-service-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/storagetransfer-release-notes.xml
created: '2026-03-13'
description: Google Cloud Storage Transfer Service enables seamless data movement across object and file storage systems, including transfers from Amazon S3, Azure Blob Storage, or Cloud Storage to Cloud Storage, and from on-premises storage to Cloud Storage. It is optimized for large-scale transfers involving terabytes or petabytes of data.
finops:
- has_sources: false
  method: generated
  name: Google Cloud Transfer Service Finops
  primary_unit: request
  service_category: API
  slug: google-cloud-transfer-service-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-transfer-service.png
json_schemas:
- name: Google Cloud Storage Transfer Job
  property_count: 8
  slug: google-cloud-transfer-service-job
jsonld:
- class_count: 0
  name: Google Cloud Transfer Service Context
  property_count: 5
  slug: google-cloud-transfer-service-context
layout: provider
modified: '2026-05-19'
name: Google Cloud Transfer Service
nav: Providers
network: true
overview: 'Google Cloud Transfer Service publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: TransferJobs API, TransferOperations API, and Agent Pools API. Tagged areas include Microsoft Azure, Cloud Storage, Data Transfer, Migration, and S3.


  The Google Cloud Transfer Service catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Transfer Service''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Google Cloud Transfer Service Plans Pricing
  plan_count: 3
  slug: google-cloud-transfer-service-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Google Cloud Transfer Service Rate Limits
  slug: google-cloud-transfer-service-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Google Cloud Transfer Service — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-transfer-service-jsonschema-spectral-rules
scopes:
- name: Google Cloud Transfer Service Scopes
  scope_count: 1
  slug: google-cloud-transfer-service-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.7
    catalog_earned_first_party: 0.0
    catalog_gap: 58.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 56.7
    developer_ergonomics: 35.7
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/google-cloud-transfer-service/google-cloud-transfer-service-2026-06-20T182144.png
security:
- kind: authentication
  name: Google Cloud Transfer Service Authentication
  slug: google-cloud-transfer-service-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Transfer Service Domain Security
  slug: google-cloud-transfer-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Transfer Service Vulnerability Disclosure
  slug: google-cloud-transfer-service-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-transfer-service
tags:
- Microsoft Azure
- Cloud Storage
- Data Transfer
- Migration
- S3
- Storage
website: https://www.google.com/
---
