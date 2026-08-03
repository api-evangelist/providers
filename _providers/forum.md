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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 64.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Forum Agentic Access
  operation_count: 24
  slug: forum-agentic-access
  summary_line: 24 operations · 6 acting
api_count: 9
apis:
- description: Account summary and balance
  name: Forum Account API
  slug: forum-account-api
- description: Exchange status and server time
  name: Forum Exchange API
  slug: forum-exchange-api
- description: Trade execution history
  name: Forum Fills API
  slug: forum-fills-api
- description: Funding rates and history
  name: Forum Funding API
  slug: forum-funding-api
- description: Attention index values and history
  name: Forum Indices API
  slug: forum-indices-api
- description: Order books, tickers, trades, and candles
  name: Forum Market Data API
  slug: forum-market-data-api
- description: Market listings and details
  name: Forum Markets API
  slug: forum-markets-api
- description: Order placement, cancellation, and queries
  name: Forum Orders API
  slug: forum-orders-api
- description: Open position data
  name: Forum Positions API
  slug: forum-positions-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: 'Check exchange status, list available attention-index markets, inspect one market, place a limit order (idempotent via clientOrderId), confirm the order, then read the resulting account and position. '
  name: Forum — discover a market and place an order
  slug: forum-place-order
artifact_total: 17
asyncapis:
- description: 'Real-time market data and private account updates via WebSocket. ## Connection Connect to `wss://api.forum.market/ws/v1` to establish a WebSocket connection. You must send a `subscribe` command within'
  name: Forum WebSocket Feed
  slug: forum-websocket-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.forum.market/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forum.market/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.forum.market/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.forum.market/api-reference/quick-start
- group: start
  title: ''
  type: Quickstart
  url: https://docs.forum.market/api-reference/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://app.forum.market/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://forum-legal.s3.us-east-2.amazonaws.com/terms-of-service.pdf
- group: operate
  title: ''
  type: Support
  url: https://docs.forum.market/guide/feedback
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/forum-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/forum-openapi-original.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/forum-websocket-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/forum-websocket-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/forum-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/forum-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forum-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/forum-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/forum-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/forum-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forum-conformance.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forum-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/forum-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/forum-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forum-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/forum-openapi-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/forum-place-order.yml
created: '2026-07-17'
description: 'Forum is a centralized exchange offering exposure to engagement-backed assets — "the first exchange to trade on attention." It turns online attention across social, search, and streaming data into measurable, tradable attention indices, then lists continuous perpetual-style futures contracts on top of them so participants can go long or short on cultural relevance as a new asset class. Forum (Y Combinator W26, based in New York City) exposes a full public developer surface: an OpenAPI 3.1 REST API at api.forum.market/v1 for market data, order management, positions, and account queries, and an AsyncAPI 3.0 WebSocket feed at wss://api.forum.market/ws/v1 for real-time order book, ticker, trade, index, and funding updates. Authentication is HMAC-SHA256 request signing with read/trade API-key permissions, and the docs ship an agent-native discovery surface (llms.txt, agent-card, agent-skills, and a documentation MCP server).'
image: https://mintcdn.com/forum-f20ab882/NO88uiJ9um9e-WSg/images/dark.png
layout: provider
mcp_servers:
- description: ''
  name: forum-mcp.yml
  slug: forum-mcpyml
modified: '2026-07-20'
name: Forum
nav: Providers
network: true
overview: 'Forum publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Exchange API, Fills API, and 6 more. Tagged areas include Company, Trading, Exchange, Perpetual Futures, and Market Data.


  The Forum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Forum''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, support, changelog, and 21 more developer resources.'
random_paper: 78
rate_limits:
- limit_count: 5
  name: Forum Rate Limits
  slug: forum-rate-limits
score:
  band: developing
  composite: 51.5
  delta: 3.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 75.1
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 35.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forum/refs/heads/main/screenshots/forum-2026-07-25T215019.png
security:
- kind: authentication
  name: Forum Authentication
  slug: forum-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Forum Domain Security
  slug: forum-domain-security
  summary_line: TLSv1.2 · DMARC
slug: forum
tags:
- Company
- Trading
- Exchange
- Perpetual Futures
- Market Data
- Attention Economy
- Fintech
- WebSocket
- Real Time
website: https://docs.forum.market/
---
