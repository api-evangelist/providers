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
  scored_at: '2026-07-23'
api_count: 6
apis:
- description: Retrieve daily EOD open/high/low/close, volume, turnover, unadjusted close, dividends and open interest as a Pandas DataFrame or NumPy array. Supports date ranges, record limits, weekly/monthly/quarte
  name: Norgate Data Price and Volume Data
  slug: norgate-data-price-volume-data
- description: Point-in-time boolean and value time series used to build survivorship-bias-free databases - historical index membership, major-exchange-listed status, capital events, dividend yield, unadjusted close
  name: Norgate Data Corporate Actions and Time Series
  slug: norgate-data-corporate-actions-timeseries
- description: Single-value reference and metadata lookups for a security - name, symbol, asset id, domicile, currency, exchange, GICS-style classification at any level, corresponding industry index, base type, list
  name: Norgate Data Security Metadata and Classifications
  slug: norgate-data-security-metadata-classifications
- description: Futures-specific reference data covering around 100 markets across 11 worldwide exchange groups - market and session names/symbols, session contracts, point value, margin and first notice date. Norgat
  name: Norgate Data Futures Metadata
  slug: norgate-data-futures-metadata
- description: Company fundamental lookups - named fundamental fields, financial summary, business summary, shares outstanding and shares float. Availability depends on subscription package. Served from the local ND
  name: Norgate Data Fundamentals
  slug: norgate-data-fundamentals
- description: Enumerate and resolve the security lists in the local database - user and Norgate-maintained watchlists, built-in databases, and their member symbols - plus database and price update timestamps used t
  name: Norgate Data Watchlists and Databases
  slug: norgate-data-watchlists-databases
artifact_total: 9
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/norgatedata
- group: company
  title: ''
  type: Website
  url: https://norgatedata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pypi.org/project/norgatedata/
- group: commercial
  title: ''
  type: Plans
  url: plans/norgate-data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/norgate-data-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/norgate-data-finops.yml
created: '2026-07-11'
description: Norgate Data provides high-quality, survivorship-bias-free end-of-day (EOD) historical market data for US, Australian and Canadian stocks, around 100 worldwide futures markets, and foreign exchange. Data is not delivered as a hosted REST API. Instead, subscribers install the Norgate Data Updater (NDU), a Windows desktop application that downloads and maintains a complete local database and runs a local data service. Programmatic access is through the norgatedata Python package (on PyPI), which talks to that local NDU service and returns price/volume history, corporate actions, index constituent history, security metadata, fundamentals, and watchlists as Pandas DataFrames or NumPy arrays. Norgate also ships plugins for platforms such as Amibroker and is widely used with Python backtesting frameworks (Zipline, Backtrader). This entry honestly models the norgatedata library's logical operations as capability areas; it is a client library over a local service, not a public HTTP/REST
  API.
finops:
- name: Norgate Data Finops
  service_category: Market Data and Financial Data
  slug: norgate-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/norgate-data.png
layout: provider
modified: '2026-07-11'
name: Norgate Data
nav: Providers
network: true
overview: 'Norgate Data publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Market Data, Financial Data, Historical Data, Futures, and Stocks.


  Norgate Data''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Norgate Data Plans Pricing
  plan_count: 6
  slug: norgate-data-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Norgate Data Rate Limits
  slug: norgate-data-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: -3.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.5
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 0.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
slug: norgate-data
tags:
- Market Data
- Financial Data
- Historical Data
- Futures
- Stocks
- End of Day
- EOD
- Backtesting
- Survivorship Bias Free
- Python
website: https://norgatedata.com/
---
