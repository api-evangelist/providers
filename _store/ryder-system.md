---
aid: ryder-system
name: Ryder System
description: Ryder System, Inc. is a leading provider of supply chain, dedicated transportation, and fleet management solutions. Ryder operates a developer portal offering REST APIs for fleet management and supply chain operations, enabling customers to integrate Ryder services into their business systems. The Fleet Management APIs support customers who lease, rent, and maintain vehicles, while the Supply Chain Solutions APIs support carrier management, load tracking, shipment management, and last-mile delivery operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Fleet Management
  - Logistics
  - Supply Chain
  - Transportation
  - Trucking
url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: ryder-system:fleet-management-api
    name: Ryder Fleet Management API
    description: The Ryder Fleet Management API (FMS) enables seamless integration of fleet and location data into business systems. It provides access to Ryder fleet details including vehicle information and specifications, location data with address and service hours, historical maintenance records, and invoice details with line items and payment status. Requires API key authentication via the Ocp-Apim-Subscription-Key header.
    humanURL: https://developer.ryder.com/fms/overview
    baseURL: https://developer.ryder.com/fms/apis
    tags:
      - Fleet Management
      - Invoices
      - Locations
      - Service History
      - Vehicles
    properties:
      - type: Documentation
        url: https://developer.ryder.com/fms/docs/fms-fleet-api/overview
      - type: GettingStarted
        url: https://developer.ryder.com/fms/docs/fms-fleet-api/getting-started
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/openapi/ryder-fleet-management-api-openapi.yml
  - aid: ryder-system:carrier-api
    name: Ryder Carrier API
    description: The Ryder Carrier API enables carriers to push updates to Ryder for managing transportation, brokerage, and tracking services. It supports resource assignment and tracking for load tenders, event updates for load events and milestones, vehicle locations, and document uploads to the RyderShare platform.
    humanURL: https://developer.ryder.com/scs/docs/scs-carrier/overview
    baseURL: https://api.ryder.com/rcsc/events/v1
    tags:
      - Carrier Management
      - Load Tracking
      - Supply Chain
      - Transportation
    properties:
      - type: Documentation
        url: https://developer.ryder.com/scs/docs/scs-carrier/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/openapi/ryder-carrier-api-openapi.yml
  - aid: ryder-system:tm-shipment-api
    name: Ryder TM Shipment Management API
    description: The Ryder TM Shipment Management API enables seamless integration for customers to manage shipments, loads, and tracking updates. It uses OAuth 2.0 Client Credentials flow via Okta combined with an API subscription key. Supports Shipment, Load, Ship Confirmation, Ship Status, and Event Notifications.
    humanURL: https://developer.ryder.com/scs/docs/tm-shipment-management/overview
    baseURL: https://api.ryder.com/tmshipment/v1
    tags:
      - Shipment Management
      - Supply Chain
      - Transportation
    properties:
      - type: Documentation
        url: https://developer.ryder.com/scs/docs/tm-shipment-management/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/openapi/ryder-tm-shipment-api-openapi.yml
  - aid: ryder-system:last-mile-api
    name: Ryder Last Mile API
    description: The Ryder Last Mile API handles last-mile delivery operations, enabling integration with Ryder's last-mile delivery network for e-commerce fulfillment and parcel delivery management.
    humanURL: https://developer.ryder.com/scs/docs/ryder-last-mile/overview
    tags:
      - E-Commerce
      - Last Mile Delivery
      - Supply Chain
    properties:
      - type: Documentation
        url: https://developer.ryder.com/scs/docs/ryder-last-mile/overview
  - aid: ryder-system:3pa-load-tracking-api
    name: Ryder 3PA Load Tracking API
    description: The Ryder 3PA Load Tracking API provides third-party logistics load tracking functionality, enabling visibility into load status and location throughout the shipment lifecycle.
    humanURL: https://developer.ryder.com/scs/docs/3pa-load-tracking/overview
    tags:
      - Load Tracking
      - Logistics
      - Supply Chain
    properties:
      - type: Documentation
        url: https://developer.ryder.com/scs/docs/3pa-load-tracking/overview
common:
  - type: Website
    url: https://www.ryder.com
  - type: DeveloperPortal
    url: https://developer.ryder.com
  - type: Documentation
    url: https://developer.ryder.com/fms/overview
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/vocabulary/ryder-system-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-ld/ryder-system-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/rules/ryder-spectral-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/capabilities/fleet-operations.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/capabilities/supply-chain-visibility.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-schema/ryder-vehicle-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ryder-system/refs/heads/main/json-schema/ryder-shipment-schema.json
  - type: Features
    data:
      - 'Ryder System: API access via partner / B2B contracts only'
      - No public API pricing published — contact enterprise sales
      - Ryder fleet management and logistics APIs offered to commercial clients via Ryder Connect.
    sources:
      - https://ryder.com/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
