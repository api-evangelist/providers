---
aid: sap-bi-tools
url: https://raw.githubusercontent.com/api-evangelist/sap-bi-tools/refs/heads/main/apis.yml
apis:
- name: SAP Analytics Cloud API
  description: RESTful API for SAP Analytics Cloud enabling data manipulation, story creation, and model management.
  image: https://www.sap.com/dam/application/shared/logos/sap-analytics-cloud.svg
  humanURL: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD
  baseURL: https://api.sapanalytics.cloud
  version: '1.0'
  tags:
  - Analytics
  - Cloud
  - Models
  - Stories
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/
  - type: OpenAPI
    url: https://api.sap.com/api/SACOpenAPI/overview
  - type: Authentication
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/b4f4d1e6e7fb4c08b0964e0b6d14d849.html
  - type: Rate Limits
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/rate-limits
  - type: Reference
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/fc2c581619264a40a37b98c19753c542.html
  - type: Getting Started
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/3ccfab3348dd407db089accb66cff9a2.html
  - type: Change Log
    url: https://www.sap.com/sea/products/data-cloud/cloud-analytics/features/release-highlights.html
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Analytics Cloud Data Export API
  description: OData-based API for exporting fact data and master data from SAP Analytics Cloud models. Allows programmatic extraction of underlying data and metadata for integration with external systems and data pipelines.
  image: https://www.sap.com/dam/application/shared/logos/sap-analytics-cloud.svg
  humanURL: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/3ccfab3348dd407db089accb66cff9a2.html
  baseURL: https://api.sapanalytics.cloud
  tags:
  - Analytics
  - Cloud
  - Data Export
  - OData
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/14cac91febef464dbb1efce20e3f1613/3ccfab3348dd407db089accb66cff9a2.html
  - type: GitHubRepository
    url: https://github.com/SAP-samples/analytics-cloud-export-api-wrapper
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Analytics Cloud Content Network REST API
  description: REST API for managing content in the SAP Analytics Cloud Content Network. Enables programmatic access to get, publish, and delete private and public content items available through the Content Network.
  image: https://www.sap.com/dam/application/shared/logos/sap-analytics-cloud.svg
  humanURL: https://help.sap.com/doc/9825c700f68e489ca5634a3da101a94c/release/en-US/ca804ae1c3874053a1e140e7c9cea019.pdf
  baseURL: https://api.sapanalytics.cloud
  tags:
  - Analytics
  - Cloud
  - Content Management
  properties:
  - type: Documentation
    url: https://help.sap.com/doc/9825c700f68e489ca5634a3da101a94c/release/en-US/ca804ae1c3874053a1e140e7c9cea019.pdf
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Analytics Cloud Analytics Designer API
  description: JavaScript-based API for building interactive analytic applications in SAP Analytics Cloud Analytics Designer. Provides scripting capabilities to control widgets, data sources, planning operations, and application behavior for embedded analytics scenarios.
  image: https://www.sap.com/dam/application/shared/logos/sap-analytics-cloud.svg
  humanURL: https://help.sap.com/doc/958d4c11261f42e992e8d01a4c0dde25/release/en-US/index.html
  tags:
  - Analytics
  - Application Design
  - Embedded Analytics
  - JavaScript
  properties:
  - type: Documentation
    url: https://help.sap.com/doc/958d4c11261f42e992e8d01a4c0dde25/release/en-US/index.html
  - type: Reference
    url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/fc2c581619264a40a37b98c19753c542.html
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP BusinessObjects BI Platform RESTful Web Services
  description: REST API for SAP BusinessObjects BI Platform for managing documents, users, and scheduling reports.
  humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM
  baseURL: https://server:port/biprws
  version: '4.3'
  tags:
  - BusinessObjects
  - Documents
  - Reports
  - Scheduling
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/e8c2e5877e9e44f9bfcc3085595b9208/
  - type: API Reference
    url: https://help.sap.com/doc/e39d9c134f1f4634addd5161f93dbf25/4.3/en-US/RESTful_Web_Services_User_Guide.pdf
  - type: SDK
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/e8c2e5877e9e44f9bfcc3085595b9208/sdk
  - type: Authentication
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/e8c2e5877e9e44f9bfcc3085595b9208/authentication
  - type: API Hub
    url: https://api.sap.com/package/BIPlatformRESTfulAPI
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP BusinessObjects Web Intelligence RESTful Web Services API
  description: REST API for SAP BusinessObjects Web Intelligence for creating, modifying, and exporting Web Intelligence reports. Provides endpoints for report management, data provider operations, and document scheduling separate from the general BI Platform REST API.
  humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/58f583a7643e48cf944cf554eb961f5b/45f8735d6e041014910aba7db0e91070.html
  baseURL: https://server:port/biprws
  version: '4.3'
  tags:
  - BusinessObjects
  - Data Providers
  - Reports
  - Web Intelligence
  properties:
  - type: Documentation
    url: https://help.sap.com/doc/1eeee826c0154c62a5cbd29359ecbc18/4.3/en-US/sbo43_webi_restws_dg_en.pdf
  - type: Reference
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/58f583a7643e48cf944cf554eb961f5b/45f8735d6e041014910aba7db0e91070.html
  - type: Quickstart
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/58f583a7643e48cf944cf554eb961f5b/7da2e2d66f701014aaab767bb0e91070.html
  - type: API Hub
    url: https://api.sap.com/api/SAPWebIntelligence/resource
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP BusinessObjects BI Semantic Layer REST API
  description: REST API for working with SAP BusinessObjects BI Semantic Layer universes. Allows querying and managing universes, executing queries against semantic layer data sources, and handling prompts and contexts programmatically.
  humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/58f583a7643e48cf944cf554eb961f5b/ec54808e6fdb101497906a7cb0e91070.html
  baseURL: https://server:port/biprws
  version: '4.3'
  tags:
  - BusinessObjects
  - Data Access
  - Semantic Layer
  - Universes
  properties:
  - type: Documentation
    url: https://help.sap.com/doc/a6296f37853c40388d5ada84c094d2cc/4.3.4/en-US/sbo43sp2_webisl_dev_guide_en.pdf
  - type: Reference
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_WEB_INTELLIGENCE/58f583a7643e48cf944cf554eb961f5b/ec54808e6fdb101497906a7cb0e91070.html
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Crystal Reports RESTful Web Services API
  description: RESTful API for SAP Crystal Reports for Enterprise that enables consuming and embedding Crystal Reports data in web and mobile applications. Supports retrieving report metadata, fetching data rows, setting parameters, and exporting reports in multiple formats.
  humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/0945312ac81f4b63be258130d2938055/45cecf3f6e041014910aba7db0e91070.html
  version: '2020'
  tags:
  - Crystal Reports
  - Embedded Analytics
  - Reporting
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/CRYSTAL_REPORTS/c5fb6213b96b4cc1bf43a55d68d9d87b/
  - type: SDK Download
    url: https://support.sap.com/en/product/analytics/crystal-reports.html
  - type: Developer Guide
    url: https://help.sap.com/doc/8f2e87893e944ec98a9c378aefdbbdd2/4.3.1/en-US/sbo43sp1_cr_restws_en.pdf
  - type: Reference
    url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/0945312ac81f4b63be258130d2938055/45cecf3f6e041014910aba7db0e91070.html
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Crystal Reports .NET SDK
  description: .NET SDK for integrating SAP Crystal Reports into Visual Studio applications. Enables developers to embed Crystal Reports into .NET web and desktop applications, programmatically create and modify reports, and manage report data sources and parameters.
  humanURL: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS,_DEVELOPER_VERSION_FOR_MICROSOFT_VISUAL_STUDIO/0d6684e153174710b8b2eb114bb7f843/a2cb609cfb6949b6a67b2effe32a347e.html
  version: '2020'
  tags:
  - .NET
  - Crystal Reports
  - SDK
  - Visual Studio
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS,_DEVELOPER_VERSION_FOR_MICROSOFT_VISUAL_STUDIO/0d6684e153174710b8b2eb114bb7f843/a2cb609cfb6949b6a67b2effe32a347e.html
  - type: Community
    url: https://pages.community.sap.com/topics/crystal-reports/visual-studio
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Lumira Discovery Extensions API
  description: JavaScript API for creating custom visualizations and extensions in SAP Lumira.
  humanURL: https://help.sap.com/docs/LUMIRA
  version: '2.4'
  tags:
  - Extensions
  - JavaScript
  - Lumira
  - Visualization
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/LUMIRA/82b8ad67e9b74a48bad806dc52c96fcc/
  - type: Extension API
    url: https://help.sap.com/docs/LUMIRA/extensions-api
  - type: Samples
    url: https://github.com/SAP/lumira-extension-viz
  - type: Developer Guide
    url: https://help.sap.com/doc/9d0bf4daa0cb41cbb630e093450b1bd8/2.3.0.0/en-US/lum_23SP00_ds_devguide_en.pdf
  contact:
  - type: GitHub
    url: https://github.com/SAP/lumira-extension-viz
