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
    agent_skills: true
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
  score: 24.3
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Agent-native commerce surface for the Italist Shopify storefront — a Universal Commerce Protocol (UCP) merchant profile and a Model Context Protocol (MCP) shopping endpoint for catalog search, cart, a
  name: Italist Commerce (UCP / MCP)
  slug: italist-commerce-ucp-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://italist.com
- group: operate
  title: ''
  type: Support
  url: https://italist.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://italist.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://italist.com/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://italist.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://italist.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/italist-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/italist-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/italist-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/italist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/italist-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/italist-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/italist-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/italist-domain-security.yml
created: '2026-07-17'
description: 'Italist is a luxury fashion e-commerce marketplace that ships designer apparel, shoes, bags, and accessories from Italy directly to shoppers worldwide, offering boutique inventory at Italian retail prices with duties and taxes handled at checkout. Originally surfaced as a portfolio company of 500 Global and added to the API Evangelist network as a stub, italist.com now runs as a Shopify-hosted storefront that exposes a modern agent-native commerce surface: a published Universal Commerce Protocol (UCP) merchant profile, a Model Context Protocol (MCP) shopping endpoint, provider-published agents.md / llms.txt agent instructions, and Shopify Customer Account API authentication over OpenID Connect. This profile was enriched by the pipeline from live probes of the storefront''s public agent surface.'
image: https://italist.com/cdn/shop/files/1200_x_400_-_1_fcc31d9b-a5bb-4f2a-a3a6-baa1712f67d1.jpg?v=1776357993
layout: provider
mcp_servers:
- description: ''
  name: italist-mcp.yml
  slug: italist-mcpyml
modified: '2026-07-19'
name: Italist
nav: Providers
network: true
overview: 'Italist publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Retail, Fashion, and Luxury.


  Italist''s developer surface includes support, engineering blog, signup flow, authentication, and 11 more developer resources.'
random_paper: 17
scopes:
- name: Italist Scopes
  scope_count: 4
  slug: italist-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 22.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/italist/refs/heads/main/screenshots/italist-2026-08-07T170928.png
security:
- kind: authentication
  name: Italist Authentication
  slug: italist-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Italist Domain Security
  slug: italist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: italist
tags:
- Company
- E-commerce
- Retail
- Fashion
- Luxury
- Marketplace
- Shopify
- Agentic Commerce
- MCP
website: https://italist.com
---
