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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
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
  name: Kyber Network Swap API
  slug: kyber-network-swap-api
- baseURL: https://aggregator-api.kyberswap.com
  baseurl_source: declared
  description: The Taker API from Kyber Network — 4 operation(s) for taker.
  name: Kyber Network Taker API
  slug: kyber-network-taker-api
artifact_total: 19
collections:
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
  href: https://artifacts.apis.io/kyber-network/overlays/kyber-network-aggregator-overlay.yaml
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
  href: https://artifacts.apis.io/kyber-network/lifecycle/kyber-network-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/kyber-network-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/kyber-network/lifecycle/kyber-network-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/kyber-network-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kyber-network/lifecycle/kyber-network-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kyber-network-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/kyber-network/rate-limits/kyber-network-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kyber-network-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/kyber-network/authentication/kyber-network-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kyber-network-authentication.yml
- group: design
  href: https://artifacts.apis.io/kyber-network/conventions/kyber-network-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kyber-network-conventions.yml
- group: design
  href: https://artifacts.apis.io/kyber-network/errors/kyber-network-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/kyber-network-error-codes.yml
- group: build
  href: https://artifacts.apis.io/kyber-network/packages/kyber-network-packages.yml
  title: ''
  type: Packages
  url: packages/kyber-network-packages.yml
- group: build
  href: https://artifacts.apis.io/kyber-network/packages/kyber-network-packages.yml
  title: ''
  type: SDKs
  url: packages/kyber-network-packages.yml
- group: design
  href: https://artifacts.apis.io/kyber-network/components/kyber-network-components.yml
  title: ''
  type: Components
  url: components/kyber-network-components.yml
- group: agent
  href: https://artifacts.apis.io/kyber-network/mcp/kyber-network-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kyber-network-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kyber-network/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kyber-network/llms/kyber-network-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kyber-network-llms.txt
- group: agent
  href: https://artifacts.apis.io/kyber-network/well-known/kyber-network-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kyber-network-well-known.yml
- group: other
  href: https://artifacts.apis.io/kyber-network/well-known/kyber-network-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/kyber-network-api-catalog.json
- group: other
  href: https://artifacts.apis.io/kyber-network/well-known/kyber-network-content-signals.txt
  title: ''
  type: ContentSignal
  url: well-known/kyber-network-content-signals.txt
- group: other
  href: https://artifacts.apis.io/kyber-network/grpc/kyber-network-zaas.proto
  title: ''
  type: Protobuf
  url: grpc/kyber-network-zaas.proto
- group: design
  href: https://artifacts.apis.io/kyber-network/conformance/kyber-network-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kyber-network-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kyber-network/conformance/kyber-network-conformance.yml
  title: ''
  type: Compliance
  url: conformance/kyber-network-conformance.yml
- group: auth
  href: https://artifacts.apis.io/kyber-network/security/kyber-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kyber-network-domain-security.yml
created: '2026-07-17'
description: 'Kyber Network is the team behind KyberSwap, a multi-chain DeFi liquidity hub and DEX aggregator that routes trades across indexed decentralized exchanges to source the best available on-chain rate. It publishes three public, unauthenticated EVM APIs: the Aggregator API for instant token swaps with dynamic trade routing, the Limit Order API for gasless price-conditional trades using off-chain relay with on-chain settlement, and the Zap as a Service (ZaaS) API for single-transaction concentrated liquidity provision, exit and migration. KyberSwap also ships embeddable React swap and liquidity widgets, an RFC 9727 API catalog, an llms.txt documentation index, a first-party MCP server and a published Agent Skills plugin, making it one of the more agent-ready providers in the DeFi category. Governance runs through KyberDAO and the KNC token.'
image: https://kyberswap.com/favicon.ico
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 13 tools listed.
  name: Kyber Network MCP Server
  slug: kyberswap
modified: '2026-07-19'
name: Kyber Network
nav: Providers
network: true
overview: 'Kyber Network publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including General API, Maker API, Service API, and 2 more. Tagged areas include Company, Cryptocurrency, DeFi, Blockchain, and Decentralized Exchange.


  The Kyber Network catalog on APIs.io includes 1 Spectral governance ruleset.


  Kyber Network''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 24 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 3
  name: Kyber Network Rate Limits
  slug: kyber-network-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Kyber Network API Rules
  rule_count: 44
  severity_counts:
    error: 32
    hint: 0
    info: 5
    warn: 7
  slug: kyber-network-rules
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 43.6
    developer_ergonomics: 71.4
    discoverability: 76.7
    operational_transparency: 57.9
  previous_composite: 49.8
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
    score: 20.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kyber-network/kyber-network-2026-07-25T224353.png
security:
- kind: authentication
  name: Kyber Network Authentication
  slug: kyber-network-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Kyber Network Domain Security
  slug: kyber-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: cancel-limit-order
  slug: kyber-network-cancel-limit-order
- name: place-limit-order
  slug: kyber-network-place-limit-order
- name: swap-with-aggregator
  slug: kyber-network-swap-with-aggregator
- name: zap-into-liquidity
  slug: kyber-network-zap-into-liquidity
slug: kyber-network
tags:
- Company
- Cryptocurrency
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
