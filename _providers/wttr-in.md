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
- description: Weather in your terminal, supports JSON output
  name: wttr.in
  slug: wttrin
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wttr-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wttr.in/:help
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Weather in your terminal, supports JSON output
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wttr-in.png
layout: provider
modified: '2026-05-28'
name: wttr.in
nav: Providers
network: true
overview: wttr.in publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 45
score:
  band: minimal
  composite: 6.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wttr-in/refs/heads/main/screenshots/wttr-in-2026-06-20T201636.png
security:
- kind: domain-security
  name: Wttr In Domain Security
  slug: wttr-in-domain-security
  summary_line: TLSv1.3
slug: wttr-in
tags:
- Weather
- Public APIs
website: https://wttr.in/:help
---
