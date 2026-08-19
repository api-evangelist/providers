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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 56
  human_in_the_loop: 0
  name: Sui Agentic Access
  operation_count: 56
  slug: sui-agentic-access
  summary_line: 56 operations · 56 acting
api_count: 11
apis:
- description: 'A generally available RPC service for flexible reads, transaction submission, and simulation backed by the Sui General-Purpose Indexer, Consistent Store, full nodes, and Archival Service. Best suited '
  name: Sui GraphQL RPC
  slug: sui-graphql-rpc
- description: The legacy JSON-RPC API for interacting with Sui full nodes, providing methods for querying objects, transactions, checkpoints, events, balances, and coin metadata. This interface is deprecated and wi
  name: Sui JSON-RPC API (Deprecated)
  slug: sui-json-rpc-api-deprecated
- description: The Coin Query API API from Sui — 6 operation(s) for coin query api.
  name: Sui Coin Query API API
  slug: sui-coin-query-api-api
- description: Extended query methods (suix_ prefix)
  name: Sui Extended API API
  slug: sui-extended-api-api
- description: The Governance Read API API from Sui — 6 operation(s) for governance read api.
  name: Sui Governance Read API API
  slug: sui-governance-read-api-api
- description: The Move Utils API from Sui — 5 operation(s) for move utils.
  name: Sui Move Utils API
  slug: sui-move-utils-api
- description: The PubSub API from Sui — 2 operation(s) for pubsub.
  name: Sui PubSub API
  slug: sui-pubsub-api
- description: Methods for reading blockchain state
  name: Sui Read API API
  slug: sui-read-api-api
- description: The Transaction Builder API API from Sui — 13 operation(s) for transaction builder api.
  name: Sui Transaction Builder API API
  slug: sui-transaction-builder-api-api
- description: The Websocket API from Sui — 2 operation(s) for websocket.
  name: Sui Websocket API
  slug: sui-websocket-api
- description: Methods for submitting transactions
  name: Sui Write API API
  slug: sui-write-api-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sui JSON-RPC Coin Query API API
  slug: open-sui-coin-query-api-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Extended API API
  slug: open-sui-extended-api-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Governance Read API API
  slug: open-sui-governance-read-api-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Move Utils API
  slug: open-sui-move-utils-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API PubSub API
  slug: open-sui-pubsub-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Read API API
  slug: open-sui-read-api-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Transaction Builder API API
  slug: open-sui-transaction-builder-api-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Websocket API
  slug: open-sui-websocket-api
- collection_type: open
  name: Sui JSON-RPC Coin Query API Write API API
  slug: open-sui-write-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sui-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sui-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sui/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sui/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sui/refs/heads/main/finops/finops.yml
- group: company
  title: ''
  type: Website
  url: https://sui.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sui.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MystenLabs/sui
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mystenlabs.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mystenlabs.com/legal/terms
- group: company
  title: ''
  type: Blog
  url: https://blog.sui.io
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sui
- group: operate
  title: ''
  type: Forums
  url: https://forums.sui.io
- group: other
  title: ''
  type: X
  url: https://x.com/SuiNetwork
- group: build
  title: ''
  type: SDKs
  url: https://sdk.mystenlabs.com/sui/clients
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.sui.io/references/sui-api/beta-graph-ql/
- group: docs
  title: ''
  type: MigrationGuide
  url: https://docs.sui.io/references/sui-api/json-rpc-migration
created: '2026-06-13'
description: Sui is a next-generation Move-based blockchain developed by Mysten Labs, designed for high throughput, low latency, and an asset-oriented programming model. It provides gRPC, GraphQL, and legacy JSON-RPC interfaces for querying objects, transactions, checkpoints, events, and balances on the Sui network. The gRPC API is the current recommended interface, replacing the deprecated JSON-RPC, while GraphQL RPC offers flexible reads for frontends and dashboards.
examples:
- key_count: 40
  name: All Methods
  slug: all-methods
- key_count: 3
  name: Checkpoints
  slug: checkpoints
- key_count: 5
  name: Coins
  slug: coins
- key_count: 2
  name: Events
  slug: events
- key_count: 5
  name: Move
  slug: move
- key_count: 6
  name: Objects
  slug: objects
- key_count: 3
  name: Staking
  slug: staking
- key_count: 7
  name: Transactions
  slug: transactions
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: 'The Sui GraphQL RPC is a generally available read/write interface for the Sui blockchain, backed by the Sui General-Purpose Indexer, Consistent Store, full nodes, and Archival Service. It exposes the '
  name: Sui GraphQL API
  slug: sui-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sui.png
json_schemas:
- name: Balance
  property_count: 5
  slug: Balance
- name: Checkpoint
  property_count: 11
  slug: Checkpoint
- name: Coin
  property_count: 6
  slug: Coin
- name: CommitteeInfo
  property_count: 2
  slug: CommitteeInfo
- name: DelegatedStake
  property_count: 3
  slug: DelegatedStake
- name: TransactionBlockResponse
  property_count: 12
  slug: TransactionBlockResponse
- name: Sui JSON-RPC Schemas
  property_count: 0
  slug: sui-schemas
layout: provider
modified: '2026-06-13'
name: Sui
nav: Providers
network: true
overview: 'Sui publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Coin Query API API, Extended API API, Governance Read API API, and 6 more. Tagged areas include Blockchain, Move, Web3, Cryptocurrency, and Smart Contracts.


  The Sui catalog on APIs.io includes 1 Spectral governance ruleset.


  Sui''s developer surface includes documentation, GitHub presence, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 39
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Sui API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sui-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.8
  delta: -12.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 54.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sui/refs/heads/main/screenshots/sui-2026-06-20T194741.png
security:
- kind: domain-security
  name: Sui Domain Security
  slug: sui-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sui
tags:
- Blockchain
- Move
- Web3
- Cryptocurrency
- Smart Contracts
website: https://sui.io
---
