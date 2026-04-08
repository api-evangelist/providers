---
aid: autodesk
url: https://raw.githubusercontent.com/api-search/autodesk/refs/heads/main/apis.yml
apis:
- aid: autodesk:autodesk
  name: Autodesk
  tags: []
  humanURL: https://aps.autodesk.com/blog/autodesk-build-photos-api
  properties:
  - url: https://aps.autodesk.com/blog/autodesk-build-photos-api
    type: Documentation
  description: It provides a single, unified place to view and manage photos and videos in Autodesk Build. This is useful, such as for documenting progress photos.
- aid: autodesk:authentication-api
  name: Autodesk Authentication API
  tags:
  - Authentication
  - OAuth
  humanURL: https://aps.autodesk.com/developer/overview/authentication-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/authentication-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/oauth/v2
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/oauth/v2/reference/http
    type: API Reference
  - url: https://aps.autodesk.com/en/docs/oauth/v2/tutorials
    type: Getting Started
  - url: openapi/autodesk-authentication-openapi.yml
    type: OpenAPI
  description: The Authentication API provides OAuth 2.0 based authentication and authorization for Autodesk Platform Services, enabling applications to securely access user data across different services without directly handling user passwords.
- aid: autodesk:data-management-api
  name: Autodesk Data Management API
  tags:
  - BIM 360
  - Data Management
  - Storage
  humanURL: https://aps.autodesk.com/developer/overview/data-management-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/data-management-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/data/v2/developers_guide/overview/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/data/v2/tutorials/
    type: Getting Started
  - url: openapi/autodesk-data-management-openapi.yml
    type: OpenAPI
  description: The Data Management API enables management of data across Autodesk Docs, BIM 360 Docs, Fusion Team, and the Object Storage Service. It provides project navigation, folder management, and version control for items stored across Autodesk cloud services.
- aid: autodesk:model-derivative-api
  name: Autodesk Model Derivative API
  tags:
  - 3D Models
  - File Conversion
  - Metadata
  humanURL: https://aps.autodesk.com/developer/overview/model-derivative-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/model-derivative-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/model-derivative/v2
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/model-derivative/v2/reference/
    type: API Reference
  - url: https://aps.autodesk.com/en/docs/model-derivative/v2/tutorials/
    type: Getting Started
  - url: openapi/autodesk-model-derivative-openapi.yml
    type: OpenAPI
  description: The Model Derivative API translates designs into formats like SVF and SVF2 for rendering in the Viewer, supports over 60 file input formats, converts designs to STL and OBJ, and extracts object hierarchy trees, properties, and geometries for analysis.
- aid: autodesk:design-automation-api
  name: Autodesk Automation API
  tags:
  - 3ds Max
  - AutoCAD
  - Automation
  - Fusion
  - Inventor
  - Revit
  humanURL: https://aps.autodesk.com/developer/overview/automation-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/automation-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/design-automation/v3
    type: Documentation
  - url: openapi/autodesk-design-automation-openapi.yml
    type: OpenAPI
  description: The Automation API enables batch processing of design files, parameter adjustments, drawing generation, and data extraction at enterprise scale using AutoCAD, Revit, Inventor, 3ds Max, and Fusion cloud engines.
- aid: autodesk:viewer-sdk
  name: Autodesk Viewer SDK
  tags:
  - 2D Visualization
  - 3D Visualization
  - Viewer
  humanURL: https://aps.autodesk.com/developer/overview/viewer-sdk
  properties:
  - url: https://aps.autodesk.com/developer/overview/viewer-sdk
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/viewer/v7
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/viewer/v7/developers_guide/
    type: Getting Started
  description: The Viewer SDK is a JavaScript library for building interactive web applications that display 2D and 3D design models. It supports various file formats, offers customizable toolbars, and provides a flexible extension framework for creating immersive design experiences.
