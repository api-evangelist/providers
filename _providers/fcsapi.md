---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: Free and fast access to Forex, cryptocurrency, and stock market data via REST and WebSocket endpoints.
  name: FCS API
  slug: fcs-api
- baseURL: https://api.fcsapi.com
  baseurl_source: declared
  description: The Forex API from FCS API — 3 operation(s) for forex.
  name: FCS API Forex API
  slug: fcsapi-forex-api
- baseURL: https://api.fcsapi.com
  baseurl_source: declared
  description: The Raw API from FCS API — 1 operation(s) for raw.
  name: FCS API Raw API
  slug: fcsapi-raw-api
- baseURL: https://api.fcsapi.com
  baseurl_source: declared
  description: The Stock API from FCS API — 6 operation(s) for stock.
  name: FCS API Stock API
  slug: fcsapi-stock-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/fcsapi/vendors/fcsapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fcsapi-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/fcsapi/plans/fcsapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fcsapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fcsapi/rules/fcsapi-rules.yml
  title: ''
  type: Spectral
  url: rules/fcsapi-rules.yml
- group: design
  href: https://artifacts.apis.io/fcsapi/json-ld/fcsapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fcsapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/fcsapi/vocabulary/fcsapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fcsapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fcsapi/data-model/fcsapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fcsapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/fcsapi/conformance/fcsapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fcsapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fcsapi/llms/fcsapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fcsapi-llms.txt
- group: other
  href: https://artifacts.apis.io/fcsapi/hosts/fcsapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fcsapi-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://fcsapi.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fcsapi.com/
- group: auth
  href: https://artifacts.apis.io/fcsapi/security/fcsapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fcsapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fcsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fcsapi.com/document/forex-api
- group: docs
  title: ''
  type: APIReference
  url: https://fcsapi.com/document/forex-api
- group: start
  title: ''
  type: GettingStarted
  url: https://fcsapi.com/document/forex-api
- group: commercial
  title: ''
  type: Pricing
  url: https://fcsapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fcsapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fcsapi.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://fcsapi.com/blog
- group: operate
  title: ''
  type: Support
  url: https://fcsapi.com/contact-us
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://fcsapi.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: FCS API provides free and fast access to Forex, cryptocurrency, and stock market data through a simple REST and WebSocket API. It offers real-time and historical rates, technical indicators, and charting data for developers building trading, analytics, or financial applications. The service includes extensive documentation, pricing tiers, and a developer portal for easy integration.
finops:
- has_sources: true
  method: derived
  name: Fcsapi Finops
  primary_unit: ''
  service_category: ''
  slug: fcsapi-finops
  template: true
image: https://fcsapi.com/assets/images/home-top-bg.webp
json_schemas:
- name: GetForexJwtTokenResponse
  property_count: 4
  slug: fcsapi-get-forex-jwt-token-response
- name: GetForexResponse
  property_count: 3
  slug: fcsapi-get-forex-response
- name: GetStockForecastResponse
  property_count: 1
  slug: fcsapi-get-stock-forecast-response
- name: GetStockResponse
  property_count: 5
  slug: fcsapi-get-stock-response
- name: GetStockStockidResponse
  property_count: 1
  slug: fcsapi-get-stock-stockid-response
- name: PostStockStockidResponse
  property_count: 3
  slug: fcsapi-post-stock-stockid-response
jsonld:
- class_count: 9
  name: Fcsapi Context
  property_count: 15
  slug: fcsapi-context
layout: provider
modified: '2026-10-16'
name: FCS API
nav: Providers
network: true
overview: 'FCS API is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Forex API, Raw API, Stock API, and 1 more. Tagged areas include Finance, Foreign Exchange, Cryptocurrency, Stocks, and Data API.


  The FCS API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FCS API''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, and 15 more developer resources.'
plans:
- name: Fcsapi Plans Pricing
  plan_count: 5
  slug: fcsapi-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: FCS API API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: fcsapi-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 22.6
    discoverability: 78.6
    operational_transparency: 0.0
  previous_composite: 40.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fcsapi/fcsapi-2026-11-03T131914.png
security:
- kind: domain-security
  name: Fcsapi Domain Security
  slug: fcsapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fcsapi
tags:
- Finance
- Foreign Exchange
- Cryptocurrency
- Stocks
- Data API
website: https://fcsapi.com/
---
