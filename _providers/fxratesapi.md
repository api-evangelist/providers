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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fxratesapi Agentic Access
  operation_count: 5
  slug: fxratesapi-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.fxratesapi.com
  baseurl_source: declared
  description: Convert an amount between two currencies.
  name: FXRatesAPI Convert API
  slug: fxratesapi-convert-api
- baseURL: https://api.fxratesapi.com
  baseurl_source: declared
  description: List of supported currencies and their metadata.
  name: FXRatesAPI Currencies API
  slug: fxratesapi-currencies-api
- baseURL: https://api.fxratesapi.com
  baseurl_source: declared
  description: Exchange rates for a specific past date.
  name: FXRatesAPI Historical Rates API
  slug: fxratesapi-historical-rates-api
- baseURL: https://api.fxratesapi.com
  baseurl_source: declared
  description: Most recent exchange rates for a base currency.
  name: FXRatesAPI Latest Rates API
  slug: fxratesapi-latest-rates-api
- baseURL: https://api.fxratesapi.com
  baseurl_source: declared
  description: Daily exchange rates across a date range.
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
- group: company
  title: ''
  type: Blog
  url: https://fxratesapi.com/blog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/agentic-access/fxratesapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fxratesapi-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/security/fxratesapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fxratesapi-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/authentication/fxratesapi-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/plans/fxratesapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fxratesapi-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/rate-limits/fxratesapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fxratesapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fxratesapi/refs/heads/main/finops/fxratesapi-finops.yml
  title: ''
  type: FinOps
  url: finops/fxratesapi-finops.yml
created: '2026-07-12'
description: FXRatesAPI is a foreign exchange rates REST API that delivers real-time and historical currency exchange rates for 185+ fiat currencies plus major cryptocurrencies and precious metals. It exposes JSON endpoints for the latest rates, historical rates for any past date, time-series ranges, currency conversion, and a currencies list. A limited tier is usable without an API key; higher request quotas, more frequent updates, and additional base-currency switching are unlocked with a paid API key passed via the api_key query parameter or an Authorization Bearer header.
finops:
- has_sources: true
  method: generated
  name: Fxratesapi Finops
  primary_unit: ''
  service_category: Financial Data
  slug: fxratesapi-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fxratesapi.png
layout: provider
modified: '2026-10-06'
name: FXRatesAPI
nav: Providers
network: true
overview: 'FXRatesAPI publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, Historical Rates API, and 2 more. Tagged areas include Foreign Exchange, Currency, Exchange Rates, Currency Conversion, and Historical Rates.


  FXRatesAPI''s developer surface includes engineering blog, authentication, documentation, and 6 more developer resources.'
plans:
- name: Fxratesapi Plans Pricing
  plan_count: 2
  slug: fxratesapi-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Fxratesapi Rate Limits
  slug: fxratesapi-rate-limits
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 19.2
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 5.3
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
- Currency
- Exchange Rates
- Currency Conversion
- Historical Rates
- Financial Data
- Cryptocurrencies
website: https://fxratesapi.com
---
