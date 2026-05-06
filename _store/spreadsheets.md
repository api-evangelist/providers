---
aid: spreadsheets
name: Spreadsheets
description: Spreadsheets covers the APIs, tools, and services for programmatic access to spreadsheet data across major platforms including Google Sheets and Microsoft Excel. The Google Sheets API v4 provides RESTful access to read, write, format, and manage Google Spreadsheets. The Microsoft Graph Excel API enables reading and writing Excel workbooks stored in OneDrive for Business and SharePoint. Third-party services like SheetDB, Sheety, Sheet Best, and Sheet2API convert spreadsheets into REST APIs for use as lightweight backends. Spreadsheet APIs are widely used for data import/export, automated reporting, form submissions, lightweight CMS, and business process automation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Spreadsheets
  - Data
  - Google Sheets
  - Excel
  - Productivity
  - Automation
created: '2026-03-16'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/spreadsheets/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: spreadsheets:google-sheets-api
    name: Google Sheets API
    description: The Google Sheets API v4 is a RESTful interface that lets developers read and modify Google Spreadsheet data programmatically. The API supports creating spreadsheets, reading and writing cell values by range (A1 notation), batch operations for efficiency, managing sheet structure and formatting, and accessing developer metadata. Authentication uses Google OAuth 2.0. The API is widely used for data pipelines, automated reporting, form data collection, and spreadsheet-powered applications.
    humanURL: https://developers.google.com/workspace/sheets/api
    baseURL: https://sheets.googleapis.com/v4
    tags:
      - Google Sheets
      - Spreadsheets
      - Data
      - Productivity
      - Google Workspace
    properties:
      - type: Documentation
        url: https://developers.google.com/workspace/sheets/api/guides/concepts
      - type: Reference
        url: https://developers.google.com/workspace/sheets/api/reference/rest
      - type: OpenAPI
        url: openapi/google-sheets-openapi.yml
      - type: Getting Started
        url: https://developers.google.com/workspace/sheets/api/quickstart/python
      - type: Discovery
        url: https://sheets.googleapis.com/$discovery/rest?version=v4
    features:
      - type: SpreadsheetCRUD
        description: Create, read, and batch-update entire spreadsheets
      - type: ValueReadWrite
        description: Read and write cell values by range using A1 notation (e.g., Sheet1!A1:B2)
      - type: BatchOperations
        description: Batch read/write multiple ranges in a single API call for efficiency
      - type: SheetFormatting
        description: Apply number formats, text formatting, conditional formatting, and cell styles
      - type: DataValidation
        description: Set and enforce data validation rules on cell ranges
      - type: PivotTables
        description: Create and manage pivot tables programmatically
      - type: Charts
        description: Create, update, and embed charts in spreadsheets
      - type: DeveloperMetadata
        description: Attach custom metadata to spreadsheets for application use
    useCases:
      - type: DataPipeline
        description: Import and export data between databases and spreadsheets
      - type: AutomatedReporting
        description: Generate weekly/monthly reports directly into Google Sheets
      - type: FormDataCollection
        description: Write form submission data to spreadsheets as a lightweight backend
      - type: FinancialModeling
        description: Programmatically update financial models with live data
      - type: ContentManagement
        description: Use Sheets as a lightweight CMS for websites and apps
  - aid: spreadsheets:microsoft-graph-excel-api
    name: Microsoft Graph Excel API
    description: The Microsoft Graph Excel API enables reading and writing Excel workbooks (.xlsx format) stored in OneDrive for Business, SharePoint, or Group drives via the Microsoft Graph REST API. Supports worksheets, ranges, tables, charts, named items, and Excel worksheet functions. Uses session-based access for efficient multi-step operations. Authentication requires Microsoft identity platform (OAuth 2.0) with Files.Read or Files.ReadWrite scopes.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/excel
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Excel
      - Microsoft Graph
      - Microsoft 365
      - Spreadsheets
      - OneDrive
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: Reference
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/graph/excel-use-functions
    features:
      - type: WorkbookAccess
        description: Read and modify .xlsx workbooks stored in OneDrive for Business and SharePoint
      - type: Sessions
        description: Persistent and non-persistent session management for efficient operations
      - type: WorksheetManagement
        description: Create, rename, delete, and reorder worksheets within a workbook
      - type: RangeOperations
        description: Read, write, format, and sort cell ranges using A1-style addressing
      - type: TableOperations
        description: Create tables, manage rows/columns, sort, filter, and convert to range
      - type: ChartOperations
        description: Create, update, and retrieve chart images from workbooks
      - type: NamedItems
        description: Work with named ranges and named expressions
      - type: WorkbookFunctions
        description: Execute Excel worksheet functions (PMT, SUM, VLOOKUP, etc.) via API
  - aid: spreadsheets:sheetdb
    name: SheetDB
    description: SheetDB is a service that turns any Google Sheet into a JSON REST API. Provides GET, POST, PUT, PATCH, and DELETE endpoints against spreadsheet data, supporting full CRUD operations without code. Used for prototyping, simple backends, and content management.
    humanURL: https://sheetdb.io/
    baseURL: https://sheetdb.io/api/v1
    tags:
      - Spreadsheets
      - No Code
      - REST API
      - Google Sheets
    properties:
      - type: Documentation
        url: https://docs.sheetdb.io/
      - type: Website
        url: https://sheetdb.io/
  - aid: spreadsheets:sheety
    name: Sheety
    description: Sheety converts Google Spreadsheets into RESTful JSON APIs, providing simple HTTP endpoints for reading and writing spreadsheet data. Supports GET, POST, PUT, PATCH, and DELETE operations with optional API key authentication.
    humanURL: https://sheety.co/
    baseURL: https://api.sheety.co
    tags:
      - Spreadsheets
      - No Code
      - REST API
      - Google Sheets
    properties:
      - type: Documentation
        url: https://sheety.co/docs
      - type: Website
        url: https://sheety.co/
common:
  - type: Website
    url: https://developers.google.com/workspace/sheets/api
  - type: Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/excel
  - type: OpenAPI
    url: openapi/google-sheets-openapi.yml
  - type: JSONSchema
    url: json-schema/spreadsheet-range-schema.json
  - type: JSONSchema
    url: json-schema/spreadsheet-value-schema.json
  - type: JSONStructure
    url: json-structure/spreadsheet-range-structure.json
  - type: JSONLD
    url: json-ld/spreadsheets-context.jsonld
  - type: SpectralRules
    url: rules/spreadsheets-rules.yml
  - type: Capabilities
    url: capabilities/spreadsheet-automation.yaml
  - type: Vocabulary
    url: vocabulary/spreadsheets-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
