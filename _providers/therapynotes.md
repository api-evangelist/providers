---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: 'Modeled capability area for managing the client (patient) roster - demographics, contacts, insurance, and portal enrollment. TherapyNotes surfaces this only in its web application; there is no public '
  name: TherapyNotes Clients API (Modeled)
  slug: therapynotes-clients-api
- description: Modeled capability area for appointments, recurring schedules, and reminders. TherapyNotes offers native one-way calendar sync to Google Calendar, Microsoft Outlook, and iCloud from within the applica
  name: TherapyNotes Scheduling API (Modeled)
  slug: therapynotes-scheduling-api
- description: Modeled capability area for interactive clinical note templates - intake, progress notes, treatment plans, and psychiatry documentation. This is PHI-bearing behavioral-health data and is available onl
  name: TherapyNotes Clinical Documentation API (Modeled)
  slug: therapynotes-clinical-documentation-api
- description: Modeled capability area for medical billing - electronic insurance claims, ERA (electronic remittance advice), superbills, and integrated credit card processing. TherapyNotes runs claims through an in
  name: TherapyNotes Billing and Claims API (Modeled)
  slug: therapynotes-billing-claims-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/therapynotes-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/therapynotes-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/therapynotes-llc
- group: company
  title: ''
  type: Website
  url: https://www.therapynotes.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.therapynotes.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/therapynotes-plans-pricing.yml
created: '2026-07-10'
description: TherapyNotes is a HIPAA-compliant practice management and electronic health record (EHR) platform built specifically for behavioral health - therapists, psychologists, psychiatrists, social workers, and group practices. It provides interactive note templates and clinical documentation, scheduling with appointment reminders, a client portal, telehealth, electronic insurance claims and ERA, credit card processing, and TherapyFuel AI tooling. As of this writing TherapyNotes does NOT expose a public or partner developer API, webhooks, or documented programmatic interface; access to client, appointment, clinical-note, and billing data is through the browser application and manual exports only. This entry documents TherapyNotes as an API-relevant provider and honestly models the capability areas a behavioral-health EHR API would cover; the API surfaces below are modeled, not published, and no endpoints are fabricated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/therapynotes.png
layout: provider
modified: '2026-07-10'
name: TherapyNotes
nav: Providers
network: true
overview: 'TherapyNotes publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, EHR, Practice Management, Mental Health, and Electronic Health Records.


  TherapyNotes'' developer surface includes documentation and 5 more developer resources.'
plans:
- name: Therapynotes Plans Pricing
  plan_count: 3
  slug: therapynotes-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 14.1
  delta: -0.5
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Therapynotes Domain Security
  slug: therapynotes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Therapynotes Vulnerability Disclosure
  slug: therapynotes-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: therapynotes
tags:
- Behavioral Health
- EHR
- Practice Management
- Mental Health
- Electronic Health Records
- Medical Billing
- HIPAA
- No Public API
website: https://www.therapynotes.com
---
