---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The HTX Spot REST API provides HTTP access to reference data (system status, symbols, currencies, chains), market data (klines, tickers, depth, trades, 24h summaries), account and balance information,
  name: HTX Spot REST API
  slug: htx-spot-api
- description: The HTX WebSocket API provides a two-way real-time channel for subscribing to market data (klines, market depth, trade detail, best bid/offer) and to authenticated account and order update topics. Pub
  name: HTX WebSocket API
  slug: htx-websocket-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://htx.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.htx.com/en-us/opend/
- group: docs
  title: ''
  type: Documentation
  url: https://www.htx.com/en-us/opend/newApiPages/
- group: docs
  title: ''
  type: APIReference
  url: https://huobiapi.github.io/docs/spot/v1/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.htx.com/support/360000203002
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HuobiRDCenter
- group: operate
  title: ''
  type: Support
  url: https://www.htx.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.htx.com/support/360000298561/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.htx.com/en-us/about/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://www.htx.com/en-us/register/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/htx-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/htx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/htx-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/htx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/htx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/htx-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/htx-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/htx-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/htx-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/htx-domain-security.yml
created: '2026-07-17'
description: HTX (formerly Huobi Global) is a cryptocurrency exchange founded in 2013 that offers spot trading, futures and derivatives, margin trading, trading bots, copy trading, and earn/staking products across BTC, ETH, XRP and 600+ digital assets. HTX exposes a public developer platform (HTX Open Platform) with a REST API and a WebSocket streaming API covering market data, account and wallet management, sub-user administration, spot and conditional order placement, and cross/isolated margin lending. Requests are authenticated with an AccessKey and an HMAC-SHA256 (Signature Version 2) request signature. Official client SDKs are published under the HuobiRDCenter GitHub organization for Java, Python, Go, C++ and C#, with separate contract/futures variants. HTX was surfaced as a portfolio company of Hongshan (formerly Sequoia Capital China).
image: https://www.htx.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: HTX
nav: Providers
network: true
overview: 'HTX publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Cryptocurrency, Crypto Exchange, and Trading.


  HTX''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 13 more developer resources.'
random_paper: 16
rate_limits:
- limit_count: 0
  name: Htx Rate Limits
  slug: htx-rate-limits
score:
  band: thin
  composite: 31.1
  delta: -2.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 79.6
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 33.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/htx/refs/heads/main/screenshots/htx-2026-07-25T221552.png
security:
- kind: authentication
  name: Htx Authentication
  slug: htx-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Htx Domain Security
  slug: htx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: htx
tags:
- Company
- Technology
- Cryptocurrency
- Crypto Exchange
- Trading
- Digital Assets
- Blockchain
- Financial Services
- Market Data
- WebSocket
website: https://htx.com
---
