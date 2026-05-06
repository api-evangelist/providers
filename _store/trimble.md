---
aid: trimble
name: Trimble
description: Trimble Inc. is a global technology company that provides advanced positioning, navigation, and data analytics solutions across construction, agriculture, transportation, and geospatial industries. Founded in 1978 as Trimble Navigation Limited, the company integrates GPS, laser, optical, and inertial technologies with software and services. Trimble's developer platform spans construction collaboration (Trimble Connect), commercial vehicle routing (PC*MILER, Trimble Maps), building information modeling (Tekla, SketchUp), fleet management (TruckMate, TMT, CoPilot), precision positioning (Mobile Manager, TAP Store), and construction ERP (Viewpoint). Publicly traded on NASDAQ as TRMB.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Construction
  - Transportation
  - Geospatial
  - GPS
  - Mapping
  - BIM
  - Fleet Management
  - Collaboration
  - Agriculture
url: https://raw.githubusercontent.com/api-evangelist/trimble/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trimble:trimble-connect
    name: Trimble Connect API
    description: The Trimble Connect API enables integration with Trimble's cloud-based construction collaboration platform. Provides access to project data, BIM models, document management, issues (BCF Topics), and team collaboration features for construction project management. Acts as the BIM collaboration hub integrating Tekla, SketchUp, and third-party tools.
    humanURL: https://developer.trimble.com/docs/connect
    tags:
      - Construction
      - Collaboration
      - BIM
      - Cloud
      - Document Management
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/connect
      - type: OpenAPI
        url: openapi/trimble-connect-openapi.yml
      - type: SpectralRules
        url: rules/trimble-rules.yml
      - type: NaftikoCapability
        url: capabilities/bim-collaboration.yaml
      - type: JSONSchema
        url: json-schema/trimble-project-schema.json
      - type: JSONStructure
        url: json-structure/trimble-project-structure.json
      - type: JSONLDContext
        url: json-ld/trimble-context.jsonld
  - aid: trimble:trimble-maps
    name: Trimble Maps API
    description: The Trimble Maps API (formerly ALK Technologies PC*MILER) provides interactive mapping and routing solutions optimized for commercial vehicles and transportation. Enables truck-specific routing, geocoding, map tile rendering, and turn-by-turn navigation services across North America, Europe, and global markets.
    humanURL: https://developer.trimble.com/docs/maps
    tags:
      - Mapping
      - Transportation
      - Routing
      - Geospatial
      - Commercial Vehicles
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/maps
      - type: DeveloperPortal
        url: https://developer.trimblemaps.com/
      - type: OpenAPI
        url: openapi/trimble-maps-openapi.yml
      - type: NaftikoCapability
        url: capabilities/commercial-routing.yaml
      - type: JSONSchema
        url: json-schema/trimble-route-schema.json
      - type: JSONStructure
        url: json-structure/trimble-route-structure.json
  - aid: trimble:trimble-pcmiler
    name: Trimble PC*MILER API
    description: PC*MILER provides commercial vehicle routing and distance calculation APIs for logistics, freight, and transportation management. Delivers mileage, routing, tolls, and fuel optimization for trucking operations across North America, Europe, and global markets.
    humanURL: https://developer.trimble.com/docs/pc-miler
    tags:
      - Transportation
      - Routing
      - Logistics
      - Distance Calculation
      - Commercial Vehicles
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/pc-miler
  - aid: trimble:trimble-tekla
    name: Tekla API
    description: The Tekla API provides programmatic access to Tekla Structures, a leading Building Information Modeling (BIM) software for structural engineering and detailing. Enables custom model creation, data extraction, and workflow automation for steel, concrete, and timber construction.
    humanURL: https://developer.tekla.com/
    tags:
      - BIM
      - Structural Engineering
      - Construction
      - Modeling
    properties:
      - type: Documentation
        url: https://developer.tekla.com/
      - type: DeveloperPortal
        url: https://developer.tekla.com/
  - aid: trimble:trimble-sketchup
    name: SketchUp API
    description: The SketchUp API enables extension development for Trimble SketchUp, a widely-used 3D modeling and design tool. Supports Ruby and JavaScript APIs for building custom tools, plugins, and integrations for architecture, interior design, and engineering workflows.
    humanURL: https://developer.sketchup.com/
    tags:
      - 3D Modeling
      - Architecture
      - Design
      - Plugins
    properties:
      - type: Documentation
        url: https://developer.sketchup.com/
  - aid: trimble:trimble-projectsight
    name: ProjectSight API
    description: The Trimble ProjectSight API provides portfolio and project information management for construction. Enables programmatic access to project data, submittals, RFIs, and document workflows for construction project management.
    humanURL: https://developer.trimble.com/docs/projectsight
    tags:
      - Construction
      - Project Management
      - Documents
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/projectsight
  - aid: trimble:trimble-truckmate
    name: TruckMate API
    description: The TruckMate REST API provides transactional and configuration operations for Trimble's transportation management system (TMS). Enables freight brokers, carriers, and logistics operators to automate dispatch, load management, and billing workflows.
    humanURL: https://developer.trimble.com/docs/truckmate
    tags:
      - Transportation
      - TMS
      - Logistics
      - Freight
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/truckmate
  - aid: trimble:trimble-copilot
    name: CoPilot Navigation API
    description: The Trimble CoPilot Navigation API enables in-cab navigation integration with cloud-based services for commercial vehicle fleets. Provides route delivery, real-time traffic, and truck-specific navigation for driver mobile applications.
    humanURL: https://developer.trimble.com/docs/copilot
    tags:
      - Navigation
      - Transportation
      - Trucking
      - In-Cab
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/copilot
      - type: DeveloperPortal
        url: https://developer.trimblemaps.com/copilot-navigation/
  - aid: trimble:trimble-tmt
    name: TMT Fleet Maintenance API
    description: The TMT (Trimble Maintenance Technology) REST API provides fleet maintenance management operations for commercial vehicle fleets. Enables work order management, preventive maintenance scheduling, parts inventory, and repair tracking.
    humanURL: https://developer.trimble.com/docs/tmt
    tags:
      - Fleet Management
      - Maintenance
      - Transportation
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/tmt
  - aid: trimble:trimble-viewpoint
    name: Viewpoint Construction ERP APIs
    description: The Viewpoint suite of construction ERP APIs includes Jobpac Connect, Spectrum, and Vista. These REST and web service APIs provide accounting, HR, project management, and operations integrations for construction firms.
    humanURL: https://developer.trimble.com/docs/vista
    tags:
      - Construction ERP
      - Accounting
      - HR
      - Finance
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/vista
  - aid: trimble:trimble-identity
    name: Trimble Identity API
    description: Trimble Identity provides OAuth 2.0 / OpenID Connect authentication and authorization for all Trimble developer applications. Enables single sign-on across the Trimble platform for web, mobile, and desktop applications.
    humanURL: https://developer.trimble.com/docs/authentication
    tags:
      - Authentication
      - OAuth 2.0
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://developer.trimble.com/docs/authentication
features:
  - BIM collaboration and model viewing via Trimble Connect
  - Commercial vehicle routing and mileage with PC*MILER
  - Interactive mapping and geocoding for web and mobile
  - Structural BIM modeling API (Tekla)
  - 3D design extension framework (SketchUp)
  - Construction project management and document control
  - Fleet TMS with dispatch and billing (TruckMate)
  - Fleet maintenance management (TMT)
  - In-cab navigation for truck drivers (CoPilot)
  - Construction ERP integration (Viewpoint Vista, Spectrum, Jobpac)
  - High-accuracy GNSS positioning (Mobile Manager, TAP Store)
  - Survey and geospatial field data management
  - Unified OAuth 2.0 authentication via Trimble Identity
