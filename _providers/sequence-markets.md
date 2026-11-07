---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Bearer-auth REST API and multiplexed WebSocket streaming surface for the Sequence Markets trading OS — credentials & wallets, market data, orders & execution graphs, positions & balances, prediction m
  name: Sequence Markets Trading API
  slug: sequence-markets-trading-api
artifact_total: 7
asyncapis:
- description: Multiplexed WebSocket streaming surface for the Sequence Markets trading OS, generated faithfully from the documented channel catalog at docs.sequencemkts.com/api/streaming. Not an official provider-p
  name: Sequence Markets Streaming API
  slug: sequence-markets-streaming-asyncapi
common:
- group: auth
  href: https://artifacts.apis.io/sequence-markets/security/sequence-markets-domain-security.yml
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
  href: https://artifacts.apis.io/sequence-markets/authentication/sequence-markets-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sequence-markets-authentication.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/conventions/sequence-markets-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sequence-markets-conventions.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/conventions/sequence-markets-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sequence-markets-conventions.yml
- group: build
  href: https://artifacts.apis.io/sequence-markets/packages/sequence-markets-packages.yml
  title: ''
  type: Packages
  url: packages/sequence-markets-packages.yml
- group: build
  href: https://artifacts.apis.io/sequence-markets/packages/sequence-markets-packages.yml
  title: ''
  type: SDKs
  url: packages/sequence-markets-packages.yml
- group: build
  href: https://artifacts.apis.io/sequence-markets/cli/sequence-markets-cli.yml
  title: ''
  type: CLI
  url: cli/sequence-markets-cli.yml
- group: start
  href: https://artifacts.apis.io/sequence-markets/sandbox/sequence-markets-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sequence-markets-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/sequence-markets/conventions/sequence-markets-conventions.yml
  title: ''
  type: RateLimits
  url: conventions/sequence-markets-conventions.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/errors/sequence-markets-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sequence-markets-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/sequence-markets/mcp/sequence-markets-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sequence-markets-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sequence-markets/llms/sequence-markets-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sequence-markets-llms.txt
- group: agent
  href: https://artifacts.apis.io/sequence-markets/well-known/sequence-markets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sequence-markets-well-known.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/lifecycle/sequence-markets-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sequence-markets-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/conformance/sequence-markets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sequence-markets-conformance.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/data-model/sequence-markets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sequence-markets-data-model.yml
- group: docs
  href: https://artifacts.apis.io/sequence-markets/asyncapi/sequence-markets-streaming-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/sequence-markets-streaming-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/sequence-markets/asyncapi/sequence-markets-streaming-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/sequence-markets-streaming-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/sequence-markets/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Sequence Markets is a Y Combinator (Winter 2026) trading operating system for institutional crypto that provides unified execution infrastructure across 12 fragmented digital-asset venues — centralized exchanges (Coinbase, Binance, Kraken, OKX, Bybit, Bitget, Crypto.com, Hyperliquid), DeFi, and prediction markets (Kalshi, Polymarket). It packages one market view into a single trade via a smart order router (SOR), execution graphs, and WASM-compiled algo strategies deployed to multi-region low-latency edges. Developers access it through a Bearer-auth REST API and multiplexed WebSocket streams, a Python SDK, a Rust SDK, an Algo SDK, a `sequence` CLI, and an MCP interface for human, algorithmic, and agent workflows, with a full paper-trading sandbox, smart order routing, and transaction-cost analytics (TCA).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sequence-markets.png
layout: provider
modified: '2026-07-21'
name: Sequence Markets
nav: Providers
network: true
overview: 'Sequence Markets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trading, Cryptocurrency, Digital Assets, and Execution.


  The Sequence Markets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sequence Markets'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, sandbox, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 40.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sequence-markets/sequence-markets-2026-08-17T081812.png
security:
- kind: authentication
  name: Sequence Markets Authentication
  slug: sequence-markets-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Sequence Markets Domain Security
  slug: sequence-markets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Connect a venue and check the unified portfolio
  slug: sequence-markets-connect-venue-and-check-portfolio
- name: Deploy a WASM algo strategy
  slug: sequence-markets-deploy-wasm-algo
- name: Place a smart-routed order
  slug: sequence-markets-place-smart-routed-order
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
- Fintech
- Developer Tools
- Real-Time
website: https://sequencemkts.com/
---
