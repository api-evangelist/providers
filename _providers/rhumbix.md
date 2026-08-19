---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: Export Data from Rhumbix
  name: Rhumbix Batch Export API
  slug: rhumbix-batch-export-api
- description: Import Data into Rhumbix
  name: Rhumbix Batch Import API
  slug: rhumbix-batch-import-api
- description: Returns appropriate headers to enable CORS for cross-domain API requests
  name: Rhumbix CORS API
  slug: rhumbix-cors-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rhumbix Public Batch Export API
  slug: open-rhumbix-batch-export-api
- collection_type: open
  name: Rhumbix Public Batch Export Batch Import API
  slug: open-rhumbix-batch-import-api
- collection_type: open
  name: Rhumbix Public Batch Export CORS API
  slug: open-rhumbix-cors-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/rhumbix-export-workshifts.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rhumbix-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rhumbix-public-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.rhumbix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rhumbix.github.io/docs.rhumbix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rhumbix.github.io/docs.rhumbix.com/
- group: docs
  title: ''
  type: APIReference
  url: https://rhumbix.github.io/docs.rhumbix.com/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/rhumbix-helpcenter
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.rhumbix.com/resources/support
- group: company
  title: ''
  type: Blog
  url: https://www.rhumbix.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rhumbix
- group: operate
  title: ''
  type: StatusPage
  url: http://status.rhumbix.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rhumbix.com/pricing
- group: start
  title: ''
  type: Login
  url: https://platform.rhumbix.com/rhumbix/login/
- group: start
  title: ''
  type: SignUp
  url: https://go.rhumbix.com/scheduledemo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rhumbix.com/service_terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rhumbix.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rhumbix-domain-security.yml
created: '2026-07-17'
description: Rhumbix is a field-first workforce management platform for construction that consolidates timekeeping, production tracking, time & materials, change orders, daily field reports, and custom forms into real-time visibility on labor and job costs for trade contractors and general contractors. Rhumbix publishes a REST Public API (Swagger 2.0, x-api-key auth) for batch import of employees and projects and batch export of workshift/timecard data, enabling bidirectional flow between the field and ERP/accounting and project-management systems (Sage, Oracle, SAP, QuickBooks, Viewpoint, CMiC, Procore, Autodesk Construction Cloud). Autodesk has signed a definitive agreement to acquire Rhumbix.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rhumbix.png
layout: provider
mcp_servers:
- description: ''
  name: rhumbix-mcp.yml
  slug: rhumbix-mcpyml
modified: '2026-07-21'
name: Rhumbix
nav: Providers
network: true
overview: 'Rhumbix publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Export API, Batch Import API, and CORS API. Tagged areas include Company, Applications, Construction, Construction Technology, and Workforce Management.


  Rhumbix''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 41.4
  delta: -0.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 51.7
    developer_ergonomics: 35.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 41.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Rhumbix Authentication
  slug: rhumbix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rhumbix Domain Security
  slug: rhumbix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rhumbix
tags:
- Company
- Applications
- Construction
- Construction Technology
- Workforce Management
- Timekeeping
- Payroll
- Field Data Collection
- Project Management
- Job Costing
- Integrations
- REST API
website: https://www.rhumbix.com
---
