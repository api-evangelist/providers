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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Bithumb Agentic Access
  operation_count: 19
  slug: bithumb-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 6
apis:
- description: Real-time WebSocket API for streaming market data including tickers, order books, and trade executions, as well as authenticated streams for personal order updates and account changes.
  name: Bithumb WebSocket API
  slug: bithumb-websocket-api
- description: Asset account management
  name: Bithumb Account API
  slug: bithumb-account-api
- description: Server time and configuration
  name: Bithumb General API
  slug: bithumb-general-api
- description: Public spot market data endpoints
  name: Bithumb Market Data API
  slug: bithumb-market-data-api
- description: Authenticated spot order management
  name: Bithumb Spot Trading API
  slug: bithumb-spot-trading-api
- description: Deposit and withdrawal history
  name: Bithumb Wallet API
  slug: bithumb-wallet-api
artifact_total: 18
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bithumb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bithumb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bithumb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bithumb.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.bithumb.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.bithumb.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.bithumb.com/changelog
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bithumb-pro/bithumb.pro-official-api-docs
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.bithumb.com/docs/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.bithumb.com/u1/US139
- group: company
  title: ''
  type: Blog
  url: https://rss.blog.naver.com/bithumb_official.xml
created: '2026-06-13'
description: Bithumb is South Korea's leading cryptocurrency exchange platform offering REST and WebSocket APIs for spot trading across KRW, BTC, and USDT markets. The APIs cover market data, order management, account management, deposit and withdrawal operations, and real-time streaming for 396+ cryptocurrencies.
examples:
- key_count: 4
  name: Get Orderbook
  slug: get-orderbook
- key_count: 4
  name: Get Ticker
  slug: get-ticker
- key_count: 4
  name: Place Order
  slug: place-order
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bithumb.png
json_schemas:
- name: Bithumb Spot Order
  property_count: 11
  slug: order
- name: Bithumb Spot Ticker
  property_count: 6
  slug: ticker
layout: provider
modified: '2026-06-13'
name: Bithumb
nav: Providers
network: true
overview: 'Bithumb publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, General API, Market Data API, and 2 more. Tagged areas include Cryptocurrency, Exchange, Trading, South Korea, and KRW.


  The Bithumb catalog on APIs.io includes 1 Spectral governance ruleset.


  Bithumb''s developer surface includes authentication, documentation, changelog, support, engineering blog, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Bithumb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bithumb-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.4
  delta: -3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.9
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 15.8
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bithumb/refs/heads/main/screenshots/bithumb-2026-06-20T173314.png
security:
- kind: authentication
  name: Bithumb Authentication
  slug: bithumb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bithumb Domain Security
  slug: bithumb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bithumb
tags:
- Cryptocurrency
- Exchange
- Trading
- South Korea
- KRW
- Bitcoin
- Market Data
- WebSocket
website: https://www.bithumb.com
---
