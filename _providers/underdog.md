---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 32.1
  scored_at: '2026-09-04'
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
artifact_total: 6
common:
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/underdog-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/underdog-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/underdog-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/underdog-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/underdog-storefront.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/underdog-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/underdog-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/underdog-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/underdog-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/underdog-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/underdog-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/underdog-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/underdog-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/underdog-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/underdog-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/underdog-rate-limits.yml
- group: agent
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
- description: ''
  name: Underdog MCP Server
  slug: underdog-mcp-server
modified: '2026-08-17'
name: Underdog
nav: Providers
network: true
overview: 'Underdog publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate Tech, Circular Economy, Refurbished Electronics, and Home Appliances.


  Underdog''s developer surface includes documentation, authentication, support, and 22 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 31.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/underdog/refs/heads/main/screenshots/underdog-2026-09-02T164849.png
security:
- kind: domain-security
  name: Underdog Domain Security
  slug: underdog-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
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
