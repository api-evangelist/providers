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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Monad Agentic Access
  operation_count: 1
  slug: monad-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 13
apis:
- description: Public Ethereum-compatible JSON-RPC endpoint for Monad mainnet (chain ID 143, native token MON). Hosted on QuickNode infrastructure with a 25 requests/sec default rate limit; alternative public endpoi
  name: Monad Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public JSON-RPC endpoint for the Monad public testnet, used for application development, integration testing, and validator software validation before deploying to mainnet.
  name: Monad Testnet JSON-RPC
  slug: testnet-rpc
- description: Full JSON-RPC method reference — standard Ethereum eth_*, net_*, web3_*, debug_*, and trace_* methods plus Monad-specific extensions and notes on method differences, rate limits, and error codes.
  name: Monad JSON-RPC API
  slug: json-rpc-api
- description: API for delegating MON to validators, querying validator stats, undelegating, and reading rewards. Backs delegation UI and external staking integrations.
  name: Monad Staking API
  slug: staking-api
- description: Protocol specification for programmable machine-to-machine payments on Monad, including account, channel, and settlement primitives.
  name: Monad Machine Payments Protocol
  slug: machine-payments-protocol
- description: Block explorer for Monad mainnet — transaction, block, contract, and token lookup with Solidity source verification.
  name: MonadVision Block Explorer
  slug: monadvision-explorer
- description: Etherscan-style Monadscan block explorer covering Monad mainnet, with transaction, address, contract, and token analytics.
  name: Monadscan Block Explorer
  slug: monadscan-explorer
- description: Socialscan instance for Monad, offering an alternative explorer view with social and on-chain identity overlays.
  name: Socialscan Monad Explorer
  slug: socialscan-explorer
- description: Monad-flavored Foundry toolkit (forge, cast, anvil) for compiling, deploying, scripting, and testing Solidity against Monad mainnet and testnet.
  name: Monad Foundry Toolkit
  slug: foundry-toolkit
- description: Registry of third-party RPC providers supporting Monad — QuickNode, Alchemy, Goldsky Edge, Ankr, MonadInfra — with rate-limit and method-availability differences documented.
  name: Monad RPC Providers
  slug: rpc-providers
- description: Indexing options for Monad data — GhostGraph (Graph-style subgraphs), QuickNode Streams, and Envio HyperIndex — for building data backends and analytics on top of Monad.
  name: Monad Indexers
  slug: indexers
- description: Token bridges and cross-chain messaging integrations for moving assets between Ethereum, other chains, and Monad.
  name: Monad Bridges
  slug: bridges
- description: The Monad JSON RPC API API from Monad — 1 operation(s) for monad json rpc api.
  name: Monad Monad JSON RPC API API
  slug: monad-monad-json-rpc-api-api
artifact_total: 20
collections:
- collection_type: open
  name: Monad JSON-RPC API
  slug: open-monad
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.monad.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monad.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.monad.xyz/developer-essentials/network-information
- group: docs
  title: ''
  type: APIReference
  url: https://docs.monad.xyz/reference/json-rpc/api
- group: other
  title: ''
  type: Playground
  url: https://docs.monad.xyz/reference/json-rpc/playground
- group: other
  title: ''
  type: App
  url: https://app.monad.xyz
- group: other
  title: ''
  type: Visualization
  url: https://gmonads.com
- group: other
  title: ''
  type: Explorer
  url: https://monadvision.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/monad-crypto
- group: company
  title: ''
  type: Blog
  url: https://www.monad.xyz/blog
- group: company
  title: ''
  type: Twitter
  url: https://x.com/monad
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/monad
- group: other
  title: ''
  type: Telegram
  url: https://t.me/monad_xyz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monad.xyz/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monad.xyz/terms
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.monad.xyz/llms.txt
created: '2026-05-23'
description: Monad is a high-performance EVM-compatible Layer 1 blockchain designed for parallel execution and pipelined consensus, targeting 10,000 TPS with 1-second block time and single-slot finality while remaining fully Ethereum bytecode-compatible. Mainnet (chain ID 143, native token MON) launched on November 24, 2025 alongside a long-running public testnet. Developer surfaces include public JSON-RPC endpoints (rpc.monad.xyz, testnet-rpc.monad.xyz), an Ethereum-compatible JSON-RPC plus Monad-specific extensions, MonadVision, Monadscan, and Socialscan explorers, native EVM tooling (Foundry, Hardhat, Remix), indexers (GhostGraph, QuickNode Streams, Envio HyperIndex), and a Staking API and Machine Payments Protocol.
finops:
- name: Monad Finops
  service_category: API
  slug: monad-finops
graphqls:
- description: Indexing options for Monad data — GhostGraph (Graph-style subgraphs), QuickNode Streams, and Envio HyperIndex — for building data backends and analytics on top of Monad.
  name: Monad GraphQL API
  slug: monad-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monad.png
layout: provider
modified: '2026-05-23'
name: Monad
nav: Providers
network: true
overview: 'Monad publishes 1 API on the [APIs.io](https://apis.io/) network: Monad JSON RPC API API. Tagged areas include Blockchain, Layer 1, EVM, High Performance, and Parallel Execution.


  Monad''s developer surface includes documentation, getting-started guide, API reference, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Monad Plans Pricing
  plan_count: 1
  slug: monad-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Monad Rate Limits
  slug: monad-rate-limits
score:
  band: developing
  composite: 44.5
  delta: 1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.4
    developer_ergonomics: 39.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monad/refs/heads/main/screenshots/monad-2026-06-20T185714.png
security:
- kind: domain-security
  name: Monad Domain Security
  slug: monad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: monad
tags:
- Blockchain
- Layer 1
- EVM
- High Performance
- Parallel Execution
- JSON-RPC
- MonadBFT
website: https://www.monad.xyz
---
