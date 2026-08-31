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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Makeup By Mario Agentic Access
  operation_count: 3
  slug: makeup-by-mario-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Shopify Storefront GraphQL API as served from MAKEUP BY MARIO's own domain. Introspection is anonymous — the full schema (416 types, 34 query fields, 41 mutations, 28 Relay connections, 49 depreca
  name: MAKEUP BY MARIO Storefront GraphQL API
  slug: storefront-graphql
- description: A live Model Context Protocol server on the MAKEUP BY MARIO storefront host. An anonymous JSON-RPC tools/list returned five tools with full JSON Schema input contracts — search_catalog, get_product_de
  name: MAKEUP BY MARIO Storefront MCP Server
  slug: storefront-mcp
- description: 'MAKEUP BY MARIO implements the Universal Commerce Protocol for agent-driven commerce. The merchant profile at /.well-known/ucp declares UCP 2026-04-08 and 2026-01-23, the dev.ucp.shopping MCP service '
  name: MAKEUP BY MARIO UCP Agentic Commerce API
  slug: ucp-commerce
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.makeupbymario.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.makeupbymario.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/makeup-by-mario-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/makeup-by-mario-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/makeup-by-mario-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/makeup-by-mario-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/makeup-by-mario-agentic-access.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/makeup-by-mario-storefront.graphql
- group: design
  title: ''
  type: DataModel
  url: data-model/makeup-by-mario-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/makeup-by-mario-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/makeup-by-mario-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/makeup-by-mario-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/makeup-by-mario-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/makeup-by-mario-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/makeup-by-mario-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/makeup-by-mario-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/makeup-by-mario-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/makeup-by-mario-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/makeup-by-mario-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/makeup-by-mario-domain-security.yml
- group: company
  title: ''
  type: About
  url: https://www.makeupbymario.com/pages/about
- group: operate
  title: ''
  type: FAQ
  url: https://www.makeupbymario.com/pages/frequently-asked-questions
- group: operate
  title: ''
  type: Support
  url: https://www.makeupbymario.com/pages/contact-us
- group: operate
  title: ''
  type: ContactUs
  url: https://www.makeupbymario.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.makeupbymario.com/blogs/education
- group: other
  title: ''
  type: LoyaltyProgram
  url: https://www.makeupbymario.com/pages/rewards
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.makeupbymario.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.makeupbymario.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.makeupbymario.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://www.makeupbymario.com/policies/shipping-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.makeupbymario.com/pages/cookies
- group: other
  title: ''
  type: DoNotSell
  url: https://www.makeupbymario.com/pages/do-not-sell-my-data
created: '2026-08-25'
description: 'MAKEUP BY MARIO is a New York-based prestige colour-cosmetics brand founded by celebrity makeup artist Mario Dedivanovic and launched direct-to-consumer in October 2020, selling face, eye, lip, brow, blush and tool products at makeupbymario.com and through Sephora. Self-funded for its first two and a half years, it took a $40M minority growth investment from Provenance and Silas Capital in January 2023. It runs no developer program and publishes no OpenAPI, but its Shopify-hosted storefront exposes a substantial machine-readable surface from its own domain: an anonymously introspectable Storefront GraphQL API, TWO live Model Context Protocol servers whose tools/list both answer anonymously, a Universal Commerce Protocol merchant profile at /.well-known/ucp declaring cart, checkout, fulfillment, discount, order and catalog capabilities plus three payment handlers, OpenID Connect and RFC 8414 discovery for customer accounts, and a provider-authored /agents.md and /llms.txt that
  tell AI agents which surface to use and that no agent may finalize payment without contemporaneous human approval.'
image: https://cdn.shopify.com/s/files/1/0275/4822/1505/files/MakeupByMario_Logo.png?height=628&pad_color=fff&v=1632760838&width=1200
layout: provider
mcp_servers:
- description: 'MAKEUP BY MARIO serves TWO live MCP endpoints from its own storefront host, and BOTH answer an anonymous JSON-RPC tools/list with HTTP 200 and full JSON Schema input contracts. The Shopify Storefront '
  name: Makeup by Mario MCP Server
  slug: makeup-by-mario-mcp-server
modified: '2026-08-25'
name: Makeup by Mario
nav: Providers
network: true
overview: 'Makeup by Mario publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Cosmetics, Consumer Packaged Goods, and E-Commerce.


  Makeup by Mario''s developer surface includes documentation, authentication, FAQ, support, engineering blog, and 28 more developer resources.'
plans:
- name: Makeup By Mario Plans Pricing
  plan_count: 0
  slug: makeup-by-mario-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Makeup By Mario Rate Limits
  slug: makeup-by-mario-rate-limits
scopes:
- name: Makeup By Mario Scopes
  scope_count: 0
  slug: makeup-by-mario-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    agentic_access: first-party
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Makeup By Mario Authentication
  slug: makeup-by-mario-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Makeup By Mario Domain Security
  slug: makeup-by-mario-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makeup-by-mario
tags:
- Company
- Beauty
- Cosmetics
- Consumer Packaged Goods
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
- GraphQL
- MCP
- Universal Commerce Protocol
website: https://www.makeupbymario.com/
---
