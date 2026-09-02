---
agent_readiness:
  band: agent-aware
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The agent-facing commerce interface for the Hero Bread online store. An MCP server at https://shop.hero.co/api/ucp/mcp implements the Universal Commerce Protocol shopping service (dev.ucp.shopping) wi
  name: Hero Bread Storefront Agent Commerce (UCP/MCP)
  slug: hero-bread-ucp-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.hero.co/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.hero.co/agents.md
- group: operate
  title: ''
  type: Support
  url: https://www.hero.co/contact
- group: company
  title: ''
  type: Blog
  url: https://www.hero.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hero.co/products
- group: start
  title: ''
  type: Login
  url: https://shop.hero.co/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hero.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hero.co/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hero-bread-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hero-bread-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hero-bread-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hero-bread-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hero-bread-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hero-bread-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hero-bread-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hero-bread-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hero-bread-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hero-bread-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hero-bread-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hero-bread-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hero-bread-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hero-bread-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/hero-bread-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hero-bread-domain-security.yml
created: '2026-08-22'
description: 'Hero Bread is an American food-technology company that makes low-net-carb, high-fiber, zero-sugar baked goods — sliced breads, tortillas, buns, rolls and bagels — sold direct-to-consumer from hero.co and through grocery and foodservice retail. It is not a developer-tools company and publishes no developer portal, OpenAPI description or API documentation. It does, however, operate a live agent-commerce surface on its own storefront subdomain: shop.hero.co serves an llms.txt and an agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an unauthenticated MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools — a Shopify platform capability exposed on the merchant''s own host against the merchant''s own catalog.'
image: https://cdn.sanity.io/images/85daklna/production/028e6f6b81bdfad5074d500c93636f8f18866203-2000x1670.webp
layout: provider
mcp_servers:
- description: ''
  name: Hero Bread MCP Server
  slug: hero-bread-mcp-server
modified: '2026-08-22'
name: Hero Bread
nav: Providers
network: true
overview: 'Hero Bread publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Retail, and E-Commerce.


  Hero Bread''s developer surface includes documentation, support, engineering blog, pricing, authentication, and 20 more developer resources.'
plans:
- name: Hero Bread Plans Pricing
  plan_count: 0
  slug: hero-bread-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Hero Bread Rate Limits
  slug: hero-bread-rate-limits
scopes:
- name: Hero Bread Scopes
  scope_count: 4
  slug: hero-bread-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Hero Bread Authentication
  slug: hero-bread-authentication
  summary_line: none/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Hero Bread Domain Security
  slug: hero-bread-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hero-bread
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Retail
- E-Commerce
- Agent Commerce
- MCP
- Universal Commerce Protocol
- Shopify
- Direct to Consumer
website: https://www.hero.co/
---
