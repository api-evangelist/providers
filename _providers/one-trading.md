---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Real-time WebSocket API for market data (order book, price ticks, book ticker) and, after authenticating, private trading events (order lifecycle, trades, settlement, funding payments, balance adjustm
  name: One Trading WebSocket Streams API
  slug: one-trading-websocket-streams-api
- description: Subaccount balance transfers
  name: One Trading Funding API
  slug: one-trading-funding-api
- description: Futures positions, funding and portfolio endpoints
  name: One Trading Futures API
  slug: one-trading-futures-api
- description: Public market-data endpoints (no authentication)
  name: One Trading Public API
  slug: one-trading-public-api
- description: Account order and trade endpoints (Bearer token, TRADE/READ scope)
  name: One Trading Trading API
  slug: one-trading-trading-api
artifact_total: 9
asyncapis:
- description: Real-time WebSocket (WSS) API for the One Trading exchange. Clients receive market data feeds (order book, price ticks, book ticker) and, after authenticating, private trading event streams (order lif
  name: One Trading WebSocket Streams API
  slug: one-trading-streams-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/one-trading-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://onetrading.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onetrading.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.onetrading.com/rest/public/currencies
- group: start
  title: ''
  type: GettingStarted
  url: https://support.onetrading.com/hc/en-gb/articles/16357722538129-What-should-I-know-about-One-Trading-API
- group: operate
  title: ''
  type: Support
  url: https://support.onetrading.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://onetrading.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/one-trading
- group: commercial
  title: ''
  type: Pricing
  url: https://onetrading.com/fees
- group: start
  title: ''
  type: Login
  url: https://account.onetrading.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onetrading.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onetrading.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/one-trading-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/one-trading-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/one-trading-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/one-trading-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/one-trading-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/one-trading-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/one-trading-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/one-trading-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/one-trading-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/one-trading-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/one-trading-streams-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/one-trading-streams-asyncapi.yml
created: '2026-07-17'
description: One Trading (One Trading Exchange B.V.) is an EU-regulated cryptocurrency and derivatives exchange for retail and institutional traders, positioning itself as "the world's fastest exchange." It offers spot crypto plus crypto futures (up to 10x leverage), index futures and 24/7 equity futures. Its public "Fast API" provides REST market-data and trading endpoints (currencies, instruments, order book, candlesticks, ticker, fees, funding rates, orders, trades, futures positions and subaccount transfers) at https://api.onetrading.com/fast, plus a real-time WebSocket streams API at wss://streams.fast.onetrading.com. Formerly operated as Bitpanda Pro. This profile was surfaced as a Speedinvest portfolio company and enriched by the API Evangelist pipeline from the provider's public documentation and live endpoints.
image: https://framerusercontent.com/images/m2JxgHpA4PAHjVJIacTjS6wnvRY.png
layout: provider
mcp_servers:
- description: ''
  name: one-trading-mcp.yml
  slug: one-trading-mcpyml
modified: '2026-07-20'
name: One Trading
nav: Providers
network: true
overview: 'One Trading publishes 5 APIs on the [APIs.io](https://apis.io/) network, including WebSocket Streams API, Funding API, Futures API, and 2 more. Tagged areas include Company, Cryptocurrency, Crypto Exchange, Trading, and Derivatives.


  The One Trading catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  One Trading''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 18 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 43.4
  delta: -5.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.8
    developer_ergonomics: 47.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: One Trading Authentication
  slug: one-trading-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: One Trading Domain Security
  slug: one-trading-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: one-trading
tags:
- Company
- Cryptocurrency
- Crypto Exchange
- Trading
- Derivatives
- Futures
- Financial Services
- Market Data
- WebSocket
- Fintech
website: https://onetrading.com
---
