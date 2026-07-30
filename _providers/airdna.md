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
- acting_count: 22
  human_in_the_loop: 0
  name: Airdna Agentic Access
  operation_count: 26
  slug: airdna-agentic-access
  summary_line: 26 operations · 22 acting
api_count: 5
apis:
- description: Market and submarket discovery, metrics, and future pricing.
  name: AirDNA Market Data API
  slug: airdna-market-data-api
- description: Revenue estimates for individual and bulk addresses.
  name: AirDNA Rentalizer API
  slug: airdna-rentalizer-api
- description: Summarized performance estimates for lead generation.
  name: AirDNA Rentalizer Lead Gen API
  slug: airdna-rentalizer-lead-gen-api
- description: Pricing strategy base rates and smart rates for listings.
  name: AirDNA Smart Rates API
  slug: airdna-smart-rates-api
- description: Short-term rental listing search, details, history, and comps.
  name: AirDNA STR Listing Data API
  slug: airdna-str-listing-data-api
artifact_total: 12
collections:
- collection_type: open
  name: AirDNA Enterprise API
  slug: open-airdna
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airdna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airdna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airdna-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airdna
- group: company
  title: ''
  type: Website
  url: https://www.airdna.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airdna.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/airdna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airdna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airdna-finops.yml
created: '2026-06-21'
description: AirDNA provides short-term rental market data and analytics for Airbnb and Vrbo, tracking over 10 million listings across 120,000+ markets. The AirDNA Enterprise API exposes market metrics, STR listing data, comparable property sets, Rentalizer revenue estimates, and Smart Rates pricing through a Bearer-authenticated REST interface.
finops:
- name: Airdna Finops
  service_category: Data and Analytics
  slug: airdna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airdna.png
layout: provider
modified: '2026-06-21'
name: AirDNA
nav: Providers
network: true
overview: 'AirDNA publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Market Data API, Rentalizer API, Rentalizer Lead Gen API, and 2 more. Tagged areas include Short-Term Rental, Vacation Rental, Market Data, Real Estate, and Analytics.


  AirDNA''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Airdna Plans Pricing
  plan_count: 1
  slug: airdna-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Airdna Rate Limits
  slug: airdna-rate-limits
score:
  band: thin
  composite: 33.1
  delta: -1.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 55.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airdna/refs/heads/main/screenshots/airdna-2026-07-25T195414.png
security:
- kind: authentication
  name: Airdna Authentication
  slug: airdna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airdna Domain Security
  slug: airdna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airdna
tags:
- Short-Term Rental
- Vacation Rental
- Market Data
- Real Estate
- Analytics
website: https://www.airdna.co
---
