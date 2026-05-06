---
aid: autodesk
name: Autodesk
description: Autodesk is a global leader in design, engineering, and entertainment software, providing cloud-connected platform APIs through Autodesk Platform Services (APS). APS APIs enable developers to build applications that access design data, automate workflows, visualize 3D models, manage construction projects, create digital twins, and integrate sustainability data across Autodesk's product ecosystem including AutoCAD, Revit, Inventor, Maya, BIM 360, and Autodesk Construction Cloud.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - 3D Modeling
  - Architecture
  - BIM
  - CAD
  - Construction
  - Design
  - Digital Twins
  - Engineering
  - Manufacturing
  - Media and Entertainment
  - Sustainability
url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/apis.yml
created: '2024-11-13'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: autodesk:autodesk-build-photos
    name: Autodesk Build Photos API
    description: Provides a single, unified place to view and manage photos and videos in Autodesk Build. This is useful for documenting progress photos on construction projects.
    humanURL: https://aps.autodesk.com/blog/autodesk-build-photos-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Photos
      - Documentation
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/blog/autodesk-build-photos-api
  - aid: autodesk:authentication-api
    name: Autodesk Authentication API
    description: The Authentication API provides OAuth 2.0 based authentication and authorization for Autodesk Platform Services, enabling applications to securely access user data across different services without directly handling user passwords.
    humanURL: https://aps.autodesk.com/developer/overview/authentication-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Authentication
      - OAuth
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/authentication-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/oauth/v2/reference/http
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/oauth/v2/tutorials
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-authentication-openapi.yml
  - aid: autodesk:data-management-api
    name: Autodesk Data Management API
    description: The Data Management API enables management of data across Autodesk Docs, BIM 360 Docs, Fusion Team, and the Object Storage Service. It provides project navigation, folder management, and version control for items stored across Autodesk cloud services.
    humanURL: https://aps.autodesk.com/developer/overview/data-management-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM 360
      - Data Management
      - Storage
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/data-management-api
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/data/v2/tutorials/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-data-management-openapi.yml
  - aid: autodesk:model-derivative-api
    name: Autodesk Model Derivative API
    description: The Model Derivative API translates designs into formats like SVF and SVF2 for rendering in the Viewer, supports over 60 file input formats, converts designs to STL and OBJ, and extracts object hierarchy trees, properties, and geometries for analysis.
    humanURL: https://aps.autodesk.com/developer/overview/model-derivative-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - 3D Models
      - File Conversion
      - Metadata
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/model-derivative-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-model-derivative-openapi.yml
  - aid: autodesk:design-automation-api
    name: Autodesk Design Automation API
    description: The Automation API enables batch processing of design files, parameter adjustments, drawing generation, and data extraction at enterprise scale using AutoCAD, Revit, Inventor, 3ds Max, and Fusion cloud engines.
    humanURL: https://aps.autodesk.com/developer/overview/automation-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - 3ds Max
      - AutoCAD
      - Automation
      - Fusion
      - Inventor
      - Revit
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/automation-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-design-automation-openapi.yml
  - aid: autodesk:viewer-sdk
    name: Autodesk Viewer SDK
    description: The Viewer SDK is a JavaScript library for building interactive web applications that display 2D and 3D design models. It supports various file formats, offers customizable toolbars, and provides a flexible extension framework for creating immersive design experiences.
    humanURL: https://aps.autodesk.com/developer/overview/viewer-sdk
    baseURL: https://developer.api.autodesk.com
    tags:
      - 2D Visualization
      - 3D Visualization
      - Viewer
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/viewer-sdk
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/
  - aid: autodesk:webhooks-api
    name: Autodesk Webhooks API
    description: The Webhooks API enables applications to receive event notifications via POST requests to a callback URL, eliminating the need for continuous polling. It works with Data Management and Model Derivative APIs to monitor events like file modifications within projects.
    humanURL: https://aps.autodesk.com/webhooks-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Events
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/webhooks-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/webhooks/v1/reference/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-webhooks-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/asyncapi/autodesk-webhooks-asyncapi.yml
  - aid: autodesk:reality-capture-api
    name: Autodesk Reality Capture API
    description: The Reality Capture API uses photogrammetry techniques to generate high-resolution 3D models, point clouds, and orthophotos from photographs. It leverages cloud computing for structure-from-motion and multi-view-geometry algorithms, with output compatible with ReCap, Civil 3D, and InfraWorks.
    humanURL: https://aps.autodesk.com/developer/overview/reality-capture-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - 3D Models
      - Photogrammetry
      - Point Clouds
      - Reality Capture
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/reality-capture-api
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/reality-capture/v1/tutorials/create-3d-mesh-from-photos/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-reality-capture-openapi.yml
  - aid: autodesk:aec-data-model-api
    name: Autodesk AEC Data Model API
    description: The AEC Data Model API provides direct cloud access to granular design data via GraphQL, enabling navigation through data structures from hubs and projects to individual elements and parameters without requiring desktop authoring plugins. Currently offers read-only access to Revit elements and properties.
    humanURL: https://aps.autodesk.com/developer/overview/aec-data-model-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - AEC
      - BIM
      - Design Data
      - GraphQL
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/aec-data-model-api
  - aid: autodesk:data-exchange-api
    name: Autodesk Data Exchange API
    description: The Data Exchange API enables seamless sharing of complete or selective 3D model data across BIM, CAD, and other business applications through Autodesk Docs. It supports both GraphQL API and .NET SDK for querying and building custom integrations.
    humanURL: https://aps.autodesk.com/developer/overview/data-exchange
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - CAD
      - Data Exchange
      - Interoperability
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/data-exchange
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/fdxgraph/v1/reference/graphql_endpoint/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/fdxgraph/v1/tutorials/getting_started/task1/
  - aid: autodesk:sustainability-data-api
    name: Autodesk Sustainability Data API
    description: The Sustainability Data API provides access to regional environmental data through a standardized interface, enabling accurate carbon calculations and integration of trusted third-party sustainability datasets into applications at all design stages.
    humanURL: https://aps.autodesk.com/developer/overview/sustainability-data-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Carbon Calculations
      - Environmental Data
      - Sustainability
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/sustainability-data-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/sustainability/v3/reference/http/
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/sustainability/v3/tutorials/tutorial_01/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-sustainability-data-openapi.yml
  - aid: autodesk:parameters-api
    name: Autodesk Parameters API
    description: The Parameters API manages parameter definitions and related metadata in the Autodesk platform cloud, including parameters, groups, collections, labels, and classifications. It enables synchronized, up-to-date parameter collections across products with support for disciplines, specs, units, and Revit categories.
    humanURL: https://aps.autodesk.com/developer/overview/parameters-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - Parameters
      - Revit
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/parameters-api
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/parameters/v1/tutorials/getting-started/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-parameters-openapi.yml
  - aid: autodesk:tandem-data-api
    name: Autodesk Tandem Data API
    description: The Tandem Data API enables reading BIM model data and reading/writing custom schema properties for facility management. It facilitates integration with external systems like asset management platforms, work-order systems, and IoT sensors for creating and managing digital twins.
    humanURL: https://aps.autodesk.com/developer/overview/tandem-data-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Digital Twins
      - Facility Management
      - IoT
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/tandem-data-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-tandem-data-openapi.yml
  - aid: autodesk:flow-graph-engine-api
    name: Autodesk Flow Graph Engine API
    description: The Flow Graph Engine API enables evaluation of Bifrost graphs in the cloud for media and entertainment workflows, allowing developers to offload heavy processing tasks like creating complex effects and simulations to concurrent cloud operations.
    humanURL: https://aps.autodesk.com/developer/overview/flow-graph-engine-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - Bifrost
      - Cloud Computing
      - Media and Entertainment
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/flow-graph-engine-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/flow_graph_engine/v1/reference/quick_reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-flow-graph-engine-openapi.yml
  - aid: autodesk:acc-account-admin-api
    name: Autodesk ACC Account Admin API
    description: The ACC Account Admin API automates the creation and management of projects, assignment and management of project users, and management of member and partner company directories within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/tutorials/admin
    baseURL: https://developer.api.autodesk.com
    tags:
      - Account Administration
      - Construction
      - Project Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
      - type: GettingStarted
        url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/admin
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/acc/v1/reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-acc-account-admin-openapi.yml
  - aid: autodesk:acc-issues-api
    name: Autodesk ACC Issues API
    description: The ACC Issues API enables creating, tracking, and managing project issues in Autodesk Construction Cloud with automated assignments, status reporting, and workflow management.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/issues/
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Issues
      - Project Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/issues/
  - aid: autodesk:acc-rfis-api
    name: Autodesk ACC RFIs API
    description: The ACC RFIs API enables creation and lifecycle tracking of Requests for Information with automated routing, support for assigning members, transitioning between states, and adding comments within Autodesk Construction Cloud projects.
    humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/rfis/
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Project Management
      - RFIs
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/rfis/
  - aid: autodesk:acc-cost-management-api
    name: Autodesk ACC Cost Management API
    description: The ACC Cost Management API provides access to cost management data including budgets, contracts, and change orders, enabling integration with ERP systems within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Budgets
      - Construction
      - Cost Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-data-connector-api
    name: Autodesk ACC Data Connector API
    description: The ACC Data Connector API retrieves data from ACC services such as Admin, Issues, Locations, Submittals, Cost, and RFIs for local data analysis, reporting, and business intelligence purposes.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Business Intelligence
      - Construction
      - Data Analytics
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-model-coordination-api
    name: Autodesk ACC Model Coordination API
    description: The ACC Model Coordination API manages model sets and clash detection test results throughout the coordination process within Autodesk Construction Cloud projects.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Clash Detection
      - Construction
      - Model Coordination
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-assets-api
    name: Autodesk ACC Assets API
    description: The ACC Assets API enables creating, searching, and managing construction assets with custom categories and attributes within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Asset Management
      - Assets
      - Construction
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-locations-api
    name: Autodesk ACC Locations API
    description: The ACC Locations API enables configuration of project location hierarchies for organizing assets, filtering issues, and structuring building areas within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Locations
      - Project Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-forms-api
    name: Autodesk ACC Forms API
    description: The ACC Forms API provides access to and management of project form submissions and templates within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Data Collection
      - Forms
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-photos-api
    name: Autodesk ACC Photos API
    description: The ACC Photos API enables retrieval of project photos and videos, with querying and filtering capabilities for visual data, progress report export, and integration with external systems.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Documentation
      - Photos
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-submittals-api
    name: Autodesk ACC Submittals API
    description: The ACC Submittals API manages submittal packages and tracks their approval status throughout the project lifecycle within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Approvals
      - Construction
      - Submittals
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-sheets-api
    name: Autodesk ACC Sheets API
    description: The ACC Sheets API handles construction sheet set management, versioning, and distribution across project teams within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Document Management
      - Sheets
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-reviews-api
    name: Autodesk ACC Reviews API
    description: The ACC Reviews API manages approval workflows and file reviews, enabling tracking of review status, automation of approval processes, and integration with document control systems.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Approvals
      - Construction
      - Reviews
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-relationships-api
    name: Autodesk ACC Relationships API
    description: The ACC Relationships API creates connections between entities across ACC domains, enabling linking of issues to files, RFIs to assets, and other cross-domain relationships.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Data Linking
      - Relationships
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-model-properties-api
    name: Autodesk ACC Model Properties API
    description: The ACC Model Properties API queries and compares model data across versions for element tracking and analysis within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - Construction
      - Model Properties
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-transmittals-api
    name: Autodesk ACC Transmittals API
    description: The ACC Transmittals API provides access to transmittal data, recipients, documents, and folders, enabling retrieval of transmittal lists and querying by ID within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Document Management
      - Transmittals
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-autospecs-api
    name: Autodesk ACC AutoSpecs API
    description: The ACC AutoSpecs API retrieves Smart Register data from specification PDFs and submittal requirements within Autodesk Construction Cloud.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Specifications
      - Submittals
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:acc-takeoff-api
    name: Autodesk ACC Takeoff API
    description: The ACC Takeoff API provides access to takeoff items, types, and classification systems, enabling extraction of quantity data, management of packages, and integration of takeoff data with estimating tools.
    humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    baseURL: https://developer.api.autodesk.com
    tags:
      - Construction
      - Quantity Estimation
      - Takeoff
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  - aid: autodesk:bim-360-api
    name: Autodesk BIM 360 API
    description: The BIM 360 API enables integration with the BIM 360 cloud-based construction management platform, providing access to project data, documents, issues, and workflows for greater customization and workflow automation.
    humanURL: https://aps.autodesk.com/developer/overview/bim-360-api
    baseURL: https://developer.api.autodesk.com
    tags:
      - BIM
      - Construction
      - Project Management
    properties:
      - type: Documentation
        url: https://aps.autodesk.com/developer/overview/bim-360-api
      - type: APIReference
        url: https://aps.autodesk.com/en/docs/bim360/v1/reference/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/openapi/autodesk-bim360-openapi.yml
