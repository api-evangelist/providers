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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Korbit Agentic Access
  operation_count: 34
  slug: korbit-agentic-access
  summary_line: 34 operations · 7 acting
api_count: 8
apis:
- description: WebSocket streaming API for the Korbit exchange. Public channels stream ticker, orderbook and trade market data; private channels stream the authenticated account's order, trade and balance changes. P
  name: Korbit Open API v2 WebSocket
  slug: korbit-open-api-v2-websocket
- description: The Asset API from Korbit — 1 operation(s) for asset.
  name: Korbit Asset API
  slug: korbit-asset-api
- description: The Deposit (Crypto) API from Korbit — 3 operation(s) for deposit (crypto).
  name: Korbit Deposit (Crypto) API
  slug: korbit-deposit-crypto-api
- description: The Deposit/Withdrawal (KRW) API from Korbit — 4 operation(s) for deposit/withdrawal (krw).
  name: Korbit Deposit/Withdrawal (KRW) API
  slug: korbit-deposit-withdrawal-krw-api
- description: The Other API from Korbit — 8 operation(s) for other.
  name: Korbit Other API
  slug: korbit-other-api
- description: The Quotation API from Korbit — 6 operation(s) for quotation.
  name: Korbit Quotation API
  slug: korbit-quotation-api
- description: The Trading API from Korbit — 4 operation(s) for trading.
  name: Korbit Trading API
  slug: korbit-trading-api
- description: The Withdrawal (Crypto) API from Korbit — 3 operation(s) for withdrawal (crypto).
  name: Korbit Withdrawal (Crypto) API
  slug: korbit-withdrawal-crypto-api
artifact_total: 14
asyncapis:
- description: WebSocket streaming API for the Korbit cryptocurrency exchange. Public channels stream market data; private channels stream the authenticated account's order, trade, and balance changes. Subscribe wit
  name: Korbit Open API v2 WebSocket
  slug: korbit-websocket-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/korbit-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/korbit-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/korbit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.korbit.co.kr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.korbit.co.kr
- group: docs
  title: ''
  type: Documentation
  url: https://docs.korbit.co.kr/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.korbit.co.kr/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.korbit.co.kr/llms/en/introduction.md
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/korbit_official
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/korbit-official
- group: start
  title: ''
  type: SignUp
  url: https://developers.korbit.co.kr
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/korbit-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/korbit-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/korbit-websocket-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/korbit-websocket-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/korbit-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/korbit-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/korbit-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/korbit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/korbit-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/korbit-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/korbit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/korbit-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/korbit-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/korbit-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/korbit-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/korbit-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/korbit-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/korbit-openapi-overlay.yaml
created: '2026-07-17'
description: 'Korbit is South Korea''s first cryptocurrency exchange, founded in 2013 and headquartered in Seoul, offering KRW-denominated spot trading of bitcoin, ether and other digital assets to Korean retail and institutional customers. Korbit publishes the Korbit Open API v2, a REST and WebSocket interface covering market data (tickers, orderbook, trades, candlesticks, tick-size policy), order placement and cancellation, order and trade history, balances, cryptocurrency deposit-address management and withdrawals, and KRW deposit/withdrawal push notifications. Authentication is by API key (X-KAPI-KEY) with per-request HMAC-SHA256 or ED25519 signatures, granular key permissions and optional IP allowlisting. Korbit is unusually agent-forward for an exchange: it ships an official Go CLI with a bundled MCP server and Agent Skill, a documented llms.txt, and a downloadable local sandbox that mocks the full REST and WebSocket surface for no-risk development.'
image: https://www.korbit.co.kr/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: korbit-mcp.yml
  slug: korbit-mcpyml
modified: '2026-07-19'
name: Korbit
nav: Providers
network: true
overview: 'Korbit publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Open API v2 WebSocket, Asset API, Deposit (Crypto) API, and 5 more. Tagged areas include Company, Crypto, Cryptocurrency Exchange, Digital Assets, and Trading.


  The Korbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Korbit''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, and 23 more developer resources.'
random_paper: 81
rate_limits:
- limit_count: 5
  name: Korbit Rate Limits
  slug: korbit-rate-limits
score:
  band: developing
  composite: 49.6
  delta: 3.5
  facets:
    commercial_clarity: 13.2
    contract_quality: 74.7
    developer_ergonomics: 77.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/korbit/refs/heads/main/screenshots/korbit-2026-07-25T224221.png
security:
- kind: authentication
  name: Korbit Authentication
  slug: korbit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Korbit Domain Security
  slug: korbit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: korbit
tags:
- Company
- Crypto
- Cryptocurrency Exchange
- Digital Assets
- Trading
- Market Data
- Financial Services
- WebSocket
- South Korea
- Blockchain
website: https://www.korbit.co.kr/
---
