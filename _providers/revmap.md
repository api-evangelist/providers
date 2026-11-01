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
- group: other
  href: https://artifacts.apis.io/revmap/hosts/revmap-hosts.yml
  title: ''
  type: Hosts
  url: hosts/revmap-hosts.yml
- group: other
  href: https://artifacts.apis.io/revmap/vendors/revmap-vendors.yml
  title: ''
  type: Vendors
  url: vendors/revmap-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://revmap.github.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revmap
coverage:
  checked: '2026-10-29'
  detail: RevMap provides an interactive map and does not expose a public API.
  evidence:
  - status: 200
    url: https://github.com/revmap/revmap.github.io
  reason: not-a-software-company
  state: none
created: '2026-10-29'
description: RevMap provides an open‑source interactive map of the CivRevolution game, visualizing the world’s territories, cities, and routes. Hosted on GitHub Pages, the site lets players explore the game’s geography, plan strategies, and share custom maps. The project is maintained by the RevMap community and is freely available.
layout: provider
modified: '2026-10-29'
name: RevMap
nav: Providers
network: true
overview: RevMap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, gaming, map, civrevolution, and open-source.
random_paper: 3
scopes:
- name: Revmap Scopes
  scope_count: 0
  slug: revmap-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 14
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
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Revmap Authentication
  slug: revmap-authentication
  summary_line: 0 schemes
slug: revmap
tags:
- Company
- gaming
- map
- civrevolution
- open-source
- interactive
website: https://revmap.github.io
---
