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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Agent-driven shopping surface for the Urban Revivo global store, declared in the store's UCP merchant profile and llms.txt. Exposes MCP tools for catalog search, cart creation, and checkout (create/up
  name: Urban Revivo UCP Shopping (MCP)
  slug: urban-revivo-ucp-shopping-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://global.urbanrevivo.com/
- group: company
  title: ''
  type: About
  url: https://global.urbanrevivo.com/pages/about-urban-revivo-hp0036
- group: operate
  title: ''
  type: Support
  url: https://global.urbanrevivo.com/pages/contact-support
- group: operate
  title: ''
  type: FAQ
  url: https://global.urbanrevivo.com/pages/faq
- group: start
  title: ''
  type: Login
  url: https://global.urbanrevivo.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://global.urbanrevivo.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://global.urbanrevivo.com/policies/privacy-policy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/urbanrevivo/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/urbanrevivo.global
- group: other
  title: ''
  type: TikTok
  url: https://www.tiktok.com/@urbanrevivo_official
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/urban-revivo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/urban-revivo-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/urban-revivo-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/urban-revivo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/urban-revivo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/urban-revivo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/urban-revivo-domain-security.yml
created: '2026-07-17'
description: 'Urban Revivo is a fast-fashion retailer founded in 2006 in Guangzhou, selling runway-inspired womenswear, menswear, and accessories through stores across Asia and Europe and a global e-commerce storefront, with design centers in London, Shanghai, and Guangzhou. Its global online store runs on Shopify and exposes an agent-ready commerce surface: a published llms.txt/agents.md agent guide, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an MCP shopping endpoint offering catalog search, cart, and buyer-approved checkout tools, with customer identity brokered by Shopify customer accounts over OpenID Connect. Urban Revivo is backed by HongShan (Sequoia China).'
image: https://global.urbanrevivo.com/cdn/shop/files/990_1_441fc199-d6cf-46a2-8360-121151cad8d2_1200x1200.jpg?v=1627871035
layout: provider
mcp_servers:
- description: ''
  name: urban-revivo-mcp.yml
  slug: urban-revivo-mcpyml
modified: '2026-07-21'
name: Urban Revivo
nav: Providers
network: true
overview: 'Urban Revivo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, Retail, and eCommerce.


  Urban Revivo''s developer surface includes support, FAQ, authentication, and 14 more developer resources.'
random_paper: 24
scopes:
- name: Urban Revivo Scopes
  scope_count: 4
  slug: urban-revivo-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Urban Revivo Authentication
  slug: urban-revivo-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Urban Revivo Domain Security
  slug: urban-revivo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: urban-revivo
tags:
- Company
- Consumer
- Fashion
- Retail
- eCommerce
- Apparel
- Agentic Commerce
website: https://global.urbanrevivo.com/
---
