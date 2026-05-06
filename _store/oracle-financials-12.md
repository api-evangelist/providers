---
aid: oracle-financials-12
name: Oracle Financials 12
description: Collection of REST APIs for Oracle E-Business Suite Financials Release 12.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-financials-12/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - name: Oracle General Ledger API
    description: API for managing general ledger operations including journals, budgets, and financial reporting.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13561/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounting
      - Financial Reporting
      - General Ledger
      - Journals
    properties:
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/openapi/gl-api.json
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13561/T302934T531415.htm
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/authentication.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Accounts Payable API
    description: API for managing supplier invoices, payments, and payables operations.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13533/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounts Payable
      - Invoices
      - Payments
      - Suppliers
    properties:
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/openapi/ap-api.json
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13533/T302934T531415.htm
      - type: API Guide
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e20280/toc.htm
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Accounts Receivable API
    description: API for managing customer invoices, receipts, and receivables operations.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13522/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounts Receivable
      - Collections
      - Customer Invoices
      - Receipts
    properties:
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/openapi/ar-api.json
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13522/T302934T531415.htm
      - type: API Guide
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e20281/toc.htm
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Cash Management API
    description: API for managing bank accounts, cash positions, and treasury operations.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13540/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Bank Accounts
      - Cash Management
      - Reconciliation
      - Treasury
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13540/T302934T531415.htm
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/api-cash-management.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Fixed Assets API
    description: API for managing fixed assets, depreciation, and asset lifecycle.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13549/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Asset Management
      - Capital Assets
      - Depreciation
      - Fixed Assets
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13549/T302934T531415.htm
      - type: API Guide
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e20282/toc.htm
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Purchasing API
    description: API for managing purchase orders, requisitions, and procurement operations.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13513/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Procurement
      - Purchase Orders
      - Purchasing
      - Requisitions
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13513/T302934T531415.htm
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/procurement/r13-update17d/oaprc/api-purchasing.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Expenses API
    description: API for managing employee expenses, expense reports, and reimbursements.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13548/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Expense Reports
      - Expenses
      - Reimbursements
      - Travel
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13548/T302934T531415.htm
      - type: API Guide
        url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/api-expenses.html
    contact:
      - type: Support
        url: https://support.oracle.com
  - name: Oracle Projects API
    description: API for managing projects, project costs, and project billing.
    image: https://www.oracle.com/a/ocom/img/oracle-financials-icon.png
    humanUrl: https://docs.oracle.com/cd/E18727_01/doc.121/e13523/toc.htm
    baseUrl: https://your-instance.oracle.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Contracts
      - Project Billing
      - Project Costing
      - Projects
    properties:
      - type: Documentation
        url: https://docs.oracle.com/cd/E18727_01/doc.121/e13523/T302934T531415.htm
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/project-management/r13-update17d/oapjm/api-projects.html
    contact:
      - type: Support
        url: https://support.oracle.com
common:
  - type: Portal
    url: https://support.oracle.com
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/authentication.html
  - type: Rate Limits
    url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/rate-limits.html
  - type: Status
    url: https://status.oracle.com
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Accounting
  - E-Business Suite
  - Enterprise
  - ERP
  - Financial Management
  - Oracle
  - Release 12
---
