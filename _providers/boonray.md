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
  href: https://raw.githubusercontent.com/api-evangelist/boonray/refs/heads/main/hosts/boonray-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boonray-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://en.boonray.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boonray/refs/heads/main/security/boonray-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boonray-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.boonray.com
coverage:
  checked: '2026-10-02'
  detail: No OpenAPI, AsyncAPI, GraphQL or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.boonray.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Boonray, also known as Shanghai Bolei Intelligent Technology Co., Ltd, develops autonomous driving and intelligent mining solutions, focusing on unmanned mining vehicles, new energy power systems, and smart car technologies. The company provides integrated charging and swapping solutions for mining equipment, aiming to enhance safety and efficiency in mining operations worldwide.
layout: provider
modified: '2026-10-02'
name: Boonray
nav: Providers
network: true
overview: Boonray is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Driving, MiningTech, SmartCars, and New Energy.
random_paper: 14
score:
  band: minimal
  composite: 3.4
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
    developer_ergonomics: 0.0
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boonray Domain Security
  slug: boonray-domain-security
  summary_line: TLSv1.2 · HSTS
slug: boonray
tags:
- Company
- Autonomous Driving
- MiningTech
- SmartCars
- New Energy
website: https://en.boonray.com
---
