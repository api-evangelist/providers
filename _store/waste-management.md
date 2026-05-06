---
aid: waste-management
name: Waste Management
description: Waste Management (WM) is the largest environmental services company in North America, providing waste collection, transfer, disposal, and recycling services to over 20 million residential, commercial, industrial, and municipal customers across the United States. WM provides RESTful APIs for customers and third-party integrators to access account data including balance, services, invoices, pickup schedules, and ETAs via JWT authentication.
url: https://www.wm.com
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Environmental Services
  - Fortune 500
  - Recycling
  - Solid Waste
  - Sustainability
  - Waste Management
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: waste-management:waste-management-customer-api
    name: Waste Management Customer API
    description: The Waste Management Customer API provides RESTful access to customer account data including balance, contract details, invoice history, service details, pickup schedules, and ETA information. Uses JWT bearer token authentication with ClientId and Request-Tracking-Id headers.
    humanURL: https://api.wm.com/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://api.wm.com/
      - type: OpenAPI
        url: openapi/waste-management-customer-api-openapi.yml
      - type: SpectralRules
        url: rules/waste-management-rules.yml
    tags:
      - Customer API
      - Billing
      - Services
      - Pickup Scheduling
      - REST
common:
  - type: Website
    url: https://www.wm.com
  - type: Portal
    url: https://api.wm.com/
  - type: OpenAPI
    url: openapi/waste-management-customer-api-openapi.yml
  - type: SpectralRules
    url: rules/waste-management-rules.yml
  - type: JSONSchema
    url: json-schema/waste-management-service-schema.json
  - type: JSONSchema
    url: json-schema/waste-management-invoice-schema.json
  - type: JSONStructure
    url: json-structure/waste-management-service-structure.json
  - type: JSON-LD
    url: json-ld/waste-management-context.jsonld
  - type: Vocabulary
    url: vocabulary/waste-management-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/customer-service.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
