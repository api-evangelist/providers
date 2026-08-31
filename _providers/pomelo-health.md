---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pomelo-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pomelo-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.pomelohealth.com/
- group: operate
  title: ''
  type: Support
  url: https://support.pomelohealth.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pomelohealth.com/privacy-policy
created: '2026-07-24'
description: 'Pomelo Health (formerly Chronometriq, founded 2012, headquartered in Montreal with offices in Boston and Toronto) is a Canadian patient-engagement software company operating within the TELUS Health ecosystem. Its cloud platform helps medical clinics reduce no-shows and modernize the front-desk experience with online booking/e-booking, automated SMS/voice/email appointment reminders, digital intake eForms, telemedicine, secure two-way messaging, patient broadcasts, and a patient portal. Pomelo ships as an EMR add-on that syncs with TELUS Health EMRs — Accuro, Medesync, and TELUS CHR — rather than as an open integration platform. As of this review Pomelo Health publishes NO public developer portal, NO documented REST/OpenAPI, and NO public HL7 FHIR CapabilityStatement or SMART-on-FHIR surface; third-party connectivity is achieved through the underlying EMR partner APIs, so this profile is an honest identity stub for a company with a gated, partner-only integration model. Home
  market: Canada.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: Pomelo Health
nav: Providers
network: true
overview: 'Pomelo Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Canada, Patient Engagement, Telehealth, and Appointment Scheduling.


  Pomelo Health''s developer surface includes support and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 5.3
    commercial_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Pomelo Health Domain Security
  slug: pomelo-health-domain-security
  summary_line: no transport/DNS hardening detected
slug: pomelo-health
tags:
- Healthcare
- Canada
- Patient Engagement
- Telehealth
- Appointment Scheduling
- Patient Portal
- eForms
- EMR Integration
- TELUS Health
- Digital Health
website: https://www.pomelohealth.com/
---
