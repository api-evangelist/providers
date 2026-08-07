---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 598
  human_in_the_loop: 291
  name: Eventscom Agentic Access
  operation_count: 979
  slug: eventscom-agentic-access
  summary_line: 979 operations · 598 acting · 291 human-in-the-loop
api_count: 4
apis:
- description: The Spring Boot backend of Events.com's DataGol data and AI platform, self-documented as "Saasxl-api doc". 865 operations across 85 controller groups covering no-code database tables (NoCoDb v1/v2/v3)
  name: DataGol Platform API (Saasxl)
  slug: datagol-platform-api-saasxl
- description: FastAPI service exposing Events.com's DataGol AI surface — conversations and messages with streaming agent runs, a SQL parser and dialect converter, dashboard and widget generation, machine-learning m
  name: DataGol AI API
  slug: datagol-ai-api
- description: FastAPI service running Events.com's sandboxed Python analysis agent — a unified query endpoint, session lifecycle and status, stale-session cleanup, streaming run cancellation, Plotly figure retrieva
  name: DataGol Python Agent API
  slug: datagol-python-agent-api
- description: Hosted Model Context Protocol server for the DataGol workbook surface, reachable at the /mcp, /sse and /messages transport paths. Connections are gated on workspace_id, workbook_id and token query par
  name: DataGol MCP Server
  slug: datagol-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Eventscom Webhooks
  slug: eventscom-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://events.com/
- group: docs
  title: ''
  type: APIReference
  url: https://datagol-be.events.com/swagger-ui/index.html
- group: operate
  title: ''
  type: Support
  url: https://events.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://events.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edc-core
- group: commercial
  title: ''
  type: Pricing
  url: https://events.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://org.events.com/#/en_US/events/create
- group: start
  title: ''
  type: Login
  url: https://org.events.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://events.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://events.com/privacy/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eventscom-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/eventscom-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eventscom-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/eventscom-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eventscom-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eventscom-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eventscom-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eventscom-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/eventscom-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eventscom-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventscom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventscom-domain-security.yml
created: '2026-08-04'
description: Events.com is a La Jolla, California event-technology company founded by Mitch Thrower (co-founder of Active.com / The Active Network) that operates an end-to-end platform for creating, promoting, selling, and discovering events. Its organizer-facing products span ticketing and registration (Sell), digital event marketing (Promote), sponsorship management (Sponsor), on-site check-in and execution (Execute), analytics (Insights), virtual and hybrid events (Virtual), and an embeddable event calendar, alongside a consumer event-discovery destination. Events.com does not publish a public developer program, but its internal DataGol / Saasxl AI and data platform exposes three anonymously reachable OpenAPI 3.x contracts and a hosted Model Context Protocol server on production hosts, covering no-code data tables, ETL and orchestration, BI dashboards, knowledge graphs, custom agents, agent skills, and MCP connectors.
image: https://events.com/wp-content/uploads/2023/09/events-featured-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: eventscom-mcp.yml
  slug: eventscom-mcpyml
modified: '2026-08-04'
name: Events.com
nav: Providers
network: true
overview: 'Events.com publishes 3 APIs on the [APIs.io](https://apis.io/) network: DataGol Platform API (Saasxl), DataGol AI API, and DataGol Python Agent API. Tagged areas include event-management, ticketing, event-registration, event-marketing, and sponsorship.


  The Events.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Events.com''s developer surface includes API reference, support, engineering blog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 76
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.4
    developer_ergonomics: 34.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 33.3
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Eventscom Authentication
  slug: eventscom-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eventscom Domain Security
  slug: eventscom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eventscom
tags:
- event-management
- ticketing
- event-registration
- event-marketing
- sponsorship
- event-discovery
- data-platform
- business-intelligence
- artificial-intelligence
- mcp
- agent-native
- no-code
website: https://events.com/
---
