---
aid: wegowise
name: WegoWise
description: WegoWise (now Comply by Measurabl) is a building energy and water benchmarking platform enabling property owners, managers, and energy service providers to programmatically manage building portfolios, track utility meter data, and benchmark energy and water performance. The REST API supports building management, apartment and commercial area tracking, utility meter data import, and normalized monthly usage analytics across multifamily and commercial properties.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Benchmarking
  - Building Energy
  - Energy Efficiency
  - Multifamily
  - Property Management
  - Utility Data
created: '2025-05-02'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/wegowise/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: wegowise:wegowise
    name: WegoWise API
    description: The WegoWise REST API (now Comply API) for managing building portfolios, utility meters, and energy data. Supports buildings, apartments, commercial areas, developments, meters, and raw usage datapoints. Authenticated via OAuth 1.0.
    humanURL: https://www.wegowise.com/api
    baseUrl: https://www.wegowise.com
    tags:
      - Apartments
      - Benchmarking
      - Buildings
      - Developments
      - Energy Data
      - Meters
      - REST
      - Utility Companies
      - Water Data
    properties:
      - type: Documentation
        url: https://www.wegowise.com/api
      - type: OpenAPI
        url: openapi/wegowise-openapi.yml
      - type: JSONSchema
        url: json-schema/wegowise-building-schema.json
      - type: JSONSchema
        url: json-schema/wegowise-meter-schema.json
      - type: JSONStructure
        url: json-structure/wegowise-building-structure.json
      - type: JSONLD
        url: json-ld/wegowise-context.jsonld
  - aid: wegowise:wegowise-pro
    name: WegoWise Pro API
    description: The WegoPro API for multifamily and commercial property portfolios. Provides endpoints for buildings, apartments, areas, meters, raw data, and monthly normalized usage data. The primary API for property managers.
    humanURL: https://www.wegowise.com/api/wego_pro
    baseUrl: https://www.wegowise.com/api/v1/wego_pro
    tags:
      - Apartments
      - Buildings
      - Commercial Areas
      - Multifamily
      - Pro
    properties:
      - type: Documentation
        url: https://www.wegowise.com/api/wego_pro
  - aid: wegowise:wegowise-data
    name: WegoWise Data API
    description: 'The WegoData API for data-only accounts. Enables meter management and automated utility data import without the full building structure hierarchy. Supports all utility types: Electric, Gas, Oil, Water, Steam, Propane, Solar.'
    humanURL: https://www.wegowise.com/api/wego_data
    baseUrl: https://www.wegowise.com/api/v1/wego_data
    tags:
      - Automated Import
      - Data Only
      - Meters
      - Utility Data
    properties:
      - type: Documentation
        url: https://www.wegowise.com/api/wego_data
  - aid: wegowise:wegowise-public
    name: WegoWise Public API
    description: Public endpoints accessible without authentication. Provides a list of utility companies supported for automated data import, useful for finding utility_company_id values when configuring meters.
    humanURL: https://www.wegowise.com/api/public
    baseUrl: https://www.wegowise.com/api/v1
    tags:
      - Public
      - Utility Companies
    properties:
      - type: Documentation
        url: https://www.wegowise.com/api/public
common:
  - type: Documentation
    url: https://www.wegowise.com/api
  - type: Website
    url: https://www.wegowise.com
  - type: Product Tour
    url: https://www.wegowise.com/tour
  - type: Energy Service Providers
    url: https://www.wegowise.com/customer-profiles/energy-service-providers
  - type: Compliance
    url: https://www.wegowise.com/compliance
  - type: Blog
    url: http://blog.wegowise.com/
  - type: SpectralRules
    url: rules/wegowise-rules.yml
  - type: Vocabulary
    url: vocabulary/wegowise-vocabulary.yml
  - type: JSONLD
    url: json-ld/wegowise-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
