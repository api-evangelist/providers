---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nse-india-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nseindia.com
created: '2026-07-17'
description: National Stock Exchange of India (NSE), operating at nseindia.com, is one of the world's largest stock exchanges by number of trades and derivatives contracts, headquartered in Mumbai. It runs electronic equity, derivatives, debt, and currency markets, publishes market data and corporate filings, and maintains the Nifty family of indices via NSE Indices. NSE exposes market data primarily through licensed data feeds and the undocumented endpoints powering nseindia.com rather than a published public developer API program; this profile was surfaced as an enrichment lead and has no documented public REST API surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nse-india.png
layout: provider
modified: '2026-07-20'
name: Nse-india
nav: Providers
network: true
overview: Nse-india is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Stock Exchange, Financial Services, Market Data, and Capital Markets.
random_paper: 76
score:
  band: minimal
  composite: 5.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nse-india/refs/heads/main/screenshots/nse-india-2026-08-07T185704.png
security:
- kind: domain-security
  name: Nse India Domain Security
  slug: nse-india-domain-security
  summary_line: DNSSEC · DMARC
slug: nse-india
tags:
- Company
- Stock Exchange
- Financial Services
- Market Data
- Capital Markets
- Trading
- India
website: https://www.nseindia.com
---
