---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: The Dolls Kill Universal Commerce Protocol (UCP) endpoint, served over MCP at /api/ucp/mcp. Anonymous tools/list returns 13 tools with full JSON Schema input contracts covering catalog search and look
  name: Dolls Kill UCP Commerce MCP API
  slug: dolls-kill-ucp-commerce-mcp-api
- description: The Shopify Storefront GraphQL API as served from Dolls Kill's own host at /api/{version}/graphql.json. Anonymous introspection succeeds without a storefront access token, returning 424 types, 31 root
  name: Dolls Kill Storefront GraphQL API
  slug: dolls-kill-storefront-graphql-api
- description: 'The read-only, unauthenticated JSON endpoints Dolls Kill documents in its own agents.md for agents that only need to browse the store: /products.json, /products/{handle}.json, /collections/{handle}/pr'
  name: Dolls Kill Storefront Product JSON API
  slug: dolls-kill-storefront-product-json-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.dollskill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dollskill.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dolls-kill-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://help.dollskill.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.dollskill.com/
- group: start
  title: ''
  type: SignUp
  url: https://account.dollskill.com/authentication/login
- group: start
  title: ''
  type: Login
  url: https://account.dollskill.com/authentication/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dollskill.com/pages/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dollskill.com/pages/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/dolls-kill-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dolls-kill-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dolls-kill-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dolls-kill-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/dolls-kill-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dolls-kill-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dolls-kill-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dolls-kill-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dolls-kill-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dolls-kill-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/dolls-kill-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dolls-kill-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/dolls-kill_stock/
created: '2026-08-12'
description: 'Dolls Kill is a Los Angeles-based online fashion boutique for alternative, punk, goth, glam, rave and festival style, founded in 2011 and operating dollskill.com plus physical store locations. Its commerce platform runs on Shopify, and its public machine-readable surface is agent-facing rather than a conventional developer program: the storefront serves an agents.md / llms.txt agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live anonymous-readable MCP endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools, an openly introspectable Shopify Storefront GraphQL API, and OAuth 2.0 / OpenID Connect discovery for customer accounts. Dolls Kill publishes no developer portal, no OpenAPI, no SDKs and no API pricing — the API surface exists to let shopping agents transact, under an explicit human-approval-before-payment rule.'
image: https://www.dollskill.com/cdn/shop/files/logo.jpg?v=1709315110
layout: provider
mcp_servers:
- description: ''
  name: Dolls Kill MCP Server
  slug: dolls-kill-mcp-server
modified: '2026-08-12'
name: Dolls Kill
nav: Providers
network: true
overview: 'Dolls Kill publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Fashion, and Apparel.


  Dolls Kill''s developer surface includes documentation, support, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Dolls Kill Plans Pricing
  plan_count: 0
  slug: dolls-kill-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Dolls Kill Rate Limits
  slug: dolls-kill-rate-limits
scopes:
- name: Dolls Kill Scopes
  scope_count: 4
  slug: dolls-kill-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 43.3
    developer_ergonomics: 28.0
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 38.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Dolls Kill Authentication
  slug: dolls-kill-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 4 schemes
- kind: domain-security
  name: Dolls Kill Domain Security
  slug: dolls-kill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dolls-kill
tags:
- Company
- Retail
- E-Commerce
- Fashion
- Apparel
- Commerce
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- GraphQL
- Direct to Consumer
website: https://www.dollskill.com/
---
