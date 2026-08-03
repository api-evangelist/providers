---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Kenjo Agentic Access
  operation_count: 80
  slug: kenjo-agentic-access
  summary_line: 80 operations · 38 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Attendance and time-tracking entries.
  name: Kenjo Attendance API
  slug: kenjo-attendance-api
- description: Exchange an API key for a bearer token and invalidate tokens.
  name: Kenjo Authentication API
  slug: kenjo-authentication-api
- description: Contracts, salaries, and additional payments.
  name: Kenjo Compensation API
  slug: kenjo-compensation-api
- description: Company documents.
  name: Kenjo Documents API
  slug: kenjo-documents-api
- description: Employee records and their profile sections.
  name: Kenjo Employees API
  slug: kenjo-employees-api
- description: Companies, offices, departments, teams, areas, and calendars.
  name: Kenjo Organization API
  slug: kenjo-organization-api
- description: Positions, candidates, and applications.
  name: Kenjo Recruiting API
  slug: kenjo-recruiting-api
- description: Absences, time-off requests, types, statuses, and balances.
  name: Kenjo Time Off API
  slug: kenjo-time-off-api
artifact_total: 13
collections:
- collection_type: open
  name: Kenjo API
  slug: open-kenjo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kenjo-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kenjohr
- group: company
  title: ''
  type: Website
  url: https://www.kenjo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kenjo.readme.io/reference
- group: operate
  title: ''
  type: SupportEmail
  url: mailto:support@kenjo.io
- group: commercial
  title: ''
  type: Plans
  url: plans/kenjo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kenjo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kenjo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kenjo.io/blog
created: '2026-07-11'
description: Kenjo is an all-in-one human resources (HRIS) software platform for small and mid-sized companies, with a strong focus on deskless and shift-based teams. It covers the full employee lifecycle - employee database, attendance and time tracking, absence and time-off management, document management, payroll and compensation, shift planning, performance reviews, and recruiting. Kenjo exposes a documented REST API (base https://api.kenjo.io/api/v1, sandbox https://sandbox-api.kenjo.io/api/v1) that lets customers read and write employees, attendances, time-off requests, company documents, compensation, org structure, and recruiting data. API access is gated - it is available on Kenjo's top-tier Connect plan and must be activated by the Kenjo Customer Success team, then keys are generated in Settings > Integrations > API and exchanged for a bearer token.
finops:
- name: Kenjo Finops
  service_category: Human Resources Software
  slug: kenjo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kenjo.png
layout: provider
modified: '2026-07-11'
name: Kenjo
nav: Providers
network: true
overview: 'Kenjo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Attendance API, Authentication API, Compensation API, and 5 more. Tagged areas include Human Resources, HRIS, Employee Management, HR Software, and Time Tracking.


  Kenjo''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Kenjo Plans Pricing
  plan_count: 3
  slug: kenjo-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Kenjo Rate Limits
  slug: kenjo-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kenjo/refs/heads/main/screenshots/kenjo-2026-07-25T223611.png
slug: kenjo
tags:
- Human Resources
- HRIS
- Employee Management
- HR Software
- Time Tracking
- Absence Management
- Payroll
- Recruiting
website: https://www.kenjo.io/
---
