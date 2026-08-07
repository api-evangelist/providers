---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 2
  name: Coldsnap Agentic Access
  operation_count: 16
  slug: coldsnap-agentic-access
  summary_line: 16 operations · 10 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: 'The live Shopify Storefront GraphQL API served from the ColdSnap primary domain. Anonymously introspectable: a full introspection query returns 428 types, 35 root query fields and 41 mutations coverin'
  name: ColdSnap Storefront GraphQL API
  slug: coldsnap-storefront-graphql-api
- description: 'An anonymous, production Model Context Protocol server served from the ColdSnap domain at /api/mcp. A live tools/list returns five tools with full JSON Schema input contracts: search_catalog, get_prod'
  name: ColdSnap Storefront MCP Server
  slug: coldsnap-storefront-mcp-server
- description: 'The unauthenticated read-only JSON surface Shopify serves from the ColdSnap storefront and which the store''s own agents.md advertises to agents: /products.json and /collections.json catalog listings, '
  name: ColdSnap Store JSON (Ajax) API
  slug: coldsnap-store-json-ajax-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://coldsnap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://coldsnap.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://coldsnap.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://coldsnap.com/pages/customer-service
- group: operate
  title: ''
  type: HelpCenter
  url: https://coldsnap.com/pages/faq
- group: operate
  title: ''
  type: Contact
  url: https://coldsnap.com/pages/get-in-touch
- group: company
  title: ''
  type: Blog
  url: https://coldsnap.com/blogs/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://coldsnap.com/blogs/blog.atom
- group: commercial
  title: ''
  type: Pricing
  url: https://coldsnap.com/collections/machine
- group: start
  title: ''
  type: Login
  url: https://coldsnap.com/customer_authentication/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coldsnap.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coldsnap.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://coldsnap.com/policies/refund-policy
- group: company
  title: ''
  type: Press
  url: https://coldsnap.com/pages/press
- group: company
  title: ''
  type: Investors
  url: https://coldsnap.com/pages/investors
- group: other
  title: ''
  type: Patents
  url: https://coldsnap.com/pages/patents
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/coldsnap_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coldsnapchill/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/coldsnap_chill/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/coldsnapchill
- group: docs
  title: ''
  type: GraphQL
  url: graphql/coldsnap-storefront.graphql
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coldsnap-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/coldsnap-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coldsnap-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coldsnap-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coldsnap-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coldsnap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coldsnap-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coldsnap-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coldsnap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coldsnap-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coldsnap-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://shopify.dev/docs/api/usage/versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://www.shopifystatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coldsnap-changelog.yml
- group: docs
  title: ''
  type: APIReference
  url: https://shopify.dev/docs/api/storefront
- group: design
  title: ''
  type: DataModel
  url: data-model/coldsnap-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coldsnap-domain-security.yml
created: '2026-08-02'
description: ColdSnap (formerly Sigma Phase, Corp.) is a Billerica, Massachusetts hardware and frozen-confection company founded in October 2018 by Matt Fonte, whose plug-and-play countertop appliance chills and churns a single serving of premium ice cream, frozen yogurt, non-dairy dessert, frozen latte, protein shake, smoothie or frozen cocktail from a shelf-stable recyclable pod in about two minutes, with no refrigeration, plumbing or cleaning between servings. The company commercially launched in April 2024 and sells machines, pods and accessories to restaurants and bars, hotels, golf and sports clubs, colleges, senior living, car dealerships, offices, convenience stores and micro markets. Its digital surface is a Shopify-hosted commerce storefront at coldsnap.com serving a live, anonymously introspectable Storefront GraphQL API, an anonymous Model Context Protocol server at /api/mcp, a Universal Commerce Protocol (UCP) merchant profile and agentic-commerce endpoint, plus published llms.txt
  and agents.md agent-instruction documents.
image: https://cdn.shopify.com/s/files/1/0973/7895/9650/files/ColdSnap-Logo-0923-FullColor_Horizontal.png?v=1763516060
layout: provider
mcp_servers:
- description: ''
  name: coldsnap-mcp.yml
  slug: coldsnap-mcpyml
modified: '2026-08-04'
name: ColdSnap
nav: Providers
network: true
overview: 'ColdSnap publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Food and Beverage.


  ColdSnap''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, YouTube channel, authentication, and 32 more developer resources.'
random_paper: 61
scopes:
- name: Coldsnap Scopes
  scope_count: 4
  slug: coldsnap-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 47.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 48.1
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Coldsnap Authentication
  slug: coldsnap-authentication
  summary_line: none/openIdConnect/oauth2/apiKey · 6 schemes
- kind: domain-security
  name: Coldsnap Domain Security
  slug: coldsnap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coldsnap
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Food and Beverage
- Consumer Products
- Hardware
- Appliances
- Foodservice
- Agentic Commerce
- Shopify
- GraphQL
- Model Context Protocol
- Universal Commerce Protocol
website: https://coldsnap.com/
---
