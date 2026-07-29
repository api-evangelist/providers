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
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'REST API for managing Estimote devices (beacons): list and configure devices, associate cloud Attachments (custom key/value data) with a device, and read events reported by LTE beacons. Authenticated '
  name: Estimote Cloud API
  slug: estimote-cloud-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://estimote.com
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
  url: https://forums.estimote.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.estimote.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Estimote
- group: start
  title: ''
  type: SignUp
  url: https://cloud.estimote.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://estimote.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: authentication/estimote-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/estimote-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/estimote-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/estimote-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/estimote-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/estimote-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/estimote-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/estimote-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/estimote-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/estimote-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/estimote-domain-security.yml
created: '2026-07-17'
description: Estimote is a proximity and indoor-location company founded in 2012 that designs Bluetooth Low Energy, Ultra-Wideband (UWB) and LTE-M/NB-IoT beacons together with the Estimote Cloud platform for managing them at fleet scale. The Estimote Cloud REST API lets developers list and configure registered devices, attach contextual key/value data (Attachments) to individual beacons, and consume events reported by LTE beacons, authenticated with an App ID and App Token over HTTP Basic or, in private beta, OAuth 2.0. Native SDKs for iOS, Android, React Native and UWB deliver on-device proximity, indoor positioning, secure iBeacon/Eddystone broadcasting and beacon fleet management. Estimote is backed by a16z and Homebrew.
image: https://estimote.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: estimote-mcp.yml
  slug: estimote-mcpyml
modified: '2026-07-19'
name: Estimote
nav: Providers
network: true
overview: 'Estimote publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Location, Proximity, Beacons, and Bluetooth.


  Estimote''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 14 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 26.7
  delta: -1.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 28.2
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/estimote/refs/heads/main/screenshots/estimote-2026-07-25T213641.png
security:
- kind: authentication
  name: Estimote Authentication
  slug: estimote-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Estimote Domain Security
  slug: estimote-domain-security
  summary_line: TLSv1.3 · DMARC
slug: estimote
tags:
- Company
- Location
- Proximity
- Beacons
- Bluetooth
- IoT
- Indoor Location
- UWB
- Asset Tracking
- Developer Tools
website: https://estimote.com
---
