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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Booking Holdings Agentic Access
  operation_count: 39
  slug: booking-holdings-agentic-access
  summary_line: 39 operations · 39 acting
api_count: 9
apis:
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: 'This API collection is specific for the stay part of the connected trip. </br></br>Use these endpoints to search for stays such as hotels and apartments, check availability, retrieve reviews, and get '
  name: Booking Holdings Accommodations API
  slug: booking-holdings-accommodations-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Provides endpoints for handling message attachments. </br></br>Use these endpoints to upload and download images shared within conversations.
  name: Booking Holdings Attachments API
  slug: booking-holdings-attachments-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: This API collection is specific to the car rentals part of the connected trip.</br></br> Use these endpoints to search for car rentals, check car details and look for depots and suppliers.
  name: Booking Holdings Cars API
  slug: booking-holdings-cars-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Provides a list of supported language codes for use in API requests.
  name: Booking Holdings Common/languages API
  slug: booking-holdings-common-languages-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: 'Provides identifiers for a wide range of geographical locations, including airports, countries, cities, and regions. </br></br>Use these identifiers to construct your requests. </br></br>Note: These i'
  name: Booking Holdings Common/locations API
  slug: booking-holdings-common-locations-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Provides generic payment-related endpoints, including supported currencies and payment types.
  name: Booking Holdings Common/payments API
  slug: booking-holdings-common-payments-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Provides endpoints to retrieve and manage messaging conversations. </br></br>Use these endpoints to list conversations, fetch conversation details, and track updates.
  name: Booking Holdings Conversations API
  slug: booking-holdings-conversations-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Provides endpoints for two-way post-booking communication between guests and properties. </br></br>Use these endpoints to send and retrieve messages, exchange images, and check conversation details.
  name: Booking Holdings Messages API
  slug: booking-holdings-messages-api
- baseURL: https://demandapi.booking.com/3.1
  baseurl_source: declared
  description: Enables management of booking orders within the Demand API. </br></br>Use these endpoints to preview and create new orders, check order details, cancel or modify existing orders. This collection is re
  name: Booking Holdings Orders API
  slug: booking-holdings-orders-api
artifact_total: 104
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Booking.com Demand Accommodations API
  slug: open-booking-holdings-accommodations-api
- collection_type: open
  name: Booking.com Demand Accommodations Attachments API
  slug: open-booking-holdings-attachments-api
- collection_type: open
  name: Booking.com Demand Accommodations Cars API
  slug: open-booking-holdings-cars-api
- collection_type: open
  name: Booking.com Demand Accommodations Common/languages API
  slug: open-booking-holdings-common-languages-api
- collection_type: open
  name: Booking.com Demand Accommodations Common/locations API
  slug: open-booking-holdings-common-locations-api
- collection_type: open
  name: Booking.com Demand Accommodations Common/payments API
  slug: open-booking-holdings-common-payments-api
- collection_type: open
  name: Booking.com Demand Accommodations Conversations API
  slug: open-booking-holdings-conversations-api
- collection_type: open
  name: Booking.com Demand Accommodations Messages API
  slug: open-booking-holdings-messages-api
- collection_type: open
  name: Booking.com Demand Accommodations Orders API
  slug: open-booking-holdings-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/booking-holdings-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/booking-holdings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/booking-holdings-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bookingholdings
- group: company
  title: ''
  type: Website
  url: https://www.bookingholdings.com
- group: company
  title: ''
  type: About
  url: https://www.bookingholdings.com/about/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.bookingholdings.com
- group: company
  title: ''
  type: Careers
  url: https://www.bookingholdings.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.bookingholdings.com/contact/
- group: commercial
  title: ''
  type: Plans
  url: plans/booking-holdings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/booking-holdings-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/booking-holdings-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/booking-com-demand-api-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/booking-holdings-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/booking-holdings-demand-api-context.jsonld
- group: build
  title: Booking.com
  type: GitHubOrganization
  url: https://github.com/bookingcom
- group: build
  title: OpenTable
  type: GitHubOrganization
  url: https://github.com/opentable
- group: build
  title: KAYAK
  type: GitHubOrganization
  url: https://github.com/kayak
- group: other
  title: ''
  type: Properties
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.bookingholdings.com/feed/
created: '2024-01-01'
description: Booking Holdings is the world's leading provider of online travel and related services, operating a portfolio of brands including Booking.com, Priceline, Agoda, KAYAK, OpenTable, Rentalcars.com, Rocketmiles, FareHarbor, HotelsCombined, Cheapflights, and Momondo. The company connects travelers with accommodations, flights, rental cars, restaurant reservations, and travel experiences worldwide.
examples:
- key_count: 5
  name: Demand Api Accommodations Availability Input Example
  slug: demand-api-accommodations-availability-input-example
- key_count: 6
  name: Demand Api Accommodations Availability Product Output Example
  slug: demand-api-accommodations-availability-product-output-example
- key_count: 6
  name: Demand Api Accommodations Details Data Output Example
  slug: demand-api-accommodations-details-data-output-example
