---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Partner-gated interface announced September 2025 that delivers real-time SM300 vessel telemetry and data feeds (position, heading, mechanical and navigational state) to external command-and-control an
  name: SMLink Streaming-API
  slug: smlink-streaming-api
- description: Partner-gated interface announced September 2025 that grants select partners the ability to command SM300 autonomy functions directly from third-party mission software. Supported on the SM300-SP and S
  name: SMLink Control-API
  slug: smlink-control-api
- description: Industrial-grade vessel intelligence system providing operator-in-the-loop autonomous command and control, multi-waypoint missions, search and survey, patrol and surveillance, and remote command. Avai
  name: SM300 Autonomous Command and Control
  slug: sm300-autonomous-control
- description: AI-ris (Artificial Intelligence Recognition and Identification System) ingests 4K imagery and processes it on-device with embedded AI/ML to detect, track, classify, and geolocate vessel traffic and ob
  name: AI-ris Computer Vision
  slug: ai-ris-perception
- description: 'Browser-based fleet monitoring and analysis platform for SM300-equipped vessels, offering real-time and historical telemetry at 5-second intervals, mechanical and navigational data (radar, ARPA, AIS, '
  name: FleetViewer
  slug: fleetviewer
artifact_total: 10
collections:
- collection_type: open
  name: Sea Machines SMLink API
  slug: open-sea-machines
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sea-machines-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sea-machines
- group: company
  title: ''
  type: Website
  url: https://sea-machines.com/
- group: docs
  title: ''
  type: Documentation
  url: https://sea-machines.com/sea-machines-launches-marine-autonomy-apis-for-third-party-c2-systems/
- group: commercial
  title: ''
  type: Plans
  url: plans/sea-machines-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sea-machines-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sea-machines-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sea-machines.com/category/blog/
created: '2026-06-20'
description: Sea Machines Robotics builds autonomous command-and-control systems (SM300-SP, SM300-NG) and computer-vision perception (AI-ris) for commercial and defense marine vessels. In September 2025 it announced the SMLink Streaming-API and SMLink Control-API, partner-gated interfaces that stream real-time vessel telemetry to external systems and let approved third parties command SM300 autonomy functions from their own mission software. These interfaces are embedded, vessel-side product features, not a self-service public developer platform; access is arranged through Sea Machines sales.
finops:
- name: Sea Machines Finops
  service_category: Marine Autonomy and Robotics
  slug: sea-machines-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sea-machines.png
layout: provider
modified: '2026-06-20'
name: Sea Machines Robotics
nav: Providers
network: true
overview: 'Sea Machines Robotics publishes 2 APIs on the [APIs.io](https://apis.io/) network: SMLink Streaming-API and SMLink Control-API. Tagged areas include Marine, Autonomy, Robotics, Maritime, and Computer Vision.


  Sea Machines Robotics'' developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Sea Machines Plans Pricing
  plan_count: 1
  slug: sea-machines-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 2
  name: Sea Machines Rate Limits
  slug: sea-machines-rate-limits
score:
  band: emerging
  composite: 28.9
  delta: 2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 37.7
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sea-machines/refs/heads/main/screenshots/sea-machines-2026-06-20T193612.png
security:
- kind: domain-security
  name: Sea Machines Domain Security
  slug: sea-machines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sea-machines
tags:
- Marine
- Autonomy
- Robotics
- Maritime
- Computer Vision
- Telemetry
website: https://sea-machines.com/
---
