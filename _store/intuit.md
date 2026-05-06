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
        type: APIReference
      - url: https://developer.intuit.com/app/developer/qbo/docs/get-started
        type: GettingStarted
      - url: https://developer.intuit.com/app/developer/qbo/docs/get-started/get-started-with-the-api-explorer
        type: Console
      - url: https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
        type: Authentication
      - url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api
        type: Documentation
      - url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
        type: Versioning
      - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples
        type: SDK
      - url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/platform-release-notes
        type: ReleaseNotes
      - url: openapi/quickbooks-accounting.yml
        type: OpenAPI
      - url: asyncapi/quickbooks-webhooks.yml
        type: AsyncAPI
      - url: json-schema/intuit-invoice-schema.json
        type: JSONSchema
      - url: json-schema/intuit-customer-schema.json
        type: JSONSchema
      - url: json-ld/intuit-context.jsonld
        type: JSONLD
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
        type: GettingStarted
      - url: https://developer.intuit.com/app/developer/qbpayments/docs/develop
        type: APIReference
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
        type: GettingStarted
      - url: https://developer.intuit.com/app/developer/payroll-time/docs/develop/develop-payroll
        type: Documentation
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
        type: APIReference
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
        type: APIReference
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
        type: APIReference
      - url: https://developer.intuit.com/app/developer/qbo/docs/develop
        type: Documentation
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
        type: APIReference
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
modified: '2026-04-18'
position: Consumer
description: Collection of APIs offered by Intuit for financial and business management services.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
  - name: Intuit Developer
    email: developer-support@intuit.com
    url: https://help.developer.intuit.com
specificationVersion: '0.19'
common:
  - url: https://developer.intuit.com
    type: DeveloperPortal
  - url: https://developer.intuit.com/app/developer/appcard/overview
    type: SignUp
  - url: https://developer.intuit.com/app/developer/blog
    type: Blog
  - url: https://help.developer.intuit.com
    type: Support
  - url: https://status.developer.intuit.com
    type: StatusPage
  - url: https://developer.intuit.com/app/developer/qbo/docs/learn/terms-of-service
    type: TermsOfService
  - url: https://www.intuit.com/privacy/
    type: PrivacyPolicy
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/authentication-and-authorization/oauth-2.0
    type: Authentication
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sandboxes/postman
    type: Sandbox
  - url: https://developer.intuit.com/app/developer/qbo/docs/get-started/get-started-with-the-api-explorer
    type: Console
  - url: https://developer.intuit.com/app/developer/qbo/docs/get-started/partner-faq
    type: FAQ
  - url: https://github.com/intuit
    type: GitHubOrganization
  - url: https://github.com/intuitdeveloper
    type: GitHubOrganization
  - url: https://github.com/intuit/QuickBooks-V3-PHP-SDK
    type: SDK
    title: PHP SDK
  - url: https://github.com/intuit/QuickBooks-V3-DotNET-SDK
    type: SDK
    title: .NET SDK
  - url: https://github.com/intuit/QuickBooks-V3-Java-SDK
    type: SDK
    title: Java SDK
  - url: https://github.com/intuit/oauth-rubyclient
    type: SDK
    title: Ruby SDK
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/nodejs
    type: SDK
    title: Node.js SDK
  - url: https://developer.intuit.com/app/developer/qbo/docs/develop/sdks-and-samples-collections/python
    type: SDK
    title: Python SDK
  - url: https://blogs.intuit.com/
    type: ChangeLog
  - url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/platform-release-notes
    type: ReleaseNotes
  - url: https://developer.intuit.com/app/developer/qbo/docs/release-notes/general-release-notes
    type: ReleaseNotes
  - url: https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api/minor-versions
    type: Versioning
  - url: https://help.developer.intuit.com/s/article/API-call-limits-and-throttling
    type: RateLimits
  - url: https://developer.intuit.com/app/developer/qbo/docs/go-live/publish-app/security-requirements
    type: Security
  - url: https://quickbooks.intuit.com/app/apps/home/en-global/
    type: Marketplace
  - url: https://x.com/IntuitDev
    type: X
  - url: https://www.linkedin.com/company/intuit-developer
    type: LinkedIn
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Secure API access using OAuth 2.0 authorization with OpenID Connect for user identity verification.
      - name: Webhooks
        description: Real-time event notifications for changes to QuickBooks entities including invoices, payments, and customers.
      - name: Minor Versioning
        description: Backward-compatible API versioning allowing access to newer fields and behaviors without breaking existing integrations.
      - name: Sandbox Environment
        description: Full-featured sandbox environment for testing and development with sample company data.
      - name: Multi-Currency Support
        description: Support for transactions in multiple currencies with automatic exchange rate management.
      - name: Custom Fields
        description: Extensible metadata system allowing up to 12 custom fields across transaction types.
  - type: UseCases
    data:
      - name: Accounting Automation
        description: Automate bookkeeping workflows by syncing invoices, payments, and expenses between business systems and QuickBooks.
      - name: Payment Processing
        description: Process credit card and ACH payments linked to QuickBooks invoices for seamless financial reconciliation.
      - name: Payroll Integration
        description: Integrate payroll and time-tracking data to streamline employee compensation and workforce management.
      - name: Tax Compliance
        description: Automate sales tax calculations and ensure tax compliance across different jurisdictions.
      - name: Financial Reporting
        description: Build custom financial reports and dashboards by querying QuickBooks accounting data programmatically.
  - type: Integrations
    data:
      - name: Shopify
        description: Sync e-commerce orders, inventory, and payments between Shopify stores and QuickBooks for automated bookkeeping.
      - name: Stripe
        description: Reconcile Stripe payment transactions with QuickBooks invoices and accounts receivable.
      - name: Square
        description: Import Square POS transactions into QuickBooks for unified financial management.
      - name: HubSpot
        description: Connect CRM data with accounting to automate invoice creation from deals and track payment status.
      - name: Salesforce
        description: Sync customer and opportunity data between Salesforce CRM and QuickBooks accounting.
---
