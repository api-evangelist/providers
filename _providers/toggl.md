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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Toggl Agentic Access
  operation_count: 10
  slug: toggl-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: 'Current REST API for managing time entries, workspaces, projects, clients, tags, tasks, users, and organizations in Toggl Track. Authentication uses HTTP Basic Auth with the API token as username and '
  name: Toggl Track API v9
  slug: track-api-v9
- description: Reporting API for generating detailed, summary, and weekly reports across time entries, with support for filtering, grouping, and export formats (JSON, CSV, PDF).
  name: Toggl Track Reports API v3
  slug: reports-api-v3
- description: Webhooks API for subscribing to events such as time entry creation, updates, deletions, and project changes within a workspace.
  name: Toggl Track Webhooks API
  slug: webhooks-api
- description: The Me API from Toggl Track — 1 operation(s) for me.
  name: Toggl Track Me API
  slug: toggl-me-api
- description: The Reports API from Toggl Track — 3 operation(s) for reports.
  name: Toggl Track Reports API
  slug: toggl-reports-api
- description: The Time Entries API from Toggl Track — 5 operation(s) for time entries.
  name: Toggl Track Time Entries API
  slug: toggl-time-entries-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toggl Track Me API
  slug: open-toggl-me-api
- collection_type: open
  name: Toggl Track Me Reports API
  slug: open-toggl-reports-api
- collection_type: open
  name: Toggl Track Me Time Entries API
  slug: open-toggl-time-entries-api
- collection_type: open
  name: Toggl Track API
  slug: open-toggl
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toggl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toggl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toggl-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toggl
- group: company
  title: ''
  type: Website
  url: https://toggl.com/track/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://engineering.toggl.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://engineering.toggl.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://toggl.com/track/pricing/
- group: start
  title: ''
  type: Signup
  url: https://toggl.com/track/signup/
- group: start
  title: ''
  type: Login
  url: https://track.toggl.com/login
- group: company
  title: ''
  type: Blog
  url: https://toggl.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.toggl.com/en/
- group: operate
  title: ''
  type: Community
  url: https://community.toggl.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/toggl
- group: operate
  title: ''
  type: StatusPage
  url: https://status.toggl.com/
created: '2026-05-11'
description: Toggl Track is a time-tracking and productivity platform for freelancers, teams, and agencies that captures billable hours, project time, and team capacity across web, desktop, mobile, and browser extension clients. The product offers automated tracking, calendar integration, custom reporting, 100+ integrations (Jira, Salesforce, Asana, GitHub), and supports billing, payroll, and project profitability use cases. The Toggl Track API v9 is a REST interface for time entries, workspaces, projects, clients, users, and reports using HTTP Basic Authentication with an API token.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toggl.png
layout: provider
modified: '2026-05-11'
name: Toggl Track
nav: Providers
network: true
overview: 'Toggl Track publishes 3 APIs on the [APIs.io](https://apis.io/) network: Me API, Reports API, and Time Entries API. Tagged areas include Time Tracking, Productivity, Project Management, Billing, and Reporting.


  Toggl Track''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 9 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 34.8
  delta: 1.4
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toggl/refs/heads/main/screenshots/toggl-2026-06-20T195434.png
security:
- kind: authentication
  name: Toggl Authentication
  slug: toggl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Toggl Domain Security
  slug: toggl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: toggl
tags:
- Time Tracking
- Productivity
- Project Management
- Billing
- Reporting
- Workforce Management
website: https://toggl.com/track/
---
