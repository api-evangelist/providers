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
- description: API for product listings and quoting as documented on the developer portal.
  name: Dinilu API
  slug: dinilu-api
- description: 'Dinilu Promotional & Printed Products API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dinilu Promotional & Printed Products API
  slug: dinilu-ca-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/dinilu-ca/rules/dinilu-ca-rules.yml
  title: ''
  type: Spectral
  url: rules/dinilu-ca-rules.yml
- group: design
  href: https://artifacts.apis.io/dinilu-ca/json-ld/dinilu-ca-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dinilu-ca-context.jsonld
- group: design
  href: https://artifacts.apis.io/dinilu-ca/vocabulary/dinilu-ca-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dinilu-ca-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dinilu-ca/data-model/dinilu-ca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dinilu-ca-data-model.yml
- group: design
  href: https://artifacts.apis.io/dinilu-ca/conformance/dinilu-ca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinilu-ca-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dinilu-ca/llms/dinilu-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-ca-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-ca/well-known/dinilu-ca-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-ca-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-ca/well-known/dinilu-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-ca/hosts/dinilu-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-ca-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dinilu.ca/about-us/developers
- group: auth
  href: https://artifacts.apis.io/dinilu-ca/security/dinilu-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.ca/
coverage:
  checked: '2026-11-05'
  detail: Developer portal provides API docs but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://dinilu.ca/about-us/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dinilu Promotional & Printed Products is a Guangzhou‑based trading company offering a wide range of custom promotional items, printed matter, branded merchandise and disposable gifts sourced from the Far East. Customers can obtain online quotations, calculate costs and delivery times quickly, and benefit from worldwide shipping, quality control and competitive pricing. The company was founded in 2024 and serves global businesses seeking reliable promotional product solutions.
image: https://cdn.dinilu.ca/art/diniluca.svg
json_schemas:
- name: GetApiProductMpnResponse
  property_count: 7
  slug: dinilu-ca-get-api-product-mpn-response
- name: GetApiProductsResponse
  property_count: 5
  slug: dinilu-ca-get-api-products-response
- name: GetApiQuoteResponse
  property_count: 12
  slug: dinilu-ca-get-api-quote-response
- name: PostApiQuoteRequest
  property_count: 5
  slug: dinilu-ca-post-api-quote-request
- name: PostApiQuoteResponse
  property_count: 12
  slug: dinilu-ca-post-api-quote-response
jsonld:
- class_count: 5
  name: Dinilu Ca Context
  property_count: 23
  slug: dinilu-ca-context
layout: provider
modified: '2026-11-05'
name: Dinilu Promotional & Printed Products
nav: Providers
network: true
overview: 'Dinilu Promotional & Printed Products is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Promotional, Printing, Custom Products, E-Commerce, and Guangzhou.


  The Dinilu Promotional & Printed Products catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Dinilu Promotional & Printed Products API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: dinilu-ca-rules
score:
  band: emerging
  composite: 17.1
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
  name: Dinilu Ca Domain Security
  slug: dinilu-ca-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-ca
tags:
- Promotional
- Printing
- Custom Products
- E-Commerce
- Guangzhou
website: https://dinilu.ca/
---
