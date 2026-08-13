---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Headout Agentic Access
  operation_count: 9
  slug: headout-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 6
apis:
- description: The Booking API from HeadOut — 2 operation(s) for booking.
  name: HeadOut Booking API
  slug: headout-booking-api
- description: The Categories API from HeadOut — 1 operation(s) for categories.
  name: HeadOut Categories API
  slug: headout-categories-api
- description: The Collections API from HeadOut — 1 operation(s) for collections.
  name: HeadOut Collections API
  slug: headout-collections-api
- description: The Inventory API from HeadOut — 1 operation(s) for inventory.
  name: HeadOut Inventory API
  slug: headout-inventory-api
- description: The Products API from HeadOut — 1 operation(s) for products.
  name: HeadOut Products API
  slug: headout-products-api
- description: The Subcategories API from HeadOut — 1 operation(s) for subcategories.
  name: HeadOut Subcategories API
  slug: headout-subcategories-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/headout-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/headout-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://headout.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/headout/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/headout/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/headout/api-docs/tree/master/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/headout/api-docs/wiki/Integration-flow-for-Partners
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/headout
- group: company
  title: ''
  type: Blog
  url: https://www.headout.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.headout.com/help/
- group: start
  title: ''
  type: SignUp
  url: https://partner.headout.com/affiliate/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.headout.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.headout.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/headout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/headout-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/headout-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/headout-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/headout-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/headout-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/headout-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/headout-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/headout-partner-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/headout-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/headout-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/headout-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/headout-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Headout is a global experiences marketplace that curates and sells tickets to tours, attractions, events, shows and activities across major cities worldwide. For developers, Headout operates a public Partner API (github.com/headout/api-docs) that lets affiliates and resellers browse the catalog (products, categories, collections and subcategories by city and language), pull live inventory and per-person/per-group pricing for a variant, and place bookings through a two-step create-then-capture flow. The API is versioned by URI path (v1 and v2 under /api/public/), authenticates with a Headout-Auth API key (pk_ production / tk_ sandbox), paginates with offset/limit, and returns a structured error envelope. A registrable seatmap iframe component is offered for seat selection. Headout is backed by 500 Global and Version One Ventures.
image: https://cdn-imgix.headout.com/static-pages/logo.png
layout: provider
mcp_servers:
- description: ''
  name: headout-mcp.yml
  slug: headout-mcpyml
modified: '2026-07-19'
name: HeadOut
nav: Providers
network: true
overview: 'HeadOut publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Booking API, Categories API, Collections API, and 3 more. Tagged areas include Travel, Tours and Activities, Experiences, Attractions, and Ticketing.


  HeadOut''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 14.9
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/headout/refs/heads/main/screenshots/headout-2026-07-25T220821.png
security:
- kind: authentication
  name: Headout Authentication
  slug: headout-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Headout Domain Security
  slug: headout-domain-security
  summary_line: TLSv1.3 · DMARC
slug: headout
tags:
- Travel
- Tours and Activities
- Experiences
- Attractions
- Ticketing
- Bookings
- Marketplace
- Partner API
- Affiliate
- Events
website: https://headout.com
---
