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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 7
apis:
- description: REST API for spot trading on Bitget including market data, order management, account queries, wallet operations, and sub-account management.
  name: Bitget Spot Trading API
  slug: bitget-spot-trading-api
- description: REST API for USDT-M, USDC-M, and Coin-M perpetual futures contracts including market data, position management, order execution, trigger orders, and VIP fee rate queries.
  name: Bitget Futures Trading API
  slug: bitget-futures-trading-api
- description: REST API for copy trading functionality covering futures copy trade and spot copy trade, including trader order tracking and profit summary endpoints for both leaders and followers.
  name: Bitget Copy Trading API
  slug: bitget-copy-trading-api
- description: REST API for non-disclosed brokers to build independent trading platforms on top of Bitget infrastructure, including sub-account creation, API key management, commission tracking, and permission contr
  name: Bitget Broker API
  slug: bitget-broker-api
- description: Real-time WebSocket API providing public and private channels for market data (tickers, candles, order book depth, trades) and private account events (orders, positions, balances) for spot and futures
  name: Bitget WebSocket API
  slug: bitget-websocket-api
- description: REST API for Bitget Earn products including staking, savings, and other yield-generating products available on the platform.
  name: Bitget Earn API
  slug: bitget-earn-api
- description: REST API for cross and isolated margin trading on Bitget, enabling leveraged spot trading with account management, borrowing, and order execution endpoints.
  name: Bitget Margin Trading API
  slug: bitget-margin-trading-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitget-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: https://www.bitget.com/api-doc/common/intro
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/rate-limits.md
- group: commercial
  title: ''
  type: Plans
  url: /plans/plans.md
- group: commercial
  title: ''
  type: FinOps
  url: /finops/finops.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bitget.com/api-doc/common/changelog
- group: operate
  title: ''
  type: Support
  url: https://www.bitget.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bitget.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bitget.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bitget.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bitget.com/api-doc/common/intro
- group: build
  title: ''
  type: SDKs
  url: https://github.com/BitgetLimited
- group: other
  title: ''
  type: Telegram
  url: https://t.me/bitgetOpenapi
created: '2026-06-13'
description: Bitget is a cryptocurrency exchange and copy trading platform offering REST and WebSocket APIs for spot trading, futures (USDT-M, USDC-M, and Coin-M perpetual contracts), margin trading, copy trading, broker services, and earn products. Developers can access real-time market data, execute trades, manage accounts and sub-accounts, and integrate copy trading leader and follower workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitget.png
layout: provider
modified: '2026-06-13'
name: Bitget
nav: Providers
network: true
overview: 'Bitget publishes 1 API on the [APIs.io](https://apis.io/) network: Spot Trading API. Tagged areas include Cryptocurrency, Exchange, Spot Trading, Futures, and Perpetual Contracts.


  Bitget''s developer surface includes authentication, changelog, support, getting-started guide, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 23.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitget/refs/heads/main/screenshots/bitget-2026-06-20T173307.png
security:
- kind: domain-security
  name: Bitget Domain Security
  slug: bitget-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitget
tags:
- Cryptocurrency
- Exchange
- Spot Trading
- Futures
- Perpetual Contracts
- Copy Trading
- WebSocket
- Finance
---
