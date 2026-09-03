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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Airbnb Agentic Access
  operation_count: 34
  slug: airbnb-agentic-access
  summary_line: 34 operations · 19 acting
api_count: 2
apis:
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: The Airbnb Webhooks API enables connectivity partners to receive real-time notifications when events occur on the Airbnb platform. It supports webhook subscriptions for reservation changes, message cr
  name: Airbnb Webhooks API
  slug: webhooks-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for managing guest bookings for experiences, including confirmations, cancellations, and attendee details.
  name: airbnb Bookings API
  slug: airbnb-bookings-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for managing listing availability, pricing, and calendar synchronization across platforms.
  name: airbnb Calendar API
  slug: airbnb-calendar-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for sending and retrieving messages between experience hosts and booked guests.
  name: airbnb Experience Messages API
  slug: airbnb-experience-messages-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for creating, reading, updating, and managing experience and activity listings on Airbnb.
  name: airbnb Experiences API
  slug: airbnb-experiences-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for creating, reading, updating, and managing property listings on Airbnb, including descriptions, amenities, and photos.
  name: airbnb Listings API
  slug: airbnb-listings-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for sending and retrieving guest and host messages within reservation threads.
  name: airbnb Messages API
  slug: airbnb-messages-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for uploading, updating, and managing listing photos.
  name: airbnb Photos API
  slug: airbnb-photos-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for managing reservations, including accepting, declining, and retrieving booking details.
  name: airbnb Reservations API
  slug: airbnb-reservations-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for retrieving and responding to guest and host reviews.
  name: airbnb Reviews API
  slug: airbnb-reviews-api
- baseURL: https://api.airbnb.com
  baseurl_source: declared
  description: Operations for managing experience schedules, time slots, and availability for hosted activities.
  name: airbnb Schedules API
  slug: airbnb-schedules-api
artifact_total: 115
asyncapis:
- description: The Airbnb Webhooks API enables connectivity partners to receive real-time notifications when events occur on the Airbnb platform. It supports webhook subscriptions for reservation changes, message cr
  name: Airbnb Webhooks API
  slug: airbnb-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airbnb Activities API
  slug: open-airbnb-activities-api
- collection_type: open
  name: Airbnb Activities Bookings API
  slug: open-airbnb-bookings-api
- collection_type: open
  name: Airbnb Activities Bookings Calendar API
  slug: open-airbnb-calendar-api
- collection_type: open
  name: Airbnb Activities Bookings Experience Messages API
  slug: open-airbnb-experience-messages-api
- collection_type: open
  name: Airbnb Activities Bookings Experiences API
  slug: open-airbnb-experiences-api
- collection_type: open
  name: Airbnb Homes API
  slug: open-airbnb-homes-api
- collection_type: open
  name: Airbnb Activities Bookings Listings API
  slug: open-airbnb-listings-api
- collection_type: open
  name: Airbnb Activities Bookings Messages API
  slug: open-airbnb-messages-api
- collection_type: open
  name: Airbnb Activities Bookings Photos API
  slug: open-airbnb-photos-api
- collection_type: open
  name: Airbnb Activities Bookings Reservations API
  slug: open-airbnb-reservations-api
- collection_type: open
  name: Airbnb Activities Bookings Schedules API
  slug: open-airbnb-schedules-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/airbnb-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airbnb-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airbnb-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airbnb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airbnb-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airbnb-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.airbnb.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.withairbnb.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/airbnb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-listing-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-reservation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-webhook-event-schema.json
- group: company
  title: ''
  type: Blog
  url: https://www.airbnb.com/resources/hosting-homes/a/airbnb-newsroom
- group: build
  title: ''
  type: GitHub
  url: https://github.com/airbnb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airbnb
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/airbnb
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.airbnb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.airbnb.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://airbnb.statuspage.io/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-address-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-booking-guest-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-booking-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-calendar-day-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-calendar-operation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-create-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-host-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-location-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-photo-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-pricing-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-experience-update-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-guest-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-listing-create-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-listing-update-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-photo-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-pricing-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-review-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-schedule-create-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-schedule-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/airbnb-schedule-update-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-address-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-booking-guest-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-booking-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-calendar-day-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-calendar-operation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-create-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-host-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-location-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-photo-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-pricing-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-experience-update-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-guest-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-listing-create-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-listing-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-listing-update-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-message-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-photo-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-pricing-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-reservation-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-review-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-schedule-create-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-schedule-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-schedule-update-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/airbnb-webhook-event-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-address-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-booking-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-booking-guest-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-calendar-day-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-calendar-operation-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-create-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-host-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-location-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-message-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-photo-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-pricing-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-experience-update-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-guest-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-listing-create-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-listing-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-listing-update-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-message-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-photo-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-pricing-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-reservation-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-review-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-schedule-create-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-schedule-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-schedule-update-example.json
- group: build
  title: ''
  type: Examples
  url: examples/airbnb-webhook-event-example.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/airbnb-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/airbnb-vocabulary.yaml
