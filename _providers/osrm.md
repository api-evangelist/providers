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
- description: Routing API for OSRM as documented.
  name: OSRM API
  slug: osrm-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/osrm/hosts/osrm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/osrm-hosts.yml
- group: other
  href: https://artifacts.apis.io/osrm/vendors/osrm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/osrm-vendors.yml
- group: build
  href: https://artifacts.apis.io/osrm/packages/osrm-packages.yml
  title: ''
  type: SDKs
  url: packages/osrm-packages.yml
- group: build
  href: https://artifacts.apis.io/osrm/packages/osrm-packages.yml
  title: ''
  type: Packages
  url: packages/osrm-packages.yml
- group: auth
  href: https://artifacts.apis.io/osrm/security/osrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/osrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://project-osrm.org/
coverage:
  checked: '2026-10-28'
  detail: Documentation page does not provide a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://project-osrm.org/docs/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: OSRM (Project OSRM) provides a high performance routing engine for road networks, offering fast route calculation, distance tables, and map matching. It is an open-source, self‑hosted solution widely used for navigation, logistics, and geographic analysis, supporting various profiles such as car, bike, and foot.
layout: provider
modified: '2026-10-28'
name: OSRM (Project OSRM, self-hosted)
nav: Providers
network: true
overview: OSRM (Project OSRM, self-hosted) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Routing, OpenSource, Navigation, and GIS.
random_paper: 17
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: unknown
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
  name: Osrm Domain Security
  slug: osrm-domain-security
  summary_line: TLSv1.3
slug: osrm
tags:
- Company
- Routing
- OpenSource
- Navigation
- GIS
website: https://project-osrm.org/
---
