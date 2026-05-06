---
aid: rentcast
name: RentCast
description: RentCast provides a real estate data API with instant access to over 140 million property records, automated valuation models (AVM) for home value and rent estimates, active and historical sale and rental listings, and aggregate real estate market statistics for US zip codes. The API enables real estate investors, property managers, landlords, and proptech applications to programmatically access comprehensive residential and commercial property data across all 50 US states.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Real Estate
  - Property Data
  - Valuation
  - Rental Market
  - AVM
url: https://raw.githubusercontent.com/api-evangelist/rentcast/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rentcast:rentcast-api
    name: RentCast API
    description: The RentCast API provides programmatic access to US real estate data including 140+ million property records with ownership details, automated valuation model (AVM) rent and home value estimates with comparable properties, active and inactive sale and rental listings across all 50 states, and aggregate market statistics for zip codes. Authentication uses an X-Api-Key header. All endpoints are read-only GET requests.
    humanURL: https://www.rentcast.io/api
    baseURL: https://api.rentcast.io/v1
    tags:
      - Real Estate
      - Property Data
      - Valuation
      - Rental Market
    properties:
      - type: Documentation
        url: https://developers.rentcast.io/reference/introduction
      - type: OpenAPI
        url: openapi/rentcast-openapi.json
      - type: PostmanCollection
        url: https://www.postman.com/rentcast/rentcast-api/documentation/ca4yudw/rentcast-api-endpoints
      - type: GitHubOrganization
        url: https://github.com/RentCast
      - type: Rules
        url: rules/rentcast-rules.yml
      - type: Capabilities
        url: capabilities/property-research.yaml
      - type: JSONSchema
        url: json-schema/rentcast-property-schema.json
      - type: JSONStructure
        url: json-structure/rentcast-property-structure.json
      - type: JSONLD
        url: json-ld/rentcast-context.jsonld
      - type: Vocabulary
        url: vocabulary/rentcast-vocabulary.yml
common:
  - url: https://www.rentcast.io
    name: RentCast
    type: Website
    description: RentCast real estate data platform homepage
  - url: https://developers.rentcast.io
    name: RentCast Developer Portal
    type: Portal
    description: API documentation and developer resources
  - url: https://app.rentcast.io/app/api
    name: RentCast API Dashboard
    type: Portal
    description: API key management and usage dashboard
  - url: https://www.rentcast.io/api
    name: RentCast API
    type: Documentation
    description: Overview of RentCast API features and pricing
  - url: https://help.rentcast.io
    name: RentCast Help Center
    type: Support
    description: Help articles and support documentation
  - url: https://www.rentcast.io/blog
    name: RentCast Blog
    type: Blog
    description: Product updates and real estate data insights
  - url: https://github.com/RentCast
    name: RentCast GitHub
    type: GitHubOrganization
    description: OpenAPI specs, Postman collections, and developer resources
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
