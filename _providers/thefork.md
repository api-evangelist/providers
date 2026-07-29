---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Thefork Agentic Access
  operation_count: 8
  slug: thefork-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: Look up customer and guest profile data.
  name: TheFork Customers API
  slug: thefork-customers-api
- description: Open and close point-of-sale orders tied to reservations.
  name: TheFork Orders API
  slug: thefork-orders-api
- description: Create, retrieve, and update reservations.
  name: TheFork Reservations API
  slug: thefork-reservations-api
- description: Retrieve guest review details.
  name: TheFork Reviews API
  slug: thefork-reviews-api
artifact_total: 62
collections:
- collection_type: postman
  name: TheFork B2B Customers API
  slug: postman-thefork-customers-api
- collection_type: postman
  name: TheFork B2B Customers Orders API
  slug: postman-thefork-orders-api
- collection_type: postman
  name: TheFork B2B Customers Reservations API
  slug: postman-thefork-reservations-api
- collection_type: postman
  name: TheFork B2B Customers Reviews API
  slug: postman-thefork-reviews-api
- collection_type: open
  name: TheFork B2B API
  slug: open-thefork-b2b
- collection_type: open
  name: TheFork POS API
  slug: open-thefork-pos
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thefork/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thefork-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thefork-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thefork-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thefork-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.thefork.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thefork.io/
- group: start
  title: ''
  type: Portal
  url: https://docs.thefork.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thefork.io/getting-started
- group: start
  title: ''
  type: Signup
  url: https://docs.thefork.io/preliminary-steps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.thefork.io/pdf/LaFourchette-Partners-API-Licence-2.pdf
- group: company
  title: ''
  type: Blog
  url: https://medium.com/thefork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lafourchette
- group: design
  title: ''
  type: SpectralRules
  url: rules/thefork-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/thefork-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/thefork-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/thefork-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thefork-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/thefork-finops.yml
created: '2026-06-02'
description: TheFork is a leading European restaurant reservations marketplace, part of Tripadvisor, connecting diners with tens of thousands of restaurants across Europe and beyond. Through its developers portal, TheFork exposes a public REST API surface for restaurants, point-of-sale systems, and third-party partners to integrate with TheFork Management platform. The API enables partners to build custom booking flows, create and manage reservations with full detail such as meal date, party size, and customer data, surface preset menus and curated dining experiences, and access personalized guest data including allergies, dietary restrictions, and seating preferences. Offerings include a B2B API for restaurants and a POS API for point-of-sale providers.
examples:
- key_count: 2
  name: Thefork B2B Create Reservation Example
  slug: thefork-b2b-create-reservation-example
- key_count: 2
  name: Thefork B2B Find Customer By Phone Example
  slug: thefork-b2b-find-customer-by-phone-example
- key_count: 2
  name: Thefork B2B Get Reservation Example
  slug: thefork-b2b-get-reservation-example
- key_count: 2
  name: Thefork B2B Get Review Example
  slug: thefork-b2b-get-review-example
- key_count: 2
  name: Thefork Pos Create Order Example
  slug: thefork-pos-create-order-example
features:
- description: Build a custom booking flow with real-time availability, offers, and preset menus, then create reservations directly against a restaurant.
  name: Custom Booking Funnel
- description: Create, retrieve, and update reservations including meal date, party size, and customer data.
  name: Reservation Management
- description: Access personalized guest data such as allergies, intolerances, dietary restrictions, and seating preferences.
  name: Guest Profiles
- description: Find customer details by phone number for a given restaurant.
  name: Customer Lookup
- description: Retrieve guest review details by review UUID.
  name: Reviews
- description: Synchronize data without requiring real-time updates, using webhooks for reservation created and updated events.
  name: Asynchronous Data Sync
- description: Open and close point-of-sale orders tied to reservations and sync final amounts back to TheFork Management.
  name: POS Order Sync
finops:
- name: Thefork Finops
  service_category: Restaurant Reservations
  slug: thefork-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thefork.png
integrations:
- description: The restaurant management platform the APIs synchronize with.
  name: TheFork Management (TFM)
