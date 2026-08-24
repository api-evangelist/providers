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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: Self-service patient check-in and registration - kiosk, tablet, and mobile intake that captures demographics, consent forms, and identity, then writes the completed registration back to the practice's
  name: Clearwave Check-In API
  slug: clearwave-check-in-api
- description: Multi-factor insurance eligibility and benefits verification run automatically as part of check-in, returning coverage status, plan details, and patient responsibility. Modeled capability area; access
  name: Clearwave Eligibility API
  slug: clearwave-eligibility-api
- description: Online and self-service appointment scheduling where every booking, cancellation, and reschedule syncs automatically to the practice management system and EHR. Modeled capability area; access is partn
  name: Clearwave Scheduling API
  slug: clearwave-scheduling-api
- description: Bidirectional patient demographic and record synchronization between Clearwave and 50+ EHR/PM systems, keeping patient data consistent across the practice's systems in real time. Modeled capability ar
  name: Clearwave Patients API
  slug: clearwave-patients-api
- description: Point-of-service and self-service patient payment capture tied to eligibility-derived patient responsibility, posting balances and payments back to the practice's revenue-cycle systems. Modeled capabi
  name: Clearwave Payments API
  slug: clearwave-payments-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearwave-intake-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clearwave-corporation
- group: company
  title: ''
  type: Website
  url: https://www.clearwaveinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.clearwaveinc.com/integrations/
created: '2026-07-05'
description: Clearwave is a patient revenue-cycle and self-service engagement platform for healthcare practices, covering online scheduling, self-service registration and intake, multi-factor insurance eligibility verification, and patient payments. Rather than publishing an open developer API, Clearwave connects to more than 50 electronic health record (EHR) and practice management (PM) systems - including athenahealth, NextGen, eClinicalWorks, Modernizing Medicine, Veradigm, Nextech, Greenway, and Unlimited Systems - through formal, partner-gated API license and integration agreements. Data such as appointments, patient demographics, eligibility results, and payments flows bidirectionally between Clearwave and the practice's EHR/PM in real time. There is no public, self-service developer portal, OpenAPI definition, or documented public WebSocket API; the API surfaces below are logical capability areas modeled from Clearwave's product documentation, not publicly documented endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearwave-intake.png
layout: provider
modified: '2026-07-05'
name: Clearwave
nav: Providers
network: true
overview: 'Clearwave publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Patient Access, Revenue Cycle, Patient Check-In, and Insurance Eligibility.


  Clearwave''s developer surface includes documentation and 3 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearwave-intake/refs/heads/main/screenshots/clearwave-intake-2026-07-25T205556.png
security:
- kind: domain-security
  name: Clearwave Intake Domain Security
  slug: clearwave-intake-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearwave-intake
tags:
- Healthcare
- Patient Access
- Revenue Cycle
- Patient Check-In
- Insurance Eligibility
- Scheduling
- Patient Payments
- EHR Integration
- Partner API
website: https://www.clearwaveinc.com/
---
