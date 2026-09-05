---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ecoflow Agentic Access
  operation_count: 5
  slug: ecoflow-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.ecoflow.com
  baseurl_source: declared
  description: Device discovery and binding
  name: EcoFlow Devices API
  slug: ecoflow-devices-api
- baseURL: https://api.ecoflow.com
  baseurl_source: declared
  description: Obtain MQTT streaming/command certificate
  name: EcoFlow MQTT API
  slug: ecoflow-mqtt-api
- baseURL: https://api.ecoflow.com
  baseurl_source: declared
  description: Read device property (quota) values and send device function commands
  name: EcoFlow Quota API
  slug: ecoflow-quota-api
artifact_total: 11
asyncapis:
- description: 'Real-time streaming and command channel for the EcoFlow IoT Open Platform. After obtaining a certificate from the HTTP `getMqttCertification` endpoint, a developer connects to the EcoFlow MQTT broker '
  name: EcoFlow IoT Open Platform MQTT API
  slug: ecoflow-mqtt-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EcoFlow IoT Open Platform Devices API
  slug: open-ecoflow-devices-api
- collection_type: open
  name: EcoFlow IoT Open Platform Devices MQTT API
  slug: open-ecoflow-mqtt-api
- collection_type: open
  name: EcoFlow IoT Open Platform Devices Quota API
  slug: open-ecoflow-quota-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ecoflow-iot-overlay.yaml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: EcoFlow
nav: Providers
network: true
overview: 'EcoFlow publishes 3 APIs on the [APIs.io](https://apis.io/) network: Devices API, MQTT API, and Quota API. Tagged areas include Company, Technology, Energy, Energy Storage, and Portable Power.


  The EcoFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EcoFlow''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, and 14 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 66.1
    developer_ergonomics: 16.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
