---
aid: sap-bi
url: https://raw.githubusercontent.com/api-evangelist/sap-bi/refs/heads/main/apis.yml
apis:
- name: SAP Analytics Cloud API
  description: REST API for SAP Analytics Cloud enabling data integration, story management, and analytics operations.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD
  baseURL: https://[tenant].sapanalytics.cloud/api/v1
  tags:
  - Analytics
  - Cloud
  - Dashboards
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/147c1fd5bb3-4f8ba65b37acf1d6dbce.html
  - type: OpenAPI
    url: https://api.sap.com/api/API_ANALYTICS_CLOUD/overview
  - type: Authentication
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/c7e7c53f91bb41f8bd1440afd47ca49e.html
  - type: Swagger
    url: https://[tenant].sapanalytics.cloud/api/v1/swagger-ui.html
  - type: OpenAPI
    url: openapi/sap-bi-analytics-cloud-openapi.yml
- name: SAP BusinessObjects BI Platform REST API
  description: RESTful web services for SAP BusinessObjects BI Platform administration, content management, and reporting.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM
  baseURL: https://[server]:[port]/biprws
  tags:
  - BusinessObjects
  - Platform Administration
  - Reports
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ca1da879759d4c76894329a42c5b88c3/5051e4f36d6d1014b3fc9283b0e91070.html
  - type: OpenAPI
    url: https://api.sap.com/api/BOBJ_BIPLATFORM/overview
  - type: SDK Documentation
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ca1da879759d4c76894329a42c5b88c3/49e9e7f26d6d1014910c91fa5b0c2cc3.html
  - type: Authentication
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/ca1da879759d4c76894329a42c5b88c3/4f0990926d6d1014a74b9c23f567b6f4.html
  - type: OpenAPI
    url: openapi/sap-bi-businessobjects-platform-openapi.yml
- name: SAP HANA XS Advanced API
  description: APIs for building analytics applications on SAP HANA XS Advanced platform.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_HANA_PLATFORM
  baseURL: https://[host]:[port]
  tags:
  - Analytics
  - Database
  - HANA
  - XS Advanced
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/df19a03dc07e4ba19db4e0006c1da429.html
  - type: Developer Guide
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/3ec885c07e844d9fb4f40e3c4af0adb8.html
  - type: API Reference
    url: https://help.sap.com/docs/SAP_HANA_PLATFORM/4505d0bdaf4948449b7f7379d24d0f0d/c102c07e04c541cc906f5fcdb3e02105.html
- name: SAP BW/4HANA OData API
  description: OData services for accessing SAP BW/4HANA data warehouse content and metadata.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_BW4HANA
  baseURL: https://[server]:[port]/sap/opu/odata/sap/
  tags:
  - BW/4HANA
  - Data Warehouse
  - ETL
  - OData
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/5e467a851e874e48afcfa4cc88b5dd28.html
  - type: OData Reference
    url: https://api.sap.com/package/SAPBW4HANA/odata
  - type: Integration Guide
    url: https://help.sap.com/docs/SAP_BW4HANA/107a6e8a38b74ede94c833ca3b7b6f51/3801c14d27f046a79eed60a22ac6bd23.html
  - type: OpenAPI
    url: openapi/sap-bi-bw4hana-odata-openapi.yml
- name: SAP Datasphere API
  description: APIs for SAP Datasphere (formerly SAP Data Warehouse Cloud) for data integration and analytics.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_DATASPHERE
  baseURL: https://[tenant].datasphere.cloud.sap/api/v1
  tags:
  - Cloud
  - Data Integration
  - Data Warehouse
  - Datasphere
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/7f1a91f95e794a5e9f29abce8856c8cf.html
  - type: OpenAPI
    url: https://api.sap.com/api/datasphere/overview
  - type: API Reference
    url: https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/6c35457c1fc54a47b39aa5cdbc16d5e7.html
  - type: Authentication
    url: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/3de81838d5cd43ee91576a3b0b4e5e36.html
  - type: OpenAPI
    url: openapi/sap-bi-datasphere-openapi.yml
- name: SAP Crystal Reports API
  description: APIs for embedding and automating SAP Crystal Reports in applications.
  image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
  humanURL: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS
  baseURL: https://[server]/crystal/
  tags:
  - Crystal Reports
  - Embedded Analytics
  - Reporting
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/9e08a56e98d446b58af012538c121ff9/4650e1fe6d6d1014b3fc9283b0e91070.html
  - type: SDK Guide
    url: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/9e08a56e98d446b58af012538c121ff9/461aff6a6d6d1014910c91fa5b0c2cc3.html
  - type: Integration Samples
    url: https://wiki.scn.sap.com/wiki/display/BOBJ/Crystal+Reports+Developer+Center
name: SAP Business Intelligence
tags:
- Analytics
- Business Intelligence
- Data Visualization
- Reporting
- SAP
type: Contract
image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for SAP Business Intelligence (BI) platform, including analytics, reporting, and data visualization services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

