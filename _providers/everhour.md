---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Everhour Agentic Access
  operation_count: 88
  slug: everhour-agentic-access
  summary_line: 88 operations · 54 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Clients and client budgets.
  name: Everhour Clients API
  slug: everhour-clients-api
- description: Expenses, expense categories, and attachments.
  name: Everhour Expenses API
  slug: everhour-expenses-api
- description: Invoices generated from tracked time and expenses.
  name: Everhour Invoices API
  slug: everhour-invoices-api
- description: Projects, sections, billing, budgets, and integration sync.
  name: Everhour Projects API
  slug: everhour-projects-api
- description: Dashboard reports for projects, clients, and users.
  name: Everhour Reports API
  slug: everhour-reports-api
- description: Resource planner assignments.
  name: Everhour Schedule API
  slug: everhour-schedule-api
- description: Tasks, task search, and task estimates.
  name: Everhour Tasks API
  slug: everhour-tasks-api
- description: Time off types and allocations.
  name: Everhour Time Off API
  slug: everhour-time-off-api
- description: Reported time records for the team, users, tasks, and projects.
  name: Everhour Time Records API
  slug: everhour-time-records-api
- description: Clock-in/clock-out attendance timecards.
  name: Everhour Timecards API
  slug: everhour-timecards-api
- description: Start, inspect, and stop running timers.
  name: Everhour Timers API
  slug: everhour-timers-api
- description: Weekly timesheets and the timesheet approval workflow.
  name: Everhour Timesheets API
  slug: everhour-timesheets-api
- description: Current user and team members.
  name: Everhour Users API
  slug: everhour-users-api
- description: Webhook subscriptions for resource change events.
  name: Everhour Webhooks API
  slug: everhour-webhooks-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Everhour Clients API
  slug: open-everhour-clients-api
- collection_type: open
  name: Everhour Clients Expenses API
  slug: open-everhour-expenses-api
- collection_type: open
  name: Everhour Clients Invoices API
  slug: open-everhour-invoices-api
- collection_type: open
  name: Everhour Clients Projects API
  slug: open-everhour-projects-api
- collection_type: open
  name: Everhour Clients Reports API
  slug: open-everhour-reports-api
- collection_type: open
  name: Everhour Clients Schedule API
  slug: open-everhour-schedule-api
- collection_type: open
  name: Everhour Clients Tasks API
  slug: open-everhour-tasks-api
- collection_type: open
  name: Everhour Clients Time Off API
  slug: open-everhour-time-off-api
- collection_type: open
  name: Everhour Clients Time Records API
  slug: open-everhour-time-records-api
- collection_type: open
  name: Everhour Clients Timecards API
  slug: open-everhour-timecards-api
- collection_type: open
  name: Everhour Clients Timers API
  slug: open-everhour-timers-api
- collection_type: open
  name: Everhour Clients Timesheets API
  slug: open-everhour-timesheets-api
- collection_type: open
  name: Everhour Clients Users API
  slug: open-everhour-users-api
- collection_type: open
  name: Everhour Clients Webhooks API
  slug: open-everhour-webhooks-api
- collection_type: open
  name: Everhour API
  slug: open-everhour
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/everhour-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/everhour-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/everhour-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/everhour-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://everhour.com
- group: docs
  title: ''
  type: Documentation
  url: https://everhour.docs.apiary.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/everhour
- group: commercial
  title: ''
  type: Pricing
  url: https://everhour.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://everhour.com/blog/
- group: commercial
  title: ''
  type: Plans
  url: plans/everhour-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/everhour-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/everhour-finops.yml
created: '2026-07-11'
description: Everhour is a time tracking and budgeting platform for teams that embeds timers and timesheets directly inside the project management tools teams already use - Asana, Trello, ClickUp, Jira, GitHub, Basecamp, Notion, Monday, Linear, and more. The Everhour REST API (api.everhour.com, X-Api-Key auth) gives programmatic access to time records, running timers, weekly timesheets and approvals, clock-in/clock-out timecards, projects and tasks, clients, invoices, expenses, resource scheduling, time off, and reporting dashboards, plus webhooks for time, timer, task, and project change events.
finops:
- name: Everhour Finops
  service_category: Business Applications
  slug: everhour-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/everhour.png
layout: provider
modified: '2026-07-11'
name: Everhour
nav: Providers
network: true
overview: 'Everhour publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Expenses API, Invoices API, and 11 more. Tagged areas include Time Tracking, Timesheets, Productivity, Project Management, and Budgeting.


  Everhour''s developer surface includes authentication, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Everhour Plans Pricing
  plan_count: 3
  slug: everhour-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Everhour Rate Limits
  slug: everhour-rate-limits
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 60.5
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/everhour/refs/heads/main/screenshots/everhour-2026-07-25T213727.png
security:
- kind: authentication
  name: Everhour Authentication
  slug: everhour-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Everhour Domain Security
  slug: everhour-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Everhour Trust Center
  slug: everhour-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: everhour
tags:
- Time Tracking
- Timesheets
- Productivity
- Project Management
- Budgeting
- Invoicing
website: https://everhour.com
---
