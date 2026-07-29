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
    asyncapi_events: true
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
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Polygon Io Agentic Access
  operation_count: 3
  slug: polygon-io-agentic-access
  summary_line: 3 operations
api_count: 8
apis:
- description: 'Real-time and historical US equity market data including aggregates (minute/hour/day bars), trades, NBBO quotes, snapshots, ticker reference, splits, dividends, and financials. Available via REST and '
  name: Polygon.io Stocks API
  slug: stocks-api
- description: 'OPRA-licensed options market data via REST and WebSocket: aggregates, trades, quotes, snapshots, contract reference, and option chains.'
  name: Polygon.io Options API
  slug: options-api
- description: Real-time and historical index values for major US and global indices via REST and WebSocket.
  name: Polygon.io Indices API
  slug: indices-api
- description: Real-time and historical FX prices for 1,000+ currency pairs via REST and WebSocket.
  name: Polygon.io Forex API
  slug: forex-api
- description: Aggregates, trades, snapshots, level-2 books, and L2 streaming for crypto pairs across major exchanges.
  name: Polygon.io Crypto API
  slug: crypto-api
- description: Real-time and historical futures market data including aggregates, trades, quotes, and snapshots.
  name: Polygon.io Futures API
  slug: futures-api
- description: Aggregate (OHLC) bar data.
  name: Polygon.io Aggregates API
  slug: polygon-io-aggregates-api
- description: Ticker reference data.
  name: Polygon.io Reference API
  slug: polygon-io-reference-api
artifact_total: 17
asyncapis:
- description: 'Streaming WebSocket APIs from Polygon.io (now operating as Massive) for real-time and delayed US Stocks, Options, Forex, Crypto, Indices, and Futures market data. Clients connect to a market-specific '
  name: Polygon.io WebSocket APIs
  slug: polygon-io-asyncapi
collections:
- collection_type: open
  name: Polygon.io REST API (Stocks)
  slug: open-polygon-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polygon-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polygon-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polygon-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polygon-io
- group: start
  title: ''
  type: Portal
  url: https://polygon.io/
- group: docs
  title: ''
  type: Documentation
  url: https://polygon.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://polygon.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.polygon.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/polygon-io
- group: commercial
  title: ''
  type: Plans
  url: plans/polygon-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/polygon-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/polygon-io-finops.yml
created: '2026-05-08'
description: Polygon.io (rebranded as Massive in early 2026) provides real-time and historical market data APIs across stocks, options, indices, forex, crypto, and futures via REST, WebSocket streaming, and S3-style flat files. APIs cover trades, quotes, aggregates, snapshots, ticker reference data, and corporate actions.
finops:
- name: Polygon Io Finops
  service_category: Fintech
  slug: polygon-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polygon-io.png
layout: provider
modified: '2026-05-29'
name: Polygon.io
nav: Providers
network: true
overview: 'Polygon.io publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Stocks API, Options API, Indices API, and 5 more. Tagged areas include Fintech, Market Data, Stocks, Options, and Forex.


  The Polygon.io catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Polygon.io''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, and 7 more developer resources.'
plans:
- name: Polygon Io Plans Pricing
  plan_count: 5
  slug: polygon-io-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 4
  name: Polygon Io Rate Limits
  slug: polygon-io-rate-limits
rules:
- name: Polygon.io API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: polygon-io-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.6
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.9
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polygon-io/refs/heads/main/screenshots/polygon-io-2026-06-20T191906.png
security:
- kind: authentication
  name: Polygon Io Authentication
  slug: polygon-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Polygon Io Domain Security
  slug: polygon-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polygon-io
tags:
- Fintech
- Market Data
- Stocks
- Options
- Forex
- Crypto
- Indices
- Futures
- WebSockets
- Real-time
- Historical
website: https://polygon.io/
---
