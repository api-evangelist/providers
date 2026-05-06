---
aid: cities-database-api
name: Cities Database API
url: https://raw.githubusercontent.com/api-evangelist/cities-database-api/refs/heads/main/apis.yml
created: '2024-03-30'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Cities
  - Data
  - Geography
  - Locations
  - Reference Data
  - Travel
description: The Cities Database API by AirLabs provides a global reference dataset of cities keyed to IATA metropolitan area codes, ISO country codes, and geographic coordinates. The API is consumed alongside the AirLabs Airports, Airlines, and Flights APIs to power travel search, mapping, geocoding, and clustering experiences. Authentication uses an api_key query parameter obtained from the AirLabs account dashboard. All responses are JSON arrays of city objects.
apis:
  - aid: cities-database-api:airlabs-cities-api
    name: AirLabs Cities API
    tags:
      - Cities
      - Geography
      - IATA
      - Reference Data
      - Travel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://airlabs.co/api/v9
    humanURL: https://airlabs.co/docs/cities
    properties:
      - url: https://airlabs.co/docs/cities
        type: Documentation
      - url: https://airlabs.co/docs
        type: API Reference
      - url: https://airlabs.co/account/api-key
        type: Authentication
      - url: openapi/cities-database-api-openapi.yml
        type: OpenAPI
    description: The AirLabs Cities API exposes a single GET /cities endpoint that returns a list of cities filterable by IATA city_code, ISO 2 country_code, or comma-separated _fields. Free-tier responses include name, city_code, latitude, longitude, and country_code; paid tiers add UN/LOCODE, elevation, timezone, population, multilingual names, Wikipedia links, and SEO slugs. Authentication uses the api_key query parameter.
common:
  - type: Website
    url: https://airlabs.co/
  - type: Documentation
    url: https://airlabs.co/docs
  - type: Pricing
    url: https://airlabs.co/pricing
  - type: Sign Up
    url: https://airlabs.co/signup
  - type: Login
    url: https://airlabs.co/login
  - type: Account
    url: https://airlabs.co/account
  - type: Authentication
    url: https://airlabs.co/account/api-key
  - type: Privacy Policy
    url: https://airlabs.co/privacy
  - type: Terms of Service
    url: https://airlabs.co/terms
  - type: Support
    url: https://airlabs.co/contact
  - type: Status
    url: https://airlabs.co/status
  - type: JSON-LD
    url: json-ld/cities-database-api-context.jsonld
  - type: JSONSchema
    url: json-schema/cities-database-api-city-schema.json
  - type: Spectral
    url: rules/cities-database-api-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cities-database-api-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
