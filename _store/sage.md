---
aid: sage
name: Sage
description: Sage provides cloud-based ERP, accounting, payroll, and HR software for businesses worldwide. The Sage Developer program provides APIs for integrating with Sage products including Sage Accounting (Business Cloud), Sage Intacct, Sage 200, Sage X3, and Sage 50. APIs support OAuth 2.0 authentication and cover contacts, invoices, payments, ledger accounts, bank accounts, products, and financial reporting. Sage Accounting API v3.1 is the current supported REST version with daily limits of 1,296,000 requests per app.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting
  - Business Management
  - Cloud Software
  - ERP
  - Payroll
  - HR
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sage/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sage:accounting
    name: Sage Accounting API
    description: Sage Accounting API (v3.1) is a RESTful web service that connects software to Sage's cloud accounting platform. Supports contacts, sales invoices, purchase invoices, payments, bank accounts, ledger accounts, products/services, and financial reports. Uses OAuth 2.0 for authentication. Covers Sage Business Cloud Accounting and Sage Business Cloud Start products.
    humanURL: https://developer.sage.com/accounting
    tags:
      - Accounting
      - ERP
      - REST
      - OAuth 2.0
    properties:
      - type: Documentation
        url: https://developer.sage.com/accounting/reference
      - type: GettingStarted
        url: https://developer.sage.com/accounting/guides/concepts/overview
      - type: OpenAPI
        url: openapi/sage-accounting-openapi.yml
  - aid: sage:intacct
    name: Sage Intacct API
    description: Sage Intacct provides both REST and XML APIs for advanced financial management including multi-entity consolidations, project accounting, revenue recognition, and advanced reporting. The REST API uses OAuth 2.0 for authorization. Targeted at mid-market and enterprise finance teams.
    humanURL: https://developer.sage.com/intacct/
    tags:
      - Accounting
      - ERP
      - REST
      - XML
      - OAuth 2.0
    properties:
      - type: Documentation
        url: https://developer.intacct.com/api/
      - type: Authentication
        url: https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/authorization-and-security/oauth2
  - aid: sage:sage-x3
    name: Sage X3 API
    description: Sage X3 provides a GraphQL API offering flexible data access for ERP operations including manufacturing, distribution, procurement, finance, and CRM. Supports SOAP API for legacy integrations. Targeted at enterprise and manufacturing organizations.
    humanURL: https://developer.sage.com/x3/
    tags:
      - ERP
      - GraphQL
      - Manufacturing
      - Distribution
    properties:
      - type: Documentation
        url: https://developer.sage.com/x3/
  - aid: sage:sage-200
    name: Sage 200 API
    description: Sage 200 API provides REST access to Sage 200 Standard and Professional business management data including customers, suppliers, stock, sales orders, purchase orders, nominal ledger, bank reconciliation, and financial reporting for UK and Ireland mid-size businesses.
    humanURL: https://developer.sage.com/sage-200/
    tags:
      - Accounting
      - ERP
      - REST
    properties:
      - type: Documentation
        url: https://developer.sage.com/sage-200/
  - aid: sage:sage-50
    name: Sage 50 Accounts API
    description: Sage 50 Accounts API enables desktop accounting integration for UK small businesses. Provides access to accounts, transactions, customers, suppliers, products, and financial data within Sage 50 Accounts software.
    humanURL: https://developer.sage.com/sage-50-accounts/
    tags:
      - Accounting
      - Desktop
      - REST
    properties:
      - type: Documentation
        url: https://developer.sage.com/sage-50-accounts/
common:
  - type: Portal
    url: https://developer.sage.com/
  - type: Documentation
    url: https://developer.sage.com/
  - type: Authentication
    url: https://developer.sage.com/accounting/guides/concepts/authentication
  - type: Sandbox
    url: https://developer.sage.com/accounting/guides/test-drive/
  - type: Website
    url: https://www.sage.com/
  - type: Support
    url: https://developer.sage.com/support/
  - type: Blog
    url: https://www.sage.com/en-us/blog/
  - type: GitHubOrganization
    url: https://github.com/Sage
  - type: OpenAPI
    url: openapi/sage-accounting-openapi.yml
  - type: SpectralRules
    url: rules/sage-rules.yml
  - type: JSONSchema
    url: json-schema/sage-contact-schema.json
  - type: JSONSchema
    url: json-schema/sage-invoice-schema.json
  - type: JSONStructure
    url: json-structure/sage-contact-structure.json
  - type: JSONStructure
    url: json-structure/sage-invoice-structure.json
  - type: JSONLDContext
    url: json-ld/sage-context.jsonld
  - type: Vocabulary
    url: vocabulary/sage-vocabulary.yml
  - type: Capabilities
    url: capabilities/accounting-and-finance.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
