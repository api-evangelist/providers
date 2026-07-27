---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
- acting_count: 18
  human_in_the_loop: 0
  name: Sesame Hr Agentic Access
  operation_count: 33
  slug: sesame-hr-agentic-access
  summary_line: 33 operations · 18 acting
api_count: 7
apis:
- description: Vacation and absence calendars, day-off requests, holidays, and leave.
  name: Sesame HR Absences and Leave API
  slug: sesame-hr-absences-and-leave-api
- description: Departments, offices, and the organization chart.
  name: Sesame HR Departments and Org API
  slug: sesame-hr-departments-and-org-api
- description: Employee records and their manager relationships.
  name: Sesame HR Employees API
  slug: sesame-hr-employees-api
- description: Token and account metadata.
  name: Sesame HR Meta API
  slug: sesame-hr-meta-api
- description: Planners, shifts, and schedule templates.
  name: Sesame HR Scheduling API
  slug: sesame-hr-scheduling-api
- description: Clock in / out, work entries, and worked-hours analytics.
  name: Sesame HR Time Tracking API
  slug: sesame-hr-time-tracking-api
- description: Webhook subscription management.
  name: Sesame HR Webhooks API
  slug: sesame-hr-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Sesame HR Public API
  slug: open-sesame-hr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sesame-hr-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sesame-hr-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sesamehr
- group: company
  title: ''
  type: Website
  url: https://www.sesamehr.com
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.sesametime.com/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/sesame-hr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sesame-hr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sesame-hr-finops.yml
created: '2026-07-11'
description: Sesame HR is an all-in-one HR and time-tracking platform used by small and mid-sized companies across Spain, Latin America, and beyond to manage employees, time clock (check-in / check-out), work hours, shifts and scheduling, vacations, absences and leave, contracts, payroll data, and recruitment. The Sesame Public API (v3) exposes that same functionality over a documented REST interface authenticated with a Bearer API token, letting teams sync HRIS data with payroll and ERP systems, build custom dashboards, and automate onboarding, shift assignment, and absence-approval workflows.
finops:
- name: Sesame Hr Finops
  service_category: Human Resources and Workforce Management
  slug: sesame-hr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sesame-hr.png
layout: provider
modified: '2026-07-11'
name: Sesame HR
nav: Providers
network: true
overview: 'Sesame HR publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Absences and Leave API, Departments and Org API, Employees API, and 4 more. Tagged areas include Human Resources, HRIS, Time Tracking, Workforce Management, and Employee Management.


  Sesame HR''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Sesame Hr Plans Pricing
  plan_count: 4
  slug: sesame-hr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Sesame Hr Rate Limits
  slug: sesame-hr-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Sesame Hr Authentication
  slug: sesame-hr-authentication
  summary_line: http · 1 scheme
slug: sesame-hr
tags:
- Human Resources
- HRIS
- Time Tracking
- Workforce Management
- Employee Management
- HR
- Attendance
- Absence Management
- Scheduling
- Payroll
website: https://www.sesamehr.com
---
