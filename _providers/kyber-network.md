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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 60.4
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: The General API from Kyber Network — 2 operation(s) for general.
  name: Kyber Network General API
  slug: kyber-network-general-api
- description: The Maker API from Kyber Network — 8 operation(s) for maker.
  name: Kyber Network Maker API
  slug: kyber-network-maker-api
- description: The Service API from Kyber Network — 3 operation(s) for service.
  name: Kyber Network Service API
  slug: kyber-network-service-api
- description: The swap API from Kyber Network — 3 operation(s) for swap.
  name: Kyber Network swap API
  slug: kyber-network-swap-api
- description: The Taker API from Kyber Network — 4 operation(s) for taker.
  name: Kyber Network Taker API
  slug: kyber-network-taker-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://kyber.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kyberswap.com/developer-guide/start-here
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kyberswap.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kyberswap.com/developer-guide/aggregator-api/aggregator-api-specification
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kyberswap.com/developer-guide/start-here
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/kyberswap
- group: company
  title: ''
  type: Blog
  url: https://blog.kyberswap.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KyberNetwork
- group: start
  title: ''
  type: SignUp
  url: https://kyberswap.com/swap
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.kyberswap.com/getting-started/fee-schedule
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/kyber-network-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kyber-network-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kyber-network-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kyber-network-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kyber-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kyber-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kyber-network-error-codes.yml
- group: build
  title: ''
  type: Packages
  url: packages/kyber-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kyber-network-packages.yml
- group: design
  title: ''
  type: Components
  url: components/kyber-network-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kyber-network-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kyber-network-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kyber-network-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/kyber-network-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/kyber-network-content-signals.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/kyber-network-zaas.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/kyber-network-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/kyber-network-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyber-network-domain-security.yml
created: '2026-07-17'
description: 'Kyber Network is the team behind KyberSwap, a multi-chain DeFi liquidity hub and DEX aggregator that routes trades across indexed decentralized exchanges to source the best available on-chain rate. It publishes three public, unauthenticated EVM APIs: the Aggregator API for instant token swaps with dynamic trade routing, the Limit Order API for gasless price-conditional trades using off-chain relay with on-chain settlement, and the Zap as a Service (ZaaS) API for single-transaction concentrated liquidity provision, exit and migration. KyberSwap also ships embeddable React swap and liquidity widgets, an RFC 9727 API catalog, an llms.txt documentation index, a first-party MCP server and a published Agent Skills plugin, making it one of the more agent-ready providers in the DeFi category. Governance runs through KyberDAO and the KNC token.'
image: https://kyberswap.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: kyber-network-mcp.yml
  slug: kyber-network-mcpyml
modified: '2026-07-19'
name: Kyber Network
nav: Providers
network: true
overview: 'Kyber Network publishes 5 APIs on the [APIs.io](https://apis.io/) network, including General API, Maker API, Service API, and 2 more. Tagged areas include Company, Crypto, DeFi, Blockchain, and Decentralized Exchange.


  Kyber Network''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 23 more developer resources.'
random_paper: 88
rate_limits:
- limit_count: 3
  name: Kyber Network Rate Limits
  slug: kyber-network-rate-limits
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 54.3
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 60.5
  previous_composite: 51.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 36.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyber-network/refs/heads/main/screenshots/kyber-network-2026-07-25T224353.png
security:
- kind: authentication
  name: Kyber Network Authentication
  slug: kyber-network-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kyber Network Domain Security
  slug: kyber-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kyber-network
tags:
- Company
- Crypto
- DeFi
- Blockchain
- Decentralized Exchange
- Token Swap
- Liquidity
- Trading
- Web3
- Ethereum
website: https://kyber.network/
---
