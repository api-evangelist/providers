---
aid: microsoft-sharepoint
name: Microsoft SharePoint
description: Microsoft SharePoint is a web-based collaboration platform that provides document management, content management, and team collaboration capabilities. It offers REST APIs, Microsoft Graph integration, and the SharePoint Framework for customization and extension.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collaboration
  - Content Management
  - Microsoft
  - Microsoft 365
  - SharePoint
url: https://raw.githubusercontent.com/api-evangelist/microsoft-sharepoint/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-sharepoint:rest-api
    name: SharePoint REST API
    tags:
      - Collaboration
      - Content Management
      - SharePoint
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{tenant}.sharepoint.com/_api/
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
    properties:
      - url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
        type: Documentation
      - url: https://learn.microsoft.com/en-us/sharepoint/dev/apis/sharepoint-rest-graph
        type: Reference
    description: The SharePoint REST API provides direct access to SharePoint sites, lists, libraries, items, and other resources using OData endpoints. Developers can perform CRUD operations on SharePoint content, manage site structures, work with content types, and interact with search and taxonomy services.
  - aid: microsoft-sharepoint:graph-sites-api
    name: Microsoft Graph SharePoint Sites API
    tags:
      - Microsoft Graph
      - SharePoint
      - Sites
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://graph.microsoft.com/v1.0/
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint
    properties:
      - url: https://learn.microsoft.com/en-us/graph/api/resources/sharepoint
        type: Documentation
    description: The Microsoft Graph SharePoint Sites API provides access to SharePoint sites, lists, and document libraries through the unified Microsoft Graph endpoint. It enables developers to manage site content, list items, drive items, and site permissions using a consistent REST interface alongside other Microsoft 365 services.
  - aid: microsoft-sharepoint:webhooks-api
    name: SharePoint Webhooks API
    tags:
      - Events
      - SharePoint
      - Webhooks
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{tenant}.sharepoint.com/_api/
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks
    properties:
      - url: https://learn.microsoft.com/en-us/sharepoint/dev/apis/webhooks/overview-sharepoint-webhooks
        type: Documentation
    description: The SharePoint Webhooks API enables applications to subscribe to change notifications on SharePoint lists and libraries. When items are created, updated, or deleted, SharePoint sends notifications to registered webhook endpoints, enabling real-time event-driven integrations without polling.
  - aid: microsoft-sharepoint:search-api
    name: SharePoint Search REST API
    tags:
      - Content Discovery
      - Search
      - SharePoint
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://{tenant}.sharepoint.com/_api/search/
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview
    properties:
      - url: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/sharepoint-search-rest-api-overview
        type: Documentation
    description: The SharePoint Search REST API provides full-text search capabilities across SharePoint content including sites, lists, libraries, and documents. It supports keyword query language, query refinement, result sorting, and content source targeting for comprehensive enterprise search scenarios.
  - aid: microsoft-sharepoint:framework
    name: SharePoint Framework (SPFx)
    tags:
      - Extensions
      - Framework
      - SharePoint
      - Web Parts
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview
    properties:
      - url: https://learn.microsoft.com/en-us/sharepoint/dev/spfx/sharepoint-framework-overview
        type: Documentation
    description: The SharePoint Framework (SPFx) is a development model for building client-side web parts, extensions, and adaptive card extensions for SharePoint and Microsoft Teams. It uses modern web technologies including TypeScript, React, and Node.js to create customizations that run in the context of SharePoint pages.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://www.microsoft.com/en-us/microsoft-365/sharepoint/collaboration
  - type: Documentation
    url: https://learn.microsoft.com/en-us/sharepoint/dev/
  - type: Developer Portal
    url: https://developer.microsoft.com/en-us/sharepoint
  - type: Authentication
    url: https://learn.microsoft.com/en-us/sharepoint/dev/solution-guidance/security-apponly-azureacs
  - type: SDKs
    url: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/complete-basic-operations-using-sharepoint-rest-endpoints
  - type: GitHub Organization
    url: https://github.com/SharePoint
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
