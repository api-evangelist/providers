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
    idempotency: derived
    mcp_server: platform
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The agent-facing commerce surface for the Agilitas store, implementing the Universal Commerce Protocol (dev.ucp.shopping) over the Model Context Protocol. Thirteen tools cover catalog search and looku
  name: Agilitas Commerce MCP API
  slug: agilitassports-commerce-mcp-api
- description: The read-only storefront JSON endpoints Agilitas names for agents in its own /llms.txt and /agents.md — product JSON at /products/{handle}.json, collection product listings at /collections/{handle}/pr
  name: Agilitas Storefront JSON API
  slug: agilitassports-storefront-json-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://agilitas.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agilitas.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://agilitas.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://agilitas.com/blogs/press-and-media
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agilitas.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agilitas.com/policies/privacy-policy
- group: agent
  href: https://artifacts.apis.io/agilitassports/mcp/agilitassports-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agilitassports-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agilitassports/llms/agilitassports-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agilitassports-llms.txt
- group: agent
  href: https://artifacts.apis.io/agilitassports/well-known/agilitassports-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agilitassports-well-known.yml
- group: auth
  href: https://artifacts.apis.io/agilitassports/authentication/agilitassports-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agilitassports-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agilitassports/scopes/agilitassports-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/agilitassports-scopes.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/conventions/agilitassports-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agilitassports-conventions.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/conventions/agilitassports-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agilitassports-conventions.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/errors/agilitassports-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agilitassports-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/agilitassports/rate-limits/agilitassports-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agilitassports-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agilitassports/plans/agilitassports-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agilitassports-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/lifecycle/agilitassports-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agilitassports-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/conformance/agilitassports-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agilitassports-conformance.yml
- group: design
  href: https://artifacts.apis.io/agilitassports/data-model/agilitassports-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agilitassports-data-model.yml
- group: agent
  href: https://artifacts.apis.io/agilitassports/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/agilitassports/packages/agilitassports-packages.yml
  title: ''
  type: Packages
  url: packages/agilitassports-packages.yml
- group: auth
  href: https://artifacts.apis.io/agilitassports/security/agilitassports-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agilitassports-domain-security.yml
created: '2026-09-12'
description: 'Agilitas Sports Private Limited is a Bengaluru-based sports and athleisure company founded in February 2023 by former Puma India leaders Abhishek Ganguly, Atul Bajaj and Amit Prabhu, built as a vertically integrated manufacture-brand-retail ecosystem rather than a software business. It acquired Mochiko Shoes, one of India''s largest sports footwear manufacturers, holds the exclusive India licence for Lotto, and runs the one8 brand with Virat Kohli. It publishes no developer program and no OpenAPI, but its Shopify storefront at agilitas.com serves a real agent-facing commerce surface: /llms.txt and /agents.md, a /.well-known/ucp Universal Commerce Protocol merchant profile (UCP 2026-08-25), and two live unauthenticated Model Context Protocol endpoints — a thirteen-tool catalog/cart/checkout/order server and a one-tool policy-and-FAQ server.'
image: https://agilitas.com/cdn/shop/files/512.jpg?v=1782028242
layout: provider
mcp_servers:
- description: Remote MCP server at agilitas.com.
  name: Agilitas Model Context Protocol servers
  slug: agilitas-model-context-protocol-servers
modified: '2026-09-12'
name: Agilitas Sports
nav: Providers
network: true
overview: 'Agilitas Sports is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Sportswear.


  Agilitas Sports'' developer surface includes documentation, support, engineering blog, authentication, and 18 more developer resources.'
plans:
- name: Agilitassports Plans Pricing
  plan_count: 0
  slug: agilitassports-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Agilitassports Rate Limits
  slug: agilitassports-rate-limits
scopes:
- name: Agilitassports Scopes
  scope_count: 4
  slug: agilitassports-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 56.7
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 23.8
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agilitassports/agilitassports-2026-10-11T093131.png
security:
- kind: authentication
  name: Agilitassports Authentication
  slug: agilitassports-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Agilitassports Domain Security
  slug: agilitassports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: agilitassports-browse-the-catalog
  slug: agilitassports-browse-the-catalog
- name: agilitassports-build-an-order
  slug: agilitassports-build-an-order
- name: agilitassports-complete-purchase-safely
  slug: agilitassports-complete-purchase-safely
slug: agilitassports
tags:
- Company
- Commerce
- E-Commerce
- Retail
- Sportswear
- Footwear
- Athleisure
- Manufacturing
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- India
website: https://agilitas.com/
---
