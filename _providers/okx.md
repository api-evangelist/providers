---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-23'
api_count: 7
apis:
- description: REST and WebSocket endpoints for order book trading, algo orders, block trading, spread trading, and copy trading across spot, futures, options, and perpetual swap instruments.
  name: OKX Trading API
  slug: okx-trading-api
- description: Public REST and WebSocket endpoints delivering real-time and historical market data including order books, tickers, candlesticks, trades, funding rates, open interest, and trading statistics.
  name: OKX Market Data API
  slug: okx-market-data-api
- description: Private endpoints for managing trading accounts, viewing balances and positions, adjusting leverage, and configuring risk settings.
  name: OKX Account API
  slug: okx-account-api
- description: Endpoints for managing asset deposits, withdrawals, and internal transfers between trading and funding accounts.
  name: OKX Funding Account API
  slug: okx-funding-account-api
- description: Endpoints for creating and managing sub-accounts, transferring assets between sub-accounts, and viewing sub-account trading activity.
  name: OKX Sub-Account API
  slug: okx-sub-account-api
- description: Endpoints for on-chain earning, staking, simple earn, and lending products available through the OKX platform.
  name: OKX Financial Products API
  slug: okx-financial-products-api
- description: Developer APIs for OKX Web3 wallet integration, including multi-chain transaction signing, DEX aggregation across 500+ DEXs on 20+ networks, and on-chain account management.
  name: OKX Wallet API (Onchain OS)
  slug: okx-wallet-api-onchain-os
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/okx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.okx.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.okx.com/docs-v5/en/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/okx
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/okxofficial
- group: company
  title: ''
  type: Blog
  url: https://www.okx.com/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.okx.com/fees
- group: operate
  title: ''
  type: StatusPage
  url: https://www.okx.com/status
- group: other
  title: ''
  type: X
  url: https://x.com/okx
- group: commercial
  title: ''
  type: Plans
  url: plans/okx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/okx-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/okx-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.okx.com/docs-v5/log_en/
- group: auth
  title: ''
  type: Authentication
  url: https://www.okx.com/docs-v5/en/#overview-api-key-creation
created: '2026-06-13'
description: Global cryptocurrency exchange providing a comprehensive REST and WebSocket API for spot and derivatives trading, account management, market data, funding, sub-account operations, block trading, and on-chain wallet services.
finops:
- name: Okx Finops
  service_category: ''
  slug: okx-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the OKX cryptocurrency exchange and Web3 platform. OKX provides a comprehensive REST and WebSocket API covering spot and derivatives trading, ac
  name: OKX Exchange GraphQL Schema
  slug: okx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/okx.png
jsonld:
- class_count: 14
  name: Okx Context
  property_count: 40
  slug: okx-context
layout: provider
modified: '2026-06-13'
name: OKX
nav: Providers
network: true
overview: 'OKX publishes 1 API on the [APIs.io](https://apis.io/) network: Trading API. Tagged areas include Cryptocurrency, Exchange, Trading, Derivatives, and Spot Trading.


  The OKX catalog on APIs.io includes 1 JSON-LD context.


  OKX''s developer surface includes documentation, engineering blog, pricing, changelog, authentication, and 9 more developer resources.'
plans:
- name: Okx Plans Pricing
  plan_count: 6
  slug: okx-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 0
  name: Okx Rate Limits
  slug: okx-rate-limits
score:
  band: thin
  composite: 42.7
  delta: -1.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.7
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/okx/refs/heads/main/screenshots/okx-2026-06-20T190651.png
security:
- kind: domain-security
  name: Okx Domain Security
  slug: okx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: okx
tags:
- Cryptocurrency
- Exchange
- Trading
- Derivatives
- Spot Trading
- Futures
- Options
- Market Data
- Web3
- Blockchain
- Wallet
website: https://www.okx.com
---
