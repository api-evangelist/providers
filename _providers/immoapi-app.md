---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API providing French real‑estate transaction data (DVF).
  name: Immo API DVF
  slug: immo-api-dvf
- description: 'immoapi-app API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: immoapi-app API
  slug: immoapi-app-api
artifact_total: 14
common:
- group: operate
  href: https://artifacts.apis.io/immoapi-app/rate-limits/immoapi-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/immoapi-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/immoapi-app/plans/immoapi-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/immoapi-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/rules/immoapi-app-rules.yml
  title: ''
  type: Spectral
  url: rules/immoapi-app-rules.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/json-ld/immoapi-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/immoapi-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/immoapi-app/vocabulary/immoapi-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/immoapi-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/data-model/immoapi-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/immoapi-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/conventions/immoapi-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/immoapi-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/immoapi-app/authentication/immoapi-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/immoapi-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/errors/immoapi-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/immoapi-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/immoapi-app/conformance/immoapi-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/immoapi-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/immoapi-app/llms/immoapi-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/immoapi-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/immoapi-app/well-known/immoapi-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/immoapi-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/immoapi-app/hosts/immoapi-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/immoapi-app-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://immoapi.app/login
- group: auth
  href: https://artifacts.apis.io/immoapi-app/security/immoapi-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/immoapi-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://immoapi.app/
- group: docs
  title: ''
  type: Documentation
  url: https://immoapi.app/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://immoapi.app/tarifs
- group: company
  title: ''
  type: Blog
  url: https://immoapi.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://immoapi.app/guides
- group: docs
  title: ''
  type: APIReference
  url: https://immoapi.app/documentation
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec extraction.
  evidence:
  - status: 200
    url: https://immoapi.app/guides
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Immo API provides a public REST and MCP API delivering official French real‑estate transaction data (DVF – Demandes de Valeurs Foncières). Users can query property sales, prices per square meter, and statistical information by commune, department or region. The service offers detailed documentation, pricing plans, guides, and a blog, and is hosted in France. It aims to facilitate developers, analysts, and public‑sector applications needing up‑to‑date property transaction data.
image: https://immoapi.app/icon.svg
json_schemas:
- name: GetApiMutationsNearbyResponse
  property_count: 4
  slug: immoapi-app-get-api-mutations-nearby-response
- name: GetApiMutationsResponse
  property_count: 2
  slug: immoapi-app-get-api-mutations-response
- name: GetApiStatsResponse
  property_count: 7
  slug: immoapi-app-get-api-stats-response
- name: PostApiMcpRequest
  property_count: 3
  slug: immoapi-app-post-api-mcp-request
- name: PostApiMutationsRequest
  property_count: 3
  slug: immoapi-app-post-api-mutations-request
jsonld:
- class_count: 5
  name: Immoapi App Context
  property_count: 14
  slug: immoapi-app-context
layout: provider
modified: '2026-10-30'
name: immoapi-app
nav: Providers
network: true
overview: 'immoapi-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, France, Data, Open Data, and Property.


  The immoapi-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  immoapi-app''s developer surface includes authentication, documentation, pricing, engineering blog, getting-started guide, API reference, and 15 more developer resources.'
plans:
- name: Immoapi App Plans Pricing
  plan_count: 2
  slug: immoapi-app-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Immoapi App Rate Limits
  slug: immoapi-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: immoapi-app API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: immoapi-app-rules
scopes:
- name: Immoapi App Scopes
  scope_count: 0
  slug: immoapi-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 73.8
    catalog_earned_first_party: 16.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 27.4
    discoverability: 57.1
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 36.9
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
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/immoapi-app/immoapi-app-2026-11-03T133712.png
security:
- kind: authentication
  name: Immoapi App Authentication
  slug: immoapi-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Immoapi App Domain Security
  slug: immoapi-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: immoapi-app
tags:
- Real Estate
- France
- Data
- Open Data
- Property
website: https://immoapi.app/
---
