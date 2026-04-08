---
aid: sharepoint
url: https://raw.githubusercontent.com/api-evangelist/sharepoint/refs/heads/main/apis.yml
apis:
- name: SharePoint REST API
  description: The SharePoint REST API enables developers to interact remotely with SharePoint data using any technology that supports REST web requests.
  image: https://example.com/sharepoint-rest-api.png
  humanUrl: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
  baseUrl: https://{site_url}/_api
  tags:
  - Documents
  - Lists
  - REST
  - Sites
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
  - type: OpenAPI
    url: https://example.com/sharepoint-rest-openapi.json
  - type: Authentication
    url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/authorization-and-authentication-of-sharepoint-add-ins
- name: Microsoft Graph API (SharePoint)
  description: Access SharePoint sites, lists, and documents through the Microsoft Graph unified API endpoint.
  image: https://example.com/microsoft-graph.png
  humanUrl: https://docs.microsoft.com/en-us/graph/api/resources/sharepoint
  baseUrl: https://graph.microsoft.com/v1.0
  tags:
  - Drive
  - Graph
  - Lists
  - Modern
  - Sites
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/graph/api/resources/sharepoint
  - type: OpenAPI
    url: https://example.com/graph-sharepoint-openapi.json
  - type: SDK
    url: https://docs.microsoft.com/en-us/graph/sdks/sdks-overview
  - type: Authentication
    url: https://docs.microsoft.com/en-us/graph/auth/
- name: SharePoint CSOM (Client-Side Object Model)
  description: Client-side object model for SharePoint that provides access to SharePoint objects through .NET managed or JavaScript libraries.
  image: https://example.com/sharepoint-csom.png
  humanUrl: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-client-library-code
  baseUrl: N/A
  tags:
  - .NET
  - Client Library
  - CSOM
  - JavaScript
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-client-library-code
  - type: NuGet Package
    url: https://www.nuget.org/packages/Microsoft.SharePointOnline.CSOM/
  - type: JavaScript Reference
    url: https://docs.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-javascript-library-code-in-sharepoint
- name: SharePoint Webhooks API
  description: SharePoint webhooks provide a way to get notified about changes to SharePoint lists and document libraries.
  image: https://example.com/sharepoint-webhooks.png
  humanUrl: https://docs.microsoft.com/en-us/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks
  baseUrl: https://{site_url}/_api/web/lists('{list-id}')/subscriptions
  tags:
  - Events
  - Notifications
  - Real-Time
  - Webhooks
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks
  - type: Getting Started
    url: https://docs.microsoft.com/en-us/sharepoint/dev/apis/webhooks/get-started-webhooks
name: Microsoft SharePoint
tags:
- Collaboration
- Document Management
- Enterprise Content Management
- Intranet
- Microsoft
type: Contract
image: https://example.com/sharepoint-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft SharePoint is a web-based collaborative platform that integrates with Microsoft Office. It provides enterprise content management, document management, and collaboration capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

