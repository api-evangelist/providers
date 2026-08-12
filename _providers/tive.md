---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Tive Agentic Access
  operation_count: 15
  slug: tive-agentic-access
  summary_line: 15 operations · 7 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Alerts API from Tive — 1 operation(s) for alerts.
  name: Tive Alerts API
  slug: tive-alerts-api
- description: The Authentication API from Tive — 1 operation(s) for authentication.
  name: Tive Authentication API
  slug: tive-authentication-api
- description: The Devices API from Tive — 2 operation(s) for devices.
  name: Tive Devices API
  slug: tive-devices-api
- description: The Sensor Data API from Tive — 1 operation(s) for sensor data.
  name: Tive Sensor Data API
  slug: tive-sensor-data-api
- description: The Shipments API from Tive — 3 operation(s) for shipments.
  name: Tive Shipments API
  slug: tive-shipments-api
- description: The Webhooks API from Tive — 2 operation(s) for webhooks.
  name: Tive Webhooks API
  slug: tive-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Tive Public API
  slug: open-tive
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tive-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tive-inc-
- group: company
  title: ''
  type: Website
  url: https://www.tive.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tive.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/tive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tive-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tive.com/blog
created: '2026-06-21'
description: Tive is a real-time supply-chain and shipment visibility platform built on cellular IoT trackers. The Tive Public API (v3) lets you programmatically create and track shipments, manage trackers/devices, pull sensor data (location, temperature, humidity, pressure, light, motion, battery), configure alert presets, and subscribe to webhooks for push event delivery.
finops:
- name: Tive Finops
  service_category: Supply Chain and Logistics
  slug: tive-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tive.png
layout: provider
modified: '2026-06-21'
name: Tive
nav: Providers
network: true
overview: 'Tive publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Authentication API, Devices API, and 3 more. Tagged areas include Supply Chain, Shipment Visibility, Logistics, IoT, and Trackers.


  Tive''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Tive Plans Pricing
  plan_count: 1
  slug: tive-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 3
  name: Tive Rate Limits
  slug: tive-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -0.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 56.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Tive Authentication
  slug: tive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tive Domain Security
  slug: tive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tive
tags:
- Supply Chain
- Shipment Visibility
- Logistics
- IoT
- Trackers
- Real Time
website: https://www.tive.com
---
