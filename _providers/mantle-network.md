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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-12'
api_count: 8
apis:
- description: Standard Ethereum JSON-RPC endpoint for Mantle mainnet (chain ID 5000). Used by wallets, dApps, indexers, and tooling to read chain state and submit transactions on the Mantle L2.
  name: Mantle JSON-RPC (Mainnet)
  slug: json-rpc-mainnet
- description: WebSocket endpoint for real-time JSON-RPC subscriptions on Mantle mainnet - new blocks, new pending transactions, and log subscriptions.
  name: Mantle WebSocket (Mainnet)
  slug: websocket-mainnet
- description: Standard Ethereum JSON-RPC endpoint for the Mantle Sepolia testnet, used for development, contract deployment dry runs, and integration testing.
  name: Mantle JSON-RPC (Sepolia Testnet)
  slug: json-rpc-sepolia
- description: Blockscout-based REST API behind explorer.mantle.xyz - blocks, transactions, addresses, tokens, smart-contract verification, and event log endpoints. Used by analytics dashboards and portfolio tools.
  name: Mantle Explorer API
  slug: explorer-api
- description: Canonical L1 <-> L2 bridge for ETH, MNT, ERC-20, and ERC-721 assets between Ethereum mainnet and Mantle. dApps integrate via the published Standard Bridge contracts and the Mantle SDK.
  name: Mantle Bridge
  slug: bridge
- description: TypeScript SDK for bridging MNT, ETH, ERC-20, and ERC-721 tokens between Ethereum L1 and Mantle L2. Mirrors the Optimism SDK shape and wraps the Standard Bridge contracts.
  name: Mantle SDK
  slug: mantle-sdk
- description: Mantle LSP issues mETH, a liquid staking token backed by ETH staked to Ethereum validators. Smart contracts on Ethereum L1 expose stake, unstake, and accounting functions; dApps and aggregators integr
  name: Mantle Liquid Staking Protocol (mETH)
  slug: meth-protocol
- description: Mantle's node software, forked from Optimism's OP Stack and modified to use EigenDA for data availability and a token-gas MNT model. Source for op-node, op-batcher, op-proposer, and op-geth equivalent
  name: Mantle OP Stack Fork
  slug: op-stack
artifact_total: 14
asyncapis:
- description: AsyncAPI description of the Mantle Network WebSocket JSON-RPC interface. Mantle is an EVM-compatible Ethereum Layer 2 built on a modified OP Stack with EigenDA for data availability. Its WebSocket end
  name: Mantle Network WebSocket JSON-RPC
  slug: mantle-network-asyncapi
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mantle-lsp/contracts/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/mantle-lsp/contracts/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mantle-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mantle.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mantle.xyz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mantlenetworkio
- group: other
  title: ''
  type: Explorer
  url: https://explorer.mantle.xyz/
- group: other
  title: ''
  type: Bridge
  url: https://app.mantle.xyz/bridge
- group: other
  title: ''
  type: X
  url: https://x.com/Mantle_Official
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/0xMantle
- group: company
  title: ''
  type: Blog
  url: https://www.mantle.xyz/blog/rss.xml
created: '2026-05-23'
description: Mantle is a high-performance, EVM-compatible Ethereum Layer 2 network with a modular architecture that combines an optimistic rollup execution layer with EigenDA for data availability. The ecosystem also includes Mantle Liquid Staking Protocol (mETH) and Mantle Restaked ETH. Developer surface is built on standard Ethereum JSON-RPC endpoints (mainnet and Mantle Sepolia testnet), WebSocket subscriptions, the Mantle Explorer (Blockscout-based REST API), a canonical L1 <-> L2 bridge, and standard EVM SDKs (viem, ethers, Hardhat, Foundry, Thirdweb).
finops:
- name: Mantle Network Finops
  service_category: API
  slug: mantle-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mantle-network.png
layout: provider
modified: '2026-05-29'
name: Mantle Network
nav: Providers
network: true
overview: 'Mantle Network publishes 1 API on the [APIs.io](https://apis.io/) network: Mantle WebSocket (Mainnet). Tagged areas include Layer 2, Ethereum, Rollup, EigenDA, and Liquid Staking.


  The Mantle Network catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mantle Network''s developer surface includes documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Mantle Network Plans Pricing
  plan_count: 1
  slug: mantle-network-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Mantle Network Rate Limits
  slug: mantle-network-rate-limits
rules:
- name: Mantle Network API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: mantle-network-asyncapi-spectral-rules
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 37.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mantle-network/refs/heads/main/screenshots/mantle-network-2026-06-20T184930.png
security:
- kind: domain-security
  name: Mantle Network Domain Security
  slug: mantle-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: mantle-network
tags:
- Layer 2
- Ethereum
- Rollup
- EigenDA
- Liquid Staking
- JSON-RPC
- Crypto
- Web3
website: https://www.mantle.xyz/
---
