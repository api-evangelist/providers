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
  name: Currencyapi Agentic Access
  operation_count: 6
  slug: currencyapi-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Convert a value between currencies.
  name: CurrencyAPI Convert API
  slug: currencyapi-convert-api
- description: Supported currency metadata.
  name: CurrencyAPI Currencies API
  slug: currencyapi-currencies-api
- description: End-of-day historical exchange rates back to 1999.
  name: CurrencyAPI Historical API
  slug: currencyapi-historical-api
- description: Latest foreign exchange rates.
  name: CurrencyAPI Latest API
  slug: currencyapi-latest-api
- description: Time-series exchange rates for a datetime range.
  name: CurrencyAPI Range API
  slug: currencyapi-range-api
- description: API health and account quota status.
  name: CurrencyAPI Status API
  slug: currencyapi-status-api
artifact_total: 13
collections:
- collection_type: open
  name: CurrencyAPI
  slug: open-currencyapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/currencyapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currencyapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/currencyapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everapihq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everapi
- group: company
  title: ''
  type: Website
  url: https://currencyapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://currencyapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://currencyapi.com/docs/latest
- group: auth
  title: ''
  type: Authentication
  url: https://currencyapi.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://currencyapi.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/currencyapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/currencyapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/currencyapi-finops.yml
created: '2026-07-11'
description: CurrencyAPI (currencyapi.com, an Everapi product) is a foreign exchange rate and currency conversion REST API delivering real-time and historical exchange rates for 150+ fiat currencies, precious metals, and cryptocurrencies. A single versioned API (base https://api.currencyapi.com/v3) covers latest rates, historical rates back to 1999, time-series ranges down to minute accuracy, value conversion, currency metadata, and account quota status - authenticated with a simple apikey header and backed by published monthly plans that start with a free tier.
finops:
- name: Currencyapi Finops
  service_category: Financial Data APIs
  slug: currencyapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/currencyapi.png
layout: provider
modified: '2026-07-11'
name: CurrencyAPI
nav: Providers
network: true
overview: 'CurrencyAPI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, Historical API, and 3 more. Tagged areas include Foreign Exchange, Currency, Exchange Rates, FX, and Currency Conversion.


  CurrencyAPI''s developer surface includes authentication, documentation, API reference, pricing, and 9 more developer resources.'
plans:
- name: Currencyapi Plans Pricing
  plan_count: 5
  slug: currencyapi-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Currencyapi Rate Limits
  slug: currencyapi-rate-limits
score:
  band: developing
  composite: 43.3
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/currencyapi/refs/heads/main/screenshots/currencyapi-2026-07-25T210945.png
security:
- kind: authentication
  name: Currencyapi Authentication
  slug: currencyapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Currencyapi Domain Security
  slug: currencyapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: currencyapi
tags:
- Foreign Exchange
- Currency
- Exchange Rates
- FX
- Currency Conversion
- Financial Data
website: https://currencyapi.com
---
