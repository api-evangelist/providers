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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Order book, tickers, mark prices, and order updates
  name: DerivaDEX Market API
  slug: derivadex-market-api
- description: Protocol aggregations, supply, positions, strategies, fees, and trader data
  name: DerivaDEX Stats API
  slug: derivadex-stats-api
- description: Health, server time, and exchange configuration
  name: DerivaDEX System API
  slug: derivadex-system-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/derivadex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://derivadex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.derivadex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.derivadex.io/
- group: docs
  title: ''
  type: APIReference
  url: https://exchange.derivadex.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.derivadex.io/introduction/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/derivadex
- group: operate
  title: ''
  type: StatusPage
  url: https://7w33wrnn4p7q.statuspage.io/
- group: start
  title: ''
  type: SignUp
  url: https://exchange.derivadex.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/derivadex-exchange-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/derivadex-exchange-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/derivadex-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/derivadex-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/derivadex-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/derivadex-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/derivadex-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/derivadex-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/derivadex-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/derivadex-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/derivadex-llms.txt
created: '2026-07-17'
description: DerivaDEX is a decentralized cryptocurrency derivatives exchange for perpetual swaps, governed from day one by the DerivaDAO and its DDX token. It aims to pair the performance and usability of a centralized exchange with the custody and transparency of DeFi, using on-chain settlement, an insurance fund, trade mining, and a checkpointed price feed. DerivaDEX publishes a public REST API (exchange system and market-data endpoints plus protocol/stats aggregations) documented at docs.derivadex.io and exchange.derivadex.com/api-docs, an Authenticated REST API and a Realtime API, an on-chain explorer, and a governance app. Mainnet runs as a limited-access pilot on Ethereum with a public Sepolia testnet, and the exchange is licensed by the Bermuda Monetary Authority. Backed by Polychain Capital.
image: https://exchange.derivadex.com/icons/512.png
layout: provider
mcp_servers:
- description: ''
  name: derivadex-mcp.yml
  slug: derivadex-mcpyml
modified: '2026-07-18'
name: DerivaDEX
nav: Providers
network: true
overview: 'DerivaDEX publishes 3 APIs on the [APIs.io](https://apis.io/) network: Market API, Stats API, and System API. Tagged areas include Company, Defi Derivatives, Cryptocurrency, Derivatives, and Perpetual Swaps.


  DerivaDEX''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, sandbox, and 15 more developer resources.'
random_paper: 28
score:
  band: thin
  composite: 39.0
  delta: -0.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 54.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 39.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/derivadex/refs/heads/main/screenshots/derivadex-2026-07-25T211741.png
security:
- kind: authentication
  name: Derivadex Authentication
  slug: derivadex-authentication
  summary_line: none/wallet-signature · 2 schemes
- kind: domain-security
  name: Derivadex Domain Security
  slug: derivadex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: derivadex
tags:
- Company
- Defi Derivatives
- Cryptocurrency
- Derivatives
- Perpetual Swaps
- Decentralized Exchange
- Trading
- Blockchain
- Market Data
- DeFi
website: https://derivadex.com
---
