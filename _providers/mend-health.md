---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: Logical grouping for creating and managing appointments, provider availability, patient self-scheduling, rescheduling, and automated appointment reminders. Mend documents these capabilities in its cus
  name: Mend Appointments and Scheduling API
  slug: mend-health-appointments-api
- description: 'Logical grouping for creating and syncing patient records, demographics, and contact details between Mend and an external EHR or practice-management system. Mend performs this synchronization through '
  name: Mend Patients API
  slug: mend-health-patients-api
- description: Logical grouping for initializing secure video telemedicine sessions and the virtual waiting room. The real-time media itself runs over WebRTC via Vonage TokBox and OpenTok relay servers, while api.me
  name: Mend Video Visits API
  slug: mend-health-video-visits-api
- description: Logical grouping for assigning digital intake forms, consents, and assessments to patients and returning their completed responses to the practice. Mend describes these digital forms as a core patient
  name: Mend Digital Forms and Intake API
  slug: mend-health-forms-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mend-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mend.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mendfamily
- group: docs
  title: ''
  type: Documentation
  url: https://bestservice.mendfamily.com/hc/en-us/sections/360007371714-API-Documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/mend-health-plans-pricing.yml
created: '2026-07-10'
description: Mend is a HIPAA-compliant telehealth and patient engagement platform for mental and behavioral healthcare organizations, powering appointment scheduling, automated reminders, secure video visits, digital intake forms and consents, patient messaging, payments, and AI no-show prediction. Mend integrates with EHR and practice-management systems through a combination of HL7, SFTP, and an API served from api.mendfamily.com. That API exists and is used by Mend's own portal for session initialization and signaling, but its reference documentation is delivered through a login-gated customer knowledge base rather than a public developer portal, so Mend's programmatic surface is best characterized as partner- and customer-gated rather than openly self-serve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mend-health.png
layout: provider
modified: '2026-07-10'
name: Mend
nav: Providers
network: true
overview: 'Mend publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telehealth, Telemedicine, Patient Engagement, Behavioral Health, and Scheduling.


  Mend''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Mend Health Plans Pricing
  plan_count: 2
  slug: mend-health-plans-pricing
random_paper: 52
score:
  band: minimal
  composite: 12.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mend-health/refs/heads/main/screenshots/mend-health-2026-08-07T172512.png
security:
- kind: domain-security
  name: Mend Health Domain Security
  slug: mend-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mend-health
tags:
- Telehealth
- Telemedicine
- Patient Engagement
- Behavioral Health
- Scheduling
- Video Visits
- Digital Forms
- HIPAA
- Healthcare
website: https://mend.com
---
