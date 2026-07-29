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
- description: 'Agent-facing commerce surface for the Beauty Pie Shopify storefront: read-only product and collection JSON, a Universal Commerce Protocol (UCP) MCP endpoint for catalog search, cart, checkout and fulf'
  name: Beauty Pie Agent Commerce (UCP)
  slug: beauty-pie-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.beautypie.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beauty-pie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beauty-pie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beauty-pie-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beauty-pie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beauty-pie-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beauty-pie-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.beautypie.com/blogs/articles
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.beautypie.com/en-US
- group: start
  title: ''
  type: SignUp
  url: https://www.beautypie.com/pages/join-beauty-pie
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beautypie.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beautypie.com/policies/terms-of-service
created: '2026-07-17'
description: 'Beauty Pie is a members'' beauty club that sells premium skincare, makeup, hair and bodycare, fragrance and supplements direct from the world''s top labs at close to factory cost, passing the savings to members rather than paying traditional retail markups. Founded by Marcia Kilgour, it operates a direct-to-consumer online store in the UK and US. The storefront is built on Shopify and exposes a modern agent-native commerce surface: a published /llms.txt (agents.md) instruction file, Shopify Customer Accounts OpenID Connect for authentication, and a Universal Commerce Protocol (UCP) MCP endpoint that lets buyer-approved AI shopping agents search the catalog, build carts and complete checkout via Shop Pay. This profile was enriched from those public agent surfaces.'
image: https://cdn.shopify.com/s/files/1/0732/6475/8967/files/beauty_pie_7fab5e86-48c8-4083-81b5-deacc00fe2d7.jpg?v=1782305542
layout: provider
mcp_servers:
- description: ''
  name: beauty-pie-mcp.yml
  slug: beauty-pie-mcpyml
modified: '2026-07-18'
name: Beauty Pie
nav: Providers
network: true
overview: 'Beauty Pie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Beauty, Cosmetics, and Skincare.


  Beauty Pie''s developer surface includes authentication, engineering blog, signup flow, and 9 more developer resources.'
random_paper: 12
scopes:
- name: Beauty Pie Scopes
  scope_count: 4
  slug: beauty-pie-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.8
  delta: -0.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.3
  provenance:
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Beauty Pie Authentication
  slug: beauty-pie-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Beauty Pie Domain Security
  slug: beauty-pie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beauty-pie
tags:
- Company
- Consumer
- Beauty
- Cosmetics
- Skincare
- Retail
- E-Commerce
- Shopify
- Agentic Commerce
website: https://www.beautypie.com
---
