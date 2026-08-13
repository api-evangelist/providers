---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 192
  human_in_the_loop: 0
  name: Cart Com Agentic Access
  operation_count: 262
  slug: cart-com-agentic-access
  summary_line: 262 operations · 192 acting
api_count: 1
apis:
- description: 'The Cart.com Online Store API (formerly the AmeriCommerce REST API) is a JSON REST API scoped to a single merchant storefront domain. It exposes 136 paths and 262 operations across catalog (products, '
  name: Cart.com Online Store API
  slug: online-store-api
artifact_total: 8
asyncapis:
- description: ''
  name: Cart Com Online Store Webhooks
  slug: cart-com-online-store-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cart-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cart-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cart-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cart.com/docs/rest-api/ZG9jOjM2MjI2-the-online-store-api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cart.com/docs/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cart.com/docs/rest-api/ZG9jOjM2MjI2-the-online-store-api
- group: operate
  title: ''
  type: Support
  url: https://cart.com/contact/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://cart.com/knowledge
- group: company
  title: ''
  type: Blog
  url: https://cart.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmeriCommerce
- group: start
  title: ''
  type: SignUp
  url: https://console.cart.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cart.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cart.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://cart.canny.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cart.com/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cart-com-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cart-com-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cart-com-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cart-com-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cart-com-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cart-com-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cart-com-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cart-com-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/cart-com-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/cart-com-code-samples.yml
- group: design
  title: ''
  type: Components
  url: components/cart-com-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cart-com-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cart-com-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cart-com-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cart-com-online-store-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cart-com-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cart-com-online-store-webhooks.yml
created: '2026-07-31'
description: Cart.com is a unified commerce and logistics provider for B2C and B2B brands, combining an ecommerce storefront platform (the former AmeriCommerce Online Store), marketplace and channel management, order management, warehouse management, and a nationwide fulfillment network into a single operating system for commerce. Its developer surface is the Online Store API — a JSON REST API published as OpenAPI 3.1 covering catalog, orders, carts, customers, content, marketing, shipping and store settings — plus a webhook subscription system with thirty event types, an OAuth 2 authorization flow with coarse read/write scopes, and a client-side JavaScript Client API for storefront themes.
image: https://cart.com/hubfs/6316383d5bc18bb4fa6ae7a9_favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: cart-com-mcp.yml
  slug: cart-com-mcpyml
modified: '2026-07-31'
name: Cart.com
nav: Providers
network: true
overview: 'Cart.com publishes 1 API on the [APIs.io](https://apis.io/) network: Online Store API. Tagged areas include Company, E-Commerce, Retail, Order Management, and Fulfillment.


  The Cart.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cart.com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 28 more developer resources.'
random_paper: 70
rate_limits:
- limit_count: 5
  name: Cart Com Rate Limits
  slug: cart-com-rate-limits
scopes:
- name: Cart Com Scopes
  scope_count: 17
  slug: cart-com-scopes
  summary_line: 17 scopes · authorizationCode
score:
  band: developing
  composite: 55.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.6
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 84.2
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cart-com/refs/heads/main/screenshots/cart-com-2026-08-07T163035.png
security:
- kind: authentication
  name: Cart Com Authentication
  slug: cart-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cart Com Domain Security
  slug: cart-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cart-com
tags:
- Company
- E-Commerce
- Retail
- Order Management
- Fulfillment
- Logistics
- Marketplaces
- Storefront
- Catalog
- Shipping
website: https://cart.com/
---
