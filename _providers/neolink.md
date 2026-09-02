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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for managing Reolink cameras through the Neolink bridge, providing RTSP streaming, camera control, and motion detection integration.
  name: Neolink Camera API
  slug: neolink-api
artifact_total: 4
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuantumEntangledAndy/neolink
created: '2024-01-15'
description: Neolink is an open-source bridge for Reolink cameras that provides an RTSP stream gateway and REST API for managing Reolink IP cameras, enabling integration with NVR software, home automation, and other camera management tools.
finops:
- name: Neolink Finops
  service_category: API
  slug: neolink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neolink.png
layout: provider
modified: '2026-04-28'
name: Neolink
nav: Providers
network: true
overview: Neolink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Camera, IoT, Open-Source, RTSP, and Smart Home.
plans:
- name: Neolink Plans Pricing
  plan_count: 3
  slug: neolink-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Neolink Rate Limits
  slug: neolink-rate-limits
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 4
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neolink/refs/heads/main/screenshots/neolink-2026-06-20T190140.png
slug: neolink
tags:
- Camera
- IoT
- Open-Source
- RTSP
- Smart Home
---
