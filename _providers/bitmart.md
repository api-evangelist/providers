---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 6
apis:
- description: The BitMart Spot Trading REST API provides programmatic access to spot trading on the BitMart global cryptocurrency exchange. Developers can place and manage limit, market, and algorithmic orders, que
  name: BitMart Spot Trading API
  slug: spot-trading-api
- description: The BitMart Spot WebSocket API delivers real-time streaming market data and private account updates via persistent WebSocket connections. Public channels include ticker prices, order book depth, trade
  name: BitMart Spot WebSocket API
  slug: spot-websocket-api
- description: 'The BitMart Futures Trading REST API enables trading of perpetual futures contracts on the BitMart derivatives platform. Developers can submit and cancel orders including plan orders, take-profit and '
  name: BitMart Futures Trading API
  slug: futures-trading-api
- description: The BitMart Futures WebSocket API streams real-time derivatives market data and account updates through persistent WebSocket connections. Public channels include depth snapshots and incremental update
  name: BitMart Futures WebSocket API
  slug: futures-websocket-api
- description: The BitMart Margin Trading API provides access to isolated margin trading functionality. Developers can submit leveraged buy and sell orders, manage isolated margin accounts, transfer assets between s
  name: BitMart Margin Trading API
  slug: margin-trading-api
- description: The BitMart Account and Wallet API provides programmatic access to funding account management, including wallet balance queries, deposit address retrieval, withdrawal application submission, and depos
  name: BitMart Account and Wallet API
  slug: account-wallet-api
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitmart-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer-pro.bitmart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-pro.bitmart.com/en/spot/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-pro.bitmart.com/en/quick/
- group: build
  title: ''
  type: SDKs
  url: https://developer-pro.bitmart.com/en/quick/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitmartexchange
- group: operate
  title: ''
  type: StatusPage
  url: https://developer-pro.bitmart.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitmart.com/about/en-US/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitmart.com/about/en-US/privacy-policy
created: '2026-06-13'
description: BitMart is a global cryptocurrency exchange providing REST and WebSocket APIs for spot trading, perpetual futures contracts, margin trading, real-time market data, and account and withdrawal management across 6 specialized API surfaces.
features:
- description: Buy and sell 1000+ cryptocurrency pairs with limit, market, and algo orders.
  name: Spot Trading
- description: Trade perpetual futures contracts with leverage on the BitMart derivatives platform.
  name: Futures Trading
- description: Trade on isolated margin with leveraged positions using borrowed assets.
  name: Margin Trading
- description: Place algorithmic orders including TWAP-style and conditional plan orders.
  name: Algo Orders
- description: Real-time market data and account event streams for spot and futures markets.
  name: WebSocket Streams
- description: Manage deposits, withdrawals, and asset transfers between accounts.
  name: Wallet Management
- description: Create and manage sub-accounts with inter-account asset transfer support.
  name: Sub-Account Management
- description: New API users receive 30-day VIP3 trial with reduced maker/taker fees.
  name: API VIP Program
finops:
- name: Bitmart Finops
  service_category: Financial Services / Trading
  slug: bitmart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitmart.png
integrations:
- description: Official BitMart Python SDK installable via pip install bitmart-python-sdk-api.
  name: Python SDK
- description: Official BitMart Node.js SDK installable via npm install @bitmartexchange/bitmart-node-sdk-api.
  name: Node.js SDK
- description: Official BitMart Go SDK available via go get github.com/bitmartexchange/bitmart-go-sdk-api.
  name: Go SDK
- description: Official BitMart Java SDK available via Maven dependency io.github.bitmartexchange:bitmart-java-sdk-api.
  name: Java SDK
- description: Official BitMart PHP SDK installable via composer require bitmartexchange/bitmart-php-sdk-api.
  name: PHP SDK
- description: Postman collection available for testing and exploring BitMart API endpoints.
  name: Postman Collection
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-13'
name: BitMart
nav: Providers
network: true
overview: 'BitMart publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Exchange, Trading, Blockchain, and Finance.


  The BitMart catalog on APIs.io includes 1 JSON-LD context.


  BitMart''s developer surface includes developer portal, documentation, getting-started guide, and 6 more developer resources.'
plans:
- name: Bitmart Plans Pricing
  plan_count: 5
  slug: bitmart-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 15
  name: Bitmart Rate Limits
  slug: bitmart-rate-limits
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 8.1
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 36.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitmart/refs/heads/main/screenshots/bitmart-2026-06-20T173312.png
security:
- kind: domain-security
  name: Bitmart Domain Security
  slug: bitmart-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitmart
tags:
- Cryptocurrency
- Exchange
- Trading
- Blockchain
- Finance
- Market Data
- Futures
use_cases:
- description: Build automated trading bots using BitMart REST and WebSocket APIs.
  name: Algorithmic Trading
- description: Track and rebalance cryptocurrency portfolios programmatically.
  name: Portfolio Management
- description: Aggregate real-time price and order book data for analytics or dashboards.
  name: Market Data Aggregation
- description: Execute leveraged perpetual futures strategies with plan orders and TP/SL.
  name: Futures Strategy Execution
- description: Exploit price differences across BitMart spot, margin, and futures markets.
  name: Arbitrage Trading
website: https://developer-pro.bitmart.com/
---
