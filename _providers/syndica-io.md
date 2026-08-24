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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.7
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: High-performance Solana JSON-RPC HTTP endpoints served from a fault-tolerant elastic-node architecture across four global regions (Northern Virginia, Oregon, London, Singapore). Supports the full stan
  name: Syndica Solana RPC (HTTP) API
  slug: syndica-solana-rpc-http-api
- description: Standard Solana RPC PubSub WebSocket service supporting accountSubscribe, programSubscribe, signatureSubscribe, slotSubscribe, blockSubscribe, logsSubscribe, and rootSubscribe. Provides a drop-in repl
  name: Syndica Solana RPC (WebSocket) API
  slug: syndica-solana-rpc-websocket-api
- description: ChainStream is Syndica's real-time Solana data streaming API. It consolidates updates from multiple validators using a "fastest wins" strategy so the subscriber benefits from the lowest-latency notifi
  name: Syndica ChainStream API
  slug: syndica-chainstream-api
- description: Sig is Syndica's open-source Solana validator client implemented in Zig, built for performance, modular RPC, and read-optimized operation. The project exposes a Solana-compatible RPC surface and is be
  name: Syndica Sig Validator RPC API
  slug: syndica-sig-validator-rpc-api
artifact_total: 40
asyncapis:
- description: 'AsyncAPI 2.6 specification for Syndica''s Solana WebSocket surface. Covers two products: 1. **Solana RPC PubSub** — JSON-RPC 2.0 subscriptions served from `wss://solana-mainnet.api.syndica.io/api-key/<'
  name: Syndica Solana RPC PubSub & ChainStream WebSocket API
  slug: syndica-io-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syndica-io-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://syndica.io
- group: start
  title: ''
  type: Portal
  url: https://syndica.io/enterprise
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syndica.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syndica.io/platform/staking/overview
- group: operate
  title: ''
  type: FAQ
  url: https://docs.syndica.io/platform/faq
- group: operate
  title: ''
  type: Support
  url: https://docs.syndica.io/platform/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.syndica.io
- group: company
  title: ''
  type: Blog
  url: https://blog.syndica.io/
- group: other
  title: ''
  type: Research
  url: https://syndica.io/research?n=library
- group: company
  title: ''
  type: AboutUs
  url: https://syndica.io/company/about-us
- group: operate
  title: ''
  type: ContactUs
  url: https://syndica.io/company/contact-us
- group: company
  title: ''
  type: Careers
  url: https://syndica.io/company/careers
- group: start
  title: ''
  type: Signup
  url: https://syndica.io/enterprise
- group: commercial
  title: ''
  type: Pricing
  url: https://syndica.io/enterprise/calculator
- group: other
  title: ''
  type: ProductPage
  url: https://syndica.io/stake
- group: other
  title: ''
  type: OpenSource
  url: https://syndica.io/open-source/sig
- group: docs
  title: ''
  type: Documentation
  url: https://sig.fun/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Syndica
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Syndica/sig
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Syndica/solana-rpc-demo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Syndica/rocksdb-zig
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/syndica-io
- group: company
  title: ''
  type: X-Twitter
  url: https://twitter.com/Syndica_io
- group: operate
  title: ''
  type: Support
  url: mailto:support@syndica.io
created: '2026-05-25T00:00:00.000Z'
description: Syndica is a Solana-only infrastructure company building developer infrastructure for Web3. Its production platform provides fault-tolerant, load-balanced Solana JSON-RPC over HTTP and WebSocket from four global regions, plus ChainStream — a real-time JSON-RPC streaming API that consolidates transaction, slot, and block updates from multiple validators using a "fastest wins" strategy with optional cross-validator verification. Syndica also operates a 0%-commission Solana staking validator running Jito-Solana for MEV optimization, publishes Solana protocol research, and develops Sig — an open-source Solana validator client written in Zig — together with companion libraries (rocksdb-zig, lsquic, boringssl-zig, zstd.zig, base58-zig) under the Apache-2.0 license.
features:
- Solana JSON-RPC over HTTP — fault-tolerant, load-balanced elastic-node architecture
- Solana JSON-RPC PubSub over WebSocket — accountSubscribe, programSubscribe, signatureSubscribe, slotSubscribe, blockSubscribe, logsSubscribe, rootSubscribe
- ChainStream real-time streaming API — transactionsSubscribe, slotsSubscribe, blocksSubscribe over WebSocket JSON-RPC 2.0 at wss://chainstream.api.syndica.io
- ChainStream "fastest wins" multi-validator consolidation for lower latency and no-miss delivery
- ChainStream `verified` parameter for cross-validator confirmation at `processed` commitment
- Edge gateway routing across four global regions — Northern Virginia, Oregon, London, Singapore
- Per-credential (API key) custom rate-limit rules — per-method, per-IP, per-credential
- Detailed observability — RPC call logging, performance metrics, usage insights, analytics dashboard
- 99.99% uptime SLA on production endpoints; billions of RPC requests served monthly
- 10M free RPC requests per month entry tier; enterprise pricing via Cost Estimator
- Open-source Sig validator client written in Zig (Apache-2.0) for read-optimized validator operation
- Solana staking validator with 0% commission, MEV optimization via Jito-Solana client
- Research arm publishing Solana protocol and consensus research
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/syndica-io.png
integrations:
- description: Drop-in replacement for `api.mainnet-beta.solana.com` HTTP and WebSocket endpoints.
  name: Solana mainnet-beta
