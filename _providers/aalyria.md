---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: The Northbound Interface allows humans or applications to define and orchestrate a Spacetime network. It carries the Model API (NMTS entities and relationships describing platforms, antennas, interfac
  name: Spacetime Northbound Interface (NBI)
  slug: spacetime-nbi
- description: The Southbound Interface, also called the Control to Data-plane Interface (CDPI), is the collection of gRPC services through which devices participating in a Spacetime network communicate with the con
  name: Spacetime Southbound Interface (SBI / CDPI)
  slug: spacetime-sbi
- description: The Federation API, or East-West Interface, allows peer networks to request and to supply network resources and interconnections between partners' networks. It carries the Interconnect service, throug
  name: Spacetime Federation API (East-West Interface)
  slug: spacetime-federation
- description: 'The Status API is a small operational gRPC service exposed by every Spacetime instance. GetVersion returns the semantic version of the running Spacetime build, and GetMetrics returns instance insight '
  name: Spacetime Status API
  slug: spacetime-status
artifact_total: 7
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aalyria/api/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/aalyria/api/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.aalyria.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spacetime.aalyria.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spacetime.aalyria.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spacetime.aalyria.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spacetime.aalyria.com/api/nbi/build-your-first-scenario/
- group: auth
  title: ''
  type: Authentication
  url: authentication/aalyria-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aalyria
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aalyria/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aalyria.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aalyria.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://github.com/aalyria/api/issues
- group: other
  title: ''
  type: Protobuf
  url: grpc/aalyria-grpc-index.yml
- group: build
  title: ''
  type: Packages
  url: packages/aalyria-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aalyria-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aalyria-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aalyria-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aalyria-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.spacetime.aalyria.com/dev-guides/api-stability-levels/
- group: design
  title: ''
  type: Conventions
  url: conventions/aalyria-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aalyria-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aalyria-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aalyria-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aalyria-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aalyria-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aalyria-domain-security.yml
created: '2026-08-02'
description: 'Aalyria Technologies builds software and hardware for operating resilient, high-throughput networks in motion across space, air, land and sea. Its flagship platform, Spacetime, is a temporospatial software-defined networking (SDN) system that models the time-dynamic position and orientation of satellites, aircraft, ships and ground stations, then continuously plans, schedules and steers the links between them. Spacetime is programmable through three open, Apache-2.0 licensed gRPC/Protocol Buffers APIs published at github.com/aalyria/api: a Northbound Interface (NBI) for defining and orchestrating the network model and provisioning traffic-engineering policies, a Southbound Interface (SBI, also called CDPI) through which participating devices receive schedule updates and push telemetry, and a Federation (East-West) API through which peer network operators request and supply interconnections and capacity. Aalyria also produces Tightbeam, a free-space optical communications system.
  The company was spun out of Alphabet in 2022, carrying technology developed for Project Loon and Taara.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/companies/aalyria.png
layout: provider
mcp_servers:
- description: ''
  name: Aalyria MCP Server
  slug: aalyria-mcp-server
modified: '2026-08-02'
name: Aalyria
nav: Providers
network: true
overview: 'Aalyria publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Networking, Satellite, Space, and Telecommunications.


  Aalyria''s developer surface includes documentation, API reference, getting-started guide, authentication, support, CLI, changelog, and 21 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 37.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aalyria/refs/heads/main/screenshots/aalyria-2026-08-07T160729.png
security:
- kind: authentication
  name: Aalyria Authentication
  slug: aalyria-authentication
  summary_line: jwt-bearer/openIdConnect · 3 schemes
- kind: domain-security
  name: Aalyria Domain Security
  slug: aalyria-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aalyria
tags:
- Company
- Networking
- Satellite
- Space
- Telecommunications
- Software Defined Networking
- Orchestration
- Aerospace
- Defense
- Connectivity
- gRPC
- Protocol Buffers
- Telemetry
- Optical Communications
website: https://www.aalyria.com/
---
