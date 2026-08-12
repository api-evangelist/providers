---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the wanelo.com storefront: a Universal Commerce Protocol (UCP) MCP endpoint for search/cart/checkout, Shopify Customer Account OAuth/OIDC, and unauthenticated Shopify'
  name: Wanelo Commerce (UCP)
  slug: wanelo-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://wanelo.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wanelo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wanelo-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wanelo-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wanelo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wanelo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wanelo-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wanelo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wanelo-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wanelo.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wanelo.com/policies/terms-of-service
created: '2026-07-17'
description: wanelo ("The intelligent everything store") is an AI-powered shopping storefront offering natural-language and visual product discovery, personalized recommendations, and a buy-for-me assistant, built on Shopify. It exposes an agent-commerce surface via the Universal Commerce Protocol (UCP, ucp.dev) with a hosted MCP endpoint for catalog search, cart, and buyer-approved checkout, plus Shopify Customer Account OAuth/OpenID Connect and a published /llms.txt (mirroring /agents.md). Originally a social-shopping product backed by Slow Ventures, wanelo.com now operates as an agent-ready commerce store. Read-only catalog browsing (products/collections/search JSON) requires no authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wanelo.png
layout: provider
mcp_servers:
- description: ''
  name: wanelo-mcp.yml
  slug: wanelo-mcpyml
modified: '2026-07-21'
name: wanelo
nav: Providers
network: true
overview: 'wanelo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shopping, Ecommerce, Retail, and Commerce.


  wanelo''s developer surface includes authentication and 10 more developer resources.'
random_paper: 66
scopes:
- name: Wanelo Scopes
  scope_count: 4
  slug: wanelo-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 17.2
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 18.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Wanelo Authentication
  slug: wanelo-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Wanelo Domain Security
  slug: wanelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wanelo
tags:
- Company
- Shopping
- Ecommerce
- Retail
- Commerce
- Agent Commerce
- MCP
- Shopify
- AI
website: https://wanelo.com
---
