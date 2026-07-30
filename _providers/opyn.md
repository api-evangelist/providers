---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: GraphQL API powered by The Graph that indexes all on-chain Squeeth events on Ethereum mainnet. Enables developers to query oSQTH positions, short vaults, vault collateral and debt, funding (mark/index
  name: Opyn Squeeth Subgraph API
  slug: squeeth-subgraph-api
- description: GraphQL API via The Graph that indexes the Gamma Protocol (Opyn v2) on Ethereum mainnet. Covers oToken creation, option series, vault collateral, minting and burning events, settlement, and operator a
  name: Opyn Gamma Subgraph API
  slug: gamma-subgraph-api
- description: Web interface and data feed for the Crab Strategy weekly auction mechanism. The Squeeth Portal at squeethportal.xyz provides auction status, hedging queue, and rebalancing parameters used by Crab v2 a
  name: Squeeth Portal Auction API
  slug: squeeth-portal-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opyn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.opyn.co
- group: company
  title: Squeeth App
  type: Website
  url: https://squeeth.opyn.co
- group: docs
  title: ''
  type: Documentation
  url: https://opyn.gitbook.io/squeeth
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opynfinance
- group: company
  title: ''
  type: Twitter
  url: https://x.com/opyn_
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/2NFdXaE
- group: other
  title: ''
  type: Medium
  url: https://medium.com/opyn
- group: auth
  title: ''
  type: BugBounty
  url: https://immunefi.com/bounty/opyn/
- group: other
  title: ''
  type: Audits
  url: https://opyn.gitbook.io/squeeth/resources/audits-and-insurance
- group: other
  title: Controller (Mainnet)
  type: SmartContracts
  url: https://etherscan.io/address/0x64187ae08781B09368e6253F9E94951243A493D5
- group: other
  title: WPowerPerp / oSQTH (Mainnet)
  type: SmartContracts
  url: https://etherscan.io/address/0xf1B99e3E573A1a9C5E6B2Ce818b617F0E664E86B
- group: other
  title: CrabStrategyV2 (Mainnet)
  type: SmartContracts
  url: https://etherscan.io/address/0x3B960E47784150F5a63777201ee2B15253D713e8
- group: other
  title: Opyn Squeeth Subgraph (The Graph)
  type: GraphExplorer
  url: https://thegraph.com/explorer/subgraphs/Ao1QSKEQzsnNyyGKR1Faurjmkr6oNVTbgdxy6diAw9r
- group: commercial
  title: ''
  type: Plans
  url: plans/opyn-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opyn-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opyn-finops.yml
created: '2026-06-14'
description: Opyn is a DeFi options protocol on Ethereum mainnet best known for Squeeth (squared ETH), a Power Perpetual that gives traders continuous exposure to ETH² without liquidation risk on long positions. The protocol encompasses the Gamma Protocol (v2 options with cash-settled European options), the Crab Strategy (automated ETH²/ETH delta-neutral vault), Bull Strategy, and Opyn Markets (concentrated-liquidity perps). Developers integrate via The Graph GraphQL subgraph for querying squeeth positions, vault data, funding rates, and on-chain event history, combined with direct Ethereum smart-contract interaction through the Controller, Oracle, WPowerPerp, and Strategy contracts. No centralised REST API key is required; data access is permissionless through the subgraph and blockchain.
finops:
- name: Opyn Finops
  service_category: API
  slug: opyn-finops
graphqls:
- description: The Opyn Gamma Protocol GraphQL API is powered by The Graph and indexes all on-chain activity for the Opyn v2 (Gamma Protocol) options system on Ethereum mainnet. It exposes oToken creation and lifecy
  name: Opyn GraphQL API
  slug: opyn-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opyn.png
layout: provider
modified: '2026-06-14'
name: Opyn
nav: Providers
network: true
overview: 'Opyn publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Options, Ethereum, Squeeth, and Power Perpetual.


  Opyn''s developer surface includes documentation and 16 more developer resources.'
plans:
- name: Opyn Plans Pricing
  plan_count: 2
  slug: opyn-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 4
  name: Opyn Rate Limits
  slug: opyn-rate-limits
score:
  band: thin
  composite: 28.9
  delta: 8.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 43.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/opyn/refs/heads/main/screenshots/opyn-2026-06-20T191115.png
security:
- kind: domain-security
  name: Opyn Domain Security
  slug: opyn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: opyn
tags:
- DeFi
- Options
- Ethereum
- Squeeth
- Power Perpetual
- Derivatives
- Cryptocurrency
- Web3
- Smart Contracts
- Subgraph
- Crab Strategy
- Vault
website: https://www.opyn.co
---
