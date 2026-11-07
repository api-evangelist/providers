---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Boletinclaro Es Agentic Access
  operation_count: 15
  slug: boletinclaro-es-agentic-access
  summary_line: 15 operations · 3 acting
api_count: 1
apis:
- baseURL: https://boletinclaro.es/v1
  baseurl_source: declared
  description: The Boletines API from Boletín Claro — 1 operation(s) for boletines.
  name: Boletín Claro Boletines API
  slug: boletinclaro-es-boletines-api
- baseURL: https://boletinclaro.es/v1
  baseurl_source: declared
  description: The Códigos API from Boletín Claro — 1 operation(s) for códigos.
  name: Boletín Claro Códigos API
  slug: boletinclaro-es-c-digos-api
- baseURL: https://boletinclaro.es/v1
  baseurl_source: declared
  description: The Dinero público API from Boletín Claro — 2 operation(s) for dinero público.
  name: Boletín Claro Dinero público API
  slug: boletinclaro-es-dinero-p-blico-api
- baseURL: https://boletinclaro.es/v1
  baseurl_source: declared
  description: The Empresas API from Boletín Claro — 2 operation(s) for empresas.
  name: Boletín Claro Empresas API
  slug: boletinclaro-es-empresas-api
- baseURL: https://boletinclaro.es/v1
  baseurl_source: declared
  description: The Referencia API from Boletín Claro — 6 operation(s) for referencia.
  name: Boletín Claro Referencia API
  slug: boletinclaro-es-referencia-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/boletinclaro-es/agentic-access/boletinclaro-es-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boletinclaro-es-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/rules/boletinclaro-es-rules.yml
  title: ''
  type: Spectral
  url: rules/boletinclaro-es-rules.yml
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/json-ld/boletinclaro-es-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/boletinclaro-es-context.jsonld
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/vocabulary/boletinclaro-es-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boletinclaro-es-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/boletinclaro-es/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/data-model/boletinclaro-es-data-model.yml
  title: ''
  type: DataModel
  url: data-model/boletinclaro-es-data-model.yml
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/errors/boletinclaro-es-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boletinclaro-es-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boletinclaro-es/conformance/boletinclaro-es-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boletinclaro-es-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boletinclaro-es/llms/boletinclaro-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boletinclaro-es-llms.txt
- group: agent
  href: https://artifacts.apis.io/boletinclaro-es/well-known/boletinclaro-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boletinclaro-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/boletinclaro-es/hosts/boletinclaro-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boletinclaro-es-hosts.yml
- group: other
  href: https://artifacts.apis.io/boletinclaro-es/vendors/boletinclaro-es-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boletinclaro-es-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://boletinclaro.es/blog
- group: auth
  href: https://artifacts.apis.io/boletinclaro-es/authentication/boletinclaro-es-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boletinclaro-es-authentication.yml
- group: auth
  href: https://artifacts.apis.io/boletinclaro-es/security/boletinclaro-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boletinclaro-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boletinclaro.es/
created: '2026-11-02'
description: Boletín Claro monitors 28 official Spanish and European bulletins and sends email alerts for relevant subsidies, tenders, and regulatory changes affecting businesses. Founded in 2026, it serves Spain with daily updates sourced from the BOE and regional publications, offering a no‑commitment service.
image: https://boletinclaro.es/og-image.png
json_schemas:
- name: Empresa
  property_count: 17
  slug: boletinclaro-es-empresa
- name: RespuestaCodigos
  property_count: 4
  slug: boletinclaro-es-respuesta-codigos
- name: RespuestaEmpresas
  property_count: 4
  slug: boletinclaro-es-respuesta-empresas
- name: RespuestaEntradas
  property_count: 4
  slug: boletinclaro-es-respuesta-entradas
jsonld:
- class_count: 13
  name: Boletinclaro Es Context
  property_count: 58
  slug: boletinclaro-es-context
layout: provider
modified: '2026-11-02'
name: Boletín Claro
nav: Providers
network: true
overview: 'Boletín Claro publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Boletines API, Códigos API, Dinero público API, and 2 more. Tagged areas include Company, Software-as-a-Service, Alerts, Spain, and Government.


  The Boletín Claro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Boletín Claro''s developer surface includes engineering blog, authentication, and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: Boletín Claro API Rules
  rule_count: 72
  severity_counts:
    error: 70
    hint: 0
    info: 1
    warn: 1
  slug: boletinclaro-es-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 67.4
    developer_ergonomics: 14.9
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boletinclaro Es Authentication
  slug: boletinclaro-es-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Boletinclaro Es Domain Security
  slug: boletinclaro-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: boletinclaro-es-search-boletines
  slug: boletinclaro-es-search-boletines
- name: boletinclaro-es-search-opportunities
  slug: boletinclaro-es-search-opportunities
slug: boletinclaro-es
tags:
- Company
- Software-as-a-Service
- Alerts
- Spain
- Government
website: https://boletinclaro.es/
---
