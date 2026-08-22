---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
asyncapis:
- description: ''
  name: Flic Cloud Buttons Webhooks
  slug: flic-cloud-buttons-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://flic.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://flic.io/flic-hub-sdk
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/50ButtonsEach/flic2-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://flic.io/start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/50ButtonsEach
- group: operate
  title: ''
  type: Support
  url: https://community.flic.io/
- group: company
  title: ''
  type: Blog
  url: https://flic.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://flic.io/shop
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flic.io/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/flic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flic-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flic-cloud-buttons-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flic-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flic-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flic-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flic-llms.txt
created: '2026-07-17'
description: 'Flic (Shortcut Labs) makes wireless smart buttons and dials — the Flic Button, Flic Twist, Flic Duo, and the Flic Hub — that let people control smart-home devices, lights, music, and cloud services with a single press. Its developer surface is SDK- and protocol-centric rather than a REST API: first-party flic2lib SDKs for iOS, Android, C, Linux, and Windows implement the open Flic 2 Bluetooth protocol, the Flic Hub SDK runs JavaScript modules (MQTT, OSC) on the hub, and "Cloud Buttons" deliver physical button presses to any HTTP endpoint as a signed-JWT webhook. Flic is backed by 500 Global and lists 1,000+ compatible devices and services across smart home, healthcare, retail, hospitality, and logistics.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flic.png
layout: provider
modified: '2026-07-19'
name: Flic
nav: Providers
network: true
overview: 'Flic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Smart Buttons, IoT, Smart Home, and Bluetooth.


  The Flic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flic''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, authentication, and 10 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 34.6
  delta: -0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 57.1
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 35.4
  provenance:
    conformance: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flic/refs/heads/main/screenshots/flic-2026-07-25T214752.png
security:
- kind: authentication
  name: Flic Authentication
  slug: flic-authentication
  summary_line: jwt-signed-webhook/ble-pairing · 2 schemes
- kind: domain-security
  name: Flic Domain Security
  slug: flic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flic
tags:
- Company
- Smart Buttons
- IoT
- Smart Home
- Bluetooth
- Webhooks
- SDK
- Hardware
website: https://flic.io
---
