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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guahao-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://guahao.com
created: '2026-07-17'
description: guahao.com is the flagship consumer domain of WeDoctor (微医), the Chinese digital-health platform that began as Guahao.com (挂号网) — literally the "appointment-registration network" — connecting patients to hospitals and physicians for online appointment booking, telemedicine consultations, e-prescriptions, and chronic-disease management. Founded in Hangzhou around 2010 and among the early investments of Qiming Venture Partners, the company operates a large internet-hospital and clinic network across China. This API Evangelist profile was surfaced from a venture-portfolio lead and enriched by the pipeline; the public site sits behind a bot-challenge WAF (Tencent EdgeOne infrastructure), so no public developer/API surface was discoverable in this pass — the captured artifact is a live domain-security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guahao.png
layout: provider
modified: '2026-07-19'
name: guahao
nav: Providers
network: true
overview: guahao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Digital Health, Telemedicine, and Appointment Booking.
random_paper: 13
score:
  band: minimal
  composite: 5.4
  delta: -2.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guahao/refs/heads/main/screenshots/guahao-2026-07-25T220411.png
security:
- kind: domain-security
  name: Guahao Domain Security
  slug: guahao-domain-security
  summary_line: TLSv1.2 · DNSSEC
slug: guahao
tags:
- Company
- Healthcare
- Digital Health
- Telemedicine
- Appointment Booking
- China
- Internet Hospital
website: https://guahao.com
---
