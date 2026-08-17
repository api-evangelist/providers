---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Acuity Scheduling Agentic Access
  operation_count: 5
  slug: acuity-scheduling-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 5
apis:
- description: REST API for managing appointments, appointment types, clients, calendars, availability, intake forms, products, and webhooks in Acuity Scheduling. Supports HTTP Basic Auth (User ID + API Key) for sin
  name: Acuity Scheduling REST API v1
  slug: rest-api-v1
- description: AsyncAPI 2.6 definition for Acuity Scheduling's outbound webhook surface. Models the documented appointment events (scheduled, rescheduled, canceled, changed) and order events (order.completed) delive
  name: Acuity Scheduling Webhooks
  slug: webhooks-asyncapi
- description: The Appointments API from Acuity Scheduling — 2 operation(s) for appointments.
  name: Acuity Scheduling Appointments API
  slug: acuity-scheduling-appointments-api
- description: The Meta API from Acuity Scheduling — 1 operation(s) for meta.
  name: Acuity Scheduling Meta API
  slug: acuity-scheduling-meta-api
- description: The Payments API from Acuity Scheduling — 1 operation(s) for payments.
  name: Acuity Scheduling Payments API
  slug: acuity-scheduling-payments-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acuity Scheduling Appointments API
  slug: open-acuity-scheduling-appointments-api
- collection_type: open
  name: Acuity Scheduling Webhooks
  slug: open-acuity-scheduling-asyncapi
- collection_type: open
  name: Acuity Scheduling Appointments Meta API
  slug: open-acuity-scheduling-meta-api
- collection_type: open
  name: Acuity Scheduling Appointments Payments API
  slug: open-acuity-scheduling-payments-api
- collection_type: open
  name: Acuity Scheduling API
  slug: open-acuity-scheduling
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acuity-scheduling-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acuity-scheduling-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acuity-scheduling-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acuity-scheduling
- group: company
  title: ''
  type: Website
  url: https://acuityscheduling.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.acuityscheduling.com
- group: commercial
  title: ''
  type: Pricing
  url: https://acuityscheduling.com/signup.php
- group: start
  title: ''
  type: Signup
  url: https://acuityscheduling.com/signup.php
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.acuityscheduling.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.acuityscheduling.com/learn
created: '2026-05-11'
description: Acuity Scheduling is an online appointment scheduling platform (a Squarespace product) used by service businesses, coaches, and practitioners to manage client bookings, calendars, intake forms, payments, and reminders. The Acuity REST API provides programmatic access to appointments, appointment types, clients, calendars, availability, forms, and webhooks at acuityscheduling.com/api/v1. Authentication uses HTTP Basic Auth (User ID + API Key) for single accounts or OAuth 2.0 for multi-tenant applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acuity-scheduling.png
layout: provider
modified: '2026-05-30'
name: Acuity Scheduling
nav: Providers
network: true
overview: 'Acuity Scheduling publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Appointments API, Meta API, and 1 more. Tagged areas include Appointment Scheduling, Booking, Calendar, Scheduling, and Squarespace.


  Acuity Scheduling''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 123
score:
  band: thin
  composite: 30.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.4
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 75.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acuity-scheduling/refs/heads/main/screenshots/acuity-scheduling-2026-06-20T164418.png
security:
- kind: authentication
  name: Acuity Scheduling Authentication
  slug: acuity-scheduling-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Acuity Scheduling Domain Security
  slug: acuity-scheduling-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: acuity-scheduling
tags:
- Appointment Scheduling
- Booking
- Calendar
- Scheduling
- Squarespace
website: https://acuityscheduling.com
---
