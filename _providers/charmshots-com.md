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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation is not publicly machine‑readable; the provider offers guides at the URL below but no OpenAPI/AsyncAPI/GraphQL spec.
  name: Charmshots API
  slug: charmshots-api
- description: 'Charmshots API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Charmshots API
  slug: charmshots-com-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/charmshots-com/plans/charmshots-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/charmshots-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/charmshots-com/rules/charmshots-com-rules.yml
  title: ''
  type: Spectral
  url: rules/charmshots-com-rules.yml
- group: design
  href: https://artifacts.apis.io/charmshots-com/json-ld/charmshots-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/charmshots-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/charmshots-com/vocabulary/charmshots-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/charmshots-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/charmshots-com/data-model/charmshots-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/charmshots-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/charmshots-com/conformance/charmshots-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/charmshots-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/charmshots-com/llms/charmshots-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/charmshots-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/charmshots-com/well-known/charmshots-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/charmshots-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/charmshots-com/hosts/charmshots-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/charmshots-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/charmshots-com/vendors/charmshots-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/charmshots-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/charmshots-com/packages/charmshots-com-packages.yml
  title: ''
  type: SDKs
  url: packages/charmshots-com-packages.yml
- group: build
  href: https://artifacts.apis.io/charmshots-com/packages/charmshots-com-packages.yml
  title: ''
  type: Packages
  url: packages/charmshots-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://charmshots.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://charmshots.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/charmshots
- group: auth
  href: https://artifacts.apis.io/charmshots-com/security/charmshots-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/charmshots-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://charmshots.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://charmshots.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://charmshots.com/guides/
- group: start
  title: ''
  type: GettingStarted
  url: https://charmshots.com/score/
coverage:
  checked: '2026-11-03'
  detail: Provider documentation is public but offers no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://charmshots.com/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Charmshots provides AI-generated dating photos from user selfies, creating natural-looking images for platforms like Hinge, Tinder, and Bumble. Users can select from 31 real-life scenes, with one-time purchase packs starting at $12, no subscription required. The service aims to enhance online dating profiles with high-quality, personalized photos quickly.
image: https://charmshots.com/social.png
json_schemas:
- name: GetV1AccountResponse
  property_count: 1
  slug: charmshots-com-get-v1-account-response
- name: GetV1PhotoshootsPhotoshootidPhotosResponse
  property_count: 1
  slug: charmshots-com-get-v1-photoshoots-photoshootid-photos-response
- name: GetV1PhotoshootsPhotoshootidResponse
  property_count: 1
  slug: charmshots-com-get-v1-photoshoots-photoshootid-response
- name: GetV1PhotoshootsResponse
  property_count: 1
  slug: charmshots-com-get-v1-photoshoots-response
jsonld:
- class_count: 4
  name: Charmshots Com Context
  property_count: 3
  slug: charmshots-com-context
layout: provider
modified: '2026-11-03'
name: Charmshots
nav: Providers
network: true
overview: 'Charmshots is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Photography, Dating, Selfie, and Image Generation.


  The Charmshots catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Charmshots'' developer surface includes pricing, documentation, getting-started guide, and 17 more developer resources.'
plans:
- name: Charmshots Com Plans Pricing
  plan_count: 3
  slug: charmshots-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 72
  extends:
  - spectral:oas
  name: Charmshots API Rules
  rule_count: 31
  severity_counts:
    error: 29
    hint: 0
    info: 1
    warn: 1
  slug: charmshots-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 17.9
    discoverability: 57.1
    operational_transparency: 2.6
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
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Charmshots Com Domain Security
  slug: charmshots-com-domain-security
  summary_line: TLSv1.3
slug: charmshots-com
tags:
- Artificial Intelligence
- Photography
- Dating
- Selfie
- Image Generation
website: https://charmshots.com/
---
