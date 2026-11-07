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
api_count: 1
apis:
- baseURL: https://brujula.day
  baseurl_source: declared
  description: 'Brújula API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Brújula API
  slug: brujula-day-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/brujula-day/rules/brujula-day-rules.yml
  title: ''
  type: Spectral
  url: rules/brujula-day-rules.yml
- group: design
  href: https://artifacts.apis.io/brujula-day/json-ld/brujula-day-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brujula-day-context.jsonld
- group: design
  href: https://artifacts.apis.io/brujula-day/vocabulary/brujula-day-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brujula-day-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/brujula-day/data-model/brujula-day-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brujula-day-data-model.yml
- group: design
  href: https://artifacts.apis.io/brujula-day/conformance/brujula-day-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brujula-day-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brujula-day/well-known/brujula-day-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brujula-day-well-known.yml
- group: other
  href: https://artifacts.apis.io/brujula-day/hosts/brujula-day-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brujula-day-hosts.yml
- group: other
  href: https://artifacts.apis.io/brujula-day/vendors/brujula-day-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brujula-day-vendors.yml
- group: auth
  href: https://artifacts.apis.io/brujula-day/security/brujula-day-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brujula-day-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brujula.day/
coverage:
  checked: '2026-11-03'
  detail: The provider's website offers no public machine‑readable API specification.
  evidence:
  - status: 200
    url: https://brujula.day/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Brújula es una plataforma que centraliza la gestión de la vida cotidiana, ofreciendo herramientas para organizar tareas, calendario, gastos, proyectos, recetas y turnos, todo desde un solo lugar. Los usuarios pueden interactuar vía WhatsApp, facilitando la anotación y seguimiento de actividades. La solución está diseñada para simplificar la planificación personal y familiar, proporcionando una experiencia integrada y accesible.
image: https://brujula.day/icons/compartir.png
json_schemas:
- name: PostApiV1TareasRequest
  property_count: 4
  slug: brujula-day-post-api-v1-tareas-request
- name: PostGastosRequest
  property_count: 9
  slug: brujula-day-post-gastos-request
- name: PostIngresosRequest
  property_count: 5
  slug: brujula-day-post-ingresos-request
- name: PostListasItemsRequest
  property_count: 3
  slug: brujula-day-post-listas-items-request
- name: PostMensajeResponse
  property_count: 2
  slug: brujula-day-post-mensaje-response
- name: PostTareasRequest
  property_count: 9
  slug: brujula-day-post-tareas-request
jsonld:
- class_count: 9
  name: Brujula Day Context
  property_count: 20
  slug: brujula-day-context
layout: provider
modified: '2026-11-03'
name: Brújula
nav: Providers
network: true
overview: 'Brújula is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Productivity, Organization, Lifestyle, Spanish, and Mobile.


  The Brújula catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: Brújula API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: brujula-day-rules
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brujula Day Domain Security
  slug: brujula-day-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: brujula-day
tags:
- Productivity
- Organization
- Lifestyle
- Spanish
- Mobile
website: https://brujula.day/
---