description: Airbnb is the world's leading home-sharing and short-term rental marketplace, connecting hosts who offer accommodations and experiences with guests worldwide. The Airbnb developer platform provides connectivity partners — property management systems, channel managers, and experience operators — with APIs to manage listings, reservations, calendars, messaging, reviews, and webhook-based event notifications. Access is restricted to approved partners.
examples:
- key_count: 7
  name: Airbnb Address Example
  slug: airbnb-address-example
- key_count: 9
  name: Airbnb Booking Example
  slug: airbnb-booking-example
- key_count: 5
  name: Airbnb Booking Guest Example
  slug: airbnb-booking-guest-example
- key_count: 6
  name: Airbnb Calendar Day Example
  slug: airbnb-calendar-day-example
- key_count: 6
  name: Airbnb Calendar Operation Example
  slug: airbnb-calendar-operation-example
- key_count: 10
  name: Airbnb Experience Create Example
  slug: airbnb-experience-create-example
- key_count: 9
  name: Airbnb Experience Example
  slug: airbnb-experience-example
- key_count: 5
  name: Airbnb Experience Host Example
  slug: airbnb-experience-host-example
- key_count: 6
  name: Airbnb Experience Location Example
  slug: airbnb-experience-location-example
- key_count: 5
  name: Airbnb Experience Message Example
  slug: airbnb-experience-message-example
- key_count: 4
  name: Airbnb Experience Photo Example
  slug: airbnb-experience-photo-example
- key_count: 3
  name: Airbnb Experience Pricing Example
  slug: airbnb-experience-pricing-example
- key_count: 10
  name: Airbnb Experience Update Example
  slug: airbnb-experience-update-example
- key_count: 7
  name: Airbnb Guest Example
  slug: airbnb-guest-example
- key_count: 14
  name: Airbnb Listing Create Example
  slug: airbnb-listing-create-example
- key_count: 12
  name: Airbnb Listing Example
  slug: airbnb-listing-example
- key_count: 13
  name: Airbnb Listing Update Example
  slug: airbnb-listing-update-example
- key_count: 6
  name: Airbnb Message Example
  slug: airbnb-message-example
- key_count: 6
  name: Airbnb Photo Example
  slug: airbnb-photo-example
- key_count: 5
  name: Airbnb Pricing Example
  slug: airbnb-pricing-example
- key_count: 10
  name: Airbnb Reservation Example
  slug: airbnb-reservation-example
- key_count: 7
  name: Airbnb Review Example
  slug: airbnb-review-example
- key_count: 3
  name: Airbnb Schedule Create Example
  slug: airbnb-schedule-create-example
- key_count: 9
  name: Airbnb Schedule Example
  slug: airbnb-schedule-example
- key_count: 3
  name: Airbnb Schedule Update Example
  slug: airbnb-schedule-update-example
- key_count: 5
  name: Airbnb Webhook Event Example
  slug: airbnb-webhook-event-example
finops:
- name: Airbnb Finops
  service_category: Hospitality Marketplace
  slug: airbnb-finops
graphqls:
- description: 'This is a conceptual GraphQL schema for the Airbnb platform, covering the core domains of the Airbnb partner API: listings, reservations, calendars, pricing, guests, hosts, messaging, reviews, experie'
  name: Airbnb GraphQL Schema
  slug: airbnb-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airbnb.png
json_schemas:
- name: Address
  property_count: 7
  slug: airbnb-address
- name: BookingGuest
  property_count: 5
  slug: airbnb-booking-guest
- name: Booking
  property_count: 12
  slug: airbnb-booking
- name: CalendarDay
  property_count: 6
  slug: airbnb-calendar-day
- name: CalendarOperation
  property_count: 6
  slug: airbnb-calendar-operation
- name: ExperienceCreate
  property_count: 10
  slug: airbnb-experience-create
- name: ExperienceHost
  property_count: 5
  slug: airbnb-experience-host
- name: ExperienceLocation
  property_count: 6
  slug: airbnb-experience-location
- name: ExperienceMessage
  property_count: 5
  slug: airbnb-experience-message
- name: ExperiencePhoto
  property_count: 4
  slug: airbnb-experience-photo
- name: ExperiencePricing
  property_count: 3
  slug: airbnb-experience-pricing
- name: Experience
  property_count: 16
  slug: airbnb-experience
- name: ExperienceUpdate
  property_count: 10
  slug: airbnb-experience-update
- name: Guest
  property_count: 6
  slug: airbnb-guest
- name: ListingCreate
  property_count: 14
  slug: airbnb-listing-create
- name: Listing
  property_count: 20
  slug: airbnb-listing
