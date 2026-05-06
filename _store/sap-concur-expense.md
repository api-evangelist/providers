---
name: SAP Concur Expense
description: SAP Concur Expense is a cloud-based travel and expense management solution that automates and streamlines expense reporting, approval workflows, and reimbursement processes for businesses. It integrates with corporate card programs, receipt capture, and ERP systems to provide end-to-end expense lifecycle management with audit controls and policy enforcement.
image: https://www.concur.com/themes/custom/concur/logo.svg
url: https://developer.concur.com/
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Expense Management
  - Financial Management
  - Receipts
  - Reimbursement
  - Reporting
  - SAP
  - Travel
apis:
  - name: Expense Report v3 API
    description: Allows developers to read and write expense report headers, manage the expense report lifecycle including submission and approval workflows, and retrieve expense report data for integration with ERP and financial systems.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Approval
      - Expenses
      - Financial
      - Reports
      - Workflow
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/v3.reports.html
      - type: Authentication
        url: https://developer.concur.com/api-reference/authentication/getting-started.html
      - type: OpenAPI
        url: openapi/sap-concur-expense-report-openapi.yml
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Expense Entry v3 API
    description: Manage individual expense entries within expense reports including itemizations, attendees, custom fields, and form field values. Supports creating, reading, updating, and deleting individual line items in expense reports.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-entry.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Expense Entries
      - Itemization
      - Line Items
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/expense-entry.html
      - type: OpenAPI
        url: openapi/sap-concur-expense-report-openapi.yml
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Quick Expense v3 API
    description: Create and manage basic expenses quickly outside of a formal expense report. Quick expenses can be added to an expense report later. Useful for capturing expenses on-the-go before being ready to file a complete report.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/quick-expense/v3.quick-expense.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Expenses
      - Mobile
      - Quick Expense
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/quick-expense/v3.quick-expense.html
      - type: OpenAPI
        url: openapi/sap-concur-expense-report-openapi.yml
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Receipt Image v3 API
    description: Upload, retrieve, and manage receipt images associated with expense entries. Supports attaching scanned receipts, e-receipts from travel providers, and credit card transaction images to expense line items for compliance and audit.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/image/v1.image.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Documents
      - Images
      - Receipts
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/image/v1.image.html
      - type: OpenAPI
        url: openapi/sap-concur-expense-report-openapi.yml
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Digital Tax Invoice API
    description: Retrieve digital tax invoice data associated with expense entries for compliance and auditing in jurisdictions that require electronic invoicing (e-invoicing). Provides access to CFDI (Mexico), NF-e (Brazil), and other country-specific digital tax documents.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/digital-tax-invoices/digital-tax-invoice.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Compliance
      - Invoice
      - Tax
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/digital-tax-invoices/digital-tax-invoice.html
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Expense Group Configuration API
    description: Retrieve expense group configurations including expense types, expense policies, payment types, and workflow settings. Used to dynamically configure expense capture UIs and enforce policy rules during expense report creation.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-group-configurations.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Configuration
      - Policies
      - Settings
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/expense-group-configurations.html
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Expense Allocations API
    description: Manage allocation of expenses across multiple cost centers, projects, departments, or GL accounts. Supports percentage-based and amount-based allocation splits for corporate expense policy compliance and financial reporting.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/expense-report/expense-allocations.html
    baseURL: https://us.api.concursolutions.com/api/v3.0
    version: '3.0'
    tags:
      - Accounting
      - Allocations
      - Cost Centers
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/expense-report/expense-allocations.html
    contact:
      - type: Support
        url: https://developer.concur.com/support
  - name: Payment Batch v1 API
    description: Retrieve and manage payment batches for processed expense reports ready for reimbursement. Provides visibility into batch payment status, amounts, and payee information for integration with payroll and ERP payment systems.
    image: https://www.concur.com/themes/custom/concur/logo.svg
    humanURL: https://developer.concur.com/api-reference/expense/payment-batch/v1.payment-batches.html
    baseURL: https://us.api.concursolutions.com/api/v1.1
    version: '1.1'
    tags:
      - Batch Processing
      - Payments
      - Reimbursement
    properties:
      - type: Documentation
        url: https://developer.concur.com/api-reference/expense/payment-batch/v1.payment-batches.html
    contact:
      - type: Support
        url: https://developer.concur.com/support
common:
  - type: Developer Portal
    url: https://developer.concur.com/
  - type: Getting Started
    url: https://developer.concur.com/api-reference/expense/
  - type: Authentication
    url: https://developer.concur.com/api-reference/authentication/getting-started.html
  - type: OAuth 2.0
    url: https://developer.concur.com/api-reference/authentication/apidoc.html
  - type: API Explorer
    url: https://developer.concur.com/api-explorer/
  - type: Support
    url: https://developer.concur.com/support
  - type: Terms of Service
    url: https://developer.concur.com/terms-of-use
  - type: Privacy Policy
    url: https://www.sap.com/about/legal/privacy.html
  - type: Status Page
    url: https://open.concur.com/
  - type: Release Notes
    url: https://developer.concur.com/tools-support/release-notes/
  - type: Community
    url: https://community.sap.com/topics/concur
  - type: Blog
    url: https://developer.concur.com/blog/
  - type: GitHub Organization
    url: https://github.com/concur
  - type: Website
    url: https://www.concur.com/
  - type: Sign Up
    url: https://www.concur.com/en-us/try-concur.html
  - type: SDKs
    url: https://github.com/concur/concur-platform-sdk-java
  - type: Postman Collection
    url: https://developer.concur.com/tools-support/postman.html
  - type: OpenAPI
    url: openapi/sap-concur-expense-report-openapi.yml
  - type: JSONSchema
    url: json-schema/sap-concur-expense-report-schema.json
  - type: JSONSchema
    url: json-schema/sap-concur-expense-entry-schema.json
  - type: JSONSchema
    url: json-schema/sap-concur-expense-receipt-schema.json
  - type: JSONStructure
    url: json-structure/sap-concur-expense-report-structure.json
  - type: JSONStructure
    url: json-structure/sap-concur-expense-entry-structure.json
  - type: JSON-LD
    url: json-ld/sap-concur-expense-context.jsonld
  - type: SpectralRules
    url: rules/sap-concur-expense-rules.yml
  - type: NaftikoCapability
    url: capabilities/expense-reporting-and-approval.yaml
  - type: NaftikoCapability
    url: capabilities/expense-capture-and-receipts.yaml
  - type: Vocabulary
    url: vocabulary/sap-concur-expense-vocabulary.yml
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
