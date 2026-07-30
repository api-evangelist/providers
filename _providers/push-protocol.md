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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: JavaScript/TypeScript SDK (@pushchain/core) for the Push Chain Universal Layer 1 blockchain. Exposes PushChain.initialize(signer, {network}) for client setup, pushChainClient.universal.sendTransaction
  name: Push Chain Core SDK
  slug: push-chain-sdk
- description: Push Chain is 100% EVM-compatible; developers can initialize standard Ethers v6 or Viem clients against Push Chain RPC endpoints without modifying existing Solidity ABIs, bytecodes, or on-chain logic.
  name: Push Chain EVM Client
  slug: push-chain-evm-client
- description: On-chain contract helpers deployed at 0x00000000000000000000000000000000000000eA (UEAFactory). getOriginForUEA(address) returns the UniversalAccountId and isUEA flag for any Push Chain address. getUEA
  name: Push Chain Contract Helpers (UEAFactory)
  slug: push-chain-contract-helpers
- description: Public testnet faucet at faucet.push.org for the Push Chain Donut Testnet. Delivers 1 PC (native gas token) per wallet address per 6 hours. Rate-limited and CAPTCHA-gated. Supports multi-chain testing
  name: Push Chain Testnet Faucet
  slug: push-chain-faucet
- description: 'React UI component library providing PushUniversalWalletProvider and PushUniversalAccountButton for abstracting wallet connection and universal signer creation in web applications. Supports MetaMask, '
  name: Push Chain UI Kit
  slug: push-chain-ui-kit
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/push-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://push.org
- group: start
  title: ''
  type: Portal
  url: https://push.org/docs
- group: docs
  title: ''
  type: Documentation
  url: https://push.org/docs/chain
- group: start
  title: ''
  type: GettingStarted
  url: https://push.org/docs/chain/quickstart
- group: learn
  title: ''
  type: Tutorials
  url: https://push.org/docs/chain/tutorials
- group: other
  title: ''
  type: Faucet
  url: https://faucet.push.org
- group: commercial
  title: ''
  type: Pricing
  url: https://push.org
- group: operate
  title: ''
  type: RateLimits
  url: https://push.org/docs/chain/setup/faucets
- group: commercial
  title: ''
  type: FinOps
  url: https://push.org
- group: build
  title: ''
  type: Github
  url: https://github.com/pushchain
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/pushprotocol
- group: company
  title: ''
  type: Twitter
  url: https://x.com/pushprotocol
- group: company
  title: ''
  type: Blog
  url: https://push.org/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://push.org/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://push.org/privacy
description: Push Protocol (formerly EPNS) is a Web3 communication and Layer 1 blockchain protocol that enables universal applications deployable once and accessible from any chain. Push Chain is the first true Universal Layer 1 blockchain offering 100% EVM compatibility, 4.2k TPS, 1-second native block time, and instant finality. The platform provides a JavaScript/TypeScript SDK (@pushchain/core) that wraps universal signing, cross-chain transaction routing, multichain execution, message signing, smart contract helpers, and utility functions. Developers can send universal transactions from Ethereum, Solana, BNB Chain, Base, and Arbitrum to Push Chain via a single SDK call, with fee abstraction allowing gas payment in any supported token (ETH, SOL, USDC, USDT). Push Chain also offers a testnet faucet (faucet.push.org) delivering 1 PC per address per 6 hours, and a UI Kit for React-based wallet and signer abstraction.
finops:
- name: Push Protocol Finops
  service_category: Blockchain Infrastructure
  slug: push-protocol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/push-protocol.png
layout: provider
modified: 2026-06-13 00:00:00+00:00
name: Push Protocol
nav: Providers
network: true
overview: 'Push Protocol publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, Blockchain, Layer 1, Universal Apps, and Cross-Chain.


  Push Protocol''s developer surface includes developer portal, documentation, getting-started guide, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Push Protocol Plans
  plan_count: 1
  slug: push-protocol-plans
random_paper: 63
rate_limits:
- limit_count: 3
  name: Push Protocol Rate Limits
  slug: push-protocol-rate-limits
score:
  band: emerging
  composite: 27.4
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/push-protocol/refs/heads/main/screenshots/push-protocol-2026-06-20T192317.png
security:
- kind: domain-security
  name: Push Protocol Domain Security
  slug: push-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: push-protocol
tags:
- Web3
- Blockchain
- Layer 1
- Universal Apps
- Cross-Chain
- EVM
- Solana
- Notifications
- Messaging
- Wallet Abstraction
- Fee Abstraction
- DeFi
website: https://push.org
---
