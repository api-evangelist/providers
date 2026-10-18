---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: REST API for managing Reolink cameras through the Neolink bridge, providing RTSP streaming, camera control, and motion detection integration.
  name: Neolink Camera API
  slug: neolink-api
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/neolink/refs/heads/main/plans/neolink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/neolink-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/neolink/refs/heads/main/rate-limits/neolink-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/neolink-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/neolink/refs/heads/main/finops/neolink-finops.yml
  title: ''
  type: FinOps
  url: finops/neolink-finops.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuantumEntangledAndy/neolink
created: '2024-01-15'
description: Neolink is an open-source bridge for Reolink cameras that provides an RTSP stream gateway and REST API for managing Reolink IP cameras, enabling integration with NVR software, home automation, and other camera management tools.
finops:
- has_sources: false
  method: generated
  name: Neolink Finops
  primary_unit: ''
  service_category: API
  slug: neolink-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neolink.png
layout: provider
modified: '2026-04-28'
name: Neolink
nav: Providers
network: true
overview: Neolink is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Camera, IoT, Open Source, RTSP, and Smart Home.
plans:
- name: Neolink Plans Pricing
  plan_count: 3
  slug: neolink-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Neolink Rate Limits
  slug: neolink-rate-limits
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 4
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/neolink/refs/heads/main/screenshots/neolink-2026-06-20T190140.png
slug: neolink
tags:
- Camera
- IoT
- Open Source
- RTSP
- Smart Home
---
