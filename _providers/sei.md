---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Sei Agentic Access
  operation_count: 177
  slug: sei-agentic-access
  summary_line: 177 operations · 2 acting
api_count: 2
apis:
- description: Ethereum-compatible JSON-RPC API for interacting with Sei's EVM layer. Supports standard Ethereum methods for sending transactions, querying account balances and code, retrieving block and transaction
  name: Sei EVM JSON-RPC API
  slug: sei-evm-json-rpc-api
- description: ABCI APIs
  name: Sei ABCI API
  slug: sei-abci-api
- description: Event subscription APIs
  name: Sei Events API
  slug: sei-events-api
- description: Evidence APIs
  name: Sei Evidence API
  slug: sei-evidence-api
- description: Informations about the node APIs
  name: Sei Info API
  slug: sei-info-api
- description: The Query API from Sei — 129 operation(s) for query.
  name: Sei Query API
  slug: sei-query-api
- description: The Service API from Sei — 10 operation(s) for service.
  name: Sei Service API
  slug: sei-service-api
- description: Transactions broadcast APIs
  name: Sei Tx API
  slug: sei-tx-api
- description: Unsafe APIs
  name: Sei Unsafe API
  slug: sei-unsafe-api
- description: Subscribe/unsubscribe are reserved for websocket events.
  name: Sei Websocket API
  slug: sei-websocket-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HTTP API Console ABCI API
  slug: open-sei-abci-api
- collection_type: open
  name: HTTP API Console ABCI Events API
  slug: open-sei-events-api
- collection_type: open
  name: HTTP API Console ABCI Evidence API
  slug: open-sei-evidence-api
- collection_type: open
  name: HTTP API Console ABCI Info API
  slug: open-sei-info-api
- collection_type: open
  name: HTTP API Console ABCI Query API
  slug: open-sei-query-api
- collection_type: open
  name: HTTP API Console ABCI Service API
  slug: open-sei-service-api
- collection_type: open
  name: HTTP API Console ABCI Tx API
  slug: open-sei-tx-api
- collection_type: open
  name: HTTP API Console ABCI Unsafe API
  slug: open-sei-unsafe-api
- collection_type: open
  name: HTTP API Console ABCI Websocket API
  slug: open-sei-websocket-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sei-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sei-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sei.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sei.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sei-protocol
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sei-protocol/sei-chain
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sei
- group: company
  title: ''
  type: Blog
  url: https://blog.sei.io
- group: other
  title: ''
  type: X
  url: https://x.com/SeiNetwork
- group: other
  title: ''
  type: BlockExplorer
  url: https://www.seiscan.app
- group: other
  title: ''
  type: Faucet
  url: https://docs.sei.io/getting-started/faucet
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sei.io
- group: commercial
  title: ''
  type: FinOps
  url: finops/sei-finops.md
created: '2026-06-13'
description: Sei is a high-performance Layer 1 blockchain optimized for trading and decentralized exchange (DEX) applications. It is the first parallelized EVM blockchain, delivering sub-second block times (~400ms), 100 MGas/s throughput, and full Ethereum compatibility without code changes. Sei combines Twin Turbo Consensus, a parallelization engine, and SeiDB to eliminate traditional performance bottlenecks. Developers can interact with Sei through EVM JSON-RPC endpoints (Ethereum-compatible) and Cosmos REST/LCD endpoints for querying markets, orders, accounts, staking, governance, and DEX state on the pacific-1 mainnet and atlantic-2 testnet networks.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sei.png
jsonld:
- class_count: 0
  name: Sei Context
  property_count: 0
  slug: sei
layout: provider
modified: '2026-06-13'
name: Sei
nav: Providers
network: true
overview: 'Sei publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ABCI API, Events API, Evidence API, and 6 more. Tagged areas include Blockchain, Layer 1, EVM, DeFi, and DEX.


  The Sei catalog on APIs.io includes 1 JSON-LD context.


  Sei''s developer surface includes documentation, GitHub presence, engineering blog, and 10 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 5
  name: Sei Cosmos Rest Api Rate Limits
  slug: sei-cosmos-rest-api-rate-limits
- limit_count: 4
  name: Sei Evm Json Rpc Api Rate Limits
  slug: sei-evm-json-rpc-api-rate-limits
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 48.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 44.7
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 77.8
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 18.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sei/refs/heads/main/screenshots/sei-2026-06-20T193635.png
security:
- kind: domain-security
  name: Sei Domain Security
  slug: sei-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sei
tags:
- Blockchain
- Layer 1
- EVM
- DeFi
- DEX
- Trading
- Cosmos
- Web3
website: https://sei.io
---
