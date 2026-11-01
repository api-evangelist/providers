---
agent_readiness:
  band: agent-aware
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/esri-uk/well-known/esri-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/esri-uk-well-known.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.esriuk.com/
- group: other
  href: https://artifacts.apis.io/esri-uk/hosts/esri-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/esri-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/esri-uk/vendors/esri-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/esri-uk-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://resource.esriuk.com/news/
- group: company
  title: ''
  type: Blog
  url: https://resource.esriuk.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://resource.esriuk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EsriUK
- group: auth
  href: https://artifacts.apis.io/esri-uk/security/esri-uk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/esri-uk-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/esri-uk/security/esri-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/esri-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.esriuk.com
coverage:
  checked: '2026-10-23'
  detail: Developer portal at https://developers.arcgis.com returns HTML pages rendered by JavaScript, with no machine‑readable OpenAPI spec discovered.
  evidence:
  - status: 200
    url: https://developers.arcgis.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Esri UK provides GIS software and spatial data analytics technology, helping organisations across the UK make data‑driven decisions. Their solutions power business intelligence, government operations and a wide range of mapping applications, delivering powerful location‑based insights and visualisations.
image: https://www.esriuk.com/en-gb/about/events/sc/2026/presentations
layout: provider
modified: '2026-10-23'
name: Esri UK
nav: Providers
network: true
overview: 'Esri UK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include GIS, Mapping, Spatial-Analytics, Enterprise-Software, and UK.


  Esri UK''s developer surface includes engineering blog, documentation, and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Esri Uk Domain Security
  slug: esri-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Esri Uk Trust Center
  slug: esri-uk-trust-center
  summary_line: ISO 27001, GDPR
slug: esri-uk
tags:
- GIS
- Mapping
- Spatial-Analytics
- Enterprise-Software
- UK
website: https://www.esriuk.com
---
