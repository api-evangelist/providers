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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Nortech Agentic Access
  operation_count: 50
  slug: nortech-agentic-access
  summary_line: 50 operations · 19 acting
api_count: 12
apis:
- description: This API includes endpoints that allow you to interact with `Assets` metadata.
  name: Nortech Asset API
  slug: nortech-asset-api
- description: This API includes endpoints that allow you to create and manage `Derivers`.
  name: Nortech Deriver API
  slug: nortech-deriver-api
- description: This API includes endpoints that allow you to interact with `Divisions` metadata.
  name: Nortech Division API
  slug: nortech-division-api
- description: The Health API from Nortech — 1 operation(s) for health.
  name: Nortech Health API
  slug: nortech-health-api
- description: This API includes endpoints that allow you to retrieve raw `Signal` Data for a specified period. The data requested is compiled into a file that you can download posteriorly.
  name: Nortech Historical Data API
  slug: nortech-historical-data-api
- description: This API includes endpoints that allow you to import signal data.
  name: Nortech Import Data API
  slug: nortech-import-data-api
- description: This API includes endpoints that allow you to retrieve live data.
  name: Nortech Live Data API
  slug: nortech-live-data-api
- description: The Me API from Nortech — 1 operation(s) for me.
  name: Nortech Me API
  slug: nortech-me-api
- description: This API provides endpoints to configure the Nortech AI Live API by selecting signals to be exported as MQTT messages. Data can then be consumed from `mqtts://live.data.apps.nor.tech` at topics with s
  name: Nortech MQTT Live Data API
  slug: nortech-mqtt-live-data-api
- description: This API includes endpoints that allow you to interact with `Signals` metadata.
  name: Nortech Signal API
  slug: nortech-signal-api
- description: This API includes endpoints that allow you to interact with `Units` metadata.
  name: Nortech Unit API
  slug: nortech-unit-api
- description: This API includes endpoints that allow you to interact with `Workspaces` metadata.
  name: Nortech Workspace API
  slug: nortech-workspace-api
artifact_total: 17
asyncapis:
- description: Real-time signal data streamed over MQTT-over-TLS. Subscribe to per-signal topics after creating a Data Connection through the HTTP API.
  name: Nortech Live Data (MQTT)
  slug: nortech-live-data-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apps.nor.tech/intro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apps.nor.tech/intro
- group: docs
  title: ''
  type: APIReference
  url: https://docs.apps.nor.tech/cloud-apis-sdks-http-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.apps.nor.tech/intro-get-started-data-extraction
- group: company
  title: ''
  type: Website
  url: https://nortech.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nortech-ai
- group: operate
  title: ''
  type: Support
  url: https://nortech.ai/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nortech.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nortech.ai/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://nortech.ai/security/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/nortech-openapi-original.json
- group: build
  title: ''
  type: Packages
  url: packages/nortech-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nortech-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nortech-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nortech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nortech-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nortech-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nortech-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nortech-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nortech-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/nortech-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nortech-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nortech-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nortech-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nortech-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/nortech-live-data-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nortech-live-data-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Nortech AI is an industrial IoT and operational-data infrastructure company (Bergen, Norway and Lisbon, Portugal) serving the maritime market and other asset-heavy industries. Its edge-plus-cloud platform extracts high-frequency data directly from industrial machinery, equipment and control systems — across vendors, protocols and equipment age — and structures it into trustworthy, contextualized signals for data-driven decision-making. The Nortech Cloud API exposes a Metadata API (workspaces, assets, divisions, units, signals), a Signal Data API (historical, live and import) and a Deriver API for computed virtual signals, plus an MQTT live-data stream.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nortech.png
layout: provider
mcp_servers:
- description: ''
  name: nortech-mcp.yml
  slug: nortech-mcpyml
modified: '2026-07-20'
name: Nortech
nav: Providers
network: true
overview: 'Nortech publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Asset API, Deriver API, Division API, and 9 more. Tagged areas include Company, Industrial IoT, IIoT, Maritime, and Operational Data.


  The Nortech catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nortech''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 23 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 49.5
  delta: -0.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 72.7
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nortech Authentication
  slug: nortech-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nortech Domain Security
  slug: nortech-domain-security
  summary_line: TLSv1.3
slug: nortech
tags:
- Company
- Industrial IoT
- IIoT
- Maritime
- Operational Data
- Time Series
- Sensors
- Data Infrastructure
website: https://nortech.ai
---
