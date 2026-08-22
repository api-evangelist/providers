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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.0
  scored_at: '2026-08-19'
api_count: 8
apis:
- description: The Bookings API from GetYourGuide — 2 operation(s) for bookings.
  name: GetYourGuide Bookings API
  slug: getyourguide-bookings-api
- description: The Carts API from GetYourGuide — 2 operation(s) for carts.
  name: GetYourGuide Carts API
  slug: getyourguide-carts-api
- description: The Categories API from GetYourGuide — 2 operation(s) for categories.
  name: GetYourGuide Categories API
  slug: getyourguide-categories-api
- description: The Configuration API from GetYourGuide — 2 operation(s) for configuration.
  name: GetYourGuide Configuration API
  slug: getyourguide-configuration-api
- description: The Options API from GetYourGuide — 1 operation(s) for options.
  name: GetYourGuide Options API
  slug: getyourguide-options-api
- description: The Reviews API from GetYourGuide — 1 operation(s) for reviews.
  name: GetYourGuide Reviews API
  slug: getyourguide-reviews-api
- description: The Suppliers API from GetYourGuide — 1 operation(s) for suppliers.
  name: GetYourGuide Suppliers API
  slug: getyourguide-suppliers-api
- description: The Tours API from GetYourGuide — 5 operation(s) for tours.
  name: GetYourGuide Tours API
  slug: getyourguide-tours-api
arazzos:
- description: Search the GetYourGuide marketplace, pick a tour option, check availability, then create and confirm a booking via the two-step cart flow.
  name: Search a tour and create a booking
  slug: getyourguide-search-and-book
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Partner Api Bookings API
  slug: open-getyourguide-bookings-api
- collection_type: open
  name: Partner Api Bookings Carts API
  slug: open-getyourguide-carts-api
- collection_type: open
  name: Partner Api Bookings Categories API
  slug: open-getyourguide-categories-api
- collection_type: open
  name: Partner Api Bookings Configuration API
  slug: open-getyourguide-configuration-api
- collection_type: open
  name: Partner Api Bookings Options API
  slug: open-getyourguide-options-api
- collection_type: open
  name: Partner Api Bookings Suppliers API
  slug: open-getyourguide-suppliers-api
- collection_type: open
  name: Partner Api Bookings Tours API
  slug: open-getyourguide-tours-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/getyourguide-partner-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://code.getyourguide.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/getyourguide/partner-api-spec
- group: docs
  title: ''
  type: APIReference
  url: https://code.getyourguide.com/partner-api-spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/getyourguide/partner-api-spec/wiki/Getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getyourguide
- group: other
  title: ''
  type: OpenSource
  url: https://code.getyourguide.com/
- group: company
  title: ''
  type: Blog
  url: https://www.getyourguide.careers/category/tech-engineering
- group: operate
  title: ''
  type: Support
  url: https://supply.getyourguide.support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getyourguide.com/terms_of_use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getyourguide.com/privacy_policy/
- group: auth
  title: ''
  type: Security
  url: https://www.getyourguide.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/getyourguide-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/getyourguide-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/getyourguide-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/getyourguide-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/getyourguide-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/getyourguide-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/getyourguide-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/getyourguide-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/getyourguide-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/getyourguide-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/getyourguide-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/getyourguide-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/getyourguide-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/getyourguide-search-and-book.yml
created: '2026-07-17'
description: GetYourGuide is a Berlin-based online travel marketplace for booking tours, activities, attraction tickets, and experiences in destinations around the world. Founded in 2009, the company connects travelers with local activity suppliers and operators, and exposes a public Partner API that gives affiliates, agencies, and technology partners programmatic access to the GetYourGuide marketplace catalog — searching tours and activities, retrieving categories, options, availability, price breakdowns, supplier details, and reviews, and creating shopping carts and bookings. The RESTful Partner API uses JSON, is secured over TLS with an API access token (X-ACCESS-TOKEN header), and publishes its OpenAPI specification as open source on GitHub. GetYourGuide is backed by Battery Ventures and SoftBank Vision Fund.
image: https://cdn.getyourguide.com/tf/assets/static/logos/gyg-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: getyourguide-mcp.yml
  slug: getyourguide-mcpyml
modified: '2026-07-19'
name: GetYourGuide
nav: Providers
network: true
overview: 'GetYourGuide publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Carts API, Categories API, and 5 more. Tagged areas include Company, Travel, Tourism, Tours and Activities, and Marketplace.


  GetYourGuide''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 20 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 43.8
  delta: 0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 53.7
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 13.2
  previous_composite: 43.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/getyourguide/refs/heads/main/screenshots/getyourguide-2026-07-25T215748.png
security:
- kind: authentication
  name: Getyourguide Authentication
  slug: getyourguide-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Getyourguide Domain Security
  slug: getyourguide-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Getyourguide Vulnerability Disclosure
  slug: getyourguide-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: getyourguide
tags:
- Company
- Travel
- Tourism
- Tours and Activities
- Marketplace
- Booking
- Experiences
- Affiliate
- Partner API
- Ecommerce
website: https://code.getyourguide.com/
---
