---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-09-24'
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
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/security/poppi-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/mcp/poppi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/poppi-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/llms/poppi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/poppi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/well-known/poppi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/poppi-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/authentication/poppi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/poppi-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/scopes/poppi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/poppi-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/conventions/poppi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/poppi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/conventions/poppi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/poppi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/conformance/poppi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/poppi-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/errors/poppi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/poppi-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/lifecycle/poppi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/poppi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/data-model/poppi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/poppi-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/graphql/poppi-graphql.yml
  title: ''
  type: GraphQL
  url: graphql/poppi-graphql.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/mcp/poppi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/poppi-tool-crosswalk.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/rate-limits/poppi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/poppi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/plans/poppi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/poppi-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/poppi/refs/heads/main/skills/_index.yml
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
random_paper: 2
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
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.5
    developer_ergonomics: 33.3
    discoverability: 75.9
    operational_transparency: 21.1
  previous_composite: 35.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
