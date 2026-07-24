---
access_model:
  confidence: medium
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: true
  try_now: true
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: RESTful weather data API providing access to 60+ endpoints for current conditions, forecasts, observations, severe weather alerts, historical data, air quality, lightning, maritime weather, road condi
  name: Xweather Weather API
  slug: weather-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerisweather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xweather.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.xweather.com/docs/weather-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/aerisweather
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aerisweather
- group: company
  title: ''
  type: Blog
  url: https://www.xweather.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xweather.com/products/weather-api
- group: operate
  title: ''
  type: StatusPage
  url: https://xweatherstatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/xweather_
- group: commercial
  title: ''
  type: Plans
  url: plans/aerisweather-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aerisweather-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aerisweather-finops.yml
created: '2026-06-13'
description: Comprehensive weather data REST API providing forecasts, observations, severe weather alerts, historical data, satellite imagery, and maps for global locations. Now operating as Xweather (acquired by Vaisala in 2022), the platform offers 60+ endpoints covering current conditions, forecasts up to 15 days, air quality, lightning, maritime weather, road conditions, wildfires, earthquakes, and tropical cyclones. Developer toolkits are available for JavaScript, Python, iOS, and Android.
finops:
- name: Aerisweather Finops
  service_category: ''
  slug: aerisweather-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aerisweather.png
layout: provider
modified: '2026-06-13'
name: AerisWeather
nav: Providers
network: true
overview: 'AerisWeather publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Weather, Forecasts, Climate, Severe Weather, and Air Quality.


  AerisWeather''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Aerisweather Plans Pricing
  plan_count: 6
  slug: aerisweather-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Aerisweather Rate Limits
  slug: aerisweather-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aerisweather/refs/heads/main/screenshots/aerisweather-2026-06-20T165453.png
security:
- kind: domain-security
  name: Aerisweather Domain Security
  slug: aerisweather-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aerisweather
tags:
- Weather
- Forecasts
- Climate
- Severe Weather
- Air Quality
- Satellite
- Mapping
- REST
website: https://www.xweather.com
---
