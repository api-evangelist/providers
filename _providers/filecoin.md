---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Public, load-balanced Lotus node endpoint hosted by Glif providing read-only access to the Filecoin mainnet JSON-RPC API, including all Filecoin and Ethereum-compatible RPC methods. Supports MPoolPush
  name: Filecoin Glif Lotus JSON-RPC API
  slug: filecoin-glif-lotus-json-rpc-api
- description: Glif-hosted public Lotus node endpoint for the Filecoin Calibration testnet. Provides the same read-only JSON-RPC surface as mainnet, including Filecoin and Ethereum-compatible RPC methods, for develo
  name: Filecoin Calibration Testnet Glif API
  slug: filecoin-calibration-testnet-glif-api
- description: OpenAPI-specified HTTP REST interface for Filecoin nodes, covering chain resources (tipsets, blocks, executed messages), actor management, payment channels, storage market asks, and storage deal initi
  name: Filecoin HTTP REST API
  slug: filecoin-http-rest-api
- description: Built-in actor method interface exposed through Filecoin Virtual Machine (FVM). Covers Account, Datacap, Miner, Multisig, Storage Market, Storage Power, and Verified Registry actors. Used for on-chain
  name: Filecoin Protocol Actor API
  slug: filecoin-protocol-actor-api
- description: High-level TypeScript SDK and API for the Filecoin Onchain Cloud — a smart-contract-based marketplace providing programmable, verifiable storage with cryptographic Proof-of-Data Possession (PDP) and a
  name: Filecoin Onchain Cloud Synapse API
  slug: filecoin-onchain-cloud-synapse-api
- description: RESTful JSON API for discovering and evaluating Filecoin storage providers (miners). Returns reputation scores, geographic distribution, pricing, verified deal history, and uptime metrics to help clie
  name: Filrep.io Storage Provider API
  slug: filrepio-storage-provider-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Collection
  slug: open-actors
- collection_type: open
  name: API Collection
  slug: open-chain
- collection_type: open
  name: API Collection
  slug: open-control
- collection_type: open
  name: API Collection
  slug: open-market
- collection_type: open
  name: API Collection
  slug: open-payment_channels
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filecoin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/filecoin-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: https://github.com/api-evangelist/filecoin/blob/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://github.com/api-evangelist/filecoin/blob/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://github.com/api-evangelist/filecoin/blob/main/finops/finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/filecoin-project
- group: build
  title: ''
  type: GitHub Glif
  url: https://github.com/glifio
- group: docs
  title: ''
  type: Documentation
  url: https://docs.filecoin.io/
- group: docs
  title: ''
  type: Protocol Specification
  url: https://spec.filecoin.io/
- group: company
  title: ''
  type: Blog
  url: https://filecoin.io/blog/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/filecoin
- group: operate
  title: ''
  type: Slack
  url: https://filecoin.io/slack
- group: operate
  title: ''
  type: Status
  url: https://status.filecoin.io/
description: Filecoin is the world's largest decentralized storage network, providing cryptographically verifiable storage backed by a global network of storage providers. Developers can query storage deals, retrieval markets, miners, blocks, and Filecoin+ verified storage operations through the Glif-hosted Lotus JSON-RPC API and the Filecoin HTTP REST API. The network also exposes protocol-level actors (Miner, Market, Datacap, Verified Registry, Storage Power) through built-in actor methods, and offers high-level storage onramps such as Filecoin Onchain Cloud (Synapse SDK) and S3-compatible Fil One storage.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://filecoin.io/favicon.ico
jsonld:
- class_count: 0
  name: Filecoin Context
  property_count: 0
  slug: filecoin
layout: provider
modified: '2026-06-13'
name: Filecoin
nav: Providers
network: true
overview: 'Filecoin publishes 1 API on the [APIs.io](https://apis.io/) network: HTTP REST API. Tagged areas include Decentralized Storage, Web3, IPFS, Blockchain, and Storage Deals.


  The Filecoin catalog on APIs.io includes 1 JSON-LD context.


  Filecoin''s developer surface includes authentication, documentation, engineering blog, status page, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 1
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 32.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filecoin/refs/heads/main/screenshots/filecoin-2026-06-20T181204.png
security:
- kind: authentication
  name: Filecoin Authentication
  slug: filecoin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Filecoin Domain Security
  slug: filecoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: filecoin
tags:
- Decentralized Storage
- Web3
- IPFS
- Blockchain
- Storage Deals
- Filecoin+
- FVM
website: https://filecoin.io/
---