- key_count: 6
  name: Demand Api Accommodations Details Input Example
  slug: demand-api-accommodations-details-input-example
- key_count: 6
  name: Demand Api Accommodations Details Room Output Example
  slug: demand-api-accommodations-details-room-output-example
- key_count: 6
  name: Demand Api Accommodations Location Output Example
  slug: demand-api-accommodations-location-output-example
- key_count: 6
  name: Demand Api Accommodations Policies Output Example
  slug: demand-api-accommodations-policies-output-example
- key_count: 6
  name: Demand Api Accommodations Review Output Example
  slug: demand-api-accommodations-review-output-example
- key_count: 6
  name: Demand Api Accommodations Reviews Scores Output Example
  slug: demand-api-accommodations-reviews-scores-output-example
- key_count: 4
  name: Demand Api Accommodations Search Input Example
  slug: demand-api-accommodations-search-input-example
- key_count: 6
  name: Demand Api Accommodations Search Product Output Example
  slug: demand-api-accommodations-search-product-output-example
- key_count: 6
  name: Demand Api Airports Input Example
  slug: demand-api-airports-input-example
- key_count: 6
  name: Demand Api Cities Input Example
  slug: demand-api-cities-input-example
- key_count: 6
  name: Demand Api Constants Data Output Example
  slug: demand-api-constants-data-output-example
- key_count: 6
  name: Demand Api Countries Input Example
  slug: demand-api-countries-input-example
- key_count: 6
  name: Demand Api Districts Input Example
  slug: demand-api-districts-input-example
- key_count: 6
  name: Demand Api Flights Output Example
  slug: demand-api-flights-output-example
- key_count: 6
  name: Demand Api Landmarks Input Example
  slug: demand-api-landmarks-input-example
- key_count: 4
  name: Demand Api Order Create Booker Input Example
  slug: demand-api-order-create-booker-input-example
- key_count: 1
  name: Demand Api Order Create Payment Input Example
  slug: demand-api-order-create-payment-input-example
- key_count: 6
  name: Demand Api Order Details Booker Output Example
  slug: demand-api-order-details-booker-output-example
- key_count: 6
  name: Demand Api Order Details Data Output Example
  slug: demand-api-order-details-data-output-example
- key_count: 6
  name: Demand Api Orders Preview Product Output Example
  slug: demand-api-orders-preview-product-output-example
- key_count: 6
  name: Demand Api Regions Input Example
  slug: demand-api-regions-input-example
- key_count: 6
  name: Demand Api Trader Output Example
  slug: demand-api-trader-output-example
finops:
- name: Booking Holdings Finops
  service_category: Travel + Accommodations
  slug: booking-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/booking-holdings.png
json_schemas:
- name: AccommodationsAvailabilityInput
  property_count: 9
  slug: demand-api-accommodations-availability-input
- name: AccommodationsAvailabilityProductOutput
  property_count: 10
  slug: demand-api-accommodations-availability-product-output
- name: AccommodationsDetailsDataOutput
  property_count: 33
  slug: demand-api-accommodations-details-data-output
- name: AccommodationsDetailsInput
  property_count: 13
  slug: demand-api-accommodations-details-input
- name: AccommodationsDetailsRoomOutput
  property_count: 13
  slug: demand-api-accommodations-details-room-output
- name: AccommodationsLocationOutput
  property_count: 7
  slug: demand-api-accommodations-location-output
- name: AccommodationsPoliciesOutput
  property_count: 6
  slug: demand-api-accommodations-policies-output
- name: AccommodationsReviewOutput
  property_count: 9
  slug: demand-api-accommodations-review-output
- name: AccommodationsReviewsScoresOutput
  property_count: 6
  slug: demand-api-accommodations-reviews-scores-output
- name: AccommodationsSearchInput
  property_count: 29
  slug: demand-api-accommodations-search-input
- name: AccommodationsSearchProductOutput
  property_count: 11
  slug: demand-api-accommodations-search-product-output
- name: AirportsInput
  property_count: 9
  slug: demand-api-airports-input
- name: CitiesInput
  property_count: 9
  slug: demand-api-cities-input
- name: ConstantsDataOutput
  property_count: 9
  slug: demand-api-constants-data-output
- name: CountriesInput
  property_count: 9
  slug: demand-api-countries-input
- name: DistrictsInput
  property_count: 9
  slug: demand-api-districts-input
- name: FlightsOutput
  property_count: 7
  slug: demand-api-flights-output
- name: LandmarksInput
  property_count: 9
  slug: demand-api-landmarks-input
- name: OrderCreateBookerInput
  property_count: 6
  slug: demand-api-order-create-booker-input
- name: OrderCreatePaymentInput
  property_count: 6
  slug: demand-api-order-create-payment-input
- name: OrderDetailsBookerOutput
  property_count: 7
  slug: demand-api-order-details-booker-output
- name: OrderDetailsDataOutput
  property_count: 14
  slug: demand-api-order-details-data-output
