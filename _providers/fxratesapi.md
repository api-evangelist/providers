---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fxratesapi Agentic Access
  operation_count: 5
  slug: fxratesapi-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Convert an amount between two currencies.
  name: FXRatesAPI Convert API
  slug: fxratesapi-convert-api
- description: List of supported currencies and their metadata.
  name: FXRatesAPI Currencies API
  slug: fxratesapi-currencies-api
- description: Exchange rates for a specific past date.
  name: FXRatesAPI Historical Rates API
  slug: fxratesapi-historical-rates-api
- description: Most recent exchange rates for a base currency.
  name: FXRatesAPI Latest Rates API
  slug: fxratesapi-latest-rates-api
- description: Daily exchange rates across a date range.
  name: FXRatesAPI Time-Series API
  slug: fxratesapi-time-series-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FXRates Convert API
  slug: open-fxratesapi-convert-api
- collection_type: open
  name: FXRates Convert Currencies API
  slug: open-fxratesapi-currencies-api
- collection_type: open
  name: FXRates Convert Historical Rates API
  slug: open-fxratesapi-historical-rates-api
- collection_type: open
  name: FXRates Convert Latest Rates API
  slug: open-fxratesapi-latest-rates-api
- collection_type: open
  name: FXRates Convert Time-Series API
  slug: open-fxratesapi-time-series-api
- collection_type: open
  name: FXRatesAPI
  slug: open-fxratesapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fxratesapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fxratesapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fxratesapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fxratesapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://fxratesapi.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/fxratesapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fxratesapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fxratesapi-finops.yml
created: '2026-07-12'
description: FXRatesAPI is a foreign exchange rates REST API that delivers real-time and historical currency exchange rates for 185+ fiat currencies plus major cryptocurrencies and precious metals. It exposes JSON endpoints for the latest rates, historical rates for any past date, time-series ranges, currency conversion, and a currencies list. A limited tier is usable without an API key; higher request quotas, more frequent updates, and additional base-currency switching are unlocked with a paid API key passed via the api_key query parameter or an Authorization Bearer header.
finops:
- name: Fxratesapi Finops
  service_category: Financial Data
  slug: fxratesapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fxratesapi.png
layout: provider
modified: '2026-07-12'
name: FXRatesAPI
nav: Providers
network: true
overview: 'FXRatesAPI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, Historical Rates API, and 2 more. Tagged areas include Foreign Exchange, FX, Currency, Exchange Rates, and Forex.


  FXRatesAPI''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Fxratesapi Plans Pricing
  plan_count: 2
  slug: fxratesapi-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Fxratesapi Rate Limits
  slug: fxratesapi-rate-limits
score:
  band: thin
  composite: 33.9
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 54.7
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/screenshots/fxratesapi-2026-07-25T215340.png
security:
- kind: authentication
  name: Fxratesapi Authentication
  slug: fxratesapi-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fxratesapi Domain Security
  slug: fxratesapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fxratesapi
tags:
- Foreign Exchange
- FX
- Currency
- Exchange Rates
- Forex
- Currency Conversion
- Historical Rates
- Financial Data
- Cryptocurrencies
website: https://fxratesapi.com
---
