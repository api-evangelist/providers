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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: operate
  title: ''
  type: Support
  url: https://en.benewake.com/support/index.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/benewake/refs/heads/main/hosts/benewake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benewake-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.benewake.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/benewake/refs/heads/main/security/benewake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benewake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.benewake.com
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://equityzen.com/company/benewake
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Benewake develops high‑performance LiDAR sensors for autonomous driving, robotics, UAVs, and smart transportation. Based in Beijing, the company offers a wide range of short‑, medium‑, long‑distance and underwater LiDAR modules, serving global markets with over 300 patents and partnerships in more than 90 countries.
layout: provider
modified: '2026-09-27'
name: Benewake
nav: Providers
network: true
overview: 'Benewake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include LiDAR, Sensors, Autonomous Vehicles, Robotics, and UAV.


  Benewake''s developer surface includes support, documentation, and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Benewake Domain Security
  slug: benewake-domain-security
  summary_line: TLSv1.3
slug: benewake
tags:
- LiDAR
- Sensors
- Autonomous Vehicles
- Robotics
- UAV
website: https://en.benewake.com
---
