---
aid: manhattan-associates
url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/apis.yml
apis:
- aid: manhattan-associates:manhattan-active-platform-api
  name: Manhattan Active Platform API
  tags:
  - Logistics
  - Platform
  - SaaS
  - Supply Chain
  image: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/image.png
  humanURL: https://platform.developer.manh.com/
  baseURL: https://api.developer.manh.com
  properties:
  - url: https://platform.developer.manh.com/
    type: Documentation
  - url: https://developer.manh.com/docs/getting-started
    type: GettingStarted
  - url: https://developer.manh.com/docs/how-to/rest-api/
    type: Authentication
  description: Manhattan Active Platform APIs provide core platform capabilities for authentication, tenant configuration, and integration with Manhattan Active solutions. REST APIs follow OAuth client credentials flows and require platform administrator setup.
- aid: manhattan-associates:manhattan-active-omni-api
  name: Manhattan Active Omni and Enterprise Promise & Fulfill API
  tags:
  - Fulfillment
  - Logistics
  - Omnichannel
  - Order Management
  image: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/image.png
  humanURL: https://omni.developer.manh.com/
  baseURL: https://api.developer.manh.com
  properties:
  - url: https://omni.developer.manh.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/openapi/manhattan-associates-omni-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/json-schema/manhattan-associates-order-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/json-ld/manhattan-associates-context.jsonld
    type: JSONLDContext
  description: Manhattan Active Omni APIs enable omnichannel order management and fulfillment, including order promising, order orchestration, inventory availability, and customer service operations for retail and distribution.
- aid: manhattan-associates:manhattan-active-supply-chain-api
  name: Manhattan Active Supply Chain API
  tags:
  - Logistics
  - Supply Chain
  - Warehouse
  - WMS
  image: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/image.png
  humanURL: https://supplychain.developer.manh.com/
  baseURL: https://api.developer.manh.com
  properties:
  - url: https://supplychain.developer.manh.com/
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/openapi/manhattan-associates-wms-openapi.yml
    type: OpenAPI
  description: Manhattan Active Supply Chain APIs provide warehouse management (WMS) capabilities including inventory tracking, order processing, labor management, yard management, and shipment execution for distribution center operations.
- aid: manhattan-associates:manhattan-active-supply-chain-planning-api
  name: Manhattan Active Supply Chain Planning API
  tags:
  - Inventory Planning
  - Logistics
  - Planning
  - Supply Chain
  image: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/image.png
  humanURL: https://scp.developer.manh.com/
  baseURL: https://api.developer.manh.com
  properties:
  - url: https://scp.developer.manh.com/
    type: Documentation
  description: Manhattan Active Supply Chain Planning APIs provide demand forecasting, inventory optimization, and replenishment planning capabilities to optimize stock levels and reduce carrying costs across supply chain networks.
- aid: manhattan-associates:manhattan-associates-api
  name: Manhattan Associates TMS/WMS API
  tags:
  - Logistics
  - Supply Chain
  - Transportation
  - Warehouse
  image: https://raw.githubusercontent.com/api-evangelist/manhattan-associates/refs/heads/main/image.png
  humanURL: https://www.manh.com/
  baseURL: https://api.manh.example.com
  properties:
  - url: https://www.manh.com/
    type: Documentation
  description: Manhattan Associates provides warehouse management (WMS) and transportation management (TMS) APIs for supply chain execution. APIs enable order management, inventory tracking, shipment planning, labor management, and yard management for distribution and logistics operations.
name: Manhattan Associates
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Manhattan Associates is a leading provider of supply chain commerce solutions, enabling unified commerce across stores, warehouses, and inventory across the supply chain.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

