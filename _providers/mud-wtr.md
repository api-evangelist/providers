---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: 'Universal Commerce Protocol (UCP) shopping service, exposed over MCP at https://mudwtr.com/api/ucp/mcp. Server identifies itself as "universal-commerce" 0.1.0 speaking MCP protocol 2025-06-18 and UCP '
  name: MUD\WTR UCP Commerce MCP Server
  slug: mud-wtr-ucp-commerce-mcp
- description: 'Shopify Storefront MCP server at https://mudwtr.com/api/mcp, identifying itself as "storefront-renderer" 0.1.0 on MCP protocol 2025-06-18. Five anonymous tools: search_catalog, get_product_details, ge'
  name: MUD\WTR Storefront MCP Server
  slug: mud-wtr-storefront-mcp
- description: 'Shopify Storefront GraphQL API served on the company''s own host at https://mudwtr.com/api/2025-10/graphql.json. Full introspection answers anonymously: 414 types, 34 query root fields and 41 mutations'
  name: MUD\WTR Storefront GraphQL API
  slug: mud-wtr-storefront-graphql
- description: 'Anonymous read-only JSON over the storefront: /products.json and /collections.json for the catalog, /products/{handle}.json and /collections/{handle}/products.json for single resources, and /cart.js f'
  name: MUD\WTR Storefront JSON Endpoints
  slug: mud-wtr-storefront-json
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mud-wtr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mudwtr.com
- group: company
  title: ''
  type: Blog
  url: https://mudwtr.com/blogs/trends-with-benefits
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mudwtr.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mudwtr.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://mudwtr.com/policies/refund-policy
- group: start
  title: ''
  type: SignUp
  url: https://mudwtr.com/account/login
- group: other
  title: ''
  type: Wholesale
  url: https://mudwtr.com/pages/wholesale
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mud-wtr-llms.txt
- group: other
  title: ''
  type: AgentInstructions
  url: llms/mud-wtr-agents.md
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mud-wtr-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mud-wtr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mud-wtr-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mud-wtr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mud-wtr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mud-wtr-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mud-wtr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mud-wtr-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mud-wtr-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mud-wtr-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mud-wtr-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mud-wtr-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mud-wtr-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/mud-wtr-storefront.graphql
created: '2026-08-26'
description: 'MUD\WTR is a certified-organic coffee alternative built on adaptogenic mushrooms and botanicals, sold direct-to-consumer from mudwtr.com. It publishes no traditional developer program, but its Shopify-hosted storefront exposes a substantial, entirely anonymous machine surface on its own domain: an agents.md/llms.txt agent contract, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, two live Model Context Protocol servers (a 13-tool UCP commerce server and a 5-tool Storefront MCP server), an anonymously introspectable Storefront GraphQL API, and the storefront JSON endpoints for products, collections and cart.'
image: https://mudwtr.com/cdn/shop/files/mud-tin_1200x1200.jpg?v=1614300033
layout: provider
mcp_servers:
- description: MUD\WTR serves TWO live, remote Model Context Protocol servers from its own domain, both advertised in its robots.txt, /agents.md and /llms.txt. They are Shopify platform servers bound to this merchan
  name: Mud\Wtr MCP Server
  slug: mudwtr-mcp-server
modified: '2026-08-26'
name: Mud\Wtr
nav: Providers
network: true
overview: 'Mud\Wtr publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Consumer Goods.


  Mud\Wtr''s developer surface includes engineering blog, signup flow, authentication, and 22 more developer resources.'
plans:
- name: Mud Wtr Plans Pricing
  plan_count: 0
  slug: mud-wtr-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Mud Wtr Rate Limits
  slug: mud-wtr-rate-limits
scopes:
- name: Mud Wtr Scopes
  scope_count: 0
  slug: mud-wtr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 16.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 29.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mud-wtr/refs/heads/main/screenshots/mud-wtr-2026-09-02T150657.png
security:
- kind: authentication
  name: Mud Wtr Authentication
  slug: mud-wtr-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Mud Wtr Domain Security
  slug: mud-wtr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mud-wtr
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Consumer Goods
- Food and Beverage
- Shopify
- Agentic Commerce
- MCP
- GraphQL
- UCP
website: https://mudwtr.com
---
