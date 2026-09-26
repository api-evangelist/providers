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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Uplisting Agentic Access
  operation_count: 18
  slug: uplisting-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Authenticated account/user context.
  name: Uplisting Account API
  slug: uplisting-account-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Properties available for a date range.
  name: Uplisting Availability API
  slug: uplisting-availability-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Reservations across all connected channels.
  name: Uplisting Bookings API
  slug: uplisting-bookings-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Availability, prices, and restrictions per property and date.
  name: Uplisting Calendar API
  slug: uplisting-calendar-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Guest records tied to bookings (modeled).
  name: Uplisting Guests API
  slug: uplisting-guests-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Guest messaging via the unified inbox (modeled).
  name: Uplisting Messages API
  slug: uplisting-messages-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Properties (listings) in the account.
  name: Uplisting Properties API
  slug: uplisting-properties-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Nightly rates and price adjustments (modeled via the calendar).
  name: Uplisting Rates API
  slug: uplisting-rates-api
- baseURL: https://connect.uplisting.io
  baseurl_source: declared
  description: Endpoints that receive booking change events.
  name: Uplisting Webhooks API
  slug: uplisting-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Uplisting Public and Partner Account API
  slug: open-uplisting-account-api
- collection_type: open
  name: Uplisting Public and Partner Account Availability API
  slug: open-uplisting-availability-api
- collection_type: open
  name: Uplisting Public and Partner Account Bookings API
  slug: open-uplisting-bookings-api
- collection_type: open
  name: Uplisting Public and Partner Account Calendar API
  slug: open-uplisting-calendar-api
- collection_type: open
  name: Uplisting Public and Partner Account Guests API
  slug: open-uplisting-guests-api
- collection_type: open
  name: Uplisting Public and Partner Account Messages API
  slug: open-uplisting-messages-api
- collection_type: open
  name: Uplisting Public and Partner Account Properties API
  slug: open-uplisting-properties-api
- collection_type: open
  name: Uplisting Public and Partner Account Rates API
  slug: open-uplisting-rates-api
- collection_type: open
  name: Uplisting Public and Partner Account Webhooks API
  slug: open-uplisting-webhooks-api
- collection_type: open
  name: Uplisting Public and Partner API
  slug: open-uplisting
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/agentic-access/uplisting-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uplisting-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/security/uplisting-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uplisting-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/authentication/uplisting-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uplisting-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uplisting.io/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uplisting
- group: company
  title: ''
  type: Website
  url: https://www.uplisting.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.uplisting.io/docs/api
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/plans/uplisting-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uplisting-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/rate-limits/uplisting-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/uplisting-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/finops/uplisting-finops.yml
  title: ''
  type: FinOps
  url: finops/uplisting-finops.yml
created: '2026-07-03'
description: Uplisting is short-term and vacation rental management software and a channel manager for professional hosts and property managers. It syncs listings, bookings, availability, rates, and guest messaging across Airbnb, Vrbo, and Booking.com, and powers a direct booking website and unified inbox. Uplisting exposes an invite-only Public and Partner REST API at https://connect.uplisting.io for reading properties, bookings, availability, and calendar (prices and restrictions), plus webhooks that push booking changes to partner endpoints. Authentication is HTTP Basic with a Base64-encoded API key generated on the Connect page. Uplisting is part of the AirDNA family.
finops:
- name: Uplisting Finops
  service_category: Property Management Software
  slug: uplisting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uplisting.png
layout: provider
modified: '2026-07-03'
name: Uplisting
nav: Providers
network: true
overview: 'Uplisting publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Availability API, Bookings API, and 6 more. Tagged areas include Vacation Rentals, Short-Term Rental, Channel Manager, Property Management, and Booking.


  Uplisting''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Uplisting Plans Pricing
  plan_count: 3
  slug: uplisting-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Uplisting Rate Limits
  slug: uplisting-rate-limits
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 44.8
    developer_ergonomics: 21.4
    discoverability: 68.3
    operational_transparency: 28.4
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/uplisting/refs/heads/main/screenshots/uplisting-2026-09-02T165042.png
security:
- kind: authentication
  name: Uplisting Authentication
  slug: uplisting-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uplisting Domain Security
  slug: uplisting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uplisting
tags:
- Vacation Rentals
- Short-Term Rental
- Channel Manager
- Property Management
- Booking
- Hospitality
website: https://www.uplisting.io
---
