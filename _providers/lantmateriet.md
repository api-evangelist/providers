---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lantmateriet/refs/heads/main/well-known/lantmateriet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lantmateriet-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lantmateriet/refs/heads/main/hosts/lantmateriet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lantmateriet-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lantmateriet.se/en/geodata/for-retailers/terms-and-conditions/
- group: company
  title: ''
  type: Newsroom
  url: https://www.lantmateriet.se/Press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lantmateriet
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lantmateriet/refs/heads/main/security/lantmateriet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lantmateriet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lantmateriet.se/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at the API host.
  evidence:
  - status: 404
    url: https://api.lantmateriet.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-15'
description: Lantmäteriet is Sweden’s national land authority, providing geospatial data, cadastral information, and mapping services. It maintains the official register of property ownership, offers free and paid datasets, and supports developers through APIs for address lookup, map tiles, and geographic data downloads. The agency aims to increase transparency and accessibility of land information for public, businesses, and municipalities.
image: https://www.lantmateriet.se/globalassets/admin---bilder-sociala-medier/magnus-fond-9x9a9638--.jpg
layout: provider
modified: '2026-10-15'
name: Lantmäteriet
nav: Providers
network: true
overview: Lantmäteriet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Geospatial, Mapping, and Land Registry.
random_paper: 14
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lantmateriet Domain Security
  slug: lantmateriet-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: lantmateriet
tags:
- Company
- Government
- Geospatial
- Mapping
- Land Registry
website: https://lantmateriet.se/
---
