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
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Peruvian Statistical Government Open Data
  name: INEI
  slug: inei
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inei-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://iinei.inei.gob.pe/microdatos/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Peruvian Statistical Government Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inei.png
layout: provider
modified: '2026-05-28'
name: INEI
nav: Providers
network: true
overview: INEI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 13
score:
  band: minimal
  composite: 7.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: domain-security
  name: Inei Domain Security
  slug: inei-domain-security
  summary_line: DNSSEC
slug: inei
tags:
- Government
- Public APIs
website: http://iinei.inei.gob.pe/microdatos/
---
