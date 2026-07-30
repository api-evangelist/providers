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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Beds24 Agentic Access
  operation_count: 23
  slug: beds24-agentic-access
  summary_line: 23 operations · 10 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Account-level information, sub-accounts, and users.
  name: Beds24 Accounts API
  slug: beds24-accounts-api
- description: Refresh and access token management and diagnostics.
  name: Beds24 Authentication API
  slug: beds24-authentication-api
- description: Read, create, and modify reservations across all channels.
  name: Beds24 Bookings API
  slug: beds24-bookings-api
- description: OTA channel connection and mapping management.
  name: Beds24 Channels API
  slug: beds24-channels-api
- description: Per-day availability calendar, availability status, and fixed prices.
  name: Beds24 Inventory API
  slug: beds24-inventory-api
- description: Invoice items, charges, and payments attached to bookings.
  name: Beds24 Invoices API
  slug: beds24-invoices-api
- description: Guest and channel messages attached to bookings.
  name: Beds24 Messages API
  slug: beds24-messages-api
- description: Property and room configuration and bookable offers.
  name: Beds24 Properties API
  slug: beds24-properties-api
artifact_total: 15
collections:
- collection_type: open
  name: Beds24 API V2
  slug: open-beds24
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beds24-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beds24-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beds24-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beds24
- group: company
  title: ''
  type: Website
  url: https://beds24.com
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.beds24.com/index.php/Category:API_V2
- group: commercial
  title: ''
  type: Plans
  url: plans/beds24-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beds24-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beds24-finops.yml
created: '2026-07-03'
description: Beds24 is a vacation rental and hotel channel manager, property management system (PMS), and online booking engine. It synchronizes availability, rates, and reservations across OTAs such as Booking.com, Airbnb, Expedia, Vrbo, and Google, and exposes a documented REST API (v2 at api.beds24.com/v2, with a legacy JSON/XML v1) for reading and writing bookings, properties, room inventory, availability calendars, prices, invoices, channels, and account data. API V2 uses expiring access tokens generated from refresh tokens, scoped permissions, optional IP whitelisting, and a credit-based rate limit enforced per account over a rolling 5-minute window.
finops:
- name: Beds24 Finops
  service_category: Hospitality and Property Management
  slug: beds24-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beds24.png
layout: provider
modified: '2026-07-03'
name: Beds24
nav: Providers
network: true
overview: 'Beds24 publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Bookings API, and 5 more. Tagged areas include Vacation Rental, Hotel, Channel Manager, Property Management System, and Booking Engine.


  Beds24''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Beds24 Plans Pricing
  plan_count: 5
  slug: beds24-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 4
  name: Beds24 Rate Limits
  slug: beds24-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beds24/refs/heads/main/screenshots/beds24-2026-07-25T202622.png
security:
- kind: authentication
  name: Beds24 Authentication
  slug: beds24-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Beds24 Domain Security
  slug: beds24-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: beds24
tags:
- Vacation Rental
- Hotel
- Channel Manager
- Property Management System
- Booking Engine
- Hospitality
- Reservations
website: https://beds24.com
---
