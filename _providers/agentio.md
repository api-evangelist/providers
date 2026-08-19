---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Agentio's hosted, remote Model Context Protocol server. A brand adds https://mcp.agentio.com/mcp to any MCP client (Claude, ChatGPT, or any other custom-connector host), authorizes over OAuth 2.1, and
  name: Agentio Brand Connector (MCP)
  slug: agentio-brand-connector-mcp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.agentio.com
- group: company
  title: ''
  type: Blog
  url: https://www.agentio.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.agentio.com/contact
- group: start
  title: ''
  type: Login
  url: https://app.agentio.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentio.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentio-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.agentio.com/connector
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agentio.com/connector
- group: start
  title: ''
  type: SignUp
  url: https://www.agentio.com/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agentio.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.agentio.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/agentio-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agentio-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agentio-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentio-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agentio-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentio-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agentio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentio-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/agentio-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agentio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agentio-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentio-llms.txt
created: '2026-07-17'
description: Agentio is an AI-native platform for creator advertising that connects brands with content creators across YouTube, Meta, and beyond. The two-sided platform gives brands agentic tooling to build, automate, and scale creator programs — handling creator matching and vetting, performance prediction from first-party creator data, campaign management, full-funnel measurement, and optimization — while giving creators personalized opportunities from top brands without manual negotiation. Founded by Arthur Leopold and Jonathan Meyers and based in Brooklyn, New York, Agentio holds official API marketing-partner status with closed advertising ecosystems and has raised $56M total, including a $40M Series B led by Forerunner at a $340M valuation. Agentio operates a private product application (app.agentio.com) and publishes no REST OpenAPI, GraphQL schema, or developer portal — but it does run a documented, production hosted MCP (Model Context Protocol) server, the Agentio Brand Connector
  at https://mcp.agentio.com/mcp, which lets a brand read its own campaigns, creator deals and deliverables, YouTube ad performance, and conversion reporting from any MCP client such as Claude or ChatGPT. Access is read-only, scoped to a single brand, and gated by OAuth 2.1 with PKCE and dynamic client registration.
image: https://cdn.prod.website-files.com/64dabf3558320122b88c5b84/6912391402abbaf1724f8173_agentio-logo-cropped%20(1).png
layout: provider
mcp_servers:
- description: ''
  name: agentio-mcp.yml
  slug: agentio-mcpyml
modified: '2026-08-12'
name: Agentio
nav: Providers
network: true
overview: 'Agentio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Adtech, Advertising, Creator Economy, and Influencer Marketing.


  Agentio''s developer surface includes engineering blog, support, documentation, getting-started guide, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Agentio Plans Pricing
  plan_count: 0
  slug: agentio-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 0
  name: Agentio Rate Limits
  slug: agentio-rate-limits
scopes:
- name: Agentio Scopes
  scope_count: 1
  slug: agentio-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 29.0
  delta: -2.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 31.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentio/refs/heads/main/screenshots/agentio-2026-07-25T181800.png
security:
- kind: authentication
  name: Agentio Authentication
  slug: agentio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Agentio Domain Security
  slug: agentio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Agentio Trust Center
  slug: agentio-trust-center
  summary_line: SOC 2 Type 2
slug: agentio
tags:
- Company
- Adtech
- Advertising
- Creator Economy
- Influencer Marketing
- Marketing
- Artificial Intelligence
- YouTube
- MCP
- Model Context Protocol
- Agents
- Analytics
website: https://www.agentio.com
---
