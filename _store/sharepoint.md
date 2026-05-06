---
name: Microsoft SharePoint
description: Microsoft SharePoint is a web-based collaborative platform that integrates with Microsoft Office. It provides enterprise content management, document management, and collaboration capabilities.
image: https://example.com/sharepoint-logo.png
tags:
  - Collaboration
  - Document Management
  - Enterprise Content Management
  - Intranet
  - Microsoft
created: '2024'
modified: '2026-04-17'
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
    aid: sharepoint:rest-api
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
    aid: sharepoint:graph-api-sharepoint
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
    aid: sharepoint:csom-client-side-object-model
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
      - type: GettingStarted
        url: https://docs.microsoft.com/en-us/sharepoint/dev/apis/webhooks/get-started-webhooks
    aid: sharepoint:webhooks-api
common:
  - type: Developer Portal
    url: https://developer.microsoft.com/en-us/sharepoint
  - type: Code Samples
    url: https://pnp.github.io/
  - type: Community
    url: https://techcommunity.microsoft.com/t5/sharepoint/ct-p/SharePoint
  - type: Support
    url: https://support.microsoft.com/en-us/sharepoint
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/sharepoint/compare-sharepoint-plans
  - type: StatusPage
    url: https://status.cloud.microsoft/
  - type: Features
    data:
      - name: Sites and Webs
        description: Create, read, update, and delete SharePoint sites and subsites.
      - name: Lists and Libraries
        description: Full CRUD operations on lists, document libraries, and list items.
      - name: Document Management
        description: Upload, download, check in/out, and manage documents and file versions.
      - name: Folders and Files
        description: Create folder hierarchies and manage files within document libraries.
      - name: Permissions and Security
        description: Manage site, list, and item-level permissions with role assignments.
      - name: Search
        description: Full-text search across sites, documents, and content using the Search REST API.
      - name: User Profiles
        description: Access user profile properties, people search, and organizational data.
      - name: Content Types
        description: Manage content types, site columns, and metadata schemas.
      - name: Webhooks
        description: Subscribe to change notifications for lists and libraries via webhooks.
      - name: Microsoft Graph Integration
        description: Access SharePoint data through Microsoft Graph API for unified Microsoft 365 integration.
      - name: Batch Requests
        description: Combine multiple REST operations into a single batch request.
      - name: OData Query Support
        description: Filter, select, expand, and order data using OData query operators.
  - type: UseCases
    data:
      - name: Document Automation
        description: Automate document upload, metadata tagging, and approval workflows.
      - name: Intranet Content Management
        description: Programmatically manage site pages, news posts, and navigation.
      - name: Data Integration
        description: Sync SharePoint list data with external databases and applications.
      - name: Migration
        description: Migrate content between SharePoint sites or from file shares to SharePoint.
      - name: Custom Applications
        description: Build SPFx web parts and extensions with SharePoint Framework.
      - name: Compliance and Governance
        description: Manage retention policies, sensitivity labels, and audit logs.
      - name: Search Integration
        description: Build custom search experiences with facets, refiners, and result types.
      - name: Power Automate Flows
        description: Trigger and manage automated workflows based on SharePoint events.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Native integration with Teams, OneDrive, Outlook, and other Microsoft 365 apps.
      - name: Microsoft Graph
        description: Unified API access to SharePoint alongside all Microsoft 365 services.
      - name: Power Platform
        description: Power Apps, Power Automate, and Power BI integration for low-code solutions.
      - name: Azure
        description: Azure AD for authentication, Azure Functions for serverless processing.
      - name: Teams
        description: SharePoint powers file storage and document collaboration in Microsoft Teams.
  - type: Solutions
    data:
      - name: SharePoint Online
        description: Cloud-hosted SharePoint as part of Microsoft 365 with REST and Graph APIs.
      - name: SharePoint Server
        description: On-premises SharePoint with REST, CSOM, and server-side object model.
      - name: SharePoint Framework (SPFx)
        description: Modern client-side development framework for building web parts and extensions.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
aid: sharepoint
type: Index
specificationVersion: '0.19'
---
