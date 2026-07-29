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
- acting_count: 4
  human_in_the_loop: 0
  name: Hotelrunner Agentic Access
  operation_count: 15
  slug: hotelrunner-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 4
apis:
- description: Connected OTA / sales channel status.
  name: HotelRunner Channels API
  slug: hotelrunner-channels-api
- description: Room types, master rates, availability, and restrictions.
  name: HotelRunner Inventory API
  slug: hotelrunner-inventory-api
- description: Read-only lookup data used for property and integration setup.
  name: HotelRunner Reference Data API
  slug: hotelrunner-reference-data-api
- description: Retrieve, confirm, cancel, and acknowledge reservations.
  name: HotelRunner Reservations API
  slug: hotelrunner-reservations-api
artifact_total: 11
collections:
- collection_type: open
  name: HotelRunner Custom Apps REST API
  slug: open-hotelrunner
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hotelrunner-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotelrunner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hotelrunner-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hotelrunner
- group: company
  title: ''
  type: Website
  url: https://hotelrunner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hotelrunner.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/hotelrunner-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hotelrunner-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hotelrunner-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://hotelrunner.com/en/blog/
created: '2026-07-03'
description: HotelRunner is a Turkey-founded global hospitality technology platform - a channel manager, central reservation system, booking engine, and website/content manager for hotels, apartments, and travel agencies. Its Custom Apps program exposes a token-authenticated REST API (and a legacy OTA-style XML/SOAP API) so a property's PMS or revenue management system can pull room and rate configuration, push availability/rate/restriction updates to connected OTAs and channels, retrieve and acknowledge reservations, and receive real-time reservation pushes via an HTTP webhook callback.
finops:
- name: Hotelrunner Finops
  service_category: Hospitality Technology / Channel Management
  slug: hotelrunner-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hotelrunner.png
layout: provider
modified: '2026-07-03'
name: HotelRunner
nav: Providers
network: true
overview: 'HotelRunner publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Inventory API, Reference Data API, and 1 more. Tagged areas include Hospitality, Hotel, Channel Manager, Booking Engine, and PMS.


  HotelRunner''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Hotelrunner Plans Pricing
  plan_count: 5
  slug: hotelrunner-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Hotelrunner Rate Limits
  slug: hotelrunner-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hotelrunner/refs/heads/main/screenshots/hotelrunner-2026-07-25T221503.png
security:
- kind: authentication
  name: Hotelrunner Authentication
  slug: hotelrunner-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hotelrunner Domain Security
  slug: hotelrunner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hotelrunner
tags:
- Hospitality
- Hotel
- Channel Manager
- Booking Engine
- PMS
- Travel
website: https://hotelrunner.com/
---
