---
aid: microsoft-office-products
name: Microsoft Office Products
description: API catalog for Microsoft Office product suite including Word, Excel, PowerPoint, Outlook, and Teams.
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
created: '2024-01-15'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-office-products/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365 services including Office applications.
    image: https://learn.microsoft.com/en-us/graph/images/microsoft-graph.png
    humanUrl: https://learn.microsoft.com/en-us/graph/overview
    baseUrl: https://graph.microsoft.com/v1.0
    tags:
      - Cloud
      - Microsoft 365
      - Office
      - Productivity
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: Changelog
        url: https://learn.microsoft.com/en-us/graph/changelog
    contact:
      - type: Support
        url: https://developer.microsoft.com/en-us/graph/support
  - name: Word JavaScript API
    description: API for building add-ins and automating Microsoft Word.
    humanUrl: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/word-add-ins-reference-overview
    baseUrl: https://graph.microsoft.com/v1.0/me/drive/items/{id}/workbook
    tags:
      - Documents
      - Office Add-Ins
      - Word
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/word
      - type: Samples
        url: https://github.com/OfficeDev/Office-Add-in-samples
      - type: Quick Start
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart
  - name: Excel JavaScript API
    description: API for creating Excel add-ins and automating spreadsheet operations.
    humanUrl: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/excel-add-ins-reference-overview
    baseUrl: https://graph.microsoft.com/v1.0/me/drive/items/{id}/workbook
    tags:
      - Data Analysis
      - Excel
      - Office Add-Ins
      - Spreadsheets
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/excel
      - type: REST API
        url: https://learn.microsoft.com/en-us/graph/api/resources/excel
      - type: Samples
        url: https://github.com/OfficeDev/Excel-Add-in-samples
      - type: Tutorial
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/tutorials/excel-tutorial
  - name: PowerPoint JavaScript API
    description: API for developing PowerPoint add-ins and presentation automation.
    humanUrl: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/powerpoint-add-ins-reference-overview
    tags:
      - Office Add-Ins
      - PowerPoint
      - Presentations
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/powerpoint
      - type: Samples
        url: https://github.com/OfficeDev/PowerPoint-Add-in-samples
      - type: Quick Start
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/powerpoint-quickstart
  - name: Outlook JavaScript API
    description: API for building Outlook add-ins for email, calendar, and contacts.
    humanUrl: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/outlook-add-ins-reference-overview
    tags:
      - Calendar
      - Email
      - Office Add-Ins
      - Outlook
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/outlook
      - type: REST API
        url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
      - type: Samples
        url: https://github.com/OfficeDev/Outlook-Add-in-samples
      - type: Patterns
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/outlook/outlook-addin-design
  - name: Microsoft Teams API
    description: API for building apps, bots, and integrations for Microsoft Teams.
    humanUrl: https://learn.microsoft.com/en-us/microsoftteams/platform/
    baseUrl: https://graph.microsoft.com/v1.0/teams
    tags:
      - Chat
      - Collaboration
      - Meetings
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
      - type: Bot Framework
        url: https://dev.botframework.com/
      - type: App Samples
        url: https://github.com/OfficeDev/Microsoft-Teams-Samples
      - type: Toolkit
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/toolkit/teams-toolkit-fundamentals
  - name: OneDrive API
    description: API for accessing and managing files in OneDrive and SharePoint.
    humanUrl: https://learn.microsoft.com/en-us/onedrive/developer/
    baseUrl: https://graph.microsoft.com/v1.0/me/drive
    tags:
      - Files
      - OneDrive
      - SharePoint
      - Storage
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/onedrive
      - type: File Picker
        url: https://learn.microsoft.com/en-us/onedrive/developer/controls/file-pickers/
      - type: Webhooks
        url: https://learn.microsoft.com/en-us/graph/api/resources/webhooks
common:
  - type: Portal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
  - type: Terms of Service
    url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/
  - type: Blog
    url: https://devblogs.microsoft.com/microsoft365dev/
  - type: Status
    url: https://status.dev.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Cloud
  - Enterprise
  - Microsoft
  - Office
  - Productivity
  - SaaS
---
