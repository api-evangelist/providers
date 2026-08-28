---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: true
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kite Hill Agentic Access
  operation_count: 0
  slug: kite-hill-agentic-access
  summary_line: 0 operations
api_count: 3
apis:
- description: The Shopify Storefront GraphQL API as served from Kite Hill's own domain. Introspection is anonymous — the full schema (416 types, 34 query fields, 41 mutations, 28 Relay connections) was retrieved wi
  name: Kite Hill Storefront GraphQL API
  slug: storefront-graphql
- description: A live Model Context Protocol server on Kite Hill's storefront host. An anonymous JSON-RPC tools/list returned five tools with full JSON Schema input contracts — search_catalog, get_product_details, g
  name: Kite Hill Storefront MCP Server
  slug: storefront-mcp
- description: Kite Hill implements the Universal Commerce Protocol for agent-driven commerce. The merchant profile at /.well-known/ucp declares UCP 2026-04-08 and 2026-01-23, the dev.ucp.shopping MCP service endpoi
  name: Kite Hill UCP Agentic Commerce API
  slug: ucp-commerce
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://kite-hill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kite-hill.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kite-hill-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kite-hill-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kite-hill-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kite-hill-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kite-hill-agentic-access.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/kite-hill-storefront.graphql
- group: design
  title: ''
  type: DataModel
  url: data-model/kite-hill-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kite-hill-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kite-hill-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kite-hill-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kite-hill-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kite-hill-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kite-hill-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kite-hill-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kite-hill-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kite-hill-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kite-hill-domain-security.yml
- group: operate
  title: ''
  type: FAQ
  url: https://kite-hill.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://kite-hill.com/blogs/recipes
- group: company
  title: ''
  type: About
  url: https://kite-hill.com/pages/about-us
- group: operate
  title: ''
  type: ContactUs
  url: https://kite-hill.com/pages/contact
- group: operate
  title: ''
  type: Support
  url: https://kite-hill.com/pages/contact
- group: other
  title: ''
  type: StoreLocator
  url: https://kite-hill.com/pages/store-locator
- group: company
  title: ''
  type: Press
  url: https://kite-hill.com/pages/press-awards
- group: start
  title: ''
  type: SignUp
  url: https://kite-hill.com/account/register
- group: start
  title: ''
  type: Login
  url: https://kite-hill.com/account/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kite-hill.com/policies/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/kite-hill_stock/
created: '2026-08-23'
description: 'Kite Hill is an American plant-based food company founded in 2010 by chef Tal Ronnen, cheesemaker Monte Casino and Stanford biochemist Pat Brown, headquartered in Hayward, California, making almond-milk yogurts, Greek-style yogurts, cream cheese and sour cream alternatives, ricotta, dips and filled pastas sold at Whole Foods, Target, Sprouts, Publix and other grocers, and direct to consumers at kite-hill.com. Kite Hill runs no developer program and publishes no OpenAPI, but its Shopify-hosted storefront exposes a substantial machine-readable surface from its own domain: an anonymously introspectable Storefront GraphQL API, TWO live Model Context Protocol servers whose tools/list both answer anonymously, a Universal Commerce Protocol merchant profile at /.well-known/ucp, OpenID Connect and RFC 8414 discovery for customer accounts, and a provider-authored /agents.md and /llms.txt that tell AI agents which surface to use and that no agent may finalize payment without contemporaneous
  human approval.'
image: https://kite-hill.com/cdn/shop/files/OG_Image_2400x1260.png?v=1734547205
layout: provider
mcp_servers:
- description: Kite Hill serves TWO live MCP endpoints from its own storefront host, and BOTH answer an anonymous JSON-RPC tools/list with HTTP 200 and full JSON Schema input contracts. The Shopify Storefront MCP se
  name: Kite Hill MCP Server
  slug: kite-hill-mcp-server
modified: '2026-08-23'
name: Kite Hill
nav: Providers
network: true
overview: 'Kite Hill publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Plant Based Foods, Dairy Alternatives, and Food and Beverage.


  Kite Hill''s developer surface includes documentation, authentication, FAQ, engineering blog, support, signup flow, and 25 more developer resources.'
plans:
- name: Kite Hill Plans Pricing
  plan_count: 0
  slug: kite-hill-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Kite Hill Rate Limits
  slug: kite-hill-rate-limits
scopes:
- name: Kite Hill Scopes
  scope_count: 4
  slug: kite-hill-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 34.3
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Kite Hill Authentication
  slug: kite-hill-authentication
  summary_line: none/openIdConnect/oauth2/agentProfile/http · 7 schemes
- kind: domain-security
  name: Kite Hill Domain Security
  slug: kite-hill-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kite-hill
tags:
- Company
- Consumer Packaged Goods
- Plant Based Foods
- Dairy Alternatives
- Food and Beverage
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
- GraphQL
- MCP
- Universal Commerce Protocol
website: https://kite-hill.com/
---
