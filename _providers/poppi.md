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
  band: agent-native
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'The agent-facing commerce surface for the poppi online store. An anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) shopping service, exposing catalog search '
  name: Poppi Agentic Commerce (UCP / MCP)
  slug: poppi-agentic-commerce
- description: The Shopify Storefront GraphQL API as deployed on poppi's own domain — 34 query fields, 41 mutations and 420 types covering products, collections, search, carts, content and customer accounts. Introsp
  name: Poppi Storefront GraphQL API
  slug: poppi-storefront-graphql
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/poppi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drinkpoppi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://drinkpoppi.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/poppi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/poppi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/poppi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/poppi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/poppi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/poppi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/poppi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/poppi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/poppi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/poppi-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/poppi-data-model.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/poppi-graphql.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/poppi-tool-crosswalk.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/poppi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/poppi-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://drinkpoppi.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://drinkpoppi.com/pages/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drinkpoppi.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drinkpoppi.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://drinkpoppi.com/account/login
created: '2026-08-26'
description: 'Poppi is an American prebiotic soda brand founded in Austin, Texas by Stephen and Allison Ellsworth, originally as Mother Beverage, rebranded to poppi in 2020 after a Shark Tank investment and acquired by PepsiCo in May 2025. Poppi sells direct to consumers from drinkpoppi.com, a Shopify storefront, and that storefront is where its machine-readable surface lives: poppi publishes agent instructions at /agents.md and /llms.txt, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an anonymous remote MCP endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools with full JSON Schema input contracts. Poppi is not a software vendor and ships no developer program, SDKs or OpenAPI — its API surface is the Shopify-native agentic-commerce stack served on and scoped to its own domain.'
image: https://drinkpoppi.com/cdn/shop/files/1680_x_750_FLAVOR_FEATURE.jpg
layout: provider
mcp_servers:
- description: ''
  name: poppi UCP shopping (MCP)
  slug: poppi-ucp-shopping-mcp
modified: '2026-08-26'
name: Poppi
nav: Providers
network: true
overview: 'Poppi publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Beverages, Food and Beverage, and E-Commerce.


  Poppi''s developer surface includes documentation, authentication, engineering blog, support, and 20 more developer resources.'
plans:
- name: Poppi Plans Pricing
  plan_count: 0
  slug: poppi-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Poppi Rate Limits
  slug: poppi-rate-limits
scopes:
- name: Poppi Scopes
  scope_count: 0
  slug: poppi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/screenshots/poppi-2026-09-02T151740.png
security:
- kind: authentication
  name: Poppi Authentication
  slug: poppi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Poppi Domain Security
  slug: poppi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: poppi
tags:
- Company
- Consumer Packaged Goods
- Beverages
- Food and Beverage
- E-Commerce
- Direct to Consumer
- Retail
- Agentic Commerce
- Shopify
- MCP
website: https://drinkpoppi.com/
---
