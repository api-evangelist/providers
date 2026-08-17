---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Hostaway Agentic Access
  operation_count: 23
  slug: hostaway-agentic-access
  summary_line: 23 operations · 11 acting
api_count: 16
apis:
- description: Manage vacation rental listings — properties, amenities, bed types, images, and custom field values. Each Hostaway listing maps to one or more external channels (Airbnb, Vrbo, Booking.com, Expedia, Go
  name: Hostaway Listings API
  slug: hostaway-listings-api
- description: Create, read, and update reservations across all connected channels. Includes coupons, reservation fees, reservation units, host proxy email handling, and channel-of-origin context (channelId/channelN
  name: Hostaway Reservations API
  slug: hostaway-reservations-api
- description: Read and update the per-listing availability and nightly pricing calendar. Supports per-day retrieval, batch updates across date ranges, and inline reservation context via the includeResources query p
  name: Hostaway Calendar API
  slug: hostaway-calendar-api
- description: Unified guest messaging across Airbnb, Vrbo, Booking.com, Expedia, email, SMS, and WhatsApp. Resources include conversations, conversation messages, and reusable message templates.
  name: Hostaway Messaging API
  slug: hostaway-messaging-api
- description: Financial operations for vacation rental managers — finance fields, price calculations, expenses and extras, offline charges, and owner statements.
  name: Hostaway Finance API
  slug: hostaway-finance-api
- description: Create, assign, and complete operational tasks (cleaning, maintenance, inspection) tied to listings and reservations.
  name: Hostaway Tasks API
  slug: hostaway-tasks-api
- description: Define and manage custom fields on listings and reservations, plus retrieve and set custom field values on individual records.
  name: Hostaway Custom Fields API
  slug: hostaway-custom-fields-api
- description: Manage guest payments and auto-payment rules for reservations.
  name: Hostaway Guest Payments API
  slug: hostaway-guest-payments-api
- description: Reference-data endpoints for cancellation policies (Airbnb, Vrbo, Booking.com, Marriott), countries, currencies, languages, and timezones.
  name: Hostaway Reference Data API
  slug: hostaway-reference-data-api
- description: Manage unified webhooks for the three Hostaway event types — reservation created, reservation updated, and new message received. Failed deliveries retry up to three times before a failure email is sen
  name: Hostaway Webhooks API
  slug: hostaway-webhooks-api
- description: Amenities offered by a listing
  name: Hostaway Listing Amenities API
  slug: hostaway-listing-amenities-api
- description: Bed types configured for a listing
  name: Hostaway Listing Bed Types API
  slug: hostaway-listing-bed-types-api
- description: Photographs attached to a listing
  name: Hostaway Listing Images API
  slug: hostaway-listing-images-api
- description: Coupons applied to a reservation
  name: Hostaway Reservation Coupons API
  slug: hostaway-reservation-coupons-api
- description: Fees applied to a reservation
  name: Hostaway Reservation Fees API
  slug: hostaway-reservation-fees-api
- description: Sub-units associated with a reservation
  name: Hostaway Reservation Units API
  slug: hostaway-reservation-units-api
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hostaway Calendar API
  slug: open-hostaway-calendar-api
- collection_type: open
  name: Hostaway Calendar Listing Amenities API
  slug: open-hostaway-listing-amenities-api
- collection_type: open
  name: Hostaway Calendar Listing Bed Types API
  slug: open-hostaway-listing-bed-types-api
- collection_type: open
  name: Hostaway Calendar Listing Images API
  slug: open-hostaway-listing-images-api
- collection_type: open
  name: Hostaway Calendar Listings API
  slug: open-hostaway-listings-api
- collection_type: open
  name: Hostaway Calendar Reservation Coupons API
  slug: open-hostaway-reservation-coupons-api
- collection_type: open
  name: Hostaway Calendar Reservation Fees API
  slug: open-hostaway-reservation-fees-api
- collection_type: open
  name: Hostaway Calendar Reservation Units API
  slug: open-hostaway-reservation-units-api
- collection_type: open
  name: Hostaway Calendar Reservations API
  slug: open-hostaway-reservations-api
- collection_type: open
  name: Hostaway Calendar Webhooks API
  slug: open-hostaway-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hostaway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hostaway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hostaway-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hostaway-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.hostaway.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.hostaway.com/documentation
- group: start
  title: ''
  type: Signup
  url: https://dashboard.hostaway.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.hostaway.com/settings/integrations
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hostaway.com/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hostaway.com/get-free-demo/
- group: docs
  title: ''
  type: Documentation
  url: https://www.hostaway.com/features/
- group: company
  title: ''
  type: Blog
  url: https://www.hostaway.com/blog/
- group: other
  title: ''
  type: Marketplace
  url: https://www.hostaway.com/marketplace/
- group: company
  title: ''
  type: Partners
  url: https://www.hostaway.com/partners/
- group: company
  title: ''
  type: About
  url: https://www.hostaway.com/about-us/
- group: operate
  title: ''
  type: Support
  url: https://www.hostaway.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hostaway.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hostaway.com/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hostaway
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/hostawaycom
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hostawaycom
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/hostawaycom/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@hostaway
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Hostaway
- group: commercial
  title: ''
  type: Plans
  url: https://plans/hostaway-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/hostaway-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/hostaway-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: other
  title: ''
  type: Channels
  url: ''
- group: other
  title: ''
  type: Recognition
  url: ''
created: '2026-05-25'
description: Hostaway is an AI-powered vacation rental management platform that consolidates property management, channel management, direct booking, guest messaging, automation, and revenue optimization for short-term rental operators. The platform connects to Airbnb, Vrbo, Booking.com, Expedia, Google Vacation Rentals, and Marriott Homes & Villas, and exposes a documented OAuth 2.0 public REST API at https://api.hostaway.com/v1 covering listings, reservations, calendar, messaging, finance, tasks, custom fields, guest payments, and unified webhooks. Pricing is quote-based; a free product demo is available. The Hostaway Marketplace contains 100+ integrated vendors spanning revenue management, operations, smart locks, payments, and accounting.
features:
- Channel manager for Airbnb, Vrbo, Booking.com, Expedia, Google Vacation Rentals, and Marriott Homes & Villas
- Unified inbox across email, SMS, WhatsApp, and channel-native messaging
- Listing and reservation management with custom fields
- Calendar with per-day pricing, minimum stay, batch updates, and inline reservation context
- Owner statements, finance fields, expenses & extras, offline charges
- Price calculation engine with coupons and per-channel fee modeling
- Automation rules and tasks (cleaning, maintenance, inspection)
- Direct booking website
- Guest payments and auto-payment rules
- Marketplace with 100+ integrated vendors (Pricelabs, Wheelhouse, Beyond, Breezeway, Turno, Operto, RemoteLock, QuickBooks, Stripe, etc.)
- Unified webhooks for reservation created, reservation updated, and new message received
- Reference data for cancellation policies (Airbnb, Vrbo, Booking.com, Marriott), countries, currencies, languages, timezones
- Public REST API at https://api.hostaway.com/v1 with OAuth 2.0 client_credentials
- Documented rate limits — 15 req/10s per IP and 20 req/10s per account
- Standard envelope response with status, result, and pagination (limit, offset, count, page, totalPages)
- HTTPS-only, JSON request/response, UTC timestamps, ISO 3166-2 country codes, booleans as 0/1
finops:
- name: Hostaway Finops
  service_category: Software as a Service
  slug: hostaway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hostaway.png
integrations:
- Pricelabs, Wheelhouse, Beyond, DPGO — revenue management
- Breezeway, Turno, Operto, Doinn — property operations and cleaning
- Safely, Autohost, Truvi — guest screening and safety
- RemoteLock, August, Yale, Nuki, Schlage — smart locks
- Stripe, Braintree, ChargeAutomation, Authorize.net — payments
- QuickBooks, Ximplifi, Clearing — accounting
- Slack, WhatsApp, Zapier — communication
- Lula Cleaning, Keepers, Tidy, Pacho — cleaning and maintenance
json_schemas:
- name: Hostaway Listing
  property_count: 23
  slug: hostaway-listing
- name: Hostaway Reservation
  property_count: 20
  slug: hostaway-reservation
jsonld:
- class_count: 0
  name: Hostaway Context
  property_count: 4
  slug: hostaway-context
layout: provider
modified: '2026-05-25'
name: Hostaway
nav: Providers
network: true
overview: 'Hostaway publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Listings API, Reservations API, Calendar API, and 7 more. Tagged areas include Vacation Rentals, Short-Term Rentals, Property Management, Channel Manager, and Airbnb.


  The Hostaway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hostaway''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Hostaway Plans Pricing
  plan_count: 2
  slug: hostaway-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 2
  name: Hostaway Rate Limits
  slug: hostaway-rate-limits
rules:
- name: Hostaway API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hostaway-jsonschema-spectral-rules
scopes:
- name: Hostaway Scopes
  scope_count: 1
  slug: hostaway-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: strong
  composite: 56.6
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 63.4
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hostaway/refs/heads/main/screenshots/hostaway-2026-06-20T182839.png
security:
- kind: authentication
  name: Hostaway Authentication
  slug: hostaway-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Hostaway Domain Security
  slug: hostaway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hostaway
tags:
- Vacation Rentals
- Short-Term Rentals
- Property Management
- Channel Manager
- Airbnb
- Vrbo
- Booking.com
- Expedia
- SaaS
website: https://www.hostaway.com
---
