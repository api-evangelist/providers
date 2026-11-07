---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Airdna Agentic Access
  operation_count: 26
  slug: airdna-agentic-access
  summary_line: 26 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: Market and submarket discovery, metrics, and future pricing.
  name: AirDNA Market Data API
  slug: airdna-market-data-api
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: Pricing strategy base rates and smart rates for listings.
  name: AirDNA Smart Rates API
  slug: airdna-smart-rates-api
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: 'This section provides data for individual Short-Term Rental listings from Airbnb, Vrbo, and Booking.com. It is ideal for searching for listings within certain parameters and also fetching metrics for '
  name: AirDNA Listing Data API
  slug: airdna-listing-data-api
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: 'Rentalizer uses AirDNA''s proprietary algorithms and data to provide Performance Estimations for addresses or locations. ### What is Rentalizer? Across our Rentalizer endpoints, our performance estimat'
  name: AirDNA Rentalizer Data API
  slug: airdna-rentalizer-data-api
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: Rentalizer uses AirDNA's proprietary algorithms and data to provide Performance Estimates for addresses or locations.
  name: AirDNA Rentalizer Summary Data API
  slug: airdna-rentalizer-summary-data-api
- baseURL: https://api.airdna.co/api/enterprise/v2
  baseurl_source: declared
  description: 'Whether you''re looking to discover trending Submarkets or learn about a Submarket''s historical performance, these endpoints can support your research. ### Historical Submarket Data We provide between '
  name: AirDNA Submarket Data API
  slug: airdna-submarket-data-api
artifact_total: 20
collections:
- collection_type: open
  name: AirDNA Enterprise Market Data API
  slug: open-airdna-market-data-api
- collection_type: open
  name: AirDNA Enterprise Market Data Rentalizer API
  slug: open-airdna-rentalizer-api
- collection_type: open
  name: AirDNA Enterprise Market Data Rentalizer Lead Gen API
  slug: open-airdna-rentalizer-lead-gen-api
- collection_type: open
  name: AirDNA Enterprise Market Data Smart Rates API
  slug: open-airdna-smart-rates-api
- collection_type: open
  name: AirDNA Enterprise Market Data STR Listing Data API
  slug: open-airdna-str-listing-data-api
- collection_type: open
  name: AirDNA Enterprise API
  slug: open-airdna
common:
- group: other
  href: https://artifacts.apis.io/airdna/capabilities/airdna-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/airdna-capability-edges.yml
- group: company
  title: ''
  type: Blog
  url: https://www.airdna.co/press
- group: agent
  href: https://artifacts.apis.io/airdna/agentic-access/airdna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airdna-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/airdna/security/airdna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airdna-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/airdna/authentication/airdna-authentication.yml
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
  href: https://artifacts.apis.io/airdna/plans/airdna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airdna-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/airdna/rate-limits/airdna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airdna-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/airdna/finops/airdna-finops.yml
  title: ''
  type: FinOps
  url: finops/airdna-finops.yml
created: '2026-06-21'
description: AirDNA provides short-term rental market data and analytics for Airbnb and Vrbo, tracking over 10 million listings across 120,000+ markets. The AirDNA Enterprise API exposes market metrics, STR listing data, comparable property sets, Rentalizer revenue estimates, and Smart Rates pricing through a Bearer-authenticated REST interface.
finops:
- has_sources: true
  method: generated
  name: Airdna Finops
  primary_unit: ''
  service_category: Data and Analytics
  slug: airdna-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airdna.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.airdna.co over HTTP.
  name: AirDNA MCP Server
  slug: airdna
modified: '2026-10-06'
name: AirDNA
nav: Providers
network: true
overview: 'AirDNA publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Market Data API, Smart Rates API, Listing Data API, and 3 more. Tagged areas include Short-Term Rental, Vacation Rentals, Market Data, Real Estate, and Analytics.


  The AirDNA catalog on APIs.io includes 1 Spectral governance ruleset.


  AirDNA''s developer surface includes engineering blog, authentication, documentation, and 8 more developer resources.'
plans:
- name: Airdna Plans Pricing
  plan_count: 1
  slug: airdna-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Airdna Rate Limits
  slug: airdna-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: AirDNA API Rules
  rule_count: 60
  severity_counts:
    error: 50
    hint: 0
    info: 2
    warn: 8
  slug: airdna-rules
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 56.2
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 5.3
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/airdna/airdna-2026-07-25T195414.png
security:
- kind: authentication
  name: Airdna Authentication
  slug: airdna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airdna Domain Security
  slug: airdna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airdna
tags:
- Short-Term Rental
- Vacation Rentals
- Market Data
- Real Estate
- Analytics
website: https://www.airdna.co
---
