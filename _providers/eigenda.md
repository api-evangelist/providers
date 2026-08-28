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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 1.3
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: gRPC API exposed by the EigenDA Disperser. Rollups submit raw blobs to DisperseBlob, then poll GetBlobStatus until the blob is confirmed and dispersed across the operator set. v2 adds GetBlobCommitmen
  name: EigenDA Disperser API
  slug: disperser-api
- description: gRPC service that fans out chunk requests to EigenDA operator nodes and reconstructs the original blob from the retrieved chunks via the RetrieveBlob RPC.
  name: EigenDA Retriever API
  slug: retriever-api
- description: gRPC service exposing GetBlob, GetChunks, and GetValidatorChunks against blobs stored by the relay layer. Relays sit between rollups and validators and front the read path for posted blobs.
  name: EigenDA Relay API
  slug: relay-api
- description: gRPC service that handles operator registration via the Churn RPC. The Churner decides whether new operators may join the EigenDA operator set and which existing operators are evicted when the registe
  name: EigenDA Churner API
  slug: churner-api
- description: gRPC API served by EigenDA operator nodes. Validators receive chunk dispersals from the Disperser, sign aggregated attestations, and serve chunk retrieval. v2 introduces node_v2.proto and a separate s
  name: EigenDA Validator Node API
  slug: validator-node-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Layr-Labs/eigenda/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Layr-Labs/eigenda/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Layr-Labs/eigenda/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Layr-Labs/eigenda/blob/master/docs/contributing.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eigenda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eigenda.xyz
- group: company
  title: ''
  type: Website
  url: https://eigencloud.xyz/da
- group: start
  title: ''
  type: Portal
  url: https://docs.eigencloud.xyz/products/eigenda/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.eigencloud.xyz/products/eigenda/api/disperser-v2-API/overview
- group: docs
  title: ''
  type: Documentation
  url: https://layr-labs.github.io/eigenda/
- group: company
  title: ''
  type: Blog
  url: https://www.blog.eigenlayer.xyz/intro-to-eigenda-hyperscale-data-availability-for-rollups/
- group: other
  title: ''
  type: BlobExplorer
  url: https://blobs.eigenda.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Layr-Labs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Layr-Labs/eigenda
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Layr-Labs/eigenda-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Layr-Labs/eigenda-rs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Layr-Labs/eigenda-client-rs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Layr-Labs/eigensdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Layr-Labs/eigensdk-rs
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/eigenda-proxy
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/eigenda-orbit-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/eigenda-orbit-setup-script
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/nitro
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/eigenda-operator-setup
- group: build
  title: ''
  type: Tools
  url: https://github.com/Layr-Labs/hokulea
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Layr-Labs/eigenda-examples
- group: operate
  title: ''
  type: Forums
  url: https://forum.eigenlayer.xyz/c/eigenda-research/36
- group: company
  title: ''
  type: Twitter
  url: https://x.com/eigen_da
- group: company
  title: ''
  type: Twitter
  url: https://x.com/eigenlayer
- group: operate
  title: ''
  type: Support
  url: mailto:eigenda-support@eigenlabs.org
- group: other
  title: ''
  type: Company
  url: https://www.eigenlabs.org
- group: other
  title: ''
  type: Whitepaper
  url: https://github.com/Layr-Labs/whitepaper
- group: commercial
  title: ''
  type: License
  url: https://github.com/Layr-Labs/eigenda/blob/master/LICENSE
created: '2026-05-24'
description: EigenDA is a secure, high-throughput, decentralized data availability (DA) service built on top of Ethereum using EigenLayer restaking primitives. Developed by Eigen Labs and operated as the flagship product of EigenCloud, EigenDA accepts blobs of rollup data from rollup sequencers, erasure-codes them, distributes the chunks across a network of EigenLayer-restaked operators, and produces aggregate BLS signatures that anchor data availability on Ethereum L1. The service is positioned as a hyperscale DA layer for rollups, advertising 1 GB/s of design throughput and is secured by 4M+ ETH restaked through EigenLayer with validators that include Coinbase, Google, Nethermind, and Puffer. EigenDA is consumed today by rollups and chains including Celo, MegaETH, and Aevo, with integrations available for Arbitrum Orbit, OP Stack, Nitro, and the Sovereign SDK. The protocol exposes a gRPC API surface across a Disperser (blob ingest and status), Relays (blob and chunk retrieval), Retriever
  (reconstructive retrieval), Churner (operator registration), and Validator/Node endpoints. v2 of the protocol introduces a payment vault and the GetPaymentState RPC on the Disperser, replacing per-account static throughput reservations with a programmatic payments surface. The reference implementation is open source in Go (with a Rust client and SDKs in Rust and TypeScript), licensed Apache-2.0 / MIT, and developed in the open on GitHub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eigenda.png
layout: provider
modified: '2026-05-24'
name: EigenDA
nav: Providers
network: true
overview: 'EigenDA publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Data Availability, Ethereum, Restaking, and EigenLayer.


  EigenDA''s developer surface includes developer portal, documentation, engineering blog, tooling, code examples, support, and 27 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 41.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 20.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eigenda/refs/heads/main/screenshots/eigenda-2026-06-20T180522.png
security:
- kind: domain-security
  name: Eigenda Domain Security
  slug: eigenda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eigenda
tags:
- Blockchain
- Data Availability
- Ethereum
- Restaking
- EigenLayer
- Rollups
- Layer 2
- Web3
- gRPC
- Decentralized Infrastructure
- KZG Commitments
- Cryptography
website: https://www.eigenda.xyz
---