- description: Parent company; TheFork is part of the Tripadvisor group.
  name: Tripadvisor
- description: Identity provider issuing OAuth 2.0 client credentials tokens.
  name: Auth0
- description: API gateway fronting the public API with auth, rate limiting, and IP allowlisting.
  name: Kong
json_schemas:
- name: CustomerInput
  property_count: 4
  slug: thefork-b2b-customer-input
- name: Customer
  property_count: 8
  slug: thefork-b2b-customer
- name: Offer
  property_count: 4
  slug: thefork-b2b-offer
- name: ReservationCreateRequest
  property_count: 6
  slug: thefork-b2b-reservation-create-request
- name: Reservation
  property_count: 9
  slug: thefork-b2b-reservation
- name: ReservationStatus
  property_count: 0
  slug: thefork-b2b-reservation-status
- name: ReservationUpdateRequest
  property_count: 2
  slug: thefork-b2b-reservation-update-request
- name: Review
  property_count: 6
  slug: thefork-b2b-review
- name: Customer
  property_count: 5
  slug: thefork-pos-customer
- name: Money
  property_count: 2
  slug: thefork-pos-money
- name: Offer
  property_count: 4
  slug: thefork-pos-offer
- name: OrderClose
  property_count: 2
  slug: thefork-pos-order-close
- name: Order
  property_count: 9
  slug: thefork-pos-order
- name: ReservationStatus
  property_count: 0
  slug: thefork-pos-reservation-status
- name: Table
  property_count: 2
  slug: thefork-pos-table
json_structures:
- name: Thefork B2B Reservation Structure
  property_count: 9
  slug: thefork-b2b-reservation-structure
- name: Thefork Pos Order Structure
  property_count: 9
  slug: thefork-pos-order-structure
jsonld:
- class_count: 8
  name: Thefork B2B Context
  property_count: 26
  slug: thefork-b2b-context
- class_count: 12
  name: Thefork Context
  property_count: 36
  slug: thefork-context
- class_count: 7
  name: Thefork Pos Context
  property_count: 23
  slug: thefork-pos-context
layout: provider
modified: '2026-06-03'
name: TheFork
nav: Providers
network: true
overview: 'TheFork publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Orders API, Reservations API, and 1 more. Tagged areas include Restaurant, Reservations, Booking, Dining, and Point Of Sale.


  The TheFork catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  TheFork''s developer surface includes authentication, documentation, developer portal, getting-started guide, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Thefork Plans Pricing
  plan_count: 1
  slug: thefork-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Thefork Rate Limits
  slug: thefork-rate-limits
rules:
- name: TheFork API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: thefork-jsonschema-spectral-rules
- name: TheFork API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: thefork-rules
scopes:
- name: Thefork Scopes
  scope_count: 0
  slug: thefork-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.4
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 80.9
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 60.1
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
screenshot: https://raw.githubusercontent.com/api-evangelist/thefork/refs/heads/main/screenshots/thefork-2026-06-20T195245.png
security:
- kind: authentication
  name: Thefork Authentication
  slug: thefork-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Thefork Domain Security
  slug: thefork-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thefork
solutions:
- description: B2B API for restaurants and groups to manage bookings and guests.
  name: For Restaurants
- description: POS API for point-of-sale vendors to sync orders and reservations.
  name: For POS Providers
- description: Partner API for third-party partners (announced as available soon).
  name: For Partners
tags:
- Restaurant
- Reservations
- Booking
- Dining
- Point Of Sale
- Marketplace
use_cases:
- description: Restaurants and groups embed TheFork availability and booking into their own websites and apps.
  name: Restaurant Booking Integration
- description: Point-of-sale vendors connect their systems to reflect seated guests, open tickets, and reconcile spend with reservations.
  name: POS Integration
- description: Use allergy, dietary, and seating preferences to personalize the dining experience and pre-service preparation.
  name: Guest Personalization
- description: Pull guest reviews into restaurant CRM and reputation tooling.
  name: Review Aggregation
website: https://www.thefork.com
---
