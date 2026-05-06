---
aid: project44
name: project44
description: project44 is a supply chain visibility platform that provides real-time shipment tracking, predictive ETAs, freight booking, rating, document management, and analytics across truckload, LTL, ocean, rail, air, and parcel modes. The Movement platform exposes RESTful APIs and webhooks for shippers, carriers, and logistics service providers.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/project44/refs/heads/main/apis.yml
tags:
  - Logistics
  - Freight
  - Supply Chain
  - Visibility
  - Tracking
  - Transportation
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: project44:project44-tracking-api
    name: project44 Tracking API
    description: The project44 Tracking API provides real-time multimodal shipment tracking, predictive ETAs, status updates, and exception alerts across truckload, LTL, ocean, rail, air, and parcel modes. Shippers and LSPs use it to integrate visibility into TMS, OMS, and customer-facing systems.
    humanURL: https://developers.project44.com/
    tags:
      - Tracking
      - Visibility
      - Shipments
      - ETA
    properties:
      - type: Documentation
        url: https://developers.project44.com/
      - type: OpenAPI
        url: openapi/project44-tracking-openapi.yml
      - type: AsyncAPI
        url: asyncapi/project44-shipment-events-asyncapi.yml
      - type: JSONSchema
        url: json-schema/project44-shipment-schema.json
  - aid: project44:project44-ltl-api
    name: project44 LTL API
    description: The project44 LTL API supports less-than-truckload workflows including rate quoting, dispatch, electronic bills of lading, image retrieval, and address book management across the LCL carrier network.
    humanURL: https://developers.project44.com/
    tags:
      - LTL
      - Quoting
      - Dispatch
      - Freight
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-tl-api
    name: project44 Truckload API
    description: The project44 Truckload (TL) API enables management of available vehicles, connected capacity, dispatch, and tracking for full truckload shipments across the carrier network.
    humanURL: https://developers.project44.com/
    tags:
      - Truckload
      - Capacity
      - Dispatch
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-rating-api
    name: project44 Rating API
    description: The project44 Rating API provides freight rate retrieval, quote generation, and carrier rate comparison across multiple modes to support procurement and real-time spot market pricing.
    humanURL: https://developers.project44.com/
    tags:
      - Rating
      - Pricing
      - Quoting
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-booking-api
    name: project44 Booking API
    description: The project44 Booking API enables programmatic freight booking, carrier tendering, and shipment dispatch across truckload, LTL, and multimodal shipments, integrating with carrier networks and TMS platforms.
    humanURL: https://developers.project44.com/
    tags:
      - Booking
      - Tendering
      - Dispatch
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-documents-api
    name: project44 Documents API
    description: The project44 Documents API enables retrieval, upload, and management of freight documents including bills of lading, proof of delivery, and customs documentation across the shipment lifecycle.
    humanURL: https://developers.project44.com/
    tags:
      - Documents
      - BOL
      - POD
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-yard-management-api
    name: project44 Yard Management API
    description: The project44 Yard Management System (YMS) API manages appointments, capacity planning, milestones, reason codes, site codes, and slot scheduling for yard operations and dock management.
    humanURL: https://developers.project44.com/
    tags:
      - Yard Management
      - Appointments
      - Dock Scheduling
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-rail-api
    name: project44 Rail API
    description: The project44 Rail API provides rail asset enrollment and tracking for intermodal and rail freight shipments, supporting visibility across rail networks.
    humanURL: https://developers.project44.com/
    tags:
      - Rail
      - Intermodal
      - Tracking
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-analytics-api
    name: project44 Analytics API
    description: The project44 Analytics API provides carrier performance metrics, port intelligence, on-time delivery analytics, lane benchmarking, and supply chain KPI data for transportation intelligence and carrier scorecarding.
    humanURL: https://developers.project44.com/
    tags:
      - Analytics
      - Performance
      - Port Intelligence
    properties:
      - type: Documentation
        url: https://developers.project44.com/
  - aid: project44:project44-webhooks-api
    name: project44 Webhooks API
    description: The project44 Webhooks API delivers real-time event notifications for shipments, inventory, orders, and loads, allowing customers to subscribe to lifecycle events and react to status changes asynchronously.
    humanURL: https://developers.project44.com/
    tags:
      - Webhooks
      - Events
      - Notifications
    properties:
      - type: Documentation
        url: https://developers.project44.com/
      - type: AsyncAPI
        url: asyncapi/project44-shipment-events-asyncapi.yml
common:
  - type: Portal
    url: https://developers.project44.com/
  - type: Documentation
    url: https://developers.project44.com/
  - type: Website
    url: https://www.project44.com/
  - type: Status
    url: https://status.project44.com/
  - type: PrivacyPolicy
    url: https://www.project44.com/privacy/
  - type: Terms of Service
    url: https://www.project44.com/legal/
  - type: GitHub Organization
    url: https://github.com/project44
  - type: JSON-LD
    url: json-ld/project44-context.jsonld
  - type: JSONSchema
    url: json-schema/project44-shipment-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
