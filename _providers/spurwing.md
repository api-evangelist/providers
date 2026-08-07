---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 3
  human_in_the_loop: 0
  name: Spurwing Agentic Access
  operation_count: 7
  slug: spurwing-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 4
apis:
- description: Spurwing references webhook-style event notifications for scheduling events in its integration guidance. Specific webhook event types and payloads are not reconciled in this artifact; verify against t
  name: Spurwing Webhooks API
  slug: webhooks
- description: The Appointments API from Spurwing — 3 operation(s) for appointments.
  name: Spurwing Appointments API
  slug: spurwing-appointments-api
- description: The Availability API from Spurwing — 2 operation(s) for availability.
  name: Spurwing Availability API
  slug: spurwing-availability-api
- description: The Services API from Spurwing — 1 operation(s) for services.
  name: Spurwing Services API
  slug: spurwing-services-api
artifact_total: 11
collections:
- collection_type: open
  name: Spurwing Appointment Scheduling API
  slug: open-spurwing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spurwing-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spurwing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spurwing-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpurwingIO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spurwingio
- group: company
  title: ''
  type: Website
  url: https://www.spurwing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spurwing.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/spurwing-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spurwing-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spurwing-finops.yml
created: '2026-06-21'
description: Spurwing is an enterprise-grade appointment scheduling, calendar, and time-management API. Its REST API powers booking widgets, marketplaces, SaaS, and healthcare scheduling with multi-user calendars, provider availability, group meetings, time-zone handling, and client booking. Public read and booking operations are scoped by a public Provider ID, while private operations use a Bearer API key. Spurwing joined Healthie.
finops:
- name: Spurwing Finops
  service_category: Scheduling and Calendar
  slug: spurwing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spurwing.png
layout: provider
modified: '2026-06-21'
name: Spurwing
nav: Providers
network: true
overview: 'Spurwing publishes 3 APIs on the [APIs.io](https://apis.io/) network: Appointments API, Availability API, and Services API. Tagged areas include Scheduling, Appointments, Booking, Calendar, and Availability.


  Spurwing''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Spurwing Plans Pricing
  plan_count: 1
  slug: spurwing-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 2
  name: Spurwing Rate Limits
  slug: spurwing-rate-limits
score:
  band: thin
  composite: 35.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Spurwing Authentication
  slug: spurwing-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spurwing Domain Security
  slug: spurwing-domain-security
  summary_line: no transport/DNS hardening detected
slug: spurwing
tags:
- Scheduling
- Appointments
- Booking
- Calendar
- Availability
website: https://www.spurwing.io/
---
