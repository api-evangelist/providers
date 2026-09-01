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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ukg Ready Agentic Access
  operation_count: 3
  slug: ukg-ready-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: RESTful API for UKG Ready providing programmatic access to employees, HR records, payroll, time and attendance, schedules, accruals, benefits, and workforce reporting. The base URL is per-tenant (http
  name: UKG Ready REST API
  slug: rest-api
- description: Access token issuance
  name: UKG Ready Authentication API
  slug: ukg-ready-authentication-api
- description: Tenant content and posts
  name: UKG Ready Content API
  slug: ukg-ready-content-api
- description: Workgroup and organizational unit management
  name: UKG Ready Groups API
  slug: ukg-ready-groups-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UKG Ready Authentication API
  slug: open-ukg-ready-authentication-api
- collection_type: open
  name: UKG Ready Authentication Content API
  slug: open-ukg-ready-content-api
- collection_type: open
  name: UKG Ready Authentication Groups API
  slug: open-ukg-ready-groups-api
- collection_type: open
  name: UKG Ready API
  slug: open-ukg-ready
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ukg-ready-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ukg-ready-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ukg-ready-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultimatesoftware
- group: company
  title: ''
  type: Website
  url: https://www.ukg.com/solutions/ukg-ready
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ukg.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ukg.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ukg.com/solutions/ukg-ready/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.ukg.com/contact
- group: operate
  title: ''
  type: Community
  url: https://community.ukg.com
- group: operate
  title: ''
  type: Support
  url: https://www.ukg.com/support
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ukg
created: '2026-05-11'
description: UKG Ready (formerly Kronos Workforce Ready) is UKG's unified Human Capital Management (HCM) suite for small and midmarket organizations, combining HR, payroll, talent management, benefits administration, time and attendance, scheduling, and compliance into a single cloud platform. UKG Ready exposes REST and GraphQL APIs (per-tenant host of the form https://{hostname}/api/...) using OAuth 2.0 authorization code flow with bearer tokens for managing employees, schedules, timekeeping, payroll, benefits, and workforce data.
graphqls:
- description: ''
  name: UKG Ready GraphQL API
  slug: ukg-ready-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ukg-ready.png
layout: provider
modified: '2026-05-11'
name: UKG Ready
nav: Providers
network: true
overview: 'UKG Ready publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Content API, and Groups API. Tagged areas include HCM, Payroll, Workforce Management, Time and Attendance, and HR.


  UKG Ready''s developer surface includes authentication, documentation, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ukg-ready/refs/heads/main/screenshots/ukg-ready-2026-06-20T200009.png
security:
- kind: authentication
  name: Ukg Ready Authentication
  slug: ukg-ready-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ukg Ready Domain Security
  slug: ukg-ready-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ukg-ready
tags:
- HCM
- Payroll
- Workforce Management
- Time and Attendance
- HR
- Benefits
website: https://www.ukg.com/solutions/ukg-ready
---