- name: ListingUpdate
  property_count: 13
  slug: airbnb-listing-update
- name: Message
  property_count: 5
  slug: airbnb-message
- name: Photo
  property_count: 6
  slug: airbnb-photo
- name: Pricing
  property_count: 6
  slug: airbnb-pricing
- name: Reservation
  property_count: 14
  slug: airbnb-reservation
- name: Review
  property_count: 8
  slug: airbnb-review
- name: ScheduleCreate
  property_count: 3
  slug: airbnb-schedule-create
- name: Schedule
  property_count: 9
  slug: airbnb-schedule
- name: ScheduleUpdate
  property_count: 3
  slug: airbnb-schedule-update
- name: Airbnb Webhook Event
  property_count: 5
  slug: airbnb-webhook-event
json_structures:
- name: Airbnb Address Structure
  property_count: 0
  slug: airbnb-address-structure
- name: Airbnb Booking Guest Structure
  property_count: 0
  slug: airbnb-booking-guest-structure
- name: Airbnb Booking Structure
  property_count: 0
  slug: airbnb-booking-structure
- name: Airbnb Calendar Day Structure
  property_count: 0
  slug: airbnb-calendar-day-structure
- name: Airbnb Calendar Operation Structure
  property_count: 0
  slug: airbnb-calendar-operation-structure
- name: Airbnb Experience Create Structure
  property_count: 0
  slug: airbnb-experience-create-structure
- name: Airbnb Experience Host Structure
  property_count: 0
  slug: airbnb-experience-host-structure
- name: Airbnb Experience Location Structure
  property_count: 0
  slug: airbnb-experience-location-structure
- name: Airbnb Experience Message Structure
  property_count: 0
  slug: airbnb-experience-message-structure
- name: Airbnb Experience Photo Structure
  property_count: 0
  slug: airbnb-experience-photo-structure
- name: Airbnb Experience Pricing Structure
  property_count: 0
  slug: airbnb-experience-pricing-structure
- name: Airbnb Experience Structure
  property_count: 0
  slug: airbnb-experience-structure
- name: Airbnb Experience Update Structure
  property_count: 0
  slug: airbnb-experience-update-structure
- name: Airbnb Guest Structure
  property_count: 0
  slug: airbnb-guest-structure
- name: Airbnb Listing Create Structure
  property_count: 0
  slug: airbnb-listing-create-structure
- name: Airbnb Listing Structure
  property_count: 0
  slug: airbnb-listing-structure
- name: Airbnb Listing Update Structure
  property_count: 0
  slug: airbnb-listing-update-structure
- name: Airbnb Message Structure
  property_count: 0
  slug: airbnb-message-structure
- name: Airbnb Photo Structure
  property_count: 0
  slug: airbnb-photo-structure
- name: Airbnb Pricing Structure
  property_count: 0
  slug: airbnb-pricing-structure
- name: Airbnb Reservation Structure
  property_count: 0
  slug: airbnb-reservation-structure
- name: Airbnb Review Structure
  property_count: 0
  slug: airbnb-review-structure
- name: Airbnb Schedule Create Structure
  property_count: 0
  slug: airbnb-schedule-create-structure
- name: Airbnb Schedule Structure
  property_count: 0
  slug: airbnb-schedule-structure
- name: Airbnb Schedule Update Structure
  property_count: 0
  slug: airbnb-schedule-update-structure
- name: Airbnb Webhook Event Structure
  property_count: 0
  slug: airbnb-webhook-event-structure
jsonld:
- class_count: 0
  name: Airbnb Context
  property_count: 34
  slug: airbnb-context
layout: provider
modified: '2026-05-19'
name: Airbnb
nav: Providers
network: true
overview: 'Airbnb publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Bookings API, Calendar API, and 8 more.


  The Airbnb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Airbnb''s developer surface includes authentication, developer portal, engineering blog, GitHub presence, code examples, and 91 more developer resources.'
plans:
- name: Airbnb Plans Pricing
  plan_count: 5
  slug: airbnb-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Airbnb Rate Limits
  slug: airbnb-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Airbnb API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: airbnb-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Airbnb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airbnb-jsonschema-spectral-rules
- effective_rule_count: 67
  extends:
  - spectral:oas
  name: Airbnb API Rules
  rule_count: 26
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 20
  slug: airbnb-spectral-rules
scopes:
- name: Airbnb Scopes
  scope_count: 13
  slug: airbnb-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 44.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 28.8
    contract_quality: 77.9
    developer_ergonomics: 26.2
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/screenshots/airbnb-2026-06-20T171418.png
security:
- kind: authentication
  name: Airbnb Authentication
  slug: airbnb-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Airbnb Domain Security
  slug: airbnb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airbnb Vulnerability Disclosure
  slug: airbnb-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: airbnb
website: https://www.airbnb.com/
---
