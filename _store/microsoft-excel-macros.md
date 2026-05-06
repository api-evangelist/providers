---
aid: microsoft-excel-macros
name: Microsoft Excel Macros
description: A collection of APIs and resources for working with Microsoft Excel Macros, VBA automation, and Excel extensibility including the Office JavaScript API and COM automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Excel
  - Macros
  - Microsoft
  - Office
  - Spreadsheets
  - VBA
url: https://raw.githubusercontent.com/api-evangelist/microsoft-excel-macros/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-excel-macros:vba-object-model
    name: Excel VBA Object Model API
    description: Core API for interacting with Excel objects, workbooks, worksheets, ranges, and cells through VBA automation.
    humanURL: https://learn.microsoft.com/en-us/office/vba/api/overview/excel
    baseURL: https://api.example.com/excel/vba
    tags:
      - Automation
      - Excel
      - Macros
      - VBA
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/vba/api/overview/excel/object-model
      - type: Reference
        url: https://learn.microsoft.com/en-us/office/vba/api/overview/excel/object-model
  - aid: microsoft-excel-macros:office-javascript-api
    name: Office JavaScript API for Excel
    description: Modern JavaScript API for creating Excel add-ins and automating Excel through web technologies.
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
    baseURL: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
    tags:
      - Excel
      - JavaScript
      - Office Add-Ins
      - Web API
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/excel
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
  - aid: microsoft-excel-macros:com-automation
    name: Excel COM Automation API
    description: Component Object Model interface for automating Excel from external applications.
    humanURL: https://learn.microsoft.com/en-us/office/vba/api/overview/excel
    tags:
      - Automation
      - COM
      - Interop
      - Windows
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/api/microsoft.office.interop.excel
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
  - type: Status
    url: https://status.office.com/
  - type: Terms of Service
    url: https://www.microsoft.com/servicesagreement
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
  - type: Support
    url: https://support.microsoft.com/excel
  - type: GitHub Organization
    url: https://github.com/OfficeDev
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
