---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-09-12'
api_count: 2
apis:
- description: The agent-facing commerce surface for the Agilitas store, implementing the Universal Commerce Protocol (dev.ucp.shopping) over the Model Context Protocol. Thirteen tools cover catalog search and looku
  name: Agilitas Commerce MCP API
  slug: agilitassports-commerce-mcp-api
- description: The read-only storefront JSON endpoints Agilitas names for agents in its own /llms.txt and /agents.md — product JSON at /products/{handle}.json, collection product listings at /collections/{handle}/pr
  name: Agilitas Storefront JSON API
  slug: agilitassports-storefront-json-api
artifact_total: 8
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
  title: ''
  type: MCPServer
  url: mcp/agilitassports-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agilitassports-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agilitassports-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agilitassports-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agilitassports-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agilitassports-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/agilitassports-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agilitassports-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agilitassports-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agilitassports-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agilitassports-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agilitassports-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agilitassports-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/agilitassports-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agilitassports-domain-security.yml
created: '2026-09-12'
description: 'Agilitas Sports Private Limited is a Bengaluru-based sports and athleisure company founded in February 2023 by former Puma India leaders Abhishek Ganguly, Atul Bajaj and Amit Prabhu, built as a vertically integrated manufacture-brand-retail ecosystem rather than a software business. It acquired Mochiko Shoes, one of India''s largest sports footwear manufacturers, holds the exclusive India licence for Lotto, and runs the one8 brand with Virat Kohli. It publishes no developer program and no OpenAPI, but its Shopify storefront at agilitas.com serves a real agent-facing commerce surface: /llms.txt and /agents.md, a /.well-known/ucp Universal Commerce Protocol merchant profile (UCP 2026-08-25), and two live unauthenticated Model Context Protocol endpoints — a thirteen-tool catalog/cart/checkout/order server and a one-tool policy-and-FAQ server.'
image: https://agilitas.com/cdn/shop/files/512.jpg?v=1782028242
layout: provider
mcp_servers:
- description: ''
  name: Agilitas Model Context Protocol servers
  slug: agilitas-model-context-protocol-servers
modified: '2026-09-12'
name: Agilitas Sports
nav: Providers
network: true
overview: 'Agilitas Sports publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, E-Commerce, Retail, and Sportswear.


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
  scope_count: 0
  slug: agilitassports-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agilitassports Authentication
  slug: agilitassports-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Agilitassports Domain Security
  slug: agilitassports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- Model Context Protocol
- Shopify
- India
website: https://agilitas.com/
---