useCases:
  - BIM coordination between structural, MEP, and architectural teams
  - Trucking route optimization for logistics and freight planning
  - Fleet management with maintenance tracking and dispatch
  - Construction project document and submittal workflows
  - Custom SketchUp extensions for design automation
  - Structural engineering model automation with Tekla
  - Real-time commercial vehicle navigation and tracking
  - Construction ERP integration with project cost controls
integrations:
  - Tekla Structures (structural BIM)
  - SketchUp (3D design)
  - Procore, Autodesk Construction Cloud (construction)
  - SAP, Oracle (ERP)
  - Esri ArcGIS (geospatial)
  - ELD/telematics providers (transportation)
solutions:
  - Construction technology companies building BIM integrations
  - Logistics and freight software integrating routing APIs
  - Surveying and geospatial platforms using positioning APIs
  - Fleet management platforms integrating TMS and navigation
  - AEC firms automating Tekla and SketchUp workflows
github:
  - name: trimble-id
    url: https://github.com/trimble-oss
    description: Trimble Open Source Software organization
common:
  - type: Website
    url: https://www.trimble.com
  - type: DeveloperPortal
    url: https://www.trimble.com/en/developer/docs
  - type: GettingStarted
    url: https://www.trimble.com/en/developer
  - type: Authentication
    url: https://developer.trimble.com/docs/authentication
  - type: Marketplace
    url: https://developer.trimble.com/docs/marketplace
  - type: DesignSystem
    url: https://modus.trimble.com/
  - type: Blog
    url: https://www.trimble.com/en/news
  - type: Vocabulary
    url: vocabulary/trimble-vocabulary.yml
  - type: JSONLDContext
    url: json-ld/trimble-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
