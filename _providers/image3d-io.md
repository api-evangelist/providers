---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic API to generate 3D models from images or text prompts, as described in the API Beta Documentation.
  name: Image3D API
  slug: image3d-api
- description: 'Image3D API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Image3D API
  slug: image3d-io-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/image3d-io/plans/image3d-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/image3d-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/image3d-io/rules/image3d-io-rules.yml
  title: ''
  type: Spectral
  url: rules/image3d-io-rules.yml
- group: design
  href: https://artifacts.apis.io/image3d-io/json-ld/image3d-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/image3d-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/image3d-io/vocabulary/image3d-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/image3d-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/image3d-io/data-model/image3d-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/image3d-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/image3d-io/changelog/image3d-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/image3d-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/image3d-io/conformance/image3d-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/image3d-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/image3d-io/llms/image3d-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/image3d-io-llms.txt
- group: other
  href: https://artifacts.apis.io/image3d-io/hosts/image3d-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/image3d-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/image3d-io/vendors/image3d-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/image3d-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://image3d.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://image3d.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://image3d.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://image3d.io/login/
- group: docs
  title: ''
  type: Documentation
  url: https://image3d.io/docs/
- group: operate
  title: ''
  type: ChangeLog
  url: https://image3d.io/changelog/
- group: company
  title: ''
  type: Blog
  url: https://image3d.io/blog/
- group: auth
  href: https://artifacts.apis.io/image3d-io/security/image3d-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/image3d-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://image3d.io/
coverage:
  checked: '2026-11-04'
  detail: API documentation is HTML only with no OpenAPI/Swagger JSON/YAML available.
  evidence:
  - status: 200
    url: https://image3d.io/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Image3D provides an AI‑powered platform that converts images or text prompts into 3D models directly in the browser. Users can preview meshes, adjust them, and export in formats such as OBJ, STL, GLB, or PLY. The service offers free public examples and paid subscription plans with credit allowances for creators and professionals.
image: https://image3d.io/assets/showcase-before-astronaut.jpg
json_schemas:
- name: GetApiV1BalanceResponse
  property_count: 5
  slug: image3d-io-get-api-v1-balance-response
- name: PostApiCreateCheckoutSessionRequest
  property_count: 4
  slug: image3d-io-post-api-create-checkout-session-request
- name: PostApiTextureRequest
  property_count: 3
  slug: image3d-io-post-api-texture-request
- name: PostApiTextureResponse
  property_count: 2
  slug: image3d-io-post-api-texture-response
- name: PostApiV1GenerationsRequest
  property_count: 3
  slug: image3d-io-post-api-v1-generations-request
jsonld:
- class_count: 5
  name: Image3D Io Context
  property_count: 15
  slug: image3d-io-context
layout: provider
modified: '2026-11-04'
name: Image3D
nav: Providers
network: true
overview: 'Image3D is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, 3D, Image-to-3D, and Software-as-a-Service.


  The Image3D catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Image3D''s developer surface includes changelog, pricing, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Image3D Io Plans Pricing
  plan_count: 3
  slug: image3d-io-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Image3D API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: image3d-io-rules
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Image3D Io Domain Security
  slug: image3d-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: image3d-io
tags:
- Company
- Artificial Intelligence
- 3D
- Image-to-3D
- Software-as-a-Service
- Graphics
website: https://image3d.io/
---
