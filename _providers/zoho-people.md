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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Zoho People Agentic Access
  operation_count: 20
  slug: zoho-people-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 7
apis:
- description: Attendance entries, check-in / check-out, regularization.
  name: Zoho People Attendance API
  slug: zoho-people-attendance-api
- description: Workflow and automation triggers.
  name: Zoho People Automation API
  slug: zoho-people-automation-api
- description: Dashboard data reads for analytics widgets.
  name: Zoho People Dashboard API
  slug: zoho-people-dashboard-api
- description: Employee record CRUD across the People HRIS.
  name: Zoho People Employee API
  slug: zoho-people-employee-api
- description: Custom and standard form record operations.
  name: Zoho People Forms API
  slug: zoho-people-forms-api
- description: Leave types, balances, and request lifecycle.
  name: Zoho People Leave API
  slug: zoho-people-leave-api
- description: Projects, jobs, and timesheet entries.
  name: Zoho People Time Tracker API
  slug: zoho-people-time-tracker-api
artifact_total: 30
collections:
- collection_type: open
  name: Zoho People REST API
  slug: open-zoho-people
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-people-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-people-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-people-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-people-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-people-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/people/
- group: other
  title: ''
  type: ProductOverview
  url: https://www.zoho.com/people/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/people/api/overview.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.zoho.com/portal/en/kb/people
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/people/zohopeople-pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/people/signup.html
- group: start
  title: ''
  type: Login
  url: https://people.zoho.com/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/people/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: operate
  title: ''
  type: StatusPageRSS
  url: https://status.zoho.com/rss
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: other
  title: ''
  type: ZohoOneSuite
  url: https://www.zoho.com/one/
- group: operate
  title: ''
  type: Community
  url: https://help.zoho.com/portal/en/community/zoho-people
created: '2026-05-23'
description: Zoho People is Zoho's cloud-based, AI-first HR management system (HRMS) spanning core HR, time and attendance, leave, performance, learning, recruitment, payroll and analytics — bundled inside the Zoho One business suite. The Zoho People REST API exposes employee records, custom forms, leave, attendance, time tracking, automation, and dashboard data in XML or JSON, secured with Zoho OAuth 2.0 via the Zoho Accounts service and the seven `ZOHOPEOPLE` scopes (employee, forms, dashboard, automation, timetracker, attendance, leave).
examples:
- key_count: 3
  name: Apply For Leave Example
  slug: apply-for-leave-example
- key_count: 3
  name: Check In Out Example
  slug: check-in-out-example
- key_count: 3
  name: Create Time Log Example
  slug: create-time-log-example
- key_count: 3
  name: List Employees Example
  slug: list-employees-example
- key_count: 3
  name: List Leave Types Example
  slug: list-leave-types-example
- key_count: 3
  name: Trigger Workflow Example
  slug: trigger-workflow-example
finops:
- name: Zoho People Finops
  service_category: ''
  slug: zoho-people-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-people.png
json_schemas:
- name: ZohoPeopleAttendanceEntry
  property_count: 7
  slug: zoho-people-attendance-entry
- name: ZohoPeopleEmployee
  property_count: 14
  slug: zoho-people-employee
- name: ZohoPeopleLeaveRequest
  property_count: 7
  slug: zoho-people-leave-request
- name: ZohoPeopleLeaveType
  property_count: 7
  slug: zoho-people-leave-type
- name: ZohoPeopleTimeLog
  property_count: 7
  slug: zoho-people-time-log
jsonld:
- class_count: 27
  name: Zoho People Context
  property_count: 8
  slug: zoho-people-context
layout: provider
modified: '2026-05-23'
name: Zoho People
nav: Providers
network: true
overview: 'Zoho People publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Attendance API, Automation API, Dashboard API, and 4 more. Tagged areas include HR, HRMS, Human Resources, HRIS, and Employee Management.


  The Zoho People catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Zoho People''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 13 more developer resources.'
plans:
- name: Zoho People Plans Pricing
  plan_count: 5
  slug: zoho-people-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Zoho People Rate Limits
  slug: zoho-people-rate-limits
rules:
- name: Zoho People API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zoho-people-jsonschema-spectral-rules
- name: Zoho People API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: zoho-people-rules
scopes:
- name: Zoho People Scopes
  scope_count: 13
  slug: zoho-people-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 59.2
    developer_ergonomics: 26.1
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 51.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-people/refs/heads/main/screenshots/zoho-people-2026-06-20T201945.png
security:
- kind: authentication
  name: Zoho People Authentication
  slug: zoho-people-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho People Domain Security
  slug: zoho-people-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho People Vulnerability Disclosure
  slug: zoho-people-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-people
tags:
- HR
- HRMS
- Human Resources
- HRIS
- Employee Management
- Attendance
- Leave Management
- Time Tracking
- Performance Management
- Onboarding
- Zoho
- OAuth 2.0
website: https://www.zoho.com/people/
---
