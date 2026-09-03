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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Parkwhiz Agentic Access
  operation_count: 36
  slug: parkwhiz-agentic-access
  summary_line: 36 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: User accounts, vehicles, and payment methods.
  name: ParkWhiz Accounts & Vehicles API
  slug: parkwhiz-accounts-vehicles-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Create and manage parking reservations and parking passes.
  name: ParkWhiz Bookings API
  slug: parkwhiz-bookings-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Recurring monthly parking bookings.
  name: ParkWhiz Monthly Parking API
  slug: parkwhiz-monthly-parking-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Token issuance for partner and user authorization.
  name: ParkWhiz OAuth API
  slug: parkwhiz-oauth-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Search bookable availability and pricing, and parking location details.
  name: ParkWhiz Quotes & Locations API
  slug: parkwhiz-quotes-locations-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Drive-up parking transactions, violations, and payment.
  name: ParkWhiz Tickets API
  slug: parkwhiz-tickets-api
- baseURL: https://api.parkwhiz.com/v4
  baseurl_source: declared
  description: Venue and event lookup for event parking.
  name: ParkWhiz Venues & Events API
  slug: parkwhiz-venues-events-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles API
  slug: open-parkwhiz-accounts-vehicles-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles Bookings API
  slug: open-parkwhiz-bookings-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles Monthly Parking API
  slug: open-parkwhiz-monthly-parking-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles OAuth API
  slug: open-parkwhiz-oauth-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles Quotes & Locations API
  slug: open-parkwhiz-quotes-locations-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles Tickets API
  slug: open-parkwhiz-tickets-api
- collection_type: open
  name: ParkWhiz / Arrive API v4 Accounts & Vehicles Venues & Events API
  slug: open-parkwhiz-venues-events-api
- collection_type: open
  name: ParkWhiz / Arrive API v4
  slug: open-parkwhiz
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/parkwhiz-capability-edges.yml
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


  ParkWhiz''s developer surface includes authentication, documentation, getting-started guide, changelog, SDKs, and 10 more developer resources.'
plans:
- name: Parkwhiz Plans Pricing
  plan_count: 3
  slug: parkwhiz-plans-pricing
random_paper: 19
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
  composite: 44.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.6
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Event
website: https://www.parkwhiz.com
---
