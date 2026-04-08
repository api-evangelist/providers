---
aid: microsoft-excel-advanced
url: https://raw.githubusercontent.com/api-evangelist/microsoft-excel-advanced/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph Excel API
  description: REST API for reading and writing Excel workbook data through Microsoft Graph.
  image: https://learn.microsoft.com/graph/images/graph-logo.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/excel
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Cloud
  - REST
  - Workbooks
  - Worksheets
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/excel
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: QuickStart
    url: https://learn.microsoft.com/en-us/graph/api/resources/excel#get-started
  contact:
  - FN: Microsoft Graph Support
    email: graphsdksupport@microsoft.com
- name: Office Scripts API
  description: TypeScript-based automation API for Excel on the web and desktop.
  humanURL: https://learn.microsoft.com/en-us/office/dev/scripts/
  baseURL: https://script.office.com
  tags:
  - Automation
  - Power-Automate
  - Scripting
  - Typescript
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
  - type: Samples
    url: https://learn.microsoft.com/en-us/office/dev/scripts/resources/samples/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/javascript/api/office-scripts/overview
  - type: Tutorials
    url: https://learn.microsoft.com/en-us/office/dev/scripts/tutorials/excel-tutorial
- name: Excel JavaScript API
  description: JavaScript API for building Excel add-ins and extensions.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
  baseURL: https://appsforoffice.microsoft.com
  tags:
  - Add-Ins
  - Extensions
  - Javascript
  - Office-Js
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/excel/
  - type: API Reference
    url: https://learn.microsoft.com/en-us/javascript/api/excel
  - type: Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
  - type: Quick Start
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
  - type: CDN
    url: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
- name: Excel Custom Functions API
  description: API for creating custom functions in Excel using JavaScript.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/excel/custom-functions-overview
  tags:
  - Calculations
  - Custom-Functions
  - Formulas
  - Udf
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/excel/custom-functions-overview
  - type: Tutorial
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/tutorials/excel-tutorial-create-custom-functions
  - type: Best Practices
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/excel/custom-functions-best-practices
- name: Excel REST API (OneDrive)
  description: REST API for accessing Excel files stored in OneDrive and SharePoint.
  humanURL: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
  baseURL: https://graph.microsoft.com/v1.0/me/drive
  tags:
  - Cloud-Storage
  - Onedrive
  - REST
  - Sharepoint
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/api/driveitem_get
  - type: API Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/driveitem
- name: Power Automate Excel Connector
  description: Pre-built connector for automating Excel workflows in Power Automate.
  humanURL: https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/
  tags:
  - Connector
  - Low-Code
  - Power-Automate
  - Workflow
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/
  - type: Actions Reference
    url: https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/#actions
  - type: Triggers Reference
    url: https://learn.microsoft.com/en-us/connectors/excelonlinebusiness/#triggers
name: Microsoft Excel (Advanced)
tags:
- Automation
- Business Intelligence
- Data Analysis
- Office
- Spreadsheets
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/excel
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Advanced automation and integration APIs for Microsoft Excel, enabling programmatic access to spreadsheet data, formulas, charts, and automation capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

