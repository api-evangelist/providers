---
aid: amc-entertainment-holdings
name: AMC Entertainment Holdings
description: AMC Entertainment Holdings is the largest movie exhibition company in the United States and the world, operating AMC Theatres, AMC Stubs loyalty programs, and related entertainment brands. AMC publishes a public developer portal at developers.amctheatres.com that exposes a REST API for movies, showtimes, theatres, locations, seating, ticketing, concessions, AMC Stubs loyalty, refunds, fee waivers, barcodes, and webhooks. The API is the primary integration surface for distributors, partners, and third-party developers building movie discovery, ticket sales, and AMC Stubs co-marketing experiences.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Movies
  - Theatres
  - Showtimes
  - Ticketing
  - Concessions
  - Loyalty
  - Fortune 500
url: https://raw.githubusercontent.com/api-evangelist/amc-entertainment-holdings/refs/heads/main/apis.yml
created: '2026-05-04'
modified: '2026-05-05'
specificationVersion: '0.19'
apis:
  - aid: amc-entertainment-holdings:amc-theatres-api
    name: AMC Theatres API
    description: The AMC Theatres API is a public REST API providing programmatic access to AMC Theatres data including theatres, locations, showtimes, movies, seating, ticketing, concessions, and AMC Stubs loyalty. The API is intended for partner integrations such as movie discovery, ticketing, and entertainment listings. Authentication is performed via a vendor API key issued through the AMC developer portal and supplied in the X-AMC-Vendor-Key header. Resource families are versioned independently under /v1, /v2, /v3, and /v4 path prefixes, and collection responses use a HAL-style envelope.
    humanURL: https://developers.amctheatres.com
    baseURL: https://api.amctheatres.com
    tags:
      - Theatres
      - Showtimes
      - Movies
      - Ticketing
      - Concessions
      - Loyalty
      - Webhooks
    properties:
      - type: DeveloperPortal
        url: https://developers.amctheatres.com
      - type: Documentation
        url: https://developers.amctheatres.com
      - type: Authentication
        url: https://developers.amctheatres.com/GettingStarted/Authentication
      - type: Sandbox
        url: https://developers.amctheatres.com/GettingStarted/Sandbox
      - type: OpenAPI
        url: openapi/amc-theatres-api-openapi.yml
      - type: SpectralRules
        url: rules/amc-theatres-rules.yml
      - type: NaftikoCapability
        url: capabilities/movie-discovery.yaml
      - type: NaftikoCapability
        url: capabilities/ticket-purchase.yaml
      - type: NaftikoCapability
        url: capabilities/loyalty-management.yaml
      - type: NaftikoSharedCapability
        url: capabilities/shared/amc-theatres-api.yaml
      - type: JSONSchema
        url: json-schema/amc-theatres-theatre-schema.json
      - type: JSONSchema
        url: json-schema/amc-theatres-movie-schema.json
      - type: JSONSchema
        url: json-schema/amc-theatres-showtime-schema.json
      - type: JSONSchema
        url: json-schema/amc-theatres-order-schema.json
      - type: JSONSchema
        url: json-schema/amc-theatres-loyalty-account-schema.json
      - type: JSONSchema
        url: json-schema/amc-theatres-attribute-schema.json
      - type: JSONStructure
        url: json-structure/amc-theatres-theatre-structure.json
      - type: JSONStructure
        url: json-structure/amc-theatres-movie-structure.json
      - type: JSONStructure
        url: json-structure/amc-theatres-showtime-structure.json
      - type: JSONStructure
        url: json-structure/amc-theatres-order-structure.json
      - type: JSONStructure
        url: json-structure/amc-theatres-loyalty-account-structure.json
      - type: JSONLD
        url: json-ld/amc-entertainment-holdings-context.jsonld
      - type: Vocabulary
        url: vocabulary/amc-entertainment-holdings-vocabulary.yml
      - type: Example
        url: examples/amc-theatres-list-theatres-example.json
      - type: Example
        url: examples/amc-theatres-list-movies-now-playing-example.json
      - type: Example
        url: examples/amc-theatres-list-theatre-showtimes-example.json
      - type: Example
        url: examples/amc-theatres-create-order-example.json
      - type: Example
        url: examples/amc-theatres-get-loyalty-account-example.json
    overlays: []
common:
  - type: Website
    url: https://www.amctheatres.com
  - type: DeveloperPortal
    url: https://developers.amctheatres.com
  - type: Customers
    url: https://www.amctheatres.com/amcstubs
  - type: TermsOfService
    url: https://www.amctheatres.com/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.amctheatres.com/legal/privacy-policy
  - type: LinkedIn
    url: https://www.linkedin.com/company/amc-theatres
  - type: GitHub
    url: https://github.com/amctheatres
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
---
