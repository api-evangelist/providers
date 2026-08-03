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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 49
  human_in_the_loop: 1
  name: Booking Com Agentic Access
  operation_count: 54
  slug: booking-com-agentic-access
  summary_line: 54 operations · 49 acting · 1 human-in-the-loop
api_count: 24
apis:
- description: Endpoints to search for stays such as hotels and apartments, check availability, retrieve reviews, and get detailed property information.
  name: booking-com Accommodations API
  slug: booking-com-accommodations-api
- description: Endpoints for updating room availability, pricing, and booking restrictions using B.XML format.
  name: booking-com Availability API
  slug: booking-com-availability-api
- description: Endpoints for searching available car rentals and retrieving vehicle details, pricing, and availability.
  name: booking-com Cars API
  slug: booking-com-cars-api
- description: Endpoints for retrieving reference data such as accommodation types, facility types, room types, and other enumerated values.
  name: booking-com Constants API
  slug: booking-com-constants-api
- description: Endpoints to retrieve and manage messaging conversations, list conversations, fetch conversation details, and track updates.
  name: booking-com Conversations API
  slug: booking-com-conversations-api
- description: Endpoints for looking up car rental depots, including locations, reviews, and score breakdowns.
  name: booking-com Depots API
  slug: booking-com-depots-api
- description: Endpoints for managing derived pricing rules that automatically calculate rates based on a parent rate plan.
  name: booking-com Derived Pricing API
  slug: booking-com-derived-pricing-api
- description: Endpoints for managing property-level and room-level facilities and amenities.
  name: booking-com Facilities API
  slug: booking-com-facilities-api
- description: Endpoints for retrieving current inventory and rate details for active room/rate combinations.
  name: booking-com Inventory API
  slug: booking-com-inventory-api
- description: Endpoints for retrieving geographical location data including countries, cities, regions, and airports.
  name: booking-com Locations API
  slug: booking-com-locations-api
- description: Endpoints for two-way post-booking communication between guests and properties, allowing you to send and retrieve messages, exchange images, and check conversation details.
  name: booking-com Messages API
  slug: booking-com-messages-api
- description: Endpoints to preview and create new orders, check order details, cancel or modify existing orders.
  name: booking-com Orders API
  slug: booking-com-orders-api
- description: OTA-based endpoints for availability and rate notifications following the OpenTravel Alliance specification.
  name: booking-com OTA Availability API
  slug: booking-com-ota-availability-api
- description: Legacy OTA-based endpoints for property content management. These endpoints follow the OpenTravel Alliance specification and are being deprecated in favor of modular APIs.
  name: booking-com OTA Legacy API
  slug: booking-com-ota-legacy-api
- description: OTA-based endpoints for reservation notification and modification following the OpenTravel Alliance specification.
  name: booking-com OTA Reservations API
  slug: booking-com-ota-reservations-api
- description: Generic payment-related endpoints, including supported currencies and payment types.
  name: booking-com Payments API
  slug: booking-com-payments-api
- description: Endpoints for adding, managing, and organizing property photos.
  name: booking-com Photos API
  slug: booking-com-photos-api
- description: Endpoints for creating, managing, and retrieving promotional offers for properties on Booking.com.
  name: booking-com Promotions API
  slug: booking-com-promotions-api
- description: Endpoints for creating and updating property information including name, location, contact details, policies, and general settings.
  name: booking-com Property Management API
  slug: booking-com-property-management-api
- description: Endpoints for creating and managing rate plans, including pricing rules and occupancy-based rates.
  name: booking-com Rates API
  slug: booking-com-rates-api
- description: Endpoints for recovering reservations that were not picked up earlier or made prior to the property being connected to the system.
  name: booking-com Recovery API
  slug: booking-com-recovery-api
- description: Endpoints for retrieving new, modified, and cancelled property reservations using B.XML format.
  name: booking-com Reservations API
  slug: booking-com-reservations-api
- description: Endpoints for managing room types, room names, bed configurations, and room-level facilities.
  name: booking-com Rooms API
  slug: booking-com-rooms-api
- description: Endpoints for retrieving information about car rental suppliers and their offerings.
  name: booking-com Suppliers API
  slug: booking-com-suppliers-api
artifact_total: 46
collections:
- collection_type: open
  name: Booking.com Car Rentals API
  slug: open-booking-com-car-rentals-api
- collection_type: open
  name: Booking.com Connectivity Content API
  slug: open-booking-com-connectivity-content-api
- collection_type: open
  name: Booking.com Connectivity Promotions API
  slug: open-booking-com-connectivity-promotions-api
- collection_type: open
  name: Booking.com Connectivity Rates and Availability API
  slug: open-booking-com-connectivity-rates-availability-api
- collection_type: open
  name: Booking.com Connectivity Reservations API
  slug: open-booking-com-connectivity-reservations-api
- collection_type: open
  name: Booking.com Demand API
  slug: open-booking-com-demand-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/booking-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/booking-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/booking-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/booking-com-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bookingcom
- group: design
  title: ''
  type: JSONLD
  url: json-ld/booking-com-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-accommodation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/booking-com-promotion-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.booking.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://news.booking.com/feed/
description: Seamlessly incorporate Booking.com inventory into your travel application.
features:
- 'Booking.com: API access via partner / B2B contracts only'
- No public API pricing published — contact enterprise sales
- Booking.com Connectivity APIs require Hotel Manager/Connectivity Partner approval; commission per booking.
finops:
- name: Booking Com Finops
  service_category: Travel / Hospitality
  slug: booking-com-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Booking.com platform, covering accommodation search, availability, booking, reviews, and property management. It is derived from the public REST/XML APIs av
  name: Booking.com GraphQL Schema
  slug: booking-com-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/booking-com.png
json_schemas:
- name: Booking.com Accommodation
  property_count: 25
  slug: booking-com-accommodation
- name: Booking.com Order
  property_count: 16
  slug: booking-com-order
- name: Booking.com Promotion
  property_count: 19
  slug: booking-com-promotion
jsonld:
- class_count: 0
  name: Booking Com Context
  property_count: 10
  slug: booking-com-context
layout: provider
modified: '2026-05-19'
name: booking-com
nav: Providers
network: true
overview: 'booking-com publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Accommodations API, Availability API, Cars API, and 21 more.


  The booking-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  booking-com''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Booking Com Plans Pricing
  plan_count: 1
  slug: booking-com-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Booking Com Rate Limits
  slug: booking-com-rate-limits
rules:
- name: booking-com API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: booking-com-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 75.0
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/booking-com/refs/heads/main/screenshots/booking-com-2026-06-20T173602.png
security:
- kind: authentication
  name: Booking Com Authentication
  slug: booking-com-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Booking Com Domain Security
  slug: booking-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Booking Com Vulnerability Disclosure
  slug: booking-com-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: booking-com
---
