---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 62.1
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The Rhombus public REST API — 952 JSON-over-HTTPS operations (all POST) across cameras, video, access control, sensors, climate, events, policy alerts, reporting, face and vehicle recognition, scene q
  name: Rhombus Public REST API
  slug: rhombus-systems-public-api
- description: Real-time organization change events delivered over a STOMP 1.2 session framed on a secure WebSocket. Clients subscribe to /topic/change/{orgUuid} and receive a MESSAGE frame for every entity change i
  name: Rhombus Console WebSocket API
  slug: rhombus-systems-console-websocket-api
artifact_total: 10
asyncapis:
- description: ''
  name: Rhombus Systems Webhooks
  slug: rhombus-systems-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rhombus-systems-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhombus-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rhombus-systems-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.rhombus.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.rhombus.community/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.rhombus.community/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.rhombus.community/_llms/en/api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.rhombus.community/index.md
- group: operate
  title: ''
  type: Support
  url: https://www.rhombus.community/
- group: company
  title: ''
  type: Blog
  url: https://www.rhombus.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RhombusSystems
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rhombus.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.rhombus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rhombus.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rhombus.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rhombus.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.rhombus.com/trust/
- group: auth
  title: ''
  type: Security
  url: security/rhombus-systems-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/rhombus-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rhombus-systems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rhombus-systems-cli.yml
- group: design
  title: ''
  type: Components
  url: components/rhombus-systems-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rhombus-systems-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/rhombus-systems-api-catalog.json
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rhombus-systems-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhombus-systems-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rhombus-systems-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/rhombus-systems-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rhombus-systems-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/rhombus-systems-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rhombus-systems-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rhombus-systems-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rhombus-systems-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/rhombus-systems-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rhombus-systems-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rhombus-systems-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rhombus-systems-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rhombus-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rhombus-systems-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rhombus-systems-webhooks.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/rhombus-systems-console-websocket-asyncapi.json
created: '2026-08-26'
description: 'Rhombus Systems is a Sacramento, California enterprise physical-security platform that unifies AI-powered security cameras, door access control, environmental and IoT sensors, audio gateways and TMA Five Diamond alarm monitoring in a single cloud console. The platform is API-first: every feature in the web console, mobile apps and firmware is backed by the same public REST API, which publishes an OpenAPI 3.0 contract of 952 operations across 64 service groups covering cameras and video streaming, access control credentials and doors, lockdown plans, face recognition, license plate and vehicle recognition, scene query, occupancy and reporting, policy alerts, webhooks, partner/MSP org management, and SAML SSO with SCIM provisioning. Rhombus also ships an AsyncAPI 3.0 contract for its STOMP-over-WebSocket change-event stream, an RFC 9727 API catalog, RFC 9728/8414 OAuth discovery, an A2A agent card, an llms.txt family, a Model Context Protocol server, a Go CLI, a React SDK, and
  a published Claude Code skills library.'
image: https://rhombus.com/img/meta-homepage.png
layout: provider
mcp_servers:
- description: ''
  name: Rhombus Systems MCP Server
  slug: rhombus-systems-mcp-server
modified: '2026-08-26'
name: Rhombus Systems
nav: Providers
network: true
overview: 'Rhombus Systems publishes 2 APIs on the [APIs.io](https://apis.io/) network: Rhombus Public REST API and Rhombus Console WebSocket API. Tagged areas include Physical Security, Video Surveillance, Access Control, IoT Sensors, and Cloud Video Management.


  The Rhombus Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rhombus Systems'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Rhombus Systems Plans Pricing
  plan_count: 4
  slug: rhombus-systems-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rhombus Systems Rate Limits
  slug: rhombus-systems-rate-limits
score:
  band: strong
  composite: 61.3
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 30.3
    contract_quality: 62.0
    developer_ergonomics: 59.5
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Rhombus Systems Authentication
  slug: rhombus-systems-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Rhombus Systems Domain Security
  slug: rhombus-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Rhombus Systems Vulnerability Disclosure
  slug: rhombus-systems-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Rhombus Systems Trust Center
  slug: rhombus-systems-trust-center
  summary_line: SOC 2, GDPR, HIPAA, PCI, BIPA, PIPEDA, CMMC, NIST, CJIS, NDAA, TAA
slug: rhombus-systems
tags:
- Physical Security
- Video Surveillance
- Access Control
- IoT Sensors
- Cloud Video Management
- Alarm Monitoring
- Computer Vision
- Building Management
- Security Cameras
- Company
website: https://www.rhombus.com/
---
