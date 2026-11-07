---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://artifacts.apis.io/divekit-app/security/divekit-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/divekit-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://divekit.app/
- group: docs
  title: ''
  type: Documentation
  url: https://divekit.app/docs/
- group: company
  title: ''
  type: Blog
  url: https://divekit.app/blog/
- group: operate
  title: ''
  type: Changelog
  url: https://divekit.app/changelog/
created: '2026-11-06'
description: Dive Kit provides a comprehensive decompression planner and a suite of free dive tools for technical divers on iOS and Android. Featuring Bühlmann ZH‑L16C, gradient factors, CCR planning, bailout schedules, gas mixing calculators, and offline access, the app supports both free and paid features while offering detailed dive‑profile graphs, plan sharing via links or QR codes, and extensive documentation for divers of all skill levels.
layout: provider
modified: '2026-11-06'
name: Dive Kit
nav: Providers
network: true
overview: 'Dive Kit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Diving, Decompression, Mobile App, and Tools.


  Dive Kit''s developer surface includes documentation, engineering blog, changelog, and 2 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Divekit App Domain Security
  slug: divekit-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: divekit-app
tags:
- Company
- Diving
- Decompression
- Mobile App
- Tools
website: https://divekit.app/
---
