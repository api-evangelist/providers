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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
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
random_paper: 17
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
