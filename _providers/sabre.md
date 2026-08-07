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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Sabre Agentic Access
  operation_count: 8
  slug: sabre-agentic-access
  summary_line: 8 operations · 6 acting
api_count: 9
apis:
- description: Sabre Air Booking API enables flight booking, passenger name record (PNR) creation and management, seat selection, ticketing, and booking modification for travel agencies and online travel application
  name: Sabre Air Booking API
  slug: air-booking
- description: Sabre Cars API provides car rental search, availability, rate shopping, reservation, and management APIs for travel agencies and OTAs, connecting to over 40 global car rental brands across 40,000 loca
  name: Sabre Cars API
  slug: cars
- description: Sabre Destination Content API provides destination guides, points of interest, geo data, and travel inspiration content for travel applications and itinerary planning tools.
  name: Sabre Destination Content API
  slug: destination-content
- description: Sabre Booking Management API provides unified management of multi-segment travel reservations including flights, hotels, and car rentals within a single booking record. Supports booking creation, retr
  name: Sabre Booking Management API
  slug: booking-management
- description: Sabre Rail API provides rail ticket search, booking, and management capabilities connecting to over 30 rail operators worldwide for travel agencies and multi-modal booking platforms.
  name: Sabre Rail API
  slug: rail
- description: Low-fare search and offer retrieval
  name: Sabre Air Shopping API
  slug: sabre-air-shopping-api
- description: Token-based authentication
  name: Sabre Authentication API
  slug: sabre-authentication-api
- description: Reservation management
  name: Sabre Hotel Booking API
  slug: sabre-hotel-booking-api
- description: Search and availability operations
  name: Sabre Hotel Search API
  slug: sabre-hotel-search-api
artifact_total: 57
collections:
- collection_type: open
  name: Sabre Bargain Finder Max API
  slug: open-sabre-bargain-finder-max
- collection_type: open
  name: Sabre Hotels API
  slug: open-sabre-hotels
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sabre-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sabre-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sabre-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sabre-corporation
- group: start
  title: ''
  type: Portal
  url: https://developer.sabre.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sabre.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sabre.com/guides/travel-agency/api-self-service-guide
- group: auth
  title: ''
  type: Authentication
  url: https://developer.sabre.com/guides/travel-agency/developer-guides/rest-apis-token-credentials
- group: company
  title: ''
  type: Website
  url: https://www.sabre.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.sabre.com/support
- group: company
  title: ''
  type: Blog
  url: https://developer.sabre.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SabreDevStudio
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SabreDevStudio
- group: design
  title: ''
  type: SpectralRules
  url: rules/sabre-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sabre-itinerary-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sabre-hotel-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sabre-air-itinerary-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sabre-hotel-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/sabre-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sabre-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/travel-booking.yaml
created: '2026-03-18'
description: Sabre Corporation is a leading technology provider for the global travel industry, operating one of the world's largest travel marketplaces through its Global Distribution System (GDS). Sabre provides APIs for air shopping, booking, hotel reservations, car rentals, rail ticketing, and travel agency workflow automation to airlines, hotels, travel agencies, and online travel agencies (OTAs).
examples:
- key_count: 2
  name: Sabre Bargain Finder Max Search Example
  slug: sabre-bargain-finder-max-search-example
- key_count: 2
  name: Sabre Get Auth Token Example
  slug: sabre-get-auth-token-example
- key_count: 2
  name: Sabre Hotel Search Example
  slug: sabre-hotel-search-example
finops:
- name: Sabre Finops
  service_category: Travel / GDS
  slug: sabre-finops
graphqls:
- description: Sabre Corporation operates one of the world's largest travel Global Distribution Systems (GDS), providing APIs for air shopping, booking, hotel reservations, car rentals, rail ticketing, and travel ag
  name: Sabre GraphQL Schema
  slug: sabre-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sabre.png
json_schemas:
- name: Address
  property_count: 5
  slug: sabre-address
- name: AirportSearch
  property_count: 2
  slug: sabre-airportsearch
- name: APIError
  property_count: 4
  slug: sabre-apierror
- name: BFMRequest
  property_count: 1
  slug: sabre-bfmrequest
- name: BFMResponse
  property_count: 1
  slug: sabre-bfmresponse
- name: CancellationResponse
  property_count: 3
  slug: sabre-cancellationresponse
- name: CitySearch
  property_count: 2
  slug: sabre-citysearch
