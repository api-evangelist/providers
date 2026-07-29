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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Celestia Agentic Access
  operation_count: 10
  slug: celestia-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 10
apis:
- description: JSON-RPC methods in the blob module of celestia-node. Submit blobs to one or more namespaces with blob.Submit, retrieve them by height with blob.Get and blob.GetAll, generate inclusion proofs with blo
  name: Celestia Node Blob API
  slug: celestia-blob-api
- description: JSON-RPC methods in the header module of celestia-node. Query ExtendedHeaders with header.LocalHead, header.NetworkHead, header.GetByHeight, header.GetByHash, and header.GetRangeByHeight; track sync s
  name: Celestia Node Header API
  slug: celestia-header-api
- description: JSON-RPC methods in the da module of celestia-node implementing the modular Data Availability interface used by Rollkit, Optimism Alt-DA, Arbitrum Nitro DAS, and other rollup frameworks. Exposes da.Su
  name: Celestia Node DA API
  slug: celestia-da-api
- description: JSON-RPC methods in the share module of celestia-node. Provides direct access to Celestia's share-level data, the extended data square (EDS), namespaced shares, and share proofs via share.SharesAvaila
  name: Celestia Node Share API
  slug: celestia-share-api
- description: JSON-RPC methods in the state module of celestia-node. Exposes state-level operations including account balances, transfers, delegations, and most importantly state.SubmitPayForBlob, the canonical ent
  name: Celestia Node State API
  slug: celestia-state-api
- description: JSON-RPC methods in the das module of celestia-node. Operational introspection over the Data Availability Sampling subsystem that light nodes run to probabilistically verify block data availability. E
  name: Celestia Node DAS API
  slug: celestia-das-api
- description: JSON-RPC methods in the fraud module of celestia-node. Exposes fraud proof retrieval and subscription for the BadEncoding fraud proof type used to slash bridge nodes that propagate incorrectly erasure
  name: Celestia Node Fraud API
  slug: celestia-fraud-api
- description: JSON-RPC methods in the p2p module of celestia-node. libp2p-level introspection and control over the Celestia DA network including peer info, NAT status, connection management, bandwidth stats, pubsub
  name: Celestia Node P2P API
  slug: celestia-p2p-api
- description: JSON-RPC methods in the node module of celestia-node. Provides administrative introspection over the running node including node.Info, node.Ready, node.LogLevelSet, and the auth-token issuance methods
  name: Celestia Node Admin API
  slug: celestia-node-api
- description: JSON-RPC methods in the blobstream module of celestia-node. Generates inclusion proofs against Blobstream data commitments so EVM chains can verify, via the Blobstream(X) bridge contracts, that a give
  name: Celestia Node Blobstream API
  slug: celestia-blobstream-api
artifact_total: 56
collections:
- collection_type: open
  name: Celestia Node Blob API
  slug: open-celestia-blob-api
- collection_type: open
  name: Celestia Node Blobstream API
  slug: open-celestia-blobstream-api
- collection_type: open
  name: Celestia Node DA API
  slug: open-celestia-da-api
- collection_type: open
  name: Celestia Node DAS API
  slug: open-celestia-das-api
- collection_type: open
  name: Celestia Node Fraud API
  slug: open-celestia-fraud-api
- collection_type: open
  name: Celestia Node Header API
  slug: open-celestia-header-api
- collection_type: open
  name: Celestia Node Admin API
  slug: open-celestia-node-api
- collection_type: open
  name: Celestia Node P2P API
  slug: open-celestia-p2p-api
- collection_type: open
  name: Celestia Node Share API
  slug: open-celestia-share-api
- collection_type: open
  name: Celestia Node State API
  slug: open-celestia-state-api
- collection_type: open
  name: Celestia Node Subscriptions
  slug: open-celestia-subscriptions-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/celestia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celestia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/celestia-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://celestia.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celestia.org
- group: docs
  title: ''
  type: Documentation
  url: https://node-rpc-docs.celestia.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celestia.org/learn/celestia-101/data-availability/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.celestia.org/build/quick-start
- group: company
  title: ''
  type: Blog
  url: https://blog.celestia.org
- group: operate
  title: ''
  type: Forums
  url: https://forum.celestia.org
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/YsnTPcSfWQ
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CelestiaOrg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celestiaorg
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-openrpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/celestia-node-client-rs
- group: build
  title: ''
  type: SDKs
  url: https://docs.rs/celestia-rpc
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celestiaorg/lumina
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/nmt
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/rsmt2d
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/go-square
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/blobstream-contracts
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/orchestrator-relayer
- group: docs
  title: ''
  type: Specification
  url: https://github.com/celestiaorg/celestia-specs
