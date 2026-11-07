---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alfil Co Agentic Access
  operation_count: 19
  slug: alfil-co-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Búsqueda API from Alfil — 1 operation(s) for búsqueda.
  name: Alfil Búsqueda API
  slug: alfil-co-b-squeda-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Congreso API from Alfil — 5 operation(s) for congreso.
  name: Alfil Congreso API
  slug: alfil-co-congreso-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Contratación API from Alfil — 4 operation(s) for contratación.
  name: Alfil Contratación API
  slug: alfil-co-contrataci-n-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Electoral API from Alfil — 4 operation(s) for electoral.
  name: Alfil Electoral API
  slug: alfil-co-electoral-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Finanzas API from Alfil — 1 operation(s) for finanzas.
  name: Alfil Finanzas API
  slug: alfil-co-finanzas-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Geografías API from Alfil — 1 operation(s) for geografías.
  name: Alfil Geografías API
  slug: alfil-co-geograf-as-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Partidos API from Alfil — 1 operation(s) for partidos.
  name: Alfil Partidos API
  slug: alfil-co-partidos-api
- baseURL: https://api.alfil.co
  baseurl_source: declared
  description: The Políticos API from Alfil — 2 operation(s) for políticos.
  name: Alfil Políticos API
  slug: alfil-co-pol-ticos-api
artifact_total: 23
common:
- group: auth
  href: https://artifacts.apis.io/alfil-co/well-known/alfil-co-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alfil-co-www-security.txt
- group: agent
  href: https://artifacts.apis.io/alfil-co/agentic-access/alfil-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alfil-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/alfil-co/rules/alfil-co-rules.yml
  title: ''
  type: Spectral
  url: rules/alfil-co-rules.yml
- group: design
  href: https://artifacts.apis.io/alfil-co/json-ld/alfil-co-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alfil-co-context.jsonld
- group: design
  href: https://artifacts.apis.io/alfil-co/vocabulary/alfil-co-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alfil-co-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/alfil-co/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/alfil-co/data-model/alfil-co-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alfil-co-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://alfil.co/tos
- group: design
  href: https://artifacts.apis.io/alfil-co/errors/alfil-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alfil-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alfil-co/conformance/alfil-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alfil-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/alfil-co/llms/alfil-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alfil-co-llms.txt
- group: auth
  href: https://artifacts.apis.io/alfil-co/well-known/alfil-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alfil-co-security.txt
- group: auth
  href: https://artifacts.apis.io/alfil-co/well-known/alfil-co-alfil-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alfil-co-alfil-security.txt
- group: agent
  href: https://artifacts.apis.io/alfil-co/well-known/alfil-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alfil-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/alfil-co/hosts/alfil-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alfil-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/alfil-co/vendors/alfil-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alfil-co-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.alfil.co/login
- group: auth
  href: https://artifacts.apis.io/alfil-co/security/alfil-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alfil-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alfil-co/security/alfil-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alfil-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alfil.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alfil.co/tos
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.alfil.co/openapi.json
  - status: 401
    url: https://api.alfil.co/mcp
  - status: 401
    url: https://alfil.co/api/graphql
  - status: 401
    url: https://alfil.co/api/mcp
  - status: 401
    url: https://www.alfil.co/api/graphql
  - status: 401
    url: https://www.alfil.co/api/mcp
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Alfil provides a catalog of editorial investigations, electoral data, public contract analysis, and political tools to understand Colombian politics. The platform aggregates information from sources such as Registraduría, SECOP, and Congreso, offering searchable profiles of politicians, contracts, and voting behavior.
image: https://www.alfil.co/opengraph-image
json_schemas:
- name: ContratoAdicionesResponse
  property_count: 2
  slug: alfil-co-contrato-adiciones-response
- name: Contrato
  property_count: 11
  slug: alfil-co-contrato
- name: ElectoralCenso
  property_count: 9
  slug: alfil-co-electoral-censo
- name: PoliticoPerfil
  property_count: 0
  slug: alfil-co-politico-perfil
- name: ProcesoContratacion
  property_count: 2
  slug: alfil-co-proceso-contratacion
- name: VotoDetalle
  property_count: 8
  slug: alfil-co-voto-detalle
jsonld:
- class_count: 50
  name: Alfil Co Context
  property_count: 113
  slug: alfil-co-context
layout: provider
modified: '2026-11-01'
name: Alfil
nav: Providers
network: true
overview: 'Alfil publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Búsqueda API, Congreso API, Contratación API, and 5 more. Tagged areas include Politics, Colombia, Elections, Public Procurement, and Data Analysis.


  The Alfil catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Alfil Co Plans Pricing
  plan_count: 0
  slug: alfil-co-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Alfil Co Rate Limits
  slug: alfil-co-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Alfil API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: alfil-co-rules
scopes:
- name: Alfil Co Scopes
  scope_count: 0
  slug: alfil-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 62.1
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - colombia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alfil Co Authentication
  slug: alfil-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alfil Co Domain Security
  slug: alfil-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alfil Co Vulnerability Disclosure
  slug: alfil-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alfil-co
tags:
- Politics
- Colombia
- Elections
- Public Procurement
- Data Analysis
- Intelligence
website: https://alfil.co/
---
