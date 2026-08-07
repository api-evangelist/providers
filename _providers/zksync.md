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
  scored_at: '2026-08-06'
api_count: 10
apis:
- description: JSON-RPC endpoint for zkSync Era mainnet (chain ID 324). Implements standard eth_* methods plus zks_* extensions for L1 batch info, fee estimation, bridge contracts, paymaster params, token addresses,
  name: zkSync Era Mainnet JSON-RPC
  slug: era-mainnet-rpc
- description: JSON-RPC endpoint for the zkSync Era Sepolia testnet (chain ID 300) used for development, contract deployment, and integration testing.
  name: zkSync Era Sepolia JSON-RPC
  slug: era-sepolia-rpc
- description: WebSocket variant of the zkSync Era JSON-RPC endpoint for real-time eth_* subscriptions (newHeads, logs, pendingTransactions) and zks_* subscriptions.
  name: zkSync Era WebSocket
  slug: era-websocket
- description: TypeScript SDK built on top of ethers.js that adds zkSync-specific providers, signers, paymaster helpers, account-abstraction utilities, deposit and withdrawal flows, and contract factories.
  name: zksync-ethers SDK
  slug: zksync-ethers
- description: Official Go SDK for zkSync Era with support for transactions, EIP-712 typed data, paymasters, deposits, and withdrawals.
  name: zksync2-go SDK
  slug: zksync-go
- description: Suite of Hardhat plugins for zkSync development — compile, deploy, verify, run local nodes, upgrade contracts, and integrate with the zkVM toolchain.
  name: hardhat-zksync
  slug: hardhat-zksync
- description: Fork of Foundry (forge / cast / anvil) with first-class zkSync support for compiling, testing, scripting, and deploying contracts to zkSync Era and ZK-Stack chains.
  name: foundry-zksync
  slug: foundry-zksync
- description: Canonical cross-chain bridge between Ethereum L1 and zkSync Era for ETH and ERC-20 tokens. The Portal also exposes bridging across ZK Chains in the Elastic Network.
  name: zkSync Era Bridge
  slug: bridge
- description: Open-source framework (zksync-era + era-contracts) for deploying customizable ZK Chains that share liquidity and security through the Elastic Network shared bridge.
  name: ZK Stack
  slug: zk-stack
- description: Official Blockscout-based block explorer for zkSync Era with REST API exposing blocks, batches, transactions, addresses, contracts, and token data.
  name: zkSync Era Block Explorer API
  slug: explorer-api
artifact_total: 16
asyncapis:
- description: AsyncAPI description for the zkSync Era WebSocket JSON-RPC PubSub endpoint. zkSync Era is fully compatible with Geth's pubsub API, except for the `syncing` subscription. Clients open a WebSocket conne
  name: zkSync Era WebSocket JSON-RPC PubSub API
  slug: zksync-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zksync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zksync.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zksync.io
- group: docs
  title: ''
  type: SDKDocs
  url: https://sdk.zksync.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/matter-labs
- group: build
  title: ''
  type: GitHubSDK
  url: https://github.com/zksync-sdk
- group: start
  title: ''
  type: Portal
  url: https://portal.zksync.io
- group: other
  title: ''
  type: Explorer
  url: https://explorer.zksync.io
- group: operate
  title: ''
  type: Status
  url: https://uptime.com/s/zksync
- group: company
  title: ''
  type: Twitter
  url: https://x.com/zksync
- group: company
  title: ''
  type: TwitterDevs
  url: https://x.com/zksyncDevs
- group: operate
  title: ''
  type: Discord
  url: https://join.zksync.dev
- group: company
  title: ''
  type: Blog
  url: https://zksync.mirror.xyz
created: '2026-05-23'
description: zkSync is a family of Ethereum Layer 2 scaling networks from Matter Labs built on zero-knowledge proofs. zkSync Era is the production zkEVM rollup; the ZK Stack is the open-source framework used to deploy ZK Chains that interoperate in the Elastic Network. Developers integrate via standard JSON-RPC (with zkSync-specific extensions for paymasters, account abstraction, and L1<->L2 messaging), the zksync-ethers / zksync2-* SDKs, hardhat-zksync and foundry-zksync toolchains, the canonical Bridge, and Blockscout-based block explorers.
finops:
- name: Zksync Finops
  service_category: API
  slug: zksync-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zksync.png
layout: provider
modified: '2026-05-29'
name: zkSync
nav: Providers
network: true
overview: 'zkSync publishes 1 API on the [APIs.io](https://apis.io/) network: Era WebSocket. Tagged areas include Layer 2, Ethereum, zkEVM, ZK Rollup, and Account Abstraction.


  The zkSync catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  zkSync''s developer surface includes documentation, GitHub presence, developer portal, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Zksync Plans Pricing
  plan_count: 1
  slug: zksync-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 2
  name: Zksync Rate Limits
  slug: zksync-rate-limits
rules:
- name: zkSync API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: zksync-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 38.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zksync/refs/heads/main/screenshots/zksync-2026-06-20T201926.png
security:
- kind: domain-security
  name: Zksync Domain Security
  slug: zksync-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: zksync
tags:
- Layer 2
- Ethereum
- zkEVM
- ZK Rollup
- Account Abstraction
- Paymaster
- ZK Stack
- Bridge
website: https://zksync.io
---
