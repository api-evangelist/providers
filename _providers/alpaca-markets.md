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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Alpaca Markets Agentic Access
  operation_count: 30
  slug: alpaca-markets-agentic-access
  summary_line: 30 operations · 10 acting
api_count: 1
apis:
- description: Real-time market data over WebSocket. Stocks stream at wss://stream.data.alpaca.markets/v2/{feed} (iex, sip, delayed_sip, test) and crypto at wss://stream.data.alpaca.markets/v1beta3/crypto/us. Authen
  name: Alpaca Market Data Streaming API
  slug: alpaca-markets-streaming-api
- description: Trading account details, configuration, and activities.
  name: Alpaca Account API
  slug: alpaca-markets-account-api
- description: Tradable asset catalog.
  name: Alpaca Assets API
  slug: alpaca-markets-assets-api
- description: Open and manage end-user brokerage accounts.
  name: Alpaca Broker - Accounts API
  slug: alpaca-markets-broker-accounts-api
- description: Transfers and journals between accounts.
  name: Alpaca Broker - Funding API
  slug: alpaca-markets-broker-funding-api
- description: Place orders on behalf of end-user accounts.
  name: Alpaca Broker - Trading API
  slug: alpaca-markets-broker-trading-api
- description: Market calendar and clock.
  name: Alpaca Market API
  slug: alpaca-markets-market-api
- description: Historical and latest crypto bars, trades, quotes, and orderbooks (v1beta3).
  name: Alpaca Market Data - Crypto API
  slug: alpaca-markets-market-data-crypto-api
- description: Real-time and historical market news (v1beta1).
  name: Alpaca Market Data - News API
  slug: alpaca-markets-market-data-news-api
- description: Options bars, trades, and snapshots (v1beta1).
  name: Alpaca Market Data - Options API
  slug: alpaca-markets-market-data-options-api
- description: Most-actives and movers screeners (v1beta1).
  name: Alpaca Market Data - Screener API
  slug: alpaca-markets-market-data-screener-api
- description: Historical and latest stock bars, trades, quotes, snapshots, and auctions.
  name: Alpaca Market Data - Stocks API
  slug: alpaca-markets-market-data-stocks-api
- description: Submit, list, replace, and cancel orders.
  name: Alpaca Orders API
  slug: alpaca-markets-orders-api
- description: Portfolio history and performance.
  name: Alpaca Portfolio API
  slug: alpaca-markets-portfolio-api
- description: Open positions and liquidation.
  name: Alpaca Positions API
  slug: alpaca-markets-positions-api
- description: User watchlists.
  name: Alpaca Watchlists API
  slug: alpaca-markets-watchlists-api
artifact_total: 39
asyncapis:
- description: AsyncAPI 2.6 description of Alpaca's **real-time market data WebSocket API**. Unlike many providers, Alpaca publishes a genuine, documented public WebSocket (`wss://`) surface for streaming market dat
  name: Alpaca Market Data Streaming (WebSocket)
  slug: alpaca-markets-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account API
  slug: open-alpaca-markets-account-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Assets API
  slug: open-alpaca-markets-assets-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Broker - Accounts API
  slug: open-alpaca-markets-broker-accounts-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Broker - Funding API
  slug: open-alpaca-markets-broker-funding-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Broker - Trading API
  slug: open-alpaca-markets-broker-trading-api
- collection_type: open
  name: Alpaca API (Trading, Data, Broker) Account Market API
  slug: open-alpaca-markets-market-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Market Data - Crypto API
  slug: open-alpaca-markets-market-data-crypto-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Market Data - News API
  slug: open-alpaca-markets-market-data-news-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Market Data - Options API
  slug: open-alpaca-markets-market-data-options-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Market Data - Screener API
  slug: open-alpaca-markets-market-data-screener-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Market Data - Stocks API
  slug: open-alpaca-markets-market-data-stocks-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Orders API
  slug: open-alpaca-markets-orders-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Portfolio API
  slug: open-alpaca-markets-portfolio-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Positions API
  slug: open-alpaca-markets-positions-api
- collection_type: open
  name: Alpaca API (Trading, Market Data, Broker) Account Watchlists API
  slug: open-alpaca-markets-watchlists-api
- collection_type: open
  name: Alpaca API
  slug: open-alpaca-markets
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alpaca-markets-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alpacahq
- group: company
  title: ''
  type: Website
  url: https://alpaca.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpaca.markets
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alpacahq
- group: commercial
  title: ''
  type: Plans
  url: plans/alpaca-markets-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alpaca-markets-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alpaca-markets-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://alpaca.markets/blog
created: '2026-07-11'
description: Alpaca is a developer-first, commission-free brokerage that exposes stock, ETF, options, and crypto trading and market data entirely through APIs. The Trading API places and manages orders against a free paper-trading sandbox (paper-api.alpaca.markets) or a live account (api.alpaca.markets/v2); the Market Data API serves historical and real-time stocks, crypto, options, news, and corporate actions over REST plus WebSocket streams (data.alpaca.markets and stream.data.alpaca.markets); and the Broker API lets businesses open and fund end-user brokerage accounts. Authentication uses APCA-API-KEY-ID and APCA-API-SECRET-KEY headers, with OAuth2 available for third-party apps.
finops:
- name: Alpaca Markets Finops
  service_category: Financial Services and Market Data
  slug: alpaca-markets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpaca-markets.png
layout: provider
modified: '2026-07-11'
name: Alpaca
nav: Providers
network: true
overview: 'Alpaca publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Market Data Streaming API, Account API, Assets API, and 13 more. Tagged areas include Market Data, Trading, Brokerage, Stocks, and Crypto.


  The Alpaca catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Alpaca''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Alpaca Markets Plans Pricing
  plan_count: 5
  slug: alpaca-markets-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Alpaca Markets Rate Limits
  slug: alpaca-markets-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Alpaca API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: alpaca-markets-asyncapi-spectral-rules
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 61.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alpaca-markets/refs/heads/main/screenshots/alpaca-markets-2026-07-25T195746.png
slug: alpaca-markets
tags:
- Market Data
- Trading
- Brokerage
- Stocks
- Crypto
- Options
- FX Trading
- Financial Data
- Streaming
- WebSocket
website: https://alpaca.markets/
---
