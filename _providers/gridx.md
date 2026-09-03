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
- acting_count: 2
  human_in_the_loop: 0
  name: Gridx Agentic Access
  operation_count: 8
  slug: gridx-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- baseURL: https://pge-pe-api.gridx.com/v1
  baseurl_source: declared
  description: The Authentication API from GridX — 1 operation(s) for authentication.
  name: GridX Authentication API
  slug: gridx-authentication-api
- baseURL: https://pge-pe-api.gridx.com/v1
  baseurl_source: declared
  description: The Customer API from GridX — 2 operation(s) for customer.
  name: GridX Customer API
  slug: gridx-customer-api
- baseURL: https://pge-pe-api.gridx.com/v1
  baseurl_source: declared
  description: The OpenADR API from GridX — 2 operation(s) for openadr.
  name: GridX OpenADR API
  slug: gridx-openadr-api
- baseURL: https://pge-pe-api.gridx.com/v1
  baseurl_source: declared
  description: The Pricing API from GridX — 1 operation(s) for pricing.
  name: GridX Pricing API
  slug: gridx-pricing-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GridX Enterprise Rate Platform Authentication API
  slug: open-gridx-authentication-api
- collection_type: open
  name: GridX Enterprise Rate Platform Authentication Customer API
  slug: open-gridx-customer-api
- collection_type: open
  name: GridX Enterprise Rate Platform Authentication OpenADR API
  slug: open-gridx-openadr-api
- collection_type: open
  name: GridX Enterprise Rate Platform Authentication Pricing API
  slug: open-gridx-pricing-api
- collection_type: open
  name: GridX Enterprise Rate Platform API
  slug: open-gridx
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gridx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gridx-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gridx-inc
- group: company
  title: ''
  type: Website
  url: https://www.gridx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-calculate-docs.gridx.com/calculate-apis-gridx-docs/get-pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/gridx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gridx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gridx-finops.yml
created: '2026-06-20'
description: GridX Inc. (Walnut Creek, California) is the Enterprise Rate Platform for modern utilities. Its cloud-based Rate Engine replicates utility billing-system (CIS) bill calculations to design, measure, implement, and bill advanced rates and programs. GridX exposes a partner/enterprise developer API (the Calculate / Empower APIs) for rate calculation, pricing retrieval, customer info/usage, bill and cost analysis, and OpenADR demand-response program subscriptions, currently documented for specific utility deployments (e.g., PG&E, SCE).
finops:
- name: Gridx Finops
  service_category: Energy and Utilities Software
  slug: gridx-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gridx.png
layout: provider
modified: '2026-06-20'
name: GridX
nav: Providers
network: true
overview: 'GridX publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Customer API, OpenADR API, and 1 more. Tagged areas include Energy, Utilities, Rate Engine, Billing, and Rate Analytics.


  GridX''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Gridx Plans Pricing
  plan_count: 1
  slug: gridx-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Gridx Rate Limits
  slug: gridx-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gridx/refs/heads/main/screenshots/gridx-2026-06-20T182406.png
security:
- kind: authentication
  name: Gridx Authentication
  slug: gridx-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gridx Domain Security
  slug: gridx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gridx
tags:
- Energy
- Utilities
- Rate Engine
- Billing
- Rate Analytics
website: https://www.gridx.com/
---
