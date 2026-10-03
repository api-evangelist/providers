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
artifact_total: 0
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beijing-geoway-software/refs/heads/main/hosts/beijing-geoway-software-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beijing-geoway-software-hosts.yml
- group: company
  title: ''
  type: Website
  url: http://www.geoway.com.cn/
coverage:
  checked: '2026-09-27'
  detail: The company website returns a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: http://www.geoway.com.cn/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-27'
description: Beijing GEOWAY Software (北京吉威空间信息股份有限公司) is a leading Chinese earth‑space information technology provider founded in 1998. It offers proprietary remote sensing image processing, digital photogrammetry, and GIS software, serving satellite remote sensing, mapping, natural resources, digital government, and smart city sectors. With dual headquarters in Beijing and Wuhan and branches across over ten provinces, the company emphasizes autonomous innovation and comprehensive services in software development, data analysis, system construction, and operations.
layout: provider
modified: '2026-09-27'
name: Beijing GEOWAY Software
nav: Providers
network: true
overview: Beijing GEOWAY Software is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Remote Sensing, GIS, and Software.
random_paper: 13
score:
  band: minimal
  composite: 2.1
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: beijing-geoway-software
tags:
- Company
- Space
- Remote Sensing
- GIS
- Software
website: http://www.geoway.com.cn/
---
