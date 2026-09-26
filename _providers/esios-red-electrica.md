---
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
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-09-25'
api_count: 2
apis:
- description: 'Red Electrica (e-sios) archive API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Red Electrica (e-sios) archive API
  slug: archive-api
- description: 'Red Electrica (e-sios) content API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Red Electrica (e-sios) content API
  slug: content-api
artifact_total: 23
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/rules/esios-red-electrica-rules.yml
  title: ''
  type: Spectral
  url: rules/esios-red-electrica-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/json-ld/esios-red-electrica-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/esios-red-electrica-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/vocabulary/esios-red-electrica-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/esios-red-electrica-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/data-model/esios-red-electrica-data-model.yml
  title: ''
  type: DataModel
  url: data-model/esios-red-electrica-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/conformance/esios-red-electrica-conformance.yml
  title: ''
  type: Conformance
  url: conformance/esios-red-electrica-conformance.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.esios.ree.es
- group: start
  title: ''
  type: GettingStarted
  url: https://www.esios.ree.es/es/token
- group: docs
  title: ''
  type: APIReference
  url: https://api.esios.ree.es
- group: start
  title: ''
  type: GettingStarted
  url: https://www.esios.ree.es/es/token
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/security/esios-red-electrica-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/esios-red-electrica-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/well-known/esios-red-electrica-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/esios-red-electrica-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/well-known/esios-red-electrica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/esios-red-electrica-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/vendors/esios-red-electrica-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esios-red-electrica-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/security/esios-red-electrica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/esios-red-electrica-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/esios-red-electrica/refs/heads/main/security/esios-red-electrica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esios-red-electrica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esios.ree.es/
- group: docs
  title: ''
  type: Documentation
  url: https://www.esios.ree.es/es/documentacion
- group: company
  title: ''
  type: About
  url: https://www.esios.ree.es/es/acerca-de-esios
- group: operate
  title: ''
  type: Support
  url: https://www.esios.ree.es/es/ayuda-preguntas-frecuentes
- group: operate
  title: ''
  type: Contact
  url: https://www.esios.ree.es/es/contacto
- group: docs
  title: ''
  type: APIReference
  url: https://api.esios.ree.es
- group: start
  title: ''
  type: GettingStarted
  url: https://www.esios.ree.es/es/token
- group: docs
  title: ''
  type: APIReference
  url: https://api.esios.ree.es
- group: start
  title: ''
  type: GettingStarted
  url: https://www.esios.ree.es/es/token
coverage:
  checked: 2026-09-22
  detail: The developer portal returns HTML pages and a 403 for /openapi.json, providing no machine‑readable specification.
  evidence:
  - status: 200
    url: https://www.esios.ree.es/developer/api
  - status: 403
    url: https://api.esios.ree.es/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Red Electrica (e-sios) operates the Spanish electricity market data platform ESIOS, providing transparent access to generation, consumption, market prices, demand forecasts, and system operation metrics. The service offers extensive datasets through a public API, supporting developers, analysts, and energy stakeholders in building applications, visualizations, and research tools. It emphasizes open data, regulatory compliance, and real‑time updates, fostering innovation in the energy sector.
json_schemas:
- name: GetArchivesArchiveidArchiveididResponse
  property_count: 3
  slug: esios-red-electrica-get-archives-archiveid-archiveidid-response
- name: GetArchivesJsonResponse
  property_count: 2
  slug: esios-red-electrica-get-archives-json-response
- name: GetArchivesResponse
  property_count: 2
  slug: esios-red-electrica-get-archives-response
- name: GetArchives3179Response
  property_count: 1
  slug: esios-red-electrica-get-archives3179-response
- name: GetArchives3183DownloadJsonResponse
  property_count: 3
  slug: esios-red-electrica-get-archives3183-download-json-response
- name: GetArchives3186Response
  property_count: 1
  slug: esios-red-electrica-get-archives3186-response
- name: GetCalculatorData72Response
  property_count: 1
  slug: esios-red-electrica-get-calculator-data72-response
- name: GetContentsContentidResponse
  property_count: 2
  slug: esios-red-electrica-get-contents-contentid-response
- name: GetEsDocumentationsResponse
  property_count: 2
  slug: esios-red-electrica-get-es-documentations-response
- name: GetEsEidContent3Response
  property_count: 2
  slug: esios-red-electrica-get-es-eid-content3-response
- name: GetEsEidResponse
  property_count: 2
  slug: esios-red-electrica-get-es-eid-response
- name: GetEsGlossariesResponse
  property_count: 2
  slug: esios-red-electrica-get-es-glossaries-response
- name: GetEsMapsResponse
  property_count: 2
  slug: esios-red-electrica-get-es-maps-response
- name: GetEsNewsResponse
  property_count: 2
  slug: esios-red-electrica-get-es-news-response
- name: GetEsStaticPagesResponse
  property_count: 2
  slug: esios-red-electrica-get-es-static-pages-response
- name: GetEsUmmsResponse
  property_count: 2
  slug: esios-red-electrica-get-es-umms-response
- name: GetIdResponse
  property_count: 2
  slug: esios-red-electrica-get-id-response
jsonld:
- class_count: 18
  name: Esios Red Electrica Context
  property_count: 3
  slug: esios-red-electrica-context
layout: provider
modified: '2026-09-22'
name: Red Electrica (e-sios)
nav: Providers
network: true
overview: 'Red Electrica (e-sios) publishes 2 APIs on the [APIs.io](https://apis.io/) network: archive API and content API. Tagged areas include Company, Energy, Data, and Spain.


  The Red Electrica (e-sios) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Red Electrica (e-sios)''s developer surface includes API reference, getting-started guide, documentation, support, and 20 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Red Electrica (e-sios) API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: esios-red-electrica-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 22.7
    developer_ergonomics: 33.3
    discoverability: 44.6
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 21.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Esios Red Electrica Domain Security
  slug: esios-red-electrica-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Esios Red Electrica Vulnerability Disclosure
  slug: esios-red-electrica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: esios-red-electrica
tags:
- Company
- Energy
- Data
- Spain
website: https://www.esios.ree.es/
---
