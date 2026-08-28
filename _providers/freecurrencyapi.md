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
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Freecurrencyapi Agentic Access
  operation_count: 4
  slug: freecurrencyapi-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Available currency information
  name: Free Currency API Currencies API
  slug: freecurrencyapi-currencies-api
- description: Current and historical exchange rate data
  name: Free Currency API Exchange Rates API
  slug: freecurrencyapi-exchange-rates-api
- description: API quota and status information
  name: Free Currency API Status API
  slug: freecurrencyapi-status-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Free Currency Currencies API
  slug: open-freecurrencyapi-currencies-api
- collection_type: open
  name: Free Currency Currencies Exchange Rates API
  slug: open-freecurrencyapi-exchange-rates-api
- collection_type: open
  name: Free Currency Currencies Status API
  slug: open-freecurrencyapi-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freecurrencyapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freecurrencyapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freecurrencyapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://freecurrencyapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://freecurrencyapi.com/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/everapihq
- group: commercial
  title: ''
  type: Pricing
  url: https://freecurrencyapi.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://api.freecurrencyapi.com/v1/status
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/freecurrencyapi/refs/heads/main/plans/freecurrencyapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/freecurrencyapi/refs/heads/main/rate-limits/freecurrencyapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/freecurrencyapi/refs/heads/main/finops/freecurrencyapi-finops.yml
created: '2026-06-13'
description: Free Currency API provides real-time and historical currency exchange rate data for 150+ currencies via a simple REST API. No registration is required for basic usage, making it ideal for hobby and development projects. The API offers daily-updated current exchange rates, historical rates dating back to 1999, and multi-currency support with official SDKs for JavaScript, Python, PHP, Go, Ruby, Rust, C#, and R.
examples:
- key_count: 4
  name: Get Currencies
  slug: get-currencies
- key_count: 4
  name: Get Historical Rates
  slug: get-historical-rates
- key_count: 4
  name: Get Latest Rates
  slug: get-latest-rates
- key_count: 4
  name: Get Status
  slug: get-status
finops:
- name: Freecurrencyapi Finops
  service_category: ''
  slug: freecurrencyapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freecurrencyapi.png
json_schemas:
- name: CurrenciesResponse
  property_count: 1
  slug: currencies-response
- name: ExchangeRatesResponse
  property_count: 1
  slug: exchange-rates-response
- name: HistoricalRatesResponse
  property_count: 1
  slug: historical-rates-response
- name: StatusResponse
  property_count: 1
  slug: status-response
jsonld:
- class_count: 0
  name: Freecurrencyapi Context
  property_count: 0
  slug: freecurrencyapi
layout: provider
modified: '2026-06-13'
name: Free Currency API
nav: Providers
network: true
overview: 'Free Currency API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Currencies API, Exchange Rates API, and Status API. Tagged areas include Currency, Exchange Rates, Finance, Historical Data, and Free.


  The Free Currency API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Free Currency API''s developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Freecurrencyapi Plans Pricing
  plan_count: 2
  slug: freecurrencyapi-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Freecurrencyapi Rate Limits
  slug: freecurrencyapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Free Currency API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: freecurrencyapi-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freecurrencyapi/refs/heads/main/screenshots/freecurrencyapi-2026-06-20T181521.png
security:
- kind: authentication
  name: Freecurrencyapi Authentication
  slug: freecurrencyapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Freecurrencyapi Domain Security
  slug: freecurrencyapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freecurrencyapi
tags:
- Currency
- Exchange Rates
- Finance
- Historical Data
- Free
website: https://freecurrencyapi.com/
---
