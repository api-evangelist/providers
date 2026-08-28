---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.7
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Maven's public REST API for integrating a fleet's TMS and other IT systems with the Maven platform. Fifteen published OpenAPI definitions cover users, vehicles and trailers, company locations, custome
  name: Maven Integrations API
  slug: maven-machines-integrations-api
- description: Per-customer middleware services Maven operates on <customer>.middleware.mavenmachines.com that translate a specific shipper or carrier's message formats into Maven platform calls. Six of these servic
  name: Maven Customer Integration Middleware
  slug: maven-machines-customer-middleware
artifact_total: 8
asyncapis:
- description: ''
  name: Maven Machines Return Events
  slug: maven-machines-return-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maven-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mavenmachines.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://maven-machines.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://maven-machines.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://maven-machines.readme.io/reference/post-shipment
- group: start
  title: ''
  type: GettingStarted
  url: https://maven-machines.readme.io/docs/basic-concepts
- group: operate
  title: ''
  type: Support
  url: https://help.mavenmachines.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mavenmachines.com/
- group: company
  title: ''
  type: Blog
  url: https://mavenmachines.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Maven-Machines
- group: start
  title: ''
  type: SignUp
  url: https://accounts.mavenmachines.com/
- group: start
  title: ''
  type: Login
  url: https://accounts.mavenmachines.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mavenmachines.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://mavenmachines.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maven-machines-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maven-machines-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maven-machines-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/maven-machines-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maven-machines-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/maven-machines-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/maven-machines-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/maven-machines-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/maven-machines-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maven-machines-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maven-machines-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/maven-machines-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maven-machines-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: EventCatalog
  url: asyncapi/maven-machines-return-events.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/maven-machines-well-known.yml
created: '2026-08-25'
description: Maven Machines (branded "Maven") is a Pittsburgh, Pennsylvania software company that builds a cloud platform for automating the planning and execution of daily trucking operations. The product suite spans route planning and optimization, dispatch execution, driver workflow, ELD / hours-of-service compliance, telematics and fleet management, delivered through a web portal for planners and dispatchers and an Android driver application. Maven publishes a public developer hub at maven-machines.readme.io covering fifteen separate OpenAPI definitions against a single production base URL, https://integrations.mavenmachines.com, secured with an `apiKey` request header. The integration model is TMS-to-Maven — master data (users, vehicles, trailers, company locations), transactional data (shipments, P&D manifests, linehaul manifests and trips, truckload trips and stops) flows in, and business activity flows back out through a polled `GET /return-events` queue and an event-sourced manifest/movement
  commands API. Maven also operates per-customer integration middleware services on <customer>.middleware.mavenmachines.com, several of which publish their own Swagger/OpenAPI documents publicly.
image: https://mavenmachines.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Maven Machines MCP Server
  slug: maven-machines-mcp-server
modified: '2026-08-25'
name: Maven Machines
nav: Providers
network: true
overview: 'Maven Machines publishes 2 APIs on the [APIs.io](https://apis.io/) network: Maven Integrations API and Maven Customer Integration Middleware. Tagged areas include Transportation, Logistics, Trucking, Fleet Management, and Telematics.


  The Maven Machines catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Maven Machines'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Maven Machines Plans Pricing
  plan_count: 0
  slug: maven-machines-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Maven Machines Rate Limits
  slug: maven-machines-rate-limits
score:
  band: developing
  composite: 41.1
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 16.7
    contract_quality: 59.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 81.3
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Maven Machines Authentication
  slug: maven-machines-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Maven Machines Domain Security
  slug: maven-machines-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: maven-machines
tags:
- Transportation
- Logistics
- Trucking
- Fleet Management
- Telematics
- ELD
- Route Optimization
- Dispatch
- Supply Chain
- Freight
website: https://mavenmachines.com/
---
