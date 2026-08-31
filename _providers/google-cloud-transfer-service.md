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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Google Cloud Transfer Service Agentic Access
  operation_count: 8
  slug: google-cloud-transfer-service-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Google Cloud Transfer Service Rate Limits
  slug: google-cloud-transfer-service-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Cloud Transfer Service API Rules
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
    artifact_dirs: 14
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
