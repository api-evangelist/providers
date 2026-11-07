---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.tickerlayer.com
  baseurl_source: declared
  description: 'TickerLayer API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: TickerLayer API
  slug: tickerlayer-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/tickerlayer/rate-limits/tickerlayer-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tickerlayer-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tickerlayer/plans/tickerlayer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tickerlayer-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tickerlayer/rules/tickerlayer-rules.yml
  title: ''
  type: Spectral
  url: rules/tickerlayer-rules.yml
- group: design
  href: https://artifacts.apis.io/tickerlayer/json-ld/tickerlayer-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tickerlayer-context.jsonld
- group: design
  href: https://artifacts.apis.io/tickerlayer/vocabulary/tickerlayer-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tickerlayer-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tickerlayer/data-model/tickerlayer-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tickerlayer-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tickerlayer/changelog/tickerlayer-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tickerlayer-changelog.yml
- group: start
  href: https://artifacts.apis.io/tickerlayer/sandbox/tickerlayer-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tickerlayer-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/tickerlayer/authentication/tickerlayer-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tickerlayer-authentication.yml
- group: design
  href: https://artifacts.apis.io/tickerlayer/conformance/tickerlayer-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tickerlayer-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tickerlayer/llms/tickerlayer-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tickerlayer-llms.txt
- group: agent
  href: https://artifacts.apis.io/tickerlayer/well-known/tickerlayer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tickerlayer-well-known.yml
- group: other
  href: https://artifacts.apis.io/tickerlayer/hosts/tickerlayer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tickerlayer-hosts.yml
- group: other
  href: https://artifacts.apis.io/tickerlayer/vendors/tickerlayer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tickerlayer-vendors.yml
- group: build
  href: https://artifacts.apis.io/tickerlayer/packages/tickerlayer-packages.yml
  title: ''
  type: SDKs
  url: packages/tickerlayer-packages.yml
- group: build
  href: https://artifacts.apis.io/tickerlayer/packages/tickerlayer-packages.yml
  title: ''
  type: Packages
  url: packages/tickerlayer-packages.yml
- group: auth
  href: https://artifacts.apis.io/tickerlayer/security/tickerlayer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tickerlayer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tickerlayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://tickerlayer.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tickerlayer.com
- group: start
  title: ''
  type: GettingStarted
  url: https://tickerlayer.com/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://tickerlayer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tickerlayer.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tickerlayer.com/privacy-policy
created: '2026-10-20'
description: TickerLayer provides real‑time market data APIs for developers, offering REST and WebSocket endpoints covering stocks, forex, crypto, indices, ETFs, commodities, bonds and perpetual contracts. The platform delivers live quotes, historical bars, and market fundamentals with flexible pricing tiers, supporting AI agents and integration into trading applications.
image: https://tickerlayer.com/opengraph-image
json_schemas:
- name: GetEtfsAggSymbolPrevResponse
  property_count: 6
  slug: tickerlayer-get-etfs-agg-symbol-prev-response
- name: GetIndicesAggSymbolNSpanFromToResponse
  property_count: 6
  slug: tickerlayer-get-indices-agg-symbol-nspan-from-to-response
- name: GetIndicesAggSymbolPrevResponse
  property_count: 6
  slug: tickerlayer-get-indices-agg-symbol-prev-response
- name: GetIndicesSnapshotSymbolResponse
  property_count: 10
  slug: tickerlayer-get-indices-snapshot-symbol-response
- name: GetIndicesSymbolsResponse
  property_count: 3
  slug: tickerlayer-get-indices-symbols-response
- name: GetStocksSnapshotSymbolResponse
  property_count: 11
  slug: tickerlayer-get-stocks-snapshot-symbol-response
jsonld:
- class_count: 21
  name: Tickerlayer Context
  property_count: 28
  slug: tickerlayer-context
layout: provider
modified: '2026-10-20'
name: TickerLayer
nav: Providers
network: true
overview: 'TickerLayer is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Market Data, Real-Time, and Finance.


  The TickerLayer catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TickerLayer''s developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, pricing, and 18 more developer resources.'
plans:
- name: Tickerlayer Plans Pricing
  plan_count: 4
  slug: tickerlayer-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 12
  name: Tickerlayer Rate Limits
  slug: tickerlayer-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: TickerLayer API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: tickerlayer-rules
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 81.8
    catalog_earned_first_party: 24.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 41.7
    discoverability: 64.3
    operational_transparency: 47.4
  previous_composite: 46.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tickerlayer/tickerlayer-2026-11-03T144725.png
security:
- kind: authentication
  name: Tickerlayer Authentication
  slug: tickerlayer-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Tickerlayer Domain Security
  slug: tickerlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tickerlayer
tags:
- Company
- Market Data
- Real-Time
- Finance
website: https://tickerlayer.com
---
