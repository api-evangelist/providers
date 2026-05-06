---
aid: oracle-financial-applications
name: Oracle Financial Applications
description: Collection of APIs for Oracle's suite of financial management applications including ERP Cloud, EPM Cloud, and related financial services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-financial-applications/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Accounting
  - Cloud Applications
  - Enterprise Performance Management
  - Enterprise Resource Planning
  - EPM
  - ERP
  - Financial Management
  - Financial Reporting
apis:
  - name: Oracle ERP Cloud REST API
    description: REST APIs for Oracle ERP Cloud covering modules like General Ledger, Accounts Payable, Accounts Receivable, Cash Management, and Fixed Assets.
    image: https://www.oracle.com/a/ocom/img/oracle-cloud.svg
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/
    tags:
      - Accounts Payable
      - Accounts Receivable
      - ERP
      - General Ledger
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/
      - type: OpenAPI
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/op-version-latest-get.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/Authentication.html
      - type: SDKs
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
  - name: Oracle General Ledger REST API
    description: APIs for managing chart of accounts, journal entries, budgets, allocations, and financial reporting in Oracle ERP Cloud.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05/
    tags:
      - Budgets
      - Chart of Accounts
      - General Ledger
      - Journals
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/api-general-ledger.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/endpoints-general-ledger.html
  - name: Oracle Accounts Payable REST API
    description: APIs for managing supplier invoices, payments, expense reports, and procurement transactions.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05/
    tags:
      - Accounts Payable
      - Invoices
      - Payments
      - Suppliers
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/api-payables.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/endpoints-payables.html
  - name: Oracle Accounts Receivable REST API
    description: APIs for managing customer invoices, receipts, credit memos, and revenue recognition.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05/
    tags:
      - Accounts Receivable
      - Customers
      - Invoices
      - Receipts
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/api-receivables.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/endpoints-receivables.html
  - name: Oracle Cash Management REST API
    description: APIs for bank account management, cash positioning, forecasting, and reconciliation.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05/
    tags:
      - Bank Accounts
      - Cash Management
      - Reconciliation
      - Treasury
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/api-cash-management.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/endpoints-cash-management.html
  - name: Oracle Fixed Assets REST API
    description: APIs for managing asset lifecycle, depreciation, mass additions, and asset tracking.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financials/
    baseUrl: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05/
    tags:
      - Asset Management
      - Depreciation
      - Fixed Assets
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/api-assets.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financials/24d/farfa/endpoints-assets.html
  - name: Oracle EPM Cloud REST API
    description: REST APIs for Oracle Enterprise Performance Management Cloud including Planning, Financial Consolidation and Close, Tax Reporting, and Account Reconciliation.
    humanUrl: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/
    baseUrl: https://{instance}.oraclecloud.com/epm/rest/
    tags:
      - Account Reconciliation
      - Budgeting
      - EPM
      - Financial Consolidation
      - Planning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/rest_endpoints.html
      - type: Authentication
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/api_authentication.html
  - name: Oracle Financial Reporting REST API
    description: APIs for creating, managing, and executing financial reports, including Smart View integration.
    humanUrl: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/
    baseUrl: https://{instance}.oraclecloud.com/epm/rest/
    tags:
      - Analytics
      - Financial Reporting
      - Reports
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/rep_rest_api_intro.html
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/rest_api_financial_reporting_overview.html
  - name: Oracle FCCS REST API
    description: APIs for Financial Consolidation and Close Cloud Service for consolidations, eliminations, currency translation, and intercompany management.
    humanUrl: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/
    baseUrl: https://{instance}.oraclecloud.com/epm/rest/
    tags:
      - Close Management
      - Consolidation
      - Currency Translation
      - Eliminations
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/fcgrs/
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/financial-consolidation-cloud/fcgrs/rest_endpoints.html
  - name: Oracle ARCS REST API
    description: APIs for Account Reconciliation Cloud Service for managing reconciliations, certifications, and compliance workflows.
    humanUrl: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/
    baseUrl: https://{instance}.oraclecloud.com/epm/rest/
    tags:
      - Account Reconciliation
      - Certifications
      - Compliance
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/suarc/
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/suarc/rest_endpoints.html
  - name: Oracle Planning REST API
    description: APIs for Planning and Budgeting Cloud Service including data management, business rules, and planning operations.
    humanUrl: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/
    baseUrl: https://{instance}.oraclecloud.com/epm/rest/
    tags:
      - Budgeting
      - Forecasting
      - Planning
      - Workforce Planning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/pfusr/
      - type: API Reference
        url: https://docs.oracle.com/en/cloud/saas/planning-budgeting-cloud/pfusr/rest_endpoints.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include:
  - name: Oracle Cloud Infrastructure APIs
    url: https://docs.oracle.com/en-us/iaas/api/
  - name: Oracle Integration Cloud APIs
    url: https://docs.oracle.com/en/cloud/paas/integration-cloud/
common:
  - type: Portal
    url: https://cloud.oracle.com/
  - type: Getting Started
    url: https://docs.oracle.com/en/cloud/saas/financials/get-started.html
  - type: Support
    url: https://support.oracle.com/
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: Pricing
    url: https://www.oracle.com/cloud/price-list.html
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
  - type: Training
    url: https://education.oracle.com/
---
