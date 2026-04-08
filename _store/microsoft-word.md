---
aid: microsoft-word
url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph Word API
  description: REST API for interacting with Word documents in Microsoft 365 and OneDrive.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/word
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Cloud
  - Documents
  - Microsoft-Graph
  - Rest
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/word
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
- name: Office JavaScript API for Word
  description: JavaScript API for building Word add-ins and automating Word tasks.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/word-add-ins-reference-overview
  baseURL: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
  tags:
  - Add-Ins
  - Automation
  - Client-Side
  - Javascript
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/javascript/api/word
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart
  - type: Code Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
  - type: Reference
    url: https://learn.microsoft.com/en-us/javascript/api/word?view=word-js-preview
- name: Word Automation Services (SharePoint)
  description: Server-side document conversion and automation for SharePoint.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/word-automation-services-in-sharepoint
  tags:
  - Conversion
  - Enterprise
  - Server-Side
  - Sharepoint
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/word-automation-services-in-sharepoint
- name: Open XML SDK for Word
  description: .NET library for programmatically creating and manipulating Word documents.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://github.com/OfficeDev/Open-XML-SDK
  tags:
  - Dotnet
  - Library
  - Offline
  - Openxml
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/open-xml/word-processing
  - type: GitHub Repository
    url: https://github.com/OfficeDev/Open-XML-SDK
name: Microsoft Word
tags:
- Documents
- Office
- Productivity
- Word Processing
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Microsoft Word document creation, manipulation, and automation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

