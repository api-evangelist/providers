---
aid: microsoft-office-suite
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-suite/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph API
  description: Unified API endpoint for accessing Microsoft 365 services including Office applications, users, and data.
  image: https://learn.microsoft.com/en-us/graph/images/microsoft-graph.png
  humanURL: https://developer.microsoft.com/en-us/graph
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Graph
  - Microsoft 365
  - Office
  - Productivity
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/overview
  - type: OpenAPI
    url: https://learn.microsoft.com/en-us/graph/api/overview
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Sandbox
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
- name: Word API (Office.js)
  description: JavaScript API for building add-ins and automating Microsoft Word.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/word-add-ins-reference-overview
  baseURL: https://officejs.org
  tags:
  - Documents
  - Office Add-Ins
  - Word
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/javascript/api/word
  - type: Quick Start
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart
  - type: Code Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
- name: Excel API (Office.js)
  description: JavaScript API for building add-ins and automating Microsoft Excel.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
  baseURL: https://officejs.org
  tags:
  - Excel
  - Office Add-Ins
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/javascript/api/excel
  - type: Quick Start
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
  - type: Code Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
- name: PowerPoint API (Office.js)
  description: JavaScript API for building add-ins and automating Microsoft PowerPoint.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/powerpoint-add-ins-reference-overview
  baseURL: https://officejs.org
  tags:
  - Office Add-Ins
  - PowerPoint
  - Presentations
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/javascript/api/powerpoint
  - type: Quick Start
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/powerpoint-quickstart
  - type: Code Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
- name: Outlook API (Office.js)
  description: JavaScript API for building add-ins and automating Microsoft Outlook.
  humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/outlook-add-ins-reference-overview
  baseURL: https://officejs.org
  tags:
  - Calendar
  - Email
  - Office Add-Ins
  - Outlook
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/javascript/api/outlook
  - type: Quick Start
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/outlook-quickstart
  - type: Code Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
- name: OneDrive API
  description: API for accessing and managing files stored in OneDrive.
  humanURL: https://learn.microsoft.com/en-us/onedrive/developer/
  baseURL: https://graph.microsoft.com/v1.0/me/drive
  tags:
  - Cloud
  - Files
  - OneDrive
  - Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/sdk
- name: SharePoint REST API
  description: API for accessing and managing SharePoint sites, lists, and documents.
  humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
  baseURL: https://{site-url}/_api/
  tags:
  - Collaboration
  - Documents
  - Lists
  - SharePoint
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
  - type: Reference
    url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index
  - type: Code Samples
    url: https://github.com/SharePoint/sp-dev-samples
- name: Microsoft Teams API
  description: API for building apps and bots integrated with Microsoft Teams.
  humanURL: https://learn.microsoft.com/en-us/microsoftteams/platform/
  baseURL: https://graph.microsoft.com/v1.0/teams
  tags:
  - Chat
  - Collaboration
  - Meetings
  - Teams
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
  - type: Bot Framework
    url: https://learn.microsoft.com/en-us/microsoftteams/platform/bots/what-are-bots
  - type: App Manifest
    url: https://learn.microsoft.com/en-us/microsoftteams/platform/resources/schema/manifest-schema
  - type: Developer Portal
    url: https://dev.teams.microsoft.com/
name: Microsoft Office Suite
tags:
- Cloud
- Collaboration
- Documents
- Microsoft 365
- Office
- Productivity
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft365.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Microsoft Office Suite applications and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

