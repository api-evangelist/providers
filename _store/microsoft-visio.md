---
aid: microsoft-visio
name: Microsoft Visio
description: APIs and resources for Microsoft Visio, a diagramming and vector graphics application that helps visualize data-connected business process flows. Provides programmatic access to diagrams, pages, shapes, data items, comments, and hyperlinks through Microsoft Graph and JavaScript APIs.
image: https://learn.microsoft.com/en-us/graph/images/visio-logo.png
url: https://raw.githubusercontent.com/api-evangelist/microsoft-visio/refs/heads/main/apis.yml
humanURL: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
tags:
  - Business Process
  - Diagramming
  - Flowcharts
  - Microsoft 365
  - Visualization
apis:
  - name: Microsoft Graph Visio API
    description: REST API for accessing and interacting with Visio files stored in SharePoint Online and OneDrive for Business through Microsoft Graph. Supports reading pages, shapes, shape data, comments, and hyperlinks.
    humanURL: https://learn.microsoft.com/en-us/graph/api/resources/visio
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Microsoft Graph
      - OneDrive
      - REST API
      - SharePoint
      - Visio Files
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/visio
      - type: OpenAPI
        url: openapi/microsoft-visio-graph-api.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/graph/api/resources/visio
      - type: JSONSchema
        url: json-schema/visio-graph-api-visio-page-schema.json
      - type: JSONSchema
        url: json-schema/visio-graph-api-visio-shape-schema.json
      - type: JSONSchema
        url: json-schema/visio-graph-api-shape-data-item-schema.json
      - type: JSONSchema
        url: json-schema/visio-graph-api-visio-comment-schema.json
      - type: JSONSchema
        url: json-schema/visio-graph-api-visio-hyperlink-schema.json
      - type: JSONStructure
        url: json-structure/visio-graph-api-visio-page-structure.json
      - type: JSON-LD
        url: json-ld/microsoft-visio-graph-api-context.jsonld
      - type: Example
        url: examples/visio-graph-api-visio-page-example.json
      - type: Example
        url: examples/visio-graph-api-visio-shape-example.json
  - name: Visio JavaScript API
    description: JavaScript API for building add-ins and extending Visio functionality in the browser with access to documents, pages, shapes, and comments.
    humanURL: https://learn.microsoft.com/en-us/javascript/api/visio
    baseURL: https://learn.microsoft.com/en-us/javascript/api/visio
    tags:
      - Add-Ins
      - Browser
      - JavaScript
      - Office Add-Ins
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/visio
      - type: APIReference
        url: https://learn.microsoft.com/en-us/javascript/api/visio?view=visio-js-1.1
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/visio/visio-add-ins-overview
      - type: CodeExamples
        url: https://github.com/OfficeDev/Office-Add-in-samples
common:
  - type: Support
    url: https://support.microsoft.com/visio
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/visio-blog/bg-p/VisioBlog
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/servicesagreement
  - type: StatusPage
    url: https://status.microsoft365.com/
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/visio/microsoft-visio-plans-and-pricing-compare-visio-options
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: SpectralRules
    url: rules/microsoft-visio-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/diagram-analysis.yaml
  - type: Vocabulary
    url: vocabulary/microsoft-visio-vocabulary.yaml
  - type: Features
    data:
      - name: Diagram Rendering
        description: Render Visio diagrams in the browser via JavaScript API.
      - name: Shape Data Access
        description: Read data items attached to diagram shapes.
      - name: Page Navigation
        description: Navigate and list pages within Visio documents.
      - name: Comment Support
        description: Read and manage comments on shapes.
      - name: Hyperlink Management
        description: Access hyperlinks associated with diagram shapes.
  - type: UseCases
    data:
      - name: Network Topology Analysis
        description: Programmatically analyze network diagrams for infrastructure review.
      - name: Business Process Review
        description: Extract and analyze business process flow data from diagrams.
      - name: Compliance Auditing
        description: Inspect diagram shapes and data for compliance validation.
  - type: Integrations
    data:
      - name: SharePoint
        description: Access Visio files stored in SharePoint document libraries.
      - name: OneDrive
        description: Work with Visio diagrams in OneDrive for Business.
      - name: Power Automate
        description: Trigger workflows based on Visio diagram changes.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
