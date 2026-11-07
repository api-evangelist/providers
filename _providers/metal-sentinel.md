---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
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
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Real-time and historical precious metal prices, crypto, forex and mining stock data.
  name: Metal Sentinel API
  slug: metal-sentinel-api
- baseURL: https://metal-sentinel.p.rapidapi.com
  baseurl_source: declared
  description: Live spot quotes for ten metals refreshed every 15 seconds, daily historical series, gold karat and silver fineness prices, crypto and forex quotes, market status and mining equities. Subscribe on Rap
  name: Metal Sentinel API API
  slug: metal-sentinel-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/metal-sentinel/rules/metal-sentinel-rules.yml
  title: ''
  type: Spectral
  url: rules/metal-sentinel-rules.yml
- group: design
  href: https://artifacts.apis.io/metal-sentinel/json-ld/metal-sentinel-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/metal-sentinel-context.jsonld
- group: design
  href: https://artifacts.apis.io/metal-sentinel/vocabulary/metal-sentinel-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/metal-sentinel-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/metal-sentinel/conformance/metal-sentinel-conformance.yml
  title: ''
  type: Conformance
  url: conformance/metal-sentinel-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/metal-sentinel/plans/metal-sentinel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/metal-sentinel-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/metal-sentinel/data-model/metal-sentinel-data-model.yml
  title: ''
  type: DataModel
  url: data-model/metal-sentinel-data-model.yml
- group: agent
  href: https://artifacts.apis.io/metal-sentinel/llms/metal-sentinel-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/metal-sentinel-llms.txt
- group: agent
  href: https://artifacts.apis.io/metal-sentinel/well-known/metal-sentinel-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/metal-sentinel-well-known.yml
- group: other
  href: https://artifacts.apis.io/metal-sentinel/hosts/metal-sentinel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metal-sentinel-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metal-sentinel.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/metal-sentinel/security/metal-sentinel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metal-sentinel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metal-sentinel.com
- group: docs
  title: ''
  type: Documentation
  url: https://metal-sentinel.com/endpoints
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metal-sentinel.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://metal-sentinel.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://metal-sentinel.com/blog
- group: operate
  title: ''
  type: Contact
  url: https://metal-sentinel.com/contact
created: '2026-10-24'
description: Metal Sentinel provides a fast REST API delivering free real-time and historical precious metal prices, including gold, silver, platinum, palladium, rhodium, copper, nickel, aluminum, lead and zinc across 180+ currencies, plus crypto, forex and mining stock quotes. The service offers tiered plans via RapidAPI and includes market news.
image: https://metal-sentinel.com/imgs/og-image.jpg
json_schemas:
- name: Equity
  property_count: 16
  slug: metal-sentinel-equity
- name: Error
  property_count: 2
  slug: metal-sentinel-error
- name: ForexQuoteResponse
  property_count: 2
  slug: metal-sentinel-forex-quote-response
- name: GoldQuoteResponse
  property_count: 2
  slug: metal-sentinel-gold-quote-response
- name: HistoricalPointsResponse
  property_count: 9
  slug: metal-sentinel-historical-points-response
- name: SilverQuoteResponse
  property_count: 2
  slug: metal-sentinel-silver-quote-response
jsonld:
- class_count: 10
  name: Metal Sentinel Context
  property_count: 42
  slug: metal-sentinel-context
layout: provider
modified: '2026-10-24'
name: Metal Sentinel
nav: Providers
network: true
overview: 'Metal Sentinel publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Company, Financial Data, Metals, and Real-Time.


  The Metal Sentinel catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Metal Sentinel''s developer surface includes documentation, pricing, engineering blog, and 14 more developer resources.'
plans:
- name: Metal Sentinel Plans Pricing
  plan_count: 1
  slug: metal-sentinel-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Metal Sentinel API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: metal-sentinel-rules
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 59.1
    developer_ergonomics: 6.0
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 38.9
  provenance:
    conformance: derived
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
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/metal-sentinel/metal-sentinel-2026-11-03T135523.png
security:
- kind: domain-security
  name: Metal Sentinel Domain Security
  slug: metal-sentinel-domain-security
  summary_line: TLSv1.3
slug: metal-sentinel
tags:
- Company
- Financial Data
- Metals
- Real-Time
website: https://metal-sentinel.com
---
