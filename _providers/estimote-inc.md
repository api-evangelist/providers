---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Estimote Cloud RESTful API lets you programmatically read and update settings for your beacon fleet (Devices and Attachments APIs), manage pending settings for remote fleet updates, access LTE Bea
  name: Estimote Cloud API
  slug: estimote-cloud-api
artifact_total: 4
asyncapis:
- description: ''
  name: Estimote Inc Lte Events Webhooks
  slug: estimote-inc-lte-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estimote-inc-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/estimote-inc-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/estimote-inc-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/estimote-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/estimote-inc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/estimote-inc-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/estimote-inc-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/estimote-inc-lte-events-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/estimote-inc-llms.txt
- group: company
  title: ''
  type: Website
  url: https://estimote.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.estimote.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.estimote.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.estimote.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.estimote.com/lte-beacon/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://community.estimote.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://forums.estimote.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.estimote.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Estimote
- group: commercial
  title: ''
  type: Pricing
  url: https://order.estimote.com/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.estimote.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.estimote.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://estimote.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://estimote.com/privacy/
created: '2026-07-17'
description: Estimote, Inc. is a location and proximity technology company founded in 2012, with offices in New York City and Kraków, Poland. Estimote designs small wireless sensors and beacons that leverage modern IoT radio technologies — Bluetooth Low Energy (BLE), Ultra Wideband (UWB), and cellular LTE-M / NB-IoT — to bring precise indoor and outdoor positioning, proximity detection, and asset tracking to physical spaces. Its current flagship product, UWB Tags, are programmable in JavaScript via a web IDE and can push events directly to the cloud over LTE. For developers, Estimote exposes the Estimote Cloud RESTful API (device and attachment management, fleet configuration, and LTE Beacon event history), OAuth 2.0 authorization, serverless cloud code, and a family of first-party iOS and Android SDKs (Proximity, Positioning, UWB, Indoor, Fleet Management). Estimote has deployed millions of sensors worldwide for clients including Apple, Amazon, Nike, and NASA.
image: https://estimote.com/estimote-logo.png
layout: provider
modified: '2026-07-19'
name: Estimote Inc
nav: Providers
network: true
overview: 'Estimote Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Proximity, Beacons, Bluetooth, and BLE.


  The Estimote Inc catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Estimote Inc''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 33
score:
  band: developing
  composite: 45.5
  delta: 8.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 37.3
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/estimote-inc/refs/heads/main/screenshots/estimote-inc-2026-07-25T213641.png
security:
- kind: authentication
  name: Estimote Inc Authentication
  slug: estimote-inc-authentication
  summary_line: oauth2/http/apiKey · 2 schemes
- kind: domain-security
  name: Estimote Inc Domain Security
  slug: estimote-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: estimote-inc
tags:
- Company
- Proximity
- Beacons
- Bluetooth
- BLE
- UWB
- Ultra Wideband
- LTE
- IoT
- Indoor Location
- Asset Tracking
- RTLS
- Sensors
- Hardware
website: https://estimote.com/
---
