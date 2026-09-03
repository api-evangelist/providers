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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Company agents
  name: AlterEstate Agents API
  slug: alterestate-agents-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Real-estate projects, their buildings and units
  name: AlterEstate Developments API
  slug: alterestate-developments-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Inbound lead submission into the CRM
  name: AlterEstate Leads API
  slug: alterestate-leads-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Cities, sectors and provinces
  name: AlterEstate Locations API
  slug: alterestate-locations-api
- baseURL: https://secure.alterestate.com/api/v1
  baseurl_source: declared
  description: Property listings and detail views
  name: AlterEstate Properties API
  slug: alterestate-properties-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AlterEstate Agents API
  slug: open-alterestate-agents-api
- collection_type: open
  name: AlterEstate Agents Developments API
  slug: open-alterestate-developments-api
- collection_type: open
  name: AlterEstate Agents Leads API
  slug: open-alterestate-leads-api
- collection_type: open
  name: AlterEstate Agents Locations API
  slug: open-alterestate-locations-api
- collection_type: open
  name: AlterEstate Agents Properties API
  slug: open-alterestate-properties-api
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
- description: Official AlterEstate hosted MCP server (branded "Brik"/alterai). Discovered via the RFC 9728 protected-resource document. Requires an OAuth 2.0 bearer token (scope "mcp"); an unauthenticated POST retu
  name: AlterEstate MCP Server
  slug: alterestate-mcp-server
modified: '2026-07-17'
name: AlterEstate
nav: Providers
network: true
overview: 'AlterEstate publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Developments API, Leads API, and 2 more. Tagged areas include Company, Real-Estate, CRM, Property Management, and Lead Management.


  AlterEstate''s developer surface includes documentation, API reference, authentication, engineering blog, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 6
scopes:
- name: Alterestate Scopes
  scope_count: 1
  slug: alterestate-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 13.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 31.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alterestate/refs/heads/main/screenshots/alterestate-2026-07-25T195823.png
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
- Real-Estate
- CRM
- Property Management
- Lead Management
- Latin America
- Software-as-a-Service
- Artificial Intelligence
- MCP
website: https://alterestate.com
---
