---
aid: sap-bw
name: SAP BW
description: SAP Business Warehouse (SAP BW) and SAP BW/4HANA provide enterprise data warehousing capabilities with APIs for data extraction, query execution, metadata management, and integration with SAP and non-SAP systems. The platform offers OData services, BAPI/RFC interfaces, and Analysis Office APIs for programmatic access to data warehouse operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/sap-bw/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Business Intelligence
  - Data Warehousing
  - Enterprise
  - ETL
  - SAP
apis:
  - aid: sap-bw:odata-api
    name: SAP BW OData API
    description: OData-based REST API for querying SAP BW data, executing BEx queries, and accessing InfoProviders. Supports analytical queries with filtering, aggregation, and hierarchical navigation.
    humanURL: https://help.sap.com/docs/SAP_BW4HANA
    baseURL: https://sap-host/sap/opu/odata/sap/
    tags:
      - Analytics
      - OData
      - Queries
      - REST
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_BW4HANA
  - aid: sap-bw:bapi-api
    name: SAP BW BAPI/RFC API
    description: Business Application Programming Interfaces (BAPIs) and Remote Function Call (RFC) interfaces for SAP BW providing access to metadata management, data loading, process chain execution, and administrative operations.
    humanURL: https://help.sap.com/docs/SAP_BW4HANA
    baseURL: https://sap-host/sap/bc/
    tags:
      - BAPI
      - Enterprise
      - Metadata
      - RFC
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_BW4HANA
  - aid: sap-bw:analysis-office-api
    name: SAP Analysis for Office API
    description: API for SAP Analysis for Microsoft Office providing programmatic control of analytical workbooks, data source connections, and report automation within Excel and PowerPoint.
    humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_ANALYSIS_OFFICE
    baseURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_ANALYSIS_OFFICE
    tags:
      - Analysis
      - Excel
      - Office Integration
      - Reporting
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_ANALYSIS_OFFICE
common:
  - type: Portal
    url: https://help.sap.com/docs/SAP_BW4HANA
  - type: Documentation
    url: https://help.sap.com/docs/SAP_BW4HANA
  - type: GettingStarted
    url: https://learning.sap.com/
  - type: Support
    url: https://support.sap.com/
  - type: Blog
    url: https://community.sap.com/topics/bw
  - type: TermsOfService
    url: https://www.sap.com/about/legal/terms-of-use.html
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: Training
    url: https://learning.sap.com/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/sap-bw
  - type: Features
    data:
      - name: Enterprise Data Warehousing
        description: Centralized data warehousing with support for structured and unstructured data across SAP and non-SAP sources.
      - name: BEx Query Execution
        description: Execute Business Explorer queries programmatically with filtering, hierarchies, and key figure calculations.
      - name: OData Query Access
        description: Access SAP BW data through standard OData REST services for modern application integration.
      - name: Process Chain Management
        description: Automate and monitor ETL process chains for scheduled data loading and transformation.
      - name: Metadata Services
        description: Programmatic access to InfoProvider metadata, hierarchies, and data model definitions.
  - type: UseCases
    data:
      - name: Enterprise Reporting
        description: Build enterprise reports and dashboards connecting to SAP BW data through OData and BAPI interfaces.
      - name: Data Integration
        description: Extract and load data between SAP BW and external systems using API-based integration.
      - name: Automated ETL Workflows
        description: Automate data warehouse loading processes with API-triggered process chain execution.
      - name: Self-Service Analytics
        description: Enable business users to access BW data through Analysis for Office API integrations.
  - type: Integrations
    data:
      - name: SAP Analytics Cloud
        description: Integration with SAP Analytics Cloud for modern analytics and planning on BW data.
      - name: SAP HANA
        description: Native HANA optimization for SAP BW/4HANA with in-memory data processing.
      - name: Microsoft Excel
        description: Analysis for Office integration for enterprise reporting directly in Excel.
      - name: SAP Data Intelligence
        description: Data pipeline integration for connecting BW with data lakes and machine learning workloads.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