- description: Use Syndica's RPC URL directly with `@solana/web3.js` `Connection` and `PublicKey` flows.
  name: Solana web3.js
- description: Configure `solana config set --url https://solana-mainnet.api.syndica.io/api-key/<KEY>` for CLI access.
  name: solana-cli
- description: Point Anchor's provider at a Syndica RPC URL for Solana program development.
  name: Anchor framework
- description: Mix-and-match providers — Syndica positions itself as the Solana-only specialist alongside multi-chain RPC vendors.
  name: Helius / Triton / QuickNode workflows
- description: Syndica's validator runs the Jito-Solana client for MEV-aware block production.
  name: Jito-Solana
- description: Open-source Sig validator and companion Zig libraries are developed publicly under the Syndica GitHub organization.
  name: GitHub
layout: provider
modified: '2026-05-25'
name: Syndica
nav: Providers
network: true
overview: 'Syndica publishes 2 APIs on the [APIs.io](https://apis.io/) network: Solana RPC (WebSocket) API and ChainStream API. Tagged areas include Solana, Blockchain, Web3, RPC, and Streaming.


  The Syndica catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Syndica''s developer surface includes developer portal, documentation, FAQ, support, engineering blog, signup flow, pricing, and 18 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Syndica API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: syndica-io-asyncapi-spectral-rules
score:
  band: thin
  composite: 32.2
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 32.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syndica-io/refs/heads/main/screenshots/syndica-io-2026-06-20T194826.png
security:
- kind: domain-security
  name: Syndica Io Domain Security
  slug: syndica-io-domain-security
  summary_line: TLSv1.2
slug: syndica-io
solutions:
- description: Multi-tenant Solana JSON-RPC HTTP and WebSocket endpoints with 10M free monthly requests, credential-level rate limits, and global edge routing.
  name: Solana RPC (Shared)
- description: Premium real-time Solana data streaming API consolidating updates from multiple validators with "fastest wins" routing and optional cross-validator verification.
  name: ChainStream
- description: Custom RPC capacity, dedicated nodes, ChainStream throughput, and SLA — priced via the Cost Estimator and direct sales.
  name: Enterprise / Dedicated
- description: Delegate SOL to the Syndica validator (0% commission, Jito-Solana, MEV optimization) with full self-custody.
  name: Staking
- description: Syndica's open-source Zig Solana validator client, plus companion libraries — free to use and contribute to.
  name: Sig (Open Source)
- description: Syndica Research Library — public protocol and consensus research alongside the Research Blog tag.
  name: Research
tags:
- Solana
- Blockchain
- Web3
- RPC
- Streaming
- Infrastructure
- Validator
- Staking
use_cases:
- description: Power on-chain trading bots, market makers, and liquidation engines with low-latency ChainStream notifications — production users have cut limit-order time-to-fill from 10s to 300ms.
  name: High-frequency Solana trading
- description: Stream account, program, and signature updates for AMMs, perps, and lending protocols without running self-hosted validator infrastructure.
  name: DEX and DeFi backends
- description: Serve high-volume getAccountInfo, getTransaction, and getSignaturesForAddress traffic from Syndica's load-balanced HTTP RPC fleet.
  name: Wallet and explorer infrastructure
- description: Continuously ingest Solana transactions, slots, and blocks via ChainStream into ClickHouse, BigQuery, or self-hosted Postgres for analytics.
  name: Indexers and data warehouses
- description: Subscribe to program-derived account changes for real-time mint, list, sale, and bid detection.
  name: NFT mint and marketplace tooling
- description: Delegate SOL to the Syndica validator (0% commission, Jito-Solana client, MEV optimization) for self-custody staking rewards.
  name: Solana staking
- description: Build on top of, or contribute to, Sig — Syndica's open-source Zig validator client — and consume its companion libraries (rocksdb-zig, lsquic, boringssl-zig).
  name: Solana protocol R&D
website: https://syndica.io
---