- name: OrdersPreviewProductOutput
  property_count: 9
  slug: demand-api-orders-preview-product-output
- name: RegionsInput
  property_count: 8
  slug: demand-api-regions-input
- name: TraderOutput
  property_count: 7
  slug: demand-api-trader-output
json_structures:
- name: Demand Api Accommodations Availability Input Structure
  property_count: 9
  slug: demand-api-accommodations-availability-input-structure
- name: Demand Api Accommodations Availability Product Output Structure
  property_count: 10
  slug: demand-api-accommodations-availability-product-output-structure
- name: Demand Api Accommodations Details Data Output Structure
  property_count: 33
  slug: demand-api-accommodations-details-data-output-structure
- name: Demand Api Accommodations Details Input Structure
  property_count: 13
  slug: demand-api-accommodations-details-input-structure
- name: Demand Api Accommodations Details Room Output Structure
  property_count: 13
  slug: demand-api-accommodations-details-room-output-structure
- name: Demand Api Accommodations Location Output Structure
  property_count: 7
  slug: demand-api-accommodations-location-output-structure
- name: Demand Api Accommodations Policies Output Structure
  property_count: 6
  slug: demand-api-accommodations-policies-output-structure
- name: Demand Api Accommodations Review Output Structure
  property_count: 9
  slug: demand-api-accommodations-review-output-structure
- name: Demand Api Accommodations Reviews Scores Output Structure
  property_count: 6
  slug: demand-api-accommodations-reviews-scores-output-structure
- name: Demand Api Accommodations Search Input Structure
  property_count: 29
  slug: demand-api-accommodations-search-input-structure
- name: Demand Api Accommodations Search Product Output Structure
  property_count: 11
  slug: demand-api-accommodations-search-product-output-structure
- name: Demand Api Airports Input Structure
  property_count: 9
  slug: demand-api-airports-input-structure
- name: Demand Api Cities Input Structure
  property_count: 9
  slug: demand-api-cities-input-structure
- name: Demand Api Constants Data Output Structure
  property_count: 9
  slug: demand-api-constants-data-output-structure
- name: Demand Api Countries Input Structure
  property_count: 9
  slug: demand-api-countries-input-structure
- name: Demand Api Districts Input Structure
  property_count: 9
  slug: demand-api-districts-input-structure
- name: Demand Api Flights Output Structure
  property_count: 7
  slug: demand-api-flights-output-structure
- name: Demand Api Landmarks Input Structure
  property_count: 9
  slug: demand-api-landmarks-input-structure
- name: Demand Api Order Create Booker Input Structure
  property_count: 6
  slug: demand-api-order-create-booker-input-structure
- name: Demand Api Order Create Payment Input Structure
  property_count: 6
  slug: demand-api-order-create-payment-input-structure
- name: Demand Api Order Details Booker Output Structure
  property_count: 7
  slug: demand-api-order-details-booker-output-structure
- name: Demand Api Order Details Data Output Structure
  property_count: 14
  slug: demand-api-order-details-data-output-structure
- name: Demand Api Orders Preview Product Output Structure
  property_count: 9
  slug: demand-api-orders-preview-product-output-structure
- name: Demand Api Regions Input Structure
  property_count: 8
  slug: demand-api-regions-input-structure
- name: Demand Api Trader Output Structure
  property_count: 7
  slug: demand-api-trader-output-structure
jsonld:
- class_count: 37
  name: Booking Holdings Demand Api Context
  property_count: 284
  slug: booking-holdings-demand-api-context
layout: provider
modified: '2026-06-02'
name: Booking Holdings
nav: Providers
network: true
overview: 'Booking Holdings publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Accommodations API, Attachments API, Cars API, and 6 more. Tagged areas include Accommodations, Airlines, Car Rentals, Hospitality, and Hotels.


  The Booking Holdings catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Booking Holdings'' developer surface includes authentication, engineering blog, and 17 more developer resources.'
plans:
- name: Booking Holdings Plans Pricing
  plan_count: 2
  slug: booking-holdings-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Booking Holdings Rate Limits
  slug: booking-holdings-rate-limits
rules:
- effective_rule_count: 30
  extends: []
  name: Booking Holdings API Rules
  rule_count: 30
  severity_counts:
    error: 10
    hint: 0
    info: 7
    warn: 13
  slug: booking-com-demand-api-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Booking Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: booking-holdings-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Booking Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: booking-holdings-spectral-rules
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 31.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 28.8
    contract_quality: 20.9
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/booking-holdings/refs/heads/main/screenshots/booking-holdings-2026-06-20T173602.png
security:
- kind: authentication
  name: Booking Holdings Authentication
  slug: booking-holdings-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Booking Holdings Domain Security
  slug: booking-holdings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: booking-holdings
tags:
- Accommodations
- Airlines
- Car Rentals
- Hospitality
- Hotels
- Restaurant
- Travel
website: https://www.bookingholdings.com
---
