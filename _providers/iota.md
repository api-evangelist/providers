---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 96
  human_in_the_loop: 1
  name: Iota Agentic Access
  operation_count: 138
  slug: iota-agentic-access
  summary_line: 138 operations · 96 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: 'GraphQL RPC interface for the IOTA blockchain, providing an alternative to the JSON-RPC API. Supports querying transaction blocks, objects, checkpoints, events, and on-chain state using GraphQL query '
  name: IOTA GraphQL API
  slug: iota-graphql-api
- description: The auth API from IOTA — 2 operation(s) for auth.
  name: IOTA auth API
  slug: iota-auth-api
- description: The chains API from IOTA — 18 operation(s) for chains.
  name: IOTA chains API
  slug: iota-chains-api
- description: 'Coin and balance queries: balances, coins list, metadata, supply'
  name: IOTA Coin Query API
  slug: iota-coin-query-api
- description: The corecontracts API from IOTA — 18 operation(s) for corecontracts.
  name: IOTA corecontracts API
  slug: iota-corecontracts-api
- description: Indexer-exclusive methods for advanced queries, events, dynamic fields, IOTA Names
  name: IOTA Extended API
  slug: iota-extended-api
- description: Governance, staking, validator, epoch, and system state queries
  name: IOTA Governance API
  slug: iota-governance-api
- description: The Health API from IOTA — 1 operation(s) for health.
  name: IOTA Health API
  slug: iota-health-api
- description: The metrics API from IOTA — 3 operation(s) for metrics.
  name: IOTA metrics API
  slug: iota-metrics-api
- description: 'Move smart contract introspection: modules, functions, structs'
  name: IOTA Move Utils API
  slug: iota-move-utils-api
- description: The node API from IOTA — 11 operation(s) for node.
  name: IOTA node API
  slug: iota-node-api
- description: 'Core read operations: objects, checkpoints, transactions, events, protocol config'
  name: IOTA Read API
  slug: iota-read-api
- description: The requests API from IOTA — 1 operation(s) for requests.
  name: IOTA requests API
  slug: iota-requests-api
- description: Build unsigned transactions for transfers, staking, Move calls (unsafe_ prefix)
  name: IOTA Transaction Builder API
  slug: iota-transaction-builder-api
- description: The users API from IOTA — 4 operation(s) for users.
  name: IOTA users API
  slug: iota-users-api
- description: Transaction execution, dry run, and dev inspection
  name: IOTA Write API
  slug: iota-write-api
- description: The Ws API from IOTA — 1 operation(s) for ws.
  name: IOTA Ws API
  slug: iota-ws-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wasp auth API
  slug: open-iota-auth-api
- collection_type: open
  name: Wasp auth chains API
  slug: open-iota-chains-api
- collection_type: open
  name: Wasp auth Coin Query API
  slug: open-iota-coin-query-api
- collection_type: open
  name: Wasp auth corecontracts API
  slug: open-iota-corecontracts-api
- collection_type: open
  name: Wasp auth Extended API
  slug: open-iota-extended-api
- collection_type: open
  name: Wasp auth Governance API
  slug: open-iota-governance-api
- collection_type: open
  name: Wasp auth Health API
  slug: open-iota-health-api
- collection_type: open
  name: Wasp auth metrics API
  slug: open-iota-metrics-api
- collection_type: open
  name: Wasp auth Move Utils API
  slug: open-iota-move-utils-api
- collection_type: open
  name: Wasp auth node API
  slug: open-iota-node-api
- collection_type: open
  name: IOTA JSON-RPC
  slug: open-iota-openrpc
- collection_type: open
  name: Wasp auth Read API
  slug: open-iota-read-api
- collection_type: open
  name: Wasp auth requests API
  slug: open-iota-requests-api
- collection_type: open
  name: Wasp auth Transaction Builder API
  slug: open-iota-transaction-builder-api
- collection_type: open
  name: Wasp auth users API
  slug: open-iota-users-api
- collection_type: open
  name: Wasp auth Write API
  slug: open-iota-write-api
- collection_type: open
  name: Wasp auth Ws API
  slug: open-iota-ws-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/iotaledger/iota/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/iotaledger/iota/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/iotaledger/iota/blob/develop/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/iotaledger/iota/blob/develop/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/iotaledger/iota/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iota-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iota-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iota-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.iota.org/
- group: start
  title: ''
  type: Portal
  url: https://docs.iota.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iota.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iota.org/developer/getting-started
- group: docs
  title: IOTA JSON-RPC API Reference
  type: APIReference
  url: https://docs.iota.org/iota-api-ref
- group: auth
  title: Public endpoints require no API key; load balanced and rate limited
  type: Authentication
  url: https://docs.iota.org/developer/network-overview
- group: build
  title: IOTA TypeScript SDK
  type: SDKs
  url: https://docs.iota.org/developer/ts-sdk/
- group: build
  title: IOTA Rust SDK
  type: SDKs
  url: https://github.com/iotaledger/iota/tree/develop/crates/iota-sdk
- group: build
  title: IOTA GraphQL RPC
  type: SDKs
  url: https://docs.iota.org/developer/references/iota-api
- group: build
  title: IOTA CLI
  type: CLI
  url: https://docs.iota.org/developer/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iotaledger
- group: build
  title: IOTA Core Repository
  type: GitHubRepository
  url: https://github.com/iotaledger/iota
- group: other
  title: IOTA Explorer (Mainnet)
  type: Explorer
  url: https://explorer.iota.org/
