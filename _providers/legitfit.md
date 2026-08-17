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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: LegitFit's Model Context Protocol server — a JSON-RPC 2.0 endpoint that exposes LegitFit resources to AI agents. Protected by OAuth 2.1 (authorization_code with PKCE S256) and gated by the mcp:read an
  name: LegitFit MCP Server
  slug: legitfit-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://legitfit.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/legitfit-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/legitfit-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/legitfit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/legitfit-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/legitfit-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/legitfit-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/legitfit-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/legitfit-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/legitfit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/legitfit-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.legitfit.com/business
- group: company
  title: ''
  type: Blog
  url: https://legitfit.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://legitfit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://legitfit.com/sign-up-free
- group: start
  title: ''
  type: Login
  url: https://legitfit.com/authenticate/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legitfit.com/terms
created: '2026-07-17'
description: LegitFit is an Irish gym, studio and fitness-business management platform based in Cork, serving gyms, yoga and pilates studios, CrossFit boxes, leisure centres, personal trainers and multi-location operators. The product covers class and appointment scheduling with drag-and-drop timetables and waiting lists, membership and package management with auto-renewals, integrated online and offline payments built on Stripe, client and staff management, payroll and performance tracking, exercise programming, automated communications and lead nurture, a branded member app, and an AI assistant ("Lia") for revenue forecasting and programming. LegitFit publishes no public developer portal or OpenAPI description, but it does operate an OAuth 2.1-protected Model Context Protocol (MCP) server at https://legitfit.com/api/mcp, discoverable through RFC 8414 authorization-server and RFC 9728 protected-resource metadata, with mcp:read and mcp:write scopes.
image: https://cdn.prod.website-files.com/604d0cad0c813222fc3c19be/62cc3c109568ace3f67540e5_favicon32x32.png
layout: provider
mcp_servers:
- description: ''
  name: legitfit-mcp.yml
  slug: legitfit-mcpyml
modified: '2026-07-19'
name: LegitFit
nav: Providers
network: true
overview: 'LegitFit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fitness, Gym Management, Studio Management, and Scheduling.


  LegitFit''s developer surface includes authentication, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 111
rate_limits:
- limit_count: 1
  name: Legitfit Rate Limits
  slug: legitfit-rate-limits
scopes:
- name: Legitfit Scopes
  scope_count: 2
  slug: legitfit-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 27.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 27.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/legitfit/refs/heads/main/screenshots/legitfit-2026-07-25T224838.png
security:
- kind: authentication
  name: Legitfit Authentication
  slug: legitfit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Legitfit Domain Security
  slug: legitfit-domain-security
  summary_line: TLSv1.2 · DMARC
slug: legitfit
tags:
- Company
- Fitness
- Gym Management
- Studio Management
- Scheduling
- Memberships
- Payments
- SaaS
- MCP
- Ireland
website: https://legitfit.com/
---
