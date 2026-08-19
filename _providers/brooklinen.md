---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.6
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: Live Universal Commerce Protocol (UCP) endpoint exposed over MCP JSON-RPC at https://www.brooklinen.com/api/ucp/mcp, advertised by the store's own /agents.md, /robots.txt and /.well-known/ucp discover
  name: Brooklinen UCP / MCP Agentic Commerce API
  slug: brooklinen-ucp-mcp-agentic-commerce-api
- description: Read-only view of the current session cart.
  name: Brooklinen Cart API
  slug: brooklinen-cart-api
- description: Products grouped into merchandising collections.
  name: Brooklinen Collections API
  slug: brooklinen-collections-api
- description: Sitemaps and agent discovery documents.
  name: Brooklinen Discovery API
  slug: brooklinen-discovery-api
- description: Product catalog listing and detail.
  name: Brooklinen Products API
  slug: brooklinen-products-api
- description: Predictive storefront search.
  name: Brooklinen Search API
  slug: brooklinen-search-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Brooklinen Shopify Storefront JSON Cart API
  slug: open-brooklinen-cart-api
- collection_type: open
  name: Brooklinen Shopify Storefront JSON Collections API
  slug: open-brooklinen-collections-api
- collection_type: open
  name: Brooklinen Shopify Storefront JSON Discovery API
  slug: open-brooklinen-discovery-api
- collection_type: open
  name: Brooklinen Shopify Storefront JSON Products API
  slug: open-brooklinen-products-api
- collection_type: open
  name: Brooklinen Shopify Storefront JSON Search API
  slug: open-brooklinen-search-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brooklinen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brooklinen.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.brooklinen.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.brooklinen.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.brooklinen.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.brooklinen.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.brooklinen.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://www.brooklinen.com/blogs/brookliving
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brooklinen
- group: start
  title: ''
  type: SignUp
  url: https://www.brooklinen.com/pages/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.brooklinen.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brooklinen.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brooklinen.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brooklinen-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/brooklinen-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brooklinen-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brooklinen-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brooklinen-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brooklinen-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brooklinen-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/brooklinen-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brooklinen-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brooklinen-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brooklinen-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brooklinen-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brooklinen-storefront-overlay.yaml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/brooklinen_stock/
created: '2026-08-02'
description: 'Brooklinen is a direct-to-consumer home essentials brand founded in Brooklyn, New York in 2014 by Rich and Vicki Fulop, selling sheets, duvet covers, comforters, pillows, towels, robes and loungewear direct from the mill to the customer. Brooklinen publishes no traditional developer API program, but its storefront runs on Shopify and exposes a substantial machine-readable agent surface: an agent instruction document at /agents.md (mirrored at /llms.txt), a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp declaring protocol versions 2026-04-08 and 2026-01-23, a live UCP/MCP JSON-RPC endpoint at /api/ucp/mcp for agent-driven catalog search, cart, checkout and order operations, OAuth 2.0 / OIDC customer-account authorization metadata at /.well-known/oauth-authorization-server and /.well-known/oauth-protected-resource, and the read-only Shopify storefront JSON endpoints for products, collections, search suggestions and cart. Checkout explicitly requires contemporaneous
  human buyer approval.'
image: https://cdn.shopify.com/s/files/1/0951/7126/files/0126_Shopify_Social_Image.jpg?v=1765839763
layout: provider
mcp_servers:
- description: ''
  name: brooklinen-mcp.yml
  slug: brooklinen-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-02'
name: Brooklinen
nav: Providers
network: true
overview: 'Brooklinen publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Collections API, Discovery API, and 2 more. Tagged areas include ecommerce, retail, direct-to-consumer, home-goods, and bedding.


  Brooklinen''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 32
scopes:
- name: Brooklinen Scopes
  scope_count: 4
  slug: brooklinen-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: developing
  composite: 46.9
  delta: 1.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 54.7
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 45.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brooklinen/refs/heads/main/screenshots/brooklinen-2026-08-07T162830.png
security:
- kind: authentication
  name: Brooklinen Authentication
  slug: brooklinen-authentication
  summary_line: oauth2/openIdConnect/none · 4 schemes
- kind: domain-security
  name: Brooklinen Domain Security
  slug: brooklinen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brooklinen
tags:
- ecommerce
- retail
- direct-to-consumer
- home-goods
- bedding
- shopify
- agentic-commerce
- universal-commerce-protocol
- mcp
- agent-native
- catalog
- checkout
website: https://www.brooklinen.com/
---
