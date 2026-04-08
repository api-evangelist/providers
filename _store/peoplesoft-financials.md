---
aid: peoplesoft-financials
url: https://raw.githubusercontent.com/api-evangelist/peoplesoft-financials/refs/heads/main/apis.yml
apis:
- name: PeopleSoft General Ledger API
  description: REST API for managing general ledger operations including journals, chartfields, budgets, and financial reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/gl/
  tags:
  - ChartFields
  - Financial Reporting
  - General Ledger
  - Journals
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/gl/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Accounts Payable API
  description: REST API for vendor management, invoice processing, payments, and AP reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/ap/
  tags:
  - Accounts Payable
  - Invoices
  - Payments
  - Vendors
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/ap/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Accounts Receivable API
  description: REST API for customer management, billing, receipts, and AR reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/ar/
  tags:
  - Accounts Receivable
  - Billing
  - Customers
  - Receipts
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/ar/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Asset Management API
  description: REST API for fixed asset tracking, depreciation, transfers, and asset reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/am/
  tags:
  - Asset Management
  - Asset Tracking
  - Depreciation
  - Fixed Assets
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/am/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Purchasing API
  description: REST API for purchase requisitions, purchase orders, receiving, and procurement reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/po/
  tags:
  - Procurement
  - Purchase Orders
  - Purchasing
  - Requisitions
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/po/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Expenses API
  description: REST API for expense reporting, reimbursements, and travel management.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/exp/
  tags:
  - Expense Reports
  - Expenses
  - Reimbursements
  - Travel
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/exp/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Projects API
  description: REST API for project costing, billing, resource management, and project reporting.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/financials/proj/
  tags:
  - Billing
  - Project Costing
  - Projects
  - Resources
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/proj/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: PeopleSoft Query API
  description: REST API for executing PeopleSoft queries and retrieving data from various financial modules.
  image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
  humanURL: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/index.html
  baseURL: https://{hostname}:{port}/psrestservice/query/
  tags:
  - Data Retrieval
  - Query
  - Reporting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E92519_02/fscm92pbr30/eng/fscm/rest_services/index.html
  - type: OpenAPI
    url: https://api.example.com/peoplesoft/query/openapi.json
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
name: PeopleSoft Financials
tags:
- Enterprise
- ERP
- Financials
- Oracle
- PeopleSoft
type: Contract
image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API collection for Oracle PeopleSoft Financials suite covering General Ledger, Accounts Payable, Accounts Receivable, Asset Management, and other financial modules.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

