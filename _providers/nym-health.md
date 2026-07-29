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
  url: security/nym-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nym.health
created: '2026-07-17'
description: Nym Health provides autonomous medical coding for health systems and physician groups. Its Clinical Language Understanding (CLU) engine reads patient charts and assigns medical codes automatically with a transparent audit trail for every code, keeping current as coding guidelines change and supporting multispecialty environments. Nym is used by 30+ health systems including Ochsner Health, Inova, Henry Ford and Geisinger, and is backed by GV and Lightspeed Venture Partners. As of this enrichment pass Nym publishes no public developer portal, API documentation, SDKs, or OpenAPI surface; integrations are handled directly with health systems via sales/demo engagement.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nym-health.png
layout: provider
modified: '2026-07-20'
name: Nym Health
nav: Providers
network: true
overview: Nym Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Life Sciences, Healthcare, Medical Coding, and Autonomous Coding.
random_paper: 43
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
security:
- kind: domain-security
  name: Nym Health Domain Security
  slug: nym-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nym-health
tags:
- Company
- Life Sciences
- Healthcare
- Medical Coding
- Autonomous Coding
- Clinical NLP
- Revenue Cycle
- Health IT
website: https://nym.health
---
