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
    agent_skills: true
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
  score: 29.8
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: 'Live MCP endpoint implementing the Universal Commerce Protocol shopping service for the UNTUCKit store: catalog search, cart, checkout, fulfillment, discounts, and orders, with Shop Pay / Google Pay /'
  name: UNTUCKit Storefront Agent Commerce (UCP/MCP) API
  slug: untuckit-storefront-agent-commerce-ucpmcp-api
- description: 'Unauthenticated read-only Shopify storefront JSON documented in the store''s agents.md: product JSON at /products/{handle}.json, collection product listings at /collections/{handle}/products.json, prod'
  name: UNTUCKit Storefront Catalog JSON API
  slug: untuckit-storefront-catalog-json-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://untuckit.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/untuckit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/untuckit-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/untuckit-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/untuckit-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/untuckit-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/untuckit-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/untuckit-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/untuckit-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/untuckit-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.untuckit.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.untuckit.com/policies/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.untuckit.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.untuckit.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.untuckit.com/account/login
created: '2026-07-17'
description: 'UNTUCKit is a US apparel brand and omnichannel retailer best known for shirts designed to be worn untucked, selling menswear and womenswear through untuckit.com and its retail stores. Its Shopify-powered storefront is notably agent-ready: the store publishes agents.md and llms.txt operating instructions, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp for catalog search, cart, and buyer-approved checkout, OIDC/OAuth discovery for the Shopify Customer Account API, and unauthenticated product and collection JSON.'
image: https://avatars.githubusercontent.com/u/48734252?v=4
layout: provider
mcp_servers:
- description: ''
  name: untuckit-mcp.yml
  slug: untuckit-mcpyml
modified: '2026-07-21'
name: UNTUCKit
nav: Providers
network: true
overview: 'UNTUCKit publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apparel, Retail, eCommerce, and Shopify.


  UNTUCKit''s developer surface includes authentication, support, engineering blog, and 13 more developer resources.'
random_paper: 20
scopes:
- name: Untuckit Scopes
  scope_count: 4
  slug: untuckit-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 22.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Untuckit Authentication
  slug: untuckit-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Untuckit Domain Security
  slug: untuckit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: untuckit
tags:
- Company
- Apparel
- Retail
- eCommerce
- Shopify
- Agentic Commerce
- MCP
- UCP
website: https://untuckit.com
---
