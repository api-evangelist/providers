---
aid: microsoft-office-pack
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-pack/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph API
  description: Unified API endpoint for accessing Microsoft 365 services including Office applications.
  image: https://learn.microsoft.com/graph/images/microsoft-graph.png
  humanUrl: https://developer.microsoft.com/graph
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Cloud
  - Microsoft 365
  - Office
  - Productivity
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/graph/api/overview
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/graph/sdks/sdks-overview
  - type: Pricing
    url: https://www.microsoft.com/microsoft-365/enterprise/compare-office-365-plans
  contact:
  - type: Support
    url: https://developer.microsoft.com/graph/support
- name: Word API
  description: API for creating, reading, and modifying Word documents.
  humanUrl: https://learn.microsoft.com/graph/api/resources/word
  baseUrl: https://graph.microsoft.com/v1.0/me/drive/items/{id}/workbook
  tags:
  - Documents
  - Text Processing
  - Word
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/office/dev/add-ins/word/word-add-ins-programming-overview
  - type: QuickStart
    url: https://learn.microsoft.com/office/dev/add-ins/quickstarts/word-quickstart
- name: Excel API
  description: API for working with Excel workbooks, worksheets, charts, and tables.
  humanUrl: https://learn.microsoft.com/graph/api/resources/excel
  baseUrl: https://graph.microsoft.com/v1.0/me/drive/items/{id}/workbook
  tags:
  - Data Analysis
  - Excel
  - Spreadsheets
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/graph/api/resources/excel
  - type: QuickStart
    url: https://learn.microsoft.com/office/dev/add-ins/quickstarts/excel-quickstart-jquery
  - type: Samples
    url: https://github.com/OfficeDev/Office-Add-in-samples
- name: PowerPoint API
  description: API for creating and modifying PowerPoint presentations.
  humanUrl: https://learn.microsoft.com/office/dev/add-ins/powerpoint/powerpoint-add-ins
  baseUrl: https://graph.microsoft.com/v1.0/me/drive/items/{id}
  tags:
  - PowerPoint
  - Presentations
  - Slides
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/office/dev/add-ins/powerpoint/powerpoint-add-ins
  - type: QuickStart
    url: https://learn.microsoft.com/office/dev/add-ins/quickstarts/powerpoint-quickstart
- name: Outlook Mail API
  description: API for accessing and managing email messages, calendars, and contacts.
  humanUrl: https://learn.microsoft.com/graph/api/resources/mail-api-overview
  baseUrl: https://graph.microsoft.com/v1.0/me/messages
  tags:
  - Calendar
  - Contacts
  - Email
  - Outlook
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/graph/api/resources/mail-api-overview
  - type: Permissions
    url: https://learn.microsoft.com/graph/permissions-reference#mail-permissions
- name: OneDrive API
  description: API for accessing files and folders stored in OneDrive.
  humanUrl: https://learn.microsoft.com/graph/api/resources/onedrive
  baseUrl: https://graph.microsoft.com/v1.0/me/drive
  tags:
  - Cloud Storage
  - Files
  - OneDrive
  - Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/graph/api/resources/onedrive
  - type: Upload
    url: https://learn.microsoft.com/graph/api/driveitem-put-content
- name: SharePoint API
  description: API for accessing SharePoint sites, lists, and content.
  humanUrl: https://learn.microsoft.com/graph/api/resources/sharepoint
  baseUrl: https://graph.microsoft.com/v1.0/sites
  tags:
  - Collaboration
  - Content Management
  - SharePoint
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/graph/api/resources/sharepoint
name: Microsoft Office Pack
tags:
- API
type: Contract
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs for Microsoft Office productivity applications including Word, Excel, PowerPoint, Outlook, and OneDrive.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

