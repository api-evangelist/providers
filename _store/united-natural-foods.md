---
aid: united-natural-foods
url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
name: United Natural Foods (UNFI)
description: United Natural Foods, Inc. (UNFI) is the largest publicly traded wholesale distributor of health and specialty food in the United States and Canada. UNFI supplies natural, organic, specialty, and conventional foods to over 30,000 retail locations. UNFI provides digital supplier and customer portals including myUNFI, supplier portal, EDI integration, and the Harmony Core API for data access.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Food Distribution
  - Wholesale
  - Natural Foods
  - Supply Chain
  - Fortune 500
apis:
  - name: UNFI Harmony Core API
    description: UNFI's Harmony Core API provides read-only access to 42 data files covering supplier, product, inventory, and sales data across UNFI's distribution network. Consumers can perform SQL-style queries including field selection and multi-table joins. Used by suppliers, retailers, and analytics platforms like Crisp to access UNFI Insights data.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://suppliers.unfi.com
    baseURL: https://api.unfi.com/v1
    tags:
      - Food Distribution
      - Supply Chain
      - Analytics
      - Wholesale
      - Data API
    properties:
      - type: Documentation
        url: https://suppliers.unfi.com
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/openapi/unfi-supplier-openapi.yml
  - name: UNFI EDI Integration
    description: UNFI supports Electronic Data Interchange (EDI) for automated exchanges of purchase orders, invoices, and fulfillment data between UNFI and its supplier and retail partners. EDI integration supports the procure-to-pay lifecycle for both suppliers and retailers.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://suppliers.unfi.com
    baseURL: https://api.unfi.com/v1
    tags:
      - EDI
      - Supply Chain
      - Procurement
      - Invoicing
    properties:
      - type: Documentation
        url: https://suppliers.unfi.com
common:
  - type: Website
    url: https://www.unfi.com
  - type: Supplier Portal
    url: https://suppliers.unfi.com
  - type: Customer Portal
    url: https://www.myunfi.com
  - type: LinkedIn
    url: https://www.linkedin.com/company/unfi
  - type: X
    url: https://twitter.com/UNFIInc
  - type: Investor Relations
    url: https://ir.unfi.com
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/openapi/unfi-supplier-openapi.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/rules/unfi-supplier-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/capabilities/supplier-management.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-schema/unfi-supplier-product-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-schema/unfi-supplier-order-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/json-ld/united-natural-foods-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/united-natural-foods/main/vocabulary/united-natural-foods-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
