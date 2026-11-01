---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: OMIE gestiona la totalidad de los mercados (diarios e intradiarios) de toda la Península Ibérica, y su modelo operativo es el mismo que el aplicado por muchos otros mercados europeos.
  name: OMIE API
  slug: omie-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/omie-es/hosts/omie-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/omie-es-hosts.yml
- group: auth
  href: https://artifacts.apis.io/omie-es/security/omie-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omie-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://omie.es/
- group: docs
  title: ''
  type: Documentation
  url: https://www.omie.es/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.omie.es/es/sobre-nosotros
- group: operate
  title: ''
  type: Support
  url: https://www.portal-asistencia.omie.es/
coverage:
  checked: '2026-10-28'
  detail: The public website provides human documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published.
  evidence:
  - status: 200
    url: https://www.omie.es/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OMIE es el operador de mercado eléctrico designado (NEMO) para la gestión del mercado diario e intradiario de electricidad en la Península Ibérica. Gestiona la totalidad de los mercados de energía en España y Portugal, participando activamente en el acoplamiento de los mercados mayoristas de la UE. Su modelo operativo es el mismo que el aplicado por muchos otros mercados europeos, ofreciendo subastas y un mercado continuo. La empresa también forma parte del Grupo OMI, proporcionando datos y servicios relacionados con la energía.
image: https://www.omie.es/sites/default/files/styles/logo/public/logo.png?itok=qTIjh2O6
layout: provider
modified: '2026-10-28'
name: OMIE (Iberian power market)
nav: Providers
network: true
overview: 'OMIE (Iberian power market) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Market, and Spain.


  OMIE (Iberian power market)''s developer surface includes documentation, getting-started guide, support, and 3 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - portugal
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Omie Es Domain Security
  slug: omie-es-domain-security
  summary_line: DMARC
slug: omie-es
tags:
- Company
- Energy
- Electricity
- Market
- Spain
- Portugal
website: https://omie.es/
---
