---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Korbit Agentic Access
  operation_count: 34
  slug: korbit-agentic-access
  summary_line: 34 operations · 7 acting
api_count: 1
apis:
- baseURL: wss://ws-api.korbit.co.kr/v2/public
  baseurl_source: declared
  description: WebSocket streaming API for the Korbit exchange. Public channels stream ticker, orderbook and trade market data; private channels stream the authenticated account's order, trade and balance changes. P
  name: Korbit Open API v2 WebSocket
  slug: korbit-open-api-v2-websocket
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Asset API from Korbit — 1 operation(s) for asset.
  name: Korbit Asset API
  slug: korbit-asset-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Deposit (Crypto) API from Korbit — 3 operation(s) for deposit (crypto).
  name: Korbit Deposit (Crypto) API
  slug: korbit-deposit-crypto-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Deposit/Withdrawal (KRW) API from Korbit — 4 operation(s) for deposit/withdrawal (krw).
  name: Korbit Deposit/Withdrawal (KRW) API
  slug: korbit-deposit-withdrawal-krw-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Other API from Korbit — 8 operation(s) for other.
  name: Korbit Other API
  slug: korbit-other-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Quotation API from Korbit — 6 operation(s) for quotation.
  name: Korbit Quotation API
  slug: korbit-quotation-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Trading API from Korbit — 4 operation(s) for trading.
  name: Korbit Trading API
  slug: korbit-trading-api
- baseURL: https://api.korbit.co.kr
  baseurl_source: declared
  description: The Withdrawal (Crypto) API from Korbit — 3 operation(s) for withdrawal (crypto).
  name: Korbit Withdrawal (Crypto) API
  slug: korbit-withdrawal-crypto-api
artifact_total: 26
asyncapis:
- description: WebSocket streaming API for the Korbit cryptocurrency exchange. Public channels stream market data; private channels stream the authenticated account's order, trade, and balance changes. Subscribe wit
  name: Korbit Open API v2 WebSocket
  slug: korbit-websocket-asyncapi
collections:
- collection_type: open
  name: Korbit Open API v2 Asset API
  slug: open-korbit-asset-api
- collection_type: open
  name: Korbit Open API v2 Asset Deposit (Crypto) API
  slug: open-korbit-deposit-crypto-api
- collection_type: open
  name: Korbit Open API v2 Asset Deposit/Withdrawal (KRW) API
  slug: open-korbit-deposit-withdrawal-krw-api
- collection_type: open
  name: Korbit Open API v2 Asset Other API
  slug: open-korbit-other-api
- collection_type: open
  name: Korbit Open API v2 Asset Quotation API
  slug: open-korbit-quotation-api
- collection_type: open
  name: Korbit Open API v2 Asset Trading API
  slug: open-korbit-trading-api
- collection_type: open
  name: Korbit Open API v2 Asset Withdrawal (Crypto) API
  slug: open-korbit-withdrawal-crypto-api
common:
- group: other
  href: https://artifacts.apis.io/korbit/capabilities/korbit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/korbit-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/korbit/security/korbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/korbit-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/korbit/agentic-access/korbit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/korbit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/korbit/authentication/korbit-authentication.yml
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
  href: https://artifacts.apis.io/korbit/llms/korbit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/korbit-llms.txt
- group: docs
  href: https://artifacts.apis.io/korbit/openapi/_original/korbit-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/korbit-openapi.yml
- group: docs
  href: https://artifacts.apis.io/korbit/asyncapi/korbit-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/korbit-websocket-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/korbit/asyncapi/korbit-websocket-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/korbit-websocket-asyncapi.yml
- group: build
  href: https://artifacts.apis.io/korbit/packages/korbit-packages.yml
  title: ''
  type: Packages
  url: packages/korbit-packages.yml
- group: build
  href: https://artifacts.apis.io/korbit/packages/korbit-packages.yml
  title: ''
  type: SDKs
  url: packages/korbit-packages.yml
