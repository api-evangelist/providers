---
name: Microsoft Applications
description: A collection of APIs for Microsoft's suite of applications and services.
image: https://www.microsoft.com/favicon.ico
url: https://www.microsoft.com/apis
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365, Windows 10, and Enterprise Mobility + Security services.
    image: https://learn.microsoft.com/favicon.ico
    humanUrl: https://developer.microsoft.com/en-us/graph
    baseUrl: https://graph.microsoft.com
    tags:
      - Calendar
      - Files
      - Groups
      - Mail
      - Teams
      - Users
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
      - type: GraphExplorer
        url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - name: Office 365 API
    description: APIs for Office 365 services including Outlook, OneDrive, and SharePoint.
    humanUrl: https://developer.microsoft.com/en-us/office
    baseUrl: https://outlook.office.com/api
    tags:
      - Calendar
      - Contacts
      - Email
      - OneDrive
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/
      - type: GettingStarted
        url: https://developer.microsoft.com/en-us/office/getting-started
  - name: Microsoft Teams API
    description: Build apps and bots for Microsoft Teams collaboration platform.
    humanUrl: https://developer.microsoft.com/en-us/microsoft-teams
    baseUrl: https://graph.microsoft.com/v1.0/teams
    tags:
      - Bots
      - Channels
      - Chat
      - Messaging
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/microsoftteams/platform/
      - type: Samples
        url: https://github.com/OfficeDev/Microsoft-Teams-Samples
      - type: BotFramework
        url: https://dev.botframework.com/
  - name: OneDrive API
    description: Access and manage files stored in OneDrive and SharePoint.
    humanUrl: https://developer.microsoft.com/en-us/onedrive
    baseUrl: https://graph.microsoft.com/v1.0/me/drive
    tags:
      - Files
      - Sharing
      - Storage
      - Sync
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/onedrive/developer/
      - type: REST-API
        url: https://learn.microsoft.com/en-us/onedrive/developer/rest-api/
  - name: Outlook Mail API
    description: Access and manage email, calendar, and contacts in Outlook.
    humanUrl: https://developer.microsoft.com/en-us/outlook
    baseUrl: https://graph.microsoft.com/v1.0/me/messages
    tags:
      - Calendar
      - Contacts
      - Email
      - Tasks
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/outlook/rest/
  - name: SharePoint REST API
    description: Programmatic access to SharePoint sites, lists, and content.
    humanUrl: https://developer.microsoft.com/en-us/sharepoint
    baseUrl: https://[tenant].sharepoint.com/_api
    tags:
      - Collaboration
      - Documents
      - Lists
      - SharePoint
      - Sites
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
      - type: Samples
        url: https://github.com/SharePoint/sp-dev-samples
  - name: Power BI REST API
    description: Embed Power BI content and manage Power BI resources.
    humanUrl: https://powerbi.microsoft.com/en-us/developers/
    baseUrl: https://api.powerbi.com
    tags:
      - Analytics
      - Dashboards
      - Datasets
      - Embedding
      - Reports
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/power-bi/
      - type: Playground
        url: https://playground.powerbi.com/
  - name: Microsoft To Do API
    description: Manage tasks and to-do lists via Microsoft To Do.
    humanUrl: https://developer.microsoft.com/en-us/to-do
    baseUrl: https://graph.microsoft.com/v1.0/me/todo
    tags:
      - Lists
      - Productivity
      - Tasks
      - ToDo
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/todo-overview
  - name: Microsoft Planner API
    description: Create and manage plans, tasks, and team collaboration.
    humanUrl: https://developer.microsoft.com/en-us/planner
    baseUrl: https://graph.microsoft.com/v1.0/planner
    tags:
      - Planning
      - Projects
      - Tasks
      - Teams
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/planner-overview
maintainers:
  - name: Microsoft Developer Relations
    email: developer@microsoft.com
    url: https://developer.microsoft.com
tags:
  - Cloud
  - Collaboration
  - Enterprise
  - Microsoft
  - Office 365
  - Productivity
---
