---
aid: excel-macros
name: Excel Macros
description: Excel Macros refer to automated sequences of actions in Microsoft Excel, primarily written using VBA (Visual Basic for Applications). Excel also supports Office Scripts (TypeScript) for cloud-based automation and the Excel JavaScript API for building Office Add-ins that run on the web, Windows, Mac, and iPad. These automation capabilities allow users to streamline repetitive tasks, manipulate workbooks, and extend Excel functionality.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Excel
  - Macros
  - Microsoft Office
  - VBA
  - Office Scripts
  - JavaScript
url: https://docs.microsoft.com/en-us/office/vba/api/overview/excel
created: '2025-01-20'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: excel-macros:excel-vba-api
    name: Excel VBA Object Model API
    description: Core VBA API for interacting with Excel workbooks, worksheets, ranges, and other Excel objects through Visual Basic for Applications.
    humanURL: https://docs.microsoft.com/en-us/office/vba/api/overview/excel
    tags:
      - Object Model
      - VBA
      - Workbooks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/office/vba/api/overview/excel
      - type: Reference
        url: https://learn.microsoft.com/en-us/office/vba/api/overview/excel/object-model
  - aid: excel-macros:office-scripts-api
    name: Office Scripts API
    description: Modern TypeScript-based API for automating Excel tasks on the web and desktop, the cloud-first successor to VBA for Excel scenarios.
    humanURL: https://learn.microsoft.com/en-us/office/dev/scripts/
    tags:
      - Office Scripts
      - TypeScript
      - Automation
      - Cloud
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/scripts/overview/excel
      - type: Reference
        url: https://learn.microsoft.com/en-us/javascript/api/office-scripts/excelscript
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/office/dev/scripts/tutorials/excel-tutorial
  - aid: excel-macros:excel-javascript-api
    name: Excel JavaScript API
    description: JavaScript API for building Excel add-ins and extending Excel functionality in web and desktop environments via Office.js.
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
    tags:
      - Add-Ins
      - JavaScript
      - Web Development
      - Office.js
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/excel/
      - type: Reference
        url: https://learn.microsoft.com/en-us/javascript/api/excel
      - type: Quickstart
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
common:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/office/vba/api/overview/excel
  - type: Portal
    url: https://developer.microsoft.com/office
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: CommunityForum
    url: https://techcommunity.microsoft.com/t5/excel/ct-p/Excel_Cat
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