common:
  - type: Portal
    url: https://aps.autodesk.com/
  - type: Blog
    url: https://aps.autodesk.com/blog
  - type: Support
    url: https://aps.autodesk.com/en/support/get-help
  - type: GettingStarted
    url: https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-started-with-aps/
  - type: TermsOfService
    url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/autodesk-web-services-api-terms-of-service
  - type: PrivacyPolicy
    url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
  - type: GitHubOrganization
    url: https://github.com/autodesk-platform-services
  - type: Documentation
    url: https://aps.autodesk.com/developer/documentation
  - type: Pricing
    url: https://aps.autodesk.com/pricing
  - type: CodeExamples
    url: https://aps.autodesk.com/code-samples
  - type: Tutorials
    url: https://tutorials.autodesk.io/
  - type: Quickstart
    url: https://get-started.aps.autodesk.com/
  - type: StatusPage
    url: https://health.autodesk.com/
  - type: ChangeLog
    url: https://aps.autodesk.com/developer/overview/changelog
  - type: Console
    url: https://aps.autodesk.com/myapps/
  - type: Login
    url: https://accounts.autodesk.com
  - type: Authentication
    url: https://aps.autodesk.com/en/docs/oauth/v2
  - type: YouTube
    url: https://www.youtube.com/@autodesk
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/autodesk-forge+or+autodesk-aps
  - type: Website
    url: https://www.autodesk.com
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-hub.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-project.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-item.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-version.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-webhook-event.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-schema/autodesk-issue.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/autodesk/refs/heads/main/json-ld/autodesk-context.jsonld
  - type: Features
    data:
      - name: OAuth 2.0 Authentication
        description: Industry-standard OAuth 2.0 authentication enabling secure access to Autodesk platform services and user data across all APS APIs.
      - name: Design File Translation
        description: Model Derivative API translates over 60 CAD file formats to web-viewable SVF and SVF2 formats, enabling browser-based 3D visualization.
      - name: Cloud Design Automation
        description: Design Automation API enables batch processing of CAD operations at scale using cloud engines for AutoCAD, Revit, Inventor, and Fusion.
      - name: Digital Twins
        description: Tandem Data API enables building digital twin applications by connecting BIM model data with IoT sensors, asset management, and facility systems.
      - name: Construction Cloud Integration
        description: ACC APIs provide programmatic access to construction project management, issues, RFIs, submittals, cost, and coordination data.
      - name: Sustainability Data
        description: Access to regional environmental and carbon emissions data for integrating sustainability calculations into design workflows.
      - name: Reality Capture
        description: Photogrammetry-based 3D model generation from photographs using cloud-scale structure-from-motion algorithms.
  - type: UseCases
    data:
      - name: Custom Viewer Applications
        description: Building web applications that display BIM and CAD models using the Viewer SDK with custom extensions, toolbars, and interactive features.
      - name: Construction Project Automation
        description: Automating construction project workflows through ACC APIs for issues, RFIs, submittals, and cost management with ERP and MES integrations.
      - name: Digital Twin Development
        description: Building facility digital twin applications connecting BIM data with live IoT sensor streams, maintenance systems, and energy monitoring.
      - name: Design Batch Processing
        description: Automating batch generation of drawings, BOMs, and reports from design models using Design Automation API cloud engines at enterprise scale.
      - name: AEC Data Analytics
        description: Extracting and analyzing design element data, model properties, and project metrics using AEC Data Model GraphQL API for reporting.
  - type: Integrations
    data:
      - name: Revit
        description: Deep integration with Autodesk Revit for BIM data access, parameter management, and design automation via APS APIs.
      - name: AutoCAD
        description: Integration with AutoCAD for cloud-based drawing generation and data extraction via the Design Automation API.
      - name: Salesforce
        description: CRM and project management integration connecting Autodesk construction data with Salesforce customer and project records.
      - name: SAP
        description: ERP integration connecting ACC cost management and project data with SAP for enterprise financial reporting and project accounting.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
