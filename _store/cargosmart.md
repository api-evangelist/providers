---
aid: cargosmart
url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/apis.yml
name: CargoSmart
description: CargoSmart (now operating as IQAX) is a global shipment management software provider that gives shippers, consignees, freight forwarders, and logistics service providers ocean freight booking, container tracking, vessel scheduling, and shipping documentation tools across multiple ocean carriers. CargoSmart co-founded the Global Shipping Business Network (GSBN), a blockchain-based data exchange for carriers, terminals, banks, and customs authorities, and exposes its APIs so trading partners can embed booking, visibility, schedule, and documentation workflows directly into TMS, ERP, and supply-chain platforms.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
tags:
  - Booking
  - Container
  - Documentation
  - GSBN
  - IQAX
  - Logistics
  - Maritime
  - Ocean Freight
  - Schedule
  - Shipping
  - Supply Chain
  - Tracking
  - Visibility
  - Vessel
created: '2025-01-15'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: cargosmart:cargosmart-container-booking-api
    name: CargoSmart Container Booking API
    description: The CargoSmart Container Booking API enables programmatic submission of container booking requests across multiple ocean carriers. APIs support booking creation, amendment, cancellation, and confirmation workflows for shippers, NVOCCs, and logistics service providers.
    humanURL: https://www.cargosmart.com/
    baseURL: https://api.cargosmart.com
    tags:
      - Booking
      - Container
      - Logistics
      - Maritime
      - Ocean Freight
      - Shipping
    image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
    properties:
      - url: https://www.cargosmart.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
        type: OpenAPI
    x-features:
      - Multi-carrier container booking submission
      - Booking creation, amendment, and cancellation
      - Acknowledgment and confirmation callbacks
      - Shipper, NVOCC, and LSP role support
      - Integration with carrier back-ends via CargoSmart
    x-use-cases:
      - Shipper TMS booking automation
      - NVOCC consolidation booking
      - Freight forwarder tender flow
      - Enterprise ERP-to-carrier booking integration
  - aid: cargosmart:cargosmart-shipment-tracking-api
    name: CargoSmart Shipment Tracking API
    description: The CargoSmart Shipment Tracking API provides real-time container tracking and shipment visibility across ocean carriers and ports. APIs return container movement events, vessel positions, ETA predictions, and port arrival/departure data for supply chain visibility platforms. An accompanying AsyncAPI channel emits milestone events so subscribers can react without polling.
    humanURL: https://www.cargosmart.com/
    baseURL: https://api.cargosmart.com
    tags:
      - Container
      - Logistics
      - Maritime
      - Shipping
      - Tracking
      - Visibility
    image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
    properties:
      - url: https://www.cargosmart.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/asyncapi/cargosmart-events-asyncapi.yml
        type: AsyncAPI
    x-features:
      - Real-time container movement events
      - Vessel position and ETA predictions
      - Port arrival/departure milestones
      - AsyncAPI event channel for push delivery
      - Cross-carrier normalized schema
      - Exception and delay detection
    x-use-cases:
      - Supply-chain visibility platforms
      - Customer self-service tracking portals
      - Proactive exception management and ETA-based allocation
      - Carrier performance analytics
  - aid: cargosmart:cargosmart-vessel-schedule-api
    name: CargoSmart Vessel Schedule API
    description: The CargoSmart Vessel Schedule API provides access to ocean carrier vessel schedules, port rotation data, and sailing frequency information. APIs support route planning, transit time calculation, and carrier selection for ocean freight shippers and forwarders.
    humanURL: https://www.cargosmart.com/
    baseURL: https://api.cargosmart.com
    tags:
      - Logistics
      - Maritime
      - Port
      - Schedule
      - Shipping
      - Vessel
    image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
    properties:
      - url: https://www.cargosmart.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
        type: OpenAPI
    x-features:
      - Carrier vessel schedule lookup
      - Port rotation and sailing frequency data
      - Transit time calculation by lane
      - Multi-carrier normalized schema
    x-use-cases:
      - Route planning and carrier selection
      - Transit time SLAs for customer quotes
      - Sailing calendar feeds in TMS platforms
  - aid: cargosmart:cargosmart-shipping-documents-api
    name: CargoSmart Shipping Documentation API
    description: The CargoSmart Shipping Documentation API enables electronic exchange of shipping documents including bills of lading, cargo manifests, and customs declarations. APIs and EDI integrations support paperless documentation workflows across carriers, ports, customs authorities, and logistics service providers.
    humanURL: https://www.cargosmart.com/
    baseURL: https://api.cargosmart.com
    tags:
      - Bill of Lading
      - Container
      - Documentation
      - EDI
      - Maritime
      - Shipping
    image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
    properties:
      - url: https://www.cargosmart.com/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
        type: OpenAPI
    x-features:
      - Bill of lading and manifest exchange
      - Customs declaration integration
      - API plus EDI support
      - GSBN-aligned document workflows
    x-use-cases:
      - Paperless carrier documentation
      - Port and customs authority integration
      - LSP document hub aggregation
common:
  - url: https://www.cargosmart.com
    type: Website
  - url: https://www.cargosmart.com/
    type: Portal
  - url: https://www.cargosmart.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/asyncapi/cargosmart-events-asyncapi.yml
    type: AsyncAPI
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-schema/cargosmart-container-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-schema/cargosmart-booking-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-ld/cargosmart-context.jsonld
    type: JSONLDContext
  - type: GSBN
    url: https://www.gsbn.trade/
  - type: IQAX
    url: https://www.iqax.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/cargosmart-limited/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
