---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.5
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: Public and authenticated REST endpoints for spot and margin trading, including order placement, cancellation, order-book queries, trade history, and account balance management.
  name: Gate API v4 — Spot & Margin
  slug: gate-api-v4-spot-margin
- description: REST and WebSocket interfaces for linear and inverse perpetual futures contracts, including order management, position tracking, funding rates, and settlement data.
  name: Gate API v4 — Futures & Perpetuals
  slug: gate-api-v4-futures-perpetuals
- description: REST endpoints for options trading, including querying available contracts, placing and managing options orders, and retrieving settlement and Greeks data.
  name: Gate API v4 — Options
  slug: gate-api-v4-options
- description: Endpoints for deposit and withdrawal management, transfer between sub-accounts and trading accounts, currency information, and fee schedules.
  name: Gate API v4 — Wallet & Account
  slug: gate-api-v4-wallet-account
- description: 'Real-time WebSocket streams for market data (order books, trades, tickers, candlesticks) and private channels for order updates, balance changes, and position events across spot, futures, and options '
  name: Gate WebSocket API v4
  slug: gate-websocket-api-v4
- description: API provides spot, margin and futures trading operations
  name: Gateio
  slug: gateio
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gateio/gatews/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/gateio/gatews/releases
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gate-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gate.com/docs/developers/apiv4/en/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/gateio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gateio
- group: company
  title: ''
  type: Blog
  url: https://www.gate.io/blog/bloglist
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gate.com/fee
- group: operate
  title: ''
  type: StatusPage
  url: https://www.saashub.com/gate-io-status
- group: other
  title: ''
  type: X
  url: https://x.com/Gate_io
- group: commercial
  title: ''
  type: Plans
  url: plans/gate-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gate-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gate-io-finops.yml
created: '2026-06-13'
description: Gate.io is a pioneering cryptocurrency exchange serving over 23 million users globally since 2013. Its Gate API v4 provides REST and WebSocket interfaces for spot, margin, futures, options, and perpetual contract trading, as well as wallet management, earn products, sub-account operations, and comprehensive market data. SDKs are available in Python, Node.js, Java, Go, PHP, C#, and JavaScript, all generated from an OpenAPI specification.
finops:
- name: Gate Io Finops
  service_category: ''
  slug: gate-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gate-io.png
jsonld:
- class_count: 0
  name: Gate Io Context
  property_count: 14
  slug: gate-io-context
layout: provider
modified: '2026-06-13'
name: Gate.io
nav: Providers
network: true
overview: 'Gate.io publishes 1 API on the [APIs.io](https://apis.io/) network: Gate API v4 — Spot & Margin. Tagged areas include Cryptocurrency, Exchange, Trading, Spot Trading, and Margin Trading.


  The Gate.io catalog on APIs.io includes 1 JSON-LD context.


  Gate.io''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Gate Io Plans Pricing
  plan_count: 5
  slug: gate-io-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Gate Io Rate Limits
  slug: gate-io-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 36.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gate-io/refs/heads/main/screenshots/gate-io-2026-06-20T181655.png
security:
- kind: domain-security
  name: Gate Io Domain Security
  slug: gate-io-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gate-io
tags:
- Cryptocurrency
- Exchange
- Trading
- Spot Trading
- Margin Trading
- Futures
- Options
- WebSocket
- Market Data
- Wallets
website: https://www.gate.io/
---
