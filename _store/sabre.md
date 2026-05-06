---
aid: sabre
name: Sabre
description: Sabre Corporation is a leading technology provider for the global travel industry, operating one of the world's largest travel marketplaces through its Global Distribution System (GDS). Sabre provides APIs for air shopping, booking, hotel reservations, car rentals, rail ticketing, and travel agency workflow automation to airlines, hotels, travel agencies, and online travel agencies (OTAs).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Travel
  - GDS
  - Airlines
  - Hotels
  - Car Rental
  - Booking
url: https://raw.githubusercontent.com/api-evangelist/sabre/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sabre:bargain-finder-max
    name: Sabre Bargain Finder Max API
    description: Sabre Bargain Finder Max (BFM) API provides low-fare search capabilities for air shopping, returning optimal flight itineraries with pricing across Sabre's global airline content inventory including ATPCO, LCC, and NDC content. Supports one-way, round-trip, open-jaw, and multi-city searches with flexible date ranges and cabin preferences.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Airlines
      - GDS
      - Air Shopping
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
      - type: OpenAPI
        url: openapi/sabre-bargain-finder-max-openapi.yml
  - aid: sabre:air-booking
    name: Sabre Air Booking API
    description: Sabre Air Booking API enables flight booking, passenger name record (PNR) creation and management, seat selection, ticketing, and booking modification for travel agencies and online travel applications. Supports NDC offer booking, ancillary services, and PNR queue management.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Airlines
      - GDS
      - Booking
      - PNR
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
      - type: SDKs
        url: https://github.com/SabreDevStudio/postman-collections
  - aid: sabre:hotels
    name: Sabre Hotels API
    description: Sabre Hotels API provides hotel search, availability, rate shopping, content retrieval, and booking APIs for travel agencies and OTAs, accessing Sabre's global lodging content covering over 2 million properties and SynXis hotel distribution network. Supports radius search, amenity filters, chain preferences, and cancellation management.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Hotels
      - GDS
      - Booking
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
      - type: SDKs
        url: https://github.com/SabreDevStudio/get-hotel-avail-v2-sample-nodejs
      - type: OpenAPI
        url: openapi/sabre-hotels-openapi.yml
  - aid: sabre:cars
    name: Sabre Cars API
    description: Sabre Cars API provides car rental search, availability, rate shopping, reservation, and management APIs for travel agencies and OTAs, connecting to over 40 global car rental brands across 40,000 locations through Sabre's GDS distribution.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Car Rental
      - GDS
      - Booking
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
  - aid: sabre:destination-content
    name: Sabre Destination Content API
    description: Sabre Destination Content API provides destination guides, points of interest, geo data, and travel inspiration content for travel applications and itinerary planning tools.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Destination
      - Content
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
  - aid: sabre:booking-management
    name: Sabre Booking Management API
    description: Sabre Booking Management API provides unified management of multi-segment travel reservations including flights, hotels, and car rentals within a single booking record. Supports booking creation, retrieval, modification, and cancellation.
    humanURL: https://developer.sabre.com/docs/rest_apis/trip/orders/booking_management
    tags:
      - Travel
      - Booking
      - GDS
      - REST
    properties:
      - type: Documentation
        url: https://developer.sabre.com/docs/rest_apis/trip/orders/booking_management
  - aid: sabre:rail
    name: Sabre Rail API
    description: Sabre Rail API provides rail ticket search, booking, and management capabilities connecting to over 30 rail operators worldwide for travel agencies and multi-modal booking platforms.
    humanURL: https://developer.sabre.com/
    tags:
      - Travel
      - Rail
      - GDS
      - Booking
    properties:
      - type: Documentation
        url: https://developer.sabre.com/
common:
  - type: Portal
    url: https://developer.sabre.com/
  - type: Documentation
    url: https://developer.sabre.com/
  - type: GettingStarted
    url: https://developer.sabre.com/guides/travel-agency/api-self-service-guide
  - type: Authentication
    url: https://developer.sabre.com/guides/travel-agency/developer-guides/rest-apis-token-credentials
  - type: Website
    url: https://www.sabre.com/
  - type: Support
    url: https://developer.sabre.com/support
  - type: Blog
    url: https://developer.sabre.com/blog
  - type: GitHubOrganization
    url: https://github.com/SabreDevStudio
  - type: SDKs
    url: https://github.com/SabreDevStudio
  - type: SpectralRules
    url: rules/sabre-rules.yml
  - type: JSONSchema
    url: json-schema/sabre-itinerary-schema.json
  - type: JSONSchema
    url: json-schema/sabre-hotel-schema.json
  - type: JSONStructure
    url: json-structure/sabre-air-itinerary-structure.json
  - type: JSONStructure
    url: json-structure/sabre-hotel-structure.json
  - type: JSONLDContext
    url: json-ld/sabre-context.jsonld
  - type: Vocabulary
    url: vocabulary/sabre-vocabulary.yml
  - type: Capabilities
    url: capabilities/travel-booking.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
