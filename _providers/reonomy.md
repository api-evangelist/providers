---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Reonomy Agentic Access
  operation_count: 5
  slug: reonomy-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 2
apis:
- description: Retrieve detailed property records by ID.
  name: Reonomy Property API
  slug: reonomy-property-api
- description: Search and resolve commercial real-estate properties.
  name: Reonomy Search API
  slug: reonomy-search-api
artifact_total: 9
collections:
- collection_type: open
  name: Reonomy Property API
  slug: open-reonomy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reonomy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reonomy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reonomy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reonomy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reonomy
- group: company
  title: ''
  type: Website
  url: https://www.reonomy.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.reonomy.com/v2/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/reonomy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reonomy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reonomy-finops.yml
created: '2026-06-21'
description: Reonomy (an Altus Group company) is a commercial real-estate property-intelligence platform whose REST API delivers property search, property detail, ownership, mortgage, sales and debt, tax, tenant, and contact / skip-trace data across U.S. commercial real estate. The API resolves addresses to a stable Reonomy property ID and returns rich detail records keyed by that ID.
finops:
- name: Reonomy Finops
  service_category: Data and Analytics
  slug: reonomy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reonomy.png
layout: provider
modified: '2026-06-21'
name: Reonomy
nav: Providers
network: true
overview: 'Reonomy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Property API and Search API. Tagged areas include Commercial Real Estate, Property Data, Property Intelligence, Ownership, and Skip Trace.


  Reonomy''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Reonomy Plans Pricing
  plan_count: 2
  slug: reonomy-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 3
  name: Reonomy Rate Limits
  slug: reonomy-rate-limits
score:
  band: thin
  composite: 36.6
  delta: -0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Reonomy Authentication
  slug: reonomy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reonomy Domain Security
  slug: reonomy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reonomy
tags:
- Commercial Real Estate
- Property Data
- Property Intelligence
- Ownership
- Skip Trace
website: https://www.reonomy.com
---
