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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Hibachi Agentic Access
  operation_count: 27
  slug: hibachi-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 1
apis:
- description: 'Authenticated capital movement: balance, deposit info, withdraw, transfer'
  name: Hibachi Capital API
  slug: hibachi-capital-api
- description: 'Public market data: contracts, prices, stats, trades, klines, orderbook, funding rates'
  name: Hibachi Market API
  slug: hibachi-market-api
- description: 'Authenticated trading: orders, positions, account info, settlements, leverage'
  name: Hibachi Trade API
  slug: hibachi-trade-api
artifact_total: 12
asyncapis:
- description: Hibachi exposes a WebSocket API alongside its REST API for lower-latency access to real-time trading and market data. Public market streams (/ws/market) require no API key; account and trading streams
  name: Hibachi WebSocket API
  slug: hibachi-ws-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hibachi Capital API
  slug: open-hibachi-capital-api
- collection_type: open
  name: Hibachi Capital Market API
  slug: open-hibachi-market-api
- collection_type: open
  name: Hibachi Capital Trade API
  slug: open-hibachi-trade-api
common:
- group: company
  title: ''
  type: Website
  url: https://hibachi.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.hibachi.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hibachi.xyz/hibachi-docs/api-and-developer-tools.md
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.hibachi.xyz/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hibachi.xyz/hibachi-docs/getting-started.md
- group: company
  title: ''
  type: Blog
  url: https://blog.hibachi.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hibachi-xyz
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.hibachi.xyz/hibachi-docs/trading/fees.md
- group: start
  title: ''
  type: SignUp
  url: https://hibachi.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hibachi.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hibachi.xyz/privacy
- group: build
  title: ''
  type: Postman
  url: https://api-doc.hibachi.xyz/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/hibachi-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hibachi-ws-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hibachi-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/hibachi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hibachi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hibachi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hibachi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hibachi-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/hibachi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hibachi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hibachi-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hibachi-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hibachi-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hibachi-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hibachi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hibachi-domain-security.yml
created: '2026-07-17'
description: Hibachi is a stablecoin-native, privacy-first decentralized exchange for perpetual futures and FX trading. Built by contributors from Citadel, Tower Research, IMC, Meta, Google and Amazon, it pairs a low-latency central-limit-orderbook trading engine with a zk-verified settlement layer, so collateral only moves on-chain when validated by a zero-knowledge proof. Hibachi exposes a public REST and WebSocket API across two hosts (api.hibachi.xyz for account, trading and capital operations; data-api.hibachi.xyz for market data), an official Python SDK, a TypeScript example integration, and a CCXT integration. Authentication uses an API key in the Authorization header, and order, withdraw and transfer operations additionally require an ECDSA or HMAC request signature. It is backed by Electric Capital.
image: https://hibachi.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Hibachi MCP Server
  slug: hibachi-mcp-server
modified: '2026-07-19'
name: Hibachi
nav: Providers
network: true
overview: 'Hibachi publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capital API, Market API, and Trade API. Tagged areas include Company, Defi, Cryptocurrency, Exchange, and Perpetual Futures.


  The Hibachi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hibachi''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 25.0
    developer_ergonomics: 67.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hibachi/refs/heads/main/screenshots/hibachi-2026-07-25T221135.png
security:
- kind: authentication
  name: Hibachi Authentication
  slug: hibachi-authentication
  summary_line: apiKey/signature · 1 scheme
- kind: domain-security
  name: Hibachi Domain Security
  slug: hibachi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hibachi
tags:
- Company
- Defi
- Cryptocurrency
- Exchange
- Perpetual Futures
- Trading
- Derivatives
- Stablecoin
- WebSocket
- Blockchain
website: https://hibachi.xyz/
---
