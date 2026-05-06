---
aid: microsoft-excel
name: Microsoft Excel
description: APIs for automating, integrating, and extending Microsoft Excel functionality including workbook management, data manipulation, charting, and formula execution through Microsoft Graph REST APIs.
image: https://learn.microsoft.com/en-us/graph/images/excel-logo.png
url: https://raw.githubusercontent.com/api-evangelist/microsoft-excel/refs/heads/main/apis.yml
humanURL: https://www.microsoft.com/excel
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
tags:
  - Automation
  - Data Analysis
  - Microsoft
  - Microsoft 365
  - Office
  - Spreadsheets
apis:
  - name: Microsoft Graph Excel API
    description: REST API for accessing and manipulating Excel workbooks stored in OneDrive for Business, SharePoint sites, or Group drives through Microsoft Graph. Supports worksheet, table, chart, range, named item, and function operations.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/excel
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Cloud
      - Microsoft Graph
      - OneDrive
      - REST API
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: OpenAPI
        url: openapi/microsoft-excel-graph-api.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: SDK
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: JSONSchema
        url: json-schema/excel-graph-api-worksheet-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-table-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-table-row-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-table-column-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-chart-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-range-schema.json
      - type: JSONSchema
        url: json-schema/excel-graph-api-named-item-schema.json
      - type: JSONStructure
        url: json-structure/excel-graph-api-worksheet-structure.json
      - type: JSON-LD
        url: json-ld/microsoft-excel-graph-api-context.jsonld
      - type: Example
        url: examples/excel-graph-api-worksheet-example.json
      - type: Example
        url: examples/excel-graph-api-table-example.json
      - type: Example
        url: examples/excel-graph-api-range-example.json
  - name: Excel JavaScript API
    description: Office Add-ins API for building custom functionality within Excel using JavaScript and TypeScript.
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
    baseURL: https://excel.office.com
    tags:
      - Client-Side
      - JavaScript
      - Office Add-Ins
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/excel
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
  - name: Office Scripts API
    description: TypeScript-based automation for Excel on the web, enabling Power Automate integration for business process automation.
    humanURL: https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
    baseURL: https://excel.office.com
    tags:
      - Automation
      - Excel Online
      - Power Automate
      - TypeScript
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/scripts/develop/scripting-fundamentals
      - type: CodeExamples
        url: https://learn.microsoft.com/en-us/office/dev/scripts/resources/samples/samples-overview
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/office/dev/scripts/tutorials/excel-tutorial
common:
  - type: DeveloperPortal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: Support
    url: https://support.microsoft.com/excel
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/excel
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/excel-blog/bg-p/ExcelBlog
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: SpectralRules
    url: rules/microsoft-excel-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/spreadsheet-automation.yaml
  - type: Vocabulary
    url: vocabulary/microsoft-excel-vocabulary.yaml
  - type: Features
    data:
      - name: Workbook Sessions
        description: Persistent and non-persistent sessions for efficient API operations.
      - name: Cell Range Operations
        description: Read, write, and format individual cells or ranges of cells.
      - name: Table Management
        description: Create, update, sort, and filter structured tables.
      - name: Chart Generation
        description: Create and manage charts with customizable source data.
      - name: Workbook Functions
        description: Invoke Excel functions programmatically via the API.
      - name: Named Ranges
        description: Define and manage named ranges for reusable cell references.
  - type: UseCases
    data:
      - name: Automated Reporting
        description: Generate and update Excel reports from external data sources.
      - name: Data Entry Automation
        description: Programmatically insert and update data in spreadsheets.
      - name: Financial Modeling
        description: Use Excel functions API for financial calculations.
      - name: Dashboard Generation
        description: Create charts and visualizations from data.
  - type: Integrations
    data:
      - name: Microsoft Power Automate
        description: Automate Excel workflows using Power Automate connectors.
      - name: SharePoint
        description: Access and modify Excel files stored in SharePoint sites.
      - name: OneDrive
        description: Work with Excel workbooks stored in OneDrive for Business.
      - name: Microsoft Teams
        description: Share and collaborate on Excel workbooks within Teams.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