- aid: autodesk:webhooks-api
  name: Autodesk Webhooks API
  tags:
  - Events
  - Notifications
  - Webhooks
  humanURL: https://aps.autodesk.com/webhooks-api
  properties:
  - url: https://aps.autodesk.com/webhooks-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/webhooks/v1
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/webhooks/v1/reference/
    type: API Reference
  - url: https://aps.autodesk.com/en/docs/webhooks/v1/tutorials/
    type: Getting Started
  - url: openapi/autodesk-webhooks-openapi.yml
    type: OpenAPI
  - url: asyncapi/autodesk-webhooks-asyncapi.yml
    type: AsyncAPI
  description: The Webhooks API enables applications to receive event notifications via POST requests to a callback URL, eliminating the need for continuous polling. It works with Data Management and Model Derivative APIs to monitor events like file modifications within projects.
- aid: autodesk:reality-capture-api
  name: Autodesk Reality Capture API
  tags:
  - 3D Models
  - Photogrammetry
  - Point Clouds
  - Reality Capture
  humanURL: https://aps.autodesk.com/developer/overview/reality-capture-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/reality-capture-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/reality-capture/v1/developers_guide/overview/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/reality-capture/v1/tutorials/create-3d-mesh-from-photos/
    type: Getting Started
  - url: openapi/autodesk-reality-capture-openapi.yml
    type: OpenAPI
  description: The Reality Capture API uses photogrammetry techniques to generate high-resolution 3D models, point clouds, and orthophotos from photographs. It leverages cloud computing for structure-from-motion and multi-view-geometry algorithms, with output compatible with ReCap, Civil 3D, and InfraWorks.
- aid: autodesk:aec-data-model-api
  name: Autodesk AEC Data Model API
  tags:
  - AEC
  - BIM
  - Design Data
  - GraphQL
  humanURL: https://aps.autodesk.com/developer/overview/aec-data-model-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/aec-data-model-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/aecdatamodel/v1/developers_guide/overview/
    type: Documentation
  - url: https://aps.autodesk.com/autodesk-aec-data-model-api
    type: Landing Page
  description: The AEC Data Model API provides direct cloud access to granular design data via GraphQL, enabling navigation through data structures from hubs and projects to individual elements and parameters without requiring desktop authoring plugins. Currently offers read-only access to Revit elements and properties.
- aid: autodesk:data-exchange-api
  name: Autodesk Data Exchange API
  tags:
  - BIM
  - CAD
  - Data Exchange
  - Interoperability
  humanURL: https://aps.autodesk.com/developer/overview/data-exchange
  properties:
  - url: https://aps.autodesk.com/developer/overview/data-exchange
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/fdxgraph/v1/reference/graphql_endpoint/
    type: API Reference
  - url: https://aps.autodesk.com/en/docs/fdxgraph/v1/tutorials/getting_started/task1/
    type: Getting Started
  description: The Data Exchange API enables seamless sharing of complete or selective 3D model data across BIM, CAD, and other business applications through Autodesk Docs. It supports both GraphQL API and .NET SDK for querying and building custom integrations.
- aid: autodesk:sustainability-data-api
  name: Autodesk Sustainability Data API
  tags:
  - Carbon Calculations
  - Environmental Data
  - Sustainability
  humanURL: https://aps.autodesk.com/developer/overview/sustainability-data-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/sustainability-data-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/sustainability/v3/developers_guide/overview/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/sustainability/v3/reference/http/
    type: API Reference
  - url: https://aps.autodesk.com/en/docs/sustainability/v3/tutorials/tutorial_01/
    type: Getting Started
  - url: openapi/autodesk-sustainability-data-openapi.yml
    type: OpenAPI
  description: The Sustainability Data API provides access to regional environmental data through a standardized interface, enabling accurate carbon calculations and integration of trusted third-party sustainability datasets into applications at all design stages.
- aid: autodesk:parameters-api
  name: Autodesk Parameters API
  tags:
  - BIM
  - Parameters
  - Revit
  humanURL: https://aps.autodesk.com/developer/overview/parameters-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/parameters-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/parameters/v1/overview/introduction/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/parameters/v1/tutorials/getting-started/
    type: Getting Started
  - url: openapi/autodesk-parameters-openapi.yml
    type: OpenAPI
  description: The Parameters API manages parameter definitions and related metadata in the Autodesk platform cloud, including parameters, groups, collections, labels, and classifications. It enables synchronized, up-to-date parameter collections across products with support for disciplines, specs, units, and Revit categories.
