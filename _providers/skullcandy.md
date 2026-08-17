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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: Universal Commerce Protocol (UCP) merchant surface for the Skullcandy Shopify storefront. Agents discover capabilities at /.well-known/ucp and transact against a hosted MCP endpoint (catalog search, c
  name: Skullcandy Agentic Commerce (UCP)
  slug: skullcandy-agentic-commerce-ucp
- description: 'Shopify Customer Account API for the Skullcandy store, secured with OpenID Connect / OAuth 2.0 (authorization code + PKCE). Scopes include customer-account-api:full and customer-account-mcp-api:full. '
  name: Skullcandy Customer Account API (Shopify)
  slug: skullcandy-customer-account-api-shopify
- description: 'Unauthenticated read-only storefront endpoints for browsing catalog data: product JSON (/products/{handle}.json), collection JSON (/collections/{handle}/products.json), search, and sitemap.xml.'
  name: Skullcandy Storefront Data (read-only)
  slug: skullcandy-storefront-data-read-only
artifact_total: 7
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skullcandy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skullcandy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skullcandy-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skullcandy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skullcandy-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skullcandy-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skullcandy-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://shopify.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ucp.dev/2026-04-08/specification/overview/
- group: operate
  title: ''
  type: Support
  url: https://support.skullcandy.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skullcandy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skullcandy.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skullcandy.com/policies/terms-of-service
created: '2026-07-17'
description: 'Skullcandy is a US consumer-audio brand that designs and sells headphones, wireless earbuds, gaming headsets, and Bluetooth speakers. Its e-commerce storefront at skullcandy.com runs on Shopify, and rather than a traditional developer program the brand exposes a modern agentic-commerce surface: an agent-facing llms.txt / agents.md, a Universal Commerce Protocol (UCP) merchant profile with a hosted Model Context Protocol (MCP) endpoint for catalog search, cart, checkout and fulfillment, a Shopify Customer Account API secured with OpenID Connect / OAuth 2.0 (including a customer-account MCP scope), and read-only storefront JSON endpoints for products and collections. This profile captures that agent- and API-facing surface as discovered on the live site.'
image: https://www.skullcandy.com/cdn/shop/files/new-social.jpg?v=1726116747
layout: provider
mcp_servers:
- description: ''
  name: skullcandy-mcp.yml
  slug: skullcandy-mcpyml
modified: '2026-07-21'
name: Skullcandy
nav: Providers
network: true
overview: 'Skullcandy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Audio, Headphones, and E-Commerce.


  Skullcandy''s developer surface includes authentication, documentation, support, and 10 more developer resources.'
random_paper: 39
scopes:
- name: Skullcandy Scopes
  scope_count: 4
  slug: skullcandy-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.4
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Skullcandy Authentication
  slug: skullcandy-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Skullcandy Domain Security
  slug: skullcandy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skullcandy
tags:
- Company
- Consumer Electronics
- Audio
- Headphones
- E-Commerce
- Retail
- Shopify
- Agentic Commerce
- MCP
- Universal Commerce Protocol
website: https://shopify.dev
---
