---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fastforex Agentic Access
  operation_count: 20
  slug: fastforex-agentic-access
  summary_line: 20 operations
api_count: 7
apis:
- description: Account admin
  name: FastForex admin API
  slug: fastforex-admin-api
- description: Digital currencies, pairs & prices
  name: FastForex crypto API
  slug: fastforex-crypto-api
- description: Physical currencies, rates and conversions
  name: FastForex currency API
  slug: fastforex-currency-api
- description: Realtime FX trading pairs - instruments, prices and history
  name: FastForex fx API
  slug: fastforex-fx-api
- description: Available on The Extra Plan
  name: FastForex plan-extra API
  slug: fastforex-plan-extra-api
- description: Available on The One Plan
  name: FastForex plan-one API
  slug: fastforex-plan-one-api
- description: Available on The Premium Plan
  name: FastForex plan-premium API
  slug: fastforex-plan-premium-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: fastFOREX.io admin API
  slug: open-fastforex-admin-api
- collection_type: open
  name: fastFOREX.io admin crypto API
  slug: open-fastforex-crypto-api
- collection_type: open
  name: fastFOREX.io admin currency API
  slug: open-fastforex-currency-api
- collection_type: open
  name: fastFOREX.io admin fx API
  slug: open-fastforex-fx-api
- collection_type: open
  name: fastFOREX.io admin plan-extra API
  slug: open-fastforex-plan-extra-api
- collection_type: open
  name: fastFOREX.io admin plan-one API
  slug: open-fastforex-plan-one-api
- collection_type: open
  name: fastFOREX.io admin plan-premium API
  slug: open-fastforex-plan-premium-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fastforex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fastforex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fastforex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.fastforex.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.fastforex.io/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/fastforex
- group: company
  title: ''
  type: Blog
  url: https://www.fastforex.io/hub
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fastforex.io/hub/2026-new-plans-new-features-new-data
- group: other
  title: ''
  type: X
  url: https://x.com/fastforex_io
- group: commercial
  title: ''
  type: Plans
  url: plans/fastforex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fastforex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fastforex-finops.yml
created: '2026-06-13'
description: FastForex is a fast, reliable REST API providing real-time and historical currency exchange rates for 160+ world currencies, 500+ cryptocurrencies, and 2,300+ FX trading pairs. Features include currency conversion, many-to-one and multi-rate lookups, OHLC candlestick data, bid/ask pricing, WebSocket streaming, and up to 55 years of historical data. Average response time of 21ms with 100% uptime SLA.
examples:
- key_count: 3
  name: Convert
  slug: convert
- key_count: 3
  name: Fetch Multi
  slug: fetch-multi
- key_count: 3
  name: Fetch One
  slug: fetch-one
- key_count: 3
  name: Fx Quote
  slug: fx-quote
- key_count: 3
  name: Historical
  slug: historical
- key_count: 3
  name: Ohlc Time Series
  slug: ohlc-time-series
finops:
- name: Fastforex Finops
  service_category: ''
  slug: fastforex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fastforex.png
json_schemas:
- name: ConvertResponse
  property_count: 4
  slug: convert-response
- name: Currency
  property_count: 0
  slug: currency
- name: FetchMultiResponse
  property_count: 4
  slug: fetch-multi-response
- name: FetchOneResponse
  property_count: 4
  slug: fetch-one-response
- name: FxQuoteResponse
  property_count: 2
  slug: fx-quote-response
- name: OhlcTimeSeriesResponse
  property_count: 10
  slug: ohlc-time-series-response
jsonld:
- class_count: 0
  name: Fastforex Context
  property_count: 36
  slug: fastforex-context
layout: provider
modified: '2026-06-13'
name: FastForex
nav: Providers
network: true
overview: 'FastForex publishes 7 APIs on the [APIs.io](https://apis.io/) network, including admin API, crypto API, currency API, and 4 more. Tagged areas include Currency Exchange, Forex, Financial Data, Exchange Rates, and Cryptocurrency.


  The FastForex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FastForex''s developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Fastforex Plans Pricing
  plan_count: 4
  slug: fastforex-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 9
  name: Fastforex Rate Limits
  slug: fastforex-rate-limits
rules:
- name: FastForex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fastforex-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fastforex/refs/heads/main/screenshots/fastforex-2026-06-20T181050.png
security:
- kind: authentication
  name: Fastforex Authentication
  slug: fastforex-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Fastforex Domain Security
  slug: fastforex-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fastforex
tags:
- Currency Exchange
- Forex
- Financial Data
- Exchange Rates
- Cryptocurrency
- FX Trading
- Historical Data
- Real-Time Data
website: https://www.fastforex.io
---