- aid: autodesk:tandem-data-api
  name: Autodesk Tandem Data API
  tags:
  - Digital Twins
  - Facility Management
  - IoT
  humanURL: https://aps.autodesk.com/developer/overview/tandem-data-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/tandem-data-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/tandem/v1/developers_guide/overview/
    type: Documentation
  - url: openapi/autodesk-tandem-data-openapi.yml
    type: OpenAPI
  description: The Tandem Data API enables reading BIM model data and reading/writing custom schema properties for facility management. It facilitates integration with external systems like asset management platforms, work-order systems, and IoT sensors for creating and managing digital twins.
- aid: autodesk:flow-graph-engine-api
  name: Autodesk Flow Graph Engine API
  tags:
  - Bifrost
  - Cloud Computing
  - Media & Entertainment
  humanURL: https://aps.autodesk.com/developer/overview/flow-graph-engine-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/flow-graph-engine-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/flow_graph_engine/v1/developers_guide/overview/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/flow_graph_engine/v1/reference/quick_reference/
    type: API Reference
  - url: openapi/autodesk-flow-graph-engine-openapi.yml
    type: OpenAPI
  description: The Flow Graph Engine API enables evaluation of Bifrost graphs in the cloud for media and entertainment workflows, allowing developers to offload heavy processing tasks like creating complex effects and simulations to concurrent cloud operations.
- aid: autodesk:acc-account-admin-api
  name: Autodesk ACC Account Admin API
  tags:
  - Account Administration
  - Construction
  - Project Management
  humanURL: https://aps.autodesk.com/en/docs/acc/v1/tutorials/admin
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/acc/v1/tutorials/admin
    type: Getting Started
  - url: https://aps.autodesk.com/en/docs/acc/v1/reference
    type: API Reference
  - url: openapi/autodesk-acc-account-admin-openapi.yml
    type: OpenAPI
  description: The ACC Account Admin API automates the creation and management of projects, assignment and management of project users, and management of member and partner company directories within Autodesk Construction Cloud.
