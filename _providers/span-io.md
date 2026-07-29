---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Span Io Agentic Access
  operation_count: 24
  slug: span-io-agentic-access
  summary_line: 24 operations · 9 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: 'Publish/subscribe streaming API hosted on SPAN Panel using the Electrification Bus (eBus) integration framework and the Homie Convention. SPAN Panel hosts an MQTT broker accessible over MQTTS (8883), '
  name: SPAN eBus MQTT API
  slug: span-ebus-mqtt-api
- description: The Auth API from SPAN — 3 operation(s) for auth.
  name: SPAN Auth API
  slug: span-io-auth-api
- description: The Circuits API from SPAN — 2 operation(s) for circuits.
  name: SPAN Circuits API
  slug: span-io-circuits-api
- description: The Islanding State API from SPAN — 1 operation(s) for islanding state.
  name: SPAN Islanding State API
  slug: span-io-islanding-state-api
- description: The Panel API from SPAN — 5 operation(s) for panel.
  name: SPAN Panel API
  slug: span-io-panel-api
- description: The Spaces API from SPAN — 2 operation(s) for spaces.
  name: SPAN Spaces API
  slug: span-io-spaces-api
- description: The Status API from SPAN — 1 operation(s) for status.
  name: SPAN Status API
  slug: span-io-status-api
- description: The Storage API from SPAN — 2 operation(s) for storage.
  name: SPAN Storage API
  slug: span-io-storage-api
- description: The Wifi API from SPAN — 2 operation(s) for wifi.
  name: SPAN Wifi API
  slug: span-io-wifi-api
artifact_total: 39
asyncapis:
- description: Publish/subscribe streaming API hosted directly on SPAN Panel using the Electrification Bus (eBus) integration framework and the Homie Convention for MQTT topic and payload structure. SPAN Panel hosts
  name: SPAN eBus MQTT API
  slug: span-ebus-asyncapi
collections:
- collection_type: open
  name: Span
  slug: open-span-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/span-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/span-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/span-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/span-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.span.io
- group: start
  title: ''
  type: Portal
  url: https://www.span.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/spanio/SPAN-API-Client-Docs
- group: docs
  title: ''
  type: Documentation
  url: https://opensource.span.io/span-panel/
- group: other
  title: ''
  type: Product
  url: https://www.span.io/smart-panel-product
- group: other
  title: ''
  type: Product
  url: https://www.span.io/products/main-32
- group: other
  title: ''
  type: Product
  url: https://www.span.io/drive
- group: other
  title: ''
  type: Product
  url: https://www.span.io/app
- group: other
  title: ''
  type: Product
  url: https://www.span.io/utilities
- group: company
  title: ''
  type: Blog
  url: https://www.span.io/blog
- group: other
  title: ''
  type: AnnouncementPost
  url: https://www.span.io/blog/introducing-span-api-and-span-home-on-premise-public-beta
- group: operate
  title: ''
  type: Support
  url: https://support.span.io/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.span.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.span.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spanio
- group: other
  title: ''
  type: Repository
  url: https://github.com/spanio/SPAN-API-Client-Docs
- group: operate
  title: ''
  type: Forums
  url: https://github.com/spanio/SPAN-API-Client-Docs/discussions
- group: operate
  title: ''
  type: Issues
  url: https://github.com/spanio/SPAN-API-Client-Docs/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/spanio/SPAN-API-Client-Docs/blob/main/CHANGELOG.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/spanio/SPAN-API-Client-Docs/blob/main/LICENSE
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SpanPanel/span-panel-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SpanPanel/Span
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SpanPanel/simulator
- group: build
  title: ''
  type: Tools
  url: https://github.com/spanio/SPAN-API-Client-Docs/tree/main/scripts
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/span_io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/span-io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@span_io
- group: company
  title: ''
  type: Careers
  url: https://www.span.io/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.span.io/contact
- group: commercial
  title: ''
  type: Plans
  url: plans/span-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/span-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/span-io-finops.yml
