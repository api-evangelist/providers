---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Single REST API spanning Cryptocurrency endpoints (listings, quotes, OHLCV, market pairs, historical), Exchange endpoints (listings, quotes, market pairs), DEX/on-chain data (networks, dexes, spot pai
  name: CoinMarketCap Pro API
  slug: pro-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinmarketcap-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoinMarketCap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinmarketcap
- group: start
  title: ''
  type: Portal
  url: https://coinmarketcap.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://coinmarketcap.com/api/documentation/v1/
- group: commercial
  title: ''
  type: Pricing
  url: https://coinmarketcap.com/api/pricing/
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox-api.coinmarketcap.com
- group: commercial
  title: ''
  type: Plans
  url: plans/coinmarketcap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coinmarketcap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coinmarketcap-finops.yml
created: '2026-05-08'
description: CoinMarketCap is the leading crypto market data and rankings platform. The CoinMarketCap Pro API exposes 40+ REST endpoints covering cryptocurrency listings, quotes, OHLCV, exchange data, DEX/on-chain data, derivatives, global metrics, Fear and Greed index, content, and tools. Most data refreshes every 1 minute. Authentication uses an X-CMC_PRO_API_KEY header.
finops:
- name: Coinmarketcap Finops
  service_category: Crypto Market Data
  slug: coinmarketcap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinmarketcap.png
layout: provider
modified: '2026-05-08'
name: CoinMarketCap
nav: Providers
network: true
overview: 'CoinMarketCap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, Crypto, Market Data, Rankings, and DEX.


  CoinMarketCap''s developer surface includes developer portal, documentation, pricing, sandbox, and 6 more developer resources.'
plans:
- name: Coinmarketcap Plans Pricing
  plan_count: 6
  slug: coinmarketcap-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 8
  name: Coinmarketcap Rate Limits
  slug: coinmarketcap-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 26.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinmarketcap/refs/heads/main/screenshots/coinmarketcap-2026-06-20T174738.png
security:
- kind: domain-security
  name: Coinmarketcap Domain Security
  slug: coinmarketcap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinmarketcap
tags:
- Web3
- Crypto
- Market Data
- Rankings
- DEX
- Exchanges
- Cryptocurrency
website: https://coinmarketcap.com/api/
---
