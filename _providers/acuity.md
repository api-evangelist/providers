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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Acuity Agentic Access
  operation_count: 5
  slug: acuity-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: The Appointments API from Acuity Scheduling — 3 operation(s) for appointments.
  name: Acuity Scheduling Appointments API
  slug: acuity-appointments-api
- description: The Meta API from Acuity Scheduling — 1 operation(s) for meta.
  name: Acuity Scheduling Meta API
  slug: acuity-meta-api
- description: The Payments API from Acuity Scheduling — 1 operation(s) for payments.
  name: Acuity Scheduling Payments API
  slug: acuity-payments-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acuity Scheduling Appointments API
  slug: open-acuity-appointments-api
- collection_type: open
  name: Acuity Scheduling Appointments Meta API
  slug: open-acuity-meta-api
- collection_type: open
  name: Acuity Scheduling Appointments Payments API
  slug: open-acuity-payments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/acuity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acuity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acuity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/acuity-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://acuityscheduling.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.acuityscheduling.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/AcuityScheduling
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acuity-scheduling
- group: company
  title: ''
  type: Blog
  url: https://www.acuityscheduling.com/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://acuityscheduling.com/signup.php
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acuityscheduling.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/acuityschedulin
- group: commercial
  title: ''
  type: Plans
  url: plans/acuity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acuity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/acuity-finops.yml
created: '2026-06-13'
description: Acuity Scheduling is an online appointment scheduling platform that enables businesses and independent professionals to automate their booking workflows. The platform provides a REST API for managing appointment types, client availability, bookings, and client records. Developers can integrate scheduling functionality into applications using HTTP Basic Auth or OAuth2, with support for webhooks to receive real-time event notifications. Acuity is a subsidiary of Squarespace and offers SDKs for Node.js and PHP alongside its embeddable client scheduler widget.
examples:
- key_count: 31
  name: Acuity Appointment Example
  slug: acuity-appointment-example
finops:
- name: Acuity Finops
  service_category: ''
  slug: acuity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/acuity.png
json_schemas:
- name: Acuity Appointment
  property_count: 32
  slug: acuity-appointment
jsonld:
- class_count: 31
  name: Acuity Context
  property_count: 10
  slug: acuity-context
layout: provider
modified: '2026-06-13'
name: Acuity Scheduling
nav: Providers
network: true
overview: 'Acuity Scheduling publishes 3 APIs on the [APIs.io](https://apis.io/) network: Appointments API, Meta API, and Payments API. Tagged areas include Scheduling, Appointments, Calendar, Booking, and HIPAA.


  The Acuity Scheduling catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Acuity Scheduling''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Acuity Plans Pricing
  plan_count: 4
  slug: acuity-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Acuity Rate Limits
  slug: acuity-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Acuity Scheduling API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: acuity-jsonschema-spectral-rules
scopes:
- name: Acuity Scopes
  scope_count: 1
  slug: acuity-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 25.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 70.5
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acuity/refs/heads/main/screenshots/acuity-2026-06-20T164353.png
security:
- kind: authentication
  name: Acuity Authentication
  slug: acuity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Acuity Domain Security
  slug: acuity-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: acuity
tags:
- Scheduling
- Appointments
- Calendar
- Booking
- HIPAA
- Webhook
website: https://acuityscheduling.com/
---
