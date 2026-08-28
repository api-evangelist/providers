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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: River Markets Agentic Access
  operation_count: 48
  slug: river-markets-agentic-access
  summary_line: 48 operations · 24 acting
api_count: 13
apis:
- description: The balance API from River Markets — 1 operation(s) for balance.
  name: River Markets balance API
  slug: river-markets-balance-api
- description: 'Manage complex orders: conditional orders (take-profit and stop-loss), TWAP, and other advanced order types.'
  name: River Markets complex-orders API
  slug: river-markets-complex-orders-api
- description: The fair-values API from River Markets — 2 operation(s) for fair-values.
  name: River Markets fair-values API
  slug: river-markets-fair-values-api
- description: Retrieve trade execution history and fill details.
  name: River Markets fills API
  slug: river-markets-fills-api
- description: The generic-assets API from River Markets — 3 operation(s) for generic-assets.
  name: River Markets generic-assets API
  slug: river-markets-generic-assets-api
- description: Search and discover prediction markets across Kalshi and Polymarket.
  name: River Markets markets API
  slug: river-markets-markets-api
- description: The orderbooks API from River Markets — 2 operation(s) for orderbooks.
  name: River Markets orderbooks API
  slug: river-markets-orderbooks-api
- description: Place and manage orders on prediction market exchanges.
  name: River Markets orders API
  slug: river-markets-orders-api
- description: View current portfolio positions across all connected exchanges.
  name: River Markets positions API
  slug: river-markets-positions-api
- description: Get historical price data and candlesticks from exchanges.
  name: River Markets prices API
  slug: river-markets-prices-api
- description: Manage trading subaccounts. Each subaccount can have its own exchange credentials and positions.
  name: River Markets subaccounts API
  slug: river-markets-subaccounts-api
- description: Recent trades for a market. Pairs with the /v1/ws/tradeprints WebSocket for live updates.
  name: River Markets tradeprints API
  slug: river-markets-tradeprints-api
- description: The watchlists API from River Markets — 4 operation(s) for watchlists.
  name: River Markets watchlists API
  slug: river-markets-watchlists-api
artifact_total: 32
asyncapis:
- description: 'Real-time WebSocket streams over wss://api.rivermarkets.com. Client frames are JSON text; server frames are orjson-serialized UTF-8 bytes. Handshake auth uses the Ed25519 signed-request flow moved to '
  name: River Markets Streaming API
  slug: river-markets-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: River Markets balance API
  slug: open-river-markets-balance-api
- collection_type: open
  name: River Markets balance complex-orders API
  slug: open-river-markets-complex-orders-api
- collection_type: open
  name: River Markets balance fair-values API
  slug: open-river-markets-fair-values-api
- collection_type: open
  name: River Markets balance fills API
  slug: open-river-markets-fills-api
- collection_type: open
  name: River Markets balance generic-assets API
  slug: open-river-markets-generic-assets-api
- collection_type: open
  name: River balance markets API
  slug: open-river-markets-markets-api
- collection_type: open
  name: River Markets balance orderbooks API
  slug: open-river-markets-orderbooks-api
- collection_type: open
  name: River Markets balance orders API
  slug: open-river-markets-orders-api
- collection_type: open
  name: River Markets balance positions API
  slug: open-river-markets-positions-api
- collection_type: open
  name: River Markets balance prices API
  slug: open-river-markets-prices-api
- collection_type: open
  name: River Markets balance subaccounts API
  slug: open-river-markets-subaccounts-api
- collection_type: open
  name: River Markets balance tradeprints API
  slug: open-river-markets-tradeprints-api
- collection_type: open
  name: River Markets balance watchlists API
  slug: open-river-markets-watchlists-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rivermarkets.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rivermarkets.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rivermarkets.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rivermarkets.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.rivermarkets.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rivermarkets
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/river-markets-openapi-original.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/river-markets-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/river-markets-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/river-markets-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/river-markets-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/river-markets-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/river-markets-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/river-markets-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/river-markets-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/river-markets-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/river-markets-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/river-markets-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/river-markets-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/river-markets-agentic-access.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/river-markets-streaming-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: River Markets is a unified prime brokerage for prediction markets, consolidating multiple exchanges — Kalshi, Polymarket, and Polymarket US (with Novig and Rothera planned) — behind a single account, order-management system, and REST + WebSocket API. Every contract across all venues is assigned a unified River ID, so professional and institutional traders can search markets, place and route orders (including icebergs, pegs, stop-losses, and take-profits with smart order routing), track positions and P&L across isolated subaccounts, and stream live fills, orderbooks, orders, and trade prints from one integration. Requests are Ed25519-signed so the private key never leaves the client process. Founded by ex-BlackRock and high-frequency trading quants and backed by Y Combinator (Spring 2026).
image: https://rivermarkets.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: River Markets MCP Server
  slug: river-markets-mcp-server
modified: '2026-07-21'
name: River Markets
nav: Providers
network: true
overview: 'River Markets publishes 13 APIs on the [APIs.io](https://apis.io/) network, including balance API, complex-orders API, fair-values API, and 10 more. Tagged areas include Company, Prediction Markets, Trading, Prime Brokerage, and Financial-Services.


  The River Markets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  River Markets'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 17 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 70.3
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: River Markets Authentication
  slug: river-markets-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: River Markets Domain Security
  slug: river-markets-domain-security
  summary_line: TLSv1.3 · DMARC
slug: river-markets
tags:
- Company
- Prediction Markets
- Trading
- Prime Brokerage
- Financial-Services
- Order Management
- Market Data
- WebSocket
- Fintech
website: https://docs.rivermarkets.com
---
