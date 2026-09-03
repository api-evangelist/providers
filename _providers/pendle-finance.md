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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.2
  scored_at: '2026-09-02'
api_count: 9
apis:
- description: A hosted REST API that generates ready-to-broadcast calldata for every Pendle protocol action — swap (including tokens-to-PT, PT-to-tokens, YT swaps), add and remove liquidity, ZPI (zero-price-impact)
  name: Pendle Hosted SDK API
  slug: pendle-hosted-sdk
- description: REST API for offchain Pendle data — markets, assets, prices, user positions, transactions, points, and governance. Cross-chain endpoints (`GET /v2/markets/all`, `GET /v1/assets/all`, `GET /v1/prices/a
  name: Pendle Backend Data API
  slug: pendle-backend-data-api
- description: Real-time data feeds delivered over Socket.IO from `https://api-v2.pendle.finance/pendle-v2`. Clients connect once over WebSocket and subscribe to per-feed room ids to receive order-book snapshots and
  name: Pendle Real-Time Feeds (Socket.IO)
  slug: pendle-realtime-feeds
- description: 'RouterStatic is an on-chain read-only helper contract that exposes simulation and quoting functions used by the Pendle SDK and frontend — previewing swap, mint, redeem, and liquidity outcomes without '
  name: Pendle Router Static (On-chain Helper)
  slug: pendle-router-static
- description: REST API for the Boros margin trading venue — querying markets, account positions, orders, fills, funding, and historical data, and submitting signed orders generated via the Boros SDK. Boros lets tra
  name: Pendle Boros HTTP API
  slug: boros-http-api
- description: Official TypeScript SDK (`@pendle/boros-sdk-public`) that wraps calldata generation, EIP-712 signing, the Agent trading model, and Send-Txs-Bot dispatch on top of the Boros HTTP API. Uses `viem` 2.x a
  name: Pendle Boros SDK
  slug: boros-sdk
- description: Open-source Solidity implementation of the Pendle V2 protocol — Router, MarketFactory, Market, PT, YT, vePENDLE, fee distributor, governance, and supporting libraries. Distributed on npm as `@pendle/c
  name: Pendle V2 Core Smart Contracts
  slug: pendle-core-v2-contracts
- description: Public repository of Standardized Yield (SY) wrapper contracts that adapt every supported yield-bearing asset (LSTs, LRTs, stablecoin vaults, RWA tokens, etc.) into a single ERC-20 surface that Pendle
  name: Pendle SY (Standardized Yield) Contracts
  slug: pendle-sy-contracts
- description: Open-source Solidity core for Boros — the order-book / margin venue that lets traders long or short yield rates with leverage. Contracts cover the exchange, market accounts, agent authorization, settl
  name: Pendle Boros Core Smart Contracts
  slug: boros-core-contracts
artifact_total: 45
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/pendle-finance/boros-sdk-public/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/pendle-finance/boros-sdk-public/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pendle-finance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pendle-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pendle.finance/
- group: other
  title: ''
  type: App
  url: https://app.pendle.finance
- group: other
  title: ''
  type: Boros
  url: https://boros.pendle.finance
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pendle.finance
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://docs.pendle.finance/pendle-dev
- group: docs
  title: ''
  type: BorosDocs
  url: https://docs.pendle.finance/boros-dev
- group: docs
  title: ''
  type: APIReference
  url: https://api-v2.pendle.finance/core/docs
- group: other
  title: ''
  type: Markets
  url: https://app.pendle.finance/trade/markets
- group: other
  title: ''
  type: Governance
  url: https://app.pendle.finance/vependle
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pendle-finance
- group: other
  title: ''
  type: Repository
  url: https://github.com/pendle-finance/pendle-core-v2-public
- group: company
  title: ''
  type: Blog
  url: https://medium.com/pendle
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/pendle_fi
- group: operate
  title: ''
  type: Discord
  url: https://pendle.finance/discord
- group: other
  title: ''
  type: Telegram
  url: https://t.me/pendle_info_bot
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@pendle/core-v2
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@pendle/boros-sdk-public
- group: build
  title: ''
  type: Examples
  url: https://github.com/pendle-finance/pendle-examples-public
created: '2026-05-24'
description: Pendle Finance is a decentralized yield-trading protocol that tokenizes future yield by stripping yield-bearing assets into Principal Tokens (PT) and Yield Tokens (YT) wrapped in a Standardized Yield (SY) layer. PT trades at a discount and matures one-to-one for the underlying at expiry, giving buyers a fixed yield; YT entitles holders to the variable yield until expiry, letting them long, hedge, or speculate on yield itself. Pendle V2 pairs this with a purpose-built AMM for trading time-decaying assets, and Boros extends the design into a margin venue for trading yield as a perpetual rate. The protocol is live on Ethereum, Arbitrum, BNB Chain, Optimism, Base, Mantle, Sonic, Berachain, HyperEVM, Monad, Katana, and Ink. Developer surface includes the Pendle Hosted SDK (a REST API for generating Pendle transactions), a Backend Data API for market, asset, price, and governance data, Socket.IO real-time feeds, the Boros TypeScript SDK and Boros HTTP API, vePENDLE / sPENDLE governance,
  and audited open-source Solidity contracts for V2 cores, SY wrappers, and Boros core.
features:
- description: Splits any yield-bearing asset into a Principal Token redeemable one-to-one at expiry and a Yield Token capturing every unit of yield until expiry, letting users trade the two halves independently.
  name: Yield Stripping (PT and YT)
- description: ERC-5115 inspired wrappers normalize hundreds of LSTs, LRTs, stablecoin vaults, and RWA tokens into a single token interface that Pendle V2 markets and AMM understand.
  name: Standardized Yield (SY) Wrappers
- description: Buying PT at a discount locks in a fixed APY through expiry, regardless of how the underlying floating yield evolves.
  name: Fixed Yield Trading
- description: Buying YT gives capital-efficient long exposure to floating yield without holding the principal, used to long, hedge, or speculate on yield rates.
  name: Leveraged Yield Exposure (YT)
- description: Purpose-built AMM that prices PT and YT against the underlying while accounting for time-to-expiry, supporting deep liquidity for yield trading.
  name: Time-Decay AMM
- description: Locking PENDLE into vePENDLE grants governance power, voting on gauge weights, fee share, and LP yield boosts across markets.
  name: vePENDLE Governance and Boosts
- description: Margin trading venue that turns variable yield rates into perpetual instruments with leverage, cross-margin, isolated margin, and an Agent trading model.
  name: Boros — Yield as a Perpetual
- description: Live on Ethereum, Arbitrum, BNB Chain, Optimism, Base, Mantle, Sonic, Berachain, HyperEVM, Monad, Katana, and Ink — markets and PT/YT pairs deployed per chain.
  name: Multi-Chain Deployment
- description: A single Convert endpoint generates calldata for every protocol action so integrators never have to patch a client SDK as underlying SY assets evolve.
  name: Hosted SDK for Drop-In Integration
- description: '`/v2/markets/all`, `/v1/assets/all`, and `/v1/prices/assets` return data across every supported chain in a single request, with pagination, points data, and partial-success error reporting.'
  name: Cross-Chain Backend Data
- description: Socket.IO order-book streams push snapshots every five seconds for every whitelisted market at four precision levels.
  name: Real-Time Order-Book Feeds
graphqls:
- description: Pendle Finance exposes on-chain protocol data through a Graph Protocol subgraph (`subgraph-v3`). The subgraph indexes Ethereum mainnet events from the Pendle Router and related contracts, making it po
  name: Pendle Finance GraphQL (Subgraph)
  slug: pendle-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pendle-finance.png
integrations:
- description: Mainnet deployment (chain id 1) — flagship Pendle markets and vePENDLE governance.
  name: Ethereum
- description: Arbitrum One (42161) — heavy LRT and stablecoin yield activity.
  name: Arbitrum
- description: BNB Chain (56) — Pendle markets for BNB-ecosystem yield assets.
  name: BNB Chain
- description: Optimism (10) — Pendle markets for OP-stack yield assets.
  name: Optimism
- description: Base (8453) — Coinbase L2 Pendle markets.
  name: Base
- description: Mantle (5000) — Pendle markets for Mantle-native yield assets.
  name: Mantle
- description: Sonic (146) — Pendle markets on the Sonic chain.
  name: Sonic
- description: Berachain (80094) — Pendle markets tied to BGT and PoL yield assets.
  name: Berachain
- description: HyperEVM (999) — Pendle markets on the Hyperliquid EVM.
  name: HyperEVM
- description: Monad (143) — Pendle markets on the Monad chain.
  name: Monad
- description: Katana (747474) — Pendle markets on the Katana chain.
  name: Katana
- description: Ink (57073) — Pendle markets on the Ink L2.
  name: Ink
- description: Default aggregator integrated by the Hosted SDK Convert endpoint for ZAP-in token routing.
  name: KyberSwap
- description: Required peer dependency for the Boros TypeScript SDK.
  name: viem
- description: Boros transaction-dispatch service used by the Boros SDK for signed-order delivery.
  name: Send Txs Bot
layout: provider
modified: '2026-05-24'
name: Pendle Finance
nav: Providers
network: true
overview: 'Pendle Finance publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, Yield Trading, Yield Stripping, Principal Tokens, and Yield Tokens.


  Pendle Finance''s developer surface includes documentation, API reference, engineering blog, code examples, and 18 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 42.6
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  open_source:
    applies: true
    score: 0.0
  previous_composite: 24.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pendle-finance/refs/heads/main/screenshots/pendle-finance-2026-06-20T191634.png
security:
- kind: domain-security
  name: Pendle Finance Domain Security
  slug: pendle-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pendle Finance Vulnerability Disclosure
  slug: pendle-finance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pendle-finance
tags:
- DeFi
- Yield Trading
- Yield Stripping
- Principal Tokens
- Yield Tokens
- Standardized Yield
- AMM
- Fixed Yield
- Perpetual Yield
- Ve Pendle
- Boros
- EVM
use_cases:
- description: Wrap PT purchases into a vault product that delivers a fixed APY on stablecoins or ETH-denominated LSTs until expiry.
  name: Fixed-Yield Vault
- description: Use YT to take leveraged directional positions on a specific asset's yield without holding the principal collateral.
  name: Yield Speculation Desk
- description: Stack ecosystem points (eigenlayer, ethena, etc.) by holding YT of point-bearing assets, with `/v2/markets/all` exposing per-market points metadata.
  name: Points / Airdrop Maximization
- description: Auto-rebalance liquidity across Pendle pools using the Hosted SDK Convert API for add/remove/transfer-liquidity and the Backend Data API for APY breakdown.
  name: LP Strategy Optimizer
- description: Quote-driven market-making or directional bot on Boros markets using the Boros SDK, Send-Txs Bot, and Socket.IO order-book feed.
  name: Boros Yield Trading Bot
- description: Build dashboards over Pendle positions using historical APY breakdown, transaction history, and price endpoints.
  name: DeFi Portfolio Analytics
- description: Aggregate Pendle markets across 12+ EVM chains via the cross-chain REST endpoints for unified yield discovery and routing.
  name: Cross-Chain Yield Aggregation
website: https://www.pendle.finance/
---
