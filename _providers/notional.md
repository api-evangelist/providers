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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: GraphQL subgraph API for querying Notional V2 on-chain data on Ethereum Mainnet via The Graph protocol. Provides access to accounts, trades, markets, nTokens, cash groups, currencies, TVL history, exc
  name: Notional V2 Subgraph API (Mainnet)
  slug: notional-v2-subgraph-api-mainnet
- description: GraphQL subgraph API for querying Notional V3 on-chain data on Ethereum Mainnet via The Graph Studio. Supports queries for accounts, leveraged vault positions, fCash markets, interest rates, and yield
  name: Notional V3 Subgraph API (Mainnet)
  slug: notional-v3-subgraph-api-mainnet
- description: GraphQL subgraph API for querying Notional V3 on-chain data on Arbitrum One via The Graph Studio. Notional V3 launched primarily on Arbitrum and this endpoint provides the most comprehensive V3 datase
  name: Notional V3 Subgraph API (Arbitrum)
  slug: notional-v3-subgraph-api-arbitrum
- description: Client-side Typescript SDK for interacting with Notional Finance smart contracts. Provides helper methods for computing fixed-rate trade values including getCashAmountGivenfCashAmount, getfCashAmountG
  name: Notional Typescript SDK
  slug: notional-typescript-sdk
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/notional-finance/sdk-v2/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/notional-finance/sdk-v2/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/notional-finance/sdk-v2/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notional-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://notional.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notional.finance/developer-documentation/
- group: docs
  title: ''
  type: V3Documentation
  url: https://docs.notional.finance/v3-technical-docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/notional-finance
- group: company
  title: ''
  type: Blog
  url: https://blog.notional.finance/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/notional
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/NotionalFinance
- group: other
  title: ''
  type: SmartContracts
  url: https://docs.notional.finance/developer-documentation/on-chain/notional-proxy
- group: docs
  title: ''
  type: ABIReference
  url: https://docs.notional.finance/developer-documentation/on-chain/notional-abi-reference.md
- group: docs
  title: ''
  type: SubgraphReference
  url: https://docs.notional.finance/developer-documentation/off-chain/subgraph-reference
created: '2026-06-14'
description: Notional Finance is a fixed-rate, fixed-term DeFi lending and borrowing protocol built on Ethereum and Arbitrum. The protocol enables users to lend and borrow crypto assets at predetermined interest rates using fCash, a zero-coupon bond instrument that represents a fixed cash flow at maturity. Notional V3 introduced leveraged vaults and expanded yield strategies, making it DeFi's leading fixed-rate lending platform with tenors ranging from three months to twenty years.
graphqls:
- description: Notional Finance exposes protocol data via GraphQL subgraphs hosted on The Graph protocol. The V2 subgraph covers Ethereum Mainnet fixed-rate lending/borrowing markets, accounts, fCash assets, cash ma
  name: Notional Finance GraphQL API
  slug: notional-graphql
image: https://notional.finance/favicon.ico
layout: provider
modified: '2026-06-14'
name: Notional Finance
nav: Providers
network: true
overview: 'Notional Finance publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Fixed-Rate Lending, Blockchain, Ethereum, and Arbitrum.


  Notional Finance''s developer surface includes documentation, GitHub presence, engineering blog, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notional/refs/heads/main/screenshots/notional-2026-06-20T190428.png
security:
- kind: domain-security
  name: Notional Domain Security
  slug: notional-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: notional
tags:
- DeFi
- Fixed-Rate Lending
- Blockchain
- Ethereum
- Arbitrum
- fCash
- Liquidity Pools
- Leveraged Vaults
- Yield
- Web3
website: https://notional.finance/
---
