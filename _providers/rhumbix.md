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
    agent_skills: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-08-10'
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
artifact_total: 5
common:
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
modified: '2026-07-21'
name: Rhumbix
nav: Providers
network: true
overview: 'Rhumbix publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Export API, Batch Import API, and CORS API. Tagged areas include Company, Applications, Construction, Construction Technology, and Workforce Management.


  Rhumbix''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 71
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.8
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 41.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
