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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Currencybeacon Agentic Access
  operation_count: 5
  slug: currencybeacon-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.currencybeacon.com/v1
  baseurl_source: declared
  description: Currency conversion operations
  name: CurrencyBeacon conversion API
  slug: currencybeacon-conversion-api
- baseURL: https://api.currencybeacon.com/v1
  baseurl_source: declared
  description: Supported currencies information
  name: CurrencyBeacon currencies API
  slug: currencybeacon-currencies-api
- baseURL: https://api.currencybeacon.com/v1
  baseurl_source: declared
  description: Currency exchange rate operations
  name: CurrencyBeacon rates API
  slug: currencybeacon-rates-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CurrencyBeacon conversion API
  slug: open-currencybeacon-conversion-api
- collection_type: open
  name: CurrencyBeacon conversion currencies API
  slug: open-currencybeacon-currencies-api
- collection_type: open
  name: CurrencyBeacon conversion rates API
  slug: open-currencybeacon-rates-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/currencybeacon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currencybeacon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/currencybeacon-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://currencybeacon.com
- group: docs
  title: ''
  type: Documentation
  url: https://currencybeacon.com/api-documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/currencybeacon
- group: commercial
  title: ''
  type: Pricing
  url: https://currencybeacon.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.currencybeacon.com
- group: other
  title: ''
  type: X
  url: https://x.com/currencybeacon
- group: commercial
  title: ''
  type: Plans
  url: plans/currencybeacon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/currencybeacon-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/currencybeacon-finops.yml
created: '2026-06-13'
description: Currency exchange rates REST API providing real-time mid-market rates for 170+ fiat currencies and cryptocurrencies, with 30 years of historical data, server-side conversion, timeseries analysis, and MCP server support for LLM integrations. Sourced from central banks and trusted financial institutions with 99.99% uptime.
examples:
- key_count: 6
  name: Conversion Example
  slug: conversion-example
- key_count: 2
  name: Currencies Example
  slug: currencies-example
- key_count: 4
  name: Latest Rates Example
  slug: latest-rates-example
- key_count: 5
  name: Timeseries Example
  slug: timeseries-example
finops:
- name: Currencybeacon Finops
  service_category: ''
  slug: currencybeacon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/currencybeacon.png
json_schemas:
- name: ConversionResponse
  property_count: 6
  slug: conversion-response
- name: CurrencyInfo
  property_count: 7
  slug: currency-info
- name: LatestRatesResponse
  property_count: 4
  slug: latest-rates-response
layout: provider
modified: '2026-06-13'
name: CurrencyBeacon
nav: Providers
network: true
overview: 'CurrencyBeacon publishes 3 APIs on the [APIs.io](https://apis.io/) network: conversion API, currencies API, and rates API. Tagged areas include Currency, Exchange Rates, Forex, Cryptocurrency, and Financial Data.


  The CurrencyBeacon catalog on APIs.io includes 1 Spectral governance ruleset.


  CurrencyBeacon''s developer surface includes authentication, documentation, pricing, and 9 more developer resources.'
plans:
- name: Currencybeacon Plans Pricing
  plan_count: 5
  slug: currencybeacon-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Currencybeacon Rate Limits
  slug: currencybeacon-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CurrencyBeacon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: currencybeacon-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.3
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 58.5
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/currencybeacon/refs/heads/main/screenshots/currencybeacon-2026-06-20T175338.png
security:
- kind: authentication
  name: Currencybeacon Authentication
  slug: currencybeacon-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Currencybeacon Domain Security
  slug: currencybeacon-domain-security
  summary_line: TLSv1.3
slug: currencybeacon
tags:
- Currency
- Exchange Rates
- Forex
- Cryptocurrency
- Financial Data
- Historical Rates
- Currency Conversion
website: https://currencybeacon.com
---
