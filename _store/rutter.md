---
aid: rutter
name: Rutter
description: Rutter is the leading unified RESTful API for B2B financial products that connects to over 60 commerce, payments, accounting, and ads platforms through a single API. Trusted by companies like Airwallex, Mercury, and Ramp, Rutter enables developers to read, update, write, and remove data across major business platforms with a unified data model and idempotency guarantees for financial data. The API supports OAuth2 and Basic authentication, versioning via the X-Rutter-Version header, cursor-based pagination, and asynchronous request processing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting
  - B2B
  - Commerce
  - Financial Data
  - Payments
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rutter:unified-api
    name: Rutter Unified API
    description: The Rutter Unified API provides a single RESTful interface to over 60 commerce, payments, and accounting platforms. It supports connection management, accounting data (accounts, transactions, invoices, bills, expenses), commerce data (orders, products, customers), payments data, ads data, and banking data through a versioned API with cursor pagination and idempotent writes.
    humanURL: https://docs.rutter.com/
    baseURL: https://production.rutterapi.com/versioned
    tags:
      - Accounting
      - B2B
      - Commerce
      - Financial Data
      - Payments
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.rutter.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/openapi/rutter-unified-api-openapi.yml
  - aid: rutter:commerce-api
    name: Rutter Commerce API
    description: The Rutter Commerce API enables reading and writing data to all major commerce platforms through a unified API, supporting platforms like Shopify, WooCommerce, Amazon, and more.
    humanURL: https://www.rutter.com/product/commerce-api
    tags:
      - Commerce
      - E-Commerce
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.rutter.com/
      - type: ProductPage
        url: https://www.rutter.com/product/commerce-api
  - aid: rutter:accounting-api
    name: Rutter Accounting API
    description: The Rutter Accounting API provides a unified interface to read and write data to all major accounting platforms including QuickBooks, Xero, Freshbooks, and Zoho Books.
    humanURL: https://www.rutter.com/product/accounting-api
    tags:
      - Accounting
      - Financial Data
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.rutter.com/
      - type: ProductPage
        url: https://www.rutter.com/product/accounting-api
  - aid: rutter:payments-api
    name: Rutter Payments API
    description: The Rutter Payments API provides a unified interface to read and write data to all major payment platforms through a single REST API.
    humanURL: https://www.rutter.com/product/payments-api
    tags:
      - Financial Data
      - Payments
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.rutter.com/
      - type: ProductPage
        url: https://www.rutter.com/product/payments-api
common:
  - type: Website
    url: https://www.rutter.com/
  - type: Documentation
    url: https://docs.rutter.com/
  - type: Pricing
    url: https://www.rutter.com/pricing
  - type: Blog
    url: https://www.rutter.com/blog
  - type: Integrations
    url: https://www.rutter.com/integrations
  - type: APIs
    url: https://www.rutter.com/our-features/apis
  - type: SignUp
    url: https://dashboard.rutterapi.com/sign-up
  - type: GitHub
    url: https://github.com/rutter
  - type: SDK
    url: https://github.com/rutter/react-rutter-link
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/vocabulary/rutter-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-ld/rutter-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/rules/rutter-spectral-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/capabilities/financial-data-sync.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/capabilities/commerce-operations.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-connection-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-invoice-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rutter/refs/heads/main/json-schema/rutter-order-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
