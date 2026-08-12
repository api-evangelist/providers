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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
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
artifact_total: 30
collections:
- collection_type: postman
  name: Open Exchange Rates Convert API
  slug: postman-openexchangerates-convert-api
- collection_type: postman
  name: Open Exchange Rates Convert Currencies API
  slug: postman-openexchangerates-currencies-api
- collection_type: postman
  name: Open Exchange Rates Convert OHLC API
  slug: postman-openexchangerates-ohlc-api
- collection_type: postman
  name: Open Exchange Convert Rates API
  slug: postman-openexchangerates-rates-api
- collection_type: postman
  name: Open Exchange Rates Convert Time Series API
  slug: postman-openexchangerates-time-series-api
- collection_type: postman
  name: Open Exchange Rates Convert Usage API
  slug: postman-openexchangerates-usage-api
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/open-exchange-rates/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openexchangerates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openexchangerates.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openexchangerates.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openexchangerates.org/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.openexchangerates.org
- group: operate
  title: ''
  type: Contact
  url: https://openexchangerates.org/contact
created: '2026-07-11'
description: Open Exchange Rates provides a simple, reliable REST API for live and historical foreign exchange (forex) rates covering 200+ world currencies, with end-of-day historical data back to January 1st, 1999. The JSON API delivers latest rates, historical snapshots, bulk time-series, currency conversion, and OHLC data, authenticated with a per-account App ID and priced in published monthly tiers that start with a free plan.
examples:
- key_count: 5
  name: Convert Response
  slug: convert-response
- key_count: 5
  name: Latest Rates
  slug: latest-rates
- key_count: 6
  name: Ohlc Response
  slug: ohlc-response
- key_count: 6
  name: Time Series Response
  slug: time-series-response
finops:
- name: Openexchangerates Finops
  service_category: Financial Data and Market Data
  slug: openexchangerates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openexchangerates.png
json_schemas:
- name: ConvertResponse
  property_count: 5
  slug: convert-response
- name: CurrenciesResponse
  property_count: 0
  slug: currencies-response
- name: ExchangeRatesResponse
  property_count: 5
  slug: exchange-rates-response
- name: OHLCResponse
  property_count: 6
  slug: ohlc-response
jsonld:
- class_count: 3
  name: Open Exchange Rates Context
  property_count: 24
  slug: open-exchange-rates
layout: provider
modified: '2026-08-08'
name: Open Exchange Rates
nav: Providers
network: true
overview: 'Open Exchange Rates publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, Historical Rates API, and 4 more. Tagged areas include Foreign Exchange, Currency, Exchange Rates, FX, and Currency Conversion.


  The Open Exchange Rates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open Exchange Rates'' developer surface includes authentication, documentation, pricing, support, and 14 more developer resources.'
plans:
- name: Openexchangerates Plans Pricing
  plan_count: 5
  slug: openexchangerates-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 6
  name: Openexchangerates Rate Limits
  slug: openexchangerates-rate-limits
rules:
- name: Open Exchange Rates API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openexchangerates-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.8
  delta: -0.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.6
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 58.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openexchangerates/refs/heads/main/screenshots/openexchangerates-2026-08-07T190554.png
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
