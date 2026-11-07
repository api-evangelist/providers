---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Channex Agentic Access
  operation_count: 42
  slug: channex-agentic-access
  summary_line: 42 operations · 22 acting
api_count: 1
apis:
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Availability, Rates, and Inventory (restrictions).
  name: Channex ARI API
  slug: channex-ari-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Retrieve and manage bookings and booking revisions.
  name: Channex Bookings API
  slug: channex-bookings-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage properties (hotels, apartments, vacation rentals).
  name: Channex Properties API
  slug: channex-properties-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage pricing plans for room types.
  name: Channex Rate Plans API
  slug: channex-rate-plans-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage room types under a property.
  name: Channex Room Types API
  slug: channex-room-types-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage event notification callbacks.
  name: Channex Webhooks API
  slug: channex-webhooks-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Applications extending Channex (PCI, Messages, payment and PMS integrations): the available catalog and per-property installations.'
  name: Channex Applications API
  slug: channex-applications-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'User accounts and sessions: sign-up and confirmation, sign-in with multi-factor verification, OAuth session exchange, token refresh, sign-out, and password recovery.'
  name: Channex Authentication API
  slug: channex-authentication-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Authorize.net Application actions: tokenize a booking''s card into an Authorize.net customer profile.'
  name: Channex Authorize.net App API
  slug: channex-authorize-net-app-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Creating and updating bookings from your own system rather than receiving them from a channel, including bookings that originated at an OTA. Requires the Booking CRS application installed on the Prope
  name: Channex Booking CRS API
  slug: channex-booking-crs-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Chat with guests at the booking level: read and send the messages of a booking, and fetch them from the channel on demand. Requires the Messages & Reviews application installed on the Property.'
  name: Channex Booking Messages API
  slug: channex-booking-messages-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Payments of a booking: list them and process charges, pre-authorizations, settlements, voids, and refunds. Requires the Payments application installed on the Property; without it every operation here '
  name: Channex Booking Payments API
  slug: channex-booking-payments-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'What Booking.com pays out for a booking: the payout details, the price breakdown behind them, and the bank transfer payout. Available for bookings that came through a Booking.com channel.'
  name: Channex Booking Payouts API
  slug: channex-booking-payouts-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Reports sent back to the OTA about what happened with a booking: a guest no-show, invalid credit card details, a cancellation caused by them, a change of stay, and guest misconduct. Supported for Book'
  name: Channex Booking Reporting API
  slug: channex-booking-reporting-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Availability overrides (stop-sales, offsets, caps) for specific Room Types and Channels over a date range — closing out a channel for a holiday week, or capping what one Room Type publishes to one Cha
  name: Channex Channel Availability Rules API
  slug: channex-channel-availability-rules-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Read-only dictionary of property- and room-type-level facilities (amenities). Channex maintains both dictionaries; they cannot be added to through the API. Contact Channex to have a missing facility a
  name: Channex Facilities API
  slug: channex-facilities-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage Group Users — a user's membership of a Group, which grants them access to every Property in it. A membership carries a role and, optionally, access policy overrides on top of it.
  name: Channex Group Users API
  slug: channex-group-users-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage Groups — sets of Properties you manage together, and the users who may reach them. Every Property belongs to at least one Group and may belong to several; a Group that still holds a Property ca
  name: Channex Groups API
  slug: channex-groups-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Manage Hotel Policies — general property rules: check-in/out windows, guest limits, internet, parking, pets, and smoking. A policy belongs to one property, and the property points at it through `hotel'
  name: Channex Hotel Policies API
  slug: channex-hotel-policies-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Feed of notable account events (new bookings, synchronization errors, guest requests): list and read them, and resolve actionable guest requests.'
  name: Channex Live Feed API
  slug: channex-live-feed-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Payment Application actions: connect and manage payment providers, report on transactions, and export them to CSV.'
  name: Channex Payment App API
  slug: channex-payment-app-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Upload and manage Property and RoomType photos.
  name: Channex Photos API
  slug: channex-photos-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage Property Users — a user's access to a single Property. An access carries a role and, optionally, access policy overrides on top of it, and ownership can be handed to another user.
  name: Channex Property Users API
  slug: channex-property-users-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Static reference lists: time zones and supported currencies.'
  name: Channex Reference Data API
  slug: channex-reference-data-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Stripe Tokenization Application actions: tokenize a booking''s card into a Stripe token or payment method.'
  name: Channex Stripe Tokenization App API
  slug: channex-stripe-tokenization-app-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Read-only log of asynchronous tasks processed for a Property (channel syncs, scheduled updates), with timing and outcome.
  name: Channex Tasks API
  slug: channex-tasks-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'Manage Tax Sets — named groups of Taxes applied to Rate Plans, with the order the taxes are calculated in. The first set of a Property becomes its default and is applied to every new Rate Plan of the '
  name: Channex Tax Sets API
  slug: channex-tax-sets-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: Manage Taxes — individual charges (VAT, city tax, fees) applicable to a Rate Plan or Property. Taxes reach a Rate Plan grouped in a Tax Set.
  name: Channex Taxes API
  slug: channex-taxes-api
- baseURL: https://secure.channex.io/api/v1
  baseurl_source: declared
  description: 'HMAC keys that sign webhook deliveries, so that a receiving endpoint can tell that a callback came from Channex and that its body was not altered on the way. A key is a shared secret: Channex holds it'
  name: Channex Webhook Signing Keys API
  slug: channex-webhook-signing-keys-api
artifact_total: 45
collections:
- collection_type: open
  name: Channex ARI API
  slug: open-channex-ari-api
- collection_type: open
  name: Channex ARI Bookings API
  slug: open-channex-bookings-api
- collection_type: open
  name: Channex ARI Channels API
  slug: open-channex-channels-api
- collection_type: open
  name: Channex ARI Properties API
  slug: open-channex-properties-api
- collection_type: open
  name: Channex ARI Rate Plans API
  slug: open-channex-rate-plans-api
- collection_type: open
  name: Channex ARI Room Types API
  slug: open-channex-room-types-api
- collection_type: open
  name: Channex ARI Webhooks API
  slug: open-channex-webhooks-api
- collection_type: open
  name: Channex API
  slug: open-channex
common:
- group: company
  title: ''
  type: Blog
  url: https://channex.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://channex.io/pricing
- group: other
  href: https://artifacts.apis.io/channex/capabilities/channex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/channex-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/channex/agentic-access/channex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/channex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/channex/security/channex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channex-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/channex/authentication/channex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/channex-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ChannexIO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/channex-io
- group: company
  title: ''
  type: Website
  url: https://channex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.channex.io/
- group: commercial
  href: https://artifacts.apis.io/channex/plans/channex-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/channex-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/channex/rate-limits/channex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/channex-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/channex/finops/channex-finops.yml
  title: ''
  type: FinOps
  url: finops/channex-finops.yml
created: '2026-06-25'
description: Channex is a white-label hotel channel manager API that gives Property Management Systems and booking engines a single JSON-based REST integration to distribute availability, rates, and restrictions (ARI) to Booking.com, Airbnb, Expedia, and 50+ other OTAs, and to receive bookings back in real time via webhooks.
finops:
- has_sources: true
  method: generated
  name: Channex Finops
  primary_unit: ''
  service_category: Hospitality and Travel
  slug: channex-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/channex.png
layout: provider
modified: '2026-10-06'
name: Channex
nav: Providers
network: true
overview: 'Channex publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including ARI API, Bookings API, Properties API, and 26 more. Tagged areas include Hospitality, Channel Manager, Hotel Distribution, OTA, and Booking.


  The Channex catalog on APIs.io includes 1 Spectral governance ruleset.


  Channex''s developer surface includes engineering blog, pricing, authentication, documentation, and 9 more developer resources.'
plans:
- name: Channex Plans Pricing
  plan_count: 15
  slug: channex-plans-pricing
- name: Channex Price Estimates
  plan_count: 0
  slug: channex-price-estimates
random_paper: 21
rate_limits:
- limit_count: 3
  name: Channex Rate Limits
  slug: channex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Channex API Rules
  rule_count: 63
  severity_counts:
    error: 49
    hint: 0
    info: 2
    warn: 12
  slug: channex-rules
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 58.7
    developer_ergonomics: 25.0
    discoverability: 66.1
    operational_transparency: 34.2
  previous_composite: 38.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 78.4
      total: 37
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/channex/channex-2026-07-25T205054.png
security:
- kind: authentication
  name: Channex Authentication
  slug: channex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Channex Domain Security
  slug: channex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: channex
tags:
- Hospitality
- Channel Manager
- Hotel Distribution
- OTA
- Booking
website: https://channex.io/
---
