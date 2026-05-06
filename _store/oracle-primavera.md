---
aid: oracle-primavera
name: Oracle Primavera
description: Oracle Primavera is a portfolio of project portfolio management (PPM) applications for construction, engineering, and capital project industries. Primavera APIs provide programmatic access to enterprise project portfolio management data including WBS structures, activity schedules, resource assignments, critical path analysis, and portfolio dashboards across cloud and on-premises deployments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-primavera/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Construction
  - Engineering
  - Project Management
  - Scheduling
  - Portfolio Management
  - Oracle
apis:
  - name: Oracle Primavera P6 EPPM REST API
    description: Oracle Primavera P6 EPPM REST API provides programmatic access to enterprise project portfolio management data including WBS structures, activity schedules, resource assignments, critical path analysis, and portfolio dashboards. Available for both cloud and on-premises deployments. Documentation covers version 6.2.1 through version 26 (2026).
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/construction-engineering/primavera-p6-project/index.html
    baseURL: https://{host}/p6ws/rest/v1
    tags:
      - Construction
      - EPPM
      - Project Management
      - REST
      - Scheduling
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/construction-engineering/primavera-p6-project/index.html
      - type: Reference
        url: https://docs.oracle.com/cd/G48897_01/index.htm
      - type: Change Log
        url: https://docs.oracle.com/cd/E64687_01/EPPM/EPPM_CFO.html
      - type: OpenAPI
        url: openapi/oracle-primavera-p6-eppm-openapi.yml
  - name: Oracle Primavera Gateway Integration API
    description: Oracle Primavera Gateway provides integration APIs for connecting Primavera P6 with other Oracle and third-party applications. Enables bi-directional data exchange for projects, resources, cost accounts, and activity data between P6 EPPM and ERP, asset management, and financial systems.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/construction-engineering/primavera-gateway/index.html
    tags:
      - Construction
      - Integration
      - Project Management
      - Scheduling
      - XML
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/construction-engineering/primavera-gateway/index.html
  - name: Oracle Primavera Analytics API
    description: Oracle Primavera Analytics provides reporting and business intelligence APIs for portfolio performance insights, project health dashboards, resource utilization analysis, and earned value management reporting across construction and engineering portfolios.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/construction-engineering/primavera-analytics/index.html
    tags:
      - Analytics
      - Construction
      - Project Management
      - Reporting
      - Scheduling
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/construction-engineering/primavera-analytics/index.html
  - name: Oracle Primavera P6 Scheduling API
    description: Oracle Primavera P6 provides project scheduling and portfolio management APIs for construction, engineering, and capital projects. REST and XML APIs enable access to WBS structures, activity schedules, resource assignments, and critical path analysis.
    image: https://www.oracle.com/a/ocom/img/social-og-oracle-cloud.jpg
    humanURL: https://docs.oracle.com/en/industries/construction-engineering/primavera/
    tags:
      - Construction
      - Project Management
      - Scheduling
      - XML
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/industries/construction-engineering/primavera/
common:
  - type: Portal
    url: https://docs.oracle.com/en/industries/construction-engineering/primavera/
  - type: Website
    url: https://www.oracle.com/construction-engineering/primavera/
  - type: Documentation
    url: https://docs.oracle.com/en/industries/construction-engineering/primavera-p6-project/index.html
  - type: Reference
    url: https://docs.oracle.com/cd/G48897_01/index.htm
  - type: Change Log
    url: https://docs.oracle.com/cd/E64687_01/EPPM/EPPM_CFO.html
  - type: Getting Started
    url: https://mylearn.oracle.com/construction
  - type: Support
    url: https://www.oracle.com/support/
  - type: Status
    url: https://ocistatus.oraclecloud.com/
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: OpenAPI
    url: openapi/oracle-primavera-p6-eppm-openapi.yml
  - type: JSON Schema
    url: json-schema/oracle-primavera-project-schema.json
  - type: JSON Schema
    url: json-schema/oracle-primavera-activity-schema.json
  - type: JSON-LD Context
    url: json-ld/oracle-primavera-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
