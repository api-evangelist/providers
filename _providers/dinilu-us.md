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
- description: Dinilu provides product catalog and quote APIs as listed in its developer portal.
  name: Dinilu API
  slug: dinilu-api
- description: 'Dinilu Promotional & Printed Products API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dinilu Promotional & Printed Products API
  slug: dinilu-us-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/dinilu-us/rules/dinilu-us-rules.yml
  title: ''
  type: Spectral
  url: rules/dinilu-us-rules.yml
- group: design
  href: https://artifacts.apis.io/dinilu-us/json-ld/dinilu-us-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dinilu-us-context.jsonld
- group: design
  href: https://artifacts.apis.io/dinilu-us/vocabulary/dinilu-us-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dinilu-us-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dinilu-us/data-model/dinilu-us-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dinilu-us-data-model.yml
- group: design
  href: https://artifacts.apis.io/dinilu-us/conformance/dinilu-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dinilu-us-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dinilu-us/llms/dinilu-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinilu-us-llms.txt
- group: auth
  href: https://artifacts.apis.io/dinilu-us/well-known/dinilu-us-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dinilu-us-security.txt
- group: agent
  href: https://artifacts.apis.io/dinilu-us/well-known/dinilu-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinilu-us-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinilu-us/hosts/dinilu-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinilu-us-hosts.yml
- group: auth
  href: https://artifacts.apis.io/dinilu-us/security/dinilu-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinilu-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinilu.us/
- group: docs
  title: ''
  type: Documentation
  url: https://dinilu.us/about-us/developers
- group: docs
  title: ''
  type: APIReference
  url: https://dinilu.us/about-us/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://dinilu.us/about-us/developers
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite public developer portal.
  evidence:
  - status: 200
    url: https://dinilu.us/about-us/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dinilu Promotional & Printed Products is a supplier of quality promotional items and printed matter from the Far East, offering online quotations, worldwide shipping, and customized branding solutions for businesses. Established in 2024, the Guangzhou‑based corporation provides a range of products including advertising specialties, logo gifts, and disposable items, ensuring competitive prices, quality control, and reliable delivery to customers worldwide.
image: https://cdn.dinilu.us/art/dinilu-1200x1200.png
json_schemas:
- name: GetApiProductMpnResponse
  property_count: 7
  slug: dinilu-us-get-api-product-mpn-response
- name: GetApiProductsResponse
  property_count: 5
  slug: dinilu-us-get-api-products-response
- name: GetApiQuoteResponse
  property_count: 12
  slug: dinilu-us-get-api-quote-response
- name: PostApiQuoteRequest
  property_count: 5
  slug: dinilu-us-post-api-quote-request
- name: PostApiQuoteResponse
  property_count: 12
  slug: dinilu-us-post-api-quote-response
jsonld:
- class_count: 5
  name: Dinilu Us Context
  property_count: 23
  slug: dinilu-us-context
layout: provider
modified: '2026-11-05'
name: Dinilu Promotional & Printed Products
nav: Providers
network: true
overview: 'Dinilu Promotional & Printed Products is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Promotional, Printing, Supplier, and Guangzhou.


  The Dinilu Promotional & Printed Products catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dinilu Promotional & Printed Products'' developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 10
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
  slug: dinilu-us-rules
score:
  band: emerging
  composite: 20.9
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
    developer_ergonomics: 28.6
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
  name: Dinilu Us Domain Security
  slug: dinilu-us-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dinilu-us
tags:
- Company
- Promotional
- Printing
- Supplier
- Guangzhou
website: https://dinilu.us/
---
