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
- description: Agent-driven commerce surface for the Revibe Shopify store implemented via the Universal Commerce Protocol (UCP). A hosted MCP endpoint exposes catalog search, cart, checkout, and fulfillment tools; c
  name: Revibe UCP Shopping (MCP)
  slug: revibe-ucp-shopping-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://revibe.me/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.revibe.me/
- group: company
  title: ''
  type: Blog
  url: https://revibe.me/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://revibe.me/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revibe.me/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revibe.me/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revibe-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revibe-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revibe-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revibe-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revibe-domain-security.yml
created: '2026-07-17'
description: Revibe (Revibe Technology FZ-LLC) is a UAE-based e-commerce marketplace for certified refurbished and renewed electronics — iPhones, Samsung phones, MacBooks, laptops, iPads, TVs, and accessories — sold with a 12-month warranty, a 10-day return window, free UAE delivery, and buy-now-pay-later options (Tabby, Tamara, Split). Every device passes a 50-point quality check and the company reports accepting only one in four supplier lots. Revibe operates in the UAE (revibe.me), Saudi Arabia (sa.revibe.me), and South Africa (revibe.co.za), and runs a trade-in program (sell.revibe.me). The storefront is built on Shopify and natively implements the Universal Commerce Protocol (UCP, ucp.dev), exposing a hosted MCP endpoint for agent-driven catalog search, cart, and human-approved checkout, plus a published /llms.txt and Shopify Customer Account OpenID Connect discovery. Backed by Partech.
image: https://revibe.me/cdn/shop/files/revibe-logo.png
layout: provider
mcp_servers:
- description: ''
  name: revibe-mcp.yml
  slug: revibe-mcpyml
modified: '2026-07-20'
name: Revibe
nav: Providers
network: true
overview: 'Revibe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, E-Commerce, Refurbished Electronics, and Consumer Electronics.


  Revibe''s developer surface includes engineering blog, signup flow, authentication, and 8 more developer resources.'
random_paper: 21
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
  name: Revibe Authentication
  slug: revibe-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Revibe Domain Security
  slug: revibe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revibe
tags:
- Company
- Marketplace
- E-Commerce
- Refurbished Electronics
- Consumer Electronics
- Retail
- UAE
- Agentic Commerce
website: https://revibe.me/
---
