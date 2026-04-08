---
aid: microsoft-exchange
url: https://raw.githubusercontent.com/api-evangelist/microsoft-exchange/refs/heads/main/apis.yml
apis:
- name: Microsoft Graph Mail API
  description: Access Exchange Online mailboxes through the Microsoft Graph API, providing modern REST endpoints for reading, sending, and managing email messages, drafts, attachments, and mail folders.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Email
  - Mail
  - Messaging
  - Microsoft Graph
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview
  - type: OpenAPI
    url: openapi/microsoft-exchange-graph-mail-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://developer.microsoft.com/en-us/graph/quick-start
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Change Log
    url: https://developer.microsoft.com/en-us/graph/changelog
  contact:
  - FN: Microsoft Support
    email: support@microsoft.com
    url: https://support.microsoft.com
- name: Microsoft Graph Calendar API
  description: Manage calendar events, meetings, and scheduling for Exchange Online users. Provides endpoints for creating, updating, and deleting events, managing attendees, and handling recurring meetings.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/api/resources/calendar
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Calendar
  - Events
  - Meetings
  - Microsoft Graph
  - Scheduling
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/api/resources/calendar
  - type: OpenAPI
    url: openapi/microsoft-exchange-graph-calendar-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: Getting Started
    url: https://developer.microsoft.com/en-us/graph/quick-start
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Change Log
    url: https://developer.microsoft.com/en-us/graph/changelog
- name: Microsoft Graph Contacts API
  description: Manage Outlook personal contacts and contact folders for Exchange Online users. Supports creating, reading, updating, and deleting contacts, organizing them into folders, and assigning categories.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Address Book
  - Contacts
  - Microsoft Graph
  - Outlook
  - People
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/outlook-contacts-concept-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/contact?view=graph-rest-1.0
  - type: OpenAPI
    url: openapi/microsoft-exchange-graph-contacts-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- name: Microsoft Graph People API
  description: Retrieve people most relevant to a user based on communication and collaboration patterns, business relationships, and contacts. Useful for people-picking scenarios and social intelligence features.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/people-insights-overview
  baseURL: https://graph.microsoft.com/v1.0
  tags:
  - Collaboration
  - Contacts
  - Microsoft Graph
  - People
  - Social Intelligence
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/people-insights-overview
  - type: Reference
    url: https://learn.microsoft.com/en-us/graph/api/user-list-people?view=graph-rest-1.0
  - type: OpenAPI
    url: openapi/microsoft-exchange-graph-people-openapi.yml
  - type: OpenAPI
    url: https://raw.githubusercontent.com/microsoftgraph/msgraph-metadata/master/openapi/v1.0/openapi.yaml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- name: Exchange Web Services (EWS)
  description: Legacy SOAP-based API for Exchange Server providing comprehensive access to mailbox data and operations. Planned for deprecation in Exchange Online in October 2026, with Microsoft Graph recommended for new development.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/explore-the-ews-managed-api-ews-and-web-services-in-exchange
  baseURL: https://outlook.office365.com/EWS/Exchange.asmx
  tags:
  - Exchange Server
  - Legacy
  - Mailbox
  - SOAP
  - Web Services
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/exchange/client-developer/web-service-reference/web-services-reference-for-exchange
  - type: WSDL
    url: https://outlook.office365.com/EWS/Exchange.asmx?wsdl
  - type: SDK
    url: https://github.com/officedev/ews-managed-api
  - type: Reference
    url: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/explore-the-ews-managed-api-ews-and-web-services-in-exchange
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-server-development
- name: Exchange Online PowerShell API
  description: PowerShell module for managing Exchange Online through REST-based cmdlets. Provides the complete Exchange management surface for administrative tasks including mailbox management, mail flow rules, and organization configuration.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell
  baseURL: https://outlook.office365.com/powershell-liveid/
  tags:
  - Administration
  - Automation
  - Exchange Online
  - Management
  - PowerShell
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2
  - type: Installation Guide
    url: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell-v2#install-and-maintain-the-exchange-online-powershell-module
  - type: Authentication
    url: https://learn.microsoft.com/en-us/powershell/exchange/connect-to-exchange-online-powershell
  - type: Reference
    url: https://learn.microsoft.com/en-us/powershell/exchange/exchange-online-powershell
- name: Exchange Autodiscover API
  description: Service that enables client applications to automatically configure themselves for Exchange connectivity using minimal user input. Supports SOAP and POX protocols for discovering EWS endpoint URLs and other Exchange service settings.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/autodiscover-for-exchange
  baseURL: https://outlook.office365.com/autodiscover/autodiscover.svc
  tags:
  - Autodiscover
  - Configuration
  - Exchange Server
  - Service Discovery
  - SOAP
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/autodiscover-for-exchange
  - type: Reference
    url: https://learn.microsoft.com/en-us/exchange/client-developer/web-service-reference/soap-autodiscover-web-service-reference-for-exchange
  - type: SDK
    url: https://github.com/officedev/ews-managed-api
- name: Exchange Online Admin API
  description: REST-based administrative API that provides cmdlet-style endpoints for Exchange Online management tasks previously available through EWS. Supports organization configuration, mailbox folder permissions, distribution group membership, and delegation management.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/exchange/reference/admin-api-overview
  baseURL: https://outlook.office365.com/adminapi/v2.0
  tags:
  - Administration
  - Exchange Online
  - Management
  - Permissions
  - REST
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/exchange/reference/admin-api-overview
  - type: OpenAPI
    url: openapi/microsoft-exchange-admin-api-openapi.yml
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/exchange/reference/admin-api-get-started
  - type: Authentication
    url: https://learn.microsoft.com/en-us/exchange/reference/admin-api-authentication
- name: Microsoft Graph Mailbox Import Export API
  description: APIs for discovering, importing, and exporting content from Exchange Online mailboxes in full fidelity. Enables mailbox migration scenarios and content copying as a replacement for EWS-based approaches.
  image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
  humanURL: https://learn.microsoft.com/en-us/graph/mailbox-import-export-concept-overview
  baseURL: https://graph.microsoft.com/beta
  tags:
  - Export
  - Import
  - Mailbox
  - Microsoft Graph
  - Migration
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/graph/mailbox-import-export-concept-overview
  - type: OpenAPI
    url: openapi/microsoft-exchange-graph-import-export-openapi.yml
  - type: Reference
    url: https://learn.microsoft.com/en-us/graph/api/resources/mailbox-import-export-api-overview?view=graph-rest-beta
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: SDKs
    url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
name: Microsoft Exchange
tags:
- Calendar
- Collaboration
- Contacts
- Email
- Enterprise
type: Contract
image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A comprehensive API collection for Microsoft Exchange Server and Exchange Online, providing programmatic access to email, calendars, contacts, and other mailbox resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

