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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chengrui/refs/heads/main/hosts/chengrui-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chengrui-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chengrui/refs/heads/main/security/chengrui-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chengrui-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://chengrui-power.com
coverage:
  checked: '2026-10-08'
  detail: Chengrui provides maritime power hardware and does not expose a public API.
  evidence:
  - status: 200
    url: http://chengrui-power.com
  reason: not-a-software-company
  state: none
created: '2026-10-08'
description: Chengrui Power Technology (Shanghai) Co., Ltd. is a Chinese company specializing in port and maritime electrification solutions, energy storage, and smart shipboard power systems. The firm offers a range of products including shore power systems for ports, energy-saving and intelligent solutions for maritime operations, storage systems, and shipboard power equipment. Their mission is to become a leading domestic and world-class provider of new energy and electrical automation technologies for the maritime industry, delivering innovative, reliable, and efficient power solutions to support sustainable port and shipping operations.
layout: provider
modified: '2026-10-08'
name: Chengrui
nav: Providers
network: true
overview: Chengrui is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Maritime, Electrification, and Automation.
random_paper: 17
score:
  band: minimal
  composite: 3.2
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chengrui Domain Security
  slug: chengrui-domain-security
  summary_line: no transport/DNS hardening detected
slug: chengrui
tags:
- Company
- Energy
- Maritime
- Electrification
- Automation
website: http://chengrui-power.com
---
