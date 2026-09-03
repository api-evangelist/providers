---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://rpc-mainnet.supra.com
  baseurl_source: declared
  description: Public, keyless REST + JSON API served by every Supra RPC node. Covers accounts (resources, modules, coin and fungible-asset statements), transaction submission and simulation, gas price estimation, b
  name: Supra RPC Node API
  slug: supra-rpc-node-api
- description: Oracle market-data REST API returning the latest price for a trading pair and historical OHLC candles for up to one month, on the DORA data feeds Supra publishes on-chain. Two documented endpoints, GE
  name: Supra Price Feeds REST API
  slug: supra-price-feeds-rest-api
- description: Streaming oracle market-data API. Clients open a WebSocket to wss://prod-kline-ws.supra.com with an x-api-key header and send a subscribe action naming the ohlc_datafeed channel, a resolution in minut
  name: Supra Price Feeds WebSocket API
  slug: supra-price-feeds-websocket-api
- baseURL: https://rpc-mainnet.supra.com
  baseurl_source: declared
  description: 'Read and observation surface for Supra''s native on-chain automation (AutoFi) registry. Automation tasks are registered and cancelled through the Supra CLI and Move entry functions rather than an HTTP '
  name: Supra Automation API
  slug: supra-automation-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://supra.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://supra.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.supra.com/
- group: docs
  title: ''
  type: APIReference
  url: https://rpc-mainnet.supra.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.supra.com/network/move/getting-started
- group: operate
  title: ''
  type: Support
  url: https://forum.supra.com/
- group: company
  title: ''
  type: Blog
  url: https://supra.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Entropy-Foundation
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supra.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supra.com/privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supra-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.supra.com/llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/supra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/supra-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/supra-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/supra-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/supra-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/supra-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/supra-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/supra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/supra-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/supra-cli.yml
- group: design
  title: ''
  type: Components
  url: components/supra-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/supra-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/supra-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/supra-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supra-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/supra-vulnerability-disclosure.yml
created: '2026-08-29'
description: 'Supra is a vertically integrated Layer 1 blockchain developed by the Swiss-based Entropy Foundation, combining a MultiVM execution layer (MoveVM plus an EVM) with services that most chains outsource: DORA native oracle price feeds (push and pull), decentralized verifiable randomness (dVRF), protocol-level automation (AutoFi), on-chain technical indicators and indices, and the SupraNova / HyperNova cross-chain bridge. Developers reach the network through a public, keyless REST + JSON node API at rpc-mainnet.supra.com that publishes a live OpenAPI 3.1 description covering 56 operations across accounts, transactions, blocks, events, view functions, tables and inclusion proofs, plus a JSON-RPC WebSocket subscription stream for newly committed blocks. Market data is served separately by an API-key-gated Price Feeds REST and WebSocket API for real-time and historical OHLC data. Supra is headquartered in Miami, Florida and was founded in 2019.'
image: https://prod-assets.cerberus.supra.com/spa-assets/og-images/og-homepage.png
layout: provider
modified: '2026-08-29'
name: Supra
nav: Providers
network: true
overview: 'Supra publishes 2 APIs on the [APIs.io](https://apis.io/) network: RPC Node API and Automation API. Tagged areas include Blockchain, Layer 1, Oracles, Web3, and Market Data.


  Supra''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, CLI, and 23 more developer resources.'
plans:
- name: Supra Plans Pricing
  plan_count: 0
  slug: supra-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Supra Rate Limits
  slug: supra-rate-limits
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 22
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.8
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 49.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/supra/refs/heads/main/screenshots/supra-2026-09-02T161308.png
security:
- kind: authentication
  name: Supra Authentication
  slug: supra-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Supra Domain Security
  slug: supra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supra Vulnerability Disclosure
  slug: supra-vulnerability-disclosure
  summary_line: Hackerone
slug: supra
tags:
- Blockchain
- Layer 1
- Oracles
- Web3
- Market Data
- Smart Contracts
- Verifiable Randomness
- Cross-Chain Bridge
- Automation
- Move
- Cryptocurrency
- DeFi
website: https://supra.com/
---
