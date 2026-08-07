---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Hubstaff Agentic Access
  operation_count: 62
  slug: hubstaff-agentic-access
  summary_line: 62 operations · 22 acting
api_count: 19
apis:
- description: Tracked time as 10-minute activity blocks and daily aggregates, with keyboard/mouse activity percentages.
  name: Hubstaff Activities API
  slug: hubstaff-activities-api
- description: Application and URL usage captured while tracking, plus tracking settings.
  name: Hubstaff App & URL Tracking API
  slug: hubstaff-app-url-tracking-api
- description: Expected work shifts (schedules), actual clock-in/clock-out shifts, and holidays.
  name: Hubstaff Attendance API
  slug: hubstaff-attendance-api
- description: Invoices issued to clients.
  name: Hubstaff Client Invoices API
  slug: hubstaff-client-invoices-api
- description: Clients that projects are billed to.
  name: Hubstaff Clients API
  slug: hubstaff-clients-api
- description: Invite users to an organization.
  name: Hubstaff Invites API
  slug: hubstaff-invites-api
- description: Organization membership - list, add, and update members and their pay/bill rates.
  name: Hubstaff Members API
  slug: hubstaff-members-api
- description: Organizations the authenticated user belongs to, plus seat usage.
  name: Hubstaff Organizations API
  slug: hubstaff-organizations-api
- description: Projects within an organization, including budgets and project members.
  name: Hubstaff Projects API
  slug: hubstaff-projects-api
- description: Screenshots captured while tracking time.
  name: Hubstaff Screenshots API
  slug: hubstaff-screenshots-api
- description: Tasks (to-dos) within projects and organizations.
  name: Hubstaff Tasks API
  slug: hubstaff-tasks-api
- description: Payments made to team members (payroll).
  name: Hubstaff Team Payments API
  slug: hubstaff-team-payments-api
- description: Teams within an organization and their membership.
  name: Hubstaff Teams API
  slug: hubstaff-teams-api
- description: Audit trail of manual time edits.
  name: Hubstaff Time Edit Logs API
  slug: hubstaff-time-edit-logs-api
- description: Create time entries for a user (manual time via the API).
  name: Hubstaff Time Entries API
  slug: hubstaff-time-entries-api
- description: Time off requests, policies, and balances.
  name: Hubstaff Time Off API
  slug: hubstaff-time-off-api
- description: Timesheet approval records - list and update status (open, submitted, approved, denied).
  name: Hubstaff Timesheets API
  slug: hubstaff-timesheets-api
- description: The authenticated user and user profiles.
  name: Hubstaff Users API
  slug: hubstaff-users-api
- description: Webhook subscriptions delivering real-time event notifications (timer.start, timer.stop, task.create, shift.late, etc.).
  name: Hubstaff Webhooks API
  slug: hubstaff-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: Hubstaff API
  slug: open-hubstaff
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hubstaff-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hubstaff-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubstaff-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hubstaff-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NetsoftHoldings
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hubstaff
- group: company
  title: ''
  type: Website
  url: https://hubstaff.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hubstaff.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://hubstaff.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.hubstaff.com/
- group: company
  title: ''
  type: Blog
  url: https://hubstaff.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/hubstaff-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hubstaff-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hubstaff-finops.yml
created: '2026-07-11'
description: Hubstaff is a time tracking and workforce analytics platform for remote, hybrid, and field teams. The Hubstaff API v2 provides read and write access to tracked time (10-minute activity blocks and daily aggregates), time entries, timesheets and approvals, time off, attendance schedules and shifts, organizations, members, teams, projects, tasks, clients, invoices, team payments, screenshots, app and URL usage, and webhooks - authenticated with OAuth 2.0 / OpenID Connect or personal access tokens.
finops:
- name: Hubstaff Finops
  service_category: Business Applications
  slug: hubstaff-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hubstaff.png
layout: provider
modified: '2026-07-11'
name: Hubstaff
nav: Providers
network: true
overview: 'Hubstaff publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Activities API, App & URL Tracking API, Attendance API, and 16 more. Tagged areas include Time Tracking, Timesheets, Workforce Management, Productivity, and Employee Monitoring.


  Hubstaff''s developer surface includes authentication, documentation, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Hubstaff Plans Pricing
  plan_count: 6
  slug: hubstaff-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 4
  name: Hubstaff Rate Limits
  slug: hubstaff-rate-limits
score:
  band: developing
  composite: 43.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hubstaff/refs/heads/main/screenshots/hubstaff-2026-07-25T221622.png
security:
- kind: authentication
  name: Hubstaff Authentication
  slug: hubstaff-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hubstaff Domain Security
  slug: hubstaff-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hubstaff Vulnerability Disclosure
  slug: hubstaff-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hubstaff
tags:
- Time Tracking
- Timesheets
- Workforce Management
- Productivity
- Employee Monitoring
- Project Management
- Payroll
website: https://hubstaff.com
---
