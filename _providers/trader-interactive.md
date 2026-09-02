---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The TraderOnline REST API is the integration surface behind Trader Interactive's marketplace network. It is an OAuth 2.0 protected, JSON, offset/limit paginated REST API served from api.traderonline.c
  name: TraderOnline (TOL) API
  slug: tol-api
artifact_total: 5
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/traderinteractive/tol-api-php/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.traderinteractive.com/
- group: company
  title: ''
  type: About
  url: https://www.traderinteractive.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.traderinteractive.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.traderinteractive.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.traderinteractive.com/newsroom/
- group: operate
  title: ''
  type: Support
  url: https://www.traderinteractive.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.traderinteractive.com/tradertraxxhelp/
- group: start
  title: ''
  type: Login
  url: https://dealers.traderinteractive.com/tradertraxx/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.traderinteractive.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.traderinteractive.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/traderinteractive
- group: build
  title: ''
  type: Packages
  url: packages/trader-interactive-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/trader-interactive-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trader-interactive-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trader-interactive-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trader-interactive-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trader-interactive-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trader-interactive-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trader-interactive-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trader-interactive-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trader-interactive-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trader-interactive-domain-security.yml
created: '2026-08-30'
description: Trader Interactive is a Norfolk, Virginia digital marketplace and dealer-services company operating a portfolio of vertical vehicle marketplaces — RV Trader, Cycle Trader, ATV Trader, PWC Trader, Snowmobile Trader, Aero Trader, Boatmart, Trade-A-Plane, Commercial Truck Trader, Equipment Trader, Next Truck, Rock & Dirt and Tradequip — alongside the Commercial Web Services and RV Web Services dealer website businesses and Statistical Surveys market research. It reaches over 13 million monthly unique visitors and has been wholly owned by CAR Group (formerly carsales.com Ltd) since 2022. Its integration surface is the TraderOnline (TOL) REST API, served from api.traderonline.com behind AWS API Gateway and consumed by dealers and syndication partners through first-party OAuth 2.0 client-credentials clients that Trader Interactive publishes as open source on GitHub, Packagist and npm. There is no public developer portal, no published API reference, and no machine-readable specification.
image: https://www.traderinteractive.com/wp-content/uploads/2026/08/TI-favicon.png
layout: provider
modified: '2026-08-30'
name: Trader Interactive
nav: Providers
network: true
overview: 'Trader Interactive publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Classifieds, Automotive, and Power-Sports.


  Trader Interactive''s developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Trader Interactive Plans Pricing
  plan_count: 0
  slug: trader-interactive-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Trader Interactive Rate Limits
  slug: trader-interactive-rate-limits
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.7
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 22.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Trader Interactive Authentication
  slug: trader-interactive-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Trader Interactive Domain Security
  slug: trader-interactive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trader-interactive
tags:
- Company
- Marketplace
- Classifieds
- Automotive
- Power-Sports
- Recreational Vehicles
- Commercial Trucks
- Heavy Equipment
- Dealer Services
- Digital Advertising
- Vehicle Listings
- Media
website: https://www.traderinteractive.com/
---
