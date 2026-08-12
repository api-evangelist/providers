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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Nookal Agentic Access
  operation_count: 36
  slug: nookal-agentic-access
  summary_line: 36 operations · 15 acting
api_count: 5
apis:
- description: Appointments, class bookings, availabilities, and the waiting list.
  name: Nookal Appointments API
  slug: nookal-appointments-api
- description: Clinic reference data - locations, practitioners, and item/type lists.
  name: Nookal Clinic API
  slug: nookal-clinic-api
- description: Invoices and their items, payments, credits, discounts, and refunds.
  name: Nookal Invoices API
  slug: nookal-invoices-api
- description: Patient records, cases, treatment notes, and patient files.
  name: Nookal Patients API
  slug: nookal-patients-api
- description: Verify that an API key is valid and connected to a Nookal account.
  name: Nookal Verification API
  slug: nookal-verification-api
artifact_total: 12
collections:
- collection_type: open
  name: Nookal API
  slug: open-nookal
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nookal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nookal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nookal-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.nookal.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.nookal.com/developers
- group: start
  title: ''
  type: SignUp
  url: https://www.nookal.com/signup
- group: commercial
  title: ''
  type: Plans
  url: plans/nookal-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nookal.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nookal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nookal-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nookal
- group: operate
  title: ''
  type: Support
  url: https://support.nookal.com
created: '2026-07-12'
description: Nookal is Australian-built practice management software for allied health clinics - physiotherapy, chiropractic, podiatry, psychology, and similar disciplines - covering online bookings, multi-practitioner scheduling, patient and case records, treatment notes, invoicing, bulk billing, and clinic reporting. Nookal exposes a documented REST API at https://api.nookal.com/production/v2/ that lets integrators read and write patients, cases, appointments, class bookings, availabilities, practitioners, locations, treatment notes, files, and invoices. The API is authenticated with an account-issued API key and returns JSON. API access is available on the paid Professional and Enterprise plans.
finops:
- name: Nookal Finops
  service_category: Practice Management Software
  slug: nookal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nookal.png
layout: provider
modified: '2026-07-12'
name: Nookal
nav: Providers
network: true
overview: 'Nookal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Clinic API, Invoices API, and 2 more. Tagged areas include Practice Management, Healthcare, Allied Health, Appointments, and Scheduling.


  Nookal''s developer surface includes authentication, documentation, signup flow, pricing, support, and 7 more developer resources.'
plans:
- name: Nookal Plans Pricing
  plan_count: 3
  slug: nookal-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Nookal Rate Limits
  slug: nookal-rate-limits
score:
  band: thin
  composite: 38.0
  delta: -0.4
  facets:
    commercial_clarity: 63.2
    contract_quality: 52.4
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nookal/refs/heads/main/screenshots/nookal-2026-08-07T185455.png
security:
- kind: authentication
  name: Nookal Authentication
  slug: nookal-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nookal Domain Security
  slug: nookal-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: nookal
tags:
- Practice Management
- Healthcare
- Allied Health
- Appointments
- Scheduling
- Patients
- Clinics
- Bookings
- Physiotherapy
- SaaS
website: https://www.nookal.com
---
