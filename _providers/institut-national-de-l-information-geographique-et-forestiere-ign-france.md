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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Geospatial data and map services provided by IGN, including map tiles, elevation models, and geographic data.
  name: IGN Geo Services
  slug: ign-geo-services
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/institut-national-de-l-information-geographique-et-forestiere-ign-france/hosts/institut-national-de-l-information-geographique-et-forestiere-ign-france-hosts.yml
  title: ''
  type: Hosts
  url: hosts/institut-national-de-l-information-geographique-et-forestiere-ign-france-hosts.yml
- group: other
  href: https://artifacts.apis.io/institut-national-de-l-information-geographique-et-forestiere-ign-france/vendors/institut-national-de-l-information-geographique-et-forestiere-ign-france-vendors.yml
  title: ''
  type: Vendors
  url: vendors/institut-national-de-l-information-geographique-et-forestiere-ign-france-vendors.yml
- group: auth
  href: https://artifacts.apis.io/institut-national-de-l-information-geographique-et-forestiere-ign-france/security/institut-national-de-l-information-geographique-et-forestiere-ign-france-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/institut-national-de-l-information-geographique-et-forestiere-ign-france-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.ign.fr
created: '2026-10-23'
description: The Institut National de l'Information Géographique et Forestière (IGN) is France's national mapping agency, providing free public access to a wide range of geographic data, maps, and cartographic services. It offers APIs for geospatial data, map tiles, elevation models, and location-based services, supporting developers, researchers, and public administrations in building location-aware applications. The IGN promotes open data, ensuring that geographic information is freely accessible and reusable for societal benefit.
layout: provider
modified: '2026-10-23'
name: Institut National de l'information geographique et forestiere (IGN - France)
nav: Providers
network: true
overview: Institut National de l'information geographique et forestiere (IGN - France) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mapping, Geospatial, Data, and France.
random_paper: 1
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Institut National De L Information Geographique Et Forestiere Ign France Domain Security
  slug: institut-national-de-l-information-geographique-et-forestiere-ign-france-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: institut-national-de-l-information-geographique-et-forestiere-ign-france
tags:
- Company
- Mapping
- Geospatial
- Data
- France
website: http://www.ign.fr
---
