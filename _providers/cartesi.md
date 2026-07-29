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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cartesi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cartesi.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cartesi.io
- group: other
  title: ''
  type: Architecture
  url: https://docs.cartesi.io/cartesi-rollups/2.0/getting-started/architecture
- group: other
  title: ''
  type: Concepts
  url: https://docs.cartesi.io/cartesi-rollups/2.0/getting-started/concepts
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cartesi.io/cartesi-rollups/2.0/api-reference
- group: other
  title: ''
  type: RollupHTTPAPI
  url: https://docs.cartesi.io/cartesi-rollups/2.0/api-reference/rollup/cartesi-rollup-http-api
- group: other
  title: ''
  type: InspectHTTPAPI
  url: https://docs.cartesi.io/cartesi-rollups/2.0/api-reference/inspect/inspect-state-http-api-for-cartesi-rollups
- group: other
  title: ''
  type: JSONRPCAPI
  url: https://docs.cartesi.io/cartesi-rollups/2.0/api-reference/jsonrpc/overview
- group: other
  title: ''
  type: CartesiMachine
  url: https://docs.cartesi.io/cartesi-machine
- group: build
  title: ''
  type: CLI
  url: https://docs.cartesi.io/get-started/cli-commands
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.cartesi.io/cartesi-rollups/2.0/tutorials/counter
- group: other
  title: ''
  type: Deployment
  url: https://docs.cartesi.io/cartesi-rollups/2.0/deployment/introduction
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cartesi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cartesi/rollups-node
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cartesi/machine-emulator
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cartesi/rollups-contracts
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cartesi/dave
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cartesi/cli
- group: other
  title: ''
  type: Foundation
  url: https://cartesi.io/foundation
- group: company
  title: ''
  type: Blog
  url: https://cartesi.io/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cartesiproject
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/pfXMwXDDfW
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/cartesi
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Cartesiproject
created: '2026-05-24'
description: Cartesi is a Linux-based optimistic rollup protocol that lets developers build decentralized applications by running rich off-chain computation inside a sandboxed Linux virtual machine. The core of the stack is the Cartesi Machine, a deterministic RISC-V emulator that boots a real Linux userland so dApps can be written in any language (Rust, Go, Python, JavaScript/TypeScript, C++) using familiar libraries, then settle results on Ethereum and other EVM chains through Cartesi Rollups smart contracts. Cartesi Rollups 2.0 is the current major version, packaging an application-specific rollup as the combination of the Cartesi Machine, the Cartesi Rollups Node middleware (Rust + Go), and a set of Solidity rollup contracts that handle settlement, consensus, and data availability. The DAVE permissionless fraud-proof system provides Stage-2 trust minimization, while the Cartesi CLI (the successor to Sunodo) packages scaffolding, build, and local devnet workflows. Cartesi is stewarded
  by The Cartesi Foundation and the CTSI token governs the network. Cartesi is fully open source under Apache-2.0 and LGPL-3.0 licenses on github.com/cartesi; there is no proprietary SaaS product, but the Rollups Node ships several developer-facing surfaces — the Rollup HTTP API used by application backends, the Inspect HTTP API for read-only queries from frontends, a GraphQL reader for advance-state inputs / outputs / vouchers / notices / reports, and a JSON-RPC node API for operations.
graphqls:
- description: ''
  name: Cartesi GraphQL API
  slug: cartesi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cartesi.png
layout: provider
modified: '2026-05-24'
name: Cartesi
nav: Providers
network: true
overview: 'Cartesi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Layer 2, Optimistic Rollups, Ethereum, and EVM.


  Cartesi''s developer surface includes documentation, API reference, CLI, GitHub presence, engineering blog, YouTube channel, and 19 more developer resources.'
random_paper: 54
score:
  band: minimal
  composite: 10.5
  delta: -1.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cartesi/refs/heads/main/screenshots/cartesi-2026-06-20T174025.png
security:
- kind: domain-security
  name: Cartesi Domain Security
  slug: cartesi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cartesi
tags:
- Blockchain
- Layer 2
- Optimistic Rollups
- Ethereum
- EVM
- RISC-V
- Linux
- Virtual Machine
- Cartesi Machine
- Rollups
- Fraud Proofs
- DAVE
- Smart Contracts
- Decentralized Applications
- Web3
- Open Source
website: https://cartesi.io
---
