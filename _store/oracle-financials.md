---
aid: oracle-financials
name: Oracle Financials
description: Collection of Oracle Financials Cloud APIs for financial management, accounting, and reporting.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/apis.yml
tags:
  - Accounting
  - Accounts Payable
  - Accounts Receivable
  - Cash Management
  - ERP
  - Expense Management
  - Financial Management
  - General Ledger
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - name: Oracle Financials General Ledger API
    description: Manage general ledger operations including journals, account balances, and period closings.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Account Balances
      - Chart of Accounts
      - General Ledger
      - Journals
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-general-ledger.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-general-ledger.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financials Accounts Payable API
    description: Manage supplier invoices, payments, and expense reports.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounts Payable
      - Invoices
      - Payments
      - Suppliers
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-payables.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-payables.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financials Accounts Receivable API
    description: Manage customer invoices, receipts, and credit management.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Accounts Receivable
      - Credit Management
      - Customer Invoices
      - Receipts
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-receivables.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-receivables.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financials Cash Management API
    description: Manage cash positioning, bank statements, and reconciliation.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Bank Accounts
      - Cash Forecasting
      - Cash Management
      - Reconciliation
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-cash-management.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-cash-management.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financials Expense Management API
    description: Manage employee expenses, reimbursements, and expense reports.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Corporate Cards
      - Expense Management
      - Expense Reports
      - Reimbursements
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-expenses.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-expenses.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financials Fixed Assets API
    description: Manage asset lifecycle, depreciation, and asset transfers.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Asset Management
      - Asset Tracking
      - Depreciation
      - Fixed Assets
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-fixed-assets.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-fixed-assets.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle Financial Reporting API
    description: Access financial reports, analytics, and business intelligence data.
    image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/
    baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
    tags:
      - Analytics
      - Business Intelligence
      - Financial Reports
      - Reporting
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/api-financial-reporting.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/openapi-reporting.yaml
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
common:
  - type: Getting Started
    url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/getting-started.html
  - type: Authentication Guide
    url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
  - type: Rate Limits
    url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/rate-limits.html
  - type: Support
    url: https://support.oracle.com
  - type: Status Page
    url: https://ocistatus.oraclecloud.com
  - type: Terms of Service
    url: https://www.oracle.com/corporate/contracts/cloud-services/
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
