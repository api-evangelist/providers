---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-09-01'
api_count: 15
apis:
- description: Returns optimal swap routes and ready-to-sign transaction calldata across aggregated DEX liquidity. Supports Classic Swap, intent-based Fusion, and cross-chain Fusion+ flows.
  name: 1inch Swap API
  slug: swap-api
- description: Limit Order Protocol orderbook — create, query, fill, and cancel signed limit orders across supported EVM chains.
  name: 1inch Orderbook API
  slug: orderbook-api
- description: Real-time USD and reference spot prices for tokens across supported networks, sourced from on-chain liquidity.
  name: 1inch Spot Price API
  slug: price-api
- description: Token metadata, lists, search, and verification across all 1inch-supported networks.
  name: 1inch Token API
  slug: token-api
- description: Enriched token details including market metrics, price history, and trading stats for individual tokens.
  name: 1inch Token Details API
  slug: token-details-api
- description: Historical OHLCV chart data for tokens and trading pairs across supported networks.
  name: 1inch Charts API
  slug: charts-api
- description: Token balance lookups and allowance checks for any wallet across supported chains, returning balances in a unified JSON schema.
  name: 1inch Balance API
  slug: balance-api
- description: Cross-chain portfolio aggregation — wallet positions, protocol exposures, profit and loss, fees, and value over time.
  name: 1inch Portfolio API
  slug: portfolio-api
- description: Submission gateway that broadcasts signed transactions and tracks status across supported EVM chains.
  name: 1inch Transaction Gateway API
  slug: transaction-gateway-api
- description: Unified wallet transaction history across all supported chains, decoded into protocol-aware events (swaps, transfers, approvals, liquidity actions).
  name: 1inch History API
  slug: history-api
- description: Detailed transaction trace data for debugging and analytics across supported EVM chains.
  name: 1inch Traces API
  slug: traces-api
- description: Current gas-price recommendations (low / medium / high / instant) for supported EVM chains, accounting for EIP-1559 base and priority fees.
  name: 1inch Gas Price API
  slug: gas-price-api
- description: Hosted JSON-RPC endpoints for 14+ EVM and non-EVM networks, exposed through the 1inch API key for unified rate limiting and access control.
  name: 1inch Web3 RPC API
  slug: web3-rpc-api
- description: Wallet NFT holdings, collection metadata, and floor prices across supported chains.
  name: 1inch NFT API
  slug: nft-api
- description: Reverse and forward resolution for Web3 naming systems (ENS, Unstoppable Domains, and other supported registries).
  name: 1inch Domains API
  slug: domains-api
artifact_total: 21
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/1inch-a2a.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/1inch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1inch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1inch.io
- group: start
  title: ''
  type: Portal
  url: https://portal.1inch.dev
- group: docs
  title: ''
  type: Documentation
  url: https://business.1inch.com/portal/documentation
- group: build
  title: ''
  type: GitHub
  url: https://github.com/1inch
- group: company
  title: ''
  type: Twitter
  url: https://x.com/1inch
- group: company
  title: ''
  type: Blog
  url: https://blog.1inch.io
- group: agent
  title: ''
  type: LlmsText
  url: https://1inch.com/llms.txt
created: '2026-05-23'
description: 1inch is a leading DeFi aggregator providing best-execution swaps across decentralized exchanges, an intent-based Fusion order flow, cross-chain Fusion+ swaps, limit orders, and rich market data. The 1inch Developer Portal (business.1inch.com/portal) exposes 13+ REST APIs covering Swap, Orderbook, Spot Price, Token, Token Details, Charts, Balance, Portfolio, Transaction Gateway, History, Traces, Gas Price, Web3 RPC, NFT, and Domains across 14+ EVM and non-EVM chains, distributed under a single API key.
finops:
- name: 1Inch Finops
  service_category: API
  slug: 1inch-finops
graphqls:
- description: 1inch exposes on-chain DeFi data through multiple subgraphs deployed on The Graph protocol. These GraphQL APIs index Ethereum mainnet events from 1inch's Mooniswap AMM, Limit Order Protocol, and Candl
  name: 1inch GraphQL (The Graph Subgraphs)
  slug: 1inch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-23'
name: 1inch
nav: Providers
network: true
overview: '1inch publishes 15 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include DeFi, DEX Aggregator, Swap, Limit Orders, and Fusion.


  1inch''s developer surface includes developer portal, documentation, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: 1Inch Plans Pricing
  plan_count: 1
  slug: 1inch-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: 1Inch Rate Limits
  slug: 1inch-rate-limits
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 31.9
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1inch/refs/heads/main/screenshots/1inch-2026-06-20T162457.png
security:
- kind: domain-security
  name: 1Inch Domain Security
  slug: 1inch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: 1Inch Trust Center
  slug: 1inch-trust-center
  summary_line: SOC 2, ISO 27001
slug: 1inch
tags:
- DeFi
- DEX Aggregator
- Swap
- Limit Orders
- Fusion
- Web3
- RPC
- Market Data
website: https://1inch.io
---
