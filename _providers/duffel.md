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
- acting_count: 21
  human_in_the_loop: 0
  name: Duffel Agentic Access
  operation_count: 39
  slug: duffel-agentic-access
  summary_line: 39 operations · 21 acting
api_count: 10
apis:
- description: The Ancillaries API from Duffel — 2 operation(s) for ancillaries.
  name: Duffel Ancillaries API
  slug: duffel-ancillaries-api
- description: Search for flights by creating offer requests.
  name: Duffel Offer Requests API
  slug: duffel-offer-requests-api
- description: Flight offers returned for an offer request.
  name: Duffel Offers API
  slug: duffel-offers-api
- description: Cancel an existing order and preview refunds.
  name: Duffel Order Cancellations API
  slug: duffel-order-cancellations-api
- description: Modify an existing order.
  name: Duffel Order Changes API
  slug: duffel-order-changes-api
- description: Create and manage flight orders (bookings).
  name: Duffel Orders API
  slug: duffel-orders-api
- description: Pay for held orders.
  name: Duffel Payments API
  slug: duffel-payments-api
- description: Seat maps for an offer.
  name: Duffel Seat Maps API
  slug: duffel-seat-maps-api
- description: Accommodation search and booking.
  name: Duffel Stays API
  slug: duffel-stays-api
- description: Register endpoints to receive event notifications.
  name: Duffel Webhooks API
  slug: duffel-webhooks-api
artifact_total: 18
collections:
- collection_type: open
  name: Duffel API
  slug: open-duffel
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/duffel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/duffel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/duffel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/duffel-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/duffelhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/duffel
- group: company
  title: ''
  type: Website
  url: https://duffel.com
- group: docs
  title: ''
  type: Documentation
  url: https://duffel.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/duffel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/duffel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/duffel-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://duffel.com/blog
created: '2026-06-25'
description: Duffel provides a single REST API for selling travel - flights from 300+ airlines, 2M+ hotel properties (Stays), loyalty programmes, and merchant-of-record payments. The Duffel API exposes offer requests, offers, orders, seat maps, order changes and cancellations, payments, and Stays search-to-booking, with webhooks for asynchronous events.
finops:
- name: Duffel Finops
  service_category: Travel and Booking
  slug: duffel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/duffel.png
layout: provider
modified: '2026-06-25'
name: Duffel
nav: Providers
network: true
overview: 'Duffel publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Ancillaries API, Offer Requests API, Offers API, and 7 more. Tagged areas include Travel, Flights, Hotels, Booking, and Payments.


  Duffel''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Duffel Plans Pricing
  plan_count: 3
  slug: duffel-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 2
  name: Duffel Rate Limits
  slug: duffel-rate-limits
score:
  band: thin
  composite: 35.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/duffel/refs/heads/main/screenshots/duffel-2026-07-25T212455.png
security:
- kind: authentication
  name: Duffel Authentication
  slug: duffel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duffel Domain Security
  slug: duffel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Duffel Vulnerability Disclosure
  slug: duffel-vulnerability-disclosure
  summary_line: disclosure policy published
slug: duffel
tags:
- Travel
- Flights
- Hotels
- Booking
- Payments
website: https://duffel.com
---
