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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Cliniko Agentic Access
  operation_count: 25
  slug: cliniko-agentic-access
  summary_line: 25 operations · 8 acting
api_count: 1
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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cliniko Appointment Types API
  slug: open-cliniko-appointment-types-api
- collection_type: open
  name: Cliniko Appointment Types Appointments API
  slug: open-cliniko-appointments-api
- collection_type: open
  name: Cliniko Appointment Types Businesses API
  slug: open-cliniko-businesses-api
- collection_type: open
  name: Cliniko Appointment Types Invoices API
  slug: open-cliniko-invoices-api
- collection_type: open
  name: Cliniko Appointment Types Patients API
  slug: open-cliniko-patients-api
- collection_type: open
  name: Cliniko Appointment Types Practitioners API
  slug: open-cliniko-practitioners-api
- collection_type: open
  name: Cliniko Appointment Types Treatment Notes API
  slug: open-cliniko-treatment-notes-api
- collection_type: open
  name: Cliniko API
  slug: open-cliniko
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cliniko-capability-edges.yml
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


  Cliniko''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Cliniko Plans Pricing
  plan_count: 8
  slug: cliniko-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Cliniko Rate Limits
  slug: cliniko-rate-limits
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.7
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.5
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Software-as-a-Service
website: https://www.cliniko.com
---
