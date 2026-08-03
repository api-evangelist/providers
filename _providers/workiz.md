---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- acting_count: 7
  human_in_the_loop: 0
  name: Workiz Agentic Access
  operation_count: 15
  slug: workiz-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 5
apis:
- description: Work orders - the core scheduling and dispatch entity in Workiz.
  name: Workiz Jobs API
  slug: workiz-jobs-api
- description: Prospective work that can be converted into jobs.
  name: Workiz Leads API
  slug: workiz-leads-api
- description: Payments recorded against a job.
  name: Workiz Payments API
  slug: workiz-payments-api
- description: Users - technicians, dispatchers, and office staff.
  name: Workiz Team API
  slug: workiz-team-api
- description: Technician time-off records that affect availability.
  name: Workiz Time Off API
  slug: workiz-time-off-api
artifact_total: 11
collections:
- collection_type: open
  name: Workiz API
  slug: open-workiz
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workiz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workiz-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.workiz.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/workiz
- group: company
  title: ''
  type: Website
  url: https://www.workiz.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.workiz.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/workiz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/workiz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/workiz-finops.yml
created: '2026-07-03'
description: Workiz is field service management (FSM) software for home-service businesses - HVAC, plumbing, electrical, appliance repair, garage doors, locksmiths, carpet cleaning, and similar trades. It combines scheduling and dispatch, a CRM, jobs and leads, estimates and invoicing, payments, and communications (calls, SMS, email) in one platform. Workiz exposes a documented REST API (the Developer API add-on) for reading and writing jobs, leads, team members, time off, and payments, plus outbound webhooks for new-job and new-lead events. All calls are made to https://api.workiz.com/api/v1/ with the account API token embedded in the request path.
finops:
- name: Workiz Finops
  service_category: Business Application Software
  slug: workiz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workiz.png
layout: provider
modified: '2026-07-03'
name: Workiz
nav: Providers
network: true
overview: 'Workiz publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Jobs API, Leads API, Payments API, and 2 more. Tagged areas include Field Service Management, FSM, Home Services, Scheduling, and Dispatch.


  Workiz''s developer surface includes engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Workiz Plans Pricing
  plan_count: 4
  slug: workiz-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Workiz Rate Limits
  slug: workiz-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Workiz Domain Security
  slug: workiz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workiz
tags:
- Field Service Management
- FSM
- Home Services
- Scheduling
- Dispatch
- CRM
- Jobs
- Invoicing
website: https://www.workiz.com
---
