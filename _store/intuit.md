---
aid: intuit
url: https://raw.githubusercontent.com/api-evangelist/intuit/refs/heads/main/apis.yml
apis:
- aid: intuit:intuit
  name: Intuit APIs
  tags:
  - Accounting
  - Financial
  - Tax Preparation
  - Taxes
  humanURL: https://developer.intuit.com/app/developer/homepage
  properties:
  - url: https://developer.intuit.com/app/developer/homepage
    type: Documentation
  description: Intuit APIs provide developers with access to a wide range of services and functionalities to help them build innovative solutions for financial management, accounting, and tax-related needs. These APIs allow developers to integrate with popular Intuit products such as QuickBooks, TurboTax, and Mint, giving users the ability to securely access and manage their financial data across multiple platforms.
- aid: intuit:quickbooks-accounting
  name: QuickBooks Online Accounting API
  tags:
  - Accounting
  - Bookkeeping
  - Financial
  - Invoicing
  - Small Business
  humanURL: https://developer.intuit.com/app/developer/qbo/docs/develop
  properties:
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop
    type: Documentation
  - url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
    type: API Reference
  - url: https://developer.intuit.com/app/developer/qbo/docs/get-started
    type: Getting Started
  - url: https://developer.intuit.com/app/developer/qbo/docs/get-started/get-started-with-the-api-explorer
    type: API Explorer
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/webhooks
    type: Webhooks
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/postman
    type: Postman Collection
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
    type: Authentication
  - url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api
    type: Overview
  - url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
    type: Versioning
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples
    type: SDKs
  - url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/platform-release-notes
    type: Release Notes
  - url: openapi/quickbooks-accounting.yml
    type: OpenAPI
  - url: asyncapi/quickbooks-webhooks.yml
    type: AsyncAPI
  - url: json-schema/intuit-invoice-schema.json
    type: JSONSchema
  - url: json-schema/intuit-customer-schema.json
    type: JSONSchema
  - url: json-ld/intuit-context.jsonld
    type: JSON-LD Context
  description: The QuickBooks Online Accounting API is a RESTful API that provides programmatic access to QuickBooks Online company data, including customers, invoices, payments, bills, vendors, accounts, and reports. It enables developers to build integrations that automate accounting workflows, synchronize financial data, and extend QuickBooks Online functionality for small and mid-sized businesses.
- aid: intuit:quickbooks-payments
  name: QuickBooks Payments API
  tags:
  - Credit Cards
  - eCommerce
  - Financial
  - Payments
  humanURL: https://developer.intuit.com/app/developer/qbpayments/docs/learn/explore-the-quickbooks-payments-api
  properties:
  - url: https://developer.intuit.com/app/developer/qbpayments/docs/learn/explore-the-quickbooks-payments-api
    type: Documentation
  - url: https://developer.intuit.com/app/developer/qbpayments/docs/get-started
    type: Getting Started
  - url: https://developer.intuit.com/app/developer/qbo/docs/workflows/use-the-quickbooks-online-and-the-quickbooks-payments-apis-together
    type: Integration Guide
  - url: https://developer.intuit.com/app/developer/qbpayments/docs/develop
    type: API Reference
  description: The QuickBooks Payments API enables developers to process credit card charges, bank account debits (ACH), and manage payment methods within the QuickBooks ecosystem. It supports tokenized card storage, refunds, and the ability to link payments directly to QuickBooks Online invoices for seamless reconciliation.
- aid: intuit:quickbooks-payroll-time
  name: QuickBooks Payroll and Time API
  tags:
  - HR
  - Payroll
  - Small Business
  - Time Tracking
  humanURL: https://developer.intuit.com/app/developer/payroll-time/docs/get-started
  properties:
  - url: https://developer.intuit.com/app/developer/payroll-time/docs/get-started
    type: Getting Started
  - url: https://developer.intuit.com/app/developer/payroll-time/docs/develop/develop-payroll
    type: Documentation
  - url: https://developer.intuit.com/app/developer/qbo/docs/workflows/integrate-with-payroll-api
    type: Integration Guide
  description: The QuickBooks Payroll and Time API provides programmatic access to payroll and time-tracking data within QuickBooks Online. It supports use cases including time entry management, payroll compensation, and deductions, enabling developers to build integrations that streamline workforce and payroll operations for small businesses.
- aid: intuit:quickbooks-desktop
  name: QuickBooks Desktop API
  tags:
  - Accounting
  - Desktop
  - Financial
  - Small Business
  humanURL: https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbdesktop
  properties:
  - url: https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference/qbdesktop
    type: API Reference
  - url: https://developer.intuit.com/app/developer/qbdesktop/docs/api-reference
    type: Documentation
  description: The QuickBooks Desktop API allows developers to integrate with QuickBooks Desktop applications using qbXML messages. It provides capabilities for adding, querying, modifying, and deleting data across list objects, transaction objects, query objects, and report objects, enabling third-party applications to interact with on-premise QuickBooks installations.
- aid: intuit:quickbooks-projects
  name: QuickBooks Projects API
  tags:
  - Accounting
  - Financial
  - Project Management
  - Projects
  - Small Business
  humanURL: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
  properties:
  - url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
    type: API Reference
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop
    type: Documentation
  description: The QuickBooks Projects API is a premium API that provides programmatic access to project data within QuickBooks Online Plus, Advanced, Accountant, and Intuit Enterprise Suite. It enables developers to create projects, track profitability, and manage project-level financial data, allowing integrations that enhance project-based accounting and reporting workflows.
- aid: intuit:quickbooks-custom-fields
  name: QuickBooks Custom Fields API
  tags:
  - Accounting
  - Custom Fields
  - Financial
  - Metadata
  - Small Business
  humanURL: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
  properties:
  - url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/account
    type: API Reference
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop
    type: Documentation
  - url: https://blogs.intuit.com/2025/12/01/custom-fields-api-extending-quickbooks-online-with-flexible-metadata/
    type: Blog Post
  description: The QuickBooks Custom Fields API is a premium API that provides programmatic access to custom field definitions and values in QuickBooks Online and Intuit Enterprise Suite. It allows developers to create and manage up to 12 custom fields that can be used across different transaction types, enabling flexible metadata extensions for invoices, estimates, sales receipts, and other entities.
- aid: intuit:quickbooks-sales-tax
  name: QuickBooks Sales Tax API
  tags:
  - Accounting
  - Financial
  - Sales Tax
  - Small Business
  - Tax
  humanURL: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxrate
  properties:
  - url: https://developer.intuit.com/app/developer/qbo/docs/api/accounting/all-entities/taxrate
    type: API Reference
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop
    type: Documentation
  description: The QuickBooks Sales Tax API is a premium API that provides programmatic access to the automated sales tax calculation capabilities within QuickBooks Online. It enables developers to leverage QuickBooks automated sales tax engine to calculate the correct sales tax for invoices and other transactions, supporting tax compliance across different jurisdictions.
name: Intuit
tags:
- Accounting
- Custom Fields
- Financial
- Financial Services
- Invoicing
- Payments
- Payroll
- Project Management
- Sales Tax
- Small Business
- Tax
- Tax Preparation
- Taxes
- Time Tracking
type: Index
image: https://developer.intuit.com/app/developer/common/imgs/IntuitDev_Logo.svg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-07'
position: Consumer
description: Collection of APIs offered by Intuit for financial and business management services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

