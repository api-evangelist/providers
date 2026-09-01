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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Smoobu Agentic Access
  operation_count: 19
  slug: smoobu-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smoobu Apartments API
  slug: open-smoobu-apartments-api
- collection_type: open
  name: Smoobu Apartments Guests API
  slug: open-smoobu-guests-api
- collection_type: open
  name: Smoobu Apartments Messaging API
  slug: open-smoobu-messaging-api
- collection_type: open
  name: Smoobu Apartments Rates and Availability API
  slug: open-smoobu-rates-and-availability-api
- collection_type: open
  name: Smoobu Apartments Reservations API
  slug: open-smoobu-reservations-api
- collection_type: open
  name: Smoobu Apartments User API
  slug: open-smoobu-user-api
- collection_type: open
  name: Smoobu API
  slug: open-smoobu
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/smoobu-capability-edges.yml
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


  Smoobu''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Smoobu Plans Pricing
  plan_count: 4
  slug: smoobu-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Smoobu Rate Limits
  slug: smoobu-rate-limits
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 59.2
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
