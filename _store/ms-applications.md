---
aid: ms-applications
name: Microsoft Applications APIs
description: Collection of Microsoft application APIs for productivity, collaboration, and enterprise services.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://developer.microsoft.com
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - name: Microsoft Graph API
    description: Unified API endpoint for accessing Microsoft 365 services including users, mail, calendar, contacts, files, and more.
    image: https://developer.microsoft.com/graph/images/graph-logo.png
    humanURL: https://developer.microsoft.com/graph
    baseURL: https://graph.microsoft.com
    tags:
      - Cloud
      - Collaboration
      - Identity
      - Productivity
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/graph/overview
      - type: OpenAPI
        url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
      - type: Authentication
        url: https://docs.microsoft.com/graph/auth/
      - type: SDKs
        url: https://docs.microsoft.com/graph/sdks/sdks-overview
      - type: Pricing
        url: https://azure.microsoft.com/pricing/details/active-directory/
  - name: Microsoft Teams API
    description: API for building apps and bots that integrate with Microsoft Teams.
    image: https://developer.microsoft.com/teams/images/teams-logo.png
    humanURL: https://developer.microsoft.com/microsoft-teams
    baseURL: https://graph.microsoft.com/v1.0/teams
    tags:
      - Chat
      - Collaboration
      - Meetings
      - Productivity
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/microsoftteams/platform/
      - type: Getting Started
        url: https://docs.microsoft.com/microsoftteams/platform/get-started/get-started-overview
      - type: Bot Framework
        url: https://docs.microsoft.com/microsoftteams/platform/bots/what-are-bots
      - type: Sample Apps
        url: https://github.com/OfficeDev/Microsoft-Teams-Samples
  - name: Outlook Mail API
    description: API for accessing and managing email messages through Microsoft Outlook.
    image: https://www.microsoft.com/outlook/favicon.ico
    humanURL: https://developer.microsoft.com/outlook
    baseURL: https://graph.microsoft.com/v1.0/me/messages
    tags:
      - Email
      - Messaging
      - Productivity
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/graph/api/resources/mail-api-overview
      - type: API Reference
        url: https://docs.microsoft.com/graph/api/resources/message
      - type: Quick Start
        url: https://developer.microsoft.com/graph/quick-start
  - name: OneDrive API
    description: API for accessing and managing files stored in OneDrive and SharePoint.
    image: https://www.microsoft.com/onedrive/favicon.ico
    humanURL: https://developer.microsoft.com/onedrive
    baseURL: https://graph.microsoft.com/v1.0/me/drive
    tags:
      - Cloud
      - Collaboration
      - Files
      - Storage
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/onedrive/developer/
      - type: API Reference
        url: https://docs.microsoft.com/graph/api/resources/onedrive
      - type: File Picker
        url: https://docs.microsoft.com/onedrive/developer/controls/file-pickers/
  - name: SharePoint API
    description: API for accessing SharePoint sites, lists, and content.
    image: https://www.microsoft.com/sharepoint/favicon.ico
    humanURL: https://developer.microsoft.com/sharepoint
    baseURL: https://graph.microsoft.com/v1.0/sites
    tags:
      - Collaboration
      - Content Management
      - Enterprise
      - Intranet
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/sharepoint/dev/
      - type: REST API Reference
        url: https://docs.microsoft.com/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
      - type: Framework
        url: https://docs.microsoft.com/sharepoint/dev/spfx/sharepoint-framework-overview
  - name: Azure Active Directory API
    description: API for identity and access management in Azure AD.
    image: https://azure.microsoft.com/favicon.ico
    humanURL: https://developer.microsoft.com/identity
    baseURL: https://graph.microsoft.com/v1.0/users
    tags:
      - Authentication
      - Authorization
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/azure/active-directory/develop/
      - type: Authentication Flows
        url: https://docs.microsoft.com/azure/active-directory/develop/authentication-flows-app-scenarios
      - type: Microsoft Identity Platform
        url: https://docs.microsoft.com/azure/active-directory/develop/v2-overview
  - name: Microsoft To Do API
    description: API for managing tasks and to-do lists.
    image: https://www.microsoft.com/microsoft-365/favicon.ico
    humanURL: https://developer.microsoft.com/graph
    baseURL: https://graph.microsoft.com/v1.0/me/todo
    tags:
      - Planning
      - Productivity
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/graph/api/resources/todo-overview
      - type: API Reference
        url: https://docs.microsoft.com/graph/api/resources/todotask
  - name: Microsoft Planner API
    description: API for creating and managing plans, tasks, and team collaboration.
    image: https://www.microsoft.com/microsoft-365/favicon.ico
    humanURL: https://developer.microsoft.com/graph
    baseURL: https://graph.microsoft.com/v1.0/planner
    tags:
      - Collaboration
      - Productivity
      - Project Management
      - Tasks
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/graph/api/resources/planner-overview
      - type: API Reference
        url: https://docs.microsoft.com/graph/api/resources/plannertask
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Cloud
  - Enterprise
  - Microsoft
  - Microsoft-365
  - Office
  - Productivity
  - Saas
include:
  - name: Microsoft Developer Network
    url: https://developer.microsoft.com
  - name: Microsoft Learn
    url: https://docs.microsoft.com
---
