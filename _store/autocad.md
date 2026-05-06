---
aid: autocad
name: AutoCAD
description: APIs for Autodesk AutoCAD, providing programmatic access to CAD design, drawing, and automation capabilities through Autodesk Platform Services (APS, formerly Forge) and desktop development environments including AutoLISP, ObjectARX, .NET, and JavaScript.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.autodesk.com/developer-network/platform-technologies/autocad
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - 3D Modeling
  - Architecture
  - CAD
  - Design
  - Drawing
  - Engineering
apis:
  - aid: autocad:autocad-api
    name: AutoCAD API
    description: Core API for AutoCAD automation, drawing manipulation, and entity management.
    humanURL: https://www.autodesk.com/developer-network/platform-technologies/autocad
    baseURL: https://developer.api.autodesk.com
    tags:
      - Automation
      - CAD
      - Drawing
      - Entities
    properties:
      - type: Documentation
        url: https://help.autodesk.com/view/OARX/2024/ENU/
      - type: Authentication
        url: https://forge.autodesk.com/en/docs/oauth/v2/reference/http/
      - type: GettingStarted
        url: https://tutorials.autodesk.io/
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://forge.autodesk.com/en/support/get-help/
  - aid: autocad:design-automation-api
    name: AutoCAD Design Automation API
    description: Cloud-based API that enables running AutoCAD scripts, AutoLISP routines, and custom add-ins in the cloud to automate drawing creation, modification, and batch processing workflows at scale.
    humanURL: https://aps.autodesk.com/apis-and-services/autocad-automation-api
    baseURL: https://developer.api.autodesk.com/da/us-east/v3
    tags:
      - AutoLISP
      - Batch Processing
      - Cloud
      - Design Automation
      - Scripting
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/design-automation/v3
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/design-automation/v3/reference/http/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/design-automation/v3/tutorials/
      - type: ChangeLog
        url: https://aps.autodesk.com/en/docs/design-automation/v3/change_history/acad_release_notes
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://aps.autodesk.com/get-help
  - aid: autocad:data-management-api
    name: AutoCAD Data Management API
    description: API for managing AutoCAD files, versions, and collaboration workflows.
    humanURL: https://forge.autodesk.com/en/docs/data/v2/developers_guide/overview/
    baseURL: https://developer.api.autodesk.com/data/v1
    tags:
      - Collaboration
      - File Management
      - Storage
      - Version Control
    properties:
      - type: Documentation
        url: https://forge.autodesk.com/en/docs/data/v2/
      - type: APIReference
        url: https://forge.autodesk.com/en/docs/data/v2/reference/http/
      - type: GettingStarted
        url: https://forge.autodesk.com/en/docs/data/v2/tutorials/
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://aps.autodesk.com/get-help
  - aid: autocad:model-derivative-api
    name: AutoCAD Model Derivative API
    description: API for translating AutoCAD design files into formats like SVF and SVF2 for rendering in the Viewer SDK, extracting metadata, object hierarchy, properties, and generating thumbnails.
    humanURL: https://aps.autodesk.com/developer/overview/model-derivative-api
    baseURL: https://developer.api.autodesk.com/modelderivative/v2
    tags:
      - File Conversion
      - Metadata
      - Model Derivative
      - Thumbnails
      - Translation
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/model-derivative/v2
      - type: ChangeLog
        url: https://aps.autodesk.com/en/docs/model-derivative/v2/change_history/changelog
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://aps.autodesk.com/get-help
  - aid: autocad:webhooks-api
    name: AutoCAD Webhooks API
    description: API enabling applications to listen for and receive notifications when specific events occur in AutoCAD data and workflows, supporting event-driven architectures.
    humanURL: https://aps.autodesk.com/developer/overview/webhooks-api
    baseURL: https://developer.api.autodesk.com/webhooks/v1
    tags:
      - Events
      - Notifications
      - Real-Time
      - Webhooks
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/webhooks/v1
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/webhooks/v1/reference/
      - type: Tutorials
        url: https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://aps.autodesk.com/get-help
  - aid: autocad:authentication-api
    name: AutoCAD Authentication API
    description: OAuth 2.0-based authentication API for securing access to AutoCAD and Autodesk Platform Services APIs, supporting both 2-legged and 3-legged authentication workflows.
    humanURL: https://aps.autodesk.com/developer/overview/authentication-api
    baseURL: https://developer.api.autodesk.com/authentication/v2
    tags:
      - Authentication
      - Authorization
      - OAuth
      - Security
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/oauth/v2
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/oauth/v2/developers_guide/basics
    contact:
      - FN: Autodesk Developer Support
        email: forge.help@autodesk.com
        url: https://aps.autodesk.com/get-help
