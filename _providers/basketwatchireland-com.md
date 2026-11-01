---
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
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Provides JSON and CSV endpoints for Irish grocery prices across major supermarkets, including catalogue, movers, promotions, barcode lookup and nutrition.
  name: BasketWatch Irish Grocery Price API
  slug: basketwatch-irish-grocery-price-api
- description: 'basketwatchireland-com API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: basketwatchireland-com API
  slug: basketwatchireland-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/basketwatchireland-com/rules/basketwatchireland-com-rules.yml
  title: ''
  type: Spectral
  url: rules/basketwatchireland-com-rules.yml
- group: design
  href: https://artifacts.apis.io/basketwatchireland-com/json-ld/basketwatchireland-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/basketwatchireland-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/basketwatchireland-com/vocabulary/basketwatchireland-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/basketwatchireland-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/basketwatchireland-com/data-model/basketwatchireland-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/basketwatchireland-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/basketwatchireland-com/conformance/basketwatchireland-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basketwatchireland-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basketwatchireland-com/llms/basketwatchireland-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basketwatchireland-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/basketwatchireland-com/well-known/basketwatchireland-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/basketwatchireland-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/basketwatchireland-com/hosts/basketwatchireland-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basketwatchireland-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basketwatchireland.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basketwatchireland.com/privacy
- group: auth
  href: https://artifacts.apis.io/basketwatchireland-com/security/basketwatchireland-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basketwatchireland-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basketwatchireland.com/
- group: docs
  title: ''
  type: APIReference
  url: https://basketwatchireland.com/api-reference
- group: operate
  title: ''
  type: Support
  url: https://basketwatchireland.com/faq
- group: company
  title: ''
  type: Blog
  url: https://basketwatchireland.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://basketwatchireland.com/#pricing
coverage:
  detail: API reference provides human docs but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract is published.
  evidence:
  - status: 200
    url: https://basketwatchireland.com/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: BasketWatch provides independent Irish grocery price intelligence, tracking daily shelf prices, promotions and loyalty offers across major supermarkets such as Aldi, Tesco, SuperValu, Dunnes Stores and Lidl. It offers a public API, dashboards, data stories and a free price comparison tool, delivering over 50,000 product price points each day.
image: https://basketwatchireland.com/og-image.png
json_schemas:
- name: GetApiAldiSpecialbuysResponse
  property_count: 3
  slug: basketwatchireland-com-get-api-aldi-specialbuys-response
- name: GetApiCompareResponse
  property_count: 7
  slug: basketwatchireland-com-get-api-compare-response
- name: GetApiStoreKpisResponse
  property_count: 12
  slug: basketwatchireland-com-get-api-store-kpis-response
- name: GetApiStoreProductsResponse
  property_count: 17
  slug: basketwatchireland-com-get-api-store-products-response
- name: GetApiStorePromotionsResponse
  property_count: 15
  slug: basketwatchireland-com-get-api-store-promotions-response
- name: GetApiStoreShrinkflationResponse
  property_count: 19
  slug: basketwatchireland-com-get-api-store-shrinkflation-response
jsonld:
- class_count: 19
  name: Basketwatchireland Com Context
  property_count: 86
  slug: basketwatchireland-com-context
layout: provider
modified: '2026-10-30'
name: basketwatchireland-com
nav: Providers
network: true
overview: 'basketwatchireland-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, Price Intelligence, API, and Ireland.


  The basketwatchireland-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  basketwatchireland-com''s developer surface includes API reference, support, engineering blog, pricing, and 12 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: basketwatchireland-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: basketwatchireland-com-rules
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 72.7
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 53.8
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basketwatchireland Com Domain Security
  slug: basketwatchireland-com-domain-security
  summary_line: TLSv1.3
slug: basketwatchireland-com
tags:
- Company
- Grocery
- Price Intelligence
- API
- Ireland
website: https://basketwatchireland.com/
---
