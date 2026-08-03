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
- acting_count: 12
  human_in_the_loop: 0
  name: Akute Agentic Access
  operation_count: 42
  slug: akute-agentic-access
  summary_line: 42 operations · 12 acting
api_count: 8
apis:
- description: The Appointments API from Akute Health — 4 operation(s) for appointments.
  name: Akute Health Appointments API
  slug: akute-appointments-api
- description: The Documents API from Akute Health — 2 operation(s) for documents.
  name: Akute Health Documents API
  slug: akute-documents-api
- description: The Encounters API from Akute Health — 2 operation(s) for encounters.
  name: Akute Health Encounters API
  slug: akute-encounters-api
- description: The Labs API from Akute Health — 11 operation(s) for labs.
  name: Akute Health Labs API
  slug: akute-labs-api
- description: The Medications API from Akute Health — 4 operation(s) for medications.
  name: Akute Health Medications API
  slug: akute-medications-api
- description: The Patients API from Akute Health — 3 operation(s) for patients.
  name: Akute Health Patients API
  slug: akute-patients-api
- description: The Tasks API from Akute Health — 2 operation(s) for tasks.
  name: Akute Health Tasks API
  slug: akute-tasks-api
- description: The Webhooks API from Akute Health — 2 operation(s) for webhooks.
  name: Akute Health Webhooks API
  slug: akute-webhooks-api
artifact_total: 15
collections:
- collection_type: open
  name: Akute Health Customer API
  slug: open-akute
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akute-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akute-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/akute-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akute-health-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akute-health
- group: company
  title: ''
  type: Website
  url: https://www.akutehealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.akutehealth.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/akute-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/akute-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/akute-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://akutehealth.com/blog
created: '2026-06-21'
description: Akute Health is an automation-first, API- and developer-friendly EHR (electronic health record) platform for digital health, telehealth, direct primary care, and GLP-1 weight-loss clinics. Its REST API at https://api.akutehealth.com/v1 exposes FHIR-aligned resources - patients, appointments, clinical notes, tasks, documents, medications and e-prescribing, lab orders and results, plus signed webhooks - so customers can enrich the record and build patient-facing or internal applications.
finops:
- name: Akute Finops
  service_category: Healthcare
  slug: akute-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akute.png
layout: provider
modified: '2026-06-21'
name: Akute Health
nav: Providers
network: true
overview: 'Akute Health publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Documents API, Encounters API, and 5 more. Tagged areas include Healthcare, EHR, EMR, FHIR, and Digital Health.


  Akute Health''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Akute Plans Pricing
  plan_count: 4
  slug: akute-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 2
  name: Akute Rate Limits
  slug: akute-rate-limits
score:
  band: thin
  composite: 33.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akute/refs/heads/main/screenshots/akute-2026-07-25T195526.png
security:
- kind: authentication
  name: Akute Authentication
  slug: akute-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Akute Domain Security
  slug: akute-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: akute
tags:
- Healthcare
- EHR
- EMR
- FHIR
- Digital Health
- Telehealth
website: https://www.akutehealth.com/
---
