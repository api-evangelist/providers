---
aid: microsoft-office
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office/refs/heads/main/apis.yml
apis:
- aid: microsoft-office:microsoft-graph-api
  name: Microsoft Graph API
  description: Unified API endpoint for accessing Microsoft 365 services including Office applications, OneDrive, Outlook, and more.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://developer.microsoft.com/en-us/graph
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Microsoft Graph
  - Office 365
  - Unified API
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/active-directory/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- aid: microsoft-office:word-api
  name: Word API
  description: API for interacting with Microsoft Word documents, including reading, writing, and formatting content.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/javascript/api/word
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Documents
  - Word
  - Word Processing
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/word-add-ins-reference-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/javascript/api/word
- aid: microsoft-office:excel-api
  name: Excel API
  description: API for working with Excel workbooks, worksheets, ranges, charts, and tables.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/javascript/api/excel
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Data Analysis
  - Excel
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/javascript/api/excel
- aid: microsoft-office:powerpoint-api
  name: PowerPoint API
  description: API for creating and manipulating PowerPoint presentations, slides, and content.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/javascript/api/powerpoint
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - PowerPoint
  - Presentations
  - Slides
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/powerpoint-add-ins-reference-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/javascript/api/powerpoint
- aid: microsoft-office:outlook-mail-api
  name: Outlook Mail API
  description: API for accessing and managing email, calendar, contacts, and tasks in Outlook.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Calendar
  - Contacts
  - Email
  - Outlook
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/graph/tutorials
- aid: microsoft-office:onedrive-api
  name: OneDrive API
  description: API for accessing files and folders stored in OneDrive and SharePoint.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/onedrive
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Cloud Storage
  - Files
  - OneDrive
  - Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/onedrive
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/onedrive/developer/
- aid: microsoft-office:teams-api
  name: Teams API
  description: API for integrating with Microsoft Teams, including messaging, channels, and collaboration features.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Chat
  - Collaboration
  - Meetings
  - Teams
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
name: Microsoft Office
tags:
- Collaboration
- Documents
- Microsoft
- Office
- Productivity
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for Microsoft Office applications and services, providing programmatic access to Word, Excel, PowerPoint, Outlook, OneDrive, and Teams through Microsoft Graph and Office JavaScript APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

