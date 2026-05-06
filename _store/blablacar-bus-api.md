---
aid: blablacar-bus-api
url: https://raw.githubusercontent.com/api-evangelist/blablacar-bus-api/refs/heads/main/apis.yml
name: BlaBlaCar Bus API
description: BlaBlaCar Bus API enables transport operators, OTAs, and travel aggregators to integrate with BlaBlaCar's coach and bus booking platform across Europe. The API provides access to route search, seat availability, booking creation, ticket management, and passenger notifications. BlaBlaCar Bus operates coach services across France, Germany, Poland, Spain, Italy, Ukraine, and other European markets under the BlaBlaBus brand.
tags:
  - Booking
  - Buses
  - Coach
  - Europe
  - Mobility
  - Ticketing
  - Transportation
  - Travel
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: blablacar-bus-api:blablacar-bus-api
    name: BlaBlaCar Bus API
    description: REST API for integrating with BlaBlaCar Bus (formerly BlaBlaBus) coach booking platform. Enables partners to search routes, check seat availability, create bookings, manage tickets, and receive booking confirmations. Targeted at OTAs, travel aggregators, mobility platforms, and enterprise travel management companies operating in European markets.
    humanURL: https://bus-api.blablacar.com/
    tags:
      - Booking
      - Buses
      - Coach
      - Europe
      - Ticketing
      - Transportation
    properties:
      - type: Documentation
        url: https://bus-api.blablacar.com/
      - type: OpenAPI
        url: openapi/blablacar-bus-api-openapi.yaml
common:
  - type: Website
    url: https://www.blablacar.com/bus
  - type: Documentation
    url: https://bus-api.blablacar.com/
  - type: GitHubOrganization
    url: https://github.com/blablacar
  - type: TermsOfService
    url: https://www.blablacar.com/about-us/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.blablacar.com/about-us/privacy-policy
  - type: SpectralRules
    url: rules/blablacar-bus-api-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/blablacar-bus-booking.yaml
  - type: Vocabulary
    url: vocabulary/blablacar-bus-api-vocabulary.yaml
  - type: Features
    data:
      - name: Route Search
        description: Search available coach routes between origin and destination stations across European markets with departure dates and passenger counts.
      - name: Seat Availability
        description: Check real-time seat availability and pricing for specific routes, trips, and departure times.
      - name: Booking Creation
        description: Create confirmed bookings for passengers with seat selection, passenger details, and payment processing integration.
      - name: Ticket Management
        description: Retrieve, modify, and cancel tickets with electronic ticket delivery and QR code generation.
      - name: Station Information
        description: Access comprehensive station data including names, addresses, GPS coordinates, and amenities across the BlaBlaCar Bus network.
      - name: Multi-Market Coverage
        description: Single API integration covering coach routes across France, Germany, Poland, Spain, Italy, Ukraine, and other European markets.
  - type: UseCases
    data:
      - name: OTA Integration
        description: Online travel agencies can search and book BlaBlaCar Bus routes alongside trains, flights, and car rentals for multimodal journey planning.
      - name: Travel Aggregator
        description: Price comparison and travel search engines can surface BlaBlaCar Bus options in coach and intercity bus search results.
      - name: Corporate Travel
        description: Enterprise travel management companies can include BlaBlaCar Bus as an affordable intercity transport option for business travelers.
      - name: Mobility Platform
        description: Mobility-as-a-Service platforms can integrate BlaBlaCar Bus as a long-distance transport mode in multimodal journey planning.
      - name: Reseller Programs
        description: Authorized resellers can distribute BlaBlaCar Bus tickets through their own branded channels and sales touchpoints.
  - type: Integrations
    data:
      - name: BlaBlaCar Carpooling
        description: BlaBlaCar Bus complements the carpooling marketplace, enabling multimodal journey planning combining bus and ridesharing.
      - name: Google Maps Platform
        description: Station coordinates and route data can be overlaid on mapping platforms for journey visualization.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
