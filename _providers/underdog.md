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
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.9
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: 'The Universal Commerce Protocol (UCP) shopping service Underdog serves from its own domain. A remote MCP endpoint that answers tools/list anonymously with 13 tools covering catalog search and lookup, '
  name: Underdog UCP Commerce MCP API
  slug: underdog-ucp-commerce
- description: 'The Shopify Storefront GraphQL API as served on underdog.shop. It answers introspection anonymously and exposes 424 types, 35 root query fields (products, collections, search, predictiveSearch, cart, '
  name: Underdog Storefront GraphQL API
  slug: underdog-storefront-graphql
- description: 'A second remote MCP endpoint on underdog.shop that answers tools/list anonymously with a single natural-language tool, search_shop_policies_and_faqs, for questions about the store''s return, shipping, '
  name: Underdog Storefront Policy MCP API
  slug: underdog-storefront-mcp
- description: 'Read-only, unauthenticated JSON representations of the Underdog catalogue published by the Shopify storefront: /products.json, /products/{handle}.json, /collections/{handle}/products.json and /search?'
  name: Underdog Storefront JSON Endpoints
  slug: underdog-storefront-json
artifact_total: 12
common:
- group: company
  title: ''
  type: Blog
  url: https://underdog.shop/pages/blog
- group: auth
  href: https://artifacts.apis.io/underdog/security/underdog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/underdog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://underdog.shop/
- group: docs
  title: ''
  type: Documentation
  url: https://underdog.shop/agents.md
- group: agent
  href: https://artifacts.apis.io/underdog/llms/underdog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/underdog-llms.txt
- group: agent
  href: https://artifacts.apis.io/underdog/well-known/underdog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/underdog-well-known.yml
- group: agent
  href: https://artifacts.apis.io/underdog/mcp/underdog-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/underdog-mcp.yml
- group: build
  href: https://artifacts.apis.io/underdog/mcp/underdog-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/underdog-tool-crosswalk.yml
- group: docs
  href: https://artifacts.apis.io/underdog/graphql/underdog-storefront.graphql
  title: ''
  type: GraphQL
  url: graphql/underdog-storefront.graphql
- group: auth
  href: https://artifacts.apis.io/underdog/authentication/underdog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/underdog-authentication.yml
- group: auth
  href: https://artifacts.apis.io/underdog/scopes/underdog-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/underdog-scopes.yml
- group: design
  href: https://artifacts.apis.io/underdog/conformance/underdog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/underdog-conformance.yml
- group: design
  href: https://artifacts.apis.io/underdog/conventions/underdog-conventions.yml
  title: ''
  type: Conventions
  url: conventions/underdog-conventions.yml
- group: design
  href: https://artifacts.apis.io/underdog/conventions/underdog-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/underdog-conventions.yml
- group: design
  href: https://artifacts.apis.io/underdog/errors/underdog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/underdog-problem-types.yml
- group: design
  href: https://artifacts.apis.io/underdog/lifecycle/underdog-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/underdog-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/underdog/data-model/underdog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/underdog-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/underdog/plans/underdog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/underdog-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/underdog/rate-limits/underdog-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/underdog-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/underdog/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/underdog-shop
- group: operate
  title: ''
  type: Support
  url: https://underdog.shop/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://underdog.shop/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://underdog.shop/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://account.underdog.shop/
created: '2026-08-17'
description: 'Underdog (legal entity Older is Better, RCS Nantes 918 609 629) is a French direct-to-consumer retailer of professionally refurbished large home appliances and televisions — washing machines, fridges, dishwashers, tumble dryers, ovens, cookers, freezers, wine cabinets, TVs and Thermomix — reconditioned in France and sold at up to 50% below new with a two-year warranty, delivery, installation and old-appliance takeback. It is a circular-economy / climate-tech company backed by Serena. Underdog has no developer programme and publishes no OpenAPI, but its storefront runs on Shopify and it exposes a genuine, live agent-commerce surface on its own domain: an /llms.txt and /agents.md agent instruction document, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, two anonymously-listable remote MCP endpoints (a 13-tool UCP commerce server and a 1-tool storefront policy server), an introspectable Shopify Storefront GraphQL API, RFC 8414 / RFC 9728 OAuth metadata,
  and read-only product and collection JSON endpoints.'
image: https://underdog.shop/cdn/shop/files/UND-logo-Noir_1_3878927d-05f3-4209-b1e5-6113f92e6567.png?v=1762513808
layout: provider
mcp_servers:
- description: Two remote MCP endpoints served from Underdog's own storefront host (Shopify platform). The UCP commerce server exposes 13 Universal Commerce Protocol shopping tools; the storefront server exposes one
  name: Underdog MCP servers
  slug: underdog-mcp-servers
modified: '2026-10-06'
name: Underdog
nav: Providers
network: true
overview: 'Underdog is listed with 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Circular Economy, Refurbished Electronics, and Home Appliances.


  Underdog''s developer surface includes engineering blog, documentation, authentication, support, and 21 more developer resources.'
plans:
- name: Underdog Plans Pricing
  plan_count: 0
  slug: underdog-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Underdog Rate Limits
  slug: underdog-rate-limits
scopes:
- name: Underdog Scopes
  scope_count: 4
  slug: underdog-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 9.3
    developer_ergonomics: 30.4
    discoverability: 71.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 26.5
  provenance:
    conformance: first-party
    mcp: platform-generated
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/underdog/underdog-2026-09-02T164849.png
security:
- kind: authentication
  name: Underdog Authentication
  slug: underdog-authentication
  summary_line: none/oauth2/openIdConnect/http · 5 schemes
- kind: domain-security
  name: Underdog Domain Security
  slug: underdog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 2
skills:
- name: underdog-browse-catalog
  slug: underdog-browse-catalog
- name: underdog-cart-and-checkout
  slug: underdog-cart-and-checkout
slug: underdog
tags:
- Company
- Climate Tech
- Circular Economy
- Refurbished Electronics
- Home Appliances
- Retail
- E-Commerce
- Shopify
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- GraphQL
- France
website: https://underdog.shop/
---
