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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The primary HTTP REST API for CoinEx, providing access to spot trading, futures, perpetual contracts, account management, asset operations, market data, and referral endpoints. Authentication uses HMA
  name: CoinEx REST API v2
  slug: coinex-rest-api-v2
- description: Real-time WebSocket API for CoinEx spot markets. Supports streaming subscriptions for market depth, trade feeds, K-line data, and account/order updates. Responses use zip compression.
  name: CoinEx WebSocket API v2 - Spot
  slug: coinex-websocket-api-v2-spot
- description: Real-time WebSocket API for CoinEx futures and perpetual contract markets. Supports streaming subscriptions for market depth, funding rates, position updates, and order events. Responses use zip compr
  name: CoinEx WebSocket API v2 - Futures
  slug: coinex-websocket-api-v2-futures
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinex-domain-security.yml
- group: start
  title: ''
  type: Console
  url: https://www.coinex.com/en/apikey
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinex.com/api/v2/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.coinex.com/api/v2/authorization
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.coinex.com/api/v2/rate-limit
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coinex.com/api/v2/changelog
- group: other
  title: ''
  type: Fees
  url: https://www.coinex.com/en/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinex.com/en/service
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.coinex.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coinexcom
- group: start
  title: ''
  type: GitHubDemoRepo
  url: https://github.com/coinexcom/coinex_api_demo
- group: agent
  title: ''
  type: GitHubMCPServer
  url: https://github.com/coinexcom/coinex_mcp_server
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/ccxt/coinex-python
- group: build
  title: ''
  type: DotNetSDK
  url: https://www.nuget.org/packages/CoinEx.Net
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/coinex/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/coinex/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/coinex/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: CoinEx is a global cryptocurrency exchange offering REST and WebSocket APIs for spot trading, futures, perpetual contracts, market data, order management, asset operations, and sub-account administration. API v2 launched January 2024 with unified authentication, restructured endpoints, and per-second rate limiting.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinex.png
layout: provider
modified: '2026-06-13'
name: CoinEx
nav: Providers
network: true
overview: 'CoinEx publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Exchange, Spot Trading, Futures, and Perpetual Contracts.


  CoinEx''s developer surface includes developer console, documentation, authentication, changelog, GitHub presence, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 34
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 29.9
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.7
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 47.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinex/refs/heads/main/screenshots/coinex-2026-06-20T174731.png
security:
- kind: domain-security
  name: Coinex Domain Security
  slug: coinex-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Coinex Vulnerability Disclosure
  slug: coinex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coinex
tags:
- Cryptocurrency
- Exchange
- Spot Trading
- Futures
- Perpetual Contracts
- Market Data
- WebSocket
- Finance
---
