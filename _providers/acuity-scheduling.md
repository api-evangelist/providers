---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Acuity Scheduling Agentic Access
  operation_count: 5
  slug: acuity-scheduling-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: REST API for managing appointments, appointment types, clients, calendars, availability, intake forms, products, and webhooks in Acuity Scheduling. Supports HTTP Basic Auth (User ID + API Key) for sin
  name: Acuity Scheduling REST API v1
  slug: rest-api-v1
- description: AsyncAPI 2.6 definition for Acuity Scheduling's outbound webhook surface. Models the documented appointment events (scheduled, rescheduled, canceled, changed) and order events (order.completed) delive
  name: Acuity Scheduling Webhooks
  slug: webhooks-asyncapi
- baseURL: https://acuityscheduling.com/api/v1
  baseurl_source: declared
  description: The Appointments API from Acuity Scheduling — 2 operation(s) for appointments.
  name: Acuity Scheduling Appointments API
  slug: acuity-scheduling-appointments-api
- baseURL: https://acuityscheduling.com/api/v1
  baseurl_source: declared
  description: The Meta API from Acuity Scheduling — 1 operation(s) for meta.
  name: Acuity Scheduling Meta API
  slug: acuity-scheduling-meta-api
- baseURL: https://acuityscheduling.com/api/v1
  baseurl_source: declared
  description: The Payments API from Acuity Scheduling — 1 operation(s) for payments.
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
random_paper: 19
score:
  band: thin
  composite: 30.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 29.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
