---
aid: shipstation
url: https://raw.githubusercontent.com/api-evangelist/shipstation/refs/heads/main/apis.yml
apis:
  - aid: shipstation:shipstation-v1-api
    name: ShipStation V1 API
    tags:
      - Ecommerce
      - Labels
      - Order Management
      - Shipping
    humanURL: https://www.shipstation.com/docs/api/
    properties:
      - url: https://www.shipstation.com/docs/api/
        type: Documentation
      - url: openapi/shipstation-v1-openapi.yml
        type: OpenAPI
      - url: json-schema/shipstation-order-schema.json
        type: JSONSchema
      - url: json-schema/shipstation-shipment-schema.json
        type: JSONSchema
      - url: json-ld/shipstation-context.jsonld
        type: JSONLD
      - url: rules/shipstation-rules.yml
        type: SpectralRules
      - url: capabilities/ecommerce-shipping.yaml
        type: NaftikoCapabilities
      - url: vocabulary/shipstation-vocabulary.yml
        type: Vocabulary
    description: The ShipStation V1 API provides programmatic access to ShipStation's shipping platform for ecommerce businesses. Endpoints cover order management, shipment creation, label generation, carrier rate shopping, package tracking, warehouse management, product management, and store integrations. Authentication uses HTTP Basic auth with API key and secret. Base URL is https://ssapi.shipstation.com with a rate limit of 40 requests per minute.
  - aid: shipstation:shipstation-v2-api
    name: ShipStation V2 API
    tags:
      - Ecommerce
      - Labels
      - Order Management
      - Shipping
    humanURL: https://docs.shipstation.com/
    properties:
      - url: https://docs.shipstation.com/
        type: Documentation
      - url: https://docs.shipstation.com/rest
        type: API Reference
    description: The ShipStation V2 API is the next-generation shipping and inventory API built on ShipEngine technology. It provides improved endpoints for creating orders, managing customers, querying order and shipping data, and integrating with ShipStation's multi-carrier shipping platform. Available to Standard plan and higher accounts with the API add-on.
name: ShipStation
tags:
  - Ecommerce
  - Labels
  - Logistics
  - Order Management
  - Shipping
  - Warehousing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-04'
position: Consumer
description: ShipStation is a leading shipping platform for ecommerce businesses providing APIs to integrate shipping workflows into applications. The ShipStation API enables developers to automate order management, create shipments, generate labels, track packages, manage warehouses, and connect to multiple carriers. ShipStation offers both V1 (ssapi.shipstation.com) and V2 (ShipEngine-powered) API versions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.shipstation.com/docs/api/
    type: Documentation
  - url: https://docs.shipstation.com/
    type: API Reference
  - url: https://docs.shipstation.com/getting-started
    type: Getting Started
  - url: https://www.shipstation.com/docs/api/requirements/
    type: Authentication
  - url: https://docs.shipstation.com/openapi/downloads
    type: OpenAPI
  - url: https://help.shipstation.com/hc/en-us/articles/360025856212-ShipStation-API
    type: Support
  - url: https://www.shipstation.com/legal/terms-of-service/
    type: Terms of Service
  - url: https://www.shipstation.com/legal/privacy-policy/
    type: Privacy Policy
  - url: https://www.shipstation.com
    type: Website
  - type: Features
    data:
      - 'Starter $14.99/mo: 50 shipments, 3 users'
      - 'Standard $29.99/mo: 50 shipments, 10 users, API access'
      - 'Premium $349.99/mo: advanced inventory + warehouse'
      - Unlimited store connections (Shopify, WooCommerce, BigCommerce, Amazon, eBay, Etsy, etc.)
      - Automated rate shopping across carriers
      - Bring your own carrier accounts
      - Return labels and exchanges
      - Shipping API v1 and v2
      - Default 40 req/min/account
      - Webhooks for order/shipment events
      - API key + secret auth
      - Auto-Routing (Premium)
      - Cubiscan integration (Premium)
      - Open Database Connectivity (ODBC) on Premium
      - Mobile app for label printing
      - Owned by Auctane (parent company)
    sources:
      - https://www.shipstation.com/pricing/
    updated: '2026-05-04'
---