- group: build
  href: https://artifacts.apis.io/korbit/cli/korbit-cli.yml
  title: ''
  type: CLI
  url: cli/korbit-cli.yml
- group: agent
  href: https://artifacts.apis.io/korbit/mcp/korbit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/korbit-mcp.yml
- group: agent
  href: https://artifacts.apis.io/korbit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/korbit/sandbox/korbit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/korbit-sandbox.yml
- group: design
  href: https://artifacts.apis.io/korbit/conventions/korbit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/korbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/korbit/conventions/korbit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/korbit-conventions.yml
- group: design
  href: https://artifacts.apis.io/korbit/errors/korbit-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/korbit-error-codes.yml
- group: operate
  href: https://artifacts.apis.io/korbit/rate-limits/korbit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/korbit-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/korbit/lifecycle/korbit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/korbit-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/korbit/conformance/korbit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/korbit-conformance.yml
- group: design
  href: https://artifacts.apis.io/korbit/data-model/korbit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/korbit-data-model.yml
- group: agent
  href: https://artifacts.apis.io/korbit/well-known/korbit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/korbit-well-known.yml
- group: other
  href: https://artifacts.apis.io/korbit/overlays/korbit-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/korbit-openapi-overlay.yaml
created: '2026-07-17'
description: 'Korbit is South Korea''s first cryptocurrency exchange, founded in 2013 and headquartered in Seoul, offering KRW-denominated spot trading of bitcoin, ether and other digital assets to Korean retail and institutional customers. Korbit publishes the Korbit Open API v2, a REST and WebSocket interface covering market data (tickers, orderbook, trades, candlesticks, tick-size policy), order placement and cancellation, order and trade history, balances, cryptocurrency deposit-address management and withdrawals, and KRW deposit/withdrawal push notifications. Authentication is by API key (X-KAPI-KEY) with per-request HMAC-SHA256 or ED25519 signatures, granular key permissions and optional IP allowlisting. Korbit is unusually agent-forward for an exchange: it ships an official Go CLI with a bundled MCP server and Agent Skill, a documented llms.txt, and a downloadable local sandbox that mocks the full REST and WebSocket surface for no-risk development.'
image: https://www.korbit.co.kr/apple-touch-icon.png
layout: provider
mcp_servers:
- description: Korbit ships an official MCP server bundled inside the korbit-cli binary. It is a local stdio server (not a hosted/remote endpoint) that exposes every Korbit Open API v2 endpoint as an MCP tool, runni
  name: Korbit MCP Server
  slug: korbit
modified: '2026-07-19'
name: Korbit
nav: Providers
network: true
overview: 'Korbit publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Open API v2 WebSocket, Asset API, Deposit (Crypto) API, and 5 more. Tagged areas include Company, Cryptocurrency, Cryptocurrency Exchange, Digital Assets, and Trading.


  The Korbit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Korbit''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, CLI, and 24 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 5
  name: Korbit Rate Limits
  slug: korbit-rate-limits
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 60.6
    developer_ergonomics: 75.6
    discoverability: 65.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 45.0
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
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/korbit/korbit-2026-07-25T224221.png
security:
- kind: authentication
  name: Korbit Authentication
  slug: korbit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Korbit Domain Security
  slug: korbit-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: Fund a Korbit account and withdraw
  slug: korbit-fund-and-withdraw
- name: Read Korbit market data
  slug: korbit-market-data
- name: Monitor Korbit orders, fills and balances
  slug: korbit-monitor-orders-and-fills
- name: Place a Korbit order safely
  slug: korbit-place-order-safely
- name: Stream Korbit market and account state over WebSocket
  slug: korbit-stream-account-state
slug: korbit
tags:
- Company
- Cryptocurrency
- Cryptocurrency Exchange
- Digital Assets
- Trading
- Market Data
- Financial Services
- WebSocket
- South Korea
- Blockchain
- Real-Time
website: https://www.korbit.co.kr/
---
