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
  href: https://raw.githubusercontent.com/api-evangelist/ascend3dbe/refs/heads/main/hosts/ascend3dbe-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ascend3dbe-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ascend3d.com/index.php/news/
- group: company
  title: ''
  type: Blog
  url: https://ascend3d.com/index.php/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ascend3dbe/refs/heads/main/security/ascend3dbe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ascend3dbe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ascend3d.com
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract could be discovered on the provider's hosts.
  evidence:
  - status: 0
    url: https://api.ascend3d.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Ascend3d Software specializes in development and licensing of software technology to improve plant floor operations and communications. This includes factory automation based on Windows PC development solutions offering a unique approach to integration and bridging the capabilities of today’s cutting edge robotics with tomorrow’s lean manufacturing practices. The company provides robotic machine vision, metrology, and integration services for manufacturers worldwide.
layout: provider
modified: '2026-09-26'
name: Ascend3dbe
nav: Providers
network: true
overview: 'Ascend3dbe is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Automation, Machine Vision, Metrology, and Manufacturing.


  Ascend3dbe''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 3.7
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
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 0.0
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
  name: Ascend3Dbe Domain Security
  slug: ascend3dbe-domain-security
  summary_line: TLSv1.3
slug: ascend3dbe
tags:
- Robotics
- Automation
- Machine Vision
- Metrology
- Manufacturing
- Software
website: https://ascend3d.com
---
