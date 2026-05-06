---
aid: workday-financials
name: Workday Financials
description: Workday Financials is a cloud-based financial management system that provides comprehensive solutions for accounting, procurement, expenses, and financial reporting.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Accounting
  - Cloud ERP
  - Financial Management
  - Procurement
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/workday-financials/refs/heads/main/apis.yml
apis:
  - name: Workday Financial Management API
    description: Core API for managing financial transactions, general ledger, accounts payable, accounts receivable, and financial reporting.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/overview.html
    baseURL: https://api.workday.com/financialManagement
    tags:
      - Accounts Payable
      - Accounts Receivable
      - Financial Reporting
      - General Ledger
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Financial_Management.json
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wwsaas/authentication-and-authorization.html
      - type: OpenAPI
        url: openapi/workday-financials-financial-management-openapi.yml
  - name: Workday Revenue Management API
    description: API for managing revenue recognition, contracts, billing, and revenue accounting in compliance with ASC 606 and IFRS 15.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/revenue-management.html
    baseURL: https://api.workday.com/revenueManagement
    tags:
      - Billing
      - Contracts
      - Revenue Recognition
      - Subscription Management
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Revenue_Management/v38.2/Revenue_Management.json
      - type: OpenAPI
        url: openapi/workday-financials-revenue-management-openapi.yml
  - name: Workday Expenses API
    description: API for expense report submission, approval workflows, receipt management, and expense policy enforcement.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/expense-management.html
    baseURL: https://api.workday.com/expenses
    tags:
      - Approvals
      - Expense Reports
      - Receipt Management
      - Travel Expenses
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Expenses/v38.2/Expenses.json
      - type: OpenAPI
        url: openapi/workday-financials-expenses-openapi.yml
  - name: Workday Procurement API
    description: API for purchase requisitions, purchase orders, supplier management, and procurement processes.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/procurement.html
    baseURL: https://api.workday.com/procurement
    tags:
      - Procurement
      - Purchase Orders
      - Requisitions
      - Suppliers
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Resource_Management/v38.2/Resource_Management.json
      - type: OpenAPI
        url: openapi/workday-financials-procurement-openapi.yml
  - name: Workday Cash Management API
    description: API for managing cash positions, bank accounts, transactions, and cash forecasting.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/cash-management.html
    baseURL: https://api.workday.com/cashManagement
    tags:
      - Bank Accounts
      - Cash Management
      - Forecasting
      - Treasury
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Cash_Management/v38.2/Cash_Management.json
      - type: OpenAPI
        url: openapi/workday-financials-cash-management-openapi.yml
  - name: Workday Financial Accounting API
    description: API for journal entries, account reconciliation, period close activities, and audit trails.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/financial-accounting.html
    baseURL: https://api.workday.com/financialAccounting
    tags:
      - Account Reconciliation
      - Audit
      - Journal Entries
      - Period Close
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Financial_Management/v38.2/Financial_Management.json
      - type: OpenAPI
        url: openapi/workday-financials-financial-accounting-openapi.yml
  - name: Workday Reporting API
    description: API for accessing financial reports, custom report execution, and analytics data extraction.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/financial-reporting.html
    baseURL: https://api.workday.com/reporting
    tags:
      - Analytics
      - Custom Reports
      - Financial Reports
      - Reporting
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Report_as_a_Service/v38.2/Report_as_a_Service.json
      - type: OpenAPI
        url: openapi/workday-financials-reporting-openapi.yml
common:
  - type: Developer Portal
    url: https://community.workday.com/developer
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wwsaas/authentication-and-authorization.html
  - type: Rate Limits
    url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wwsaas/rate-limiting.html
  - type: Status Page
    url: https://status.workday.com/
  - type: Support
    url: https://www.workday.com/en-us/company/latest/support.html
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Contact
    url: https://www.workday.com/en-us/company/latest/contact-us.html
  - type: JSON-LD
    url: json-ld/workday-financials-context.jsonld
  - type: JSONSchema
    url: json-schema/workday-financials-journal-entry-schema.json
  - type: JSONSchema
    url: json-schema/workday-financials-supplier-invoice-schema.json
  - type: Spectral Rules
    url: rules/workday-financials-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/financial-close.yaml
  - type: Naftiko Capabilities
    url: capabilities/procure-to-pay.yaml
  - type: Vocabulary
    url: vocabulary/workday-financials-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
