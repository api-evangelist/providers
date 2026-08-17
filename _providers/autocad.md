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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.8
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: Core API for AutoCAD automation, drawing manipulation, and entity management.
  name: AutoCAD API
  slug: autocad-api
- description: Cloud-based API that enables running AutoCAD scripts, AutoLISP routines, and custom add-ins in the cloud to automate drawing creation, modification, and batch processing workflows at scale.
  name: AutoCAD Design Automation API
  slug: design-automation-api
- description: API for managing AutoCAD files, versions, and collaboration workflows.
  name: AutoCAD Data Management API
  slug: data-management-api
- description: API for translating AutoCAD design files into formats like SVF and SVF2 for rendering in the Viewer SDK, extracting metadata, object hierarchy, properties, and generating thumbnails.
  name: AutoCAD Model Derivative API
  slug: model-derivative-api
- description: API enabling applications to listen for and receive notifications when specific events occur in AutoCAD data and workflows, supporting event-driven architectures.
  name: AutoCAD Webhooks API
  slug: webhooks-api
- description: OAuth 2.0-based authentication API for securing access to AutoCAD and Autodesk Platform Services APIs, supporting both 2-legged and 3-legged authentication workflows.
  name: AutoCAD Authentication API
  slug: authentication-api
artifact_total: 36
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autocad-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/autocad-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/autocad-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/autocad-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/autocad-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/autocad-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autocad-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/autocad-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autocad-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autocad-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autocad-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autocad-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/autocad-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/autocad-components.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/autodesk-platform-services/skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/autodeskautocad
- group: start
  title: ''
  type: Portal
  url: https://aps.autodesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aps.autodesk.com/developer/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://tutorials.autodesk.io/
- group: auth
  title: ''
  type: Authentication
  url: https://forge.autodesk.com/en/docs/oauth/v2/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/autodesk-platform-services/aps-sdk-node
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/autodesk-platform-services/aps-sdk-net
- group: company
  title: ''
  type: Blog
  url: https://aps.autodesk.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autodesk-platform-services
- group: operate
  title: ''
  type: Support
  url: https://forge.autodesk.com/en/support/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/autodesk-forge
- group: start
  title: ''
  type: Signup
  url: https://aps.autodesk.com/
- group: start
  title: ''
  type: Login
  url: https://manage.autodesk.com/home
- group: commercial
  title: ''
  type: Pricing
  url: https://aps.autodesk.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://health.autodesk.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/forge-platform-web-services-api-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
- group: operate
  title: ''
  type: ChangeLog
  url: https://aps.autodesk.com/topics/product-updates
- group: build
  title: ''
  type: CodeExamples
  url: https://aps.autodesk.com/code-samples
created: '2024-01-01'
description: APIs for Autodesk AutoCAD, providing programmatic access to CAD design, drawing, and automation capabilities through Autodesk Platform Services (APS, formerly Forge) and desktop development environments including AutoLISP, ObjectARX, .NET, and JavaScript.
features:
- description: Run AutoCAD scripts and add-ins in the cloud for batch processing without local AutoCAD installation.
  name: Cloud-Based Design Automation
- description: Translate CAD files between formats and extract metadata for web-based viewing and analysis.
  name: 3D Model Translation
- description: Manage design file versions, revisions, and collaboration workflows through the Data Management API.
  name: File Version Management
- description: Receive real-time notifications when design files are created, updated, or shared.
  name: Event-Driven Webhooks
- description: Secure API access with 2-legged and 3-legged OAuth flows for application and user-level authorization.
  name: OAuth 2.0 Authentication
- description: Embed 2D and 3D design viewers in web applications with the Viewer SDK.
  name: Web-Based Viewer
finops:
- name: Autocad Finops
  service_category: API
  slug: autocad-finops
image: /assets/icons/autocad.png
integrations:
- description: Integration with ACC for construction project management and design coordination.
  name: Autodesk Construction Cloud
- description: Cloud-based BIM collaboration platform integration for construction workflows.
  name: BIM 360
- description: Interoperability with Revit for architectural design and BIM workflows.
  name: Revit
- description: Integration for 3D coordination, clash detection, and project review.
  name: Navisworks
- description: Data visualization integration for design analytics and project reporting.
  name: Power BI
layout: provider
mcp_servers:
- description: ''
  name: autocad-mcp.yml
  slug: autocad-mcpyml
modified: '2026-06-20'
name: AutoCAD
nav: Providers
network: true
overview: 'AutoCAD publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Modeling, Architecture, CAD, Design, and Drawing.


  AutoCAD''s developer surface includes authentication, changelog, developer portal, documentation, getting-started guide, engineering blog, support, and 27 more developer resources.'
plans:
- name: Autocad Plans Pricing
  plan_count: 3
  slug: autocad-plans-pricing
random_paper: 141
rate_limits:
- limit_count: 5
  name: Autocad Rate Limits
  slug: autocad-rate-limits
scopes:
- name: Autocad Scopes
  scope_count: 16
  slug: autocad-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 44.5
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 44.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autocad/refs/heads/main/screenshots/autocad-2026-06-20T172619.png
security:
- kind: authentication
  name: Autocad Authentication
  slug: autocad-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Autocad Domain Security
  slug: autocad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Autocad Vulnerability Disclosure
  slug: autocad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Autocad Trust Center
  slug: autocad-trust-center
  summary_line: SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, FedRAMP, CSA STAR Level 1
skill_count: 5
skills:
- name: acad-arx-wizard
  slug: acad-arx-wizard
- name: acad-cuix-builder
  slug: acad-cuix-builder
- name: acad-dotnet
  slug: acad-dotnet
- name: aps-docs-portal
  slug: aps-docs-portal
- name: aps-mcp-server-gen
  slug: aps-mcp-server-gen
slug: autocad
tags:
- 3D Modeling
- Architecture
- CAD
- Design
- Drawing
- Engineering
use_cases:
- description: Generate construction drawings, floor plans, and engineering diagrams automatically using Design Automation API.
  name: Automated Drawing Generation
- description: Build collaborative design workflows with file sharing, version control, and real-time notifications.
  name: Design File Collaboration
- description: Process thousands of CAD files in the cloud for format conversion, data extraction, and quality checks.
  name: Batch File Processing
- description: Integrate Building Information Modeling data with enterprise systems for construction project management.
  name: BIM Integration
- description: Build custom AutoCAD plugins and extensions using ObjectARX, .NET, AutoLISP, or JavaScript APIs.
  name: Custom CAD Applications
website: https://aps.autodesk.com/
---
