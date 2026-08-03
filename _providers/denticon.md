---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: Create new patients, update and synchronize patient demographics and medical history, and upload patient documents into Denticon. Access is partner approved and scoped by practice group (PGID) and off
  name: Denticon Patient API
  slug: denticon-patient-api
- description: Read appointments on the schedule, query open scheduling availability, and book, confirm, reschedule, or cancel appointments to increase chair utilization. Appointment status writebacks update Dentico
  name: Denticon Appointments API
  slug: denticon-appointments-api
- description: Retrieve insurance eligibility and claims data and post writebacks that automate insurance verification and revenue cycle workflows. Part of the July 2024 Revenue Cycle Management API set. Endpoints m
  name: Denticon Revenue Cycle Management API
  slug: denticon-revenue-cycle-management-api
- description: Access patient ledger, account balance, and transaction data for analytics, patient billing, and payment reconciliation, with ledger writebacks into Denticon. Endpoints modeled from the published Fina
  name: Denticon Financial Ledger API
  slug: denticon-financial-ledger-api
- description: Read clinical data including medical history, treatment plans, and clinical notes, and write back updates to patient medical history and documents. Part of the Clinical Tools API set. Endpoints modele
  name: Denticon Clinical API
  slug: denticon-clinical-api
- description: Retrieve practice configuration - office locations (OIDs), providers, and setup data - so that every query can be scoped to the correct location in Denticon's multi-location single-database model. Cor
  name: Denticon Practice API
  slug: denticon-practice-api
- description: Event-driven architecture that pushes synchronized patient and appointment updates to partner-registered webhook endpoints when records are created, modified, or cancelled - removing the need for poll
  name: Denticon Events and Webhooks API
  slug: denticon-events-webhooks-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/denticon-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/denticon-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planet-dds
- group: company
  title: ''
  type: Website
  url: https://www.planetdds.com/denticon/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.planetdds.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.denticon.com/Home/GettingStarted
- group: start
  title: ''
  type: SignUp
  url: https://developer.planetdds.com/
- group: company
  title: ''
  type: Partners
  url: https://www.planetdds.com/integrations/
created: '2026-07-04'
description: Denticon is a cloud-based dental practice management platform built for dental service organizations (DSOs) and multi-location group practices, owned and operated by Planet DDS (which also owns Cloud 9 Ortho and Apteryx imaging). The Denticon API program - relaunched in July 2024 on a new developer portal powered by Azure API Management - exposes RESTful APIs, webhooks, and batch data extracts covering patient, appointment, financial/ledger, insurance and claims (Revenue Cycle Management), clinical, and practice/office data, with OAuth 2.0 auth, an event-driven architecture for synchronized updates, and writebacks into Denticon. API access is partner-gated - Planet DDS must approve vendors and each client practice authorizes vendor access to specific office locations (OIDs). Public documentation exists, but keys and interactive access require program enrollment, so the endpoint surface below is modeled from the published API categories rather than a downloadable OpenAPI specification.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/denticon.png
layout: provider
modified: '2026-07-04'
name: Denticon
nav: Providers
network: true
overview: 'Denticon publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Practice Management, Healthcare, DSO, and EHR.


  Denticon''s developer surface includes documentation, signup flow, and 6 more developer resources.'
random_paper: 92
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/denticon/refs/heads/main/screenshots/denticon-2026-07-25T211726.png
security:
- kind: domain-security
  name: Denticon Domain Security
  slug: denticon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Denticon Trust Center
  slug: denticon-trust-center
  summary_line: HIPAA, GDPR
slug: denticon
tags:
- Dental
- Practice Management
- Healthcare
- DSO
- EHR
- Patient Data
- Revenue Cycle Management
- Partner API
website: https://www.planetdds.com/denticon/
---
