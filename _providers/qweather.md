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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Location-based weather data
  name: QWeather
  slug: qweather
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qweather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dev.qweather.com/en/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Location-based weather data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qweather.png
layout: provider
modified: '2026-05-28'
name: QWeather
nav: Providers
network: true
overview: QWeather publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 120
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qweather/refs/heads/main/screenshots/qweather-2026-06-20T192454.png
security:
- kind: domain-security
  name: Qweather Domain Security
  slug: qweather-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qweather
tags:
- Weather
- Public APIs
website: https://dev.qweather.com/en/
---
