---
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The store's Universal Commerce Protocol service, exposed over MCP at /api/ucp/mcp. An anonymous tools/list returns thirteen tools covering catalog search and lookup, product detail, cart create / read
  name: Ministry of Supply Agentic Commerce API (UCP / MCP)
  slug: ministry-of-supply-agentic-commerce-api-ucp-mcp
- description: Read-only, unauthenticated storefront JSON the store's own agents.md points agents at — /products.json, /collections.json, /products/{handle}.json, /collections/{handle}/products.json and /search. Sho
  name: Ministry of Supply Storefront JSON
  slug: ministry-of-supply-storefront-json
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ministry-of-supply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ministryofsupply.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ministryofsupply.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ministry-of-supply-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ministry-of-supply-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ministry-of-supply-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ministry-of-supply-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ministry-of-supply-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ministry-of-supply-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ministry-of-supply-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ministry-of-supply-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ministry-of-supply-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ministry-of-supply-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ministry-of-supply-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ministry-of-supply-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ministry-of-supply-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/ministry-of-supply-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.ministryofsupply.com/pages/service
- group: company
  title: ''
  type: Blog
  url: https://www.ministryofsupply.com/blogs/news
- group: start
  title: ''
  type: Login
  url: https://www.ministryofsupply.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ministryofsupply.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ministryofsupply.com/policies/privacy-policy
created: '2026-08-25'
description: 'Ministry of Supply is a Boston-based performance apparel company founded in 2011 out of MIT, engineering technical dress shirts, pants, suits, knitwear and outerwear for work, travel and commuting using temperature-regulating, wrinkle-resistant and stretch-recovery fabrics. It sells direct to consumer from a Shopify storefront at ministryofsupply.com. Its API surface is not a developer program but an agentic commerce surface: the store publishes an agents.md / llms.txt instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a live, anonymously-callable Model Context Protocol endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools with full JSON Schema inputs, plus Shopify customer-account OpenID Connect discovery documents. Checkout requires contemporaneous human approval; complete_checkout requires an idempotency key.'
image: https://www.ministryofsupply.com/cdn/shop/files/Ministry_of_Supply_-_Stacked_-_Square_-_Black.jpg?v=1728528819
layout: provider
mcp_servers:
- description: ''
  name: Ministry of Supply MCP Server
  slug: ministry-of-supply-mcp-server
modified: '2026-08-25'
name: Ministry of Supply
nav: Providers
network: true
overview: 'Ministry of Supply publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Apparel, Retail, E-Commerce, and Direct to Consumer.


  Ministry of Supply''s developer surface includes documentation, authentication, support, engineering blog, and 19 more developer resources.'
plans:
- name: Ministry Of Supply Plans Pricing
  plan_count: 0
  slug: ministry-of-supply-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Ministry Of Supply Rate Limits
  slug: ministry-of-supply-rate-limits
scopes:
- name: Ministry Of Supply Scopes
  scope_count: 4
  slug: ministry-of-supply-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Ministry Of Supply Authentication
  slug: ministry-of-supply-authentication
  summary_line: none/openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Ministry Of Supply Domain Security
  slug: ministry-of-supply-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ministry-of-supply
tags:
- Company
- Apparel
- Retail
- E-Commerce
- Direct to Consumer
- Agentic Commerce
- MCP
- Universal Commerce Protocol
- Shopify
- Manufacturing
website: https://www.ministryofsupply.com/
---
