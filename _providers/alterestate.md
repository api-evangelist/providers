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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: Company agents
  name: AlterEstate Agents API
  slug: alterestate-agents-api
- description: Real-estate projects, their buildings and units
  name: AlterEstate Developments API
  slug: alterestate-developments-api
- description: Inbound lead submission into the CRM
  name: AlterEstate Leads API
  slug: alterestate-leads-api
- description: Cities, sectors and provinces
  name: AlterEstate Locations API
  slug: alterestate-locations-api
- description: Property listings and detail views
  name: AlterEstate Properties API
  slug: alterestate-properties-api
artifact_total: 9
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.alterestate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.alterestate.com/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.alterestate.com/properties
- group: auth
  title: ''
  type: Authentication
  url: authentication/alterestate-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alterestate-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alterestate-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alterestate-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alterestate-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/alterestate-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/alterestate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alterestate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alterestate-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alterestate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alterestate-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alterestate-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://alterestate.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://ayuda.alterestate.com
- group: operate
  title: ''
  type: Support
  url: https://ayuda.alterestate.com
- group: commercial
  title: ''
  type: Pricing
  url: https://alterestate.com/precios
- group: start
  title: ''
  type: SignUp
  url: https://app.alterestate.com/registro
- group: start
  title: ''
  type: Login
  url: https://app.alterestate.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alterestate.com/terminos-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alterestate.com/politica-de-privacidad
- group: company
  title: ''
  type: Website
  url: https://alterestate.com
created: '2026-07-17'
description: AlterEstate is the leading real-estate CRM SaaS for agents across Latin America, serving more than 5,000 agents in seven countries. Its platform centralizes leads, properties and sales in a visual funnel and adds a WhatsApp-integrated AI assistant (Brik), a no-code website builder, a unified inbox, an inter-agency inventory network, and a marketing hub. AlterEstate exposes a public REST API at secure.alterestate.com/api/v1 covering property listings (with backend currency conversion across USD, DOP, MXN, COP, CRC, GTQ and PEN), project developments (buildings and units), agents, geographic locations, and inbound lead submission, plus an OAuth-protected hosted MCP server for agentic access. Backed by 500 Global.
image: https://alterestate.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: alterestate-mcp.yml
  slug: alterestate-mcpyml
modified: '2026-07-17'
name: AlterEstate
nav: Providers
network: true
overview: 'AlterEstate publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Developments API, Leads API, and 2 more. Tagged areas include Company, Real Estate, CRM, Property Management, and Lead Management.


  AlterEstate''s developer surface includes documentation, API reference, authentication, engineering blog, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 9
scopes:
- name: Alterestate Scopes
  scope_count: 1
  slug: alterestate-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 44.8
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 58.4
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 44.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Alterestate Authentication
  slug: alterestate-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Alterestate Domain Security
  slug: alterestate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alterestate
tags:
- Company
- Real Estate
- CRM
- Property Management
- Lead Management
- Latin America
- SaaS
- Artificial Intelligence
- MCP
website: https://alterestate.com
---
