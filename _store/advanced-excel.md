---
aid: advanced-excel
url: https://raw.githubusercontent.com/api-evangelist/advanced-excel/refs/heads/main/apis.yml
name: Advanced Excel
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Business Intelligence
  - Data Analysis
  - Data Processing
  - Excel
  - Microsoft
  - Spreadsheets
description: Advanced Excel is a subject-matter topic encompassing Microsoft Excel's programmatic capabilities for data analysis, formula execution, workbook management, chart generation, and automation. This topic index covers REST APIs, open data schemas, and developer tools for working with Excel workbooks programmatically, including Microsoft Graph Excel API, open-source spreadsheet libraries, and data interchange formats used in business intelligence and automation workflows.
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: Microsoft Graph Excel API
    description: The Microsoft Graph Excel API provides REST access to Excel workbooks stored in OneDrive, SharePoint, or Teams. Supports reading and writing cell values, executing formulas, managing worksheets, creating charts and tables, and running workbook sessions for transactional batch operations.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/excel
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Excel
      - Microsoft
      - OneDrive
      - REST API
      - Spreadsheets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: OpenAPI
        url: openapi/microsoft-graph-excel-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/microsoft-graph-excel-api-context.jsonld
      - type: Vocabulary
        url: vocabulary/advanced-excel-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/excel
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/excel-concept-overview
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/api/resources/excel
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/servicesagreement
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: Features
    data:
      - name: Workbook and Worksheet Management
        description: Create, read, update, and delete Excel workbooks and worksheets via REST API calls.
      - name: Formula Execution
        description: Execute Excel formulas and retrieve computed values programmatically via the Microsoft Graph API.
      - name: Range and Cell Operations
        description: Read and write cell values, apply formatting, and manipulate named ranges and tables.
      - name: Chart Generation
        description: Create and configure charts from worksheet data including column, line, pie, and bar chart types.
      - name: Table and PivotTable Operations
        description: Create, query, and manipulate Excel tables and pivot tables via API.
      - name: Session Management
        description: Manage persistent workbook sessions for transactional multi-step operations on Excel files.
      - name: Named Items and Functions
        description: Access named ranges, defined names, and custom functions within Excel workbooks.
      - name: Conditional Formatting
        description: Apply and query conditional formatting rules on cell ranges via the REST API.
  - type: UseCases
    data:
      - name: Automated Reporting
        description: Generate Excel-based financial, operational, or analytical reports programmatically from business data.
      - name: Data Import and Export
        description: Read data from Excel workbooks into business applications or write application data into Excel formats.
      - name: Spreadsheet Automation
        description: Automate repetitive Excel tasks such as data cleanup, formula recalculation, and sheet formatting.
      - name: Business Intelligence Pipelines
        description: Extract and transform Excel data for loading into data warehouses and BI tools.
      - name: Financial Modeling
        description: Execute complex financial models stored in Excel and retrieve results via API for application integration.
      - name: Form and Survey Data Collection
        description: Use Excel as a data store for forms and survey responses collected via web or mobile applications.
  - type: Integrations
    data:
      - name: Microsoft Power Automate
        description: No-code automation flows that read and write Excel data using the Excel Online Business connector.
      - name: Microsoft Power BI
        description: Publish Excel workbooks to Power BI for interactive dashboards and data visualization.
      - name: Azure Logic Apps
        description: Enterprise workflow automation that connects Excel data to Azure services and external APIs.
      - name: Python openpyxl
        description: Open-source Python library for reading and writing Excel 2010+ files without Microsoft Office.
      - name: Apache POI
        description: Java library for reading and writing Microsoft Office formats including Excel XLSX files.
      - name: ExcelJS
        description: Node.js library for reading, manipulating, and writing Excel workbook files.
      - name: Google Sheets API
        description: Google's spreadsheet REST API offering similar capabilities for Sheets-based workflows.
---
