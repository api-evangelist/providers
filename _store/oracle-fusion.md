---
aid: oracle-fusion
url: https://raw.githubusercontent.com/api-evangelist/oracle-fusion/refs/heads/main/apis.yml
apis:
- name: Oracle Fusion ERP REST API
  description: REST APIs for Oracle Fusion Cloud ERP, providing programmatic access to financials, procurement, project management, and risk management capabilities. The API supports viewing and managing financial data including general ledger, accounts payable, accounts receivable, fixed assets, and cash management.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/financials/
  baseURL: https://{instance}.oraclecloud.com/fscmRestApi/
  tags:
  - ERP
  - Financials
  - Procurement
  - Projects
  - Risk Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
  - type: OpenAPI
    url: https://docs.oracle.com/en/cloud/saas/financials/22r3/farfa/api-rest-api.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/financials/22r3/farfa/Authentication.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/financials/26a/index.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-erp-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion HCM REST API
  description: REST APIs for Oracle Fusion Cloud Human Capital Management, enabling integration with core HR, talent management, workforce management, and payroll systems. The API provides access to employee records, absence management, benefits, compensation, recruiting, and learning resources.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/human-resources/
  baseURL: https://{instance}.oraclecloud.com/hcmRestApi/
  tags:
  - HCM
  - Human Resources
  - Payroll
  - Talent Management
  - Workforce
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/human-resources/22r3/farws/
  - type: OpenAPI
    url: https://docs.oracle.com/en/cloud/saas/human-resources/22r3/farws/api-rest-api.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/human-resources/22r3/farws/Authentication.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/human-resources/26a/index.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/hcm/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-hcm-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion SCM REST API
  description: REST APIs for Oracle Fusion Cloud Supply Chain Management, providing access to inventory, order management, procurement, logistics, and manufacturing capabilities. The API enables integration with supply chain planning, product lifecycle management, service logistics, and supply chain execution processes.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/supply-chain-management/
  baseURL: https://{instance}.oraclecloud.com/fscmRestApi/
  tags:
  - Inventory
  - Logistics
  - Manufacturing
  - Order Management
  - SCM
  - Supply Chain
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/supply-chain-management/22r3/fasrs/
  - type: OpenAPI
    url: https://docs.oracle.com/en/cloud/saas/supply-chain-management/22r3/fasrs/api-rest-api.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/supply-chain-management/22r3/fasrs/Authentication.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/supply-chain-management/26a/index.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/scm/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-scm-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion CX Sales and Fusion Service REST API
  description: REST APIs for Oracle Fusion Cloud Customer Experience, enabling integration with sales force automation, fusion service, customer data management, and commerce applications. The API provides access to accounts, contacts, opportunities, leads, service requests, activities, and other CRM resources.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/sales/
  baseURL: https://{instance}.oraclecloud.com/crmRestApi/
  tags:
  - Commerce
  - Customer Experience
  - CX
  - Marketing
  - Sales
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/sales/faaps/index.html
  - type: OpenAPI
    url: https://docs.oracle.com/en/cloud/saas/cx-sales/rest-api.html
  - type: Authentication
    url: https://docs.oracle.com/en/cloud/saas/cx-sales/rest-authentication.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/sales/index.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/sales.html
  - type: OpenAPI
    url: openapi/oracle-fusion-cx-sales-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion Common Features REST API
  description: REST APIs for Oracle Fusion Cloud Applications Common features, providing access to shared services such as attachments, flexfields, lookup types, roles, users, security, and approval workflows used across all Fusion Cloud application pillars. This is the foundational API that supports cross-pillar integration capabilities.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/applications-common/
  baseURL: https://{instance}.oraclecloud.com/fscmRestApi/
  tags:
  - Attachments
  - Common
  - Flexfields
  - Roles
  - Security
  - Users
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/applications-common/26a/farca/index.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/applications-common/26a/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-common-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion Project Management REST API
  description: REST APIs for Oracle Fusion Cloud Project Management, enabling integration with project planning, project costing, project billing, grants management, and project execution capabilities. The API supports managing project resources, tasks, budgets, and deliverables.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/project-management/
  baseURL: https://{instance}.oraclecloud.com/fscmRestApi/
  tags:
  - Grants
  - Project Billing
  - Project Costing
  - Project Management
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/project-management/26a/fapap/index.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/project-management/26a/index.html
  - type: Change Log
    url: https://docs.oracle.com/en/cloud/saas/readiness/erp/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-project-management-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
- name: Oracle Fusion EPM REST API
  description: REST APIs for Oracle Fusion Cloud Enterprise Performance Management, enabling integration with planning, budgeting, forecasting, financial consolidation, account reconciliation, tax reporting, and narrative reporting capabilities. The EPM REST APIs allow infrastructure consultants to integrate environments with Oracle EPM Cloud services.
  image: https://www.oracle.com/a/ocom/img/oracle-logo.svg
  humanURL: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/
  baseURL: https://{instance}.oraclecloud.com/HyperionPlanning/rest/
  tags:
  - Budgeting
  - Consolidation
  - EPM
  - Financial Close
  - Planning
  properties:
  - type: Documentation
    url: https://docs.oracle.com/en/cloud/saas/enterprise-performance-management-common/prest/index.html
  - type: GettingStarted
    url: https://docs.oracle.com/en/cloud/saas/epm-cloud/index.html
  - type: OpenAPI
    url: openapi/oracle-fusion-epm-openapi.yml
  contact:
  - FN: Oracle Support
    email: support@oracle.com
    url: https://support.oracle.com
name: Oracle Fusion Cloud Applications
tags:
- Cloud
- CX
- Enterprise
- EPM
- ERP
- HCM
- Project Management
- REST API
- SaaS
- SCM
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Fusion Cloud Applications represent a comprehensive suite of cloud-based enterprise resource planning (ERP), human capital management (HCM), customer experience (CX), supply chain management (SCM), and enterprise performance management (EPM) solutions. Oracle Fusion Cloud provides REST APIs across all application pillars, enabling programmatic access to business data and processes for integration, automation, and extension of cloud applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

