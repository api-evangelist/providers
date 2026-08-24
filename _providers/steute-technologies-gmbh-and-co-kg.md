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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 18
  human_in_the_loop: 18
  name: Steute Technologies Gmbh And Co Kg Agentic Access
  operation_count: 27
  slug: steute-technologies-gmbh-and-co-kg-agentic-access
  summary_line: 27 operations · 18 acting · 18 human-in-the-loop
api_count: 7
apis:
- description: The Access Point API from steute Technologies GmbH & Co. KG — 6 operation(s) for access point.
  name: steute Technologies GmbH & Co. KG Access Point API
  slug: steute-technologies-gmbh-and-co-kg-access-point-api
- description: The Auth API from steute Technologies GmbH & Co. KG — 2 operation(s) for auth.
  name: steute Technologies GmbH & Co. KG Auth API
  slug: steute-technologies-gmbh-and-co-kg-auth-api
- description: The History API from steute Technologies GmbH & Co. KG — 3 operation(s) for history.
  name: steute Technologies GmbH & Co. KG History API
  slug: steute-technologies-gmbh-and-co-kg-history-api
- description: The Notification Config API from steute Technologies GmbH & Co. KG — 3 operation(s) for notification config.
  name: steute Technologies GmbH & Co. KG Notification Config API
  slug: steute-technologies-gmbh-and-co-kg-notification-config-api
- description: The Switch API from steute Technologies GmbH & Co. KG — 3 operation(s) for switch.
  name: steute Technologies GmbH & Co. KG Switch API
  slug: steute-technologies-gmbh-and-co-kg-switch-api
- description: The Switch Group API from steute Technologies GmbH & Co. KG — 3 operation(s) for switch group.
  name: steute Technologies GmbH & Co. KG Switch Group API
  slug: steute-technologies-gmbh-and-co-kg-switch-group-api
- description: The System Status API from steute Technologies GmbH & Co. KG — 1 operation(s) for system status.
  name: steute Technologies GmbH & Co. KG System Status API
  slug: steute-technologies-gmbh-and-co-kg-system-status-api
artifact_total: 20
asyncapis:
- description: The Sensor Bridge sends JSON data via HTTP POST to configured target URLs whenever a switch is actuated, a switch or actor sends a wake-up message, or expected wake-up messages are not received (wake-
  name: steute nexy Sensor Bridge HTTP(S) Notifications
  slug: steute-technologies-gmbh-and-co-kg-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point API
  slug: open-steute-technologies-gmbh-and-co-kg-access-point-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point Auth API
  slug: open-steute-technologies-gmbh-and-co-kg-auth-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point History API
  slug: open-steute-technologies-gmbh-and-co-kg-history-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point Notification Config API
  slug: open-steute-technologies-gmbh-and-co-kg-notification-config-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point Switch API
  slug: open-steute-technologies-gmbh-and-co-kg-switch-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point Switch Group API
  slug: open-steute-technologies-gmbh-and-co-kg-switch-group-api
- collection_type: open
  name: Sensor Bridge API Version 2 Access Point System Status API
  slug: open-steute-technologies-gmbh-and-co-kg-system-status-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/steute-technologies-gmbh-and-co-kg-sensor-bridge-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/steute-technologies-gmbh-and-co-kg-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/steute-technologies-gmbh-and-co-kg-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.steute.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nexy.net/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.nexy.net/docs/sensor-bridge/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nexy.net/docs/getting-started/basic-system-setup
- group: auth
  title: ''
  type: Authentication
  url: authentication/steute-technologies-gmbh-and-co-kg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/steute-technologies-gmbh-and-co-kg-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/steute-technologies-gmbh-and-co-kg-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/steute-technologies-gmbh-and-co-kg-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.nexy.net/docs/sensor-bridge/rest-api/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/steute-technologies-gmbh-and-co-kg-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/steute-technologies-gmbh-and-co-kg-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/steute-technologies-gmbh-and-co-kg-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/steute-technologies-gmbh-and-co-kg-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/steute-technologies-gmbh-and-co-kg-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://www.steute.com/en/contact
- group: company
  title: ''
  type: Blog
  url: https://www.steute.com/en/news-media/press-releases
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.steute.com/en/data-privacy
- group: other
  title: ''
  type: Imprint
  url: https://www.steute.com/en/imprint
created: '2026-07-17'
description: 'steute Technologies GmbH & Co. KG is a German industrial technology company headquartered in Löhne that develops switchgear, sensors and controls under the tagline "Applied Intelligence", organized into three divisions: Meditec (certified user interfaces such as foot and hand controls for medical devices), Controltec (safe industrial automation with switches, sensors and wireless solutions) and Leantec (digital shop floor solutions). Its Leantec "nexy" IIoT wireless network, built on the sWave.NET radio protocol, connects hundreds of wireless switches and sensors to shop-floor IT through a Sensor Bridge gateway that exposes a JWT-secured REST API (OpenAPI 3.0), HTTP(S) push notifications, Modbus TCP and optional OPC UA and SAP modules for eKanban, AGV, Andon and material-flow integration. steute was surfaced as a portfolio company of Battery Ventures.'
image: https://www.steute.com/_assets/0fec2969a2bae73d42576ee80ea2af42/Icons/icon.png
layout: provider
mcp_servers:
- description: ''
  name: steute Technologies GmbH & Co. KG MCP Server
  slug: steute-technologies-gmbh-co-kg-mcp-server
modified: '2026-07-21'
name: steute Technologies GmbH & Co. KG
nav: Providers
network: true
overview: 'steute Technologies GmbH & Co. KG publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Access Point API, Auth API, History API, and 4 more. Tagged areas include Company, Industrial, Manufacturing, IIoT, and Wireless.


  The steute Technologies GmbH & Co. KG catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  steute Technologies GmbH & Co. KG''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 15 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 41.5
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 60.7
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 23.7
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Steute Technologies Gmbh And Co Kg Authentication
  slug: steute-technologies-gmbh-and-co-kg-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Steute Technologies Gmbh And Co Kg Domain Security
  slug: steute-technologies-gmbh-and-co-kg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: steute-technologies-gmbh-and-co-kg
tags:
- Company
- Industrial
- Manufacturing
- IIoT
- Wireless
- Sensors
- Switches
- Intralogistics
- Automation
- Medical Devices
website: https://www.steute.com/
---
