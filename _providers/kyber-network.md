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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The General API from Kyber Network — 2 operation(s) for general.
  name: Kyber Network General API
  slug: kyber-network-general-api
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The Maker API from Kyber Network — 8 operation(s) for maker.
  name: Kyber Network Maker API
  slug: kyber-network-maker-api
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The Service API from Kyber Network — 3 operation(s) for service.
  name: Kyber Network Service API
  slug: kyber-network-service-api
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The swap API from Kyber Network — 3 operation(s) for swap.
  name: Kyber Network swap API
  slug: kyber-network-swap-api
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The Taker API from Kyber Network — 4 operation(s) for taker.
  name: Kyber Network Taker API
  slug: kyber-network-taker-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KyberSwap Aggregator General API
  slug: open-kyber-network-general-api
- collection_type: open
  name: KyberSwap Aggregator General Maker API
  slug: open-kyber-network-maker-api
- collection_type: open
  name: KyberSwap Aggregator General Service API
  slug: open-kyber-network-service-api
- collection_type: open
  name: KyberSwap Aggregator General swap API
  slug: open-kyber-network-swap-api
- collection_type: open
  name: KyberSwap Aggregator General Taker API
  slug: open-kyber-network-taker-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kyber-network-aggregator-overlay.yaml
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
  name: Kyber Network MCP Server
  slug: kyber-network-mcp-server
modified: '2026-07-19'
name: Kyber Network
nav: Providers
network: true
overview: 'Kyber Network publishes 5 APIs on the [APIs.io](https://apis.io/) network, including General API, Maker API, Service API, and 2 more. Tagged areas include Company, Crypto, DeFi, Blockchain, and Decentralized Exchange.


  Kyber Network''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 24 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 3
  name: Kyber Network Rate Limits
  slug: kyber-network-rate-limits
score:
  band: developing
  composite: 50.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 48.4
    developer_ergonomics: 71.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 50.8
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 36.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
