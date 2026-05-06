---
aid: stadia-maps
url: https://raw.githubusercontent.com/api-evangelist/stadia-maps/refs/heads/main/apis.yml
name: Stadia Maps
description: Stadia Maps is a cutting-edge mapping platform providing high-quality, detailed maps and location APIs for developers. The platform offers routing and navigation, geocoding and search, elevation data, time zone lookups, isochrone analysis, and account management. Stadia Maps delivers GDPR-compliant EU endpoints, rich map styling options, and official SDKs for TypeScript, Python, Swift, Kotlin, and PHP. Trusted by developers building web, mobile, and data visualization applications worldwide.
tags:
  - Mapping
  - Maps
  - Geocoding
  - Routing
  - Navigation
  - Geospatial
  - Location
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-16'
modified: '2026-05-02'
position: Consuming
common:
  - url: https://stadiamaps.com/
    type: Portal
  - url: https://docs.stadiamaps.com/
    type: Documentation
  - url: https://docs.stadiamaps.com/api-reference/
    type: API Reference
  - url: https://stadiamaps.com/pricing/
    type: Pricing
  - url: https://stadiamaps.com/contact/
    type: Contact
  - url: https://docs.stadiamaps.com/authentication/
    type: Authentication
  - url: https://github.com/stadiamaps
    type: GitHub Organization
  - url: https://www.npmjs.com/package/@stadiamaps/api
    type: SDK
  - url: https://pypi.org/project/stadiamaps-api/
    type: SDK
apis:
  - aid: stadia-maps:stadia-maps
    name: Stadia Maps Geospatial API
    tags:
      - Attributes
      - Autocomplete
      - Elevation
      - Geospatial
      - Geocoding
      - Isochrone
      - Lookups
      - Mapping
      - Match
      - Navigation
      - Place
      - Reverse
      - Roads
      - Routes
      - Routing
      - Search
      - Time Zone
    humanURL: https://docs.stadiamaps.com/
    baseURL: https://api.stadiamaps.com
    description: The Stadia Maps Geospatial API provides routing and turn-by-turn navigation, geocoding and autocomplete search, reverse geocoding, place lookups, elevation profiles, time zone information, road attributes, isochrones, map matching, time-distance matrices, and optimized routing. Secured with API key authentication. EU-region endpoint available for GDPR compliance.
    properties:
      - url: https://docs.stadiamaps.com/
        type: Documentation
      - url: openapi/stadia-maps-openapi.yml
        type: OpenAPI
      - url: https://docs.stadiamaps.com/authentication/
        type: Authentication
      - url: https://docs.stadiamaps.com/routing/
        type: Documentation
      - url: https://docs.stadiamaps.com/geocoding-search-autocomplete/
        type: Documentation
      - url: rules/stadia-maps-rules.yml
        type: SpectralRuleset
      - url: capabilities/geospatial-services.yaml
        type: NaftikoCapability
      - url: json-schema/stadia-maps-location-schema.json
        type: JSONSchema
      - url: json-ld/stadia-maps-context.jsonld
        type: JSONLDContext
      - url: vocabulary/stadia-maps-vocabulary.yml
        type: Vocabulary
  - aid: stadia-maps:stadia-maps-account-management
    name: Stadia Maps Account Management API
    tags:
      - Account Management
      - API Keys
      - Domains
      - Properties
    humanURL: https://docs.stadiamaps.com/client-api/
    baseURL: https://client.stadiamaps.com/api/v1
    description: The Stadia Maps Account Management API enables programmatic management of properties, domains, and API keys. Useful for managing large numbers of properties, automating domain allowlisting, and programmatically rotating API keys. Access is available on request.
    properties:
      - url: https://docs.stadiamaps.com/client-api/
        type: Documentation
      - url: https://client.stadiamaps.com/api/v1/openapi/
        type: OpenAPI
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
