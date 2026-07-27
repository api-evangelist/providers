---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Trimble Agentic Access
  operation_count: 16
  slug: trimble-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 15
apis:
- description: PC*MILER provides commercial vehicle routing and distance calculation APIs for logistics, freight, and transportation management. Delivers mileage, routing, tolls, and fuel optimization for trucking o
  name: Trimble PC*MILER API
  slug: trimble-pcmiler
- description: The Tekla API provides programmatic access to Tekla Structures, a leading Building Information Modeling (BIM) software for structural engineering and detailing. Enables custom model creation, data ext
  name: Tekla API
  slug: trimble-tekla
- description: The SketchUp API enables extension development for Trimble SketchUp, a widely-used 3D modeling and design tool. Supports Ruby and JavaScript APIs for building custom tools, plugins, and integrations f
  name: SketchUp API
  slug: trimble-sketchup
- description: The Trimble ProjectSight API provides portfolio and project information management for construction. Enables programmatic access to project data, submittals, RFIs, and document workflows for construct
  name: ProjectSight API
  slug: trimble-projectsight
- description: 'The TruckMate REST API provides transactional and configuration operations for Trimble''s transportation management system (TMS). Enables freight brokers, carriers, and logistics operators to automate '
  name: TruckMate API
  slug: trimble-truckmate
- description: The Trimble CoPilot Navigation API enables in-cab navigation integration with cloud-based services for commercial vehicle fleets. Provides route delivery, real-time traffic, and truck-specific navigat
  name: CoPilot Navigation API
  slug: trimble-copilot
- description: The TMT (Trimble Maintenance Technology) REST API provides fleet maintenance management operations for commercial vehicle fleets. Enables work order management, preventive maintenance scheduling, part
  name: TMT Fleet Maintenance API
  slug: trimble-tmt
- description: The Viewpoint suite of construction ERP APIs includes Jobpac Connect, Spectrum, and Vista. These REST and web service APIs provide accounting, HR, project management, and operations integrations for c
  name: Viewpoint Construction ERP APIs
  slug: trimble-viewpoint
- description: Trimble Identity provides OAuth 2.0 / OpenID Connect authentication and authorization for all Trimble developer applications. Enables single sign-on across the Trimble platform for web, mobile, and de
  name: Trimble Identity API
  slug: trimble-identity
- description: Building Collaboration Format issue tracking
  name: Trimble BCF Topics API
  slug: trimble-bcf-topics-api
- description: File and document management
  name: Trimble Files API
  slug: trimble-files-api
- description: Address and coordinate conversion
  name: Trimble Geocoding API
  slug: trimble-geocoding-api
- description: Project management
  name: Trimble Projects API
  slug: trimble-projects-api
- description: Route calculation and optimization
  name: Trimble Routing API
  slug: trimble-routing-api
- description: User and team management
  name: Trimble Users API
  slug: trimble-users-api
artifact_total: 56
collections:
- collection_type: open
  name: Trimble Connect API
  slug: open-trimble-connect
- collection_type: open
  name: Trimble Maps API
  slug: open-trimble-maps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trimble-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/trimble-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trimble-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trimble-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trimble
- group: company
  title: ''
  type: Website
  url: https://www.trimble.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.trimble.com/en/developer/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.trimble.com/en/developer
- group: auth
  title: ''
  type: Authentication
  url: https://developer.trimble.com/docs/authentication
- group: other
  title: ''
  type: Marketplace
  url: https://developer.trimble.com/docs/marketplace
- group: other
  title: ''
  type: DesignSystem
  url: https://modus.trimble.com/
- group: company
  title: ''
  type: Blog
  url: https://www.trimble.com/en/news
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trimble-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/trimble-context.jsonld
created: '2026-05-03'
description: Trimble Inc. is a global technology company that provides advanced positioning, navigation, and data analytics solutions across construction, agriculture, transportation, and geospatial industries. Founded in 1978 as Trimble Navigation Limited, the company integrates GPS, laser, optical, and inertial technologies with software and services. Trimble's developer platform spans construction collaboration (Trimble Connect), commercial vehicle routing (PC*MILER, Trimble Maps), building information modeling (Tekla, SketchUp), fleet management (TruckMate, TMT, CoPilot), precision positioning (Mobile Manager, TAP Store), and construction ERP (Viewpoint). Publicly traded on NASDAQ as TRMB.
examples:
- key_count: 2
  name: Trimble Connect Create Bcf Topic Example
  slug: trimble-connect-create-bcf-topic-example
