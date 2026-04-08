---
aid: cargosmart
url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/apis.yml
apis:
- aid: cargosmart:cargosmart-container-booking-api
  name: CargoSmart Container Booking API
  tags:
  - Booking
  - Container
  - Logistics
  - Maritime
  - Ocean Freight
  - Shipping
  image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
  humanURL: https://www.cargosmart.com/
  baseURL: https://api.cargosmart.com
  properties:
  - url: https://www.cargosmart.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
    type: OpenAPI
  description: The CargoSmart Container Booking API enables programmatic submission of container booking requests across multiple ocean carriers. APIs support booking creation, amendment, cancellation, and confirmation workflows for shippers, NVOCCs, and logistics service providers.
- aid: cargosmart:cargosmart-shipment-tracking-api
  name: CargoSmart Shipment Tracking API
  tags:
  - Container
  - Logistics
  - Maritime
  - Shipping
  - Tracking
  - Visibility
  image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
  humanURL: https://www.cargosmart.com/
  baseURL: https://api.cargosmart.com
  properties:
  - url: https://www.cargosmart.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/asyncapi/cargosmart-events-asyncapi.yml
    type: AsyncAPI
  description: The CargoSmart Shipment Tracking API provides real-time container tracking and shipment visibility across ocean carriers and ports. APIs return container movement events, vessel positions, ETA predictions, and port arrival/departure data for supply chain visibility platforms.
- aid: cargosmart:cargosmart-vessel-schedule-api
  name: CargoSmart Vessel Schedule API
  tags:
  - Logistics
  - Maritime
  - Port
  - Schedule
  - Shipping
  - Vessel
  image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
  humanURL: https://www.cargosmart.com/
  baseURL: https://api.cargosmart.com
  properties:
  - url: https://www.cargosmart.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
    type: OpenAPI
  description: The CargoSmart Vessel Schedule API provides access to ocean carrier vessel schedules, port rotation data, and sailing frequency information. APIs support route planning, transit time calculation, and carrier selection for ocean freight shippers and forwarders.
- aid: cargosmart:cargosmart-shipping-documents-api
  name: CargoSmart Shipping Documentation API
  tags:
  - Bill of Lading
  - Container
  - Documentation
  - EDI
  - Maritime
  - Shipping
  image: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/image.png
  humanURL: https://www.cargosmart.com/
  baseURL: https://api.cargosmart.com
  properties:
  - url: https://www.cargosmart.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
    type: OpenAPI
  description: The CargoSmart Shipping Documentation API enables electronic exchange of shipping documents including bills of lading, cargo manifests, and customs declarations. APIs and EDI integrations support paperless documentation workflows across carriers, ports, customs authorities, and logistics service providers.
name: Cargosmart
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CargoSmart is a global shipment management software solutions provider that helps shippers, consignees, freight forwarders, and logistics service providers improve shipment planning, visibility, and collaboration.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

