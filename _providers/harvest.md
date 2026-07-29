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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 31
  human_in_the_loop: 2
  name: Harvest Agentic Access
  operation_count: 55
  slug: harvest-agentic-access
  summary_line: 55 operations · 31 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: REST API for managing clients, projects, tasks, time entries, expenses, invoices, estimates, and users in Harvest. Supports OAuth 2.0 and Personal Access Token authentication, requires a Harvest-Accou
  name: Harvest API v2
  slug: api-v2
- description: The Clients API from Harvest — 2 operation(s) for clients.
  name: Harvest Clients API
  slug: harvest-clients-api
- description: The Company API from Harvest — 1 operation(s) for company.
  name: Harvest Company API
  slug: harvest-company-api
- description: The Estimates API from Harvest — 2 operation(s) for estimates.
  name: Harvest Estimates API
  slug: harvest-estimates-api
- description: The Expenses API from Harvest — 2 operation(s) for expenses.
  name: Harvest Expenses API
  slug: harvest-expenses-api
- description: The Invoices API from Harvest — 2 operation(s) for invoices.
  name: Harvest Invoices API
  slug: harvest-invoices-api
- description: The Projects API from Harvest — 2 operation(s) for projects.
  name: Harvest Projects API
  slug: harvest-projects-api
- description: The Reports API from Harvest — 4 operation(s) for reports.
  name: Harvest Reports API
  slug: harvest-reports-api
- description: The Roles API from Harvest — 2 operation(s) for roles.
  name: Harvest Roles API
  slug: harvest-roles-api
- description: The Tasks API from Harvest — 2 operation(s) for tasks.
  name: Harvest Tasks API
  slug: harvest-tasks-api
- description: The TimeEntries API from Harvest — 5 operation(s) for timeentries.
  name: Harvest TimeEntries API
  slug: harvest-timeentries-api
- description: The Users API from Harvest — 3 operation(s) for users.
  name: Harvest Users API
  slug: harvest-users-api
artifact_total: 18
collections:
- collection_type: open
  name: Harvest API v2
  slug: open-harvest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/harvest-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/harvest-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/harvest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harvest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harvest-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.getharvest.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.getharvest.com/api-v2/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getharvest.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://id.getharvest.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.getharvest.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.getharvest.com
- group: operate
  title: ''
  type: StatusPage
  url: https://www.harveststatus.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harvesthq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/harvest
created: '2026-05-11'
description: Harvest is a cloud-based time tracking, project management, expense tracking, and invoicing platform used by agencies, consultancies, and professional services teams to track billable hours, manage budgets, and bill clients. The platform provides reporting on team utilization, project profitability, and budget burn, and integrates with tools like Asana, Trello, Slack, and QuickBooks. Harvest's REST API v2 provides full programmatic access to clients, projects, tasks, time entries, expenses, invoices, estimates, and users using OAuth 2.0 or Personal Access Token authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/harvest.png
layout: provider
modified: '2026-05-11'
name: Harvest
nav: Providers
network: true
overview: 'Harvest publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Company API, Estimates API, and 8 more. Tagged areas include Time Tracking, Project Management, Invoicing, Expense Tracking, and Timesheets.


  Harvest''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 8 more developer resources.'
random_paper: 36
score:
  band: thin
  composite: 32.4
  delta: -2.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harvest/refs/heads/main/screenshots/harvest-2026-06-20T182526.png
security:
- kind: authentication
  name: Harvest Authentication
  slug: harvest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Harvest Domain Security
  slug: harvest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Harvest Vulnerability Disclosure
  slug: harvest-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Harvest Trust Center
  slug: harvest-trust-center
  summary_line: SOC 2, PCI DSS
slug: harvest
tags:
- Time Tracking
- Project Management
- Invoicing
- Expense Tracking
- Timesheets
- Professional Services
website: https://www.getharvest.com
---
