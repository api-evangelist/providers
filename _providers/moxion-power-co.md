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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: The Device Faults API from Moxion Power Co — 1 operation(s) for device faults.
  name: Moxion Power Co Device Faults API
  slug: moxion-power-co-device-faults-api
- description: The Device Location API from Moxion Power Co — 2 operation(s) for device location.
  name: Moxion Power Co Device Location API
  slug: moxion-power-co-device-location-api
- description: The Device Metrics API from Moxion Power Co — 1 operation(s) for device metrics.
  name: Moxion Power Co Device Metrics API
  slug: moxion-power-co-device-metrics-api
- description: The Devices API from Moxion Power Co — 2 operation(s) for devices.
  name: Moxion Power Co Devices API
  slug: moxion-power-co-devices-api
- description: The Fleet Snapshot (AEMP) API from Moxion Power Co — 3 operation(s) for fleet snapshot (aemp).
  name: Moxion Power Co Fleet Snapshot (AEMP) API
  slug: moxion-power-co-fleet-snapshot-aemp-api
- description: The Organizations API from Moxion Power Co — 1 operation(s) for organizations.
  name: Moxion Power Co Organizations API
  slug: moxion-power-co-organizations-api
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.moxionpower.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.moxionpower.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.moxionpower.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.moxionpower.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/moxion-power-co-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://developer.moxionpower.com/login
- group: company
  title: ''
  type: Website
  url: https://www.moxionpower.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moxion-power-co-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moxion-power-co-fault-codes.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/moxion-power-co-metrics.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moxion-power-co-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moxion-power-co-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moxion-power-co-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moxion-power-co-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moxion-power-co-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/moxion-power-co-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moxion-power-co-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Moxion Power Co is a mobile energy storage company (a Y Combinator alum) that builds trailer-mounted, zero-emission Mobile Power Units (MPUs) used as quiet, clean replacements for diesel generators on construction sites, film productions, events, and grid-support jobs. Moxion operated a REST Developer API that let fleet operators fetch device metadata, real-time GPS location, and time-series telemetry (state of charge, pack voltage, net/output power, energy available/capacity, cellular signal) for their Mobile Power Units, along with active fault codes. The API additionally exposed AEMP 2.0 (ISO 15143-3 v.20190501) compliant fleet-snapshot endpoints so telematics platforms could ingest Moxion equipment alongside other heavy-equipment fleets. Authentication used bearer tokens issued to Service Accounts. Note the company filed for bankruptcy in August 2024; the developer documentation remains online but the API host may no longer be operational.
image: https://files.readme.io/6ee0605-small-Moxion_Icon_Logo_PNG.png
layout: provider
mcp_servers:
- description: ''
  name: moxion-power-co-mcp.yml
  slug: moxion-power-co-mcpyml
modified: '2026-07-20'
name: Moxion Power Co
nav: Providers
network: true
overview: 'Moxion Power Co publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Device Faults API, Device Location API, Device Metrics API, and 3 more. Tagged areas include Company, Energy Storage, Mobile Power, Battery, and Telemetry.


  Moxion Power Co''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, and 13 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 40.6
  delta: -0.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 60.2
    developer_ergonomics: 49.5
    discoverability: 92.6
    governance: 31.3
    operational_transparency: 0.0
  previous_composite: 41.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moxion Power Co Authentication
  slug: moxion-power-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moxion Power Co Domain Security
  slug: moxion-power-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moxion-power-co
tags:
- Company
- Energy Storage
- Mobile Power
- Battery
- Telemetry
- IoT
- Fleet Management
- Clean Energy
- Construction
- Device Metrics
website: https://www.moxionpower.com
---
