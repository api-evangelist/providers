---
aid: tripadvisor
url: https://raw.githubusercontent.com/api-evangelist/tripadvisor/refs/heads/main/apis.yml
name: Tripadvisor
description: Tripadvisor is the world's largest travel guidance platform, helping hundreds of millions of travelers each month find places to stay, things to do, and restaurants through reviews, photos, and tools. The platform maintains over 7.5 million locations and 1 billion reviews across 43 markets and 29 languages. Tripadvisor provides APIs for content integration, hotel connectivity, and restaurant reservations.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Attractions
  - Hotels
  - Hospitality
  - Restaurants
  - Reviews
  - Travel
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tripadvisor:content-api
    name: Tripadvisor Content API
    tags:
      - Attractions
      - Hotels
      - Locations
      - Restaurants
      - Reviews
      - Travel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.content.tripadvisor.com/api/v1
    humanURL: https://developer-tripadvisor.com/content-api/
    properties:
      - url: https://developer-tripadvisor.com/content-api/
        type: Documentation
      - url: openapi/tripadvisor-content-api-openapi.yml
        type: OpenAPI
    description: The Tripadvisor Content API provides developers with access to Tripadvisor's extensive dataset of more than 7.5 million locations, 1 billion reviews and opinions, and content in 29 languages. The API includes endpoints for location search, nearby search, location details, location photos, and location reviews, enabling developers to integrate rich travel content into their websites and applications. The first 5,000 API calls per month are free, making it accessible for initial development and testing.
  - aid: tripadvisor:hotel-availability-check-api
    name: Tripadvisor Hotel Availability Check API
    tags:
      - Availability
      - Booking
      - Connectivity
      - Hospitality
      - Hotels
      - Travel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://partner-endpoint.example.com
    humanURL: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/
    properties:
      - url: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/
        type: Documentation
      - url: openapi/tripadvisor-hotel-availability-check-api-openapi.yml
        type: OpenAPI
    description: The Tripadvisor Hotel Availability Check (HAC) API allows hotel booking partners to display their availability and pricing on Tripadvisor. When a user views a hotel page, Tripadvisor sends HTTP POST requests to the partner's API to retrieve real-time price and availability data. The API supports batch requests for multiple hotels and requires responses within 5 seconds on average. The current version (v8) provides richer availability data to help partners increase conversions.
  - aid: tripadvisor:hotel-inventory-api
    name: Tripadvisor Hotel Inventory API
    tags:
      - Connectivity
      - Hospitality
      - Hotels
      - Inventory
      - Travel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://partner-endpoint.example.com
    humanURL: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/documentation/hotel_inventory/
    properties:
      - url: https://developer-tripadvisor.com/connectivity-solutions/hotel-availability-check-api/documentation/hotel_inventory/
        type: Documentation
      - url: openapi/tripadvisor-hotel-availability-check-api-openapi.yml
        type: OpenAPI
    description: The Tripadvisor Hotel Inventory API enables connectivity partners to manage their hotel inventory listings on the Tripadvisor platform. Partners use this API to register and update the hotels they can provide availability and pricing data for, ensuring that their connected properties are accurately represented. This API works in conjunction with the Hotel Availability Check API as part of Tripadvisor's connectivity solutions for the hospitality industry.
common:
  - type: Website
    url: https://www.tripadvisor.com
    name: Tripadvisor
  - type: DeveloperPortal
    url: https://developer-tripadvisor.com
    name: Tripadvisor Developer Portal
  - type: Documentation
    url: https://tripadvisor-content-api.readme.io/reference/overview
    name: Content API Reference
  - type: SignUp
    url: https://developer-tripadvisor.com/content-api/
    name: Register for Content API
  - type: TermsOfService
    url: https://developer-tripadvisor.com/content-api/terms-of-use/
    name: Content API Terms of Use
  - type: GitHubOrganization
    url: https://github.com/tripadvisor
    name: Tripadvisor GitHub Organization
  - type: GitHubOrganization
    url: https://github.com/tripadvisor-dev
    name: Tripadvisor Developers GitHub
  - type: JSON-LD
    url: json-ld/tripadvisor-context.jsonld
    name: Tripadvisor JSON-LD Context
  - type: JSONSchema
    url: json-schema/tripadvisor-location-schema.json
    name: Location JSON Schema
  - type: JSONSchema
    url: json-schema/tripadvisor-review-schema.json
    name: Review JSON Schema
  - type: JSONSchema
    url: json-schema/tripadvisor-hotel-availability-schema.json
    name: Hotel Availability JSON Schema
  - url: rules/tripadvisor-rules.yml
    name: Tripadvisor Spectral Rules
    type: SpectralRules
  - url: vocabulary/tripadvisor-vocabulary.yml
    name: Tripadvisor Vocabulary
    type: Vocabulary
  - name: Features
    type: Features
    data:
      - name: Location Search
      - name: Nearby Search
      - name: Location Details
      - name: Location Photos
      - name: Location Reviews
      - name: Hotel Availability Check
      - name: Hotel Inventory Management
      - name: 7.5 Million Locations
      - name: 1 Billion Reviews
      - name: 29 Languages
      - name: 43 Markets
  - name: UseCases
    type: UseCases
    data:
      - name: Travel Content Integration
      - name: Hotel Booking Widget
      - name: Restaurant Discovery
      - name: Attraction Finder
      - name: Hotel Connectivity Partner
      - name: Travel App Development
      - name: Review Aggregation
  - name: Integrations
    type: Integrations
    data:
      - name: Booking.com
      - name: Expedia
      - name: Hotels.com
      - name: Viator
      - name: TheFork
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
