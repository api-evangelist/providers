---
aid: arcbest
name: ArcBest
description: ArcBest is a logistics company offering less-than-truckload (LTL) freight, truckload, moving, and supply chain management services. The ArcBest API platform provides integration capabilities for freight rating, booking, tracking, and supply chain visibility.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Logistics
  - Freight
  - LTL
  - Supply Chain
  - Shipping
  - Transportation
url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: arcbest:arcbest-api
    name: ArcBest API
    description: The ArcBest API provides programmatic access to freight services including LTL rate quotes, shipment booking, tracking, BOL generation, and supply chain visibility. Access is by invitation only.
    humanURL: https://www.arcbest.com/
    tags:
      - LTL Freight
      - Rate Quote
      - Shipment Tracking
      - BOL
      - Supply Chain
    properties:
      - type: Documentation
        url: https://www.arcbest.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/openapi/arcbest-api.yaml
common:
  - type: Portal
    url: https://www.arcbest.com/
  - type: SignUp
    url: https://www.arcbest.com/
  - type: Features
    data:
      - name: LTL Rate Quotes
        description: Real-time less-than-truckload freight rate quotes with transit time estimates.
      - name: Shipment Booking
        description: API-based shipment booking and scheduling for LTL and truckload freight.
      - name: Shipment Tracking
        description: Real-time tracking of freight shipments with status updates and delivery notifications.
      - name: BOL Generation
        description: Electronic Bill of Lading generation and management through API integration.
      - name: Pickup Scheduling
        description: Automated pickup scheduling and confirmation for outbound freight.
      - name: Supply Chain Visibility
        description: End-to-end supply chain visibility across ArcBest freight and logistics services.
  - type: UseCases
    data:
      - name: E-Commerce Shipping
        description: Integrate ArcBest freight rates and booking into e-commerce platforms for automated shipping.
      - name: ERP Integration
        description: Connect ArcBest freight services to ERP systems for automated freight procurement and accounting.
      - name: TMS Integration
        description: Integrate with Transportation Management Systems for multi-carrier freight optimization.
      - name: Warehouse Management
        description: Connect ArcBest pickup scheduling with warehouse management systems for outbound logistics automation.
  - type: Integrations
    data:
      - name: SAP
        description: Integration with SAP ERP for freight cost allocation and logistics management.
      - name: Oracle
        description: Connect to Oracle ERP and WMS systems for automated freight operations.
      - name: Salesforce
        description: Integrate shipment tracking and freight data with Salesforce CRM.
      - name: ShipStation
        description: Multi-carrier shipping management platform integration.
      - name: Shopify
        description: E-commerce platform integration for LTL freight rate display and booking.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/rules/arcbest-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/vocabulary/arcbest-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/arcbest/refs/heads/main/json-ld/arcbest-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
