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
- description: Free weather API with forecast data similar to Dark Sky
  name: Pirate Weather
  slug: pirate-weather
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pirate-weather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pirateweather.net/en/latest/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Free weather API with forecast data similar to Dark Sky
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pirate-weather.png
layout: provider
modified: '2026-05-28'
name: Pirate Weather
nav: Providers
network: true
overview: Pirate Weather publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 20
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
screenshot: https://raw.githubusercontent.com/api-evangelist/pirate-weather/refs/heads/main/screenshots/pirate-weather-2026-06-20T191728.png
security:
- kind: domain-security
  name: Pirate Weather Domain Security
  slug: pirate-weather-domain-security
  summary_line: TLSv1.3
slug: pirate-weather
tags:
- Weather
- Public APIs
website: https://pirateweather.net/en/latest/
---
