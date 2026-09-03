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
  scored_at: '2026-09-03'
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
  title: ''
  type: AgenticAccess
  url: agentic-access/uplisting-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uplisting-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/uplisting-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uplisting-rate-limits.yml
- group: commercial
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
overview: 'Uplisting publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Availability API, Bookings API, and 6 more. Tagged areas include Vacation Rental, Short-Term Rental, Channel Manager, Property Management, and Bookings.


  Uplisting''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Uplisting Plans Pricing
  plan_count: 3
  slug: uplisting-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Uplisting Rate Limits
  slug: uplisting-rate-limits
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 11.1
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- Vacation Rental
- Short-Term Rental
- Channel Manager
- Property Management
- Bookings
- Hospitality
website: https://www.uplisting.io
---