- aid: autodesk:acc-issues-api
  name: Autodesk ACC Issues API
  tags:
  - Construction
  - Issues
  - Project Management
  humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/issues/
  properties:
  - url: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/issues/
    type: Documentation
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Issues API enables creating, tracking, and managing project issues in Autodesk Construction Cloud with automated assignments, status reporting, and workflow management.
- aid: autodesk:acc-rfis-api
  name: Autodesk ACC RFIs API
  tags:
  - Construction
  - Project Management
  - RFIs
  humanURL: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/rfis/
  properties:
  - url: https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/rfis/
    type: Documentation
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC RFIs API enables creation and lifecycle tracking of Requests for Information with automated routing, support for assigning members, transitioning between states, and adding comments within Autodesk Construction Cloud projects.
- aid: autodesk:acc-cost-management-api
  name: Autodesk ACC Cost Management API
  tags:
  - Budgets
  - Construction
  - Cost Management
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Cost Management API provides access to cost management data including budgets, contracts, and change orders, enabling integration with ERP systems within Autodesk Construction Cloud.
- aid: autodesk:acc-data-connector-api
  name: Autodesk ACC Data Connector API
  tags:
  - Business Intelligence
  - Construction
  - Data Analytics
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Data Connector API retrieves data from ACC services such as Admin, Issues, Locations, Submittals, Cost, and RFIs for local data analysis, reporting, and business intelligence purposes.
- aid: autodesk:acc-model-coordination-api
  name: Autodesk ACC Model Coordination API
  tags:
  - Clash Detection
  - Construction
  - Model Coordination
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Model Coordination API manages model sets and clash detection test results throughout the coordination process within Autodesk Construction Cloud projects.
- aid: autodesk:acc-assets-api
  name: Autodesk ACC Assets API
  tags:
  - Asset Management
  - Assets
  - Construction
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Assets API enables creating, searching, and managing construction assets with custom categories and attributes within Autodesk Construction Cloud.
- aid: autodesk:acc-locations-api
  name: Autodesk ACC Locations API
  tags:
  - Construction
  - Locations
  - Project Management
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Locations API enables configuration of project location hierarchies for organizing assets, filtering issues, and structuring building areas within Autodesk Construction Cloud.
- aid: autodesk:acc-forms-api
  name: Autodesk ACC Forms API
  tags:
  - Construction
  - Data Collection
  - Forms
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Forms API provides access to and management of project form submissions and templates within Autodesk Construction Cloud.
- aid: autodesk:acc-photos-api
  name: Autodesk ACC Photos API
  tags:
  - Construction
  - Documentation
  - Photos
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Photos API enables retrieval of project photos and videos, with querying and filtering capabilities for visual data, progress report export, and integration with external systems.
- aid: autodesk:acc-submittals-api
  name: Autodesk ACC Submittals API
  tags:
  - Approvals
  - Construction
  - Submittals
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Submittals API manages submittal packages and tracks their approval status throughout the project lifecycle within Autodesk Construction Cloud.
- aid: autodesk:acc-sheets-api
  name: Autodesk ACC Sheets API
  tags:
  - Construction
  - Document Management
  - Sheets
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Sheets API handles construction sheet set management, versioning, and distribution across project teams within Autodesk Construction Cloud.
- aid: autodesk:acc-reviews-api
  name: Autodesk ACC Reviews API
  tags:
  - Approvals
  - Construction
  - Reviews
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Reviews API manages approval workflows and file reviews, enabling tracking of review status, automation of approval processes, and integration with document control systems.
- aid: autodesk:acc-relationships-api
  name: Autodesk ACC Relationships API
  tags:
  - Construction
  - Data Linking
  - Relationships
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Relationships API creates connections between entities across ACC domains, enabling linking of issues to files, RFIs to assets, and other cross-domain relationships.
- aid: autodesk:acc-model-properties-api
  name: Autodesk ACC Model Properties API
  tags:
  - BIM
  - Construction
  - Model Properties
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Model Properties API queries and compares model data across versions for element tracking and analysis within Autodesk Construction Cloud.
- aid: autodesk:acc-transmittals-api
  name: Autodesk ACC Transmittals API
  tags:
  - Construction
  - Document Management
  - Transmittals
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Transmittals API provides access to transmittal data, recipients, documents, and folders, enabling retrieval of transmittal lists and querying by ID within Autodesk Construction Cloud.
- aid: autodesk:acc-autospecs-api
  name: Autodesk ACC AutoSpecs API
  tags:
  - Construction
  - Specifications
  - Submittals
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC AutoSpecs API retrieves Smart Register data from specification PDFs and submittal requirements within Autodesk Construction Cloud.
- aid: autodesk:acc-takeoff-api
  name: Autodesk ACC Takeoff API
  tags:
  - Construction
  - Quantity Estimation
  - Takeoff
  humanURL: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
  properties:
  - url: https://aps.autodesk.com/developer/overview/autodesk-construction-cloud
    type: Documentation
  description: The ACC Takeoff API provides access to takeoff items, types, and classification systems, enabling extraction of quantity data, management of packages, and integration of takeoff data with estimating tools.
- aid: autodesk:bim-360-api
  name: Autodesk BIM 360 API
  tags:
  - BIM
  - Construction
  - Project Management
  humanURL: https://aps.autodesk.com/developer/overview/bim-360-api
  properties:
  - url: https://aps.autodesk.com/developer/overview/bim-360-api
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/bim360/v1/overview/
    type: Documentation
  - url: https://aps.autodesk.com/en/docs/bim360/v1/reference/
    type: API Reference
  - url: openapi/autodesk-bim360-openapi.yml
    type: OpenAPI
  description: The BIM 360 API enables integration with the BIM 360 cloud-based construction management platform, providing access to project data, documents, issues, and workflows for greater customization and workflow automation.
name: Autodesk
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
- Media & Entertainment
- Sustainability
type: Contract
image: https://www.autodesk.com/favicon.ico
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-07'
position: Consuming
description: A collection of APIs provided by Autodesk for design, engineering, and entertainment software solutions.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

