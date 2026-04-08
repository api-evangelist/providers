---
aid: office-365
url: https://raw.githubusercontent.com/api-evangelist/office-365/refs/heads/main/apis.yml
apis:
- aid: office-365:microsoft-graph-api
  name: Microsoft Graph API
  description: The primary API for Office 365, providing access to data and intelligence in Microsoft 365, Windows 10, and Enterprise Mobility + Security.
  humanURL: https://developer.microsoft.com/en-us/graph
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Calendar
  - Graph
  - Mail
  - SharePoint
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
  - type: Change Log
    url: https://developer.microsoft.com/en-us/graph/changelog
- aid: office-365:outlook-mail-api
  name: Outlook Mail API
  description: Access email, manage folders, send mail, and manage mail settings via Microsoft Graph.
  humanURL: https://learn.microsoft.com/en-us/graph/outlook-mail-concept-overview
  baseURL: https://graph.microsoft.com/v1.0/me/messages
  tags:
  - Email
  - Mail
  - Outlook
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
- aid: office-365:outlook-calendar-api
  name: Outlook Calendar API
  description: Access and manage calendar events, meeting requests, and calendar groups.
  humanURL: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview
  baseURL: https://graph.microsoft.com/v1.0/me/calendar
  tags:
  - Calendar
  - Events
  - Meetings
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/calendar
- aid: office-365:onedrive-api
  name: OneDrive API
  description: Access and manage files stored in OneDrive and SharePoint.
  humanURL: https://learn.microsoft.com/en-us/onedrive/developer/
  baseURL: https://graph.microsoft.com/v1.0/me/drive
  tags:
  - Files
  - OneDrive
  - Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/onedrive
- aid: office-365:microsoft-teams-api
  name: Microsoft Teams API
  description: Integrate with Microsoft Teams for chat, channels, meetings, and collaboration.
  humanURL: https://learn.microsoft.com/en-us/graph/teams-concept-overview
  baseURL: https://graph.microsoft.com/v1.0/teams
  tags:
  - Chat
  - Collaboration
  - Teams
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/teams-api-overview
name: Office 365
tags:
- Cloud
- Collaboration
- Documents
- Email
- Enterprise
- Productivity
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Office 365 is a cloud-based suite of productivity and collaboration applications that integrates all Microsoft's existing online applications into a single platform including email, calendar, files, Teams, and SharePoint.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

