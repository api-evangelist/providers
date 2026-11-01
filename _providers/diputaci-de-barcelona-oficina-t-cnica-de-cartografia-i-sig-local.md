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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local/hosts/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local-hosts.yml
- group: auth
  href: https://artifacts.apis.io/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local/security/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.diba.cat/
coverage:
  checked: '2026-10-26'
  detail: The provider's documentation site renders content via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.diba.cat/ca/inici
  - status: 301
    url: https://www.diba.cat/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: The Diputació de Barcelona – Oficina Tècnica de Cartografia i SIG Local is the technical office of the Barcelona Provincial Council responsible for cartography, geographic information systems, and spatial data services. It supports the 311 municipalities of the province with mapping, land‑use data, and geospatial analysis tools, fostering local government transparency and citizen services through open data initiatives.
layout: provider
modified: '2026-10-26'
name: Diputació de Barcelona-Oficina Tècnica de Cartografia i Sig Local
nav: Providers
network: true
overview: Diputació de Barcelona-Oficina Tècnica de Cartografia i Sig Local is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, GIS, Cartography, and OpenData.
random_paper: 3
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diputaci De Barcelona Oficina T Cnica De Cartografia I Sig Local Domain Security
  slug: diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: diputaci-de-barcelona-oficina-t-cnica-de-cartografia-i-sig-local
tags:
- Company
- Government
- GIS
- Cartography
- OpenData
website: https://www.diba.cat/
---
