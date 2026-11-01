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
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/camptocamp-sa/well-known/camptocamp-sa-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/camptocamp-sa-support-security.txt
- group: agent
  href: https://artifacts.apis.io/camptocamp-sa/well-known/camptocamp-sa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/camptocamp-sa-well-known.yml
- group: other
  href: https://artifacts.apis.io/camptocamp-sa/hosts/camptocamp-sa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/camptocamp-sa-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://camptocamp.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/camptocamp
- group: auth
  href: https://artifacts.apis.io/camptocamp-sa/security/camptocamp-sa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/camptocamp-sa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://camptocamp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.camptocamp.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Camptocamp SA is a European consulting firm specializing in open-source GIS solutions, geospatial data management, and software development. They provide expertise in mapping, spatial analysis, and support for platforms such as QGIS, GeoServer, and MapServer, helping organizations leverage geospatial technologies for decision making and public services.
image: https://camptocamp.com/home/new_homepage_elements/image-thumb__2099__auto_c66707b6ce7cf31a8dd5942745ba8f88/we_are_camptocamp.png
layout: provider
modified: '2026-10-23'
name: Camptocamp SA
nav: Providers
network: true
overview: Camptocamp SA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GIS, OpenSource, Consulting, and Geospatial.
random_paper: 22
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Camptocamp Sa Domain Security
  slug: camptocamp-sa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: camptocamp-sa
tags:
- Company
- GIS
- OpenSource
- Consulting
- Geospatial
- Mapping
website: https://camptocamp.com
---
