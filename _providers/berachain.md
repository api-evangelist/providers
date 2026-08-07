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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 10
apis:
- description: Public Ethereum-compatible JSON-RPC endpoint for Berachain mainnet (chain ID 80094). Supports the standard eth_* method set used by web3 clients, wallets, and indexers.
  name: Berachain Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public JSON-RPC endpoint for the Bepolia testnet (chain ID 80069), used for application development and integration testing before deploying to mainnet.
  name: Berachain Bepolia Testnet JSON-RPC
  slug: bepolia-rpc
- description: Modular consensus layer for Ethereum-based chains used by Berachain to drive validator operations and block production with single-slot finality derived from CometBFT.
  name: BeaconKit Consensus
  slug: beaconkit
- description: Primary Berachain execution client based on Reth, providing Ethereum-equivalent EVM execution and JSON-RPC for node operators.
  name: Bera-Reth Execution Client
  slug: bera-reth
- description: Berachain execution client based on Go-Ethereum, offered as a Geth-compatible alternative to Bera-Reth for node operators.
  name: Bera-Geth Execution Client
  slug: bera-geth
- description: Berachain's economic coordination layer — Reward Vaults, BGT, and validator boost contracts that turn block emissions into application liquidity rather than passive staking yield.
  name: Proof of Liquidity Protocol
  slug: proof-of-liquidity
- description: Etherscan-style block explorer for Berachain mainnet — view transactions, blocks, contracts, tokens, and verify Solidity source.
  name: Berascan Block Explorer
  slug: berascan-explorer
- description: Berascan instance for the Bepolia testnet, supporting transaction lookup and contract verification for testnet deployments.
  name: Berascan Bepolia Testnet Explorer
  slug: berascan-testnet-explorer
- description: Curated registry of RPC providers, oracles, indexers, wallets, dev IDEs, and SDK packages supported on Berachain.
  name: Berachain Developer Tools
  slug: developer-tools
- description: Registry of core protocol contract addresses on mainnet and Bepolia — Reward Vaults, BGT, HONEY, BERA wrapper, multicall, deterministic deployers, and staking-pool addresses.
  name: Berachain Deployed Contracts
  slug: deployed-contracts
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/berachain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.berachain.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.berachain.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.berachain.com/build/getting-started/common-resources
- group: docs
  title: ''
  type: APIReference
  url: https://docs.berachain.com/build/getting-started/common-resources
- group: other
  title: ''
  type: Hub
  url: https://hub.berachain.com
- group: other
  title: ''
  type: TestnetHub
  url: https://bepolia.hub.berachain.com
- group: other
  title: ''
  type: Explorer
  url: https://berascan.com
- group: other
  title: ''
  type: TestnetExplorer
  url: https://testnet.berascan.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/berachain
- group: company
  title: ''
  type: Blog
  url: https://blog.berachain.com
- group: company
  title: ''
  type: Twitter
  url: https://x.com/berachain
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/berachain
- group: other
  title: ''
  type: Telegram
  url: https://t.me/berachain
- group: operate
  title: ''
  type: Forums
  url: https://forum.berachain.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.berachain.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.berachain.com/terms
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.berachain.com/llms.txt
created: '2026-05-23'
description: Berachain is a high-performance EVM-identical Layer 1 blockchain built on BeaconKit consensus with a novel Proof-of-Liquidity (PoL) economic model that routes block rewards into productive liquidity via Reward Vaults. Mainnet launched in early 2025 (chain ID 80094) with a Bepolia testnet (chain ID 80069). Developer surfaces include public JSON-RPC at rpc.berachain.com, BeaconKit consensus client, EVM execution via Bera-Reth and Bera-Geth, Berascan block explorer, indexers (Goldsky, Envio), and dApps such as BEX (DEX) and Bend / Honey.
finops:
- name: Berachain Finops
  service_category: API
  slug: berachain-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/berachain.png
layout: provider
modified: '2026-05-23'
name: Berachain
nav: Providers
network: true
overview: 'Berachain publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Layer 1, EVM, Proof of Liquidity, and DeFi.


  Berachain''s developer surface includes documentation, getting-started guide, API reference, GitHub presence, engineering blog, and 13 more developer resources.'
plans:
- name: Berachain Plans Pricing
  plan_count: 1
  slug: berachain-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Berachain Rate Limits
  slug: berachain-rate-limits
score:
  band: emerging
  composite: 26.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 26.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/berachain/refs/heads/main/screenshots/berachain-2026-06-20T173147.png
security:
- kind: domain-security
  name: Berachain Domain Security
  slug: berachain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: berachain
tags:
- Blockchain
- Layer 1
- EVM
- Proof of Liquidity
- DeFi
- JSON-RPC
- BeaconKit
website: https://www.berachain.com
---
