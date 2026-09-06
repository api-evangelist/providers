---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Travelport Agentic Access
  operation_count: 30
  slug: travelport-agentic-access
  summary_line: 30 operations · 22 acting
api_count: 1
apis:
- description: RESTful JSON API providing end-to-end air travel workflows including search, price, book, ticket, cancel, and exchange. Covers both GDS and NDC content from 400+ airlines and low-cost carriers, with w
  name: Travelport TripServices Flights API
  slug: trip-services-flights
- description: RESTful JSON API for hotel search, availability, rules, reservation management, and modification across 180+ countries. Supports searches by coordinates, address, airport/city code, or property ID, pl
  name: Travelport TripServices Stays API
  slug: trip-services-stays
- description: RESTful JSON payments API enabling online travel agencies to perform credit card authorizations, address validations, 3D Secure transactions, and reversals against designated merchant vendors. Current
  name: Travelport TripServices Pay API
  slug: trip-services-pay
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Booking API from Travelport — 1 operation(s) for booking.
  name: Travelport Booking API
  slug: travelport-booking-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The EMDs API from Travelport — 2 operation(s) for emds.
  name: Travelport EMDs API
  slug: travelport-emds-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Fare Rules API from Travelport — 2 operation(s) for fare rules.
  name: Travelport Fare Rules API
  slug: travelport-fare-rules-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Modifications API from Travelport — 3 operation(s) for modifications.
  name: Travelport Modifications API
  slug: travelport-modifications-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Pricing API from Travelport — 2 operation(s) for pricing.
  name: Travelport Pricing API
  slug: travelport-pricing-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Queues API from Travelport — 3 operation(s) for queues.
  name: Travelport Queues API
  slug: travelport-queues-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Reservations API from Travelport — 2 operation(s) for reservations.
  name: Travelport Reservations API
  slug: travelport-reservations-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Search API from Travelport — 3 operation(s) for search.
  name: Travelport Search API
  slug: travelport-search-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Seats and Ancillaries API from Travelport — 2 operation(s) for seats and ancillaries.
  name: Travelport Seats and Ancillaries API
  slug: travelport-seats-and-ancillaries-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Ticketing API from Travelport — 4 operation(s) for ticketing.
  name: Travelport Ticketing API
  slug: travelport-ticketing-api
- baseURL: https://api.travelport.net/11
  baseurl_source: declared
  description: The Workbench API from Travelport — 3 operation(s) for workbench.
  name: Travelport Workbench API
  slug: travelport-workbench-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Travelport TripServices Flights Booking API
  slug: open-travelport-booking-api
- collection_type: open
  name: Travelport TripServices Flights Booking EMDs API
  slug: open-travelport-emds-api
- collection_type: open
  name: Travelport TripServices Flights Booking Fare Rules API
  slug: open-travelport-fare-rules-api
- collection_type: open
  name: Travelport TripServices Flights Booking Modifications API
  slug: open-travelport-modifications-api
- collection_type: open
  name: Travelport TripServices Flights Booking Pricing API
  slug: open-travelport-pricing-api
- collection_type: open
  name: Travelport TripServices Flights Booking Queues API
  slug: open-travelport-queues-api
- collection_type: open
  name: Travelport TripServices Flights Booking Reservations API
  slug: open-travelport-reservations-api
- collection_type: open
  name: Travelport TripServices Flights Booking Search API
  slug: open-travelport-search-api
- collection_type: open
  name: Travelport TripServices Flights Booking Seats and Ancillaries API
  slug: open-travelport-seats-and-ancillaries-api
- collection_type: open
  name: Travelport TripServices Flights Booking Ticketing API
  slug: open-travelport-ticketing-api
- collection_type: open
  name: Travelport TripServices Flights Booking Workbench API
  slug: open-travelport-workbench-api
- collection_type: open
  name: Travelport TripServices Flights API
  slug: open-travelport
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/travelport-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/travelport-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/travelport-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/travelport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/travelport
- group: company
  title: ''
  type: Website
  url: https://www.travelport.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.travelport.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.travelport.com/getting-started
- group: other
  title: ''
  type: DevKits
  url: https://developer.travelport.com/downloads
- group: operate
  title: ''
  type: Support
  url: https://developer.travelport.com/support
- group: start
  title: ''
  type: LegacyPortal
  url: https://support.travelport.com/
- group: company
  title: ''
  type: About
  url: https://www.travelport.com/about-us
- group: company
  title: ''
  type: News
  url: https://www.travelport.com/news
- group: company
  title: ''
  type: Investors
  url: https://investors.travelport.com/
- group: company
  title: ''
  type: Careers
  url: https://www.travelport.com/careers
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.travelport.com/llms.txt
created: '2026-05-05'
description: A global travel technology company connecting travel providers with online and offline travel agencies. Operates a commerce platform facilitating airline, hotel, and car rental bookings through its Galileo, Apollo, and Worldspan systems.
graphqls:
- description: 'Travelport operates a global travel commerce platform that connects travel providers (airlines, hotels, car rental companies, rail operators) with online and offline travel agencies. Its core systems '
  name: Travelport GraphQL Schema
  slug: travelport-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travelport.png
layout: provider
modified: '2026-05-16'
name: Travelport
nav: Providers
network: true
overview: 'Travelport publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Booking API, EMDs API, Fare Rules API, and 8 more. Tagged areas include Travel, Travel Technology, Reservations, GDS, and NDC.


  Travelport''s developer surface includes authentication, getting-started guide, support, product news, and 13 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 26.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/travelport/refs/heads/main/screenshots/travelport-2026-06-20T195638.png
security:
- kind: authentication
  name: Travelport Authentication
  slug: travelport-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Travelport Domain Security
  slug: travelport-domain-security
  summary_line: TLSv1.3 · DMARC
slug: travelport
tags:
- Travel
- Travel Technology
- Reservations
- GDS
- NDC
- Flights
- Hotels
- Payments
website: https://www.travelport.com/
---