common:
  - type: Portal
    url: https://aps.autodesk.com/
  - type: Documentation
    url: https://aps.autodesk.com/developer/documentation
  - type: GettingStarted
    url: https://tutorials.autodesk.io/
  - type: Authentication
    url: https://forge.autodesk.com/en/docs/oauth/v2/
  - type: SDK
    url: https://github.com/autodesk-platform-services/aps-sdk-node
    title: Node.js SDK
  - type: SDK
    url: https://github.com/autodesk-platform-services/aps-sdk-net
    title: .NET SDK
  - type: Blog
    url: https://aps.autodesk.com/blog
  - type: GitHubOrganization
    url: https://github.com/autodesk-platform-services
  - type: Support
    url: https://forge.autodesk.com/en/support/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/autodesk-forge
  - type: SignUp
    url: https://aps.autodesk.com/
  - type: Login
    url: https://manage.autodesk.com/home
  - type: Pricing
    url: https://aps.autodesk.com/pricing
  - type: StatusPage
    url: https://health.autodesk.com/
  - type: TermsOfService
    url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service
  - type: PrivacyPolicy
    url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
  - type: ChangeLog
    url: https://aps.autodesk.com/topics/product-updates
  - type: CodeExamples
    url: https://aps.autodesk.com/code-samples
  - type: Features
    data:
      - name: Cloud-Based Design Automation
        description: Run AutoCAD scripts and add-ins in the cloud for batch processing without local AutoCAD installation.
      - name: 3D Model Translation
        description: Translate CAD files between formats and extract metadata for web-based viewing and analysis.
      - name: File Version Management
        description: Manage design file versions, revisions, and collaboration workflows through the Data Management API.
      - name: Event-Driven Webhooks
        description: Receive real-time notifications when design files are created, updated, or shared.
      - name: OAuth 2.0 Authentication
        description: Secure API access with 2-legged and 3-legged OAuth flows for application and user-level authorization.
      - name: Web-Based Viewer
        description: Embed 2D and 3D design viewers in web applications with the Viewer SDK.
  - type: UseCases
    data:
      - name: Automated Drawing Generation
        description: Generate construction drawings, floor plans, and engineering diagrams automatically using Design Automation API.
      - name: Design File Collaboration
        description: Build collaborative design workflows with file sharing, version control, and real-time notifications.
      - name: Batch File Processing
        description: Process thousands of CAD files in the cloud for format conversion, data extraction, and quality checks.
      - name: BIM Integration
        description: Integrate Building Information Modeling data with enterprise systems for construction project management.
      - name: Custom CAD Applications
        description: Build custom AutoCAD plugins and extensions using ObjectARX, .NET, AutoLISP, or JavaScript APIs.
  - type: Integrations
    data:
      - name: Autodesk Construction Cloud
        description: Integration with ACC for construction project management and design coordination.
      - name: BIM 360
        description: Cloud-based BIM collaboration platform integration for construction workflows.
      - name: Revit
        description: Interoperability with Revit for architectural design and BIM workflows.
      - name: Navisworks
        description: Integration for 3D coordination, clash detection, and project review.
      - name: Power BI
        description: Data visualization integration for design analytics and project reporting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
