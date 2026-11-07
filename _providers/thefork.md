---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Thefork Agentic Access
  operation_count: 29
  slug: thefork-agentic-access
  summary_line: 29 operations · 14 acting · 1 human-in-the-loop
api_count: 7
apis:
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: Look up customer and guest profile data.
  name: TheFork Customers API
  slug: thefork-customers-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: Open and close point-of-sale orders tied to reservations.
  name: TheFork Orders API
  slug: thefork-orders-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: Create, retrieve, and update reservations.
  name: TheFork Reservations API
  slug: thefork-reservations-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: Retrieve guest review details.
  name: TheFork Reviews API
  slug: thefork-reviews-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Booking flow API from TheFork — 8 operation(s) for booking flow.
  name: TheFork Booking flow API
  slug: thefork-booking-flow-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Create API from TheFork — 1 operation(s) for create.
  name: TheFork Create API
  slug: thefork-create-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Data API from TheFork — 4 operation(s) for data.
  name: TheFork Data API
  slug: thefork-data-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Logo API from TheFork — 1 operation(s) for logo.
  name: TheFork Logo API
  slug: thefork-logo-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Phone API from TheFork — 3 operation(s) for phone.
  name: TheFork Phone API
  slug: thefork-phone-api
- baseURL: https://api.thefork.io
  baseurl_source: declared
  description: The Review flow API from TheFork — 3 operation(s) for review flow.
  name: TheFork Review flow API
  slug: thefork-review-flow-api
artifact_total: 71
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
  name: TheFork B2B Customers API
  slug: open-thefork-customers-api
- collection_type: open
  name: TheFork B2B Customers Orders API
  slug: open-thefork-orders-api
- collection_type: open
  name: TheFork POS API
  slug: open-thefork-pos
- collection_type: open
  name: TheFork B2B Customers Reservations API
  slug: open-thefork-reservations-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thefork/overview
- group: agent
  href: https://artifacts.apis.io/thefork/agentic-access/thefork-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thefork-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/thefork/security/thefork-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thefork-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/thefork/authentication/thefork-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thefork-authentication.yml
- group: auth
  href: https://artifacts.apis.io/thefork/scopes/thefork-scopes.yml
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
  href: https://artifacts.apis.io/thefork/rules/thefork-rules.yml
  title: ''
  type: SpectralRules
  url: rules/thefork-rules.yml
- group: design
  href: https://artifacts.apis.io/thefork/vocabulary/thefork-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thefork-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/thefork/json-ld/thefork-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thefork-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/thefork/plans/thefork-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thefork-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/thefork/rate-limits/thefork-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thefork-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thefork/finops/thefork-finops.yml
  title: ''
  type: FinOps
  url: finops/thefork-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thefork.io/B2B-API/API%20specifications/get-v-1-customers
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
- has_sources: true
  method: generated
  name: Thefork Finops
  primary_unit: ''
  service_category: Restaurant Reservations
  slug: thefork-finops
  template: false
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
overview: 'TheFork publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Customers API, Orders API, Reservations API, and 7 more. Tagged areas include Restaurant, Reservations, Booking, Dining, and Point-of-Sale.


  The TheFork catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  TheFork''s developer surface includes authentication, documentation, developer portal, getting-started guide, signup flow, engineering blog, API reference, and 13 more developer resources.'
plans:
- name: Thefork Plans Pricing
  plan_count: 1
  slug: thefork-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Thefork Rate Limits
  slug: thefork-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: TheFork — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: thefork-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 11
  extends: []
  name: TheFork API Rules
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
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 71.8
    catalog_earned_first_party: 0.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 23.5
    contract_quality: 41.6
    developer_ergonomics: 53.6
    discoverability: 71.4
    operational_transparency: 15.8
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 70.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thefork/thefork-2026-06-20T195245.png
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
- Point-of-Sale
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
