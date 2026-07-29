---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Pancakeswap Agentic Access
  operation_count: 10
  slug: pancakeswap-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 13
apis:
- description: GraphQL subgraph for querying PancakeSwap V2 exchange data on BNB Smart Chain, including swaps, liquidity pools, trading pairs, volume, and price history. Hosted on NodeReal MegaNode API Marketplace.
  name: PancakeSwap Exchange V2 Subgraph (BSC)
  slug: pancakeswap-exchange-v2-subgraph-bsc
- description: GraphQL subgraph for querying PancakeSwap V2 exchange data on Ethereum mainnet, including swaps, liquidity pools, pairs, and historical volume data hosted on The Graph decentralized network.
  name: PancakeSwap Exchange V2 Subgraph (Ethereum)
  slug: pancakeswap-exchange-v2-subgraph-ethereum
- description: GraphQL subgraph for querying PancakeSwap V3 concentrated liquidity exchange data on BNB Smart Chain, including positions, pools, ticks, swaps, and fee tiers. Hosted on The Graph and NodeReal.
  name: PancakeSwap Exchange V3 Subgraph (BSC)
  slug: pancakeswap-exchange-v3-subgraph-bsc
- description: GraphQL subgraph for querying PancakeSwap V3 concentrated liquidity exchange data on Ethereum mainnet, including positions, pools, swaps, and historical volume data hosted on The Graph decentralized n
  name: PancakeSwap Exchange V3 Subgraph (Ethereum)
  slug: pancakeswap-exchange-v3-subgraph-ethereum
- description: GraphQL subgraph for querying PancakeSwap StableSwap pools on BNB Smart Chain, providing stable coin pair liquidity, swap volumes, and pool statistics for low-slippage stablecoin trading pairs.
  name: PancakeSwap StableSwap Subgraph (BSC)
  slug: pancakeswap-stableswap-subgraph-bsc
- description: GraphQL subgraph for querying PancakeSwap NFT Market data on BNB Smart Chain, including NFT collections, listings, sales, bids, and trading history for the PancakeSwap NFT marketplace.
  name: PancakeSwap NFT Market Subgraph
  slug: pancakeswap-nft-market-subgraph
- description: GraphQL subgraph for querying PancakeSwap yield farming data via MasterChef V3 on BNB Smart Chain, including active farms, CAKE emission rates, staking positions, and farm APR data for V3 concentrated
  name: PancakeSwap MasterChef V3 Subgraph
  slug: pancakeswap-masterchef-v3-subgraph
- description: The Leaderboard API from PancakeSwap — 2 operation(s) for leaderboard.
  name: PancakeSwap Leaderboard API
  slug: pancakeswap-leaderboard-api
- description: The Miscellaneous API from PancakeSwap — 1 operation(s) for miscellaneous.
  name: PancakeSwap Miscellaneous API
  slug: pancakeswap-miscellaneous-api
- description: The Pairs API from PancakeSwap — 1 operation(s) for pairs.
  name: PancakeSwap Pairs API
  slug: pancakeswap-pairs-api
- description: The Summary API from PancakeSwap — 1 operation(s) for summary.
  name: PancakeSwap Summary API
  slug: pancakeswap-summary-api
- description: The Tokens API from PancakeSwap — 2 operation(s) for tokens.
  name: PancakeSwap Tokens API
  slug: pancakeswap-tokens-api
- description: The Users API from PancakeSwap — 3 operation(s) for users.
  name: PancakeSwap Users API
  slug: pancakeswap-users-api
artifact_total: 27
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pancakeswap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pancakeswap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pancakeswap.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pancakeswap.finance
- group: docs
  title: ''
  type: Documentation
  url: https://developer.pancakeswap.finance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pancakeswap
- group: company
  title: ''
  type: Blog
  url: https://blog.pancakeswap.finance
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PancakeSwap
- group: other
  title: ''
  type: Telegram
  url: https://t.me/PancakeSwap
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/pancakeswap
- group: other
  title: ''
  type: Reddit
  url: https://reddit.com/r/pancakeswap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pancakeswap.finance/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pancakeswap.finance/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pancakeswap.finance
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/pancakeswap/pancake-frontend
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/pancakeswap/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/pancakeswap/refs/heads/main/rate-limits/rate-limits.yml
- group: other
  title: ''
  type: FinancialOperations
  url: https://raw.githubusercontent.com/api-evangelist/pancakeswap/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: PancakeSwap is the largest decentralized exchange (DEX) on BNB Chain, operating across ten blockchains including Ethereum, Arbitrum, Base, Solana, zkSync, Linea, Polygon zkEVM, opBNB, and Aptos. It provides REST and GraphQL APIs for accessing token prices, liquidity pool data, swap routing, farm yields, trading pair statistics, NFT market data, and prediction markets. Developers can query on-chain data via hosted subgraphs on The Graph Protocol and NodeReal.
examples:
- key_count: 2
  name: Get Pairs Response
  slug: get-pairs-response
- key_count: 2
  name: Get Tokens Response
  slug: get-tokens-response
- key_count: 5
  name: Get User Profile Response
  slug: get-user-profile-response
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: 'PancakeSwap exposes on-chain DeFi data through GraphQL subgraphs hosted on The Graph Protocol and NodeReal. The primary subgraph is the Exchange V3 subgraph, which indexes concentrated liquidity pool '
  name: PancakeSwap GraphQL API
  slug: pancakeswap-graphql
image: https://pancakeswap.finance/logo.png
json_schemas:
- name: PancakeSwap Trading Pair
  property_count: 12
  slug: pair
- name: PancakeSwap Token
  property_count: 4
  slug: token
- name: PancakeSwap User Profile
  property_count: 5
  slug: user-profile
jsonld:
- class_count: 6
  name: Pancakeswap Context
  property_count: 6
  slug: pancakeswap
layout: provider
modified: '2026-06-13'
name: PancakeSwap
nav: Providers
network: true
overview: 'PancakeSwap publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Leaderboard API, Miscellaneous API, Pairs API, and 3 more. Tagged areas include DeFi, DEX, BNB Chain, Decentralized Exchange, and Blockchain.


  The PancakeSwap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PancakeSwap''s developer surface includes documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 60
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: PancakeSwap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pancakeswap-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.6
  delta: -3.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pancakeswap/refs/heads/main/screenshots/pancakeswap-2026-06-20T191335.png
security:
- kind: domain-security
  name: Pancakeswap Domain Security
  slug: pancakeswap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pancakeswap
tags:
- DeFi
- DEX
- BNB Chain
- Decentralized Exchange
- Blockchain
- Swap
- Liquidity
- Yield Farming
- NFT
- Web3
website: https://pancakeswap.finance
---
