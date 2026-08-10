---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
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
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Cliniko Agentic Access
  operation_count: 25
  slug: cliniko-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 7
apis:
- description: The named services a clinic offers.
  name: Cliniko Appointment Types API
  slug: cliniko-appointment-types-api
- description: Individual appointments and the unified bookings feed.
  name: Cliniko Appointments API
  slug: cliniko-appointments-api
- description: Businesses / physical locations in a Cliniko account.
  name: Cliniko Businesses API
  slug: cliniko-businesses-api
- description: Patient and appointment invoices.
  name: Cliniko Invoices API
  slug: cliniko-invoices-api
- description: The people who book in for appointments.
  name: Cliniko Patients API
  slug: cliniko-patients-api
- description: Practitioners and the businesses (locations) they work from.
  name: Cliniko Practitioners API
  slug: cliniko-practitioners-api
- description: Structured clinical notes about a patient visit.
  name: Cliniko Treatment Notes API
  slug: cliniko-treatment-notes-api
artifact_total: 14
collections:
- collection_type: open
  name: Cliniko API
  slug: open-cliniko
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cliniko-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cliniko-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cliniko-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/redguava
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cliniko
- group: company
  title: ''
  type: Website
  url: https://www.cliniko.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.cliniko.com
- group: commercial
  title: ''
  type: Plans
  url: plans/cliniko-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cliniko-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cliniko-finops.yml
created: '2026-07-12'
description: Cliniko is practice management software for allied health practices and clinics - physiotherapy, osteopathy, chiropractic, podiatry, psychology, massage, and similar - covering patient records, appointment scheduling and online bookings, practitioners and businesses (locations), treatment notes, invoicing, and payments. Cliniko exposes a well-documented public REST API over HTTPS. The API is region-sharded - the base host is derived from the shard suffix on your API key (for example `https://api.au1.cliniko.com/v1/`) - and is authenticated with an API key passed as the username in HTTP Basic authentication. Every request must also send a `User-Agent` header containing an app/vendor name and a valid contact email, or requests may be blocked.
finops:
- name: Cliniko Finops
  service_category: Practice Management Software (SaaS)
  slug: cliniko-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cliniko.png
layout: provider
modified: '2026-07-12'
name: Cliniko
nav: Providers
network: true
overview: 'Cliniko publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointment Types API, Appointments API, Businesses API, and 4 more. Tagged areas include Practice Management, Healthcare, Allied Health, Appointments, and Scheduling.


  Cliniko''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Cliniko Plans Pricing
  plan_count: 8
  slug: cliniko-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Cliniko Rate Limits
  slug: cliniko-rate-limits
score:
  band: thin
  composite: 36.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cliniko/refs/heads/main/screenshots/cliniko-2026-07-25T205628.png
security:
- kind: authentication
  name: Cliniko Authentication
  slug: cliniko-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cliniko Domain Security
  slug: cliniko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cliniko
tags:
- Practice Management
- Healthcare
- Allied Health
- Appointments
- Scheduling
- Patients
- EHR
- Clinics
- Bookings
- SaaS
website: https://www.cliniko.com
---
