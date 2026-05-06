---
name: ScanSource
description: ScanSource is an international technology distributor specializing in point-of-sale (POS), payments, barcode, physical security, unified communications, collaboration, telecom, and cloud services. Founded in 1992 in Greenville, South Carolina, ScanSource provides APIs that give partners real-time access to inventory, pricing, order management, and product information to automate the sales cycle and integrate with backend ERP systems and customer portals.
url: https://github.com/api-evangelist/scansource
x-type: company
bapiId: scansource
tags:
  - ScanSource
  - Distribution
  - Barcode
  - Point Of Sale
  - AIDC
  - Inventory
  - Order Management
  - E-Commerce
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: ScanSource Product API
    description: The ScanSource Product API provides real-time product information, pricing, and availability checks for technology distribution partners. Supports single and batch queries for up to 40 items per request, with integration targets including ERP systems, sales tools, and customer self-service portals.
    humanURL: https://services.scansource.com/api/Help
    baseURL: https://services.scansource.com/api
    tags:
      - Products
      - Pricing
      - Availability
      - Inventory
    properties:
      - type: Documentation
        url: https://services.scansource.com/api/Help
      - type: OpenAPI
        url: openapi/scansource-product-openapi.yml
      - type: JSONSchema
        url: json-schema/scansource-product-schema.json
    contact:
      - FN: ScanSource Partner Support
        email: B2BRequest@scansource.com
    x-auth:
      type: apiKey
      name: Ocp-Apim-Subscription-Key
      in: header
  - name: ScanSource Sales Order API
    description: The ScanSource Sales Order API enables partners to create, track, and manage purchase orders programmatically. Supports synchronous and asynchronous order creation, order status queries, shipping quotes, order cancellation, and serial number tracking.
    humanURL: https://services.scansource.com/api/Help
    baseURL: https://services.scansource.com/api
    tags:
      - Orders
      - Sales
      - Commerce
      - Fulfillment
    properties:
      - type: Documentation
        url: https://services.scansource.com/api/Help
      - type: OpenAPI
        url: openapi/scansource-sales-order-openapi.yml
      - type: JSONSchema
        url: json-schema/scansource-order-schema.json
    contact:
      - FN: ScanSource Partner Support
        email: B2BRequest@scansource.com
    x-auth:
      type: apiKey
      name: Ocp-Apim-Subscription-Key
      in: header
  - name: ScanSource Invoice API
    description: The ScanSource Invoice API provides access to invoicing data including invoice summaries, detailed invoice lists, individual invoice details, and PDF exports. Supports filtering by date range, sales order number, invoice number, and purchase order number.
    humanURL: https://services.scansource.com/api/Help
    baseURL: https://services.scansource.com/api
    tags:
      - Invoices
      - Billing
      - Finance
      - Accounting
    properties:
      - type: Documentation
        url: https://services.scansource.com/api/Help
      - type: OpenAPI
        url: openapi/scansource-invoice-openapi.yml
    contact:
      - FN: ScanSource Partner Support
        email: B2BRequest@scansource.com
    x-auth:
      type: apiKey
      name: Ocp-Apim-Subscription-Key
      in: header
common:
  - type: Website
    url: https://www.scansource.com
  - type: DeveloperPortal
    url: https://partnerportal.scansource.com
  - type: Documentation
    url: https://services.scansource.com/api/Help
  - type: GettingStarted
    url: https://partnerportal.scansource.com/getstarted
  - type: PartnerPortal
    url: https://partnerdevportal.scansource.com
  - type: SpectralRules
    url: rules/scansource-rules.yml
  - type: JSONStructure
    url: json-structure/scansource-product-structure.json
  - type: JSONLDContext
    url: json-ld/scansource-context.jsonld
  - type: Vocabulary
    url: vocabulary/scansource-vocabulary.yml
  - type: Capabilities
    url: capabilities/partner-commerce.yaml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
