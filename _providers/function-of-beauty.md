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
api_count: 1
apis:
- description: Live hosted Shopify Storefront MCP server on the Function of Beauty domain, exposing product catalog search, cart management, store policy/FAQ lookup, and product detail tools over JSON-RPC 2.0.
  name: Function of Beauty Storefront MCP
  slug: function-of-beauty-storefront-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://functionofbeauty.com/
- group: operate
  title: ''
  type: Support
  url: https://functionofbeauty.com/pages/faq
- group: operate
  title: ''
  type: Support
  url: https://functionofbeauty.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://functionofbeauty.com/blogs/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://functionofbeauty.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://functionofbeauty.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://functionofbeauty.com/account/register
- group: start
  title: ''
  type: Login
  url: https://functionofbeauty.com/account/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/function-of-beauty-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/function-of-beauty-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/function-of-beauty-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/function-of-beauty-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/function-of-beauty-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/function-of-beauty-llms.txt
created: '2026-07-17'
description: 'Function of Beauty is a direct-to-consumer beauty and personal-care brand built around personalization, best known for quiz-driven customizable hair care (shampoo and conditioner) and skin and body products formulated to an individual profile. The company sells online through a Shopify-hosted storefront. Its customer-facing programmatic surface is therefore the Shopify commerce platform: a live hosted Storefront MCP server at /api/mcp (product search, cart, policies, product details) and the Shopify Customer Account API exposed through OpenID Connect discovery on the company domain. Function of Beauty was added to the API Evangelist network as a GGV Capital portfolio company and enriched from its public discovery surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/function-of-beauty.png
layout: provider
mcp_servers:
- description: ''
  name: function-of-beauty-mcp.yml
  slug: function-of-beauty-mcpyml
modified: '2026-07-19'
name: Function of Beauty
nav: Providers
network: true
overview: 'Function of Beauty publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Beauty, Personal Care, and Personalization.


  Function of Beauty''s developer surface includes support, engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 55
scopes:
- name: Function Of Beauty Scopes
  scope_count: 4
  slug: function-of-beauty-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 21.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Function Of Beauty Authentication
  slug: function-of-beauty-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Function Of Beauty Domain Security
  slug: function-of-beauty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: function-of-beauty
tags:
- Company
- Consumer
- Beauty
- Personal Care
- Personalization
- E-Commerce
- Shopify
- Direct to Consumer
- MCP
website: https://functionofbeauty.com/
---
