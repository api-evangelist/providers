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
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ecoflow Agentic Access
  operation_count: 5
  slug: ecoflow-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 3
apis:
- description: Device discovery and binding
  name: EcoFlow Devices API
  slug: ecoflow-devices-api
- description: Obtain MQTT streaming/command certificate
  name: EcoFlow MQTT API
  slug: ecoflow-mqtt-api
- description: Read device property (quota) values and send device function commands
  name: EcoFlow Quota API
  slug: ecoflow-quota-api
artifact_total: 8
asyncapis:
- description: 'Real-time streaming and command channel for the EcoFlow IoT Open Platform. After obtaining a certificate from the HTTP `getMqttCertification` endpoint, a developer connects to the EcoFlow MQTT broker '
  name: EcoFlow IoT Open Platform MQTT API
  slug: ecoflow-mqtt-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecoflow-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ecoflow-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecoflow-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ecoflow.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ecoflow.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ecoflow.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ecoflow.com
- group: operate
  title: ''
  type: Support
  url: https://developer.ecoflow.com
- group: company
  title: ''
  type: Blog
  url: https://www.ecoflow.com/us/blog
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/ecoflow-mqtt-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ecoflow-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ecoflow-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/ecoflow-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ecoflow-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ecoflow-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ecoflow-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ecoflow-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: EcoFlow is a portable power and home energy-storage company known for its Delta and River portable power stations, PowerStream balcony micro-inverter, Power Kits, smart generators, whole-home backup systems and solar panels. For developers it operates the EcoFlow IoT Open Platform (developer.ecoflow.com), an HTTP + MQTT API that lets applications discover the EcoFlow devices bound to a user account, read live device telemetry ("quota" property values such as battery state of charge, input/output watts, temperatures and switch states), send device function commands, and stream real-time updates over MQTT. Access is authenticated with an accessKey / secretKey pair from the developer console and an HMAC-SHA256 request signature. The platform serves both a global/US region (api.ecoflow.com) and a separate Europe region (api-e.ecoflow.com), reflecting EcoFlow's strict per-region account separation.
image: https://cdn-fe.ecoflow.com/ef-open-platform/logo192.png
layout: provider
mcp_servers:
- description: ''
  name: ecoflow-mcp.yml
  slug: ecoflow-mcpyml
modified: '2026-07-19'
name: EcoFlow
nav: Providers
network: true
overview: 'EcoFlow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Devices API, MQTT API, and Quota API. Tagged areas include Company, Technology, Energy, Energy Storage, and Portable Power.


  The EcoFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EcoFlow''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 13 more developer resources.'
random_paper: 55
score:
  band: thin
  composite: 36.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 75.6
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ecoflow/refs/heads/main/screenshots/ecoflow-2026-07-25T212755.png
security:
- kind: authentication
  name: Ecoflow Authentication
  slug: ecoflow-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Ecoflow Domain Security
  slug: ecoflow-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ecoflow
tags:
- Company
- Technology
- Energy
- Energy Storage
- Portable Power
- IoT
- Smart Home
- Solar
- Developer API
website: https://ecoflow.com
---
