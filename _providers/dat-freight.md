---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Dat Freight Agentic Access
  operation_count: 10
  slug: dat-freight-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 6
apis:
- description: Instant digital load booking.
  name: DAT Freight & Analytics BookNow API
  slug: dat-freight-booknow-api
- description: Create and manage load and truck postings.
  name: DAT Freight & Analytics Freight Posting API
  slug: dat-freight-freight-posting-api
- description: Two-tier organization and user token issuance.
  name: DAT Freight & Analytics Identity API
  slug: dat-freight-identity-api
- description: Search available loads and trucks on the DAT One marketplace.
  name: DAT Freight & Analytics Load Board Search API
  slug: dat-freight-load-board-search-api
- description: Spot and contract freight-rate lookups.
  name: DAT Freight & Analytics RateView API
  slug: dat-freight-rateview-api
- description: Shipment location and status visibility.
  name: DAT Freight & Analytics Tracking API
  slug: dat-freight-tracking-api
artifact_total: 13
collections:
- collection_type: open
  name: DAT Freight & Analytics API (Modeled)
  slug: open-dat-freight
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dat-freight-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dat-freight-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dat-freight-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dat-solutions
- group: company
  title: ''
  type: Website
  url: https://www.dat.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dat.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.dat.com/api-integration
- group: commercial
  title: ''
  type: Plans
  url: plans/dat-freight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dat-freight-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dat-freight-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.dat.com/blog
created: '2026-07-05'
description: 'DAT Freight & Analytics operates the largest truckload freight marketplace in North America - the DAT One load board - along with RateView, the industry''s benchmark for spot and contract freight rates drawn from hundreds of billions of dollars in real transactions. DAT exposes these products to Transportation Management Systems (TMS) and freight platforms through the DAT Developer Portal (developer.dat.com), a RESTful API suite covering load posting and search, RateView rate lookups, BookNow instant booking, and shipment tracking. Access is subscription-gated: RESTful integration requires a DAT One load board subscription and a service (organization) account, and RateView access requires a Combo Pro or Combo Premium plan. Every request is authenticated with a two-tier token model - an organization token issued from service-account credentials plus a user token for the account making the call.'
finops:
- name: Dat Freight Finops
  service_category: Freight and Logistics Data
  slug: dat-freight-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dat-freight.png
layout: provider
modified: '2026-07-05'
name: DAT Freight & Analytics
nav: Providers
network: true
overview: 'DAT Freight & Analytics publishes 6 APIs on the [APIs.io](https://apis.io/) network, including BookNow API, Freight Posting API, Identity API, and 3 more. Tagged areas include Freight, Trucking, Load Board, Logistics, and Freight Rates.


  DAT Freight & Analytics'' developer surface includes authentication, documentation, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Dat Freight Plans Pricing
  plan_count: 4
  slug: dat-freight-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Dat Freight Rate Limits
  slug: dat-freight-rate-limits
score:
  band: developing
  composite: 42.3
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dat-freight/refs/heads/main/screenshots/dat-freight-2026-07-25T211230.png
security:
- kind: authentication
  name: Dat Freight Authentication
  slug: dat-freight-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dat Freight Domain Security
  slug: dat-freight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dat-freight
tags:
- Freight
- Trucking
- Load Board
- Logistics
- Freight Rates
- RateView
- Supply Chain
- Transportation
- Analytics
website: https://www.dat.com
---
