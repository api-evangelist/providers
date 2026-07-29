---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: CoinGecko/CMC-style aggregator market-data feed.
  name: Overlay Aggregator API
  slug: overlay-aggregator-api
- description: Price overview and OHLC chart data.
  name: Overlay Charts API
  slug: overlay-charts-api
- description: Market catalog and metadata.
  name: Overlay Markets API
  slug: overlay-markets-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://overlay.market
- group: docs
  title: ''
  type: Documentation
  url: https://docs.overlay.market/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.overlay.market/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.overlay.market/api/aggregator-market-data
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/overlay-market
- group: operate
  title: ''
  type: Support
  url: https://redrct.overlay.market/discord
- group: other
  title: ''
  type: Whitepaper
  url: https://redrct.overlay.market/whitepaper
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/overlay-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/overlay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/overlay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/overlay-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/overlay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/overlay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/overlay-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/overlay-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/overlay-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/overlay-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/overlay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/overlay-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/overlay-market.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overlay-domain-security.yml
created: '2026-07-17'
description: Overlay is a decentralized perpetual-futures protocol on BNB Smart Chain (chain id 56) that lets anyone trade and permissionlessly create markets for emerging, pre-CEX, and narrative-driven assets against any verifiable data feed. Positions are synthetic — traders trade against a protocol-managed price feed with USDT/stablecoin collateral rather than an order book — with a dynamic risk engine managing thin markets and zero liquidity requirements. Overlay exposes a public, unauthenticated market-data API (aggregator contracts, contract specs, market catalog, charts price overview), a TypeScript SDK, a GraphQL subgraph, and a provider-published Agent Skill for automated trading. Backed by Polychain.
image: https://avatars.githubusercontent.com/u/70023182?v=4
layout: provider
mcp_servers:
- description: ''
  name: overlay-mcp.yml
  slug: overlay-mcpyml
modified: '2026-07-20'
name: Overlay
nav: Providers
network: true
overview: 'Overlay publishes 3 APIs on the [APIs.io](https://apis.io/) network: Aggregator API, Charts API, and Markets API. Tagged areas include Company, Defi, DeFi, Perpetual Futures, and Derivatives.


  Overlay''s developer surface includes documentation, API reference, support, authentication, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 31.6
  delta: -4.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 39.8
    developer_ergonomics: 54.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 36.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Overlay Authentication
  slug: overlay-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Overlay Domain Security
  slug: overlay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overlay
tags:
- Company
- Defi
- DeFi
- Perpetual Futures
- Derivatives
- Trading
- Market Data
- BNB Smart Chain
- Blockchain
- Web3
website: https://overlay.market
---
