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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.ecosoulhome.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ecosoul-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ecosoul-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ecosoul-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ecosoul-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ecosoul-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecosoul-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ecosoulhome.com/blogs/sustainable-living
- group: operate
  title: ''
  type: Support
  url: https://www.ecosoulhome.com/pages/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.ecosoulhome.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.ecosoulhome.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ecosoulhome.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ecosoulhome.com/policies/terms-of-service
created: '2026-07-17'
description: 'EcoSoul Home is a direct-to-consumer sustainable home-essentials brand selling compostable and eco-friendly tableware — plates, bowls, hot cups, cutlery, napkins, bagasse and areca-leaf products — plus everyday household goods made from renewable materials. The brand sells online through its Shopify storefront (and via major retail marketplaces) with the mission of replacing single-use plastic in the home. Backed by Accel, EcoSoul was added to the API Evangelist network as a portfolio lead and enriched from its public agent-native commerce surface: a published /llms.txt (agents.md) instruction file, Shopify Customer Accounts OpenID Connect for authentication, and a Universal Commerce Protocol (UCP) MCP endpoint that lets buyer-approved AI shopping agents search the catalog, build carts, and complete checkout via Shop Pay, Google Pay, or card.'
image: https://www.ecosoulhome.com/cdn/shop/files/B1.webp?v=1755690792
layout: provider
mcp_servers:
- description: ''
  name: ecosoul-mcp.yml
  slug: ecosoul-mcpyml
modified: '2026-07-19'
name: EcoSoul Home
nav: Providers
network: true
overview: 'EcoSoul Home is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Sustainability, Home Goods, and Compostable.


  EcoSoul Home''s developer surface includes authentication, engineering blog, support, signup flow, and 9 more developer resources.'
random_paper: 14
scopes:
- name: Ecosoul Scopes
  scope_count: 4
  slug: ecosoul-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Ecosoul Authentication
  slug: ecosoul-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Ecosoul Domain Security
  slug: ecosoul-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ecosoul
tags:
- Company
- Consumer
- Sustainability
- Home Goods
- Compostable
- Tableware
- Retail
- E-Commerce
- Shopify
- Agentic Commerce
website: https://www.ecosoulhome.com/
---
