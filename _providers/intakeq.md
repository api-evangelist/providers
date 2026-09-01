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
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Intakeq Agentic Access
  operation_count: 30
  slug: intakeq-agentic-access
  summary_line: 30 operations · 11 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IntakeQ Appointments API
  slug: open-intakeq-appointments-api
- collection_type: open
  name: IntakeQ Appointments Clients API
  slug: open-intakeq-clients-api
- collection_type: open
  name: IntakeQ Appointments Files API
  slug: open-intakeq-files-api
- collection_type: open
  name: IntakeQ Appointments Intake Forms API
  slug: open-intakeq-intake-forms-api
- collection_type: open
  name: IntakeQ Appointments Invoices API
  slug: open-intakeq-invoices-api
- collection_type: open
  name: IntakeQ Appointments Treatment Notes API
  slug: open-intakeq-treatment-notes-api
- collection_type: open
  name: IntakeQ API
  slug: open-intakeq
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/intakeq-capability-edges.yml
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


  IntakeQ''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Intakeq Plans Pricing
  plan_count: 4
  slug: intakeq-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Intakeq Rate Limits
  slug: intakeq-rate-limits
score:
  band: thin
  composite: 37.9
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
    contract_quality: 51.7
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.9
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
