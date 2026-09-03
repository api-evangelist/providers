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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'Corvera''s hosted Model Context Protocol server. A single OAuth-secured HTTP MCP endpoint that exposes governed CPG datasets — retailer, distributor, logistics, ERP, warehouse, and ecommerce data — as '
  name: Corvera MCP Server
  slug: corvera-mcp-server
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corvera.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corvera.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corvera.ai/quickstart
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corvera-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corvera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corvera-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corvera-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corvera-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/corvera-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corvera-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corvera-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corvera-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://corvera.ai/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://corvera.ai/faq
- group: start
  title: ''
  type: SignUp
  url: https://corvera.ai/schedule-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corvera.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corvera.ai/terms-conditions
- group: company
  title: ''
  type: Website
  url: https://corvera.ai/
created: '2026-07-17'
description: Corvera is an AI-native context layer for consumer packaged goods (CPG) brands, backed by Y Combinator (Winter 2026). It unifies data from retailers, distributors, logistics providers, ERP systems, data warehouses, and ecommerce platforms into a single governed source of truth that AI tools can query directly over the Model Context Protocol (MCP). Rather than shipping a traditional REST API or SDKs, Corvera exposes a hosted, OAuth-secured MCP server at https://mcp.corvera.ai/mcp that any MCP-capable tool (Claude, ChatGPT, Cursor, Lovable, Replit) can connect to; the tools an account can call are gated by the integrations it has connected. Capabilities span category management, pricing and promotion ROI, demand forecasting, inventory management, cashflow tracking, and marketing-mix ROI, with role-based dataset access controls, a shared business glossary (Context), canonical entity mappings, and an admin activity feed. The platform normalizes cross-retailer sales calendars, resolves
  product mappings across sources, and makes governed datasets legible to AI-native CPG teams without dedicated data engineers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corvera.png
layout: provider
mcp_servers:
- description: ''
  name: Corvera MCP Server
  slug: corvera-mcp-server
modified: '2026-07-18'
name: Corvera
nav: Providers
network: true
overview: 'Corvera publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, CPG, Consumer Packaged Goods, and Retail.


  Corvera''s developer surface includes documentation, getting-started guide, authentication, changelog, engineering blog, signup flow, and 13 more developer resources.'
random_paper: 19
scopes:
- name: Corvera Scopes
  scope_count: 4
  slug: corvera-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 22.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corvera/refs/heads/main/screenshots/corvera-2026-07-25T210449.png
security:
- kind: authentication
  name: Corvera Authentication
  slug: corvera-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Corvera Domain Security
  slug: corvera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: corvera
tags:
- Company
- MCP
- CPG
- Consumer Packaged Goods
- Retail
- Data
- Context Layer
- AI Agents
- Analytics
- Y Combinator
website: https://corvera.ai/
---
