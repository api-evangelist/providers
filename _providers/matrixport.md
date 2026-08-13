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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Matrixport Agentic Access
  operation_count: 39
  slug: matrixport-agentic-access
  summary_line: 39 operations · 10 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The Account API from Matrixport — 9 operation(s) for account.
  name: Matrixport Account API
  slug: matrixport-account-api
- description: The Batch Orders API from Matrixport — 2 operation(s) for batch orders.
  name: Matrixport Batch Orders API
  slug: matrixport-batch-orders-api
- description: The Block Trade API from Matrixport — 2 operation(s) for block trade.
  name: Matrixport Block Trade API
  slug: matrixport-block-trade-api
- description: The Market API from Matrixport — 11 operation(s) for market.
  name: Matrixport Market API
  slug: matrixport-market-api
- description: The Order API from Matrixport — 8 operation(s) for order.
  name: Matrixport Order API
  slug: matrixport-order-api
- description: The System API from Matrixport — 3 operation(s) for system.
  name: Matrixport System API
  slug: matrixport-system-api
- description: The WebSocket API from Matrixport — 1 operation(s) for websocket.
  name: Matrixport WebSocket API
  slug: matrixport-websocket-api
artifact_total: 12
asyncapis:
- description: 'Public and private WebSocket streaming for the bit.com exchange. Channel names are taken verbatim from the official bitcom-python-umapi SDK (bit_ws_public.py / bit_ws_private.py). Clients connect and '
  name: bit.com (Matrixport) WebSocket streaming API
  slug: matrixport-websocket
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/matrixport-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.bit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bit.com/docs/en-us/spot.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.bit.com/docs/en-us/futures.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitcom-exchange
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bit.com/docs/en-us/change_log.html
- group: build
  title: ''
  type: Packages
  url: packages/matrixport-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/matrixport-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/matrixport-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/matrixport-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/matrixport-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/matrixport-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/matrixport-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matrixport-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/matrixport-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/matrixport-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/matrixport-websocket.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/matrixport-websocket.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/matrixport-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/matrixport-data-model.yml
created: '2026-07-17'
description: Matrixport is a digital-asset financial services firm whose trading and derivatives venue, bit.com, exposes a public v1 REST and WebSocket API for spot, USD-margined (USD-M) and coin-margined (COIN-M) futures, perpetual swaps, and options, plus Paradigm-style block trades. The API authenticates with an access key and HMAC-SHA256 request signing, and covers market data (index, instruments, tickers, orderbooks, klines, funding), account, position, and full order-management (new/amend/cancel/close, batch orders, stop orders, MMP). First-party SDKs are published for Go, Python, and Java. Added to the API Evangelist network as a crypto-finance provider and enriched from its public developer surface and official SDK repositories.
image: https://www.bit.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: matrixport-mcp.yml
  slug: matrixport-mcpyml
modified: '2026-07-20'
name: Matrixport
nav: Providers
network: true
overview: 'Matrixport publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Batch Orders API, Block Trade API, and 4 more. Tagged areas include Company, Crypto Finance, Cryptocurrency Exchange, Trading, and Derivatives.


  The Matrixport catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Matrixport''s developer surface includes documentation, API reference, changelog, authentication, and 17 more developer resources.'
random_paper: 34
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.8
    developer_ergonomics: 36.4
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 34.2
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matrixport/refs/heads/main/screenshots/matrixport-2026-07-25T230424.png
security:
- kind: authentication
  name: Matrixport Authentication
  slug: matrixport-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Matrixport Domain Security
  slug: matrixport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matrixport
tags:
- Company
- Crypto Finance
- Cryptocurrency Exchange
- Trading
- Derivatives
- Options
- Futures
- Perpetuals
- WebSocket
- REST API
website: https://www.bit.com
---
