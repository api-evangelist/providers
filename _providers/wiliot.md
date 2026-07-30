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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Manage traceability entities - Pixels (tags), assets, categories, asset types, locations, zones, metadata and events - scoped per owner.
  name: Wiliot Platform (Traceability) API
  slug: wiliot-platform-traceability-api
- description: Manage edge infrastructure - gateways, bridges, verification bridges and debug/coverage surveys.
  name: Wiliot Edge API
  slug: wiliot-edge-api
- description: Manufacturing operations - pixel ownership changes, reels, tag serialization, shipment approval, payload parse/resolve and sensor/tester data upload.
  name: Wiliot Manufacturing API
  slug: wiliot-manufacturing-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://wiliot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wiliot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wiliot.com/
- group: start
  title: ''
  type: Login
  url: https://platform.wiliot.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wiliot.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.wiliot.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wiliot
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wiliot.com/site-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wiliot.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/wiliot-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wiliot-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wiliot-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wiliot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wiliot-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/wiliot-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wiliot-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wiliot-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiliot-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/wiliot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wiliot-packages.yml
created: '2026-07-17'
description: 'Wiliot operates an ambient IoT platform built on battery-free "IoT Pixels" - postage-stamp-sized Bluetooth sensor tags - and a cloud that turns everyday physical items into a continuous, real-time data source for supply-chain visibility ("Physical AI"). Wiliot''s Cloud APIs expose three surfaces: a Platform (traceability) API for pixels, assets, categories, locations, zones and events; an Edge API for gateways, bridges and coverage surveys; and a Manufacturing API for pixel ownership, reels, serialization and sensor/tester data. Access uses an API key (or username/password) exchanged for a JWT bearer token, over a versioned REST surface scoped per owner. Official Python SDKs (wiliot-api, wiliot-core, and others) plus a React Native SDK are published.'
image: https://platform.wiliot.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: wiliot-mcp.yml
  slug: wiliot-mcpyml
modified: '2026-07-21'
name: Wiliot
nav: Providers
network: true
overview: 'Wiliot publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Internet of Things, Ambient IoT, Supply Chain, and Asset Tracking.


  Wiliot''s developer surface includes documentation, engineering blog, support, authentication, changelog, and 15 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 26.8
  delta: -2.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wiliot Authentication
  slug: wiliot-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Wiliot Domain Security
  slug: wiliot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wiliot
tags:
- Company
- Internet of Things
- Ambient IoT
- Supply Chain
- Asset Tracking
- Traceability
- Bluetooth
- Sensors
- RFID
website: https://wiliot.com
---