- group: other
  title: IOTA Testnet Faucet
  type: Faucet
  url: https://faucet.testnet.iota.cafe
- group: company
  title: ''
  type: Blog
  url: https://blog.iota.org/
- group: other
  title: IOTA Network Overview (Mainnet, Testnet, Devnet)
  type: NetworkOverview
  url: https://docs.iota.org/developer/network-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iota.org/privacy-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iota.org/privacy-policy
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iota-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iota-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/iota-finops.yml
- group: docs
  title: IOTA JSON-RPC OpenAPI 3.0 (75 methods, derived from OpenRPC)
  type: OpenAPI
  url: openapi/_original/iota-jsonrpc-openapi.json
- group: docs
  title: IOTA EVM WASP Node REST API OpenAPI 3.0 (59 paths)
  type: OpenAPI
  url: openapi/_original/iota-evm-wasp-openapi.yaml
- group: other
  title: IOTA JSON-RPC OpenRPC Specification (source)
  type: OpenRPC
  url: openapi/iota-openrpc.json
- group: design
  title: IOTA JSON-LD Context
  type: JSONLDContext
  url: json-ld/iota-context.jsonld
- group: docs
  title: IOTA GraphQL RPC Schema and Docs
  type: GraphQL
  url: graphql/iota-graphql.md
created: '2026-06-14'
description: IOTA is an open-source distributed ledger technology built to bring real-world applications on-chain. It is the first internet-scale programmable blockchain platform powered by the Move programming language with horizontal scaling, feeless transactions, and a unique parallel transaction processing model. IOTA exposes a JSON-RPC 2.0 API over HTTP and a GraphQL RPC for querying objects, checkpoints, transactions, coins, events, and on-chain state on Mainnet, Testnet, and Devnet networks. The platform targets trade and supply chains, decentralized finance, digital identity, real-world asset tokenization, and product lifecycle management.
features:
- description: Standard JSON-RPC 2.0 protocol over HTTP POST to IOTA full nodes and indexers
  name: JSON-RPC 2.0 over HTTP
- description: GraphQL interface as an alternative to JSON-RPC for flexible on-chain data queries
  name: GraphQL RPC
- description: Mainnet (production), Testnet (testing), and Devnet (development) environments with faucets
  name: Three Network Environments
- description: Asset-oriented Move programming language for type-safe, resource-oriented smart contracts
  name: Move Smart Contracts
- description: Ethereum-compatible EVM Layer 2 chain enabling Solidity contract deployment and tooling reuse
  name: EVM Layer 2
- description: Public endpoints are open and require no API key for development and testing use
  name: No Authentication Required
- description: All list endpoints support cursor-based pagination for efficient data traversal
  name: Cursor-based Pagination
- description: Binary Canonical Serialization (BCS) support alongside JSON for efficient data transfer
  name: BCS Binary Encoding
finops:
- name: Iota Finops
  service_category: Blockchain Infrastructure
  slug: iota-finops
graphqls:
- description: The IOTA GraphQL RPC provides a flexible, typed interface for querying on-chain state on the IOTA blockchain. It serves as an alternative to the JSON-RPC 2.0 API and is served by the IOTA indexer. The
  name: IOTA GraphQL API
  slug: iota-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iota.png
jsonld:
- class_count: 1
  name: Iota Context
  property_count: 30
  slug: iota-context
layout: provider
modified: '2026-06-14'
name: IOTA
nav: Providers
network: true
overview: 'IOTA publishes 16 APIs on the [APIs.io](https://apis.io/) network, including auth API, chains API, Coin Query API, and 13 more. Tagged areas include Blockchain, Distributed Ledger, Web3, DeFi, and Cryptocurrency.


  The IOTA catalog on APIs.io includes 1 JSON-LD context.


  IOTA''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, CLI, engineering blog, and 27 more developer resources.'
plans:
- name: Iota Plans
  plan_count: 3
  slug: iota-plans
random_paper: 131
rate_limits:
- limit_count: 4
  name: Iota Rate Limits
  slug: iota-rate-limits
score:
  band: strong
  composite: 56.8
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.5
    developer_ergonomics: 69.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iota/refs/heads/main/screenshots/iota-2026-06-20T183535.png
security:
- kind: authentication
  name: Iota Authentication
  slug: iota-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Iota Domain Security
  slug: iota-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: iota
tags:
- Blockchain
- Distributed Ledger
- Web3
- DeFi
- Cryptocurrency
- Move
- Tangle
use_cases:
- description: Query coin balances, object states, and submit transactions for decentralized finance apps on IOTA
  name: DeFi Application Backend
- description: Track real-world assets and product lifecycle data on the IOTA distributed ledger
  name: Supply Chain Traceability
- description: Manage decentralized identifiers (DIDs) and verifiable credentials on-chain
  name: Digital Identity
- description: Tokenize and manage traditional financial assets bridged to IOTA using Move smart contracts
  name: Real-World Asset Tokenization
- description: Query checkpoints, transaction blocks, and events for real-time analytics and data pipelines
  name: Blockchain Analytics
- description: Check coin balances, fetch transaction history, build and submit signed transactions
  name: Wallet Development
- description: Introspect Move modules, deploy packages, and interact with on-chain programs via Move Utils
  name: Smart Contract Development
- description: Deploy existing Solidity smart contracts on IOTA EVM Layer 2 using standard Ethereum tooling
  name: EVM dApp Migration
website: https://www.iota.org/
---
