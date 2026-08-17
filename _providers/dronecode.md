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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: API for accessing Dronecode Foundation resources including PX4 autopilot documentation and MAVLink protocol specifications for drone development.
  name: Dronecode Foundation API
  slug: dronecode-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dronecode-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dronecode-foundation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.px4.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/PX4
- group: company
  title: ''
  type: Blog
  url: https://dronecode.org/feed/
created: '2026-03-16'
description: The Dronecode Foundation is a vendor-neutral Linux Foundation project for open source drone projects. It hosts PX4 autopilot flight control software and MAVLink communication protocol used worldwide for unmanned aerial vehicles, providing a complete open source platform for drone development.
finops:
- name: Dronecode Finops
  service_category: API
  slug: dronecode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dronecode.png
layout: provider
modified: '2026-04-28'
name: Dronecode Foundation
nav: Providers
network: true
overview: 'Dronecode Foundation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Drones, Linux Foundation, Robotics, and UAV.


  Dronecode Foundation''s developer surface includes documentation, engineering blog, and 3 more developer resources.'
plans:
- name: Dronecode Plans Pricing
  plan_count: 3
  slug: dronecode-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Dronecode Rate Limits
  slug: dronecode-rate-limits
score:
  band: minimal
  composite: 12.1
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 12.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dronecode/refs/heads/main/screenshots/dronecode-2026-06-20T180242.png
security:
- kind: domain-security
  name: Dronecode Domain Security
  slug: dronecode-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dronecode
tags:
- Drones
- Linux Foundation
- Robotics
- UAV
---
