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
  href: https://raw.githubusercontent.com/api-evangelist/contoro-robotics/refs/heads/main/hosts/contoro-robotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contoro-robotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contoro-robotics/refs/heads/main/vendors/contoro-robotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contoro-robotics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contoro-robotics/refs/heads/main/security/contoro-robotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contoro-robotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contoro.com/
created: '2026-10-10'
description: Contoro Robotics, founded in 2022 and based in Austin, Texas, develops AI‑powered autonomous robots that unload non‑palletized boxes from trailers and shipping containers. Their human‑in‑the‑loop platform combines teleoperation, AI training, and DuoGrasp grippers to provide a reliable, affordable, and safe solution for logistics operators, reducing labor costs and improving safety without requiring upfront capital or long‑term contracts.
layout: provider
modified: '2026-10-10'
name: Contoro Robotics
nav: Providers
network: true
overview: Contoro Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Artificial Intelligence, Logistics, and Automation.
random_paper: 14
score:
  band: minimal
  composite: 3.0
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
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contoro Robotics Domain Security
  slug: contoro-robotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contoro-robotics
tags:
- Company
- Robotics
- Artificial Intelligence
- Logistics
- Automation
- Warehouse
website: https://contoro.com/
---
