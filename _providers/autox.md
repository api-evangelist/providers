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
api_count: 1
apis:
- description: AutoX provides autonomous driving platform APIs.
  name: AutoX API
  slug: autox-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autox/refs/heads/main/hosts/autox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autox-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autox/refs/heads/main/vendors/autox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autox-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autox/refs/heads/main/security/autox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.autox.ai
coverage:
  checked: 2026-09-26
  detail: The homepage returns a 404 shell and no machine‑readable API documentation is available.
  evidence:
  - status: 200
    url: https://www.autox.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: AutoX is an autonomous driving technology company based in San Jose, California. It develops AI‑enabled self‑driving platforms for robo‑taxis and grocery delivery, aiming to democratize autonomy. Founded in 2016, AutoX has raised significant funding and operates Level‑4 driverless services in China, with a focus on safety through advanced sensors, solid‑state LiDAR, radar, and AI perception.
layout: provider
modified: '2026-09-26'
name: AutoX
nav: Providers
network: true
overview: AutoX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Autonomous Driving, Artificial Intelligence, Robotics, Transportation, and San Jose.
random_paper: 11
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 5
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
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autox Domain Security
  slug: autox-domain-security
  summary_line: TLSv1.3
slug: autox
tags:
- Autonomous Driving
- Artificial Intelligence
- Robotics
- Transportation
- San Jose
website: https://www.autox.ai
---
