---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Pred Agentic Access
  operation_count: 18
  slug: pred-agentic-access
  summary_line: 18 operations · 9 acting
api_count: 7
apis:
- description: 'Required headers, token refresh, and EIP-712 CreateProxy signature for login. For overview, getting started, and environment configuration, see **Overview**. ## Required headers - `Authorization: Bear'
  name: Pred Authentication API
  slug: pred-authentication-api
- description: 'Market information and discovery (public; no auth). Use this section to understand **parent_market_id** and **market_id** and to list all markets. ## What are parent_market_id and market_id? - **paren'
  name: Pred Market Discovery API
  slug: pred-market-discovery-api
- description: 'Order placement, cancellation, and management endpoints. ## EIP-712 order signature All orders must be signed using EIP-712. Format: `0x<r><s><v>` (132 hex characters), low-s normalized. **Domain (HAS'
  name: Pred Orders API
  slug: pred-orders-api
- description: '## About PRED PRED is a fully decentralized prediction market platform built on Base (Ethereum L2), enabling users to trade on real-world events with LONG and SHORT positions—similar to perpetual futu'
  name: Pred Overview API
  slug: pred-overview-api
- description: 'Portfolio, balance, positions, and open orders. **Endpoints:** - Balance: `GET /api/v1/portfolio/balance` - Positions: `GET /api/v1/portfolio/positions` - Earnings: `GET /api/v1/portfolio/earnings` - '
  name: Pred Portfolio API
  slug: pred-portfolio-api
- description: 'Safe approval endpoints for enabling trading on your proxy wallet. ## Safe approval signature — raw secp256k1 - Sign the `transactionHash` from prepare response **directly** (raw secp256k1) - **No EIP'
  name: Pred User API
  slug: pred-user-api
- description: 'PRED uses [Ably](https://ably.com/) for real-time WebSocket data. Use Ably''s token auth with `POST /api/v1/auth/ably` as your `authCallback`. ## Token auth Call `POST /api/v1/auth/ably` to get raw Abl'
  name: Pred WebSocket API
  slug: pred-websocket-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: End-to-end signed-order trading flow on the Pred prediction exchange.
  name: PRED trading workflows
  slug: pred-trading
artifact_total: 14
asyncapis:
- description: Real-time market and order data for the Pred prediction exchange, delivered over Ably WebSocket. Obtain an Ably token via POST /api/v1/auth/ably (use it as Ably authCallback). The private user channel
  name: PRED Real-Time API (Ably WebSocket)
  slug: pred-realtime-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pred-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pred-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pred-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.pred.app/
- group: docs
  title: ''
  type: Documentation
  url: https://pred-1.gitbook.io/pred-docs
- group: docs
  title: ''
  type: APIReference
  url: https://pred-1.gitbook.io/pred-docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://pred-1.gitbook.io/pred-docs/getting-started/core-concepts
- group: start
  title: ''
  type: SignUp
  url: https://pred-1.gitbook.io/pred-docs/getting-started/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://pred-1.gitbook.io/pred-docs/trading/fees
- group: company
  title: ''
  type: Blog
  url: https://game.pred.app/
- group: company
  title: ''
  type: BlogRSS
  url: https://game.pred.app/rss/
- group: operate
  title: ''
  type: Support
  url: https://pred-1.gitbook.io/pred-docs/support/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pred.app/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pred.app/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pred-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/pred-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pred-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pred-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pred-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pred-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pred-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/pred-openapi-overlay.yaml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pred-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/pred-realtime-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pred-trading.yml
- group: other
  title: ''
  type: X
  url: https://x.com/predofficial
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/3gwsAAzEsp
- group: other
  title: ''
  type: Telegram
  url: https://t.me/+eZ8oAUDwn7Q3Zjg9
created: '2026-07-17'
description: Pred (PRED) is a fully decentralized, peer-to-peer sports prediction exchange built on Base, Coinbase's Ethereum Layer 2 network. Rather than a traditional sportsbook, Pred runs a real-time central limit order book where traders take LONG (YES) and SHORT (NO) positions on sporting outcomes priced between 0.00 and 1.00 USDC, and prices emerge from live supply and demand. Users keep full self-custody of collateral through per-user Gnosis Safe proxy wallets and authorize every order with EIP-712 signatures, with on-chain settlement of USDC on Base. Winning traders are welcome with no account limits, sub-200ms order execution and spreads under 2%. Pred publishes a documented HTTP trading API (login-with-signature auth, market discovery, order placement/cancellation, portfolio) plus an Ably WebSocket stream for real-time orderbook and order events. Initial markets cover the English Premier League and NBA. The company has raised $2.5M backed by Accel, Coinbase Ventures and Reverie.
image: https://public-assets.pred.app/banners/image.png
layout: provider
mcp_servers:
- description: ''
  name: pred-mcp.yml
  slug: pred-mcpyml
modified: '2026-07-20'
name: Pred
nav: Providers
network: true
overview: 'Pred publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Market Discovery API, Orders API, and 4 more. Tagged areas include Company, Fintech, Prediction Markets, Sports, and Trading.


  The Pred catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pred''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, and 22 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 46.0
  delta: -2.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 65.6
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pred Authentication
  slug: pred-authentication
  summary_line: http/apiKey/signature · 4 schemes
- kind: domain-security
  name: Pred Domain Security
  slug: pred-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pred
tags:
- Company
- Fintech
- Prediction Markets
- Sports
- Trading
- Exchange
- Web3
- Blockchain
- Base
- USDC
website: https://www.pred.app/
---
