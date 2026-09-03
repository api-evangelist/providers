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
    agent_card: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 5
apis:
- description: Retrieve daily EOD open/high/low/close, volume, turnover, unadjusted close, dividends and open interest as a Pandas DataFrame or NumPy array. Supports date ranges, record limits, weekly/monthly/quarte
  name: Norgate Data Price and Volume Data
  slug: norgate-data-price-volume-data
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
artifact_total: 8
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
modified: '2026-07-25'
name: Norgate Data
nav: Providers
network: true
overview: 'Norgate Data publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Market Data, Financial Data, Historical Data, Futures, and Stocks.


  Norgate Data''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Norgate Data Plans Pricing
  plan_count: 6
  slug: norgate-data-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Norgate Data Rate Limits
  slug: norgate-data-rate-limits
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 4
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 17.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/norgate-data/refs/heads/main/screenshots/norgate-data-2026-08-07T185515.png
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