created: '2026-05-25'
description: SPAN is a San Francisco-based home energy technology company building smart electrical panels that replace traditional residential breaker boxes with a software-defined, controllable, and metered panel. SPAN Panel provides whole-home real-time power and energy metering, per-circuit monitoring and remote relay control, grid/islanding state management for whole-home backup with solar and energy storage, EV charging coordination via SPAN Drive, and a mobile app for energy management. As of the SPAN Panel firmware r202603 release (Q1 2026), SPAN exposes a public-beta on-premise SPAN API for software integrations between SPAN Panel and other devices on the home Local Area Network. The SPAN API is a real, documented HTTP + MQTT/Homie surface that runs directly on the panel — there is no cloud-hosted developer endpoint. The REST surface provides authentication, system status, Wi-Fi setup, panel state, per-circuit control, panel grid relay, energy storage state-of-energy, and emergency
  reconnect operations. The publish/subscribe surface uses the Electrification Bus (eBus) framework and Homie Convention over MQTT for streaming real-time panel state, per-circuit telemetry, and control of relays. SPAN API is licensed for personal, non-commercial use under MIT-0 for docs and example code; commercial / fleet use requires the separately licensed SPAN Fleet Manager.
features:
- SPAN Panel — software-defined smart electrical panel replacing traditional residential breaker boxes
- Whole-home and per-circuit real-time power and energy metering
- Per-circuit remote relay control with named circuits and priority groups
- Grid / islanding state management for whole-home backup with solar and energy storage
- SPAN Drive — integrated Level 2 EV charging coordinated with the panel
- SPAN Home mobile and on-premise apps for energy management and monitoring
- On-premise SPAN API hosted on the panel — REST + MQTT, LAN-only, no cloud
- HTTP Bearer JWT authentication minted by the panel and bound to a named API client
- REST resources for circuits, panel state, panel grid relay, panel meter and power, islanding state, energy storage SoE and nice-to-have thresholds, Wi-Fi scan/connect, system status, emergency reconnect
- MQTT pub/sub via the Electrification Bus (eBus) framework using the Homie Convention
- mDNS-advertised local discovery (`_span._tcp`, `_span-api._tcp`, `_mqtt._tcp`) for zero-config integration
- JSON Schema for Homie device descriptions and mDNS service records
- Reference shell + Python scripts (span-discover, span-auth, span-curl, span-mqtt-sub, span-mdns-query)
- Public beta — initial firmware r202603 for SPAN Panel MAIN 32, rolling out to MAIN 16 / MLO 24 / MAIN 40 / MLO 48 in H2 2026
- Commercial / fleet integrations served separately via SPAN Fleet Manager licensing
- SPAN Utilities — distributed energy resource (DER) management platform for utility partners
finops:
- name: Span Io Finops
  service_category: ''
  slug: span-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/span-io.png
json_schemas:
- name: Span Homie
  property_count: 0
  slug: span-homie
- name: Span Mdns Services
  property_count: 0
  slug: span-mdns-services
jsonld:
- class_count: 18
  name: Span Context
  property_count: 5
  slug: span-context
layout: provider
modified: '2026-05-25'
name: SPAN
nav: Providers
network: true
overview: 'SPAN publishes 9 APIs on the [APIs.io](https://apis.io/) network, including eBus MQTT API, Auth API, Circuits API, and 6 more. Tagged areas include Energy, Home Energy, Electrification, Smart Panel, and Electrical Panel.


  The SPAN catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  SPAN''s developer surface includes authentication, developer portal, documentation, engineering blog, support, changelog, tooling, and 29 more developer resources.'
plans:
- name: Span Io Plans Pricing
  plan_count: 3
  slug: span-io-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Span Io Rate Limits
  slug: span-io-rate-limits
rules:
- name: SPAN API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: span-io-asyncapi-spectral-rules
- name: SPAN API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: span-io-rules
score:
  band: developing
  composite: 51.7
  delta: -6.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.3
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 21.1
  previous_composite: 57.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/span-io/refs/heads/main/screenshots/span-io-2026-06-20T194242.png
security:
- kind: authentication
  name: Span Io Authentication
  slug: span-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Span Io Domain Security
  slug: span-io-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Span Io Vulnerability Disclosure
  slug: span-io-vulnerability-disclosure
  summary_line: disclosure policy published
slug: span-io
tags:
- Energy
- Home Energy
- Electrification
- Smart Panel
- Electrical Panel
- Home Automation
- Solar
- Energy Storage
- EV Charging
- Grid
- Islanding
- Backup Power
- Demand Response
- IoT
- MQTT
- Homie
- Electrification Bus
- On-Premise
website: https://www.span.io
---
