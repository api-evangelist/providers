---
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 150
  human_in_the_loop: 2
  name: Outdoorsy Agentic Access
  operation_count: 312
  slug: outdoorsy-agentic-access
  summary_line: 312 operations · 150 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: The core Outdoorsy REST API (Trailblazer Partner API). Resource-oriented URLs, standard HTTP verbs and response codes, semantic versioning, and 283 operations across rentals, bookings, booking proposa
  name: Outdoorsy API
  slug: outdoorsy-api
- description: The Outdoorsy Search API — a read-only JSON:API-formatted search surface over rentals, campgrounds, external campgrounds, national/state parks, localities, breadcrumbs, users and vacation packages, wi
  name: Outdoorsy Search API
  slug: outdoorsy-search-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.outdoorsy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.outdoorsy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.outdoorsy.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.outdoorsy.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.outdoorsy.com/help
- group: start
  title: ''
  type: SignUp
  url: https://wheelbase.typeform.com/to/XANb4C
- group: operate
  title: ''
  type: Support
  url: https://www.outdoorsy.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.outdoorsy.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.outdoorsy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outdoorsy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outdoorsy.com/help/outdoorsy-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.outdoorsy.com/hc/en-us/articles/37423118744987-Privacy-Policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/outdoorsy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/outdoorsy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/outdoorsy-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outdoorsy-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/outdoorsy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/outdoorsy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/outdoorsy-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/outdoorsy-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/outdoorsy-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/outdoorsy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/outdoorsy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/outdoorsy-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/outdoorsy-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outdoorsy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outdoorsy-domain-security.yml
created: '2026-08-02'
description: 'Outdoorsy is an RV and campervan rental marketplace founded in 2014 and headquartered in Austin, Texas, connecting owners of recreational vehicles with travelers across North America, Europe and Australia/New Zealand. The Outdoorsy Group also operates Roamly (embedded RV insurance) and Wheelbase (RV rental fleet-management software). For developers, Outdoorsy publishes the Trailblazer Partner API at developers.outdoorsy.com — a REST platform with three integration surfaces: a fully-featured REST API for search, quoting, booking, payments and fleet management; INSTASearch embeddable JavaScript widgets; and partner deep links for attribution. Two live Swagger 2.0 contracts are published on the API hosts themselves — the core Outdoorsy API (api.outdoorsy.com/v0, 283 operations) and the Outdoorsy Search API (search.outdoorsy.com, JSON:API-formatted rental, campground, park and locality search).'
image: https://avatars.githubusercontent.com/u/9725809?v=4
layout: provider
mcp_servers:
- description: ''
  name: outdoorsy-mcp.yml
  slug: outdoorsy-mcpyml
modified: '2026-08-02'
name: Outdoorsy
nav: Providers
network: true
overview: 'Outdoorsy publishes 2 APIs on the [APIs.io](https://apis.io/) network, including Search API, and 1 more. Tagged areas include Company, Travel, Marketplace, Rentals, and Recreational Vehicles.


  Outdoorsy''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 21 more developer resources.'
random_paper: 66
rate_limits:
- limit_count: 1
  name: Outdoorsy Rate Limits
  slug: outdoorsy-rate-limits
score:
  band: thin
  composite: 41.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.9
  scored_at: '2026-08-03'
security:
- kind: authentication
  name: Outdoorsy Authentication
  slug: outdoorsy-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Outdoorsy Domain Security
  slug: outdoorsy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outdoorsy
tags:
- Company
- Travel
- Marketplace
- Rentals
- Recreational Vehicles
- Bookings
- Search
- Payments
- Insurance
- Camping
- Tourism
website: https://www.outdoorsy.com/
---
