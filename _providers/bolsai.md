---
access_model:
  confidence: high
  label: Self-serve freemium — Google login, free 200 req/day tier, in-browser playground
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://usebolsai.com/#pricing
  - https://usebolsai.com/#playground
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST/JSON API for Brazilian financial-market data — equities, FIIs, fundamentals, dividends, financial statements, and macro series. Authenticated via X-API-Key header.
  name: Bolsai Financial Data API
  slug: bolsai-financial-data-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bolsai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bolsai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/bolsai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bolsai-well-known.yml
- group: company
  title: ''
  type: Blog
  url: https://usebolsai.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://usebolsai.com/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:vinicius.lazzari@usebolsai.com
created: '2026-07-06'
description: Brazilian financial-market data REST API serving equities, real-estate funds (FIIs), fundamentals, dividends, financial statements, and macroeconomic series sourced from official feeds (B3, CVM, BCB). Covers 350+ B3 stocks, 400+ FIIs and 40 years of price history, with an official MCP server (hosted OAuth endpoint and PyPI package) for AI agents.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bolsai.png
layout: provider
mcp_servers:
- description: Official Bolsai MCP server exposing Brazilian financial-market data (B3 stocks, FIIs, fundamentals, dividends, CVM financial statements, BCB macro series) to MCP clients. Available BOTH as a hosted re
  name: Bolsai MCP Server
  slug: bolsai-mcp-server
modified: '2026-09-03'
name: Bolsai
nav: Providers
network: true
overview: 'Bolsai publishes 1 API on the [APIs.io](https://apis.io/) network: Financial Data API. Tagged areas include Finance, Financial Data, Market Data, Stocks/equities, and Real Estate Funds.


  Bolsai''s developer surface includes authentication, engineering blog, pricing, support, and 3 more developer resources.'
plans:
- name: Bolsai Plans Pricing
  plan_count: 3
  slug: bolsai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Bolsai Rate Limits
  slug: bolsai-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 34.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bolsai/refs/heads/main/screenshots/bolsai-2026-07-25T203539.png
security:
- kind: authentication
  name: Bolsai Authentication
  slug: bolsai-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Bolsai Domain Security
  slug: bolsai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bolsai
tags:
- Finance
- Financial Data
- Market Data
- Stocks/equities
- Real Estate Funds
- Dividends
- Fundamentals
- Macroeconomic Data
- Brazil
- Developer Tools
- MCP
- AI Agents
---
