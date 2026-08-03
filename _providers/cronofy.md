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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cronofy Agentic Access
  operation_count: 16
  slug: cronofy-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 5
apis:
- description: Availability queries and hosted real-time scheduling.
  name: Cronofy Availability API
  slug: cronofy-availability-api
- description: Connected calendars, application calendars, and account identity.
  name: Cronofy Calendars API
  slug: cronofy-calendars-api
- description: Reading, creating, updating, and deleting events plus free/busy.
  name: Cronofy Events API
  slug: cronofy-events-api
- description: Notification channels for real-time calendar changes.
  name: Cronofy Push Notifications API
  slug: cronofy-push-notifications-api
- description: Calendar invites tracked without calendar authorization.
  name: Cronofy Smart Invites API
  slug: cronofy-smart-invites-api
artifact_total: 12
collections:
- collection_type: open
  name: Cronofy API
  slug: open-cronofy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cronofy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cronofy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cronofy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cronofy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cronofy
- group: company
  title: ''
  type: Website
  url: https://www.cronofy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cronofy.com/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/cronofy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cronofy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cronofy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.cronofy.com/blog
created: '2026-06-21'
description: Cronofy is a scheduling and calendar API platform that provides a unified interface to Google Calendar, Microsoft 365 / Outlook, Exchange, and Apple iCloud. Its REST API powers two-way calendar sync, real-time availability and scheduling, smart invites, scheduling links, and push notifications for software teams embedding scheduling into their products.
finops:
- name: Cronofy Finops
  service_category: Developer Tools and Scheduling
  slug: cronofy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cronofy.png
layout: provider
modified: '2026-06-21'
name: Cronofy
nav: Providers
network: true
overview: 'Cronofy publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Calendars API, Events API, and 2 more. Tagged areas include Scheduling, Calendar, Availability, Booking, and Productivity.


  Cronofy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cronofy Plans Pricing
  plan_count: 4
  slug: cronofy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Cronofy Rate Limits
  slug: cronofy-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/cronofy/refs/heads/main/screenshots/cronofy-2026-07-25T210745.png
security:
- kind: authentication
  name: Cronofy Authentication
  slug: cronofy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cronofy Domain Security
  slug: cronofy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cronofy
tags:
- Scheduling
- Calendar
- Availability
- Booking
- Productivity
website: https://www.cronofy.com
---
