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
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public JSON REST API for product catalogue and quoting
  name: Dinilu API
  slug: dinilu-api
- description: 'Dinilu Promotional & Printed Products API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dinilu Promotional & Printed Products API
  slug: dinilu-co-uk-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/dinilu-co-uk/rules/dinilu-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/dinilu-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/dinilu-co-uk/json-ld/dinilu-co-uk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dinilu-co-uk-context.jsonld
- group: design
  href: https://artifacts.apis.io/dinilu-co-uk/vocabulary/dinilu-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dinilu-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dinilu-co-uk/data-model/dinilu-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dinilu-co-uk-data-model.yml
- group: design
  href: https://artifacts.apis.io/dinilu-co-uk/conformance/dinilu-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinilu-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dinilu-co-uk/llms/dinilu-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-co-uk-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-co-uk/well-known/dinilu-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-co-uk/well-known/dinilu-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-co-uk/hosts/dinilu-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-co-uk-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dinilu-co-uk/security/dinilu-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dinilu.co.uk/about-us/developers
coverage:
  checked: '2026-11-05'
  detail: Developers page is HTML with JavaScript rendering; no machine‑readable OpenAPI or other contract discovered.
  evidence:
  - status: 200
    url: https://dinilu.co.uk/about-us/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: Dinilu Promotional & Printed Products offers online quotations for promotional items, advertising specialties, branded merchandise, printed matter, disposables, logo gifts and customised products from China. They specialise in delivery across Europe with good prices, quality control, transport and delivery to your door, acting as factory, wholesaler and shipping company in one.
image: https://cdn.dinilu.co.uk/art/dinilu-1200x1200.png
json_schemas:
- name: GetApiProductMpnResponse
  property_count: 7
  slug: dinilu-co-uk-get-api-product-mpn-response
- name: GetApiProductsResponse
  property_count: 5
  slug: dinilu-co-uk-get-api-products-response
- name: GetApiQuoteResponse
  property_count: 13
  slug: dinilu-co-uk-get-api-quote-response
- name: PostApiQuoteRequest
  property_count: 5
  slug: dinilu-co-uk-post-api-quote-request
- name: PostApiQuoteResponse
  property_count: 13
  slug: dinilu-co-uk-post-api-quote-response
jsonld:
- class_count: 5
  name: Dinilu Co Uk Context
  property_count: 24
  slug: dinilu-co-uk-context
layout: provider
modified: '2026-11-05'
name: Dinilu Promotional & Printed Products
nav: Providers
network: true
overview: 'Dinilu Promotional & Printed Products is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Promotional, Printing, E-Commerce, and Europe.


  The Dinilu Promotional & Printed Products catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Dinilu Promotional & Printed Products API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: dinilu-co-uk-rules
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.5
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
  name: Dinilu Co Uk Domain Security
  slug: dinilu-co-uk-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-co-uk
tags:
- Company
- Promotional
- Printing
- E-Commerce
- Europe
website: https://dinilu.co.uk/
---
