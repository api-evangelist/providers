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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: On-device HTTP/JSON control API for Insta360 consumer 360 cameras (ONE X/X2/X3/X4/X5, ONE R/RS), implemented on Google's Open Spherical Camera (OSC) standard. The camera runs a built-in HTTP server re
  name: Insta360 OSC API
  slug: insta360-osc-api
- description: 'JSON-over-HTTP command API for Insta360 Pro, Pro 2, and Titan professional 360 cameras. Commands are issued to the camera''s built-in HTTP server (osc/commands/execute, osc/state) with file access and '
  name: Insta360 Pro Camera API
  slug: insta360-pro-camera-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://insta360.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.insta360.com/enterprise
- group: docs
  title: ''
  type: Documentation
  url: https://insta360develop.github.io/Insta360-Developer_Docs/
- group: docs
  title: ''
  type: APIReference
  url: https://insta360develop.github.io/Insta360-Developer_Docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Insta360Develop
- group: build
  title: ''
  type: Packages
  url: packages/insta360-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/insta360-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/insta360-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/insta360-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/insta360-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insta360-domain-security.yml
created: '2026-07-17'
description: 'Insta360 (Arashi Vision Co., Ltd) is a consumer and professional imaging company best known for its 360-degree and action cameras (the X, GO, ACE, Link, and Pro/Titan lines). For developers, Insta360 runs a first-party developer program through its Insta360Develop GitHub organization and a VitePress developer-documentation site. Cameras expose on-device HTTP control APIs: consumer models implement Google''s Open Spherical Camera (OSC) API over the camera Wi-Fi AP, and the Pro/Titan line adds a JSON-over-HTTP command API (ProCameraApi) for capture, live streaming, and file access. Native SDKs wrap this surface for C++ (camera control and media stitching/editing), Android, and iOS so third-party apps can connect to, configure, capture from, and post-process footage from Insta360 hardware.'
image: https://raw.githubusercontent.com/api-evangelist/insta360/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-19'
name: Insta360
nav: Providers
network: true
overview: 'Insta360 publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Technology, Cameras, Imaging, and 360 Video.


  Insta360''s developer surface includes documentation, API reference, and 9 more developer resources.'
random_paper: 100
score:
  band: emerging
  composite: 14.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 14.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insta360/refs/heads/main/screenshots/insta360-2026-07-25T222554.png
security:
- kind: domain-security
  name: Insta360 Domain Security
  slug: insta360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: insta360
tags:
- Company
- Consumer Technology
- Cameras
- Imaging
- 360 Video
- Action Cameras
- SDK
- Open Spherical Camera
- IoT
website: https://insta360.com/
---
