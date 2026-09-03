---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.deepmap.ai'', ''status'': 301, ''note'': ''declared website redirects to https://www.nvidia.com/en-us/solutions/autonomous-vehicles/ — a different registrable domain (deepmap.ai -> nvidia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/nvidia/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepmap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.deepmap.ai
created: '2026-07-17'
description: DeepMap was a high-definition mapping and localization software company for autonomous vehicles, building HD maps, real-time localization, and map-update infrastructure that let self-driving cars know precisely where they were. Backed by a16z and Accel, DeepMap was acquired by NVIDIA in 2021 and folded into NVIDIA's autonomous-vehicle platform; the deepmap.ai domain now resolves to NVIDIA's self-driving solutions page. No independent DeepMap developer portal, documentation, or public API surface exists post-acquisition. This profile is retained as a network/portfolio record.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepmap.png
layout: provider
modified: '2026-08-21'
name: DeepMap
nav: Providers
network: true
overview: DeepMap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Autonomous Vehicles, HD Mapping, Localization, and Self-Driving.
random_paper: 18
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepmap/refs/heads/main/screenshots/deepmap-2026-07-25T211557.png
security:
- kind: domain-security
  name: Deepmap Domain Security
  slug: deepmap-domain-security
  summary_line: TLSv1.2 · DMARC
slug: deepmap
tags:
- Company
- Autonomous Vehicles
- HD Mapping
- Localization
- Self-Driving
- Robotics
- Acquired
website: http://www.deepmap.ai
---
