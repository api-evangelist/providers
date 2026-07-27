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
    agent_skills: true
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
  score: 29.8
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://blume.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.blume.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://www.blume.com/blogs/blume-university
- group: operate
  title: ''
  type: Support
  url: https://www.blume.com/pages/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.blume.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.blume.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blume.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blume.com/policies/terms-of-service
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blume-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blume-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blume-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blume-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blume-domain-security.yml
created: '2026-07-17'
description: 'Blume is a women-owned self-care and skincare brand (blume.com) selling cleansers, serums, oils, gel creams, and sunscreen for acne, dark spots, and sensitive skin, marketed as vegan, certified clean, climate neutral, and plastic neutral. Its direct-to-consumer storefront runs on Shopify and exposes a genuine agent-native commerce surface: a canonical /agents.md, a Universal Commerce Protocol (UCP 2026-04-08) merchant profile at /.well-known/ucp, a live Model Context Protocol endpoint for agent-driven shopping (search, cart, checkout, fulfillment), and Shopify Customer Account OAuth2/OpenID Connect authentication. Surfaced from the 500 Global and Felicis portfolios and enriched by the API Evangelist pipeline from live discovery documents.'
image: https://www.blume.com/cdn/shop/files/Screenshot_2026-06-01_at_11.33.49_AM_1.png?v=1782260453
layout: provider
mcp_servers:
- description: ''
  name: blume-mcp.yml
  slug: blume-mcpyml
modified: '2026-07-18'
name: Blume
nav: Providers
network: true
overview: 'Blume is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Skincare, Beauty, Self-Care, and E-commerce.


  Blume''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 9 more developer resources.'
random_paper: 57
score:
  band: emerging
  composite: 21.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Blume Authentication
  slug: blume-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Blume Domain Security
  slug: blume-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blume
tags:
- Company
- Skincare
- Beauty
- Self-Care
- E-commerce
- Consumer
- Shopify
- Agent Commerce
- Universal Commerce Protocol
- MCP
website: https://blume.com
---
