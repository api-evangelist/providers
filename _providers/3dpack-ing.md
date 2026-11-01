---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: 3Dpack Ing Agentic Access
  operation_count: 6
  slug: 3dpack-ing-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://3dpack.ing
  baseurl_source: declared
  description: The packing API from 3dpack-ing — 1 operation(s) for packing.
  name: 3dpack-ing Packing API
  slug: 3dpack-ing-packing-api
- baseURL: https://3dpack.ing
  baseurl_source: declared
  description: The typed API from 3dpack-ing — 2 operation(s) for typed.
  name: 3dpack-ing Typed API
  slug: 3dpack-ing-typed-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/3dpack-ing/agentic-access/3dpack-ing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/3dpack-ing-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/3dpack-ing/rules/3dpack-ing-rules.yml
  title: ''
  type: Spectral
  url: rules/3dpack-ing-rules.yml
- group: design
  href: https://artifacts.apis.io/3dpack-ing/json-ld/3dpack-ing-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/3dpack-ing-context.jsonld
- group: design
  href: https://artifacts.apis.io/3dpack-ing/vocabulary/3dpack-ing-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/3dpack-ing-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/3dpack-ing/data-model/3dpack-ing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/3dpack-ing-data-model.yml
- group: design
  href: https://artifacts.apis.io/3dpack-ing/errors/3dpack-ing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/3dpack-ing-problem-types.yml
- group: design
  href: https://artifacts.apis.io/3dpack-ing/conformance/3dpack-ing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/3dpack-ing-conformance.yml
- group: agent
  href: https://artifacts.apis.io/3dpack-ing/well-known/3dpack-ing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/3dpack-ing-well-known.yml
- group: other
  href: https://artifacts.apis.io/3dpack-ing/hosts/3dpack-ing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/3dpack-ing-hosts.yml
- group: build
  href: https://artifacts.apis.io/3dpack-ing/packages/3dpack-ing-packages.yml
  title: ''
  type: SDKs
  url: packages/3dpack-ing-packages.yml
- group: build
  href: https://artifacts.apis.io/3dpack-ing/packages/3dpack-ing-packages.yml
  title: ''
  type: Packages
  url: packages/3dpack-ing-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://3dpack.ing/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://3dpack.ing/privacy.html
- group: start
  title: ''
  type: Login
  url: https://3dpack.ing/login
- group: auth
  href: https://artifacts.apis.io/3dpack-ing/authentication/3dpack-ing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/3dpack-ing-authentication.yml
- group: auth
  href: https://artifacts.apis.io/3dpack-ing/security/3dpack-ing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/3dpack-ing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://3dpack.ing/
- group: docs
  title: ''
  type: Documentation
  url: https://3dpack.ing/api-docs.html
- group: commercial
  title: ''
  type: Pricing
  url: https://3dpack.ing/#pricing
- group: company
  title: ''
  type: Blog
  url: https://3dpack.ing/blog
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@3dpack.ing
created: '2026-10-29'
description: 3dpack-ing provides a web‑based 3D container loading calculator and an HTTP API that lets developers submit shipment descriptions in plain English and receive optimized packing plans with 3D visualizations. The service offers a free preview and paid packs for full results, targeting logistics, e‑commerce and supply‑chain applications.
image: https://3dpack.ing/assets/icons/og-image.png
json_schemas:
- name: Calculation Input
  property_count: 4
  slug: 3dpack-ing-best-boxes-request
- name: Calculation Output
  property_count: 0
  slug: 3dpack-ing-best-boxes-response
- name: PackRequest
  property_count: 5
  slug: 3dpack-ing-pack-request
- name: PackResult
  property_count: 3
  slug: 3dpack-ing-pack-result
- name: Calculation Input
  property_count: 6
  slug: 3dpack-ing-solver-calculate-request
- name: Calculation Output
  property_count: 4
  slug: 3dpack-ing-solver-calculate-response
jsonld:
- class_count: 12
  name: 3Dpack Ing Context
  property_count: 43
  slug: 3dpack-ing-context
layout: provider
modified: '2026-10-29'
name: 3dpack-ing
nav: Providers
network: true
overview: '3dpack-ing publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Packing API and Typed API. Tagged areas include Company, Logistics, 3D, API, and SaaS.


  The 3dpack-ing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  3dpack-ing''s developer surface includes authentication, documentation, pricing, engineering blog, and 17 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: 3dpack-ing API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: 3dpack-ing-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
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
- kind: authentication
  name: 3Dpack Ing Authentication
  slug: 3dpack-ing-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 3Dpack Ing Domain Security
  slug: 3dpack-ing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 3dpack-ing
tags:
- Company
- Logistics
- 3D
- API
- SaaS
website: https://3dpack.ing/
---
