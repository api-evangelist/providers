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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.beautypie.com/
- group: company
  title: ''
  type: Blog
  url: https://www.beautypie.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://www.beautypie.com/pages/contact
- group: start
  title: ''
  type: Login
  url: https://www.beautypie.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beautypie.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beautypie.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beautypie-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beautypie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beautypie-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beautypie-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beautypie-domain-security.yml
created: '2026-07-17'
description: 'Beauty Pie is a London-based direct-to-consumer beauty and skincare membership club founded by Marcia Kilgore in 2016. Members pay an annual fee to buy luxury-quality skincare, makeup, fragrance, haircare, and wellness supplements at factory-adjacent prices, bypassing traditional retail markups. The company sells online (and via a small retail/wholesale footprint) and is backed by Balderton Capital, Index Ventures, Insight Partners, and General Catalyst. Its digital storefront runs on Shopify: customer authentication is handled by Shopify Customer Account OAuth2/OIDC, and the store exposes a live Shopify Storefront MCP server (Universal Commerce Protocol) at /api/mcp for agent-driven catalog search, cart, and product lookup. Beauty Pie does not publish an open, general-purpose developer API; its programmable surfaces are the platform-provided storefront MCP and customer-account authentication endpoints.'
image: https://cdn.shopify.com/s/files/1/0732/6475/8967/files/beauty_pie_7fab5e86-48c8-4083-81b5-deacc00fe2d7.jpg?v=1782305542
layout: provider
mcp_servers:
- description: ''
  name: Beauty Pie Storefront MCP
  slug: beauty-pie-storefront-mcp
modified: '2026-07-18'
name: Beauty Pie
nav: Providers
network: true
overview: 'Beauty Pie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Skincare, Cosmetics, and Ecommerce.


  Beauty Pie''s developer surface includes engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 44
scopes:
- name: Beautypie Scopes
  scope_count: 4
  slug: beautypie-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.2
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Beautypie Authentication
  slug: beautypie-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Beautypie Domain Security
  slug: beautypie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beautypie
tags:
- Company
- Beauty
- Skincare
- Cosmetics
- Ecommerce
- Direct-to-Consumer
- Membership
- Retail
- Shopify
- Storefront MCP
website: https://www.beautypie.com/
---
