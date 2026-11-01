---
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Mocki provides mock API endpoints for testing and development.
  name: Mocki API
  slug: mocki-api-2
- description: 'Mocki API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: Mocki API
  slug: mocki-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/mocki/rules/mocki-rules.yml
  title: ''
  type: Spectral
  url: rules/mocki-rules.yml
- group: design
  href: https://artifacts.apis.io/mocki/json-ld/mocki-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mocki-context.jsonld
- group: design
  href: https://artifacts.apis.io/mocki/vocabulary/mocki-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mocki-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mocki/data-model/mocki-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mocki-data-model.yml
- group: start
  href: https://artifacts.apis.io/mocki/sandbox/mocki-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mocki-sandbox.yml
- group: design
  href: https://artifacts.apis.io/mocki/conformance/mocki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mocki-conformance.yml
- group: other
  href: https://artifacts.apis.io/mocki/hosts/mocki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mocki-hosts.yml
- group: other
  href: https://artifacts.apis.io/mocki/vendors/mocki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mocki-vendors.yml
- group: build
  href: https://artifacts.apis.io/mocki/packages/mocki-packages.yml
  title: ''
  type: SDKs
  url: packages/mocki-packages.yml
- group: build
  href: https://artifacts.apis.io/mocki/packages/mocki-packages.yml
  title: ''
  type: Packages
  url: packages/mocki-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mocki.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mocki.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://mocki.io/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://mocki.io/docs
- group: company
  title: ''
  type: Blog
  url: https://mocki.io/blog
- group: auth
  href: https://artifacts.apis.io/mocki/security/mocki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mocki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mocki.io/
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://mocki.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: Mocki provides a SaaS platform for creating, running, and deploying mock APIs to aid developers in testing, designing, and simulating API behavior. Users can design static responses, simulate error scenarios, and eliminate dependencies on external services, with a free 7‑day trial and easy integration into development workflows.
json_schemas:
- name: GetV1D4867D8BB5D54A48A4Ab79131B5809B8Response
  property_count: 2
  slug: mocki-get-v1-d4867-d8-bb5-d54-a48-a4-ab79131-b5809-b8-response
- name: PostRequest
  property_count: 1
  slug: mocki-post-request
jsonld:
- class_count: 2
  name: Mocki Context
  property_count: 3
  slug: mocki-context
layout: provider
modified: '2026-10-18'
name: Mocki
nav: Providers
network: true
overview: 'Mocki is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Mock API, Testing, and Development.


  The Mocki catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mocki''s developer surface includes sandbox, pricing, documentation, engineering blog, and 13 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Mocki API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: mocki-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 26.2
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mocki Domain Security
  slug: mocki-domain-security
  summary_line: TLSv1.3
slug: mocki
tags:
- Company
- Software-as-a-Service
- Mock API
- Testing
- Development
website: https://mocki.io/
---
