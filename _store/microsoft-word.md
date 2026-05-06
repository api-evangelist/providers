---
aid: microsoft-word
name: Microsoft Word
description: APIs for Microsoft Word document creation, manipulation, and automation across Microsoft 365 cloud services, Office Add-ins, SharePoint, and Open XML document processing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Documents
  - Microsoft 365
  - Office
  - Productivity
  - Word Processing
created: '2024'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - name: Microsoft Graph Word API
    description: REST API for interacting with Word documents in Microsoft 365 and OneDrive via the Microsoft Graph unified endpoint. Provides operations for file management, content access, sharing, permissions, and document metadata.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
    baseURL: https://graph.microsoft.com/v1.0
    tags:
      - Cloud
      - Documents
      - Microsoft Graph
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
      - type: OpenAPI
        url: openapi/microsoft-word-graph-api.yaml
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0
      - type: SDK
        url: https://www.nuget.org/packages/Microsoft.Graph
        title: C# SDK
      - type: SDK
        url: https://pypi.org/project/msgraph-sdk/
        title: Python SDK
      - type: SDK
        url: https://www.npmjs.com/package/@microsoft/microsoft-graph-client
        title: JavaScript SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-java
        title: Java SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-go
        title: Go SDK
      - type: SDK
        url: https://github.com/microsoftgraph/msgraph-sdk-php
        title: PHP SDK
      - type: JSONSchema
        url: json-schema/graph-api-drive-item-schema.json
        title: DriveItem Schema
      - type: JSONSchema
        url: json-schema/graph-api-permission-schema.json
        title: Permission Schema
      - type: JSONStructure
        url: json-structure/graph-api-drive-item-structure.json
        title: DriveItem Structure
      - type: JSONStructure
        url: json-structure/graph-api-permission-structure.json
        title: Permission Structure
      - type: JSONLD
        url: json-ld/microsoft-word-graph-api-context.jsonld
      - type: Example
        url: examples/graph-api-drive-item-example.json
        title: DriveItem Example
      - type: Example
        url: examples/graph-api-permission-example.json
        title: Permission Example
  - name: Office JavaScript API for Word
    description: JavaScript API for building Word add-ins and automating Word tasks. Provides strongly-typed objects for document manipulation, content controls, tables, formatting, comments, collaboration, and shapes.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/dev/add-ins/reference/overview/word-add-ins-reference-overview
    baseURL: https://appsforoffice.microsoft.com/lib/1/hosted/office.js
    tags:
      - Add-Ins
      - Automation
      - Client-Side
      - JavaScript
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/javascript/api/word
      - type: OpenAPI
        url: openapi/microsoft-word-javascript-api.yaml
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/quickstarts/word-quickstart
      - type: CodeExamples
        url: https://github.com/OfficeDev/Office-Add-in-samples
      - type: APIReference
        url: https://learn.microsoft.com/en-us/javascript/api/word?view=word-js-preview
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/office/dev/add-ins/tutorials/word-tutorial
      - type: JSONSchema
        url: json-schema/javascript-api-paragraph-schema.json
        title: Paragraph Schema
      - type: JSONSchema
        url: json-schema/javascript-api-content-control-schema.json
        title: ContentControl Schema
      - type: JSONSchema
        url: json-schema/javascript-api-table-schema.json
        title: Table Schema
      - type: JSONSchema
        url: json-schema/javascript-api-comment-schema.json
        title: Comment Schema
      - type: JSONStructure
        url: json-structure/javascript-api-paragraph-structure.json
        title: Paragraph Structure
      - type: JSONStructure
        url: json-structure/javascript-api-content-control-structure.json
        title: ContentControl Structure
      - type: JSONStructure
        url: json-structure/javascript-api-table-structure.json
        title: Table Structure
      - type: JSONStructure
        url: json-structure/javascript-api-comment-structure.json
        title: Comment Structure
      - type: JSONLD
        url: json-ld/microsoft-word-javascript-api-context.jsonld
      - type: Example
        url: examples/javascript-api-paragraph-example.json
        title: Paragraph Example
      - type: Example
        url: examples/javascript-api-content-control-example.json
        title: ContentControl Example
      - type: Example
        url: examples/javascript-api-table-example.json
        title: Table Example
      - type: Example
        url: examples/javascript-api-comment-example.json
        title: Comment Example
  - name: Word Automation Services (SharePoint)
    description: Server-side document conversion and automation service for SharePoint. Supports batch conversion of Word documents to PDF, XPS, and other formats without user interaction.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/word-automation-services-in-sharepoint
    tags:
      - Conversion
      - Enterprise
      - Server-Side
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/sharepoint/dev/general-development/word-automation-services-in-sharepoint
  - name: Open XML SDK for Word
    description: .NET library for programmatically creating and manipulating Word documents using the ECMA-376 Open XML standard. Provides strongly-typed classes for document structure, styles, tables, images, and content manipulation.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk
    tags:
      - Dotnet
      - Library
      - Offline
      - OpenXML
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/open-xml/open-xml-sdk
      - type: OpenAPI
        url: openapi/microsoft-word-open-xml-sdk.yaml
      - type: GitHubRepository
        url: https://github.com/OfficeDev/Open-XML-SDK
      - type: SDK
        url: https://www.nuget.org/packages/DocumentFormat.OpenXml
        title: .NET SDK
      - type: JSONSchema
        url: json-schema/open-xml-sdk-document-properties-schema.json
        title: DocumentProperties Schema
      - type: JSONStructure
        url: json-structure/open-xml-sdk-document-properties-structure.json
        title: DocumentProperties Structure
      - type: JSONLD
        url: json-ld/microsoft-word-open-xml-sdk-context.jsonld
      - type: Example
        url: examples/open-xml-sdk-document-properties-example.json
        title: DocumentProperties Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.microsoft.com/
  - type: DeveloperPortal
    url: https://developer.microsoft.com/en-us/graph
  - type: Console
    url: https://developer.microsoft.com/en-us/graph/graph-explorer
  - type: SignUp
    url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
  - type: Authentication
    url: https://learn.microsoft.com/en-us/graph/auth/
  - type: GettingStarted
    url: https://learn.microsoft.com/en-us/graph/get-started
  - type: Blog
    url: https://devblogs.microsoft.com/microsoft365dev/
  - type: Support
    url: https://developer.microsoft.com/graph/support
  - type: StatusPage
    url: https://status.office.com/
  - type: ChangeLog
    url: https://developer.microsoft.com/en-us/graph/changelog
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/
  - type: GitHubOrganization
    url: https://github.com/OfficeDev
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/microsoft-graph
  - type: X
    url: https://twitter.com/MSGraphDev
  - type: YouTube
    url: https://www.youtube.com/@Microsoft365Developer
  - type: Training
    url: https://learn.microsoft.com/en-us/training/browse/?products=ms-graph
  - type: SpectralRules
    url: rules/microsoft-word-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/microsoft-word-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/document-management.yaml
    title: Document Management
  - type: Features
    data:
      - name: Document Creation
        description: Programmatically create Word documents from templates or scratch using REST APIs or JavaScript.
      - name: Document Conversion
        description: Convert Word documents to PDF, HTML, and other formats using server-side automation services.
      - name: Content Manipulation
        description: Insert, edit, and format text, paragraphs, tables, images, and content controls in Word documents.
      - name: Collaboration
        description: Track changes, manage comments, co-authoring sessions, and revision history through APIs.
      - name: Template Processing
        description: Mail merge, document assembly, and template-based document generation for enterprise workflows.
      - name: Cloud Storage Integration
        description: Access and manipulate Word documents stored in OneDrive, SharePoint, and Microsoft 365 cloud services.
      - name: Add-In Extensibility
        description: Build custom Word add-ins with JavaScript APIs for task panes, content insertion, and document automation.
      - name: Open XML Processing
        description: Low-level manipulation of Word document structure using the ECMA-376 Open XML standard.
  - type: UseCases
    data:
      - name: Automated Report Generation
        description: Generate standardized reports from data sources using templates and API-driven document creation.
      - name: Contract and Legal Document Assembly
        description: Assemble legal documents by merging clauses, terms, and client data into Word templates.
      - name: Document Review Workflows
        description: Automate review cycles with tracked changes, comments, and approval workflows via APIs.
      - name: Bulk Document Processing
        description: Process large volumes of Word documents for format conversion, content extraction, or metadata updates.
      - name: Custom Business Add-Ins
        description: Build task pane add-ins that connect Word to CRM, ERP, or other business systems for data insertion.
      - name: Compliance Document Management
        description: Ensure regulatory compliance by automating document formatting, metadata tagging, and archiving.
  - type: Integrations
    data:
      - name: Microsoft SharePoint
        description: Store, manage, and collaborate on Word documents through SharePoint document libraries and workflows.
      - name: Microsoft OneDrive
        description: Access and sync Word documents via OneDrive cloud storage through Microsoft Graph APIs.
      - name: Microsoft Teams
        description: Collaborate on Word documents directly within Teams channels and chat conversations.
      - name: Microsoft Power Automate
        description: Automate Word document workflows including creation, conversion, and approval routing with Power Automate flows.
      - name: Microsoft Copilot
        description: AI-powered document creation, editing, and summarization through Copilot agents with add-in actions.
      - name: Azure Active Directory
        description: OAuth 2.0 authentication and authorization for secure API access through Microsoft Identity Platform.
---
