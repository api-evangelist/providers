---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Ratehawk Agentic Access
  operation_count: 13
  slug: ratehawk-agentic-access
  summary_line: 13 operations · 12 acting
api_count: 6
apis:
- description: The Booking API from RateHawk — 3 operation(s) for booking.
  name: RateHawk Booking API
  slug: ratehawk-booking-api
- description: The Cancellation API from RateHawk — 1 operation(s) for cancellation.
  name: RateHawk Cancellation API
  slug: ratehawk-cancellation-api
- description: The Hotel Content API from RateHawk — 2 operation(s) for hotel content.
  name: RateHawk Hotel Content API
  slug: ratehawk-hotel-content-api
- description: The Hotel Search API from RateHawk — 4 operation(s) for hotel search.
  name: RateHawk Hotel Search API
  slug: ratehawk-hotel-search-api
- description: The Orders API from RateHawk — 2 operation(s) for orders.
  name: RateHawk Orders API
  slug: ratehawk-orders-api
- description: The Prebook API from RateHawk — 1 operation(s) for prebook.
  name: RateHawk Prebook API
  slug: ratehawk-prebook-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking API
  slug: open-ratehawk-booking-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking Cancellation API
  slug: open-ratehawk-cancellation-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking Hotel Content API
  slug: open-ratehawk-hotel-content-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking Hotel Search API
  slug: open-ratehawk-hotel-search-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking Orders API
  slug: open-ratehawk-orders-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3) Booking Prebook API
  slug: open-ratehawk-prebook-api
- collection_type: open
  name: RateHawk / ETG API (WorldOta APIv3)
  slug: open-ratehawk
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ratehawk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ratehawk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ratehawk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EmergingTravel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ratehawk-com
- group: company
  title: ''
  type: Website
  url: https://www.ratehawk.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.emergingtravel.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/ratehawk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ratehawk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ratehawk-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.ratehawk.com/feed/
created: '2026-06-25'
description: RateHawk is the B2B hotel and travel booking brand of Emerging Travel Group (ETG). Its Partner API (pAPI v3, served from api.worldota.net) gives OTAs, travel platforms, and agencies programmatic access to 2.5M+ properties with net rates, covering hotel search, prebook, the asynchronous order booking flow, static hotel content, and cancellation over a JSON REST interface secured with HTTP Basic auth.
finops:
- name: Ratehawk Finops
  service_category: Travel and Booking
  slug: ratehawk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ratehawk.png
layout: provider
modified: '2026-06-25'
name: RateHawk
nav: Providers
network: true
overview: 'RateHawk publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Booking API, Cancellation API, Hotel Content API, and 3 more. Tagged areas include Travel, Hotels, Booking, B2B, and Reservations.


  RateHawk''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Ratehawk Plans Pricing
  plan_count: 3
  slug: ratehawk-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Ratehawk Rate Limits
  slug: ratehawk-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Ratehawk Authentication
  slug: ratehawk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ratehawk Domain Security
  slug: ratehawk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ratehawk
tags:
- Travel
- Hotels
- Booking
- B2B
- Reservations
website: https://www.ratehawk.com
---
