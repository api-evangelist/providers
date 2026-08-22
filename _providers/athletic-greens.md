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
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The Shopify Storefront GraphQL API as served from AG1's own storefront host, shop.drinkag1.com. Anonymous schema introspection succeeds, exposing 35 query fields, 41 mutations and 416 types covering p
  name: AG1 Storefront GraphQL API
  slug: athletic-greens-storefront-graphql
- description: Anonymous Model Context Protocol server on AG1's storefront host exposing five tools - search_catalog, get_product_details, get_cart, update_cart and search_shop_policies_and_faqs - with full JSON Sch
  name: AG1 Storefront MCP Server
  slug: athletic-greens-storefront-mcp
- description: The Universal Commerce Protocol MCP transport for AG1's store, advertised in the store's /.well-known/ucp merchant profile. Implements the dev.ucp.shopping service at UCP 2026-04-08 with cart, checkou
  name: AG1 UCP Commerce Endpoint
  slug: athletic-greens-ucp-mcp
- description: Model Context Protocol server on AG1's customer account host exposing four order-management tools - get_most_recent_order_status, get_order_status, get_store_credit_balances and request_return. tools/
  name: AG1 Customer Account MCP Server
  slug: athletic-greens-customer-account-mcp
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athletic-greens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drinkag1.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/athletic-greens_stock/
- group: operate
  title: ''
  type: FAQ
  url: https://drinkag1.com/about-ag1/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkag1.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkag1.com/about-us/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: mailto:support@drinkag1.com
- group: start
  title: ''
  type: SignUp
  url: https://drinkag1.com/members
- group: docs
  title: ''
  type: Documentation
  url: https://shop.drinkag1.com/agents.md
- group: docs
  title: ''
  type: GraphQL
  url: graphql/athletic-greens-storefront.graphql
- group: agent
  title: ''
  type: MCPServer
  url: mcp/athletic-greens-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/athletic-greens-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/athletic-greens-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/athletic-greens-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/athletic-greens-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/athletic-greens-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/athletic-greens-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/athletic-greens-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/athletic-greens-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/athletic-greens-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/athletic-greens-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/athletic-greens-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-02'
description: 'AG1 (formerly Athletic Greens) is a direct-to-consumer health and nutrition company founded in December 2010 by Chris Ashenden and headquartered in Carson City, Nevada. It sells a single flagship product - AG1, a daily foundational nutrition powder - on a subscription model through drinkag1.com, and the brand was renamed from Athletic Greens to AG1 in December 2021. Revenue grew from roughly $160M in 2021 to approximately $600M in 2024, with a valuation near $1.2B reported in January 2025, built largely on podcast and creator affiliate marketing. AG1 is a consumer commerce business rather than a developer-facing API provider - it publishes no developer portal, no API reference and no OpenAPI - but its Shopify storefront at shop.drinkag1.com does expose a real, anonymously reachable agentic commerce surface: a Universal Commerce Protocol (UCP 2026-04-08) merchant profile at /.well-known/ucp, a Storefront MCP server at /api/mcp, a UCP/MCP commerce endpoint at /api/ucp/mcp, a
  Customer Account MCP server at account.drinkag1.com, an introspectable Shopify Storefront GraphQL API, and published agents.md / llms.txt / robots.txt agent instructions. Authentication for customer-scoped surfaces is Shopify customer accounts OAuth 2.0 + OpenID Connect with PKCE.'
image: https://cdn.shopify.com/s/files/1/1523/4600/files/pouch_original_ae887f0b-a676-4453-adba-76bc51c30214.png?v=1770236075
layout: provider
mcp_servers:
- description: ''
  name: athletic-greens-mcp.yml
  slug: athletic-greens-mcpyml
modified: '2026-08-02'
name: AG1
nav: Providers
network: true
overview: 'AG1 publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Health, Nutrition, and Supplements.


  AG1''s developer surface includes FAQ, support, signup flow, documentation, authentication, and 18 more developer resources.'
random_paper: 2
scopes:
- name: Athletic Greens Scopes
  scope_count: 4
  slug: athletic-greens-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.6
  delta: -3.3
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 43.3
    developer_ergonomics: 28.0
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/athletic-greens/refs/heads/main/screenshots/athletic-greens-2026-08-07T161847.png
security:
- kind: authentication
  name: Athletic Greens Authentication
  slug: athletic-greens-authentication
  summary_line: oauth2/openIdConnect/none · 4 schemes
- kind: domain-security
  name: Athletic Greens Domain Security
  slug: athletic-greens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: athletic-greens
tags:
- Company
- Consumer
- Health
- Nutrition
- Supplements
- Direct to Consumer
- Ecommerce
- Subscription
- Wellness
- Agentic Commerce
- MCP
- UCP
- Shopify
- GraphQL
website: https://drinkag1.com/
---
