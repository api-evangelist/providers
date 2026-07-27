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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenlittle-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tenlittle-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tenlittle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tenlittle-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tenlittle-mcp.yml
- group: company
  title: ''
  type: Blog
  url: https://tenlittle.com/blogs/give-a-little
- group: operate
  title: ''
  type: Support
  url: https://tenlittle.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenlittle.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenlittle.com/pages/privacy
- group: start
  title: ''
  type: Login
  url: https://tenlittle.com/account/login
- group: company
  title: ''
  type: Website
  url: https://tenlittle.com/
created: '2026-07-17'
description: Ten Little is a direct-to-consumer children's footwear and essentials brand that designs healthy, non-toxic shoes for babies and kids. Its APMA-approved shoes use a proprietary TenForm Fit System — wide, foot-shaped toe boxes and flexible zero-drop soles grounded in medical and biomechanical research — to support natural movement and healthy foot development at every size and stage, and to accommodate AFO/SMO orthotics and braces. The brand sells online through a Shopify storefront and publishes no first-party developer API; the only API surfaces reachable on its domain are Shopify's platform-level Customer Account OIDC/OAuth and MCP endpoints.
image: https://tenlittle.com/cdn/shop/t/47/assets/social_preview_1024x.png
layout: provider
mcp_servers:
- description: ''
  name: tenlittle-mcp.yml
  slug: tenlittle-mcpyml
modified: '2026-07-21'
name: Ten Little
nav: Providers
network: true
overview: 'Ten Little is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-commerce, Consumer Goods, and Children.


  Ten Little''s developer surface includes authentication, engineering blog, support, and 8 more developer resources.'
random_paper: 29
scopes:
- name: Tenlittle Scopes
  scope_count: 4
  slug: tenlittle-scopes
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
  name: Tenlittle Authentication
  slug: tenlittle-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Tenlittle Domain Security
  slug: tenlittle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tenlittle
tags:
- Company
- Retail
- E-commerce
- Consumer Goods
- Children
- Footwear
- Direct-to-Consumer
- Shopify
website: https://tenlittle.com/
---
