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
api_count: 1
apis:
- description: ChangingTek provides SDKs and API support for secondary development, compatible with ROS, EtherCAT, CAN, and offers RS485 and IO control.
  name: ChangingTek API
  slug: changingtek-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/changingtek/refs/heads/main/hosts/changingtek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changingtek-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/changingtek/refs/heads/main/security/changingtek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changingtek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.changingtek.com
- group: docs
  title: ''
  type: Documentation
  url: https://en.changingtek.com/product
- group: company
  title: ''
  type: Blog
  url: https://en.changingtek.com/news
- group: operate
  title: ''
  type: Support
  url: https://en.changingtek.com/service
coverage:
  checked: '2026-10-08'
  detail: Product page mentions SDK and API support but provides no machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 404
    url: https://en.changingtek.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Changingtek Robotics Technology (Suzhou) Co., Ltd., founded in August 2018, is a Chinese high‑tech enterprise specializing in the research, development, and manufacturing of dexterous robotic hands, humanoid grippers, and embodied intelligent robots. The company provides a portfolio of collaborative robot grippers, parallel gripper series, integrated actuators, and mobile manipulators for industrial automation, warehouse logistics, aerospace, and other fields. It serves global customers with product selection manuals, digital models, user manuals, and software support, positioning itself as a leader in intelligent gripping solutions.
layout: provider
modified: '2026-10-08'
name: Changingtek
nav: Providers
network: true
overview: 'Changingtek is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Automation, Manufacturing, and Artificial Intelligence.


  Changingtek''s developer surface includes documentation, engineering blog, support, and 3 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Changingtek Domain Security
  slug: changingtek-domain-security
  summary_line: TLSv1.3 · HSTS
slug: changingtek
tags:
- Company
- Robotics
- Automation
- Manufacturing
- Artificial Intelligence
website: https://en.changingtek.com
---
