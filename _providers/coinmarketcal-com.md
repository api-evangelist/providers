---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.coinmarketcal.com
  baseurl_source: declared
  description: 'CoinMarketCal API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CoinMarketCal API
  slug: coinmarketcal-com-api
artifact_total: 12
asyncapis:
- description: ''
  name: Coinmarketcal Com Webhooks
  slug: coinmarketcal-com-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/coinmarketcal-com/rate-limits/coinmarketcal-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coinmarketcal-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/rules/coinmarketcal-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coinmarketcal-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/json-ld/coinmarketcal-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinmarketcal-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/vocabulary/coinmarketcal-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinmarketcal-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/asyncapi/coinmarketcal-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coinmarketcal-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/data-model/coinmarketcal-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinmarketcal-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/coinmarketcal-com/changelog/coinmarketcal-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coinmarketcal-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/conventions/coinmarketcal-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinmarketcal-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/coinmarketcal-com/authentication/coinmarketcal-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinmarketcal-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/coinmarketcal-com/lifecycle/coinmarketcal-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/coinmarketcal-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/lifecycle/coinmarketcal-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coinmarketcal-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coinmarketcal-com/conformance/coinmarketcal-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinmarketcal-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinmarketcal-com/llms/coinmarketcal-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinmarketcal-com-llms.txt
- group: other
  href: https://artifacts.apis.io/coinmarketcal-com/hosts/coinmarketcal-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinmarketcal-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinmarketcal-com/vendors/coinmarketcal-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinmarketcal-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://coinmarketcal.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.coinmarketcal.com</code
- group: auth
  href: https://artifacts.apis.io/coinmarketcal-com/security/coinmarketcal-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinmarketcal-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinmarketcal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://coinmarketcal.com/developer/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://coinmarketcal.com/developer/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://coinmarketcal.com/developer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinmarketcal.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinmarketcal.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://coinmarketcal.com/contact
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are HTML rendered with JavaScript and provide no machine‑readable OpenAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://coinmarketcal.com/developer/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: CoinMarketCal provides a crypto events calendar API that aggregates verified market-moving events for cryptocurrencies. The platform offers free and paid plans, detailed event data, categories, and coin information, enabling developers to integrate real-time catalyst data into dashboards, trading bots, and research tools. It emphasizes accurate sourcing, impact scoring, and comprehensive coverage of upcoming crypto events.
image: https://coinmarketcal.com/opengraph-image
json_schemas:
- name: GetV2CoinsResponse
  property_count: 2
  slug: coinmarketcal-com-get-v2-coins-response
- name: GetV2EventsIdResponse
  property_count: 6
  slug: coinmarketcal-com-get-v2-events-id-response
- name: GetV2EventsResponse
  property_count: 2
  slug: coinmarketcal-com-get-v2-events-response
- name: GetV2ExportsEventsCsvResponse
  property_count: 1
  slug: coinmarketcal-com-get-v2-exports-events-csv-response
- name: GetV2ExportsEventsSnapshotResponse
  property_count: 1
  slug: coinmarketcal-com-get-v2-exports-events-snapshot-response
jsonld:
- class_count: 5
  name: Coinmarketcal Com Context
  property_count: 10
  slug: coinmarketcal-com-context
layout: provider
modified: '2026-11-04'
name: CoinMarketCal
nav: Providers
network: true
overview: 'CoinMarketCal is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Event, Calendar, and Data.


  The CoinMarketCal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CoinMarketCal''s developer surface includes changelog, authentication, documentation, getting-started guide, pricing, support, and 19 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 15
  name: Coinmarketcal Com Rate Limits
  slug: coinmarketcal-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: CoinMarketCal API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: coinmarketcal-com-rules
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 33.8
    developer_ergonomics: 47.6
    discoverability: 58.9
    operational_transparency: 63.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coinmarketcal Com Authentication
  slug: coinmarketcal-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coinmarketcal Com Domain Security
  slug: coinmarketcal-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coinmarketcal-com
tags:
- Cryptocurrency
- Event
- Calendar
- Data
website: https://coinmarketcal.com/
---
