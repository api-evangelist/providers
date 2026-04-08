---
aid: microsoft-suite
url: https://raw.githubusercontent.com/api-evangelist/microsoft-suite/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph API
  description: Unified API endpoint for accessing Microsoft 365 services including users, groups, mail, calendars, contacts, files, and more.
  image: https://docs.microsoft.com/graph/images/microsoft-graph.png
  humanUrl: https://developer.microsoft.com/graph
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Collaboration
  - Identity
  - Microsoft-365
  - Unified-Api
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/graph/api/overview
  - type: OpenAPI
    url: https://developer.microsoft.com/graph/openapi
  - type: Authentication
    url: https://docs.microsoft.com/graph/auth/
  - type: SDKs
    url: https://docs.microsoft.com/graph/sdks/sdks-overview
  - type: Pricing
    url: https://azure.microsoft.com/pricing/details/active-directory/
- name: Microsoft Teams API
  description: API for integrating with Microsoft Teams to create bots, tabs, messaging extensions, and connectors.
  humanUrl: https://developer.microsoft.com/microsoft-teams
  baseUrl: https://graph.microsoft.com/v1.0/teams
  tags:
  - Bots
  - Chat
  - Collaboration
  - Meetings
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/microsoftteams/platform/
  - type: Getting Started
    url: https://docs.microsoft.com/microsoftteams/platform/get-started/get-started-overview
  - type: Webhooks
    url: https://docs.microsoft.com/microsoftteams/platform/webhooks-and-connectors/what-are-webhooks-and-connectors
- name: OneDrive API
  description: REST API for accessing files stored in OneDrive and SharePoint document libraries.
  humanUrl: https://developer.microsoft.com/onedrive
  baseUrl: https://graph.microsoft.com/v1.0/me/drive
  tags:
  - Cloud-Storage
  - Files
  - Storage
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/onedrive/developer/
  - type: REST API Reference
    url: https://docs.microsoft.com/onedrive/developer/rest-api/
  - type: SDKs
    url: https://docs.microsoft.com/onedrive/developer/sdks/
- name: Outlook Mail API
  description: Access to Outlook mail, calendar, contacts, and tasks via Microsoft Graph.
  humanUrl: https://developer.microsoft.com/outlook
  baseUrl: https://graph.microsoft.com/v1.0/me/messages
  tags:
  - Calendar
  - Contacts
  - Email
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/graph/outlook-mail-concept-overview
  - type: REST API Reference
    url: https://docs.microsoft.com/graph/api/resources/mail-api-overview
- name: SharePoint API
  description: Access SharePoint sites, lists, and content via REST and Microsoft Graph APIs.
  humanUrl: https://developer.microsoft.com/sharepoint
  baseUrl: https://graph.microsoft.com/v1.0/sites
  tags:
  - Collaboration
  - Content-Management
  - Intranet
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/sharepoint/dev/
  - type: REST API
    url: https://docs.microsoft.com/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
  - type: Graph API
    url: https://docs.microsoft.com/graph/api/resources/sharepoint
- name: Azure Active Directory API
  description: Identity and access management API for authentication and authorization.
  humanUrl: https://developer.microsoft.com/identity
  baseUrl: https://graph.microsoft.com/v1.0/users
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
- name: Power BI API
  description: Embed Power BI reports and dashboards, and manage Power BI resources programmatically.
  humanUrl: https://developer.microsoft.com/power-bi
  baseUrl: https://api.powerbi.com/v1.0
  tags:
  - Analytics
  - Business-Intelligence
  - Visualization
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/power-bi/developer/
  - type: REST API Reference
    url: https://docs.microsoft.com/rest/api/power-bi/
  - type: Embedding
    url: https://docs.microsoft.com/power-bi/developer/embedded/embedding
name: Microsoft Suite
tags:
- Cloud
- Enterprise
- Productivity
- SaaS
type: Contract
image: https://www.microsoft.com/favicon.ico
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Microsoft's productivity and cloud services suite.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

