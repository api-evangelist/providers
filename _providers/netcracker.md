---
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 77.9
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 137
  human_in_the_loop: 36
  name: Netcracker Agentic Access
  operation_count: 276
  slug: netcracker-agentic-access
  summary_line: 276 operations · 137 acting · 36 human-in-the-loop
api_count: 4
apis:
- description: The external, public-facing API contract for APIHUB — Netcracker's open-source API registry and developer portal product. Covers package and catalog operations, publication workflows, versions, export
  name: Qubership APIHUB Registry API
  slug: qubership-apihub-registry-api
- description: The external administration API contract for APIHUB, covering technical administration operations — package transitions, system operations, role management and administrator management. OpenAPI 3.0.3,
  name: Qubership APIHUB System Administrators API
  slug: qubership-apihub-admin-api
- description: The REST API for Qubership MaaS, Netcracker's open-source messaging-as-a-service component that provisions and manages Kafka topics and RabbitMQ virtual hosts for microservices running on the Qubershi
  name: Qubership MaaS (Messaging as a Service) API
  slug: qubership-maas-api
- description: The REST API for Qubership DBaaS, Netcracker's open-source Database as a Service aggregator. It collects requests for managed databases and routes them to the appropriate database adapter, tracking ev
  name: Qubership DBaaS Aggregator API
  slug: qubership-dbaas-aggregator-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/netcracker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netcracker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/netcracker-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/netcracker-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/netcracker-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/netcracker-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/netcracker-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/netcracker-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/netcracker-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/netcracker-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/netcracker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/netcracker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/netcracker-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/netcracker-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://netcracker.github.io/apihub/releases/
- group: design
  title: ''
  type: Conformance
  url: conformance/netcracker-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.netcracker.com/portfolio/services/netcracker-cybersecurity
- group: auth
  title: ''
  type: TrustCenter
  url: security/netcracker-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netcracker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Netcracker/qubership-apihub/blob/main/SECURITY.md
- group: build
  title: ''
  type: CLI
  url: cli/netcracker-cli.yml
- group: design
  title: ''
  type: Components
  url: components/netcracker-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/netcracker-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/netcracker-sandbox.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/netcracker-qubership-control-plane-bus.proto
- group: company
  title: ''
  type: Website
  url: https://www.netcracker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://netcracker.github.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://netcracker.github.io/apihub/deploy/
- group: operate
  title: ''
  type: Support
  url: https://github.com/Netcracker/qubership-apihub/issues
- group: build
  title: ''
  type: Postman
  url: https://github.com/Netcracker/qubership-apihub-postman-collections
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netcracker.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netcracker.com/privacy-notice
- group: operate
  title: ''
  type: ContactUs
  url: https://www.netcracker.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Netcracker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netcracker-technology
- group: company
  title: ''
  type: Blog
  url: https://www.netcracker.com/blog
- group: operate
  title: ''
  type: PressReleases
  url: https://www.netcracker.com/news/press-releases
- group: other
  title: ''
  type: ProductPage
  url: https://www.netcracker.com/portfolio/products/netcracker-api-management-integration
- group: other
  title: ''
  type: Portfolio
  url: https://www.netcracker.com/portfolio
created: '2026-07-25'
description: 'Netcracker Technology is a Waltham, Massachusetts-based BSS/OSS and digital business software vendor and a wholly owned subsidiary of NEC Corporation. It sells cloud BSS, digital commerce and monetization, convergent charging, service and network orchestration, and API management and integration software to communications service providers worldwide — it is a supplier to carriers rather than a carrier itself, sitting one layer behind the operator in the telecom value chain and never touching a public developer directly. Netcracker is a long-standing TM Forum participant, claims the TM Forum Platinum Badge for Open API and "Ready for ODA" certification for its BSS/OSS portfolio, and contributed conformance toolkits to the TM Forum Open API program. Its API posture toward the outside world is honestly partner-gated: netcracker.com publishes no developer portal (developer., developers., docs., api. subdomains do not resolve; /developer, /developers and /api all return 404), no
  product OpenAPI is downloadable, and every commercial API — the TM Forum Open APIs its products implement — reaches integrators only through a customer or partner engagement. The one genuinely public, self-serve API surface Netcracker publishes is Qubership, its open-source cloud platform at github.com/Netcracker and netcracker.github.io, which ships real, downloadable OpenAPI contracts for its APIHUB API registry, integration, messaging and database services. On CAMARA, Netcracker names the standard in product marketing alongside TM Forum, MEF, ETSI, 3GPP and O-RAN and says CSPs can monetize "plug and play developer APIs, such as those from CAMARA" — but no CAMARA API is implemented, specified or callable anywhere in its public surface. That is a positioning statement, not an implementation.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: netcracker-mcp.yml
  slug: netcracker-mcpyml
modified: '2026-07-25'
name: Netcracker
nav: Providers
network: true
overview: 'Netcracker publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Qubership APIHUB Registry API, Qubership APIHUB System Administrators API, Qubership MaaS (Messaging as a Service) API, and 1 more. Tagged areas include Telecommunications, United States, BSS, OSS, and Network Vendor.


  Netcracker''s developer surface includes authentication, changelog, CLI, sandbox, documentation, getting-started guide, support, and 33 more developer resources.'
random_paper: 38
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 56.6
    developer_ergonomics: 76.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 49.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Netcracker Authentication
  slug: netcracker-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Netcracker Domain Security
  slug: netcracker-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Netcracker Vulnerability Disclosure
  slug: netcracker-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Netcracker Trust Center
  slug: netcracker-trust-center
  summary_line: PCI DSS, ISO 27001, ISO 27018, ISO 22301, SOC reporting
slug: netcracker
tags:
- Telecommunications
- United States
- BSS
- OSS
- Network Vendor
- API Management
- TM Forum
- Open API
- CAMARA
- Standards
- Orchestration
- Monetization
- Open Source
website: https://www.netcracker.com/
---
