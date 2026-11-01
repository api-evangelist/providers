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
- description: The OpenHistoricalMap platform provides a time‑aware basemap style and map data access via its web interface, but no public machine‑readable API specification was found.
  name: OpenHistoricalMap API
  slug: openhistoricalmap-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/openhistoricalmap/hosts/openhistoricalmap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openhistoricalmap-hosts.yml
- group: other
  href: https://artifacts.apis.io/openhistoricalmap/vendors/openhistoricalmap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openhistoricalmap-vendors.yml
- group: build
  href: https://artifacts.apis.io/openhistoricalmap/packages/openhistoricalmap-packages.yml
  title: ''
  type: SDKs
  url: packages/openhistoricalmap-packages.yml
- group: build
  href: https://artifacts.apis.io/openhistoricalmap/packages/openhistoricalmap-packages.yml
  title: ''
  type: Packages
  url: packages/openhistoricalmap-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.openhistoricalmap.org/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenHistoricalMap
- group: auth
  href: https://artifacts.apis.io/openhistoricalmap/security/openhistoricalmap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openhistoricalmap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openhistoricalmap.org/
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation site renders via JavaScript, preventing automated extraction of a machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.openhistoricalmap.org/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: OpenHistoricalMap provides a time-aware basemap style that visualizes historical geographic data across different eras. It is an open, nonprofit project affiliated with the OpenStreetMap Foundation, offering an interactive map where users can explore, edit, and contribute historical map data. The platform supports various routing engines, data export, and user-contributed diaries, aiming to make historical geospatial information publicly accessible and reusable.
image: https://upload.wikimedia.org/wikipedia/commons/d/de/OpenHistoricalMap_logo.svg
layout: provider
modified: '2026-10-28'
name: OpenHistoricalMap time-aware basemap style
nav: Providers
network: true
overview: 'OpenHistoricalMap time-aware basemap style is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mapping, Historical, Open-Source, Nonprofit, and Geospatial.


  OpenHistoricalMap time-aware basemap style''s developer surface includes support and 7 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 5.3
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
  name: Openhistoricalmap Domain Security
  slug: openhistoricalmap-domain-security
  summary_line: TLSv1.3 · HSTS
slug: openhistoricalmap
tags:
- Mapping
- Historical
- Open-Source
- Nonprofit
- Geospatial
- Community
website: https://openhistoricalmap.org/
---
