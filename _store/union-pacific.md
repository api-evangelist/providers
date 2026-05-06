---
aid: union-pacific
url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/apis.yml
apis:
  - aid: union-pacific:union-pacific
    name: Union Pacific API
    tags:
      - Freight
      - Railroads
      - Shipping
      - Trains
      - Supply Chain
      - Logistics
    humanURL: https://www.up.com/customers/all/api-developer/index.htm
    baseURL: https://api.up.com
    properties:
      - url: https://www.up.com/customers/all/api-developer/index.htm
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/openapi/union-pacific-api.yaml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/rules/union-pacific-spectral-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/capabilities/shared/union-pacific-api.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/capabilities/rail-freight-operations.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/vocabulary/union-pacific-vocabulary.yaml
        type: Vocabulary
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-ld/union-pacific-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-shipment-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-case-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-equipment-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-location-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-waybill-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-intermodal-reservation-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-intermodal-lane-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-intermodal-departure-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-account-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-action-response-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-order-equipment-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-release-shipment-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-schema/union-pacific-cancel-request-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-shipment-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-case-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-equipment-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-location-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-intermodal-reservation-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/json-structure/union-pacific-waybill-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/examples/union-pacific-list-shipments-example.json
        type: Example
      - url: https://raw.githubusercontent.com/api-evangelist/union-pacific/refs/heads/main/examples/union-pacific-create-intermodal-reservation-example.json
        type: Example
    description: The Union Pacific API provides programmatic access to real-time railroad supply chain data and operational actions. The API enables shipment tracking, equipment management, order placement, exception case management, and intermodal planning. APIs are structured as data objects that can be used standalone or combined to create robust supply chain workflows. Authentication uses OAuth 2.0 Client Credentials flow.
    data:
      - name: Features
        data:
          - name: Real-Time Shipment Tracking
            description: Track active rail shipments with current location and estimated arrival times
          - name: Exception Case Management
            description: Monitor and resolve supply chain exceptions for off-course or delayed shipments
          - name: Equipment Management
            description: Search, order, and release rail car equipment including intermodal containers
          - name: Intermodal Planning
            description: Create reservations, find service lanes, and view departure schedules for intermodal transport
          - name: Network Locations
            description: Access Union Pacific facility, yard, and terminal location data across the network
          - name: Waybill Lookup
            description: Retrieve waybill documents with shipment routing and billing information
          - name: OAuth 2.0 Security
            description: Secure API access using OAuth 2.0 Client Credentials flow
      - name: UseCases
        data:
          - name: Supply Chain Visibility
            description: Logistics managers monitor active shipments across the UP network in real time
          - name: Exception Resolution
            description: Operations teams identify and resolve shipment exceptions to minimize delays
          - name: Intermodal Logistics
            description: Shippers book intermodal container space between UP terminals for coast-to-coast transport
          - name: Equipment Procurement
            description: Businesses order rail car equipment for upcoming shipping needs
          - name: Supply Chain Integration
            description: ERP and TMS platforms integrate UP freight data via API for automated logistics workflows
      - name: Integrations
        data:
          - name: ERP Systems
            description: Integrate with SAP, Oracle, and other ERP platforms for automated freight management
          - name: TMS Platforms
            description: Connect transportation management systems to UP rail data for multimodal planning
          - name: Supply Chain Platforms
            description: Embed UP tracking and exception data in supply chain visibility platforms
          - name: Warehouse Management
            description: Synchronize inbound rail shipment ETAs with warehouse receiving operations
name: Union Pacific
tags:
  - Freight
  - Railroads
  - Shipping
  - Trains
  - Supply Chain
  - Logistics
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-05-03'
position: Consumer
description: Union Pacific is one of the largest freight railroad networks in the United States, operating across 23 states in the western two-thirds of the country. The company transports a diverse range of commodities including agricultural products, automotive goods, chemicals, energy resources, and industrial materials. Union Pacific's API platform gives businesses programmatic access to real-time shipment tracking, equipment management, intermodal planning, and supply chain exception handling, enabling seamless integration with logistics and supply chain management systems.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
