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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/rocketchat/hosts/rocketchat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rocketchat-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://rocketchat.com
coverage:
  checked: '2026-10-23'
  detail: Documentation is served as a JavaScript-rendered site with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.rocket.chat
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Rocket.Chat is an open-source team communication platform offering messaging, voice, video, apps, and AI integration. It enables organizations to deploy a customizable, self‑hosted chat solution under their control, supporting collaboration across devices and integrating with numerous services.
layout: provider
modified: '2026-10-22'
name: Rocket.Chat
nav: Providers
network: true
overview: Rocket.Chat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Communication, OpenSource, Collaboration, and SelfHosted.
random_paper: 8
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 7
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: rocketchat
tags:
- Company
- Communication
- OpenSource
- Collaboration
- SelfHosted
website: https://rocketchat.com
---
