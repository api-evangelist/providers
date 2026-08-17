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
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the CandyClub Shopify storefront: a Universal Commerce Protocol (UCP) MCP endpoint plus read-only storefront browsing, governed by an llms.txt agent guide and Shopify'
  name: CandyClub Agent Commerce (UCP)
  slug: candyclub-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://candyclub.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/candyclub-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/candyclub-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/candyclub-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/candyclub-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/candyclub-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/candyclub-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/candyclub-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://account.candyclub.com/authentication/oauth/authorize
- group: commercial
  title: ''
  type: TermsOfService
  url: https://candyclub.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://candyclub.com/policies/privacy-policy
created: '2026-07-17'
description: 'CandyClub is a premium candy and confectionery brand founded in 2015, best known for its direct-to-consumer candy subscription boxes and its wholesale program that supplies curated specialty candies to boutique shops, hotels, resorts, and national retailers. The candyclub.com storefront runs on Shopify and is agent-commerce ready: it publishes an llms.txt agent guide, Shopify Customer Account OpenID Connect authentication, and a Universal Commerce Protocol (UCP) MCP endpoint that lets AI shopping agents search the catalog, build carts, apply discounts, and complete buyer-approved checkouts. CandyClub was added to the API Evangelist network as a 500 Global portfolio company; this profile is enriched from its public storefront, well-known discovery documents, and UCP/agent surface.'
image: https://candyclub.com/cdn/shop/files/cc_logo.webp?v=1767705737&width=300
layout: provider
mcp_servers:
- description: ''
  name: candyclub-mcp.yml
  slug: candyclub-mcpyml
modified: '2026-07-18'
name: CandyClub
nav: Providers
network: true
overview: 'CandyClub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Candy, Confectionery, Ecommerce, and Subscription.


  CandyClub''s developer surface includes authentication and 10 more developer resources.'
random_paper: 55
scopes:
- name: Candyclub Scopes
  scope_count: 4
  slug: candyclub-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/candyclub/refs/heads/main/screenshots/candyclub-2026-08-07T162931.png
security:
- kind: authentication
  name: Candyclub Authentication
  slug: candyclub-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Candyclub Domain Security
  slug: candyclub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: candyclub
tags:
- Company
- Candy
- Confectionery
- Ecommerce
- Subscription
- Retail
- Shopify
- Agent Commerce
- UCP
website: https://candyclub.com
---
