---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Currencyapi Agentic Access
  operation_count: 6
  slug: currencyapi-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: Convert a value between currencies.
  name: CurrencyAPI Convert API
  slug: currencyapi-convert-api
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: Supported currency metadata.
  name: CurrencyAPI Currencies API
  slug: currencyapi-currencies-api
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: End-of-day historical exchange rates back to 1999.
  name: CurrencyAPI Historical API
  slug: currencyapi-historical-api
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: Latest foreign exchange rates.
  name: CurrencyAPI Latest API
  slug: currencyapi-latest-api
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: Time-series exchange rates for a datetime range.
  name: CurrencyAPI Range API
  slug: currencyapi-range-api
- baseURL: https://api.currencyapi.com/v3
  baseurl_source: declared
  description: API health and account quota status.
  name: CurrencyAPI Status API
  slug: currencyapi-status-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Currency Convert API
  slug: open-currencyapi-convert-api
- collection_type: open
  name: Currency Convert Currencies API
  slug: open-currencyapi-currencies-api
- collection_type: open
  name: Currency Convert Historical API
  slug: open-currencyapi-historical-api
- collection_type: open
  name: Currency Convert Latest API
  slug: open-currencyapi-latest-api
- collection_type: open
  name: Currency Convert Range API
  slug: open-currencyapi-range-api
- collection_type: open
  name: Currency Convert Status API
  slug: open-currencyapi-status-api
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
random_paper: 13
rate_limits:
- limit_count: 6
  name: Currencyapi Rate Limits
  slug: currencyapi-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