- name: ErrorResponse
  property_count: 4
  slug: sabre-errorresponse
- name: FlightSegment
  property_count: 11
  slug: sabre-flightsegment
- name: GeoCodeSearch
  property_count: 3
  slug: sabre-geocodesearch
- name: GuestInfo
  property_count: 6
  slug: sabre-guestinfo
- name: Sabre Hotel
  property_count: 10
  slug: sabre-hotel
- name: HotelRatesResponse
  property_count: 3
  slug: sabre-hotelratesresponse
- name: HotelReservationRequest
  property_count: 8
  slug: sabre-hotelreservationrequest
- name: HotelReservationResponse
  property_count: 8
  slug: sabre-hotelreservationresponse
- name: HotelSearchRequest
  property_count: 6
  slug: sabre-hotelsearchrequest
- name: HotelSearchResponse
  property_count: 3
  slug: sabre-hotelsearchresponse
- name: HotelSummary
  property_count: 8
  slug: sabre-hotelsummary
- name: Sabre Itinerary
  property_count: 5
  slug: sabre-itinerary
- name: OriginDestinationInformation
  property_count: 4
  slug: sabre-origindestinationinformation
- name: OriginDestinationOption
  property_count: 1
  slug: sabre-origindestinationoption
- name: PaymentInfo
  property_count: 4
  slug: sabre-paymentinfo
- name: PricedItinerary
  property_count: 3
  slug: sabre-priceditinerary
- name: Rate
  property_count: 2
  slug: sabre-rate
- name: RatePlan
  property_count: 7
  slug: sabre-rateplan
- name: ReShopRequest
  property_count: 1
  slug: sabre-reshoprequest
- name: RoomType
  property_count: 6
  slug: sabre-roomtype
- name: TokenResponse
  property_count: 3
  slug: sabre-tokenresponse
- name: TravelerInfoSummary
  property_count: 2
  slug: sabre-travelerinfosummary
- name: TravelPreferences
  property_count: 3
  slug: sabre-travelpreferences
json_structures:
- name: Sabre Air Itinerary Structure
  property_count: 0
  slug: sabre-air-itinerary-structure
- name: Sabre Hotel Structure
  property_count: 0
  slug: sabre-hotel-structure
- name: Sabre Structure
  property_count: 0
  slug: sabre-structure
jsonld:
- class_count: 37
  name: Sabre Context
  property_count: 10
  slug: sabre-context
layout: provider
modified: '2026-05-19'
name: Sabre
nav: Providers
network: true
overview: 'Sabre publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Air Shopping API, Authentication API, Hotel Booking API, and 1 more. Tagged areas include Travel, GDS, Airlines, Hotels, and Car Rental.


  The Sabre catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sabre''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, and 15 more developer resources.'
plans:
- name: Sabre Plans Pricing
  plan_count: 1
  slug: sabre-plans-pricing
press:
- date: '2026-05-25'
  title: Sabre unveils once-in-a-generation company rebuild and ...
  url: https://www.prnewswire.com/news-releases/sabre-unveils-once-in-a-generation-company-rebuild-and-its-ai-first-platform-at-itb-berlin-2026-302701932.html
- date: '2026-05-25'
  title: SABR Stock Price, News & Analysis
  url: https://www.stocktitan.net/overview/SABR/
- date: '2026-05-25'
  title: 'Sabre: the open platform powering modern travel'
  url: https://www.sabre.com/
- date: '2026-05-25'
  title: Sabre Forges 10-Year Partnership with Google to Build ...
  url: https://www.googlecloudpresscorner.com/2020-01-21-Sabre-Forges-10-Year-Partnership-with-Google-to-Build-the-Future-of-Travel
- date: '2026-05-25'
  title: Press Releases Archive
  url: https://www.sabre.com/releases/
random_paper: 73
rate_limits:
- limit_count: 1
  name: Sabre Rate Limits
  slug: sabre-rate-limits
rules:
- name: Sabre API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: sabre-jsonschema-spectral-rules
- name: Sabre API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 4
  slug: sabre-rules
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 77.4
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sabre/refs/heads/main/screenshots/sabre-2026-06-20T193316.png
security:
- kind: authentication
  name: Sabre Authentication
  slug: sabre-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sabre Domain Security
  slug: sabre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sabre
tags:
- Travel
- GDS
- Airlines
- Hotels
- Car Rental
- Booking
website: https://www.sabre.com/
---
