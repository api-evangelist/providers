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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Public gRPC API for the StellarStation ground-station-as-a-service platform. Lets satellite operators list upcoming available passes, reserve and cancel plans, add and retrieve TLE orbital data, set p
  name: StellarStation API
  slug: stellarstation-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infostellar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infostellar.net
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/infostellarinc/stellarstation-api
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/infostellarinc/stellarstation-api#readme
- group: docs
  title: ''
  type: APIReference
  url: https://javadoc.io/doc/com.stellarstation.api/stellarstation-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infostellarinc
- group: other
  title: ''
  type: Product
  url: https://www.stellarstation.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/infostellarinc/stellarstation-api/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infostellar-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infostellar-lifecycle.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/infostellar-stellarstation.proto
- group: build
  title: ''
  type: Packages
  url: packages/infostellar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infostellar-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infostellar-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infostellar-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infostellar-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infostellar-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infostellar-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infostellar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infostellar-llms.txt
created: '2026-07-17'
description: Infostellar is a Tokyo-based space infrastructure company that operates StellarStation, a cloud ground-station-as-a-service (GSaaS) platform. It aggregates partner and operator antennas into a shared global network so satellite operators can discover and reserve upcoming passes, schedule and cancel plans, manage two-line element (TLE) orbital data, and stream live telemetry and commands to and from their spacecraft. StellarStation exposes a public gRPC API (defined with Protocol Buffers) at api.stellarstation.com, with precompiled client stubs published for Java, Python, Go, and Node.js and authentication handled via JWT bearer service-account credentials issued from the StellarStation Console. The API separates a satellite-operator service (StellarStationService) from a ground-station-operator service (GroundStationService), plus supporting definitions for antennas, radios, orbit, monitoring, and transport.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/infostellar.png
layout: provider
mcp_servers:
- description: ''
  name: infostellar-mcp.yml
  slug: infostellar-mcpyml
modified: '2026-07-19'
name: Infostellar
nav: Providers
network: true
overview: 'Infostellar publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Satellite, Ground Station, and Aerospace.


  Infostellar''s developer surface includes documentation, API reference, changelog, authentication, and 17 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.1
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 19.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infostellar/refs/heads/main/screenshots/infostellar-2026-07-25T222423.png
security:
- kind: authentication
  name: Infostellar Authentication
  slug: infostellar-authentication
  summary_line: jwt-bearer · 1 scheme
- kind: domain-security
  name: Infostellar Domain Security
  slug: infostellar-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: infostellar
tags:
- Company
- Space
- Satellite
- Ground Station
- Aerospace
- Telemetry
- gRPC
- GSaaS
- Orbital
website: https://www.infostellar.net
---
