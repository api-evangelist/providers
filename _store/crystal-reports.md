---
aid: crystal-reports
name: Crystal Reports
description: APIs and resources for Crystal Reports, a business intelligence application for designing and generating reports from various data sources.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/crystal-reports/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-17'
apis:
  - name: Crystal Reports REST API
    description: RESTful API for managing and generating Crystal Reports programmatically.
    image: https://www.sap.com/dam/application/shared/logos/sap-logo.svg
    humanURL: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS
    baseURL: https://api.sap.com/crystal/v1
    tags:
      - Business Intelligence
      - Data Visualization
      - Enterprise
      - Reports
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/api
      - type: OpenAPI
        url: https://api.sap.com/crystal/openapi.json
      - type: Authentication
        url: https://help.sap.com/docs/SAP_CRYSTAL_REPORTS/authentication
    contact:
      - FN: SAP Support
        email: support@sap.com
        url: https://support.sap.com
    aid: crystal-reports:rest-api
  - name: Crystal Reports SDK
    description: Software Development Kit for embedding Crystal Reports into applications.
    humanURL: https://help.sap.com/docs/CRYSTAL_REPORTS_SDK
    baseURL: https://www.sap.com/sdk/crystal
    tags:
      - .NET
      - Embedding
      - Java
      - SDK
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/CRYSTAL_REPORTS_SDK
      - type: Download
        url: https://www.sap.com/products/technology-platform/crystal-reports/downloads.html
      - type: Code Samples
        url: https://github.com/SAP-samples/crystal-reports
    aid: crystal-reports:sdk
  - name: Crystal Reports Server REST API
    description: API for Crystal Reports Server administration and report management.
    humanURL: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM
    baseURL: https://server:port/biprws
    tags:
      - Administration
      - BI Platform
      - Report Management
      - Server
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/SAP_BUSINESSOBJECTS_BUSINESS_INTELLIGENCE_PLATFORM/rest-api
      - type: API Reference
        url: https://help.sap.com/doc/rest-api-reference
    aid: crystal-reports:server-rest-api
common:
  - type: Portal
    url: https://api.sap.com
  - type: Blog
    url: https://blogs.sap.com/tags/73554900100800000134/
  - type: Community
    url: https://community.sap.com/topics/crystal-reports
  - type: Support
    url: https://support.sap.com/crystal-reports
  - type: TermsOfService
    url: https://www.sap.com/about/legal/terms-of-use.html
  - type: PrivacyPolicy
    url: https://www.sap.com/about/legal/privacy.html
  - type: Features
    data:
      - name: Report Generation
        description: Generate formatted reports from relational databases, spreadsheets, and XML data sources.
      - name: Report Viewing
        description: Embed report viewers in web and desktop applications for interactive report consumption.
      - name: Report Scheduling
        description: Schedule automated report generation and delivery via email or file system.
      - name: Parameter Prompts
        description: Pass dynamic parameters to filter and customize report content at runtime.
      - name: Export Formats
        description: Export reports to PDF, Excel, Word, CSV, XML, and other formats programmatically.
      - name: Sub-Reports
        description: Embed linked sub-reports within parent reports for drill-down capabilities.
      - name: Cross-Tab Reports
        description: Generate pivot-table style cross-tabulation reports from data.
      - name: Charting
        description: Create charts and graphs within reports for data visualization.
      - name: Data Source Connectivity
        description: Connect to SQL Server, Oracle, SAP HANA, ODBC, JDBC, and other data sources.
      - name: Report Server Management
        description: Manage report server instances, folders, users, and security via REST API.
  - type: UseCases
    data:
      - name: Financial Reporting
        description: Generate financial statements, balance sheets, and P&L reports from ERP data.
      - name: Operational Dashboards
        description: Create operational reports for manufacturing, logistics, and supply chain.
      - name: Compliance Reports
        description: Generate regulatory compliance reports for auditing and governance.
      - name: Customer Invoicing
        description: Produce formatted invoices and statements from billing data.
      - name: HR Analytics
        description: Generate employee reports, headcount analytics, and compensation summaries.
      - name: Embedded Reporting
        description: Embed Crystal Reports viewer into custom applications for end-user reporting.
  - type: Solutions
    data:
      - name: SAP Crystal Reports
        description: Desktop report designer for creating and editing report templates.
      - name: SAP Crystal Reports Server
        description: Server platform for scheduling, managing, and distributing reports.
      - name: SAP BusinessObjects BI
        description: Enterprise BI platform with Crystal Reports integration.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Business Intelligence
  - Crystal Reports
  - Data Analytics
  - Enterprise Software
  - Reporting
  - SAP
specificationVersion: '0.19'
---