- key_count: 2
  name: Trimble Connect List Projects Example
  slug: trimble-connect-list-projects-example
- key_count: 2
  name: Trimble Maps Calculate Route Example
  slug: trimble-maps-calculate-route-example
- key_count: 2
  name: Trimble Maps Geocode Address Example
  slug: trimble-maps-geocode-address-example
finops:
- name: Trimble Finops
  service_category: Industrial Software
  slug: trimble-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trimble.png
json_schemas:
- name: AddressResponse
  property_count: 6
  slug: trimble-addressresponse
- name: Coords
  property_count: 2
  slug: trimble-coords
- name: DirectionStep
  property_count: 6
  slug: trimble-directionstep
- name: ErrorResponse
  property_count: 3
  slug: trimble-errorresponse
- name: File
  property_count: 13
  slug: trimble-file
- name: FileListResponse
  property_count: 3
  slug: trimble-filelistresponse
- name: GeocodeResponse
  property_count: 8
  slug: trimble-geocoderesponse
- name: Member
  property_count: 5
  slug: trimble-member
- name: MemberListResponse
  property_count: 2
  slug: trimble-memberlistresponse
- name: MileageResponse
  property_count: 4
  slug: trimble-mileageresponse
- name: Trimble Connect Project
  property_count: 12
  slug: trimble-project
- name: ProjectCreate
  property_count: 4
  slug: trimble-projectcreate
- name: ProjectListResponse
  property_count: 4
  slug: trimble-projectlistresponse
- name: ProjectUpdate
  property_count: 4
  slug: trimble-projectupdate
- name: Trimble PC*MILER Route
  property_count: 10
  slug: trimble-route
- name: RouteLeg
  property_count: 4
  slug: trimble-routeleg
- name: RouteResponse
  property_count: 5
  slug: trimble-routeresponse
- name: StopPoint
  property_count: 2
  slug: trimble-stoppoint
- name: Topic
  property_count: 15
  slug: trimble-topic
- name: TopicCreate
  property_count: 8
  slug: trimble-topiccreate
- name: TopicListResponse
  property_count: 2
  slug: trimble-topiclistresponse
- name: TopicUpdate
  property_count: 6
  slug: trimble-topicupdate
json_structures:
- name: Trimble Project Structure
  property_count: 0
  slug: trimble-project-structure
- name: Trimble Route Structure
  property_count: 0
  slug: trimble-route-structure
- name: Trimble Structure
  property_count: 0
  slug: trimble-structure
jsonld:
- class_count: 32
  name: Trimble Context
  property_count: 7
  slug: trimble-context
layout: provider
modified: '2026-05-19'
name: Trimble
nav: Providers
network: true
overview: 'Trimble publishes 6 APIs on the [APIs.io](https://apis.io/) network, including BCF Topics API, Files API, Geocoding API, and 3 more. Tagged areas include Construction, Transportation, Geospatial, GPS, and Mapping.


  The Trimble catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trimble''s developer surface includes authentication, getting-started guide, engineering blog, and 11 more developer resources.'
plans:
- name: Trimble Plans Pricing
  plan_count: 1
  slug: trimble-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Trimble Rate Limits
  slug: trimble-rate-limits
rules:
- name: Trimble API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: trimble-jsonschema-spectral-rules
- name: Trimble API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 8
  slug: trimble-rules
score:
  band: developing
  composite: 54.7
  delta: 4.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 75.5
    developer_ergonomics: 32.6
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 50.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trimble/refs/heads/main/screenshots/trimble-2026-06-20T195713.png
security:
- kind: authentication
  name: Trimble Authentication
  slug: trimble-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Trimble Domain Security
  slug: trimble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Trimble Trust Center
  slug: trimble-trust-center
  summary_line: SOC 2, ISO 27001
slug: trimble
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
website: https://www.trimble.com
---
