---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Hospitable Agentic Access
  operation_count: 13
  slug: hospitable-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 8
apis:
- description: Hospitable v2 webhooks push near-real-time event notifications (reservation.created, reservation.changed, property.created/changed/deleted/merged, message.created, review.created) as JSON POST request
  name: Hospitable Webhooks API
  slug: hospitable-webhooks-api
- description: Nightly availability, pricing, and restrictions per property.
  name: Hospitable Calendar API
  slug: hospitable-calendar-api
- description: Channel listings (Airbnb, Vrbo, Booking.com, direct) mapped to a property.
  name: Hospitable Listings API
  slug: hospitable-listings-api
- description: Guest-host message threads per reservation.
  name: Hospitable Messages API
  slug: hospitable-messages-api
- description: Vacation rental properties connected to the account.
  name: Hospitable Properties API
  slug: hospitable-properties-api
- description: Bookings across all connected channels.
  name: Hospitable Reservations API
  slug: hospitable-reservations-api
- description: Guest reviews and host responses.
  name: Hospitable Reviews API
  slug: hospitable-reviews-api
- description: The authenticated Hospitable user.
  name: Hospitable User API
  slug: hospitable-user-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hospitable Public Calendar API
  slug: open-hospitable-calendar-api
- collection_type: open
  name: Hospitable Public Calendar Listings API
  slug: open-hospitable-listings-api
- collection_type: open
  name: Hospitable Public Calendar Messages API
  slug: open-hospitable-messages-api
- collection_type: open
  name: Hospitable Public Calendar Properties API
  slug: open-hospitable-properties-api
- collection_type: open
  name: Hospitable Public Calendar Reservations API
  slug: open-hospitable-reservations-api
- collection_type: open
  name: Hospitable Public Calendar User API
  slug: open-hospitable-user-api
- collection_type: open
  name: Hospitable Public API v2
  slug: open-hospitable
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hospitable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hospitable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hospitable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hospitable
- group: company
  title: ''
  type: Website
  url: https://hospitable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hospitable.com/docs/public-api-docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/hospitable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hospitable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hospitable-finops.yml
created: '2026-07-03'
description: Hospitable (formerly Smartbnb) is a short-term and vacation rental automation platform for Airbnb, Vrbo, Booking.com, and direct-booking hosts and property managers. It centralizes multi-channel calendar syncing, AI-powered guest messaging in a unified inbox, cleaning and operations tasks, reviews, and a direct booking website. The Hospitable Public API v2 is a REST API at https://public.api.hospitable.com/v2 that lets hosts and vendors programmatically manage properties, channel listings, reservations, guest messaging, calendar availability and pricing, and reviews, authenticated with OAuth 2.0 (for vendors) or Personal Access Tokens (for personal use). v2 webhooks push reservation, property, message, and review events to a host's server.
finops:
- name: Hospitable Finops
  service_category: Vacation Rental Management Software
  slug: hospitable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hospitable.png
layout: provider
modified: '2026-07-03'
name: Hospitable
nav: Providers
network: true
overview: 'Hospitable publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Listings API, Messages API, and 4 more. Tagged areas include Vacation Rental, Short-Term Rental, Property Management, Airbnb, and Hospitality.


  Hospitable''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Hospitable Plans Pricing
  plan_count: 5
  slug: hospitable-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 3
  name: Hospitable Rate Limits
  slug: hospitable-rate-limits
score:
  band: thin
  composite: 38.0
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hospitable/refs/heads/main/screenshots/hospitable-2026-07-25T221454.png
security:
- kind: authentication
  name: Hospitable Authentication
  slug: hospitable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hospitable Domain Security
  slug: hospitable-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hospitable
tags:
- Vacation Rental
- Short-Term Rental
- Property Management
- Airbnb
- Hospitality
- Automation
website: https://hospitable.com/
---
