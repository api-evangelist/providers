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
api_count: 1
apis:
- description: IP/domain/URL reputation
  name: Phisherman
  slug: phisherman
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phisherman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phisherman.gg/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: IP/domain/URL reputation
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phisherman.png
layout: provider
modified: '2026-05-28'
name: Phisherman
nav: Providers
network: true
overview: Phisherman publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anti Malware and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Phisherman Domain Security
  slug: phisherman-domain-security
  summary_line: no transport/DNS hardening detected
slug: phisherman
tags:
- Anti Malware
- Public APIs
website: https://phisherman.gg/
---
