---
aid: powerpoint
name: PowerPoint
description: Microsoft PowerPoint provides programmatic access through the Microsoft Graph API and the Office JavaScript API for creating, reading, and manipulating PowerPoint presentations. PowerPoint files stored in OneDrive and SharePoint are accessible as drive items via Microsoft Graph, while the Office JavaScript API enables in-document automation for Office Add-ins.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Microsoft Office
  - Microsoft 365
  - Presentations
  - Productivity
  - Documents
url: https://raw.githubusercontent.com/api-evangelist/powerpoint/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: powerpoint:powerpoint-graph-api
    name: PowerPoint via Microsoft Graph
    description: Microsoft Graph exposes PowerPoint presentation files (.pptx) stored in OneDrive and SharePoint as drive items, enabling upload, download, sharing, and metadata operations against presentations programmatically.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/driveitem
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Microsoft Graph
      - Files
      - Presentations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/driveitem
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
  - aid: powerpoint:powerpoint-javascript-api
    name: Office JavaScript API for PowerPoint
    description: Office JavaScript API namespace for building PowerPoint Add-ins that read, write, and manipulate slides, shapes, text, and tables inside the running PowerPoint application.
    humanURL: https://learn.microsoft.com/en-us/javascript/api/powerpoint
    tags:
      - Office Add-ins
      - JavaScript
      - Presentations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/powerpoint
      - type: SDK
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/powerpoint-quickstart
common:
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/powerpoint
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/overview
  - type: Developer
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
