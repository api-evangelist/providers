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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Kenjo Agentic Access
  operation_count: 80
  slug: kenjo-agentic-access
  summary_line: 80 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Attendance and time-tracking entries.
  name: Kenjo Attendance API
  slug: kenjo-attendance-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Exchange an API key for a bearer token and invalidate tokens.
  name: Kenjo Authentication API
  slug: kenjo-authentication-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Contracts, salaries, and additional payments.
  name: Kenjo Compensation API
  slug: kenjo-compensation-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Company documents.
  name: Kenjo Documents API
  slug: kenjo-documents-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Employee records and their profile sections.
  name: Kenjo Employees API
  slug: kenjo-employees-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Companies, offices, departments, teams, areas, and calendars.
  name: Kenjo Organization API
  slug: kenjo-organization-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Positions, candidates, and applications.
  name: Kenjo Recruiting API
  slug: kenjo-recruiting-api
- baseURL: https://api.kenjo.io/api/v1
  baseurl_source: declared
  description: Absences, time-off requests, types, statuses, and balances.
  name: Kenjo Time Off API
  slug: kenjo-time-off-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kenjo Attendance API
  slug: open-kenjo-attendance-api
- collection_type: open
  name: Kenjo Attendance Authentication API
  slug: open-kenjo-authentication-api
- collection_type: open
  name: Kenjo Attendance Compensation API
  slug: open-kenjo-compensation-api
- collection_type: open
  name: Kenjo Attendance Documents API
  slug: open-kenjo-documents-api
- collection_type: open
  name: Kenjo Attendance Employees API
  slug: open-kenjo-employees-api
- collection_type: open
  name: Kenjo Attendance Organization API
  slug: open-kenjo-organization-api
- collection_type: open
  name: Kenjo Attendance Recruiting API
  slug: open-kenjo-recruiting-api
- collection_type: open
  name: Kenjo Attendance Time Off API
  slug: open-kenjo-time-off-api
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
random_paper: 10
rate_limits:
- limit_count: 3
  name: Kenjo Rate Limits
  slug: kenjo-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 16.8
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
