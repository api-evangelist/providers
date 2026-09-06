---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hyperliquid Agentic Access
  operation_count: 1
  slug: hyperliquid-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Public REST API for the Hyperliquid exchange. Read endpoints expose market metadata, order books, candles, trades, funding rates, user state, open orders, fills, and historical data. Write endpoints (
  name: Hyperliquid REST API
  slug: rest-api
- description: Real-time WebSocket feed delivering order-book deltas, trades, candles, BBO, user fills, user funding, user-events, and active asset context. Also supports WebSocket-based POST actions for low-latency
  name: Hyperliquid WebSocket API
  slug: websocket-api
- description: Official Python SDK for the Hyperliquid REST and WebSocket APIs. Handles EIP-712 signing, action serialization, websocket subscription management, and typed wrappers for market and trading endpoints.
  name: Hyperliquid Python SDK
  slug: python-sdk
- description: Official Rust SDK for the Hyperliquid REST and WebSocket APIs, suited for high-performance market-making and trading clients.
  name: Hyperliquid Rust SDK
  slug: rust-sdk
- description: Open-source Hyperliquid validator / non-validating node distribution used to participate in the HyperBFT consensus network and serve HyperCore + HyperEVM state.
  name: Hyperliquid Node
  slug: node
- description: EVM-compatible JSON-RPC endpoint exposed by Hyperliquid for deploying and interacting with smart contracts on HyperEVM (chain ID 999), executed alongside HyperCore.
  name: HyperEVM JSON-RPC
  slug: hyperevm-rpc
- baseURL: https://api.hyperliquid.xyz
  baseurl_source: declared
  description: The Info API from Hyperliquid — 1 operation(s) for info.
  name: Hyperliquid Info API
  slug: hyperliquid-info-api
artifact_total: 17
asyncapis:
- description: AsyncAPI 2.6 specification for the Hyperliquid public WebSocket API. Clients connect to wss://api.hyperliquid.xyz/ws (mainnet) or wss://api.hyperliquid-testnet.xyz/ws (testnet) and send subscribe / un
  name: Hyperliquid WebSocket API
  slug: hyperliquid-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hyperliquid Info API
  slug: open-hyperliquid-info-api
- collection_type: open
  name: Hyperliquid Info API
  slug: open-hyperliquid
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hyperliquid-dex/hyperliquid-python-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hyperliquid-dex/hyperliquid-python-sdk/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hyperliquid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperliquid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hyperliquid.xyz
- group: other
  title: ''
  type: Foundation
  url: https://hyperfoundation.org
- group: docs
  title: ''
  type: Documentation
  url: https://hyperliquid.gitbook.io/hyperliquid-docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hyperliquid-dex
- group: other
  title: ''
  type: App
  url: https://app.hyperliquid.xyz
- group: other
  title: ''
  type: Stats
  url: https://stats.hyperliquid.xyz
- group: company
  title: ''
  type: Twitter
  url: https://x.com/HyperliquidX
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/hyperliquid
created: '2026-05-23'
description: Hyperliquid is a high-performance Layer 1 blockchain (HyperBFT consensus, HyperCore + HyperEVM execution) best known for its native perpetual futures and spot DEX with capacity for hundreds of thousands of orders per second. Developers and traders interact with Hyperliquid through a public REST and WebSocket API at api.hyperliquid.xyz for trading, order management, market data, and account state. Official Python and Rust SDKs wrap the API, and the node, order-book server, and HyperEVM tooling are open-sourced under the hyperliquid-dex GitHub organization.
finops:
- name: Hyperliquid Finops
  service_category: API
  slug: hyperliquid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hyperliquid.png
layout: provider
modified: '2026-05-29'
name: Hyperliquid
nav: Providers
network: true
overview: 'Hyperliquid publishes 2 APIs on the [APIs.io](https://apis.io/) network: WebSocket API and Info API. Tagged areas include DeFi, Perpetuals, DEX, Layer 1, and Trading.


  The Hyperliquid catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hyperliquid''s developer surface includes documentation, GitHub presence, and 12 more developer resources.'
plans:
- name: Hyperliquid Plans Pricing
  plan_count: 1
  slug: hyperliquid-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Hyperliquid Rate Limits
  slug: hyperliquid-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Hyperliquid API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: hyperliquid-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 60.1
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 60.0
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperliquid/refs/heads/main/screenshots/hyperliquid-2026-06-20T183045.png
security:
- kind: domain-security
  name: Hyperliquid Domain Security
  slug: hyperliquid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperliquid
tags:
- DeFi
- Perpetuals
- DEX
- Layer 1
- Trading
- Order Book
- HyperEVM
website: https://hyperliquid.xyz
---
