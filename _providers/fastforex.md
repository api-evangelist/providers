---
access_model:
  confidence: medium
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fastforex Agentic Access
  operation_count: 20
  slug: fastforex-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- baseURL: https://api.fastforex.io
  baseurl_source: declared
  description: Account admin
  name: FastForex admin API
  slug: fastforex-admin-api
- baseURL: https://api.fastforex.io
  baseurl_source: declared
  description: Digital currencies, pairs & prices
  name: FastForex crypto API
  slug: fastforex-crypto-api
- baseURL: https://api.fastforex.io
  baseurl_source: declared
  description: Physical currencies, rates and conversions
  name: FastForex currency API
  slug: fastforex-currency-api
- baseURL: https://api.fastforex.io
  baseurl_source: declared
  description: Realtime FX trading pairs - instruments, prices and history
  name: FastForex fx API
  slug: fastforex-fx-api
artifact_total: 32
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
overview: 'FastForex publishes 4 APIs on the [APIs.io](https://apis.io/) network, including admin API, crypto API, currency API, and 1 more. Tagged areas include Currency Exchange, Forex, Financial Data, Exchange Rates, and Cryptocurrency.


  The FastForex catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FastForex''s developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Fastforex Plans Pricing
  plan_count: 4
  slug: fastforex-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 9
  name: Fastforex Rate Limits
  slug: fastforex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FastForex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fastforex-jsonschema-spectral-rules
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
