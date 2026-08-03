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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.primary.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/primary-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/primary-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/primary-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/primary-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/primary-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/primary-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primary-domain-security.yml
created: '2026-07-17'
description: 'Primary (Primary Kids, Inc.) is a direct-to-consumer children''s apparel brand selling simple, slogan-free, mix-and-match clothing "in all colors, for all kids" — babies through age 14, plus adult sizes, swimwear, school uniforms and licensed Sesame Street collaborations. The company operates a Shopify-hosted online store at primary.com and is a portfolio company of Homebrew. Primary has no first-party developer API, but its storefront is agent-accessible: it serves a live hosted Shopify Storefront MCP server (catalog search, product lookup, cart, checkout, policy/FAQ lookup) and exposes Shopify''s Customer Account API (OAuth2/OIDC) for customer-scoped operations, along with a published llms.txt agent-instructions document.'
image: https://www.primary.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Primary Shopify Storefront MCP
  slug: primary-shopify-storefront-mcp
modified: '2026-07-20'
name: Primary
nav: Providers
network: true
overview: 'Primary is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, Ecommerce, and Apparel.


  Primary''s developer surface includes authentication and 7 more developer resources.'
random_paper: 12
scopes:
- name: Primary Scopes
  scope_count: 4
  slug: primary-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: minimal
  composite: 12.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Primary Authentication
  slug: primary-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Primary Domain Security
  slug: primary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: primary
tags:
- Company
- Consumer
- Retail
- Ecommerce
- Apparel
- Children
- Shopify
- Agent
website: https://www.primary.com
---
