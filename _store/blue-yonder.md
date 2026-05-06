---
aid: blue-yonder
url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/apis.yml
apis:
  - aid: blue-yonder:blue-yonder-demand-planning-api
    name: Blue Yonder Demand Planning API
    tags:
      - Demand Planning
      - Forecasting
      - REST
      - Retail
      - Supply Chain
    image: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/image.png
    humanURL: https://blueyonder.com/
    baseURL: https://api.blueyonder.example.com
    properties:
      - url: https://blueyonder.com/solutions/blue-yonder-platform
        type: Documentation
    description: The Blue Yonder Demand Planning API enables access to demand forecasting models, statistical baselines, and demand signals for retail and manufacturing supply chains. REST APIs support integration with ERP and POS systems for demand sensing, shaping, and response workflows.
  - aid: blue-yonder:blue-yonder-warehouse-management-api
    name: Blue Yonder Warehouse Management API
    tags:
      - Logistics
      - REST
      - Supply Chain
      - Warehouse Management
      - WMS
    image: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/image.png
    humanURL: https://blueyonder.com/
    baseURL: https://api.blueyonder.example.com
    properties:
      - url: https://blueyonder.com/solutions/blue-yonder-platform
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/openapi/blue-yonder-warehouse-management-openapi.yml
        type: OpenAPI
    description: The Blue Yonder Warehouse Management API provides access to warehouse operations data including inventory positions, task management, labor optimization, and fulfillment workflows. REST APIs support integration with automation systems, robotics, and ERP platforms for distribution center operations.
  - aid: blue-yonder:blue-yonder-transportation-management-api
    name: Blue Yonder Transportation Management API
    tags:
      - Logistics
      - REST
      - Supply Chain
      - TMS
      - Transportation Management
    image: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/image.png
    humanURL: https://blueyonder.com/
    baseURL: https://api.blueyonder.example.com
    properties:
      - url: https://blueyonder.com/solutions/blue-yonder-platform
        type: Documentation
    description: The Blue Yonder Transportation Management API enables access to transportation planning, carrier management, load optimization, and freight audit capabilities. REST APIs support carrier connectivity, shipment tracking, and transportation cost optimization across multimodal freight networks.
  - aid: blue-yonder:blue-yonder-connect-api
    name: Blue Yonder Connect API & Expansion Pack
    tags:
      - API Management
      - EDI
      - Integration
      - MuleSoft
      - REST
      - Supply Chain
    image: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/image.png
    humanURL: https://info.blueyonder.com/blue-yonder-platform/what-is-blue-yonder-connect-api-expansion-pack
    baseURL: https://api.blueyonder.example.com
    properties:
      - url: https://info.blueyonder.com/blue-yonder-platform/what-is-blue-yonder-connect-api-expansion-pack
        type: Documentation
    description: Blue Yonder Connect - API & Expansion Pack provides an advanced integration suite with pre-built MuleSoft connectors, enhanced API management tools, and higher throughput capacity. Supports REST, SOAP, EDI, and OData protocols for connecting Blue Yonder supply chain platform with SAP, Oracle, Salesforce, and custom applications.
common:
  - url: https://blueyonder.com
    type: Website
  - url: https://blueyonder.com/solutions/blue-yonder-platform
    type: Portal
  - url: https://blueyonder.com/solutions/blue-yonder-platform
    type: Documentation
  - url: https://info.blueyonder.com/blue-yonder-platform/what-is-blue-yonder-connect-api-expansion-pack
    type: GettingStarted
  - url: https://blog.blueyonder.com/
    type: Blog
  - url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/openapi/blue-yonder-warehouse-management-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/json-schema/blue-yonder-inventory-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/blue-yonder/refs/heads/main/json-ld/blue-yonder-context.jsonld
    type: JSONLDContext
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-21'
description: Transforming supply chains through an end-to-end platform for planning, execution, commerce and returns.
---
