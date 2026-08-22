---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The ASP.NET Core backend that powers www.hyperlabs.com — product catalog, product classes, categories, tags and filtering, application notes, datasheets, software/DLL downloads, website content (banne
  name: HYPERLABS Web API
  slug: hyperlabs-web-api
- description: Public gRPC control and acquisition interface for the HYPERLABS TDR11100 Time Domain Reflectometer. The proto3 service radium.v1.Radium exposes 22 unary RPCs covering readiness and board state, reset,
  name: HYPERLABS Radium gRPC API (TDR11100)
  slug: hyperlabs-radium-grpc-api-tdr11100
artifact_total: 7
asyncapis:
- description: 'Server-streaming surface of the radium.v1.Radium gRPC service running on a HYPERLABS TDR11100 Time Domain Reflectometer. A client opens a gRPC channel to the instrument on TCP 50052 and subscribes to '
  name: HYPERLABS Radium instrument event streams (TDR11100)
  slug: hyperlabs-radium-asyncapi
collections:
- collection_type: open
  name: Hyperlabs.Web
  slug: open-hyperlabs-web-openapi-original
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hyperlabs-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HYPERLABS/TDR11100/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/HYPERLABS/TDR11100/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hyperlabs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hyperlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hyperlabs.com/support/
- group: docs
  title: ''
  type: APIReference
  url: https://www.hyperlabs.com/api/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hyperlabs.com/applications/
- group: company
  title: ''
  type: About
  url: https://www.hyperlabs.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.hyperlabs.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.hyperlabs.com/support/faq/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HYPERLABS
- group: start
  title: ''
  type: Login
  url: https://www.hyperlabs.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hyperlabs.com/support/sales-and-warranty-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hyperlabs.com/support/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.hyperlabs.com/contact/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.hyperlabs.com/support/discontinued-products/
- group: build
  title: ''
  type: SDKs
  url: packages/hyperlabs-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/hyperlabs-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hyperlabs-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hyperlabs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hyperlabs-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hyperlabs-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hyperlabs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hyperlabs-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hyperlabs-data-model.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/hyperlabs-radium.proto
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/hyperlabs-web-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/hyperlabs-web-overlay.yaml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/hyperlabs-radium-asyncapi.yml
- group: build
  title: ''
  type: Examples
  url: https://github.com/HYPERLABS/TDR11100/raw/main/gRPC_Sample_Script.zip
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hyperlabs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'HYPERLABS, Inc. designs and manufactures signal-integrity products for high-speed digital and datacom test in the United States. Two product classes: ultra-broadband Components (amplifiers, baluns, DC blocks, bias tees, pick-off tees, power dividers, attenuators, terminations, inverters) built for 112 and 224 Gbps PAM-4 applications, and Instruments — USB-powered and USB-controlled TDRs, Signal Path Analyzers, controlled-impedance analyzers and impulse generators with 1-20 channels and rise times as fast as 35 ps. Founded in 1992, with engineering and manufacturing in Louisville, Colorado and Beaverton, Oregon. HYPERLABS publishes two machine-readable contracts: an OpenAPI 3.0.1 definition (175 operations, served with Swagger UI) for the hyperlabs.com product-catalog and customer web backend, and an MIT-licensed proto3 gRPC service definition, radium.v1.Radium, for programmatic control and waveform streaming from the TDR11100 Time Domain Reflectometer. Instrument automation
  is also offered as first-party Windows DLL packages (ZTDR and XTDR) with C++ sample source and manuals.'
image: https://www.hyperlabs.com/assets/logoFull.svg
layout: provider
mcp_servers:
- description: ''
  name: hyperlabs-mcp.yml
  slug: hyperlabs-mcpyml
modified: '2026-08-01'
name: HYPERLABS
nav: Providers
network: true
overview: 'HYPERLABS publishes 2 APIs on the [APIs.io](https://apis.io/) network: Web API and Radium gRPC API (TDR11100). Tagged areas include signal-integrity, test-and-measurement, electronic-components, instrumentation, and time-domain-reflectometry.


  The HYPERLABS catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HYPERLABS''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, code examples, and 26 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 32.4
  delta: -10.3
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 53.1
    developer_ergonomics: 28.0
    discoverability: 77.8
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 42.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/hyperlabs/refs/heads/main/screenshots/hyperlabs-2026-08-07T170547.png
security:
- kind: authentication
  name: Hyperlabs Authentication
  slug: hyperlabs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hyperlabs Domain Security
  slug: hyperlabs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hyperlabs
tags:
- signal-integrity
- test-and-measurement
- electronic-components
- instrumentation
- time-domain-reflectometry
- high-speed-digital
- datacom
- hardware
- grpc
- manufacturing
website: https://www.hyperlabs.com/
---
