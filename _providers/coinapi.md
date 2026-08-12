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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Normalized cryptocurrency market data covering more than 350 exchanges and 28,000+ assets. Provides trades, quotes, order books, OHLCV time series, exchange rates, and derivatives metrics (funding rat
  name: CoinAPI Market Data API
  slug: market-data-api
- description: CoinAPI's Execution Management System (EMS) is a unified, multi-exchange crypto trading API that lets institutional traders, market makers, and builders place, modify, and cancel orders across many co
  name: CoinAPI EMS Trading API
  slug: ems-trading-api
- description: The Indexes API aggregates data from many exchanges to compute reference rates and benchmark indexes that summarize broad market conditions for a given asset. Useful for derivatives settlement, NAV co
  name: CoinAPI Indexes API
  slug: indexes-api
artifact_total: 9
asyncapis:
- description: Real-time cryptocurrency market data streaming over WebSocket using a Subscribe-Publish model. After establishing the WebSocket connection the client sends a `hello` (or `subscribe`) message containin
  name: CoinAPI Market Data WebSocket API
  slug: coinapi-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinapi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinapi
- group: company
  title: ''
  type: Website
  url: https://www.coinapi.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinapi.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinapi.io/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coinapi.io/general/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinapi.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/coinapi
- group: company
  title: ''
  type: Blog
  url: https://www.coinapi.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinapi.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinapi.io/terms-of-service
- group: agent
  title: ''
  type: LlmsText
  url: https://www.coinapi.io/llms.txt
created: '2025-03-01'
description: CoinAPI is a financial data and execution platform delivering normalized real-time and historical cryptocurrency market data and trade execution across more than 350 exchanges. Its product family covers a Market Data API (REST, WebSocket, FIX, and flat-file S3 delivery) for trades, quotes, order books, OHLCV, exchange rates, and derivatives metrics; an EMS Trading API (Execution Management System) that lets users place, manage, and route orders across multiple venues through one normalized REST/WebSocket/FIX interface; and Index and Metrics APIs that aggregate cross-exchange data into reference indexes and risk metrics. FIX endpoints (fix.coinapi.io) use GeoDNS to route to the nearest datacenter for low-latency connectivity.
finops:
- name: Coinapi Finops
  service_category: API
  slug: coinapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinapi.png
layout: provider
modified: '2026-05-29'
name: CoinAPI
nav: Providers
network: true
overview: 'CoinAPI publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data API. Tagged areas include Blockchain, Crypto Indexes, Crypto Metrics, Cryptocurrency, and EMS.


  The CoinAPI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  CoinAPI''s developer surface includes documentation, pricing, changelog, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Coinapi Plans Pricing
  plan_count: 3
  slug: coinapi-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Coinapi Rate Limits
  slug: coinapi-rate-limits
rules:
- name: CoinAPI API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: coinapi-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.0
  delta: -6.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 50.6
    developer_ergonomics: 10.9
    discoverability: 72.2
    governance: 41.7
    operational_transparency: 44.7
  previous_composite: 47.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/coinapi/refs/heads/main/screenshots/coinapi-2026-06-20T174721.png
security:
- kind: domain-security
  name: Coinapi Domain Security
  slug: coinapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coinapi
tags:
- Blockchain
- Crypto Indexes
- Crypto Metrics
- Cryptocurrency
- EMS
- Execution Management
- FIX
- Market Data
- Order Books
- REST
- WebSocket
website: https://www.coinapi.io/
---
