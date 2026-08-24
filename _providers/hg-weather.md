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
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Provides weather forecast data for cities in Brazil
  name: HG Weather
  slug: hg-weather
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hg-weather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hgbrasil.com/status/weather
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provides weather forecast data for cities in Brazil
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hg-weather.png
layout: provider
modified: '2026-05-28'
name: HG Weather
nav: Providers
network: true
overview: HG Weather publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather and Public APIs.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hg-weather/refs/heads/main/screenshots/hg-weather-2026-06-20T182720.png
security:
- kind: domain-security
  name: Hg Weather Domain Security
  slug: hg-weather-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hg-weather
tags:
- Weather
- Public APIs
website: https://hgbrasil.com/status/weather
---
