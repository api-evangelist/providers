---
aid: shippo
url: https://raw.githubusercontent.com/api-evangelist/shippo/refs/heads/main/apis.yml
apis:
  - aid: shippo:shippo-api
    name: Shippo API
    tags:
      - Ecommerce
      - Labels
      - Logistics
      - Shipping
      - Tracking
    humanURL: https://docs.goshippo.com/
    properties:
      - url: https://docs.goshippo.com/
        type: Documentation
      - url: openapi/shippo-openapi.yml
        type: OpenAPI
      - url: https://docs.goshippo.com/spec/shippoapi/public-api.yaml
        type: OpenAPI
      - url: https://github.com/goshippo/shippo-python-sdk
        type: SDK
      - url: https://github.com/goshippo/shippo-javascript-sdk
        type: SDK
      - url: https://github.com/goshippo/shippo-php-client
        type: SDK
      - url: https://github.com/goshippo/shippo-java-client
        type: SDK
      - url: https://github.com/goshippo/shippo-ruby-client
        type: SDK
      - url: https://github.com/goshippo/shippo-node-client
        type: SDK
      - url: json-schema/shippo-shipment-schema.json
        type: JSONSchema
      - url: json-schema/shippo-transaction-schema.json
        type: JSONSchema
      - url: json-ld/shippo-context.jsonld
        type: JSONLD
      - url: rules/shippo-rules.yml
        type: SpectralRules
      - url: capabilities/shipping-fulfillment.yaml
        type: NaftikoCapabilities
      - url: vocabulary/shippo-vocabulary.yml
        type: Vocabulary
    description: Shippo is a multi-carrier shipping API that enables developers to add complete shipping functionality to their applications. The API supports address validation, carrier rate comparison across USPS, UPS, FedEx, DHL, and 80+ other carriers, label generation, package tracking, returns management, and webhook notifications. Shippo's API drives efficiency at scale from pre-purchase to returns.
name: Shippo
tags:
  - Ecommerce
  - Labels
  - Logistics
  - Returns
  - Shipping
  - Tracking
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-04'
position: Consumer
description: Shippo provides a robust shipping API architecture that helps developers drive efficiency at scale. The Shippo API covers the complete shipping lifecycle from pre-purchase rate shopping across 80+ carriers to label generation, package tracking, and returns management. SDKs are available for Python, JavaScript, PHP, Java, Ruby, and Node.js.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://docs.goshippo.com/
    type: Documentation
  - url: https://docs.goshippo.com/shippoapi/public-api
    type: API Reference
  - url: https://docs.goshippo.com/docs/guides_general/clientlibraries
    type: SDKs
  - url: https://support.goshippo.com/hc/en-us/articles/4404415886491-Shippo-API-Quick-Start-Guide
    type: Getting Started
  - url: https://goshippo.com/pricing/api
    type: Pricing
  - url: https://github.com/goshippo
    type: GitHub Organization
  - url: https://goshippo.com/products/api
    type: Developer Portal
  - url: https://goshippo.com
    type: Website
  - type: Features
    data:
      - 'API Starter: 30 free labels/mo + 7¢/label'
      - 'API Premier: custom volume discounts, 24/7 monitoring optional'
      - 40+ shipping carriers (USPS, FedEx, UPS, DHL, Royal Mail, Canada Post, etc.)
      - 'Address validation (US: included; non-US: $0.09 Starter, $0.06 Premier)'
      - Tracking webhooks
      - Returns labels
      - Insurance
      - Rating across carriers
      - REST API at api.goshippo.com
      - Default 250 req/min/token
      - Bearer token auth
      - Webhooks for shipment, transaction, batch events
      - Carrier accounts management API
      - Customs documents API
      - Batch label creation
      - API calls not associated with labels billed at API Starter rates
    sources:
      - https://goshippo.com/pricing/api
    updated: '2026-05-04'
---
