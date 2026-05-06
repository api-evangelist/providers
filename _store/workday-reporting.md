---
aid: workday-reporting
name: Workday Reporting
description: APIs for accessing Workday reporting functionality including custom reports, report data extraction, and report management.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/workday-reporting/refs/heads/main/apis.yml
tags:
  - Analytics
  - Business Intelligence
  - Financial Reporting
  - Hr Data
  - Reporting
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
common:
  - type: Developer Portal
    url: https://developer.workday.com
  - type: Community
    url: https://community.workday.com
  - type: Getting Started
    url: https://community.workday.com/api-start
  - type: Documentation
    url: https://community.workday.com/api
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
  - type: Rate Limits
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/f8K9WJ7Kh5FfQDNnvlHNFQ
  - type: Status
    url: https://community.workday.com/trust/status
  - type: Support
    url: https://www.workday.com/en-us/customer-experience/support.html
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Blog
    url: https://blog.workday.com/en-us/application-development.html
  - type: Website
    url: https://www.workday.com
  - type: Sign Up
    url: https://resourcecenter.workday.com/
  - type: GitHub Organization
    url: https://github.com/Workday
  - type: Reference
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: Marketplace
    url: https://marketplace.workday.com/en-US/home
  - type: Partners
    url: https://www.workday.com/en-us/company/partners/overview.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
