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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Bearer-auth REST API and multiplexed WebSocket streaming surface for the Sequence Markets trading OS — credentials & wallets, market data, orders & execution graphs, positions & balances, prediction m
  name: Sequence Markets Trading API
  slug: sequence-markets-trading-api
artifact_total: 5
asyncapis:
- description: Multiplexed WebSocket streaming surface for the Sequence Markets trading OS, generated faithfully from the documented channel catalog at docs.sequencemkts.com/api/streaming. Not an official provider-p
  name: Sequence Markets Streaming API
  slug: sequence-markets-streaming-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequence-markets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sequencemkts.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sequencemkts.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sequencemkts.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sequencemkts.com/api/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sequencemkts.com/quick-start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bai-Funds
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sequencemkts.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sequencemkts.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://sequencemkts.com/signup
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequence-markets-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sequence-markets-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sequence-markets-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/sequence-markets-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sequence-markets-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sequence-markets-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sequence-markets-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/sequence-markets-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sequence-markets-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sequence-markets-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sequence-markets-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sequence-markets-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sequence-markets-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sequence-markets-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sequence-markets-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sequence-markets-streaming-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sequence-markets-streaming-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Sequence Markets is a Y Combinator (Winter 2026) trading operating system for institutional crypto that provides unified execution infrastructure across 12 fragmented digital-asset venues — centralized exchanges (Coinbase, Binance, Kraken, OKX, Bybit, Bitget, Crypto.com, Hyperliquid), DeFi, and prediction markets (Kalshi, Polymarket). It packages one market view into a single trade via a smart order router (SOR), execution graphs, and WASM-compiled algo strategies deployed to multi-region low-latency edges. Developers access it through a Bearer-auth REST API and multiplexed WebSocket streams, a Python SDK, a Rust SDK, an Algo SDK, a `sequence` CLI, and an MCP interface for human, algorithmic, and agent workflows, with a full paper-trading sandbox, smart order routing, and transaction-cost analytics (TCA).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sequence-markets.png
layout: provider
mcp_servers:
- description: ''
  name: sequence-markets-mcp.yml
  slug: sequence-markets-mcpyml
modified: '2026-07-21'
name: Sequence Markets
nav: Providers
network: true
overview: 'Sequence Markets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading, Cryptocurrency, Digital Assets, and Execution.


  The Sequence Markets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sequence Markets'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, sandbox, and 21 more developer resources.'
random_paper: 61
score:
  band: developing
  composite: 43.9
  delta: 2.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 41.8
  provenance:
    conformance: derived
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
  trend: flat
security:
- kind: authentication
  name: Sequence Markets Authentication
  slug: sequence-markets-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Sequence Markets Domain Security
  slug: sequence-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sequence-markets
tags:
- Company
- Trading
- Cryptocurrency
- Digital Assets
- Execution
- Smart Order Routing
- Prediction Markets
- Algorithmic Trading
- DeFi
- Market Data
- FinTech
- Developer Tools
website: https://sequencemkts.com/
---
