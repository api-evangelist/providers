---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Parkwhiz Agentic Access
  operation_count: 36
  slug: parkwhiz-agentic-access
  summary_line: 36 operations · 17 acting
api_count: 7
apis:
- description: User accounts, vehicles, and payment methods.
  name: ParkWhiz Accounts & Vehicles API
  slug: parkwhiz-accounts-vehicles-api
- description: Create and manage parking reservations and parking passes.
  name: ParkWhiz Bookings API
  slug: parkwhiz-bookings-api
- description: Recurring monthly parking bookings.
  name: ParkWhiz Monthly Parking API
  slug: parkwhiz-monthly-parking-api
- description: Token issuance for partner and user authorization.
  name: ParkWhiz OAuth API
  slug: parkwhiz-oauth-api
- description: Search bookable availability and pricing, and parking location details.
  name: ParkWhiz Quotes & Locations API
  slug: parkwhiz-quotes-locations-api
- description: Drive-up parking transactions, violations, and payment.
  name: ParkWhiz Tickets API
  slug: parkwhiz-tickets-api
- description: Venue and event lookup for event parking.
  name: ParkWhiz Venues & Events API
  slug: parkwhiz-venues-events-api
artifact_total: 15
collections:
- collection_type: open
  name: ParkWhiz / Arrive API v4
  slug: open-parkwhiz
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parkwhiz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parkwhiz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parkwhiz-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parkwhiz-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.parkwhiz.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parkwhiz
- group: docs
  title: ''
  type: Documentation
  url: https://developer.parkwhiz.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.parkwhiz.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.parkwhiz.com/getting_started/
- group: operate
  title: ''
  type: Changelog
  url: https://developer.parkwhiz.com/changes/
- group: build
  title: ''
  type: SDK
  url: https://developer.parkwhiz.com/libraries/
- group: commercial
  title: ''
  type: Plans
  url: plans/parkwhiz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parkwhiz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/parkwhiz-finops.yml
created: '2026-07-03'
description: ParkWhiz is a parking reservation and mobility platform (with the BestParking discovery brand) that lets drivers search, price, reserve, and pay for parking at facilities, venues, and events across North America. Its consumer apps and website are backed by a documented v4 REST API (api.parkwhiz.com / api.arrive.com) covering location and quote search, bookings, parking passes, venues and events, monthly parking, vehicles, payment methods, and accounts. ParkWhiz was rebranded to Arrive / Arrive Mobility and merged into FlashParking (Flash) in January 2021; separately, EasyPark Group acquired the rights to the "Arrive" name from Flash and rebranded itself to Arrive in 2025. The v4 API is publicly documented but partner-gated - OAuth client credentials are issued to approved partners on request (dev@parkwhiz.com), not self-serve.
finops:
- name: Parkwhiz Finops
  service_category: Mobility and Parking
  slug: parkwhiz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parkwhiz.png
layout: provider
modified: '2026-07-03'
name: ParkWhiz
nav: Providers
network: true
overview: 'ParkWhiz publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts & Vehicles API, Bookings API, Monthly Parking API, and 4 more. Tagged areas include Parking, Mobility, Reservations, Bookings, and Transportation.


  ParkWhiz''s developer surface includes authentication, documentation, getting-started guide, changelog, SDKs, and 9 more developer resources.'
plans:
- name: Parkwhiz Plans Pricing
  plan_count: 3
  slug: parkwhiz-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 3
  name: Parkwhiz Rate Limits
  slug: parkwhiz-rate-limits
scopes:
- name: Parkwhiz Scopes
  scope_count: 4
  slug: parkwhiz-scopes
  summary_line: 4 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.5
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.7
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parkwhiz/refs/heads/main/screenshots/parkwhiz-2026-08-07T191441.png
security:
- kind: authentication
  name: Parkwhiz Authentication
  slug: parkwhiz-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Parkwhiz Domain Security
  slug: parkwhiz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: parkwhiz
tags:
- Parking
- Mobility
- Reservations
- Bookings
- Transportation
- Location
- Events
website: https://www.parkwhiz.com
---
