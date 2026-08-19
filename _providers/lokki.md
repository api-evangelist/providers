---
access_model:
  confidence: high
  label: Paid · Sales-gated API keys
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The partner-facing read-only Lokki API — seven GET operations over rental providers (stores), their store items with date-range pricing and stock, and the two-level verticale / category taxonomy. Docu
  name: Lokki External API
  slug: lokki-external-api
- description: 'The main API powering the Lokki Dashboard and Online Store: 896 operations across company, order, order-event, long-term-rental (LLD), online-store, products, payment, delivery, workshop, reconditioni'
  name: Lokki Dashboard API
  slug: lokki-dashboard-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.lokki.rent/
- group: start
  title: ''
  type: Portal
  url: https://solutions.lokki.rent/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getlokki.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getlokki.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getlokki.com/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.getlokki.com/api-reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/lokki-authentication.yml
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getlokki.com/fr/
- group: company
  title: ''
  type: Blog
  url: https://solutions.lokki.rent/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LokkiApp
- group: commercial
  title: ''
  type: Pricing
  url: https://solutions.lokki.rent/en/tarifs
- group: commercial
  title: ''
  type: Plans
  url: plans/lokki-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.getlokki.com/welcome
- group: start
  title: ''
  type: Login
  url: https://app.getlokki.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solutions.lokki.rent/legals/conditions-generales-dutilisation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solutions.lokki.rent/legals/politique-de-confidentialite
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getlokki.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.getlokki.com/api-reference/stores/deprecations
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lokki-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lokki-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lokki-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lokki-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lokki-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lokki-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/lokki-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lokki-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lokki-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lokki-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/lokki-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/lokki-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: Lokki is a Grenoble, France rental-management SaaS (getlokki.com) used by 2,500+ equipment rental businesses across bikes, e-bikes, scooters, cars, ski, climbing, surf, paddle, canoe/kayak, boats, event gear, groundskeeping equipment and tooling, paired with the lokki.rent consumer rental marketplace. Lokki publishes a partner-facing read-only REST API — the Lokki External API, seven operations on https://prod.api.eu-west-3.lokki.rent covering stores (rental providers), store items with date-range pricing and stock, and the verticale/category taxonomy — documented on a Mintlify docs host at docs.getlokki.com with an OpenAPI 3.1 specification, llms.txt, an A2A agent card, a provider-authored Agent Skill and an anonymous documentation MCP server. Authentication is an environment-scoped API key in the x-api-key header (lokki_sk_test_ for staging, lokki_sk_live_ for production) issued by a Lokki representative under a partnership agreement, with scopes at domain, action and route
  level. The same production host also serves an unauthenticated NestJS Swagger document for the 896-operation internal Dashboard / Online Store API. Lokki has raised roughly €6.3M, led by blisce with Racine2 (Serena + makesense), 50 Partners Impact, FJ Labs and Silence VC.
image: https://cdn.prod.website-files.com/5e287889fb7cee1c505303f4/66d86a1b9b17225aee5db549_logo.png
layout: provider
mcp_servers:
- description: ''
  name: lokki-mcp.yml
  slug: lokki-mcpyml
modified: '2026-08-17'
name: Lokki
nav: Providers
network: true
overview: 'Lokki publishes 2 APIs on the [APIs.io](https://apis.io/) network: External API and Dashboard API. Tagged areas include Company, Climate Tech, Circular Economy, Rental, and Equipment Rental.


  Lokki''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Lokki Plans Pricing
  plan_count: 0
  slug: lokki-plans-pricing
random_paper: 91
rate_limits:
- limit_count: 1
  name: Lokki Rate Limits
  slug: lokki-rate-limits
score:
  band: developing
  composite: 48.7
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 44.2
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Lokki Authentication
  slug: lokki-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lokki Domain Security
  slug: lokki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lokki
tags:
- Company
- Climate Tech
- Circular Economy
- Rental
- Equipment Rental
- Bike Rental
- Marketplace
- Booking
- Reservations
- Inventory
- Catalog
- Pricing
- Availability
- Mobility
- Outdoor Recreation
- Point of Sale
- SaaS
- France
- MCP
- Agents
- Agent Skills
website: https://www.lokki.rent/
---