- group: docs
  title: ''
  type: Specification
  url: https://github.com/celestiaorg/CIPs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/celestiaorg/docs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/celestiaorg/awesome-celestia
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/celestiaorg/networks
- group: build
  title: ''
  type: Tools
  url: https://github.com/celestiaorg/helm-charts
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-05-24T00:00:00.000Z'
description: Celestia is the first production modular data availability blockchain. It separates consensus and data availability from execution and settlement, letting rollups, sovereign chains, and other execution layers post their transaction data as blobs to Celestia under namespaces while running their own state machines. Light nodes use Data Availability Sampling and Namespaced Merkle Trees to verify availability without downloading full blocks, and the Blobstream / Blobstream X bridge attests Celestia data commitments on Ethereum and other EVM chains. The reference stack — celestia-app (consensus, Cosmos SDK + CometBFT) and celestia-node (DA bridge/full/ light nodes) — exposes a JSON-RPC API with nine modules (blob, header, share, state, das, fraud, p2p, node, da, blobstream), plus a modular DA interface used by Rollkit, Optimism Alt-DA, Arbitrum Nitro DAS, and other rollup frameworks.
examples:
- key_count: 4
  name: Celestia Blob Get Example
  slug: celestia-blob-get-example
- key_count: 4
  name: Celestia Blob Submit Example
  slug: celestia-blob-submit-example
- key_count: 4
  name: Celestia Da Submit Example
  slug: celestia-da-submit-example
- key_count: 4
  name: Celestia Header Getbyheight Example
  slug: celestia-header-getbyheight-example
- key_count: 4
  name: Celestia Share Getnamespacedata Example
  slug: celestia-share-getnamespacedata-example
- key_count: 4
  name: Celestia State Submitpayforblob Example
  slug: celestia-state-submitpayforblob-example
features:
- First production modular data availability layer; separates consensus + DA from execution and settlement
- Mainnet Beta launched October 2023; chain id celestia
- Mocha-4 public testnet and Arabica devnet for application developers
- PayForBlobs (MsgPayForBlobs) transactions for publishing namespaced blob data
- Namespaced Merkle Trees (NMT) so each rollup only downloads data for its namespace
- 2D Reed-Solomon erasure coding over the extended data square (EDS)
- Data Availability Sampling (DAS) lets light nodes verify availability without downloading full blocks
- Bridge, full, and light celestia-node modes
- JSON-RPC over HTTP (default :26658) with bearer-token auth and four permission scopes (public, read, write, admin)
- WebSocket subscriptions for blob.Subscribe, header.Subscribe, fraud.Subscribe
- Modular DA interface (da.*) compatible with Rollkit, Optimism Alt-DA, Arbitrum Nitro DAS, OP-Succinct, Kona, Hana
- celestia-app exposes Cosmos SDK gRPC (:9090), REST (:1317), and CometBFT RPC (:26657) for consensus-level queries
- Blobstream and Blobstream X bridge to Ethereum and EVM chains for cross-chain data root verification
- Lumina Rust+Wasm light node runs in the browser
- Funded by TIA staking and PayForBlobs gas fees; no central API key or commercial pricing tier
- Reference implementations in Go (celestia-node, celestia-app) and Rust (lumina, celestia-rpc)
- Apache-2.0 licensed across the celestia-node, celestia-app, celestia-core, and tooling repos
- Active CIP (Celestia Improvement Proposal) process for protocol governance
- Ecosystem rollups include Manta Pacific, Eclipse, Movement, Lightlink, Polygon CDK Validium, Astria, Hyperliquid (DA usage), and many more
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celestia.png
json_schemas:
- name: Celestia Blob
  property_count: 6
  slug: celestia-blob
- name: Celestia Extended Header
  property_count: 4
  slug: celestia-extended-header
- name: Celestia Namespace
  property_count: 3
  slug: celestia-namespace
json_structures:
- name: Celestia Blob Structure
  property_count: 6
  slug: celestia-blob-structure
jsonld:
- class_count: 39
  name: Celestia Context
  property_count: 0
  slug: celestia-context
layout: provider
modified: '2026-05-30'
name: celestia
nav: Providers
network: true
overview: 'celestia publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Node Blob API, Node Header API, Node DA API, and 7 more.


  The celestia catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  celestia''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, tooling, code examples, and 26 more developer resources.'
random_paper: 52
rules:
- name: celestia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: celestia-jsonschema-spectral-rules
- name: celestia API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 4
  slug: celestia-rules
score:
  band: thin
  composite: 40.6
  delta: -4.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 64.2
    developer_ergonomics: 56.5
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/celestia/refs/heads/main/screenshots/celestia-2026-06-20T174212.png
security:
- kind: authentication
  name: Celestia Authentication
  slug: celestia-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Celestia Domain Security
  slug: celestia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: celestia
website: https://celestia.org
---
