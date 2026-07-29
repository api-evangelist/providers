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
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Transfer Service Agentic Access
  operation_count: 8
  slug: google-cloud-transfer-service-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 3
apis:
- description: Operations for managing on-premises transfer agent pools
  name: Google Cloud Transfer Service AgentPools API
  slug: google-cloud-transfer-service-agentpools-api
- description: Operations for managing transfer jobs
  name: Google Cloud Transfer Service TransferJobs API
  slug: google-cloud-transfer-service-transferjobs-api
- description: Operations for monitoring transfer operations
  name: Google Cloud Transfer Service TransferOperations API
  slug: google-cloud-transfer-service-transferoperations-api
artifact_total: 15
collections:
- collection_type: open
  name: Google Cloud Transfer Service Google Storage Transfer API
  slug: open-storage-transfer-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-transfer-service-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-transfer-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-transfer-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-transfer-service-authentication.yml
- group: auth
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
- name: Google Cloud Transfer Service Finops
  service_category: API
  slug: google-cloud-transfer-service-finops
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
overview: 'Google Cloud Transfer Service publishes 3 APIs on the [APIs.io](https://apis.io/) network: AgentPools API, TransferJobs API, and TransferOperations API. Tagged areas include Azure, Cloud Storage, Data Transfer, Migration, and S3.


  The Google Cloud Transfer Service catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud Transfer Service''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Google Cloud Transfer Service Plans Pricing
  plan_count: 3
  slug: google-cloud-transfer-service-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Google Cloud Transfer Service Rate Limits
  slug: google-cloud-transfer-service-rate-limits
rules:
- name: Google Cloud Transfer Service API Rules
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
  band: developing
  composite: 50.9
  delta: -4.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 55.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-transfer-service/refs/heads/main/screenshots/google-cloud-transfer-service-2026-06-20T182144.png
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
- Azure
- Cloud Storage
- Data Transfer
- Migration
- S3
- Storage
---
