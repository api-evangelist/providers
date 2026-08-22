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
  url: security/mylife-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stopbreathethink.com
created: '2026-07-17'
description: MyLife (formerly Stop, Breathe & Think) was a meditation and mindfulness mobile app backed by 500 Global that guided users through short check-ins and recommended meditations based on how they were feeling. As of this enrichment pass the company's primary web presence at stopbreathethink.com no longer resolves to a live site (DNS and CAA records remain but there is no reachable HTTPS host), and no public developer, API, documentation, or SDK surface could be located. The company appears defunct.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mylife.png
layout: provider
modified: '2026-07-20'
name: MyLife
nav: Providers
network: true
overview: MyLife is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Meditation, Mindfulness, Wellness, and Mental Health.
random_paper: 16
score:
  band: minimal
  composite: 3.3
  delta: -2.1
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Mylife Domain Security
  slug: mylife-domain-security
  summary_line: no transport/DNS hardening detected
slug: mylife
tags:
- Company
- Meditation
- Mindfulness
- Wellness
- Mental Health
- Mobile App
- Consumer
website: https://stopbreathethink.com
---
