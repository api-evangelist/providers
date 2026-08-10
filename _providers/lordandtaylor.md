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
    well_known_catalog: true
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://lordandtaylor.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lordandtaylor-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lordandtaylor-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lordandtaylor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lordandtaylor-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.lordandtaylor.com/.well-known/openid-configuration
- group: design
  title: ''
  type: Conformance
  url: conformance/lordandtaylor-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lordandtaylor-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://account.lordandtaylor.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lordandtaylor.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lordandtaylor.com/policies/terms-of-service
created: '2026-07-17'
description: 'Lord & Taylor is one of the oldest American department-store apparel and home-goods retail brands, now operating as a direct-to-consumer online store at lordandtaylor.com. The storefront runs on the Shopify commerce platform, so its public, agent-accessible API surface is the Shopify commerce stack: OAuth 2.0 / OpenID Connect customer authentication (issued via Shopify Customer Accounts) plus two hosted Model Context Protocol (MCP) servers — an unauthenticated Storefront MCP exposing product search, cart, product-detail and store-policy tools, and an OAuth-protected Customer Account MCP exposing order-status, return-request and store-credit tools. Surfaced into the API Evangelist network as a portfolio-lead stub and enriched from live discovery documents and MCP tool listings.'
image: https://www.lordandtaylor.com/cdn/shop/files/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Lord & Taylor Shopify MCP servers (Storefront + Customer Account)
  slug: lord-taylor-shopify-mcp-servers-storefront-customer-account
modified: '2026-07-20'
name: Lord & Taylor
nav: Providers
network: true
overview: 'Lord & Taylor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Shopping.


  Lord & Taylor''s developer surface includes authentication and 10 more developer resources.'
random_paper: 15
scopes:
- name: Lordandtaylor Scopes
  scope_count: 4
  slug: lordandtaylor-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 61.1
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lordandtaylor/refs/heads/main/screenshots/lordandtaylor-2026-08-07T171807.png
security:
- kind: authentication
  name: Lordandtaylor Authentication
  slug: lordandtaylor-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Lordandtaylor Domain Security
  slug: lordandtaylor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lordandtaylor
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Shopping
- Department Store
- Agentic Commerce
- MCP
website: https://lordandtaylor.com
---
