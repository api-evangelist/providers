---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'High-level gRPC (proto3) API to directly control the Clone Robot — muscle actuation (impulses/pulses/pressures), pinch/hydra valve control, water-pump pressure source, telemetry streaming, and camera '
  name: Clone Robot Control API
  slug: clone-robot-control-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://clonerobotics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clonerobotics
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/clonerobotics/clone_client
- group: build
  title: ''
  type: Packages
  url: packages/clone-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clone-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clone-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clone-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clone-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clone-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clone-llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clonerobotics.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clonerobotics.com/terms-of-use
- group: other
  title: ''
  type: X
  url: https://x.com/clonerobotics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clonerobotics/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCd0xLOw6No5IAsq3Y2-b0eA
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/clonerobotics
created: '2026-07-17'
description: Clone Robotics develops musculoskeletal, intelligent humanoid androids and robotic hands built on Myofiber, its artificial-muscle technology pioneered in 2021, driven by water-based hydraulics and biomimetic joints. Its flagship Clone Alpha is a full-body biomimetic humanoid with synthetic organs; the Clone Hand is its foundational dexterous-manipulation platform. The developer surface is a first-party Python client (clone_client) exposing a high-level gRPC (proto3) API to directly control the Clone Robot over the local network — actuating muscles via impulses/pulses/pressures, driving pinch and hydra valves, managing the water-pump pressure source, streaming IMU/pose/joint telemetry, and configuring cameras. There is no public HTTP/REST API or hosted endpoint; control is LAN-scoped gRPC discovered over zeroconf/mDNS by robot name or IP. Co-founded 2021 by Dhanush Radhakrishna and Lukasz Kozlik.
image: https://avatars.githubusercontent.com/u/140611352?v=4
layout: provider
modified: '2026-07-18'
name: Clone
nav: Providers
network: true
overview: 'Clone publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Frontier Tech, Robotics, Humanoid, and Androids.


  Clone''s developer surface includes YouTube channel and 16 more developer resources.'
random_paper: 49
score:
  band: minimal
  composite: 12.9
  delta: -1.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clone/refs/heads/main/screenshots/clone-2026-07-25T205641.png
security:
- kind: domain-security
  name: Clone Domain Security
  slug: clone-domain-security
  summary_line: TLSv1.3
slug: clone
tags:
- Company
- Frontier Tech
- Robotics
- Humanoid
- Androids
- Artificial Muscle
- gRPC
- Hardware
- Actuation
website: https://clonerobotics.com/
---
