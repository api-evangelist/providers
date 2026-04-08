---
aid: microsoft-office-applications
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-applications/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph API
  description: Unified API endpoint for accessing Microsoft 365 services including Office applications.
  image: https://docs.microsoft.com/en-us/graph/images/microsoft-graph.png
  humanURL: https://developer.microsoft.com/en-us/graph
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Graph
  - Microsoft 365
  - Office
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/microsoft-graph-openapi/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
- name: Word API
  description: API for creating, editing, and managing Word documents.
  humanURL: https://docs.microsoft.com/en-us/javascript/api/word
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Documents
  - Word
  - Word Processing
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/word/
  - type: Reference
    url: https://docs.microsoft.com/en-us/javascript/api/word
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart
- name: Excel API
  description: API for creating, editing, and managing Excel spreadsheets.
  humanURL: https://docs.microsoft.com/en-us/javascript/api/excel
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Data Analysis
  - Excel
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/excel/
  - type: Reference
    url: https://docs.microsoft.com/en-us/javascript/api/excel
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/quickstarts/excel-quickstart-jquery
- name: PowerPoint API
  description: API for creating, editing, and managing PowerPoint presentations.
  humanURL: https://docs.microsoft.com/en-us/javascript/api/powerpoint
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - PowerPoint
  - Presentations
  - Slides
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/powerpoint/
  - type: Reference
    url: https://docs.microsoft.com/en-us/javascript/api/powerpoint
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/quickstarts/powerpoint-quickstart
- name: Outlook Mail API
  description: API for accessing and managing email in Outlook.
  humanURL: https://docs.microsoft.com/en-us/graph/api/resources/mail-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Email
  - Mail
  - Outlook
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/mail-api-overview
  - type: Reference
    url: https://docs.microsoft.com/en-us/graph/api/resources/message
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/office/dev/add-ins/quickstarts/outlook-quickstart
- name: OneNote API
  description: API for creating and managing OneNote notebooks, sections, and pages.
  humanURL: https://docs.microsoft.com/en-us/graph/api/resources/onenote-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Notebooks
  - Notes
  - OneNote
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/onenote-api-overview
  - type: Reference
    url: https://docs.microsoft.com/en-us/graph/api/resources/onenote
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/graph/onenote-get-started
- name: OneDrive API
  description: API for accessing and managing files in OneDrive.
  humanURL: https://docs.microsoft.com/en-us/graph/api/resources/onedrive
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Files
  - OneDrive
  - Storage
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/onedrive/developer/
  - type: Reference
    url: https://docs.microsoft.com/en-us/graph/api/resources/onedrive
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/
- name: Teams API
  description: API for Microsoft Teams collaboration and communication.
  humanURL: https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Chat
  - Collaboration
  - Teams
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview
  - type: Reference
    url: https://docs.microsoft.com/en-us/graph/api/resources/team
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/microsoftteams/platform/
name: Microsoft Office Applications
tags:
- Documents
- Office
- Presentations
- Productivity
- Spreadsheets
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for Microsoft Office suite including Word, Excel, PowerPoint, Outlook, and other Office applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

