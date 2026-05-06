---
aid: spothero
name: SpotHero
description: SpotHero is the leading digital parking marketplace in North America, offering a flexible parking API and developer toolkit that connects vehicles, drivers, and mobility apps with the largest network of off-street parking facilities. The platform enables navigation apps, rideshare services, connected cars, and enterprise fleets to seamlessly book and manage parking reservations. SpotHero was acquired by Uber in 2026 to power parking reservation experiences within the Uber app.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Parking
  - Mobility
  - Transportation
  - Navigation
  - Reservations
created: '2025-02-06'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/spothero/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: spothero:spothero-parking-api
    name: SpotHero Parking API
    description: The SpotHero Parking API provides programmatic access to the largest network of off-street parking facilities in North America. Partners can search for available parking spots, check real-time availability, create and manage reservations, and access facility details including pricing, amenities, and directions. The API supports navigation apps, mobility platforms, connected car dashboards, event ticketing systems, and enterprise fleet management solutions. SpotHero covers 400+ cities with 8,000+ parking locations and has facilitated 100M+ parking reservations.
    humanURL: https://spothero.com/developers
    baseURL: https://api.spothero.com/v2
    tags:
      - Parking
      - Reservations
      - Availability
      - Mobility
      - Navigation
    properties:
      - type: Documentation
        url: https://spothero.com/developers
      - type: Developer Portal
        url: https://api.spothero.com/v2/docs
      - type: Getting Started
        url: https://spothero.com/developers
      - type: OpenAPI
        url: openapi/spothero-parking-openapi.yml
    contact:
      - FN: SpotHero Partner Support
        email: partner.support@spothero.com
    features:
      - type: ParkingSearch
        description: Search for available parking by location, date, time, and vehicle type
      - type: RealTimeAvailability
        description: Real-time availability checks across 8,000+ parking facilities
      - type: Reservations
        description: Create, modify, and cancel parking reservations
      - type: FacilityDetails
        description: Access facility amenities, pricing, hours, and directions
      - type: BrandedExperience
        description: White-label integration with custom branding and logo on parking passes
      - type: WebWidget
        description: Copy-and-paste web widget for website integration
      - type: ParkingLink
        description: Deep-link routing to SpotHero app or web for minimal-development integrations
    useCases:
      - type: UrbanMobility
        description: Last-mile parking solutions for rideshare, transit, and navigation apps
      - type: ConnectedCar
        description: In-vehicle parking search and reservation from car dashboards
      - type: EventParking
        description: Pre-book parking for venues, stadiums, and events
      - type: FleetManagement
        description: Enterprise parking management for corporate fleets
      - type: CarshareRental
        description: Parking integration for carshare and rental fleet services
    integrations:
      - type: AppleMaps
        url: https://developer.apple.com/maps/
      - type: Uber
        url: https://developer.uber.com/
      - type: Cordova
        url: https://github.com/spothero/cordova-plugin-spothero
    solutions:
      - type: ParkingMarketplace
        description: Access to North America's largest off-street parking network
      - type: DeveloperToolkit
        description: API, SDK, Web Widget, and Parking Link routing tools for all integration needs
  - aid: spothero:spotnow-api
    name: SpotHero SpotNow API
    description: SpotNow is SpotHero's server and API built in Kotlin for real-time parking availability and instant booking functionality, exposed via the HeroLab platform.
    humanURL: https://github.com/spothero/herolab-spotnow
    baseURL: https://api.spothero.com
    tags:
      - Parking
      - Real-Time
      - Availability
      - Kotlin
    properties:
      - type: Repository
        url: https://github.com/spothero/herolab-spotnow
common:
  - type: Documentation
    url: https://spothero.com/developers
  - type: Developer Portal
    url: https://api.spothero.com/v2/docs
  - type: Terms of Service
    url: https://spothero.com/terms
  - type: Privacy Policy
    url: https://spothero.com/privacy
  - type: Website
    url: https://spothero.com
  - type: Contact
    url: mailto:partner.support@spothero.com
  - type: JSONSchema
    url: json-schema/spothero-reservation-schema.json
  - type: JSONSchema
    url: json-schema/spothero-facility-schema.json
  - type: JSONStructure
    url: json-structure/spothero-reservation-structure.json
  - type: JSONStructure
    url: json-structure/spothero-facility-structure.json
  - type: JSONLD
    url: json-ld/spothero-context.jsonld
  - type: SpectralRules
    url: rules/spothero-rules.yml
  - type: Capabilities
    url: capabilities/parking-mobility.yaml
  - type: Vocabulary
    url: vocabulary/spothero-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
