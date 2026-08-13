---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 36.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Hegic Agentic Access
  operation_count: 17
  slug: hegic-agentic-access
  summary_line: 17 operations
api_count: 10
apis:
- description: Block explorer API for querying Hegic (HEGIC) token data on Arbitrum One, including token supply, holder information, transfer events, and contract interactions. The HEGIC token contract address on Ar
  name: Arbiscan Token API
  slug: arbiscan-token-api
- description: GraphQL API powered by The Graph Protocol for querying Hegic options positions, historical trades, liquidity pool states, and protocol events on Ethereum. Enables developers to query open and closed o
  name: Hegic Options Subgraph API
  slug: hegic-options-subgraph-api
- description: Hegic's core options protocol is implemented as smart contracts on Arbitrum One. Developers can interact directly with the contracts using standard JSON-RPC calls, including querying option positions,
  name: Hegic Smart Contracts (Arbitrum)
  slug: hegic-smart-contracts-arbitrum
- description: Account and holder information
  name: Hegic Accounts API
  slug: hegic-accounts-api
- description: Smart contract interactions and ABI
  name: Hegic Contracts API
  slug: hegic-contracts-api
- description: Protocol fees and revenue
  name: Hegic Fees API
  slug: hegic-fees-api
- description: Options DEX volume and analytics
  name: Hegic Options API
  slug: hegic-options-api
- description: Token price data
  name: Hegic Prices API
  slug: hegic-prices-api
- description: ERC-20 token data for HEGIC token on Arbitrum
  name: Hegic Tokens API
  slug: hegic-tokens-api
- description: Total Value Locked data for Hegic and other protocols
  name: Hegic TVL API
  slug: hegic-tvl-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hegic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hegic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hegic-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hegic.co/
- group: other
  title: ''
  type: Application
  url: https://www.hegic.co/app
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hegic
- group: other
  title: ''
  type: Analytics
  url: https://dune.com/Juan_X/hegic-herge
- group: operate
  title: ''
  type: Forums
  url: https://gov.hegic.co/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/hegic
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HegicOptions
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hegic.co/
- group: operate
  title: ''
  type: Status
  url: https://arbiscan.io/token/0x431402e8b9de9aa016c743880e04e517074d8cec
created: '2026-06-14'
description: Hegic is an on-chain peer-to-pool options trading protocol deployed on Arbitrum, enabling users to trade ETH and WBTC call and put options with AMM mechanics. Liquidity providers fund shared pools and earn premiums, while traders access non-custodial options with on-chain settlement in USDC. Protocol data including option positions, liquidity pool TVL, strike prices, premiums, open interest, and hedge contract analytics are queryable via DefiLlama's public REST API, the Arbiscan token API, and community-maintained Graph Protocol subgraphs.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Hegic is a decentralized peer-to-pool options trading protocol deployed on Ethereum and Arbitrum. The GraphQL API is served via The Graph Protocol subgraph maintained by cvauclair, indexing Hegic smar
  name: Hegic GraphQL API
  slug: hegic-graphql
image: https://hegic.co/favicon.ico
layout: provider
modified: '2026-06-14'
name: Hegic
nav: Providers
network: true
overview: 'Hegic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contracts API, Fees API, and 4 more. Tagged areas include DeFi, Options Trading, On-Chain, Arbitrum, and Ethereum.


  Hegic''s developer surface includes authentication, engineering blog, status page, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 32
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.0
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 36.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hegic/refs/heads/main/screenshots/hegic-2026-06-20T182611.png
security:
- kind: authentication
  name: Hegic Authentication
  slug: hegic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hegic Domain Security
  slug: hegic-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: hegic
tags:
- DeFi
- Options Trading
- On-Chain
- Arbitrum
- Ethereum
- Liquidity Pools
- AMM
- Derivatives
- Web3
website: https://www.hegic.co/
---
