---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 3
  name: Tecovas Agentic Access
  operation_count: 17
  slug: tecovas-agentic-access
  summary_line: 17 operations · 9 acting · 3 human-in-the-loop
api_count: 3
apis:
- description: Read-only JSON endpoints on the Tecovas storefront host, published in the company's own RFC 9727 api-catalog linkset and documented in its agents.md. Covers product detail by slug, collection metadata
  name: Tecovas Storefront Content API
  slug: tecovas-storefront-content-api
- description: 'The Shopify Storefront GraphQL API as deployed on the Tecovas checkout host. Anonymous introspection succeeds (424 types, 35 query fields, 41 mutations), covering products, collections, carts, blogs, '
  name: Tecovas Storefront GraphQL API
  slug: tecovas-storefront-graphql-api
- description: Tecovas implements the Universal Commerce Protocol 2026-04-08 on its Shopify checkout host, exposing an MCP endpoint whose tools/list returns 13 tools with full JSON Schema inputs for catalog search a
  name: Tecovas Agentic Commerce (UCP/MCP)
  slug: tecovas-ucp-agentic-commerce
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.tecovas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tecovas.com/agents.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.tecovas.com/.well-known/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tecovas.com/agents.md#typical-agent-flow
- group: operate
  title: ''
  type: Support
  url: https://www.tecovas.com/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.tecovas.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tecovas.com/p/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tecovas.com/p/terms-and-conditions
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tecovas-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tecovas-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/tecovas-api-catalog.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/tecovas-robots.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tecovas-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tecovas-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/tecovas-storefront.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/tecovas-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tecovas-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tecovas-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tecovas-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tecovas-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecovas-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tecovas-agentic-access.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tecovas-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tecovas-problem-types.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/tecovas_stock/
created: '2026-08-05'
description: 'Tecovas is an Austin, Texas direct-to-consumer Western wear brand selling handcrafted cowboy boots, work boots, hats, leather goods and apparel for men, women and kids, made by artisans in Leon, Mexico and sold online and through its own US retail stores. Its storefront runs on Shopify Hydrogen (React Router 7) with Sanity content and Algolia search, and it publishes an unusually complete agent-facing surface for a retailer: an llms.txt, an agents.md, an RFC 9727 api-catalog linkset of read-only JSON endpoints, a Cloudflare-style agent-skills discovery index, an anonymously introspectable Shopify Storefront GraphQL API, and a Universal Commerce Protocol (UCP) MCP endpoint on its Shopify checkout host for agent-driven cart and checkout.'
image: https://cdn.sanity.io/images/v8kybopt/production/073bf9cd1134041e2c334a569e22504347e336eb-8108x5289.jpg?auto=format&fit=max&w=1200
layout: provider
mcp_servers:
- description: ''
  name: Tecovas MCP Server
  slug: tecovas-mcp-server
modified: '2026-08-05'
name: Tecovas
nav: Providers
network: true
overview: 'Tecovas publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Footwear.


  Tecovas'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 20 more developer resources.'
random_paper: 1
scopes:
- name: Tecovas Scopes
  scope_count: 4
  slug: tecovas-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Tecovas Authentication
  slug: tecovas-authentication
  summary_line: none/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Tecovas Domain Security
  slug: tecovas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tecovas
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Footwear
- Direct to Consumer
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- Product Catalog
website: https://www.tecovas.com/
---
