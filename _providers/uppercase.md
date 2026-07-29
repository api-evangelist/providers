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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Agent-driven shopping surface on the uppercase storefront implementing the Universal Commerce Protocol over MCP: discover via /.well-known/ucp, then search_catalog, create_cart, create_checkout, updat'
  name: Uppercase Storefront Agent Commerce (UCP/MCP)
  slug: uppercase-storefront-agent-commerce-ucpmcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://uppercase.co.in/
- group: company
  title: ''
  type: Blog
  url: https://uppercase.co.in/blogs/blogs
- group: operate
  title: ''
  type: Support
  url: https://uppercase.co.in/pages/complaint-form
- group: start
  title: ''
  type: Login
  url: https://uppercase.co.in/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uppercase.co.in/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uppercase.co.in/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uppercase-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uppercase-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uppercase-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uppercase-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uppercase-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uppercase-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uppercase-domain-security.yml
created: '2026-07-17'
description: 'Uppercase is an Accel-backed, design-first and environmentally sensitive Indian travel-gear brand selling backpacks, trolley bags, duffles, messenger and sling bags direct-to-consumer at uppercase.co.in. The Shopify-powered storefront is notably agent-ready: it publishes /llms.txt and /agents.md agent instructions, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP shopping endpoint at /api/ucp/mcp (catalog search, cart, checkout with buyer-approved payment), OIDC/OAuth 2.0 customer authentication, and unauthenticated product/collection JSON for read-only agents.'
image: https://uppercase.co.in/cdn/shop/files/uc_web_logo.svg
layout: provider
mcp_servers:
- description: ''
  name: uppercase-mcp.yml
  slug: uppercase-mcpyml
modified: '2026-07-21'
name: Uppercase
nav: Providers
network: true
overview: 'Uppercase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Travel, Luggage, and Backpacks.


  Uppercase''s developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
random_paper: 44
scopes:
- name: Uppercase Scopes
  scope_count: 4
  slug: uppercase-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.3
  delta: 1.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Uppercase Authentication
  slug: uppercase-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Uppercase Domain Security
  slug: uppercase-domain-security
  summary_line: TLSv1.3 · HSTS
slug: uppercase
tags:
- Company
- Consumer
- Travel
- Luggage
- Backpacks
- Ecommerce
- Retail
- Sustainability
- Agentic Commerce
website: https://uppercase.co.in/
---
