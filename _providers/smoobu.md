---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Smoobu Agentic Access
  operation_count: 19
  slug: smoobu-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 6
apis:
- description: Properties / listings in the Smoobu account.
  name: Smoobu Apartments API
  slug: smoobu-apartments-api
- description: Guest contact records.
  name: Smoobu Guests API
  slug: smoobu-guests-api
- description: Reservation messages and unified inbox threads.
  name: Smoobu Messaging API
  slug: smoobu-messaging-api
- description: Daily rates, prices, availability, and booking availability checks.
  name: Smoobu Rates and Availability API
  slug: smoobu-rates-and-availability-api
- description: Bookings across all connected channels and their price elements.
  name: Smoobu Reservations API
  slug: smoobu-reservations-api
- description: The authenticated Smoobu account.
  name: Smoobu User API
  slug: smoobu-user-api
artifact_total: 13
collections:
- collection_type: open
  name: Smoobu API
  slug: open-smoobu
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smoobu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smoobu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smoobu-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smoobu
- group: company
  title: ''
  type: Website
  url: https://www.smoobu.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.smoobu.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/smoobu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smoobu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smoobu-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.smoobu.com/blog/
created: '2026-07-03'
description: Smoobu is an all-in-one vacation rental channel manager and property management system for short-term rental hosts and property managers. It synchronizes availability, rates, and reservations across Airbnb, Booking.com, Vrbo, and other channels, and provides a booking website, unified guest inbox, automated messaging, guest online check-in, invoicing, and dynamic pricing. The Smoobu REST API (base https://login.smoobu.com/api) lets Professional subscribers and integration partners read and write apartments, reservations, rates and availability, guests, and guest messages, and receive webhook notifications when bookings change. Authentication is via an API key header (with HMAC-signed requests recommended and OAuth 2 available for partners).
finops:
- name: Smoobu Finops
  service_category: Vacation Rental Management Software
  slug: smoobu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smoobu.png
layout: provider
modified: '2026-07-03'
name: Smoobu
nav: Providers
network: true
overview: 'Smoobu publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apartments API, Guests API, Messaging API, and 3 more. Tagged areas include Vacation Rental, Channel Manager, Property Management, Short-Term Rental, and Reservations.


  Smoobu''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Smoobu Plans Pricing
  plan_count: 4
  slug: smoobu-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 1
  name: Smoobu Rate Limits
  slug: smoobu-rate-limits
score:
  band: thin
  composite: 37.7
  delta: -0.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Smoobu Authentication
  slug: smoobu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Smoobu Domain Security
  slug: smoobu-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: smoobu
tags:
- Vacation Rental
- Channel Manager
- Property Management
- Short-Term Rental
- Reservations
- Hospitality
website: https://www.smoobu.com
---
