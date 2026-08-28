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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: On-chain smart contract interface for the Sudoswap AMM protocol. Developers interact with LSSVMPairFactory to create pools, with LSSVMPair contracts to deposit/withdraw assets, and with VeryFastRouter
  name: Sudoswap Smart Contract API
  slug: sudoswap-smart-contract-api
- description: 'GraphQL subgraph deployed on The Graph that indexes sudoswap.xyz smart contract events and statistics. Enables querying of pool creation events, swap history, NFT collection liquidity, pair metadata, '
  name: Sudoswap Subgraph API
  slug: sudoswap-subgraph-api
- description: TypeScript/JavaScript SDK published on npm as sudo-defined-quoter that wraps the Defined (formerly Codex) API to retrieve bid and ask quotes for any NFT collection across multiple EVM chains. Provides
  name: Sudoswap SDK (sudo-defined-quoter)
  slug: sudoswap-sdk-sudo-defined-quoter
artifact_total: 8
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sudoswap/lssvm2/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sudoswap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sudoswap.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sudoswap.xyz/
- group: company
  title: ''
  type: Blog
  url: https://blog.sudoswap.xyz/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/sudoswap
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sudoswap
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/sudoswap
- group: operate
  title: ''
  type: FAQ
  url: https://docs.sudoswap.xyz/managing-collections/faq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sudoswap.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sudoswap.xyz/privacy
- group: operate
  title: ''
  type: Status
  url: https://github.com/sudoswap/upptime
description: Sudoswap is a minimal, gas-efficient automated market maker (AMM) protocol for NFTs that facilitates NFT-to-token swaps using customizable bonding curves. It supports ERC-721 and ERC-1155 NFTs alongside ETH and ERC-20 tokens. Liquidity providers can create single-sided buy/sell pools or dual-sided trade pools to earn fees. Developers interact with the protocol through smart contracts (LSSVMPair, VeryFastRouter, bonding curve contracts) and off-chain indexing services such as The Graph subgraph and the Defined/Codex data API. Sudoswap v2 is deployed on Ethereum mainnet, Arbitrum, Base, Berachain, Sanko, and other EVM-compatible networks.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://sudoswap.xyz/favicon.ico
jsonld:
- class_count: 0
  name: Apis Context
  property_count: 0
  slug: apis
layout: provider
modified: '2026-06-14'
name: Sudoswap
nav: Providers
network: true
overview: 'Sudoswap publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include NFT, AMM, DeFi, Liquidity, and Bonding Curves.


  The Sudoswap catalog on APIs.io includes 1 JSON-LD context.


  Sudoswap''s developer surface includes documentation, engineering blog, GitHub presence, FAQ, status page, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 4
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 16.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 21.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sudoswap/refs/heads/main/screenshots/sudoswap-2026-06-20T194636.png
security:
- kind: domain-security
  name: Sudoswap Domain Security
  slug: sudoswap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sudoswap
tags:
- NFT
- AMM
- DeFi
- Liquidity
- Bonding Curves
- ERC-721
- ERC-1155
- Ethereum
website: https://sudoswap.xyz/
---
