---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Dinilu provides a quotation API for custom promotional products as described on the Developers page.
  name: Dinilu API
  slug: dinilu-api
- description: 'Dinilu API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dinilu API
  slug: dinilu-eu-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/dinilu-eu/rules/dinilu-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/dinilu-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/dinilu-eu/json-ld/dinilu-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dinilu-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/dinilu-eu/vocabulary/dinilu-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dinilu-eu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dinilu-eu/data-model/dinilu-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dinilu-eu-data-model.yml
- group: design
  href: https://artifacts.apis.io/dinilu-eu/conformance/dinilu-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinilu-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dinilu-eu/llms/dinilu-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-eu-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-eu/well-known/dinilu-eu-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-eu-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-eu/well-known/dinilu-eu-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-eu-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-eu/hosts/dinilu-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-eu-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dinilu.eu/about-us/developers
- group: auth
  href: https://artifacts.apis.io/dinilu-eu/security/dinilu-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.eu/
coverage:
  detail: Developers page loads content via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://dinilu.eu/about-us/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Dinilu is a supplier of quality promotional products and printed matter from the Far East. They offer a quick quotation tool for customized items, with competitive pricing, quality control, shipping and delivery to customers' doors. The company operates online, providing a range of branded products, including temporary tattoos, playing cards, rolling papers, and first aid supplies, catering to businesses seeking promotional merchandise. Their site includes product catalogs, RSS feeds, and contact information, reflecting a comprehensive e‑commerce platform for promotional and printed goods.
image: https://cdn.dinilu.eu/art/dinilueu.svg
json_schemas:
- name: GetApiProductMpnResponse
  property_count: 7
  slug: dinilu-eu-get-api-product-mpn-response
- name: GetApiProductsResponse
  property_count: 5
  slug: dinilu-eu-get-api-products-response
- name: GetApiQuoteResponse
  property_count: 12
  slug: dinilu-eu-get-api-quote-response
- name: PostApiQuoteRequest
  property_count: 5
  slug: dinilu-eu-post-api-quote-request
- name: PostApiQuoteResponse
  property_count: 12
  slug: dinilu-eu-post-api-quote-response
jsonld:
- class_count: 5
  name: Dinilu Eu Context
  property_count: 23
  slug: dinilu-eu-context
layout: provider
modified: '2026-11-05'
name: Dinilu
nav: Providers
network: true
overview: 'Dinilu is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Promotional Products, Printed Matter, and Custom Merchandise.


  The Dinilu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Dinilu API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: dinilu-eu-rules
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dinilu Eu Domain Security
  slug: dinilu-eu-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-eu
tags:
- Company
- E-Commerce
- Promotional Products
- Printed Matter
- Custom Merchandise
website: https://dinilu.eu/
---
