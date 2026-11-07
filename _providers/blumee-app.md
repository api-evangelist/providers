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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Blumee App Agentic Access
  operation_count: 7
  slug: blumee-app-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.blumee.app
  baseurl_source: declared
  description: Browse and filter the offers.
  name: Blumee Catalog API
  slug: blumee-app-catalog-api
- baseURL: https://api.blumee.app
  baseurl_source: declared
  description: Find offers by meaning or by photo. Budgeted.
  name: Blumee Search API
  slug: blumee-app-search-api
- baseURL: https://api.blumee.app
  baseurl_source: declared
  description: Liveness.
  name: Blumee Service API
  slug: blumee-app-service-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/blumee-app/agentic-access/blumee-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blumee-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/blumee-app/rules/blumee-app-rules.yml
  title: ''
  type: Spectral
  url: rules/blumee-app-rules.yml
- group: design
  href: https://artifacts.apis.io/blumee-app/json-ld/blumee-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blumee-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/blumee-app/vocabulary/blumee-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blumee-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blumee-app/data-model/blumee-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blumee-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/blumee-app/errors/blumee-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blumee-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blumee-app/conformance/blumee-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blumee-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blumee-app/llms/blumee-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blumee-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/blumee-app/well-known/blumee-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blumee-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/blumee-app/hosts/blumee-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blumee-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/blumee-app/vendors/blumee-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blumee-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/blumee-app/security/blumee-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blumee-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blumee.app/
created: '2026-11-02'
description: Blumee is an online flower delivery service that lets users find and compare bouquets and potted plants from vetted partner florists, order via photo, voice, or description, and be directed to the shop. The platform operates in Germany and offers apps for iOS and Android, with a focus on quality and convenience for sending flowers.
json_schemas:
- name: CatalogFacets
  property_count: 6
  slug: blumee-app-catalog-facets
- name: CatalogStats
  property_count: 8
  slug: blumee-app-catalog-stats
- name: PhotoSearchResponse
  property_count: 7
  slug: blumee-app-photo-search-response
- name: ProductDetail
  property_count: 23
  slug: blumee-app-product-detail
- name: TextSearchRequest
  property_count: 4
  slug: blumee-app-text-search-request
- name: TextSearchResponse
  property_count: 5
  slug: blumee-app-text-search-response
jsonld:
- class_count: 22
  name: Blumee App Context
  property_count: 89
  slug: blumee-app-context
layout: provider
modified: '2026-11-02'
name: Blumee
nav: Providers
network: true
overview: 'Blumee publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API, Search API, and Service API. Tagged areas include Flower Delivery, E-Commerce, Germany, Mobile App, and Online Shopping.


  The Blumee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Blumee API Rules
  rule_count: 65
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 2
  slug: blumee-app-rules
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 62.4
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
  name: Blumee App Domain Security
  slug: blumee-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blumee-app
tags:
- Flower Delivery
- E-Commerce
- Germany
- Mobile App
- Online Shopping
website: https://blumee.app/
---
