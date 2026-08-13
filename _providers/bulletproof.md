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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: The Shopify Storefront GraphQL API served from the Bulletproof store host. Anonymous introspection succeeded on 2026-08-08 (424 types, QueryRoot + Mutation), and anonymous queries against shop, produc
  name: Bulletproof Storefront GraphQL API
  slug: bulletproof-storefront-graphql-api
- description: A live Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) for agent-driven commerce. An anonymous tools/list returned 13 tools with complete JSON Schema input contracts
  name: Bulletproof UCP Agentic Commerce MCP
  slug: bulletproof-ucp-agentic-commerce-mcp
- description: 'The unauthenticated Shopify storefront JSON catalog endpoints (/products.json, /collections.json, /products/{handle}.json, /collections/{handle}/products.json) documented in the store''s own agents.md '
  name: Bulletproof Storefront JSON Catalog
  slug: bulletproof-storefront-json-catalog
- description: The WordPress REST API behind the Bulletproof editorial site (bulletproof.com), self-describing 16 namespaces and 384 routes at /wp-json/ with no authentication schemes advertised. Covers posts, pages
  name: Bulletproof WordPress Content REST API
  slug: bulletproof-wordpress-content-rest-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://www.bulletproof.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bulletproof_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.bulletproof.com/agents.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bulletproof360
- group: company
  title: ''
  type: Blog
  url: https://www.bulletproof.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.bulletproof.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://shop.bulletproof.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://shop.bulletproof.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shop.bulletproof.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shop.bulletproof.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bulletproof-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bulletproof-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bulletproof-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bulletproof-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bulletproof-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bulletproof-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bulletproof-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/bulletproof-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bulletproof-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bulletproof-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bulletproof-domain-security.yml
created: '2026-08-08'
description: 'Bulletproof (Bulletproof 360, Inc.) is a Seattle-founded functional nutrition and health-and-wellness brand — toxin-tested coffee, C8 MCT oil, collagen, creamers and supplements — founded in 2013 by Dave Asprey and sold direct-to-consumer and through national retail. Bulletproof is not a software vendor and publishes no developer program, yet its commerce and content stacks expose a real, callable, unauthenticated machine surface: a Shopify Storefront GraphQL API that answers introspection anonymously at shop.bulletproof.com, a live UCP (Universal Commerce Protocol) MCP endpoint whose tools/list returns 13 agent tools with full JSON Schema input contracts, OAuth 2.0 / OpenID Connect discovery documents for customer accounts, agent-facing llms.txt and agents.md instructions on the storefront, and a 384-route WordPress REST API behind the editorial site.'
examples:
- key_count: 2
  name: Bulletproof Storefront Graphql Response
  slug: bulletproof-storefront-graphql-response
- key_count: 1
  name: Bulletproof Storefront Products Json
  slug: bulletproof-storefront-products-json
- key_count: 3
  name: Bulletproof Ucp Mcp Initialize
  slug: bulletproof-ucp-mcp-initialize
image: https://cdn.shopify.com/s/files/1/0004/3470/0319/files/bp-logo-large.png?v=1785948157
layout: provider
mcp_servers:
- description: ''
  name: bulletproof-mcp.yml
  slug: bulletproof-mcpyml
modified: '2026-08-08'
name: BulletProof
nav: Providers
network: true
overview: 'BulletProof publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Food and Beverage, Health and Wellness, and Supplements.


  BulletProof''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 118
scopes:
- name: Bulletproof Scopes
  scope_count: 4
  slug: bulletproof-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 43.2
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 36.4
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Bulletproof Authentication
  slug: bulletproof-authentication
  summary_line: none/oauth2/openIdConnect/bearer · 6 schemes
- kind: domain-security
  name: Bulletproof Domain Security
  slug: bulletproof-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bulletproof
tags:
- Company
- Consumer Packaged Goods
- Food and Beverage
- Health and Wellness
- Supplements
- Ecommerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
website: https://www.bulletproof.com/
---
