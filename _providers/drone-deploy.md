---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Drone Deploy Agentic Access
  operation_count: 1
  slug: drone-deploy-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 3
apis:
- description: DroneDeploy's GraphQL API is the primary programmatic interface for the DroneDeploy reality-capture platform. A single POST endpoint at https://www.dronedeploy.com/graphql exposes a strongly-typed sch
  name: DroneDeploy GraphQL API
  slug: drone-deploy-graphql-api
- description: The DroneDeploy Apps Platform lets third parties build embedded apps and serverless "functions" that run inside the DroneDeploy web application and the DroneDeploy App Market. Apps consume the GraphQL
  name: DroneDeploy Apps Platform
  slug: drone-deploy-apps-platform
- description: Open-source JavaScript/TypeScript library for parsing DroneDeploy flight log files (the .csv/.json telemetry files emitted by the DroneDeploy Flight App). MIT-licensed, maintained on GitHub.
  name: DroneDeploy Flight Log Parser
  slug: drone-deploy-flight-log-parser
artifact_total: 31
collections:
- collection_type: postman
  name: DroneDeploy GraphQL API
  slug: postman-drone-deploy-graphql-api
- collection_type: open
  name: DroneDeploy GraphQL API
  slug: open-drone-deploy-graphql-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dronedeploy/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drone-deploy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drone-deploy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/drone-deploy-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.dronedeploy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.dronedeploy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.dronedeploy.com/dronedeploy-apps
- group: docs
  title: ''
  type: Documentation
  url: https://developer-docs.dronedeploy.com/api/introduction
- group: start
  title: ''
  type: Sandbox
  url: https://www.dronedeploy.com/graphiql/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dronedeploy.com
- group: start
  title: ''
  type: Signup
  url: https://www.dronedeploy.com/get-started
- group: start
  title: ''
  type: Login
  url: https://www.dronedeploy.com/app2/auth/signin
- group: operate
  title: ''
  type: Support
  url: https://help.dronedeploy.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dronedeploy.com/legal/master-services-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dronedeploy.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.dronedeploy.com/blog
- group: company
  title: ''
  type: Careers
  url: https://www.dronedeploy.com/about/careers
- group: company
  title: ''
  type: AboutUs
  url: https://www.dronedeploy.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dronedeploy
- group: other
  title: ''
  type: AppMarket
  url: https://www.dronedeploy.com/product/market
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dronedeploy
- group: other
  title: ''
  type: X
  url: https://twitter.com/dronedeploy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/DroneDeploy
- group: commercial
  title: ''
  type: Plans
  url: https://www.dronedeploy.com/pricing
- group: start
  title: ''
  type: Trial
  url: https://www.dronedeploy.com/get-started
- group: commercial
  title: ''
  type: Plans
  url: plans/drone-deploy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drone-deploy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drone-deploy-finops.yml
created: '2026-05-25'
description: DroneDeploy is the unified reality-capture platform for construction, agriculture, mining, energy, oil & gas, and inspection workflows. Founded in 2013 and headquartered in San Francisco, DroneDeploy combines aerial drone mapping, ground 360 capture, robotics (DJI Dock, Boston Dynamics Spot), and vision-language AI (Progress AI, Safety AI, Earthworks AI) into a single platform that operates across 3M+ sites in 180 countries and has processed 2.8B+ images. Developers integrate via a GraphQL API at https://www.dronedeploy.com/graphql, an Apps Platform with OAuth2 templates that embed third-party apps into the DroneDeploy web application, and a 40+ partner App Market spanning construction (Procore, Autodesk Construction Cloud, PlanGrid), GIS (ArcGIS, Mapbox), cloud storage (S3, Google Drive, OneDrive, Box, Azure), and agriculture (Climate FieldView).
examples:
- key_count: 2
  name: Drone Deploy Create Export Example
  slug: drone-deploy-create-export-example
- key_count: 2
  name: Drone Deploy List Plans Example
  slug: drone-deploy-list-plans-example
features:
- DroneDeploy Aerial — automated drone flight, photogrammetry, orthomosaic, 3D models, design overlays
- DroneDeploy Ground — 360 walks, mobile 3D scanning, LiDAR, 8K imagery, BIM overlays
- DroneDeploy Robotics — dock automation and industrial inspection with Boston Dynamics and DJI Dock
- Progress AI — automated schedule and progress tracking from reality capture
- Safety AI — visual hazard detection ranked by severity
- Earthworks AI — cut/fill volumetrics and earthworks progress
- GraphQL API at https://www.dronedeploy.com/graphql with strongly-typed schema and Relay-style cursor pagination
- GraphiQL interactive explorer at https://www.dronedeploy.com/graphiql/
- Apps Platform with OAuth2 templates and serverless function model
- DroneDeploy App Market with 40+ integration partners (Procore, Autodesk Construction Cloud, ArcGIS, S3, Google Drive, OneDrive, Box, Azure, Climate FieldView)
- 14-day free trial, no credit card required
- Operates across 3M+ sites in 180 countries; 2.8B+ images processed
finops:
- name: Drone Deploy Finops
  service_category: Geospatial and Reality Capture
  slug: drone-deploy-finops
graphqls:
- description: DroneDeploy's GraphQL API is the primary programmatic interface for the DroneDeploy reality-capture platform. A single POST endpoint at https://www.dronedeploy.com/graphql exposes a strongly-typed sch
  name: DroneDeploy GraphQL API
  slug: drone-deploy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drone-deploy.png
json_schemas:
- name: DroneDeploy Export
  property_count: 6
  slug: drone-deploy-export
- name: DroneDeploy Plan
  property_count: 6
  slug: drone-deploy-plan
jsonld:
- class_count: 0
  name: Drone Deploy Context
  property_count: 7
  slug: drone-deploy-context
layout: provider
modified: '2026-05-25'
name: DroneDeploy
nav: Providers
network: true
overview: 'DroneDeploy publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Drones, Reality Capture, Mapping, Photogrammetry, and 3D Models.


  The DroneDeploy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  DroneDeploy''s developer surface includes authentication, developer portal, documentation, sandbox, signup flow, support, engineering blog, and 21 more developer resources.'
plans:
- name: Drone Deploy Plans Pricing
  plan_count: 4
  slug: drone-deploy-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Drone Deploy Rate Limits
  slug: drone-deploy-rate-limits
rules:
- name: DroneDeploy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: drone-deploy-jsonschema-spectral-rules
- name: DroneDeploy API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 2
  slug: drone-deploy-rules
score:
  band: strong
  composite: 62.8
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 79.8
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/drone-deploy/refs/heads/main/screenshots/drone-deploy-2026-06-20T180248.png
security:
- kind: authentication
  name: Drone Deploy Authentication
  slug: drone-deploy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drone Deploy Domain Security
  slug: drone-deploy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drone-deploy
tags:
- Drones
- Reality Capture
- Mapping
- Photogrammetry
- 3D Models
- Orthomosaic
- LiDAR
- Construction
- Agriculture
- AI
- Aerial
- Robotics
website: https://www.dronedeploy.com
---
