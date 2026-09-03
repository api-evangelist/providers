---
access_model:
  confidence: high
  label: Enterprise (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Evisort Agentic Access
  operation_count: 5
  slug: evisort-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.evisort.com/v1
  baseurl_source: declared
  description: Exchange an Evisort API key for a short-lived JWT bearer token.
  name: Evisort Authentication API
  slug: evisort-authentication-api
- baseURL: https://api.evisort.com/v1
  baseurl_source: declared
  description: Upload, retrieve, and download contract documents.
  name: Evisort Documents API
  slug: evisort-documents-api
- baseURL: https://api.evisort.com/v1
  baseurl_source: declared
  description: Read and write AI-extracted fields, clauses, and metadata.
  name: Evisort Fields API
  slug: evisort-fields-api
- baseURL: https://api.evisort.com/v1
  baseurl_source: declared
  description: Query documents across a workspace.
  name: Evisort Search API
  slug: evisort-search-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Evisort Authentication API
  slug: open-evisort-authentication-api
- collection_type: open
  name: Evisort Authentication Documents API
  slug: open-evisort-documents-api
- collection_type: open
  name: Evisort Authentication Fields API
  slug: open-evisort-fields-api
- collection_type: open
  name: Evisort Authentication Search API
  slug: open-evisort-search-api
- collection_type: open
  name: Evisort API
  slug: open-evisort
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/workday/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/evisort-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evisort-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/evisort-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evisort
- group: company
  title: ''
  type: Website
  url: https://www.evisort.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.evisort.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/evisort-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/evisort-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/evisort-finops.yml
created: '2026-06-21'
description: Evisort is an AI-powered contract lifecycle management (CLM) and contract intelligence platform that lets teams upload, search, and extract data from contracts, and automate contract generation and review workflows. Evisort was acquired by Workday in 2024 and is now offered as Workday Contract Lifecycle Management, powered by Evisort. Its REST API supports document upload and retrieval, field and metadata extraction, search, workflow automation, and webhooks, authenticated with an Evisort API key exchanged for a JWT bearer token.
finops:
- name: Evisort Finops
  service_category: Management and Governance
  slug: evisort-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evisort.png
layout: provider
modified: '2026-06-21'
name: Evisort
nav: Providers
network: true
overview: 'Evisort publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Fields API, and 1 more. Tagged areas include Contract Lifecycle Management, CLM, Contract Intelligence, Document AI, and Legal Tech.


  Evisort''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Evisort Plans Pricing
  plan_count: 1
  slug: evisort-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Evisort Rate Limits
  slug: evisort-rate-limits
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/evisort/refs/heads/main/screenshots/evisort-2026-07-25T213806.png
security:
- kind: authentication
  name: Evisort Authentication
  slug: evisort-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Evisort Domain Security
  slug: evisort-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: evisort
tags:
- Contract Lifecycle Management
- CLM
- Contract Intelligence
- Document AI
- Legal Tech
website: https://www.evisort.com
---
