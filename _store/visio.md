---
aid: visio
name: Microsoft Visio API
description: Microsoft Visio provides APIs for creating, editing, and managing Visio diagrams and drawings. The Visio JavaScript API enables developers to build Office Add-ins that interact with Visio diagrams embedded in SharePoint Online pages, accessing document elements such as pages, shapes, hyperlinks, comments, and shape data. Visio APIs support programmatic diagram manipulation, visual overlay creation, mouse event handling, and data visualization workflows.
image: https://www.microsoft.com/en-us/microsoft-365/visio/visio-logo.png
type: Index
tags:
  - Business Process
  - Collaboration
  - Diagrams
  - Enterprise
  - Flowcharts
  - Microsoft 365
  - Visualization
url: https://raw.githubusercontent.com/api-evangelist/visio/refs/heads/main/apis.yml
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: visio:visio-javascript-api
    name: Visio JavaScript API
    description: The Visio JavaScript API enables building Office Add-ins that interact with Visio diagrams embedded in classic SharePoint Online pages. The API provides access to document elements including pages, shapes, hyperlinks, comments, shape data items, and shape views. Developers can create visual markup overlays, register mouse event handlers, read shape text and shape data, and control application toolbar visibility. The API uses a request context and proxy object pattern with batch execution via Visio.run() and context.sync().
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/visio/visio-overview
    baseURL: https://appsforoffice.microsoft.com/embedded/1.0
    tags:
      - Add-Ins
      - Client-Side
      - Diagrams
      - JavaScript
      - Office
      - SharePoint
      - Web
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/visio/visio-overview
      - type: Reference
        url: https://learn.microsoft.com/en-us/javascript/api/visio
      - type: Getting Started
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/visio-quickstart
      - type: Samples
        url: https://github.com/OfficeDev/Office-Add-in-samples
      - type: OpenAPI
        url: openapi/visio-javascript-openapi.yml
    contact:
      - FN: Microsoft Office Dev
        email: officedevfeedback@microsoft.com
        url: https://developer.microsoft.com/office
  - aid: visio:microsoft-graph-visio-api
    name: Microsoft Graph Visio API
    description: Access and manipulate Visio files stored in OneDrive and SharePoint through Microsoft Graph. While direct Visio-specific REST endpoints are limited, Microsoft Graph provides file management capabilities for Visio documents through the DriveItem resource, enabling upload, download, and metadata operations on .vsdx and .vsd files stored in SharePoint and OneDrive.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/visio
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Cloud
      - Collaboration
      - Diagrams
      - Enterprise
      - Microsoft Graph
      - OneDrive
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/visio
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
    contact:
      - FN: Microsoft Support
        email: support@microsoft.com
        url: https://support.microsoft.com
common:
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Developer Portal
    url: https://developer.microsoft.com/en-us/microsoft-365
  - type: Status Page
    url: https://status.office.com
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
  - type: Blog
    url: https://devblogs.microsoft.com/microsoft365dev/
  - type: Change Log
    url: https://learn.microsoft.com/en-us/javascript/api/overview/visio/release-notes
  - type: OpenAPI
    url: openapi/visio-javascript-openapi.yml
  - type: JSONSchema
    url: json-schema/visio-shape-schema.json
  - type: JSONSchema
    url: json-schema/visio-page-schema.json
  - type: JSONStructure
    url: json-structure/visio-shape-structure.json
  - type: JSONLD
    url: json-ld/visio-context.jsonld
  - type: Vocabulary
    url: vocabulary/visio-vocabulary.yml
  - type: SpectralRules
    url: rules/visio-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
