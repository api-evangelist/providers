---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Lbank Agentic Access
  operation_count: 19
  slug: lbank-agentic-access
  summary_line: 19 operations · 11 acting
api_count: 6
apis:
- description: Real-time WebSocket API for streaming live market data from LBank. Clients can subscribe to K-line (candlestick) data across multiple timeframes (1-minute to monthly), order book depth updates at conf
  name: LBank WebSocket Market Data API
  slug: websocket-market-api
- description: Authenticated WebSocket API for receiving real-time account balance and order status updates from LBank. Clients can subscribe to asset balance change notifications and live order execution updates in
  name: LBank WebSocket Account and Order API
  slug: websocket-account-order-api
- description: Account balance and transaction history
  name: LBank Account API
  slug: lbank-account-api
- description: Public market data endpoints for ticker, depth, trades, and K-line data
  name: LBank Market Data API
  slug: lbank-market-data-api
- description: Order placement, cancellation, and query
  name: LBank Orders API
  slug: lbank-orders-api
- description: Deposit and withdrawal management endpoints
  name: LBank Wallet API
  slug: lbank-wallet-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lbank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lbank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lbank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lbank.com
- group: start
  title: ''
  type: Portal
  url: https://www.lbank.com/en-US/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lbank.com/en-US/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LBank-exchange
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/LBank-exchange/lbank-official-api-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lbank.com/en-US/agreement/
- group: commercial
  title: ''
  type: Plans
  url: plans/lbank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lbank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lbank-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/lbank-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lbank-vocabulary.json
created: '2026-06-13'
description: LBank is a global cryptocurrency exchange providing REST and WebSocket APIs for spot trading, ETF/leveraged token products, market data, order management, account information, and wallet operations. The platform supports multiple signature schemes (RSA and HmacSHA256) and offers public market data endpoints alongside authenticated trading and account management endpoints.
examples:
- key_count: 6
  name: Create Order Request
  slug: create-order-request
- key_count: 2
  name: Create Order Response
  slug: create-order-response
- key_count: 2
  name: Get Depth Response
  slug: get-depth-response
- key_count: 2
  name: Get Ticker Response
  slug: get-ticker-response
features:
- description: Place and manage limit, market, IOC, FOK, and maker-only orders across 500+ trading pairs.
  name: Spot Trading
- description: Access real-time ticker, depth, K-line, and trade history for all listed pairs.
  name: Market Data
- description: Query 24-hour ticker data for leveraged token products via dedicated ETF endpoints.
  name: ETF/Leveraged Tokens
- description: Subscribe to live K-line, depth, trade, and ticker streams with sub-second latency.
  name: WebSocket Streams
- description: Receive real-time push notifications for order fills and account balance changes.
  name: Account and Order Streaming
- description: Manage multi-chain deposits and withdrawals with fee queries and history retrieval.
  name: Wallet Management
- description: Supports both RSA asymmetric and HmacSHA256 symmetric signing for API requests.
  name: RSA and HMAC Authentication
- description: Three interchangeable REST base URLs for redundancy and regional access.
  name: Multiple Base URLs
finops:
- name: Lbank Finops
  service_category: Financial Services / Trading
  slug: lbank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lbank.png
json_schemas:
- name: LBank Market Ticker
  property_count: 3
  slug: lbank-market-ticker
- name: LBank Order
  property_count: 9
  slug: lbank-order
jsonld:
- class_count: 21
  name: Lbank Context
  property_count: 0
  slug: lbank-context
layout: provider
modified: '2026-06-13'
name: LBank
nav: Providers
network: true
overview: 'LBank publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Market Data API, Orders API, and 1 more. Tagged areas include Cryptocurrency, Exchange, Trading, Market Data, and Finance.


  The LBank catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LBank''s developer surface includes authentication, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Lbank Plans Pricing
  plan_count: 3
  slug: lbank-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Lbank Rate Limits
  slug: lbank-rate-limits
rules:
- name: LBank API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lbank-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.4
    developer_ergonomics: 28.3
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 54.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lbank/refs/heads/main/screenshots/lbank-2026-06-20T184341.png
security:
- kind: authentication
  name: Lbank Authentication
  slug: lbank-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lbank Domain Security
  slug: lbank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lbank
tags:
- Cryptocurrency
- Exchange
- Trading
- Market Data
- Finance
- Blockchain
use_cases:
- description: Build automated trading bots using authenticated REST and WebSocket APIs.
  name: Algorithmic Trading
- description: Aggregate real-time pricing and order book data across LBank trading pairs.
  name: Market Data Aggregation
- description: Monitor account balances and order history programmatically.
  name: Portfolio Tracking
- description: Exploit price discrepancies using real-time WebSocket streams and fast REST order placement.
  name: Arbitrage
- description: Integrate LBank liquidity into multi-exchange trading platforms using the CCXT library.
  name: Exchange Integration
website: https://www.lbank.com
---
