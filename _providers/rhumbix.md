---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://async-api.rhumbix.com
  baseurl_source: declared
  description: Export Data from Rhumbix
  name: Rhumbix Batch Export API
  slug: rhumbix-batch-export-api
- baseURL: https://async-api.rhumbix.com
  baseurl_source: declared
  description: Import Data into Rhumbix
  name: Rhumbix Batch Import API
  slug: rhumbix-batch-import-api
- baseURL: https://async-api.rhumbix.com
  baseurl_source: declared
  description: Returns appropriate headers to enable CORS for cross-domain API requests
  name: Rhumbix CORS API
  slug: rhumbix-cors-api
artifact_total: 9
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: Rhumbix
nav: Providers
network: true
overview: 'Rhumbix publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch Export API, Batch Import API, and CORS API. Tagged areas include Company, Application, Construction, Construction Technology, and Workforce Management.


  Rhumbix''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 50.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rhumbix/refs/heads/main/screenshots/rhumbix-2026-09-02T153759.png
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
- Application
- Construction
- Construction Technology
- Workforce Management
- Timekeeping
- Payroll
- Field Data Collection
- Project Management
- Job Costing
- Integration
- REST API
website: https://www.rhumbix.com
---
