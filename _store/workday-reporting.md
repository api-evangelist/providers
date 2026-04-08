---
aid: workday-reporting
url: https://raw.githubusercontent.com/api-evangelist/workday-reporting/refs/heads/main/apis.yml
apis:
- name: Workday Report as a Service (RaaS)
  description: REST API for retrieving report data from custom reports in Workday.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Reporting/v1/index.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/service/{tenant}/Reporting
  tags:
  - Data Extraction
  - Raas
  - Reports
  - Rest
  properties:
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Reporting/v1/index.html
  - type: OpenAPI
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Reporting/v1/Reporting.yaml
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
  - type: Client Libraries
    url: https://github.com/Workday/raas-python
  contact:
  - FN: Workday Support
    email: support@workday.com
    url: https://community.workday.com
- name: Workday Custom Reports API
  description: API for managing and executing custom reports programmatically.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/sxVLLu9fFSJM5BffiOZwmA
  baseURL: https://wd2-impl-services1.workday.com/ccx/service/{tenant}
  tags:
  - Custom Reports
  - Report Execution
  - Soap
  properties:
  - type: Documentation
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/sxVLLu9fFSJM5BffiOZwmA
  - type: WSDL
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Report_as_a_Service/Report_as_a_Service.html
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
- name: Workday Advanced Reports API
  description: API for accessing advanced reporting features including matrix reports and composite reports.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://doc.workday.com/reader/wsiU0cn5CkB~MbuzChYv1w/_YO8X6WAWjLFBkBLamVxkw
  baseURL: https://wd2-impl-services1.workday.com/ccx/service/{tenant}
  tags:
  - Advanced Reporting
  - Composite Reports
  - Matrix Reports
  properties:
  - type: Documentation
    url: https://doc.workday.com/reader/wsiU0cn5CkB~MbuzChYv1w/_YO8X6WAWjLFBkBLamVxkw
  - type: Guides
    url: https://doc.workday.com/reader/wsiU0cn5CkB~MbuzChYv1w/root_landing.html
- name: Workday Prism Analytics REST API
  description: REST API for working with Workday Prism Analytics tables, data change tasks, and datasets. Enables programmatic creation and management of analytics data including ingesting external data, building transformation pipelines, and publishing datasets for reporting and analysis.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://doc.workday.com/admin-guide/en-us/workday-prism-analytics/workday-prism-analytics-api.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/api/prismAnalytics/v2/{tenant}
  tags:
  - Analytics
  - Data Integration
  - Datasets
  - Prism Analytics
  properties:
  - type: Documentation
    url: https://doc.workday.com/admin-guide/en-us/workday-prism-analytics/workday-prism-analytics-api.html
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
  - type: Client Libraries
    url: https://github.com/Workday/prism-python
- name: Workday Prism Analytics SOAP Web Service
  description: SOAP web service for creating, editing, and retrieving objects related to Prism Analytics, including analytic dimension business objects, analytic dimension hierarchies, and analytic dimension values.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://community.workday.com/sites/default/files/file-hosting/productionapi/Prism_Analytics/v45.2/Prism_Analytics.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/service/{tenant}/Prism_Analytics
  tags:
  - Analytic Dimensions
  - Hierarchies
  - Prism Analytics
  - SOAP
  properties:
  - type: Documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Prism_Analytics/v45.2/Prism_Analytics.html
  - type: WSDL
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Prism_Analytics/v45.2/Prism_Analytics.wsdl
- name: Workday WQL API
  description: Workday Query Language (WQL) API enabling SQL-like querying of Workday data through REST endpoints. Provides high-performance data access for reporting and analytics use cases, with support for pagination, filtering, sorting, and aggregation controlled via OAuth 2.0 tokens.
  image: https://www.workday.com/content/dam/web/en-us/images/misc/workday-logo.svg
  humanURL: https://doc.workday.com/admin-guide/en-us/reporting-and-analytics/custom-reports-and-analytics/workday-query-language-wql-/aht1611188422513.html
  baseURL: https://wd2-impl-services1.workday.com/ccx/api/wql/v1/{tenant}
  tags:
  - Analytics
  - Data Access
  - Query Language
  - Reporting
  properties:
  - type: Documentation
    url: https://doc.workday.com/admin-guide/en-us/reporting-and-analytics/custom-reports-and-analytics/workday-query-language-wql-/aht1611188422513.html
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
name: Workday Reporting
tags:
- Analytics
- Business Intelligence
- Financial Reporting
- Hr Data
- Reporting
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for accessing Workday reporting functionality including custom reports, report data extraction, and report management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

