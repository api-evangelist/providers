---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 36.2
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: The Universal Commerce Protocol commerce server David serves at davidprotein.com/api/ucp/mcp, advertised in the store robots.txt and agents.md. Thirteen MCP tools cover catalog search and lookup, prod
  name: David Protein UCP Commerce MCP
  slug: david-protein-ucp-commerce-mcp
- description: 'The Shopify storefront MCP server David serves at davidprotein.com/api/mcp, declared in the storefront page as window.Shopify.MCP.mcpEndpoint and mirrored into the browser through the WebMCP adapter. '
  name: David Protein Storefront MCP
  slug: david-protein-storefront-mcp
- description: 'The customer-account MCP server David serves at account.davidprotein.com/customer/api/mcp. Four tools: get_most_recent_order_status, get_order_status, get_store_credit_balances and request_return. too'
  name: David Protein Customer Account MCP
  slug: david-protein-customer-account-mcp
- description: 'The unauthenticated read-only JSON surface David documents in agents.md for agents that only need to browse: /products.json and /collections.json store-wide, /products/{handle}.json per product, /coll'
  name: David Protein Storefront JSON
  slug: david-protein-storefront-json
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/david-protein-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://davidprotein.com
- group: docs
  title: ''
  type: Documentation
  url: https://davidprotein.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://davidprotein.com/agents.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/david-protein-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/david-protein-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/david-protein-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/david-protein-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/david-protein-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/david-protein-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/david-protein-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/david-protein-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/david-protein-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/david-protein-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/david-protein-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/david-protein-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/david-protein-packages.yml
- group: design
  title: ''
  type: Components
  url: components/david-protein-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/david-protein-data-model.yml
- group: operate
  title: ''
  type: Support
  url: https://davidprotein.com/pages/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://davidprotein.com/pages/frequently-asked-questions
- group: company
  title: ''
  type: Blog
  url: https://davidprotein.com/blogs/the-column
- group: company
  title: ''
  type: BlogRSS
  url: https://davidprotein.com/blogs/the-column.atom
- group: commercial
  title: ''
  type: Pricing
  url: https://davidprotein.com/collections/shop
- group: start
  title: ''
  type: SignUp
  url: https://davidprotein.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://davidprotein.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://davidprotein.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://davidprotein.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://davidprotein.com/policies/shipping-policy
- group: company
  title: ''
  type: Careers
  url: https://davidprotein.com/pages/careers
- group: company
  title: ''
  type: Investors
  url: https://www.hiive.com/securities/david-protein-stock
created: '2026-08-11'
description: 'David is a New York nutrition company founded in 2023 by RXBAR co-founder Peter Rahal, selling high-protein bars (28g protein, 150 calories, 0g sugar), the Bronze and Gold bar lines, and protein ice cream pints direct-to-consumer, through wholesale, and in retail. David runs no developer program and publishes no OpenAPI, but its Shopify-hosted storefront at davidprotein.com serves a complete agent-commerce surface from its own hostnames: an agents.md / llms.txt instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, OAuth 2.0 and OpenID Connect discovery documents, and three live Model Context Protocol servers covering catalog search, product lookup, cart, checkout, shop policy Q&A, order status and returns.'
image: https://davidprotein.com/cdn/shop/files/Group_524_4.png?v=1776707158
layout: provider
mcp_servers:
- description: ''
  name: David Protein MCP Server
  slug: david-protein-mcp-server
modified: '2026-08-11'
name: David Protein
nav: Providers
network: true
overview: 'David Protein publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, MCP, Universal Commerce Protocol, Commerce, and E-Commerce.


  David Protein''s developer surface includes documentation, getting-started guide, authentication, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: David Protein Plans Pricing
  plan_count: 0
  slug: david-protein-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: David Protein Rate Limits
  slug: david-protein-rate-limits
scopes:
- name: David Protein Scopes
  scope_count: 4
  slug: david-protein-scopes
  summary_line: 4 scopes · authorizationCode/refreshToken/urn:ietf:params:oauth:grant-type:jwt-bearer
score:
  band: thin
  composite: 32.1
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
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/david-protein/refs/heads/main/screenshots/david-protein-2026-09-02T145223.png
security:
- kind: authentication
  name: David Protein Authentication
  slug: david-protein-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: David Protein Domain Security
  slug: david-protein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: david-protein
tags:
- Agents
- MCP
- Universal Commerce Protocol
- Commerce
- E-Commerce
- Shopping
- Catalog
- Checkout
- Nutrition
- Food and Beverage
- Consumer Packaged Goods
- Shopify
website: https://davidprotein.com
---
