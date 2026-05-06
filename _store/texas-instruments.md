---
aid: texas-instruments
name: Texas Instruments
description: Texas Instruments is an American technology company that designs and manufactures semiconductors and various integrated circuits for industrial, automotive, personal electronics, communications equipment, and enterprise systems markets. TI provides a developer API portal at api-portal.ti.com offering Store APIs for inventory, ordering, and shipment tracking, as well as Product Information APIs for accessing parametric data, quality, and reliability information on TI's extensive semiconductor catalog.
url: https://raw.githubusercontent.com/api-evangelist/texas-instruments/refs/heads/main/apis.yml
modified: '2026-05-03'
created: '2026-03-21'
type: Index
specificationVersion: '0.19'
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Electronics
  - Ordering
  - Semiconductors
  - Supply Chain
apis:
  - aid: texas-instruments:ti-store-api
    name: Texas Instruments Store API
    description: 'The TI Store API enables enterprise customers to integrate with TI''s ordering platform. It provides real-time inventory and pricing data, order creation and retrieval, advanced ship notice (ASN) tracking, and financial document retrieval. OAuth 2.0 client credentials authentication against transact.ti.com. Production base URL: https://transact.ti.com/v2/store'
    humanURL: https://www.ti.com/developer-api/store-api/getting-started.html
    baseURL: https://transact.ti.com/v2/store
    tags:
      - Inventory
      - Ordering
      - Semiconductors
      - Supply Chain
    properties:
      - type: Documentation
        url: https://www.ti.com/developer-api/store-api/getting-started.html
      - type: OpenAPI
        url: openapi/texas-instruments-store-openapi.yml
      - type: Portal
        url: https://api-portal.ti.com/
  - aid: texas-instruments:ti-product-information-api
    name: Texas Instruments Product Information API
    description: 'The TI Product Information API suite provides access to TI''s semiconductor product catalog including parametric data, quality and reliability information. Available as standard (multiple calls, 3,000/day limit) and orchestrated (single call, 1,500/day limit) variants. Base URL: https://transact.ti.com/v1'
    humanURL: https://www.ti.com/developer-api/product-information-api-suite/getting-started.html
    baseURL: https://transact.ti.com/v1
    tags:
      - Electronics
      - Product Data
      - Semiconductors
    properties:
      - type: Documentation
        url: https://www.ti.com/developer-api/product-information-api-suite/getting-started.html
      - type: OpenAPI
        url: openapi/texas-instruments-product-information-openapi.yml
      - type: Portal
        url: https://api-portal.ti.com/
common:
  - type: Website
    url: https://www.texas-instruments.com
  - type: Developer Portal
    url: https://api-portal.ti.com/
  - type: Documentation
    url: https://www.ti.com/developer-api/overview.html
  - type: Getting Started
    url: https://api-portal.ti.com/store-api-getstarted
  - type: Support
    url: https://api-portal.ti.com/support
  - type: FAQ
    url: https://api-portal.ti.com/faq
  - type: OpenAPI
    url: openapi/texas-instruments-store-openapi.yml
  - type: OpenAPI
    url: openapi/texas-instruments-product-information-openapi.yml
  - type: JSONSchema
    url: json-schema/ti-product-schema.json
  - type: JSON-LD
    url: json-ld/texas-instruments-context.jsonld
  - type: Vocabulary
    url: vocabulary/texas-instruments-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
