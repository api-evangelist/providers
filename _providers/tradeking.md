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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradeking-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tradeking.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradeking
- group: build
  title: ''
  type: Packages
  url: packages/tradeking-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tradeking-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradeking-llms.txt
created: '2026-07-17'
description: TradeKing was a US online brokerage offering commission-based self-directed trading of stocks and options, backed by Battery Ventures. It pioneered one of the first public brokerage APIs, letting developers manage accounts, place equity and options orders, stream real-time market quotes, and manage watchlists over OAuth 1.0. TradeKing was acquired by Ally Financial in 2016 and rebranded as Ally Invest; its API surface lives on as the Ally Invest API (profiled separately as ally-invest in this network). tradeking.com now redirects to ally.com/invest and the historical API hosts no longer resolve. This profile is maintained as a historical record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradeking.png
layout: provider
modified: '2026-07-21'
name: TradeKing
nav: Providers
network: true
overview: TradeKing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brokerage, Trading, Investing, and Stocks.
random_paper: 73
score:
  band: minimal
  composite: 7.9
  delta: -0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Tradeking Domain Security
  slug: tradeking-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tradeking
tags:
- Company
- Brokerage
- Trading
- Investing
- Stocks
- Options
- Acquired
website: https://www.tradeking.com
---
