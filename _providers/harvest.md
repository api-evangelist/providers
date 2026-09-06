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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 31
  human_in_the_loop: 2
  name: Harvest Agentic Access
  operation_count: 55
  slug: harvest-agentic-access
  summary_line: 55 operations · 31 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: REST API for managing clients, projects, tasks, time entries, expenses, invoices, estimates, and users in Harvest. Supports OAuth 2.0 and Personal Access Token authentication, requires a Harvest-Accou
  name: Harvest API v2
  slug: api-v2
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Clients API from Harvest — 2 operation(s) for clients.
  name: Harvest Clients API
  slug: harvest-clients-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Company API from Harvest — 1 operation(s) for company.
  name: Harvest Company API
  slug: harvest-company-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Estimates API from Harvest — 2 operation(s) for estimates.
  name: Harvest Estimates API
  slug: harvest-estimates-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Expenses API from Harvest — 2 operation(s) for expenses.
  name: Harvest Expenses API
  slug: harvest-expenses-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Invoices API from Harvest — 2 operation(s) for invoices.
  name: Harvest Invoices API
  slug: harvest-invoices-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Projects API from Harvest — 2 operation(s) for projects.
  name: Harvest Projects API
  slug: harvest-projects-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Reports API from Harvest — 4 operation(s) for reports.
  name: Harvest Reports API
  slug: harvest-reports-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Roles API from Harvest — 2 operation(s) for roles.
  name: Harvest Roles API
  slug: harvest-roles-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Tasks API from Harvest — 2 operation(s) for tasks.
  name: Harvest Tasks API
  slug: harvest-tasks-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The TimeEntries API from Harvest — 5 operation(s) for timeentries.
  name: Harvest TimeEntries API
  slug: harvest-timeentries-api
- baseURL: https://api.harvestapp.com/v2
  baseurl_source: declared
  description: The Users API from Harvest — 3 operation(s) for users.
  name: Harvest Users API
  slug: harvest-users-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Harvest API v2 Clients API
  slug: open-harvest-clients-api
- collection_type: open
  name: Harvest API v2 Clients Company API
  slug: open-harvest-company-api
- collection_type: open
  name: Harvest API v2 Clients Estimates API
  slug: open-harvest-estimates-api
- collection_type: open
  name: Harvest API v2 Clients Expenses API
  slug: open-harvest-expenses-api
- collection_type: open
  name: Harvest API v2 Clients Invoices API
  slug: open-harvest-invoices-api
- collection_type: open
  name: Harvest API v2 Clients Projects API
  slug: open-harvest-projects-api
- collection_type: open
  name: Harvest API v2 Clients Reports API
  slug: open-harvest-reports-api
- collection_type: open
  name: Harvest API v2 Clients Roles API
  slug: open-harvest-roles-api
- collection_type: open
  name: Harvest API v2 Clients Tasks API
  slug: open-harvest-tasks-api
- collection_type: open
  name: Harvest API v2 Clients TimeEntries API
  slug: open-harvest-timeentries-api
- collection_type: open
  name: Harvest API v2 Clients Users API
  slug: open-harvest-users-api
- collection_type: open
  name: Harvest API v2
  slug: open-harvest
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/harvest-capability-edges.yml
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


  Harvest''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, support, and 9 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 34.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
