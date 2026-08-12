---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Family of OAuth 2.0 secured REST APIs for the iHotelier Booking Engine 4.0 (CRS). Enables B2C / web-client applications to search availability, hold and create reservations (including group reservatio
  name: Amadeus iHotelier BE API
  slug: amadeus-ihotelier-be-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/travelclick-amadeus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amadeus-hospitality.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.travelclick.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.travelclick.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.travelclick.com/getstarted
- group: start
  title: ''
  type: SignUp
  url: https://developer.travelclick.com/getstarted
- group: operate
  title: ''
  type: Support
  url: mailto:api-admin.tc@amadeus.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/travelclick-amadeus-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/travelclick-amadeus-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amadeus-hospitality.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amadeus-hospitality.com/privacy-policy/
created: '2026-07-17'
description: TravelClick, now Amadeus Hospitality, is a hotel commerce and distribution technology provider whose flagship product is the iHotelier Booking Engine 4.0 (CRS/central reservation system). For developers it publishes the Amadeus iHotelier BE API — a family of OAuth 2.0 secured REST APIs that let web and B2C guest-facing applications search availability, hold and create reservations, manage group bookings, and drive the hotel booking flow. TravelClick also operates OTA Connect, a distribution API that connects channel-management partners and OTAs to hotel inventory. API documentation and interactive testing are available to accounts registered on the developer portal at developer.travelclick.com; non-production API keys are issued on request.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/travelclick-amadeus.png
layout: provider
modified: '2026-07-21'
name: TravelClick (Amadeus)
nav: Providers
network: true
overview: 'TravelClick (Amadeus) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Hospitality, Hotels, and Travel.


  TravelClick (Amadeus)''s developer surface includes documentation, getting-started guide, signup flow, support, authentication, and 6 more developer resources.'
random_paper: 97
score:
  band: emerging
  composite: 22.4
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Travelclick Amadeus Authentication
  slug: travelclick-amadeus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Travelclick Amadeus Domain Security
  slug: travelclick-amadeus-domain-security
  summary_line: TLSv1.3 · DMARC
slug: travelclick-amadeus
tags:
- Company
- Ai Apps
- Hospitality
- Hotels
- Travel
- Booking Engine
- Reservations
- Distribution
- Central Reservation System
- OAuth2
website: https://www.amadeus-hospitality.com/
---
