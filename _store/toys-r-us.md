---
aid: toys-r-us
name: Toys R Us
description: Toys 'R' Us is a leading toys and juvenile-products retailer offering a vast selection of toys, games, baby products, and children's apparel through retail stores and e-commerce sites. The brand integrates with suppliers and dropship vendors via the LogicBroker commerce platform, providing APIs for order management, shipment processing, product catalog synchronization, and invoice workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commerce
  - Dropship
  - E-Commerce
  - Retail
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/toys-r-us/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: toys-r-us:logicbroker-commerce
    name: Toys R Us Commerce API
    description: The Toys R Us Commerce API, powered by LogicBroker, enables supplier and dropship vendor integrations for the complete order lifecycle. Supports purchase order retrieval (EDI 850), order acknowledgement (EDI 855), shipment notification (EDI 856), invoice processing (EDI 810), and product catalog synchronization. Vendors authenticate using an API subscription key.
    humanURL: https://toysrus.logicbroker.com/hc/en-us/articles/9357008230164-API-Documentation
    baseURL: https://commerceapi.io
    tags:
      - Commerce
      - Dropship
      - E-Commerce
      - Invoices
      - Order Management
      - Retail
      - Shipments
      - Supplier Integration
    properties:
      - type: Documentation
        url: https://toysrus.logicbroker.com/hc/en-us/articles/9357008230164-API-Documentation
      - type: OpenAPI
        url: openapi/toys-r-us-commerce-openapi.yml
      - type: JSONSchema
        url: json-schema/toys-r-us-order-schema.json
      - type: JSONStructure
        url: json-structure/toys-r-us-order-structure.json
      - type: JSONLd
        url: json-ld/toys-r-us-context.jsonld
      - type: SpectralRules
        url: rules/toys-r-us-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/dropship-fulfillment.yaml
      - type: Vocabulary
        url: vocabulary/toys-r-us-vocabulary.yml
      - type: Swagger
        url: https://commerceapi.io/swagger/ui/index
      - type: SwaggerStage
        url: https://stage.commerceapi.io/swagger/ui/index
common:
  - type: Website
    url: https://www.toysrus.com
  - type: SupplierPortal
    url: https://toysrus.logicbroker.com
  - type: Documentation
    url: https://toysrus.logicbroker.com/hc/en-us/articles/9357008230164-API-Documentation
  - type: DeveloperPortal
    url: https://dev.logicbroker.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
