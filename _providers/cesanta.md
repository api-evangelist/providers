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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Cesanta Agentic Access
  operation_count: 12
  slug: cesanta-agentic-access
  summary_line: 12 operations · 8 acting
api_count: 4
apis:
- description: Device data storage and retrieval
  name: Cesanta Data API
  slug: cesanta-data-api
- description: Device registration, updates, RPC, and OTA
  name: Cesanta Devices API
  slug: cesanta-devices-api
- description: API key management
  name: Cesanta Keys API
  slug: cesanta-keys-api
- description: Notification logs
  name: Cesanta Logs API
  slug: cesanta-logs-api
artifact_total: 8
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cesanta-mdash-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cesanta-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cesanta-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cesanta-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cesanta-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cesanta-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cesanta-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cesanta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cesanta-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cesanta-mdash-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/cesanta-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cesanta-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cesanta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cesanta-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mdash.net/home/
- group: docs
  title: ''
  type: Documentation
  url: https://mongoose-os.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://mongoose-os.com/docs/mdash/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://mdash.net/home/tech-guides.html
- group: operate
  title: ''
  type: Support
  url: https://forum.mdash.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cesanta
- group: commercial
  title: ''
  type: Pricing
  url: https://mdash.net/home/pricing.html
- group: start
  title: ''
  type: Login
  url: https://mdash.net/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cesanta.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mongoose-os.com/terms.html
- group: company
  title: ''
  type: Website
  url: https://cesanta.com
created: '2026-07-17'
description: Cesanta is an embedded software and IoT company, established in 2013 to develop and support the Mongoose embedded web server and networking library (HTTP, WebSocket, MQTT, CoAP, TCP/IP) that ships in over 100 million devices from vendors such as Siemens, Bosch, Samsung, Schneider Electric, Broadcom, Google, and Caterpillar — and even runs aboard the International Space Station. Alongside the Mongoose library, Cesanta builds Mongoose OS (an IoT firmware development framework for ESP32, ESP8266, STM32 and other microcontrollers with AWS/Azure/Google Cloud integration), VCON.io (remote firmware update and automated firmware testing), and mDash — a managed IoT device cloud offering device management, over-the-air (OTA) updates, a device database/shadow, remote RPC, access control, and a documented REST API for programmatic fleet management.
image: https://cesanta.com/images/logo1.png
layout: provider
mcp_servers:
- description: ''
  name: cesanta-mcp.yml
  slug: cesanta-mcpyml
modified: '2026-07-18'
name: Cesanta
nav: Providers
network: true
overview: 'Cesanta publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data API, Devices API, Keys API, and 1 more. Tagged areas include Company, IoT, Embedded, Device Management, and Firmware.


  Cesanta''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 20 more developer resources.'
random_paper: 39
score:
  band: developing
  composite: 44.9
  delta: -1.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.1
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cesanta/refs/heads/main/screenshots/cesanta-2026-07-25T205012.png
security:
- kind: authentication
  name: Cesanta Authentication
  slug: cesanta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cesanta Domain Security
  slug: cesanta-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cesanta
tags:
- Company
- IoT
- Embedded
- Device Management
- Firmware
- OTA
- Networking
- MQTT
website: https://cesanta.com
---
