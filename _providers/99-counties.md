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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Agent-driven commerce for the 99 Counties Shopify store via the Universal Commerce Protocol over MCP — catalog search, cart, checkout, fulfillment, and buyer-approved order completion.
  name: 99 Counties Commerce (UCP)
  slug: 99-counties-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://99counties.com
- group: docs
  title: ''
  type: Documentation
  url: https://99counties.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/99-counties-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/99-counties-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/99-counties-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/99-counties-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/99-counties-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/99-counties-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/99-counties-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/99-counties-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/99-counties-ucp-shopping.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/99-counties-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://99counties.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://99counties.com/account/register
- group: start
  title: ''
  type: Login
  url: https://99counties.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://99counties.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://99counties.com/policies/privacy-policy
created: '2026-07-17'
description: 99 Counties is a regenerative-agriculture meat company selling 100% grass-fed and grass-finished beef and bison, pasture-raised pork, poultry, and lamb, plus wild-caught seafood, sourced from small family farms across Iowa, Wisconsin, and Minnesota. Its Shopify storefront exposes an agent-native commerce surface implementing the Universal Commerce Protocol (UCP) over a published MCP endpoint, alongside Shopify Customer Account OAuth 2.0 / OpenID Connect and standard read-only product and collection JSON. It was surfaced through the API Evangelist VC-portfolio pipeline and enriched from its live public agent-commerce surfaces.
image: https://cdn.shopify.com/s/files/1/0350/7175/4378/files/Beef_Sub_Nav_f7d12905-6f5c-4d2a-a699-a144b387aabc.jpg?v=1665766002
layout: provider
mcp_servers:
- description: ''
  name: 99-counties-mcp.yml
  slug: 99-counties-mcpyml
modified: '2026-07-17'
name: 99 Counties
nav: Providers
network: true
overview: '99 Counties publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Agent Commerce, Regenerative Agriculture, and Food and Beverage.


  99 Counties'' developer surface includes documentation, authentication, engineering blog, signup flow, and 13 more developer resources.'
random_paper: 105
scopes:
- name: 99 Counties Scopes
  scope_count: 4
  slug: 99-counties-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.4
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 23.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/99-counties/refs/heads/main/screenshots/99-counties-2026-08-07T160727.png
security:
- kind: authentication
  name: 99 Counties Authentication
  slug: 99-counties-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: 99 Counties Domain Security
  slug: 99-counties-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 99-counties
tags:
- Company
- E-Commerce
- Agent Commerce
- Regenerative Agriculture
- Food and Beverage
- Shopify
- Model Context Protocol
- Universal Commerce Protocol
website: https://99counties.com
---
