---
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
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Universal Commerce Protocol (UCP) shopping service, exposed over MCP at https://offgridstores.com/api/ucp/mcp. The server identifies itself as "universal-commerce" 0.1.0 speaking MCP protocol 2025-06-
  name: Off Grid Stores UCP Commerce MCP Server
  slug: offgridstores-ucp-commerce-mcp
- description: Shopify Storefront MCP server at https://offgridstores.com/api/mcp, identifying itself as "storefront-renderer" 0.1.0 on MCP protocol 2025-06-18. Five tools that answer anonymously end to end — search
  name: Off Grid Stores Storefront MCP Server
  slug: offgridstores-storefront-mcp
- description: 'Shopify Storefront GraphQL API served on the company''s own host at https://offgridstores.com/api/2025-10/graphql.json. Full introspection answers anonymously: 422 types, 34 query root fields and 41 mu'
  name: Off Grid Stores Storefront GraphQL API
  slug: offgridstores-storefront-graphql
- description: 'Anonymous read-only JSON over the storefront: /products.json and /collections.json for the catalog, /products/{handle}.json and /collections/{handle}/products.json for single resources, and /cart.js f'
  name: Off Grid Stores Storefront JSON Endpoints
  slug: offgridstores-storefront-json
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://offgridstores.com
- group: docs
  title: ''
  type: Documentation
  url: https://offgridstores.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offgridstores-llms.txt
- group: other
  title: ''
  type: AgentInstructions
  url: llms/offgridstores-agents.md
- group: company
  title: ''
  type: Blog
  url: https://offgridstores.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://offgridstores.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://offgridstores.com/pages/faqs
- group: start
  title: ''
  type: SignUp
  url: https://offgridstores.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offgridstores.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offgridstores.com/policies/privacy-policy
- group: other
  title: ''
  type: RefundPolicy
  url: https://offgridstores.com/policies/refund-policy
- group: other
  title: ''
  type: ShippingPolicy
  url: https://offgridstores.com/policies/shipping-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/offgridstores-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/offgridstores-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/offgridstores-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/offgridstores-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/offgridstores-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/offgridstores-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/offgridstores-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/offgridstores-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/offgridstores-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/offgridstores-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/offgridstores-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/offgridstores-tool-crosswalk.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/offgridstores-mcp.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/offgridstores-storefront.graphql
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offgridstores-domain-security.yml
created: '2026-08-26'
description: 'Off Grid Stores is a US direct-to-consumer retailer of off-grid solar equipment — solar generators and kits, portable and rigid panels, LiFePO4 battery banks, inverters, charge controllers and composting toilets — operating from offgridstores.com. It publishes no traditional developer program, but its Shopify-hosted storefront exposes a substantial, entirely anonymous machine surface on its own domain: an agents.md/llms.txt agent contract (indexed by a dedicated /sitemap_agentic_discovery.xml), a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp declaring UCP 2026-04-08, two live Model Context Protocol servers (a 13-tool UCP commerce server and a 5-tool Storefront MCP server), an anonymously introspectable Storefront GraphQL API of 422 types, and the storefront JSON endpoints for products, collections and cart.'
image: https://offgridstores.com/cdn/shop/files/Off_Grid_Stores_Logo_1204x630.png
layout: provider
mcp_servers:
- description: 'Off Grid Stores serves TWO live, remote Model Context Protocol servers from its own domain, both advertised in its /llms.txt and /agents.md. They are Shopify platform servers bound to this merchant''s '
  name: Off Grid Stores - All Things Off-Grid Solar MCP Server
  slug: off-grid-stores-all-things-off-grid-solar-mcp-server
modified: '2026-08-26'
name: Off Grid Stores - All Things Off-Grid Solar
nav: Providers
network: true
overview: 'Off Grid Stores - All Things Off-Grid Solar publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and off-grid solar.


  Off Grid Stores - All Things Off-Grid Solar''s developer surface includes documentation, engineering blog, support, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Offgridstores Plans Pricing
  plan_count: 0
  slug: offgridstores-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Offgridstores Rate Limits
  slug: offgridstores-rate-limits
scopes:
- name: Offgridstores Scopes
  scope_count: 0
  slug: offgridstores-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 37.2
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 38.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Offgridstores Authentication
  slug: offgridstores-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Offgridstores Domain Security
  slug: offgridstores-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: offgridstores
tags:
- Company
- Commerce
- E-Commerce
- Retail
- off-grid solar
- Renewable Energy
- Backup Power
- solar generators
- LiFePO4 batteries
- Inverters
- homesteading
- Agentic Commerce
- MCP
- GraphQL
- UCP
website: https://offgridstores.com
---
