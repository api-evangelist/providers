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
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/well-known/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-security.txt
- group: agent
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/well-known/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-well-known.yml
- group: other
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/hosts/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-hosts.yml
  title: ''
  type: Hosts
  url: hosts/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://land.gov.ua/index.php/category/prestsentr/news/
- group: auth
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/state-service-of-ukraine-for-geodesy-cartography-and-cadastre/security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/state-service-of-ukraine-for-geodesy-cartography-and-cadastre-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://land.gov.ua/
coverage:
  checked: '2026-10-23'
  detail: The provider's website serves only JavaScript‑rendered pages with no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://land.gov.ua/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: 'The State Service of Ukraine for Geodesy, Cartography and Cadastre (Ukrainian: Державна служба України з питань геодезії, картографії та кадастру) is a governmental agency responsible for maintaining the national geodetic network, cadastral mapping, and cartographic services. It provides public access to land registry data, geographic information system (GIS) resources, and official maps, supporting urban planning, property rights, and infrastructure development across Ukraine. The agency’s digital platforms offer APIs for accessing cadastral parcels, topographic maps, and coordinate transformation services, facilitating developers, researchers, and public institutions in integrating authoritative spatial data into their applications.'
layout: provider
modified: '2026-10-23'
name: State Service of Ukraine for Geodesy, Cartography and Cadastre
nav: Providers
network: true
overview: State Service of Ukraine for Geodesy, Cartography and Cadastre is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Government, Geospatial, GIS, Cadastral, and Mapping.
random_paper: 11
score:
  band: minimal
  composite: 5.8
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
    discoverability: 46.4
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: State Service Of Ukraine For Geodesy Cartography And Cadastre Domain Security
  slug: state-service-of-ukraine-for-geodesy-cartography-and-cadastre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: State Service Of Ukraine For Geodesy Cartography And Cadastre Vulnerability Disclosure
  slug: state-service-of-ukraine-for-geodesy-cartography-and-cadastre-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: state-service-of-ukraine-for-geodesy-cartography-and-cadastre
tags:
- Government
- Geospatial
- GIS
- Cadastral
- Mapping
website: https://land.gov.ua/
---
