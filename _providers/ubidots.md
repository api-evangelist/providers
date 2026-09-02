---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
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
api_count: 3
apis:
- description: The Ubidots Data API v1.6 provides REST endpoints for sending and retrieving time-series data (dots) from IoT devices. Supports device and variable creation, data ingestion via HTTP POST, and historic
  name: Ubidots Data API v1.6
  slug: data-api-v16
- description: The Ubidots Data API v2 adds advanced filtering and sorting, bulk asynchronous operations for thousands of entities, dynamic field responses, and device provisioning in a single request. Supports full
  name: Ubidots Data API v2
  slug: data-api-v2
- description: Ubidots supports MQTT for lightweight device telemetry ingestion. Devices publish dots to Ubidots broker topics and subscribe to receive configuration or command payloads. Subject to the same per-toke
  name: Ubidots MQTT API
  slug: mqtt-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubidots-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ubidots.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ubidots.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ubidots
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ubidots
- group: other
  title: ''
  type: X
  url: https://x.com/ubidots
- group: company
  title: ''
  type: Blog
  url: https://ubidots.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ubidots.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://ubidots.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ubidots.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.ubidots.com
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/plans/ubidots-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/rate-limits/ubidots-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/finops/ubidots-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://ubidots.com/blog/rss/
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/json-ld/ubidots-context.jsonld
created: '2026-06-12'
description: Ubidots is an Industrial AIoT platform designed for OEMs, system integrators, and engineering firms that need to ingest, visualize, and act on device telemetry at scale. The platform exposes a REST API (v1.6 and v2) and an MQTT API for sending and retrieving time-series data from IoT sensors and devices. Developers can manage devices, variables, dashboards, organizations, and event-triggered alerts programmatically, while serverless UbiFunctions enable custom processing logic without managing infrastructure. Authentication uses short-lived or persistent tokens passed via the X-Auth-Token header or URL parameter, and throughput is gated per plan from 6 dots per second (Professional) up to 1,000 dots per second on private Enterprise deployments.
finops:
- name: Ubidots Finops
  service_category: ''
  slug: ubidots-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ubidots.png
jsonld:
- class_count: 12
  name: Ubidots Context
  property_count: 0
  slug: ubidots-context
layout: provider
modified: '2026-06-12'
name: Ubidots
nav: Providers
network: true
overview: 'Ubidots publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Internet of Things, Telemetry, Time Series, and MQTT.


  The Ubidots catalog on APIs.io includes 1 JSON-LD context.


  Ubidots'' developer surface includes documentation, engineering blog, changelog, pricing, and 13 more developer resources.'
plans:
- name: Ubidots Plans Pricing
  plan_count: 4
  slug: ubidots-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 14
  name: Ubidots Rate Limits
  slug: ubidots-rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 31.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ubidots/refs/heads/main/screenshots/ubidots-2026-06-20T195930.png
security:
- kind: domain-security
  name: Ubidots Domain Security
  slug: ubidots-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ubidots
tags:
- IoT
- Internet of Things
- Telemetry
- Time Series
- MQTT
- REST
- Dashboards
- Device Management
- Analytics
- Industrial IoT
- AIoT
website: https://ubidots.com
---
