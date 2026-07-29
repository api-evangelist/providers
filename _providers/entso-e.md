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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Entso E Agentic Access
  operation_count: 2
  slug: entso-e-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Single query endpoint for every Transparency Platform data item. The documentType, processType, and domain parameters select the dataset.
  name: ENTSO-E Market Data Query API
  slug: entso-e-market-data-query-api
artifact_total: 8
collections:
- collection_type: open
  name: ENTSO-E Transparency Platform RESTful API
  slug: open-entso-e
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/entso-e-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entso-e-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/entso-e-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entso-e
- group: company
  title: ''
  type: Website
  url: https://www.entsoe.eu/
- group: start
  title: ''
  type: Portal
  url: https://transparency.entsoe.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://transparencyplatform.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/entso-e-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/entso-e-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/entso-e-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.entsoe.eu/news/
created: '2026-07-11'
description: ENTSO-E, the European Network of Transmission System Operators for Electricity, operates the Transparency Platform - the central publication point for pan-European electricity market data under EU Regulation 543/2013. Its free RESTful API returns day-ahead prices, system load, generation, balancing, and cross-border transmission data for every European bidding zone and control area as IEC 62325 XML market documents, selected by coded documentType and processType parameters against a single endpoint.
finops:
- name: Entso E Finops
  service_category: Analytics and Data
  slug: entso-e-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/entso-e.png
layout: provider
modified: '2026-07-11'
name: ENTSO-E
nav: Providers
network: true
overview: 'ENTSO-E publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data Query API. Tagged areas include Electricity, Energy, Energy Markets, Day-Ahead Prices, and Balancing.


  ENTSO-E''s developer surface includes authentication, developer portal, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Entso E Plans Pricing
  plan_count: 1
  slug: entso-e-plans-pricing
random_paper: 67
rate_limits:
- limit_count: 5
  name: Entso E Rate Limits
  slug: entso-e-rate-limits
score:
  band: thin
  composite: 35.0
  delta: -5.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.9
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 16.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/entso-e/refs/heads/main/screenshots/entso-e-2026-07-25T213441.png
security:
- kind: authentication
  name: Entso E Authentication
  slug: entso-e-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Entso E Domain Security
  slug: entso-e-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: entso-e
tags:
- Electricity
- Energy
- Energy Markets
- Day-Ahead Prices
- Balancing
- Transmission
- Grid Data
- Europe
website: https://www.entsoe.eu/
---
