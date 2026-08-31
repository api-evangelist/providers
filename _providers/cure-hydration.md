---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'A live, first-party, anonymously discoverable Model Context Protocol server implementing the Shopify Universal Commerce Protocol shopping service for the CURE storefront. Thirteen tools cover catalog '
  name: CURE Universal Commerce Protocol (UCP) MCP Server
  slug: cure-universal-commerce-protocol-ucp-mcp-server
- description: 'The Shopify Storefront GraphQL API served on Cure Hydration''s own apex domain, pinned to API version 2026-04. Full introspection answered anonymously on 2026-08-11 — 416 types, 35 root queries and 41 '
  name: CURE Storefront GraphQL API
  slug: cure-storefront-graphql-api
- description: Read-only, unauthenticated JSON endpoints the store documents for agents in /agents.md — product list, product detail by handle, collection list, collection products, store metadata and search. Unvers
  name: CURE Storefront JSON Endpoints
  slug: cure-storefront-json-endpoints
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.curehydration.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.curehydration.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.curehydration.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: skills/cure-hydration-browse-catalog.md
- group: operate
  title: ''
  type: Support
  url: https://www.curehydration.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.curehydration.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://www.curehydration.com/blogs/news
- group: commercial
  title: ''
  type: Pricing
  url: https://www.curehydration.com/collections/shop-all
- group: start
  title: ''
  type: SignUp
  url: https://www.curehydration.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curehydration.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curehydration.com/policies/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.curehydration.com/pages/about-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cure-hydration-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cure-hydration-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/cure-hydration-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/cure-hydration-storefront.graphql
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cure-hydration-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/cure-hydration-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/cure-hydration-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cure-hydration-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cure-hydration-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cure-hydration-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cure-hydration-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cure-hydration-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cure-hydration-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cure-hydration-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cure-hydration-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cure-hydration-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cure-hydration-domain-security.yml
created: '2026-08-11'
description: 'Cure Hydration (CURE) is a New York based direct-to-consumer beverage brand founded in 2019 by Lauren Picasso, selling plant-based electrolyte drink mixes built on the World Health Organization''s Oral Rehydration Solution formula — organic coconut water, pink Himalayan salt, no added sugar. It is not a software company and it runs no developer programme, but its Shopify storefront serves a substantive first-party machine surface: a live Universal Commerce Protocol (UCP 2026-04-08) MCP server at /api/ucp/mcp with 13 catalog, cart, checkout and order tools, an anonymously introspectable Storefront GraphQL API, agent instructions at /agents.md and /llms.txt, a dedicated agent-discovery sitemap, and OpenID Connect discovery for shopper accounts. This profile records that surface as probed.'
examples:
- key_count: 1
  name: Cure Hydration Collections Example
  slug: cure-hydration-collections-example
- key_count: 16
  name: Cure Hydration Meta Example
  slug: cure-hydration-meta-example
- key_count: 1
  name: Cure Hydration Products Example
  slug: cure-hydration-products-example
image: https://www.curehydration.com/cdn/shop/files/cure-logo1.jpg?v=1646413004
layout: provider
mcp_servers:
- description: CURE (Cure Hydration) serves a live, first-party, anonymously reachable Model Context Protocol server on its own domain at /api/ucp/mcp. It is the Shopify Universal Commerce Protocol (UCP) shopping se
  name: CURE Universal Commerce Protocol (UCP) MCP Server
  slug: cure-universal-commerce-protocol-ucp-mcp-server
modified: '2026-08-11'
name: Cure Hydration
nav: Providers
network: true
overview: 'Cure Hydration publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Beverages, Health and Wellness, and E-Commerce.


  Cure Hydration''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Cure Hydration Plans Pricing
  plan_count: 0
  slug: cure-hydration-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Cure Hydration Rate Limits
  slug: cure-hydration-rate-limits
scopes:
- name: Cure Hydration Scopes
  scope_count: 0
  slug: cure-hydration-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cure-hydration/refs/heads/main/screenshots/cure-hydration-2026-08-17T080844.png
security:
- kind: authentication
  name: Cure Hydration Authentication
  slug: cure-hydration-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Cure Hydration Domain Security
  slug: cure-hydration-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cure-hydration
tags:
- Company
- Consumer Packaged Goods
- Beverages
- Health and Wellness
- E-Commerce
- Direct to Consumer
- Retail
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- GraphQL
website: https://www.curehydration.com
---
