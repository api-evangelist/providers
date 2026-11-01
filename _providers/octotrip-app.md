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
- group: other
  href: https://artifacts.apis.io/octotrip-app/hosts/octotrip-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octotrip-app-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octotrip
- group: auth
  href: https://artifacts.apis.io/octotrip-app/security/octotrip-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octotrip-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octotrip.app/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite probing known hosts.
  evidence:
  - status: 404
    url: https://api.octotrip.app/openapi.json
  - status: 404
    url: https://octotrip.app/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: OctoTrip provides free MCP servers for travel search, offering live flight and rental car data without requiring API keys or authentication. The platform enables AI agents and developers to integrate real-time travel intelligence into applications instantly, supporting both web and mobile clients. It emphasizes open access, zero configuration, and supports multiple MCP clients, fostering seamless travel data integration for human users and AI agents alike.
image: https://octotrip.app/assets/images/OctoTrip_Logo.png
layout: provider
modified: '2026-10-30'
name: octotrip-app
nav: Providers
network: true
overview: octotrip-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, MCP, Flights, and RentalCars.
random_paper: 2
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 7
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
  name: Octotrip App Domain Security
  slug: octotrip-app-domain-security
  summary_line: TLSv1.3
slug: octotrip-app
tags:
- Company
- Travel
- MCP
- Flights
- RentalCars
website: https://octotrip.app/
---
