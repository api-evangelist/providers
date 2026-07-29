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
- acting_count: 2
  human_in_the_loop: 0
  name: Blablacar Bus Api Agentic Access
  operation_count: 7
  slug: blablacar-bus-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 5
apis:
- description: Create and manage bookings
  name: BlaBlaCar Bus API Bookings API
  slug: blablacar-bus-api-bookings-api
- description: Search and browse available coach routes
  name: BlaBlaCar Bus API Routes API
  slug: blablacar-bus-api-routes-api
- description: Access station information
  name: BlaBlaCar Bus API Stations API
  slug: blablacar-bus-api-stations-api
- description: Retrieve and manage passenger tickets
  name: BlaBlaCar Bus API Tickets API
  slug: blablacar-bus-api-tickets-api
- description: Search trip availability and pricing
  name: BlaBlaCar Bus API Trips API
  slug: blablacar-bus-api-trips-api
artifact_total: 43
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blablacar-bus-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/blablacar-bus-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blablacar-bus-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blablacar-bus-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blablacar
- group: company
  title: ''
  type: Website
  url: https://www.blablacar.com/bus
- group: docs
  title: ''
  type: Documentation
  url: https://bus-api.blablacar.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blablacar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blablacar.com/about-us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blablacar.com/about-us/privacy-policy
- group: design
  title: ''
  type: SpectralRules
  url: rules/blablacar-bus-api-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blablacar-bus-api-vocabulary.yaml
created: '2024-11-14'
description: BlaBlaCar Bus API enables transport operators, OTAs, and travel aggregators to integrate with BlaBlaCar's coach and bus booking platform across Europe. The API provides access to route search, seat availability, booking creation, ticket management, and passenger notifications. BlaBlaCar Bus operates coach services across France, Germany, Poland, Spain, Italy, Ukraine, and other European markets under the BlaBlaBus brand.
examples:
- key_count: 4
  name: Blablacar Bus Api Booking Example
  slug: blablacar-bus-api-booking-example
- key_count: 5
  name: Blablacar Bus Api Route Example
  slug: blablacar-bus-api-route-example
- key_count: 7
  name: Blablacar Bus Api Station Example
  slug: blablacar-bus-api-station-example
- key_count: 9
  name: Blablacar Bus Api Ticket Example
  slug: blablacar-bus-api-ticket-example
- key_count: 6
  name: Blablacar Bus Api Trip Example
  slug: blablacar-bus-api-trip-example
features:
- description: Search available coach routes between origin and destination stations across European markets with departure dates and passenger counts.
  name: Route Search
- description: Check real-time seat availability and pricing for specific routes, trips, and departure times.
  name: Seat Availability
- description: Create confirmed bookings for passengers with seat selection, passenger details, and payment processing integration.
  name: Booking Creation
- description: Retrieve, modify, and cancel tickets with electronic ticket delivery and QR code generation.
  name: Ticket Management
- description: Access comprehensive station data including names, addresses, GPS coordinates, and amenities across the BlaBlaCar Bus network.
  name: Station Information
- description: Single API integration covering coach routes across France, Germany, Poland, Spain, Italy, Ukraine, and other European markets.
  name: Multi-Market Coverage
finops:
- name: Blablacar Bus Api Finops
  service_category: API
  slug: blablacar-bus-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blablacar-bus-api.png
integrations:
- description: BlaBlaCar Bus complements the carpooling marketplace, enabling multimodal journey planning combining bus and ridesharing.
  name: BlaBlaCar Carpooling
- description: Station coordinates and route data can be overlaid on mapping platforms for journey visualization.
  name: Google Maps Platform
json_schemas:
- name: Booking
  property_count: 4
  slug: blablacar-bus-api-booking
- name: Route
  property_count: 5
  slug: blablacar-bus-api-route
- name: Station
  property_count: 7
  slug: blablacar-bus-api-station
- name: Ticket
  property_count: 9
  slug: blablacar-bus-api-ticket
- name: Trip
  property_count: 6
  slug: blablacar-bus-api-trip
json_structures:
- name: Blablacar Bus Api Booking Structure
  property_count: 4
  slug: blablacar-bus-api-booking-structure
- name: Blablacar Bus Api Route Structure
  property_count: 5
  slug: blablacar-bus-api-route-structure
- name: Blablacar Bus Api Station Structure
  property_count: 7
  slug: blablacar-bus-api-station-structure
- name: Blablacar Bus Api Ticket Structure
  property_count: 9
  slug: blablacar-bus-api-ticket-structure
- name: Blablacar Bus Api Trip Structure
  property_count: 6
  slug: blablacar-bus-api-trip-structure
jsonld:
- class_count: 13
  name: Blablacar Bus Api Context
  property_count: 20
  slug: blablacar-bus-api-context
layout: provider
modified: '2026-05-19'
name: BlaBlaCar Bus API
nav: Providers
network: true
overview: 'BlaBlaCar Bus API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Routes API, Stations API, and 2 more. Tagged areas include Booking, Buses, Coach, Europe, and Mobility.


  The BlaBlaCar Bus API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BlaBlaCar Bus API''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Blablacar Bus Api Plans Pricing
  plan_count: 3
  slug: blablacar-bus-api-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 5
  name: Blablacar Bus Api Rate Limits
  slug: blablacar-bus-api-rate-limits
rules:
- name: BlaBlaCar Bus API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: blablacar-bus-api-jsonschema-spectral-rules
- name: BlaBlaCar Bus API API Rules
  rule_count: 41
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 23
  slug: blablacar-bus-api-spectral-rules
score:
  band: developing
  composite: 50.6
  delta: -7.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/blablacar-bus-api/refs/heads/main/screenshots/blablacar-bus-api-2026-06-20T173332.png
security:
- kind: authentication
  name: Blablacar Bus Api Authentication
  slug: blablacar-bus-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blablacar Bus Api Domain Security
  slug: blablacar-bus-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Blablacar Bus Api Vulnerability Disclosure
  slug: blablacar-bus-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: blablacar-bus-api
tags:
- Booking
- Buses
- Coach
- Europe
- Mobility
- Ticketing
- Transportation
- Travel
use_cases:
- description: Online travel agencies can search and book BlaBlaCar Bus routes alongside trains, flights, and car rentals for multimodal journey planning.
  name: OTA Integration
- description: Price comparison and travel search engines can surface BlaBlaCar Bus options in coach and intercity bus search results.
  name: Travel Aggregator
- description: Enterprise travel management companies can include BlaBlaCar Bus as an affordable intercity transport option for business travelers.
  name: Corporate Travel
- description: Mobility-as-a-Service platforms can integrate BlaBlaCar Bus as a long-distance transport mode in multimodal journey planning.
  name: Mobility Platform
- description: Authorized resellers can distribute BlaBlaCar Bus tickets through their own branded channels and sales touchpoints.
  name: Reseller Programs
website: https://www.blablacar.com/bus
---
