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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beyond2/refs/heads/main/hosts/beyond2-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyond2-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beyond2/refs/heads/main/security/beyond2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyond2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyond2.com
coverage:
  checked: '2026-09-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at known endpoints.
  evidence:
  - status: error
    url: https://api.beyond2.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Beyond2 is a classic car restoration and service company specializing in the legendary 2oo2 sedan. Based in the San Francisco Bay Area, they offer consultation, restoration, and parts services for vintage vehicles. Their website showcases services, detailed about information, and a catalog of classic car parts, reflecting a deep commitment to preserving automotive history.
layout: provider
modified: '2026-09-28'
name: Beyond2
nav: Providers
network: true
overview: Beyond2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include ClassicCars, Restoration, Consultation, San Francisco, and VintageVehicles.
random_paper: 9
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beyond2 Domain Security
  slug: beyond2-domain-security
  summary_line: TLSv1.3
slug: beyond2
tags:
- ClassicCars
- Restoration
- Consultation
- San Francisco
- VintageVehicles
website: https://beyond2.com
---
