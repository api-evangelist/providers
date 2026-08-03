---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cargurus Dealer Agentic Access
  operation_count: 6
  slug: cargurus-dealer-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 4
apis:
- description: Open API for building new/used listing search widgets.
  name: CarGurus Car Selector API
  slug: cargurus-dealer-car-selector-api
- description: Retrieve sales reviews for a specific dealer.
  name: CarGurus Dealer Reviews API
  slug: cargurus-dealer-dealer-reviews-api
- description: Retrieve dealer inventory performance statistics.
  name: CarGurus Dealer Stats API
  slug: cargurus-dealer-dealer-stats-api
- description: Retrieve CarGurus Instant Market Value and deal rating for cars.
  name: CarGurus Instant Market Value API
  slug: cargurus-dealer-instant-market-value-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cargurus-dealer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargurus-dealer-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargurus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cargurus
- group: company
  title: ''
  type: Website
  url: https://www.cargurus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cargurus.com/Cars/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargurus.com/Cars/developers/docs/CarSelector.html
- group: start
  title: ''
  type: SignUp
  url: https://dealers.cargurus.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/cargurus-dealer-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://dealers.cargurus.com/drc
created: '2026-07-10'
description: CarGurus is an automotive shopping and dealer marketing platform that connects car shoppers with franchise and independent dealers through data-driven listings, its Instant Market Value (IMV) deal ratings, and dealer reviews. For developers and partners, CarGurus publishes a small set of documented HTTP APIs under /Cars/api/ - an open Car Selector API for building new/used search widgets, and partner/dealer-gated APIs for Instant Market Value, dealer reviews, and dealer performance statistics (leads, VDPs, SRPs, impressions). Dealer inventory itself is ingested through inventory feeds (feed providers / IMT), not a documented public pull API, and leads are delivered to dealer CRMs rather than exposed as a public REST endpoint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cargurus-dealer.png
layout: provider
modified: '2026-07-10'
name: CarGurus
nav: Providers
network: true
overview: 'CarGurus publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Car Selector API, Dealer Reviews API, Dealer Stats API, and 1 more. Tagged areas include Automotive, Marketplace, Car Listings, Dealer, and Vehicle Pricing.


  CarGurus'' developer surface includes documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Cargurus Dealer Plans Pricing
  plan_count: 3
  slug: cargurus-dealer-plans-pricing
random_paper: 22
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargurus-dealer/refs/heads/main/screenshots/cargurus-dealer-2026-07-25T204615.png
security:
- kind: domain-security
  name: Cargurus Dealer Domain Security
  slug: cargurus-dealer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cargurus-dealer
tags:
- Automotive
- Marketplace
- Car Listings
- Dealer
- Vehicle Pricing
- Reviews
- Inventory
website: https://www.cargurus.com
---
