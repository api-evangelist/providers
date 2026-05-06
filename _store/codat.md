---
aid: codat
name: Codat
segments:
  - Unified_API
description: Codat is a unified API platform focused on SMB financial data, connecting to 30+ accounting, ERP, banking, and payment platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Unified_API
created: '2026-03-03'
modified: '2026-04-01'
url: https://raw.githubusercontent.com/api-evangelist/codat/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: codat:platform-api
    name: Codat Platform API
    description: The Codat Platform API provides core functionality used across all Codat solutions, including programmatic creation and management of companies, data connections, and configuration of integrations with accounting, banking, and commerce platforms.
    humanURL: https://docs.codat.io/using-the-api/overview
    tags:
      - Companies
      - Connections
      - Platform
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/using-the-api/overview
      - type: API Reference
        url: https://docs.codat.io/platform-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
      - type: OpenAPI
        url: openapi/codat-platform-openapi.json
  - aid: codat:lending-api
    name: Codat Lending API
    description: The Codat Lending API enables digital lenders, neobanks, and corporate card providers to make smarter credit decisions on small businesses by aggregating and analyzing standardized financial data from accounting, banking, and commerce platforms to assess SMB creditworthiness.
    humanURL: https://docs.codat.io/lending/overview
    tags:
      - Credit
      - Financial Data
      - Lending
      - Underwriting
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/lending/overview
      - type: API Reference
        url: https://docs.codat.io/lending-api
      - type: OpenAPI
        url: openapi/codat-lending-openapi.json
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:bank-feeds-api
    name: Codat Bank Feeds API
    description: The Codat Bank Feeds API enables banks, neobanks, corporate card issuers, and payment providers to set up automatic bank feeds from their applications to supported accounting software, simplifying the deployment of bank statement synchronization into SMB accounting platforms through a single standardized integration.
    humanURL: https://docs.codat.io/bank-feeds/overview
    tags:
      - Accounting
      - Bank Feeds
      - Reconciliation
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/bank-feeds/overview
      - type: OpenAPI
        url: openapi/codat-bank-feeds-openapi.json
      - type: API Reference
        url: https://docs.codat.io/bank-feeds-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:sync-for-expenses-api
    name: Codat Sync for Expenses API
    description: The Codat Sync for Expenses API enables corporate card and expense management platforms to provide high-quality integrations with multiple accounting platforms, synchronizing categorized expense data including receipts, general ledger mappings, and tracking categories into SMB accounting software through a standardized data model.
    humanURL: https://docs.codat.io/expenses/overview
    tags:
      - Accounting Sync
      - Corporate Cards
      - Expenses
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/expenses/overview
      - type: API Reference
        url: https://docs.codat.io/sync-for-expenses-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:sync-for-payables-api
    name: Codat Bill Pay API
    description: The Codat Bill Pay API (Sync for Payables) enables neobanks, expense management providers, and B2B payment platforms to automate customers' accounts payable workflows, providing a standardized data model to sync bills and bill payments with all major accounting software in real time.
    humanURL: https://docs.codat.io/payables/overview
    tags:
      - Accounts Payable
      - Bill Pay
      - Payables
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/payables/overview
      - type: API Reference
        url: https://docs.codat.io/sync-for-payables-v2-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:spend-insights-api
    name: Codat Spend Insights API
    description: The Codat Spend Insights API enables banks and commercial card issuers to access clients' accounts payable data from their ERP or accounting software within minutes, providing insights on spend and supplier activity to identify suppliers eligible for virtual card programs and grow commercial card volume in B2B payments.
    humanURL: https://docs.codat.io/spend-insights/overview
    tags:
      - Accounts Payable
      - Spend Insights
      - Unified_API
      - Virtual Cards
    properties:
      - type: Documentation
        url: https://docs.codat.io/spend-insights/overview
      - type: API Reference
        url: https://docs.codat.io/spend-insights-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:sync-for-commerce-api
    name: Codat Sync for Commerce API
    description: The Codat Sync for Commerce API automatically replicates and reconciles sales data from merchant point-of-sale, payments, and eCommerce systems into their accounting software, transforming raw sales and payments data into detailed sales invoices for automated accounting reconciliation.
    humanURL: https://docs.codat.io/commerce/overview
    tags:
      - Commerce
      - Point of Sale
      - Reconciliation
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/commerce/overview
      - type: API Reference
        url: https://docs.codat.io/sync-for-commerce-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
  - aid: codat:sync-for-payroll-api
    name: Codat Sync for Payroll API
    description: The Codat Sync for Payroll API enables HR, payroll, and vertical SaaS platforms to integrate their customers' payroll data into accounting software and support its reconciliation, providing a standardized data model to create and manage accounts, journal entries, and tracking categories across all supported accounting and ERP packages.
    humanURL: https://docs.codat.io/payroll/overview
    tags:
      - Accounting Sync
      - HR
      - Payroll
      - Unified_API
    properties:
      - type: Documentation
        url: https://docs.codat.io/payroll/overview
      - type: API Reference
        url: https://docs.codat.io/sync-for-payroll-api
      - type: OpenAPI Source
        url: https://github.com/codatio/oas
common:
  - type: Portal
    url: https://app.codat.io/
  - type: Documentation
    url: https://docs.codat.io/
  - type: Getting Started
    url: https://docs.codat.io/get-started/first-steps
  - type: SDKs
    url: https://docs.codat.io/get-started/libraries
  - type: OpenAPI Source
    url: https://github.com/codatio/oas
  - type: GitHub Organization
    url: https://github.com/codatio
  - type: Blog
    url: https://codat.io/blog/
  - type: Change Log
    url: https://docs.codat.io/updates
  - type: Status
    url: https://status.codat.io
  - type: Sign Up
    url: https://codat.io/start-building/
  - type: About
    url: https://codat.io/about/
  - type: Legal
    url: https://legal.codat.io/
  - type: TypeScript SDK
    url: https://github.com/codatio/client-sdk-typescript
  - type: Python SDK
    url: https://github.com/codatio/client-sdk-python
  - type: C# SDK
    url: https://github.com/codatio/client-sdk-csharp
  - type: Go SDK
    url: https://github.com/codatio/client-sdk-go
  - type: Java SDK
    url: https://github.com/codatio/client-sdk-java
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
