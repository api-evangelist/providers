---
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Adrenalineshoc Agentic Access
  operation_count: 13
  slug: adrenalineshoc-agentic-access
  summary_line: 13 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: An anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service on the Accelerator Active Energy storefront host. tools/list returns thirteen tools wit
  name: Accelerator Active Energy UCP Commerce MCP API
  slug: adrenalineshoc-ucp-commerce-mcp
- description: The Shopify Storefront GraphQL API as deployed on the Accelerator Active Energy domain. Anonymous full introspection is open and returns 428 types, 34 query root fields and 41 mutations covering produ
  name: Accelerator Active Energy Storefront GraphQL API
  slug: adrenalineshoc-storefront-graphql
- description: The read-only JSON surface the store's own agent instructions document for agents that only need to browse catalog data without transacting - product JSON by handle, collection product listings, and p
  name: Accelerator Active Energy Storefront JSON Endpoints
  slug: adrenalineshoc-storefront-json
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adrenalineshoc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.drinkaccelerator.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.drinkaccelerator.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adrenalineshoc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adrenalineshoc-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/adrenalineshoc-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/adrenalineshoc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adrenalineshoc-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adrenalineshoc-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adrenalineshoc-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adrenalineshoc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adrenalineshoc-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adrenalineshoc-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adrenalineshoc-agentic-access.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adrenalineshoc-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adrenalineshoc-rate-limits.yml
- group: start
  title: ''
  type: Login
  url: https://www.drinkaccelerator.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.drinkaccelerator.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.drinkaccelerator.com/pages/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.drinkaccelerator.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.drinkaccelerator.com/policies/privacy-policy
created: '2026-09-07'
description: 'Adrenaline Shoc (A SHOC) is the performance energy drink brand of A Shoc Beverage, LLC, trading today as Accelerator Active Energy and headquartered in Newport Beach, California. Founded in 2019 by beverage entrepreneur Lance Collins, the company sells zero-sugar 16oz energy drinks built on a plant-based caffeine blend of green coffee bean, yerba mate, coffee fruit extract and guarana with electrolytes and amino acids, distributed nationally through Keurig Dr Pepper and sold in roughly 80,000 US retail doors. It is not a software company and publishes no developer program, OpenAPI, SDK or API reference. Its entire public machine-readable surface is its direct-to-consumer storefront at drinkaccelerator.com (ashoc.com redirects there): a Shopify-hosted store that serves agent instructions at /agents.md and /llms.txt, a Universal Commerce Protocol merchant profile at /.well-known/ucp, an anonymous Model Context Protocol endpoint exposing thirteen catalog, cart, checkout and order
  tools, and an openly introspectable Storefront GraphQL API. The storefront catalog itself is currently empty — /products.json returns zero products and the sitemap index carries no product sitemap — so the commerce protocol is live over a store that sells nothing online; purchase is directed to Amazon and physical retail.'
image: https://www.drinkaccelerator.com/cdn/shop/files/email-template-header2.png?v=1698185358
layout: provider
mcp_servers:
- description: ''
  name: Adrenaline Shoc MCP Server
  slug: adrenaline-shoc-mcp-server
modified: '2026-09-07'
name: Adrenaline Shoc
nav: Providers
network: true
overview: 'Adrenaline Shoc publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beverage, Energy Drinks, Consumer Packaged Goods, and Retail.


  Adrenaline Shoc''s developer surface includes documentation, authentication, support, and 19 more developer resources.'
plans:
- name: Adrenalineshoc Plans Pricing
  plan_count: 0
  slug: adrenalineshoc-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Adrenalineshoc Rate Limits
  slug: adrenalineshoc-rate-limits
scopes:
- name: Adrenalineshoc Scopes
  scope_count: 4
  slug: adrenalineshoc-scopes
  summary_line: 4 scopes · authorizationCode
security:
- kind: authentication
  name: Adrenalineshoc Authentication
  slug: adrenalineshoc-authentication
  summary_line: none/oauth2/openIdConnect/apiKey · 6 schemes
- kind: domain-security
  name: Adrenalineshoc Domain Security
  slug: adrenalineshoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adrenalineshoc
tags:
- Company
- Beverage
- Energy Drinks
- Consumer Packaged Goods
- Retail
- E-Commerce
- Direct to Consumer
- Agentic Commerce
- Shopify
- Sports Nutrition
website: https://www.drinkaccelerator.com/
---
