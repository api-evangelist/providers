---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 19
  human_in_the_loop: 0
  name: Autodesk Bim360 Agentic Access
  operation_count: 44
  slug: autodesk-bim360-agentic-access
  summary_line: 44 operations · 19 acting
api_count: 25
apis:
- description: Automates setting up projects, assigning project admins, managing member and partner company directories, and synchronizing data with external systems. Enables programmatic control of BIM 360 account-
  name: BIM 360 Account Admin API
  slug: bim-360-account-admin-api
- description: Creates, tracks, and updates issues within BIM 360 projects. Issues are items created for tracking, managing, and communicating problems and other points of concern through to resolution. Version 2 of
  name: BIM 360 Issues API
  slug: bim-360-issues-api
- description: Connects BIM APIs to access, upload, and share 2D plans, 3D BIM models, and any other project documents to maximize collaboration. Provides programmatic access to BIM 360 Docs for document storage and
  name: BIM 360 Document Management API
  slug: bim-360-document-management-api
- description: Creates and manages assets in the BIM 360 Assets service, allowing developers to define settings such as categories, custom attributes, and sets of statuses. Provides full programmatic access to asset
  name: BIM 360 Assets API
  slug: bim-360-assets-api
- description: Provides access to cost and budget changes within construction projects, including budget, contract, and change order information. Enables integration with financial systems and programmatic managemen
  name: BIM 360 Cost Management API
  slug: bim-360-cost-management-api
- description: Provides full access to model coordination services used by the BIM 360 Model Coordination web application. Enables detection and management of clashes and issues that arise when 3D models from differ
  name: BIM 360 Model Coordination API
  slug: bim-360-model-coordination-api
- description: Creates, tracks, and updates RFIs (Requests for Information) within BIM 360 projects. Provides programmatic access to the RFI workflow, enabling integration with external project management and commun
  name: BIM 360 RFIs API
  slug: bim-360-rfis-api
- description: Creates and tracks quality checklists within BIM 360 projects. Supports field inspection workflows and quality assurance processes by providing programmatic access to checklist templates and responses
  name: BIM 360 Checklists API
  slug: bim-360-checklists-api
- description: Retrieves aggregated data from BIM 360 services including Admin, Issues, Locations, Submittals, Cost, and RFIs. Enables bulk data extraction for analytics, reporting, and integration with business int
  name: BIM 360 Data Connector API
  slug: bim-360-data-connector-api
- description: Manages and shares the hierarchy of building areas within construction projects. Provides programmatic access to location trees used to organize and contextualize issues, assets, and other project dat
  name: BIM 360 Locations API
  slug: bim-360-locations-api
- description: Creates, retrieves, and deletes links between entities across domains in BIM 360. Enables cross-domain data linking between issues, RFIs, assets, documents, and other project entities to provide trace
  name: BIM 360 Relationships API
  slug: bim-360-relationships-api
- description: The Account Users API from Autodesk BIM 360 — 6 operation(s) for account users.
  name: Autodesk BIM 360 Account Users API
  slug: autodesk-bim360-account-users-api
- description: The Business Units API from Autodesk BIM 360 — 1 operation(s) for business units.
  name: Autodesk BIM 360 Business Units API
  slug: autodesk-bim360-business-units-api
- description: The Companies API from Autodesk BIM 360 — 7 operation(s) for companies.
  name: Autodesk BIM 360 Companies API
  slug: autodesk-bim360-companies-api
- description: The Issue Attachments API from Autodesk BIM 360 — 3 operation(s) for issue attachments.
  name: Autodesk BIM 360 Issue Attachments API
  slug: autodesk-bim360-issue-attachments-api
- description: The Issue Attribute Definitions API from Autodesk BIM 360 — 1 operation(s) for issue attribute definitions.
  name: Autodesk BIM 360 Issue Attribute Definitions API
  slug: autodesk-bim360-issue-attribute-definitions-api
- description: The Issue Attribute Mappings API from Autodesk BIM 360 — 1 operation(s) for issue attribute mappings.
  name: Autodesk BIM 360 Issue Attribute Mappings API
  slug: autodesk-bim360-issue-attribute-mappings-api
- description: The Issue Comments API from Autodesk BIM 360 — 1 operation(s) for issue comments.
  name: Autodesk BIM 360 Issue Comments API
  slug: autodesk-bim360-issue-comments-api
- description: The Issue Root Cause Categories API from Autodesk BIM 360 — 1 operation(s) for issue root cause categories.
  name: Autodesk BIM 360 Issue Root Cause Categories API
  slug: autodesk-bim360-issue-root-cause-categories-api
- description: The Issue Types API from Autodesk BIM 360 — 1 operation(s) for issue types.
  name: Autodesk BIM 360 Issue Types API
  slug: autodesk-bim360-issue-types-api
- description: The Issues API from Autodesk BIM 360 — 2 operation(s) for issues.
  name: Autodesk BIM 360 Issues API
  slug: autodesk-bim360-issues-api
