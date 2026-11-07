---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openexchangerates Agentic Access
  operation_count: 7
  slug: openexchangerates-agentic-access
  summary_line: 7 operations
api_count: 2
apis:
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: Convert a value between two currencies at the latest rates.
  name: Open Exchange Rates Convert API
  slug: openexchangerates-convert-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: List of supported currency symbols and names.
  name: Open Exchange Rates Currencies API
  slug: openexchangerates-currencies-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: Open, high, low, close, and average rates for a period.
  name: Open Exchange Rates OHLC API
  slug: openexchangerates-ohlc-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: Bulk daily historical rates for a date range.
  name: Open Exchange Rates Time Series API
  slug: openexchangerates-time-series-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: Account plan and usage statistics.
  name: Open Exchange Rates Usage API
  slug: openexchangerates-usage-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: Live and historical exchange rate data
  name: Open Exchange Rates API
  slug: openexchangerates-rates-api
artifact_total: 38
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
  name: Open Exchange Rates Convert API
  slug: open-openexchangerates-convert-api
- collection_type: open
  name: Open Exchange Rates Convert Currencies API
  slug: open-openexchangerates-currencies-api
- collection_type: open
  name: Open Exchange Rates Convert Historical Rates API
  slug: open-openexchangerates-historical-rates-api
- collection_type: open
  name: Open Exchange Rates Convert Latest Rates API
  slug: open-openexchangerates-latest-rates-api
- collection_type: open
  name: Open Exchange Rates Convert OHLC API
  slug: open-openexchangerates-ohlc-api
- collection_type: open
  name: Open Exchange Convert Rates API
  slug: open-openexchangerates-rates-api
- collection_type: open
  name: Open Exchange Rates Convert Time Series API
  slug: open-openexchangerates-time-series-api
- collection_type: open
  name: Open Exchange Rates Convert Usage API
  slug: open-openexchangerates-usage-api
- collection_type: open
  name: Open Exchange Rates API
  slug: open-openexchangerates
common:
- group: other
  href: https://artifacts.apis.io/openexchangerates/capabilities/openexchangerates-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openexchangerates-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/openexchangerates/agentic-access/openexchangerates-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openexchangerates-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/openexchangerates/security/openexchangerates-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openexchangerates-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/openexchangerates/authentication/openexchangerates-authentication.yml
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
  href: https://artifacts.apis.io/openexchangerates/plans/openexchangerates-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openexchangerates-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/openexchangerates/rate-limits/openexchangerates-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openexchangerates-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openexchangerates/finops/openexchangerates-finops.yml
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
- has_sources: true
  method: derived
  name: Openexchangerates Finops
  primary_unit: subscription
  service_category: ''
  slug: openexchangerates-finops
  template: false
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
modified: '2026-09-16'
name: Open Exchange Rates
nav: Providers
network: true
overview: 'Open Exchange Rates publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Convert API, Currencies API, OHLC API, and 3 more. Tagged areas include Foreign Exchange, Currency, Exchange Rates, Currency Conversion, and Financial Data.


  The Open Exchange Rates catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open Exchange Rates'' developer surface includes authentication, documentation, pricing, support, and 15 more developer resources.'
plans:
- name: Openexchangerates Plans Pricing
  plan_count: 5
  slug: openexchangerates-plans-pricing
- name: Openexchangerates Price Estimates
  plan_count: 0
  slug: openexchangerates-price-estimates
random_paper: 12
rate_limits:
- limit_count: 6
  name: Openexchangerates Rate Limits
  slug: openexchangerates-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Open Exchange Rates — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openexchangerates-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 66.3
    catalog_earned_first_party: 12.0
    catalog_gap: 48.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 71.1
    contract_governance: 9.8
    contract_quality: 55.1
    developer_ergonomics: 34.5
    discoverability: 66.1
    operational_transparency: 26.3
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/openexchangerates/openexchangerates-2026-08-07T190554.png
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
- Currency Conversion
- Financial Data
website: https://openexchangerates.org
---
