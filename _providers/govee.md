---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Govee Agentic Access
  operation_count: 5
  slug: govee-agentic-access
  summary_line: 5 operations · 4 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Send capability commands to a device.
  name: Govee Device Control API
  slug: govee-device-control-api
- description: Query the live state of a device.
  name: Govee Device State API
  slug: govee-device-state-api
- description: Enumerate account devices and their capabilities.
  name: Govee Devices API
  slug: govee-devices-api
- description: Dynamic light scenes and DIY scenes.
  name: Govee Scenes API
  slug: govee-scenes-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Govee Developer Device Control API
  slug: open-govee-device-control-api
- collection_type: open
  name: Govee Developer Device Control Device State API
  slug: open-govee-device-state-api
- collection_type: open
  name: Govee Developer Device Control Devices API
  slug: open-govee-devices-api
- collection_type: open
  name: Govee Developer Device Control Scenes API
  slug: open-govee-scenes-api
- collection_type: open
  name: Govee Developer API
  slug: open-govee
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/govee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/govee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/govee-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Govee-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/govee
- group: company
  title: ''
  type: Website
  url: https://www.govee.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.govee.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/govee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/govee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/govee-finops.yml
created: '2026-07-03'
description: Govee builds smart lighting and smart-home devices - RGBIC LED strips, light bars, floor and table lamps, string and permanent outdoor lights, plus sensors, humidifiers, heaters, and other connected appliances. The Govee Developer API (v1, hosted at https://openapi.api.govee.com/router/api/v1) is a free, cloud REST API authenticated with a Govee-API-Key header that lets developers enumerate a user's devices and their capabilities, query live device state, and send control commands - power, brightness, RGB and color-temperature, dynamic light scenes, DIY scenes, and per-segment color and brightness. Device events (for capabilities that support them) are delivered over MQTT, and a separate local LAN API allows direct UDP control on the local network.
finops:
- name: Govee Finops
  service_category: IoT and Smart Home
  slug: govee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/govee.png
layout: provider
modified: '2026-07-03'
name: Govee
nav: Providers
network: true
overview: 'Govee publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Device Control API, Device State API, Devices API, and 1 more. Tagged areas include Smart Home, Smart Lighting, IoT, LED, and Home Automation.


  Govee''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Govee Plans Pricing
  plan_count: 2
  slug: govee-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 3
  name: Govee Rate Limits
  slug: govee-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -1.8
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 59.3
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/govee/refs/heads/main/screenshots/govee-2026-07-25T220132.png
security:
- kind: authentication
  name: Govee Authentication
  slug: govee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Govee Domain Security
  slug: govee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: govee
tags:
- Smart Home
- Smart Lighting
- IoT
- LED
- Home Automation
- Device Control
website: https://www.govee.com
---
