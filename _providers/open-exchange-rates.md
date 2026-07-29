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
  name: Open Exchange Rates Agentic Access
  operation_count: 7
  slug: open-exchange-rates-agentic-access
  summary_line: 7 operations
api_count: 6
apis:
- description: Currency conversion (Unlimited plan)
  name: Open Exchange Rates Convert API
  slug: open-exchange-rates-convert-api
- description: Available currency list
  name: Open Exchange Rates Currencies API
  slug: open-exchange-rates-currencies-api
- description: Open/High/Low/Close data (VIP Platinum plan)
  name: Open Exchange Rates OHLC API
  slug: open-exchange-rates-ohlc-api
- description: Live and historical exchange rate data
  name: Open Exchange Rates Rates API
  slug: open-exchange-rates-rates-api
- description: Historical time-series data (Enterprise/Unlimited plans)
  name: Open Exchange Rates Time Series API
  slug: open-exchange-rates-time-series-api
- description: Plan and usage statistics
  name: Open Exchange Rates Usage API
  slug: open-exchange-rates-usage-api
artifact_total: 28
collections:
- collection_type: postman
  name: Open Exchange Rates Convert API
  slug: postman-open-exchange-rates-convert-api
- collection_type: postman
  name: Open Exchange Rates Convert Currencies API
  slug: postman-open-exchange-rates-currencies-api
- collection_type: postman
  name: Open Exchange Rates Convert OHLC API
  slug: postman-open-exchange-rates-ohlc-api
- collection_type: postman
  name: Open Exchange Convert Rates API
  slug: postman-open-exchange-rates-rates-api
- collection_type: postman
  name: Open Exchange Rates Convert Time Series API
  slug: postman-open-exchange-rates-time-series-api
- collection_type: postman
  name: Open Exchange Rates Convert Usage API
  slug: postman-open-exchange-rates-usage-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/open-exchange-rates/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-exchange-rates-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-exchange-rates-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-exchange-rates-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openexchangerates.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openexchangerates.org/reference/api-introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openexchangerates
- group: commercial
  title: ''
  type: Pricing
  url: https://openexchangerates.org/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openexchangerates.org
- group: commercial
  title: ''
  type: Plans
  url: plans/open-exchange-rates-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-exchange-rates-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-exchange-rates-finops.yml
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
created: '2026-06-13'
description: Foreign exchange rates REST API providing historical and real-time currency exchange data for 200+ currencies with hourly updates and USD as the default base currency. Trusted by over 100,000 organizations globally, Open Exchange Rates has delivered reliable forex data since 2011 with historical coverage back to January 1, 1999.
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
- name: Open Exchange Rates Finops
  service_category: ''
  slug: open-exchange-rates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-exchange-rates.png
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
modified: '2026-06-13'
name: Open Exchange Rates
nav: Providers
network: true
overview: 'Open Exchange Rates publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, OHLC API, and 3 more. Tagged areas include Foreign Exchange, Currency, Forex, Finance, and Exchange Rates.


  The Open Exchange Rates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open Exchange Rates'' developer surface includes authentication, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Open Exchange Rates Plans Pricing
  plan_count: 5
  slug: open-exchange-rates-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Open Exchange Rates Rate Limits
  slug: open-exchange-rates-rate-limits
rules:
- name: Open Exchange Rates API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: open-exchange-rates-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.5
  delta: -3.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 73.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 63.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/open-exchange-rates/refs/heads/main/screenshots/open-exchange-rates-2026-06-20T190738.png
security:
- kind: authentication
  name: Open Exchange Rates Authentication
  slug: open-exchange-rates-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Open Exchange Rates Domain Security
  slug: open-exchange-rates-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: open-exchange-rates
tags:
- Foreign Exchange
- Currency
- Forex
- Finance
- Exchange Rates
- Currency Conversion
- Historical Rates
website: https://openexchangerates.org
---