- description: The Issues Profile API from Autodesk BIM 360 — 1 operation(s) for issues profile.
  name: Autodesk BIM 360 Issues Profile API
  slug: autodesk-bim360-issues-profile-api
- description: The Project Users API from Autodesk BIM 360 — 3 operation(s) for project users.
  name: Autodesk BIM 360 Project Users API
  slug: autodesk-bim360-project-users-api
- description: The Projects API from Autodesk BIM 360 — 3 operation(s) for projects.
  name: Autodesk BIM 360 Projects API
  slug: autodesk-bim360-projects-api
- description: The User Projects API from Autodesk BIM 360 — 1 operation(s) for user projects.
  name: Autodesk BIM 360 User Projects API
  slug: autodesk-bim360-user-projects-api
artifact_total: 46
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/autodesk-bim360-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autodesk-bim360-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autodesk-bim360-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autodesk-bim360-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://construction.autodesk.com/products/autodesk-bim-360/
- group: docs
  title: ''
  type: Documentation
  url: https://aps.autodesk.com/en/docs/bim360/v1/overview/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/autodesk-platform-services
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/autodeskplatformservices/
- group: company
  title: ''
  type: Blog
  url: https://aps.autodesk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aps.autodesk.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://health.autodesk.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/BIM360
- group: commercial
  title: ''
  type: Plans
  url: plans/autodesk-bim360-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/autodesk-bim360-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/autodesk-bim360-finops.yml
created: '2026-06-13'
description: Autodesk BIM 360 is a cloud-based construction project management platform that provides a comprehensive suite of REST APIs enabling developers to integrate construction workflows into custom applications. The platform supports managing projects, documents, issues, RFIs, submittals, quality checklists, assets, cost management, and field reports throughout the construction lifecycle. BIM 360 APIs use OAuth 2.0 authentication through Autodesk Platform Services (APS) and allow teams to automate project setup, synchronize data with external systems, and extend platform capabilities. The APIs cover account administration, document management, model coordination, and field management, making it a central hub for construction data integration and workflow automation.
examples:
- key_count: 19
  name: Autodesk Bim360 Issue Example
  slug: autodesk-bim360-issue-example
- key_count: 24
  name: Autodesk Bim360 Project Example
  slug: autodesk-bim360-project-example
- key_count: 12
  name: Autodesk Bim360 User Example
  slug: autodesk-bim360-user-example
finops:
- name: Autodesk Bim360 Finops
  service_category: ''
  slug: autodesk-bim360-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/autodesk-bim360.png
json_schemas:
- name: attachment
  property_count: 20
  slug: autodesk-bim360-attachment
- name: BusinessUnit
  property_count: 8
  slug: autodesk-bim360-businessunit
- name: comment
  property_count: 10
  slug: autodesk-bim360-comment
- name: Company
  property_count: 15
  slug: autodesk-bim360-company
- name: Issue
  property_count: 42
  slug: autodesk-bim360-issue
- name: Project
  property_count: 37
  slug: autodesk-bim360-project
- name: ProjectUser
  property_count: 27
  slug: autodesk-bim360-projectuser
- name: Role
  property_count: 7
  slug: autodesk-bim360-role
- name: User
  property_count: 27
  slug: autodesk-bim360-user
jsonld:
- class_count: 23
  name: Autodesk Bim360 Context
  property_count: 38
  slug: autodesk-bim360-context
layout: provider
modified: '2026-06-13'
name: Autodesk BIM 360
nav: Providers
network: true
overview: 'Autodesk BIM 360 publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account Users API, Business Units API, Companies API, and 11 more. Tagged areas include Construction, Project Management, BIM, Document Management, and Field Management.


  The Autodesk BIM 360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Autodesk BIM 360''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Autodesk Bim360 Plans Pricing
  plan_count: 4
  slug: autodesk-bim360-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Autodesk Bim360 Rate Limits
  slug: autodesk-bim360-rate-limits
rules:
- name: Autodesk BIM 360 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: autodesk-bim360-jsonschema-spectral-rules
scopes:
- name: Autodesk Bim360 Scopes
  scope_count: 17
  slug: autodesk-bim360-scopes
  summary_line: 17 scopes · clientCredentials/implicit/authorizationCode
score:
  band: developing
  composite: 52.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 52.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autodesk-bim360/refs/heads/main/screenshots/autodesk-bim360-2026-06-20T172629.png
security:
- kind: authentication
  name: Autodesk Bim360 Authentication
  slug: autodesk-bim360-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Autodesk Bim360 Domain Security
  slug: autodesk-bim360-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: autodesk-bim360
tags:
- Construction
- Project Management
- BIM
- Document Management
- Field Management
- Issues Tracking
- Cost Management
- Model Coordination
- RFIs
- Checklists
website: https://construction.autodesk.com/products/autodesk-bim-360/
---
