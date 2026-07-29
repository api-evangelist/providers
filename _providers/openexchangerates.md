---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openexchangerates Agentic Access
  operation_count: 7
  slug: openexchangerates-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: Convert a value between two currencies at the latest rates.
  name: Open Exchange Rates Convert API
  slug: openexchangerates-convert-api
- description: List of supported currency symbols and names.
  name: Open Exchange Rates Currencies API
  slug: openexchangerates-currencies-api
- description: End-of-day rates for any date back to 1999-01-01.
  name: Open Exchange Rates Historical Rates API
  slug: openexchangerates-historical-rates-api
- description: Current exchange rates relative to a base currency.
  name: Open Exchange Rates Latest Rates API
  slug: openexchangerates-latest-rates-api
- description: Open, high, low, close, and average rates for a period.
  name: Open Exchange Rates OHLC API
  slug: openexchangerates-ohlc-api
- description: Bulk daily historical rates for a date range.
  name: Open Exchange Rates Time Series API
  slug: openexchangerates-time-series-api
- description: Account plan and usage statistics.
  name: Open Exchange Rates Usage API
  slug: openexchangerates-usage-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Exchange Rates API
  slug: open-openexchangerates
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openexchangerates-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openexchangerates-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openexchangerates-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openexchangerates
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-exchange-rates
- group: company
  title: ''
  type: Website
  url: https://openexchangerates.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openexchangerates.org
- group: commercial
  title: ''
  type: Pricing
  url: https://openexchangerates.org/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/openexchangerates-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openexchangerates-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openexchangerates-finops.yml
created: '2026-07-11'
description: Open Exchange Rates provides a simple, reliable REST API for live and historical foreign exchange (forex) rates covering 200+ world currencies, with end-of-day historical data back to January 1st, 1999. The JSON API delivers latest rates, historical snapshots, bulk time-series, currency conversion, and OHLC data, authenticated with a per-account App ID and priced in published monthly tiers that start with a free plan.
finops:
- name: Openexchangerates Finops
  service_category: Financial Data and Market Data
  slug: openexchangerates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openexchangerates.png
layout: provider
modified: '2026-07-11'
name: Open Exchange Rates
nav: Providers
network: true
overview: 'Open Exchange Rates publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, Historical Rates API, and 4 more. Tagged areas include Foreign Exchange, Currency, Exchange Rates, FX, and Currency Conversion.


  Open Exchange Rates'' developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Openexchangerates Plans Pricing
  plan_count: 5
  slug: openexchangerates-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 6
  name: Openexchangerates Rate Limits
  slug: openexchangerates-rate-limits
score:
  band: thin
  composite: 41.6
  delta: -2.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Openexchangerates Authentication
  slug: openexchangerates-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Openexchangerates Domain Security
  slug: openexchangerates-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: openexchangerates
tags:
- Foreign Exchange
- Currency
- Exchange Rates
- FX
- Currency Conversion
- Forex
- Financial Data
website: https://openexchangerates.org
---
