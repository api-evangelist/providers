---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Intakeq Agentic Access
  operation_count: 30
  slug: intakeq-agentic-access
  summary_line: 30 operations · 11 acting
api_count: 6
apis:
- description: Appointments, booking settings, and cancellation.
  name: IntakeQ Appointments API
  slug: intakeq-appointments-api
- description: Clients (patients), tags, and diagnoses.
  name: IntakeQ Clients API
  slug: intakeq-clients-api
- description: Client file attachments and folders.
  name: IntakeQ Files API
  slug: intakeq-files-api
- description: Intake questionnaires, consent forms, templates, and practitioners.
  name: IntakeQ Intake Forms API
  slug: intakeq-intake-forms-api
- description: Invoice query and retrieval.
  name: IntakeQ Invoices API
  slug: intakeq-invoices-api
- description: Treatment / clinical notes and PDF export.
  name: IntakeQ Treatment Notes API
  slug: intakeq-treatment-notes-api
artifact_total: 13
collections:
- collection_type: open
  name: IntakeQ API
  slug: open-intakeq
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intakeq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intakeq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intakeq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intakeq
- group: company
  title: ''
  type: Website
  url: https://intakeq.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.intakeq.com/category/560-api
- group: commercial
  title: ''
  type: Plans
  url: plans/intakeq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intakeq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/intakeq-finops.yml
created: '2026-07-05'
description: IntakeQ is a HIPAA-compliant practice management platform for health and wellness practitioners - therapists, chiropractors, counselors, dietitians, and other small practices. It provides secure electronic intake forms, e-signatures, and document sharing, and through its PracticeQ tier adds appointment scheduling, a booking widget, a secure client portal, payments and invoicing, treatment notes, telehealth, and insurance billing. IntakeQ publishes a documented REST API under https://intakeq.com/api/v1 authenticated with an X-Auth-Key header, covering clients, appointments, intake questionnaires, treatment notes, invoices, and file attachments, plus webhooks for intake completion, note locking, and invoice events.
finops:
- name: Intakeq Finops
  service_category: Practice Management Software
  slug: intakeq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intakeq.png
layout: provider
modified: '2026-07-05'
name: IntakeQ
nav: Providers
network: true
overview: 'IntakeQ publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Clients API, Files API, and 3 more. Tagged areas include Practice Management, Intake Forms, Scheduling, Health and Wellness, and EHR.


  IntakeQ''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Intakeq Plans Pricing
  plan_count: 4
  slug: intakeq-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 4
  name: Intakeq Rate Limits
  slug: intakeq-rate-limits
score:
  band: thin
  composite: 34.1
  delta: -0.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intakeq/refs/heads/main/screenshots/intakeq-2026-07-25T222634.png
security:
- kind: authentication
  name: Intakeq Authentication
  slug: intakeq-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Intakeq Domain Security
  slug: intakeq-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: intakeq
tags:
- Practice Management
- Intake Forms
- Scheduling
- Health and Wellness
- EHR
- Telehealth
- HIPAA
website: https://intakeq.com
---
