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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-03'
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
  name: Revibe MCP Server
  slug: revibe-mcp-server
modified: '2026-07-20'
name: Revibe
nav: Providers
network: true
overview: 'Revibe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, E-Commerce, Refurbished Electronics, and Consumer Electronics.


  Revibe''s developer surface includes engineering blog, signup flow, authentication, and 8 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revibe/refs/heads/main/screenshots/revibe-2026-09-02T153722.png
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
