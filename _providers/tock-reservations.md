---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: Twice-daily export of all historical reservation and guest data for the locations in a Tock business group. Payloads follow the published Reservation data model (party, purchased experiences, options,
  name: Tock Data Exports API
  slug: tock-data-exports-api
- description: Add and update basic guest information and guest-profile tags in Tock, following the published Guest data model (patron identity, contact details, dietary restrictions, hospitality preferences, busine
  name: Tock Guest Profile Ingest API
  slug: tock-guest-profile-ingest-api
- description: Real-time webhook that delivers reservation updates for all locations within a Tock business group to a partner-supplied endpoint URL. The partner provides the receiving endpoint and any required auth
  name: Tock Real-time Reservation Webhook
  slug: tock-reservation-webhook
- description: Real-time webhook that delivers guest-profile updates for all locations within a Tock business group to a partner-supplied endpoint URL. Tock POSTs guest-profile events shaped by the published Guest d
  name: Tock Real-time Guest Profile Webhook
  slug: tock-guest-profile-webhook
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tock-reservations-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tock-hq
- group: company
  title: ''
  type: Website
  url: https://www.exploretock.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.exploretock.com/docs/latest/reservation.html
- group: docs
  title: ''
  type: Documentation
  url: https://tock.zendesk.com/hc/en-us/articles/25447494175508-API-FAQ
- group: company
  title: ''
  type: Partnerships
  url: https://www.exploretock.com/join/partnerships/
- group: commercial
  title: ''
  type: Plans
  url: plans/tock-reservations-plans-pricing.yml
created: '2026-07-05'
description: Tock is a restaurant and hospitality reservations, events, and ordering platform used by restaurants, wineries, bars, and hotels to manage bookings, prepaid experiences, waitlists, and guest data. Tock is owned by American Express (acquired from Squarespace in 2024). Tock exposes a partner and enterprise-gated data API and webhook program rather than an open self-serve developer API - access is limited to Premium and Premium Unlimited plans and is provisioned by request to Tock. The documented surface consists of a twice-daily Data Exports API for historical reservation and guest data, a Guest Profile Ingest API for adding and updating basic guest information and tags, and real-time reservation and guest-profile webhooks. Reservation records cannot be created or manipulated through the API. Data-model reference documentation is published publicly at api.exploretock.com, but concrete endpoint paths, methods, and OpenAPI definitions are only shared with approved partners; the
  API entries below are modeled from the public data model and API FAQ.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tock-reservations.png
layout: provider
modified: '2026-07-05'
name: Tock
nav: Providers
network: true
overview: 'Tock publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Reservations, Restaurants, Hospitality, Events, and Ordering.


  Tock''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Tock Reservations Plans Pricing
  plan_count: 3
  slug: tock-reservations-plans-pricing
random_paper: 85
score:
  band: emerging
  composite: 15.5
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Tock Reservations Domain Security
  slug: tock-reservations-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tock-reservations
tags:
- Reservations
- Restaurants
- Hospitality
- Events
- Ordering
- Guest Data
- Webhooks
- Partner API
- American Express
website: https://www.exploretock.com
---
