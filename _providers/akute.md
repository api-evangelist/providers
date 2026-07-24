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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
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
random_paper: 28
rate_limits:
- limit_count: 2
  name: Akute Rate Limits
  slug: akute-rate-limits
score:
  band: thin
  composite: 33.6
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