- name: SAP HANA Cloud Data Lake Files REST API
  description: RESTful API for accessing and managing files in SAP HANA Cloud Data Lake file containers. Supports file operations, auditing file access, and managing data stored in the HANA Cloud Data Lake for BI and analytics workloads.
  humanURL: https://help.sap.com/docs/hana-cloud-data-lake
  baseURL: https://api.hana.ondemand.com
  version: '1.0'
  tags:
  - Cloud
  - Data Access
  - Data Lake
  - HANA
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/hana-cloud-data-lake
  - type: OpenAPI
    url: https://api.sap.com/api/HanaCloudDataLake/overview
  - type: Getting Started
    url: https://developers.sap.com/tutorials/data-lake-file-containers-restapi..html
  - type: Reference
    url: https://help.sap.com/doc/9d084a41830f46d6904fd4c23cd4bbfa/QRC_3_2021/en-US/html/index.html
  - type: API Hub
    url: https://api.sap.com/package/SAPHanaCloud/rest
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Datasphere API
  description: API for SAP Datasphere (formerly SAP Data Warehouse Cloud) for data integration, modeling, and consumption. Provides REST and OData endpoints for managing spaces, connections, data products, and consuming relational and analytical models.
  humanURL: https://help.sap.com/docs/SAP_DATASPHERE
  baseURL: https://datasphere-api.cfapps.eu10.hana.ondemand.com
  version: '2023'
  tags:
  - Data Modeling
  - Data Warehouse
  - Datasphere
  - Integration
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_DATASPHERE/9f804b8efa8043539289f42f372c4862/
  - type: API Reference
    url: https://help.sap.com/docs/SAP_DATASPHERE/api-reference
  - type: OpenAPI
    url: https://api.sap.com/api/Datasphere/overview
  - type: API Hub
    url: https://api.sap.com/package/sapdatasphere/overview
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
- name: SAP Datasphere Consumption and Catalog API
  description: OData V4 API for browsing the SAP Datasphere catalog and consuming datasets and metadata from consumable data assets. Enables external applications to discover available spaces, access relational and analytical models, and retrieve data products programmatically.
  humanURL: https://api.sap.com/api/DatasphereCatalog/resource/SAP_Datasphere_Consumption_Catalog
  baseURL: https://datasphere-api.cfapps.eu10.hana.ondemand.com
  tags:
  - Catalog
  - Data Consumption
  - Datasphere
  - OData
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/SAP_DATASPHERE/43509d67b8b84e66a30851e832f66911/7a453609c8694b029493e7d87e0de60a.html
  - type: API Hub
    url: https://api.sap.com/package/sapdatasphere/odatav4
  contact:
  - type: Support
    url: https://support.sap.com/en/index.html
name: SAP BI Tools
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
description: Collection of SAP Business Intelligence tools and APIs for analytics, reporting, and data visualization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

