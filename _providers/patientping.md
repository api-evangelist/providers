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
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patientping-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://patientping.com
- group: start
  title: ''
  type: Login
  url: https://my.patientping.com/
created: '2026-07-17'
description: PatientPing is a real-time care-coordination network that delivers e-notifications ("Pings") and ADT-based admission, discharge, and transfer alerts across hospitals, post-acute facilities, health plans, pharmacies, and community providers. Its Route solution helps hospitals meet the CMS Interoperability and Patient Access Rule e-notifications Condition of Participation. PatientPing was acquired by Appriss Health in 2021 and rebranded as Bamboo Health; patientping.com now redirects to bamboohealth.com. No public developer portal or API documentation is published — clinical integration is handled privately via HL7/ADT data feeds embedded in provider workflow.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patientping.png
layout: provider
modified: '2026-07-20'
name: PatientPing
nav: Providers
network: true
overview: PatientPing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bio Healthcare, Care Coordination, Health IT, and Interoperability.
random_paper: 144
score:
  band: minimal
  composite: 4.6
  delta: -3.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patientping/refs/heads/main/screenshots/patientping-2026-08-07T191554.png
security:
- kind: domain-security
  name: Patientping Domain Security
  slug: patientping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: patientping
tags:
- Company
- Bio Healthcare
- Care Coordination
- Health IT
- Interoperability
- Notifications
- HL7 ADT
website: https://patientping.com
---
