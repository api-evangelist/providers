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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://casper.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/casper-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/casper-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casper-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/casper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/casper-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/casper-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casper-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casper.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casper.com/policies/terms-of-service
created: '2026-07-17'
description: 'Casper (Casper Sleep Inc.) is a direct-to-consumer sleep and home goods brand that sells mattresses, bedding, pillows, and sleep accessories online at casper.com and through retail partners. Its casper.com storefront runs on Shopify and exposes a modern agentic-commerce surface: a published llms.txt/agents.md with agent instructions, the Universal Commerce Protocol (UCP) merchant profile, a UCP shopping MCP endpoint for AI agents to search, cart, and check out, and Shopify Customer Account API OpenID Connect authentication. Casper was added to the API Evangelist network as a portfolio company of IVP and Slow Ventures and enriched from its live public agent/commerce surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/casper.png
layout: provider
mcp_servers:
- description: ''
  name: Casper UCP shopping MCP
  slug: casper-ucp-shopping-mcp
modified: '2026-07-18'
name: Casper
nav: Providers
network: true
overview: 'Casper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ecommerce, Retail, Sleep, and Mattresses.


  Casper''s developer surface includes authentication and 9 more developer resources.'
random_paper: 26
scopes:
- name: Casper Scopes
  scope_count: 4
  slug: casper-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: minimal
  composite: 14.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Casper Authentication
  slug: casper-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Casper Domain Security
  slug: casper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casper
tags:
- Company
- Ecommerce
- Retail
- Sleep
- Mattresses
- Direct to Consumer
- Agentic Commerce
- Shopify
website: https://casper.com
---
