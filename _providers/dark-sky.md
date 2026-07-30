---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dark Sky Agentic Access
  operation_count: 2
  slug: dark-sky-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Current and forecast weather data for a given location
  name: Dark Sky Forecast API
  slug: dark-sky-forecast-api
- description: Historical or future weather data for a specific point in time
  name: Dark Sky Time Machine API
  slug: dark-sky-time-machine-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dark-sky-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dark-sky-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dark-sky-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://darksky.net
- group: docs
  title: ''
  type: Documentation
  url: https://darksky.net/dev/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/darkskyapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dark-sky
- group: company
  title: ''
  type: Blog
  url: https://blog.darksky.net
- group: commercial
  title: ''
  type: Pricing
  url: https://darksky.net/dev
- group: operate
  title: ''
  type: StatusPage
  url: https://darksky.net/dev/console
- group: other
  title: ''
  type: X
  url: https://x.com/darkskyapp
- group: commercial
  title: ''
  type: Plans
  url: plans/dark-sky-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dark-sky-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dark-sky-finops.yml
created: '2026-06-13'
description: Dark Sky is a hyperlocal weather forecast REST API (now part of Apple) that provided minute-by-minute precipitation forecasts, hourly weather conditions, and multi-day outlooks powered by machine-learning models. The API delivered real-time and historical weather data for any latitude and longitude worldwide, including current conditions, 60-minute minutely precipitation intensity, 48-hour hourly forecasts, and 7-day daily summaries. It was acquired by Apple in March 2020; new developer signups closed immediately, and the API was permanently shut down on March 31, 2023. Apple's WeatherKit REST API is the successor service.
examples:
- key_count: 10
  name: Forecast Response
  slug: forecast-response
- key_count: 8
  name: Time Machine Response
  slug: time-machine-response
finops:
- name: Dark Sky Finops
  service_category: ''
  slug: dark-sky-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dark-sky.png
json_schemas:
- name: Dark Sky Forecast Response
  property_count: 10
  slug: dark-sky-forecast-response
jsonld:
- class_count: 0
  name: Dark Sky Context
  property_count: 46
  slug: dark-sky-context
layout: provider
modified: '2026-06-13'
name: Dark Sky
nav: Providers
network: true
overview: 'Dark Sky publishes 2 APIs on the [APIs.io](https://apis.io/) network: Forecast API and Time Machine API. Tagged areas include Weather, Forecast, Hyperlocal, Precipitation, and Machine Learning.


  The Dark Sky catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dark Sky''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Dark Sky Plans Pricing
  plan_count: 2
  slug: dark-sky-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 2
  name: Dark Sky Rate Limits
  slug: dark-sky-rate-limits
rules:
- name: Dark Sky API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: dark-sky-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.0
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.7
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dark-sky/refs/heads/main/screenshots/dark-sky-2026-06-20T175456.png
security:
- kind: authentication
  name: Dark Sky Authentication
  slug: dark-sky-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dark Sky Domain Security
  slug: dark-sky-domain-security
  summary_line: TLSv1.3
slug: dark-sky
tags:
- Weather
- Forecast
- Hyperlocal
- Precipitation
- Machine Learning
- REST
- Apple
website: https://darksky.net
---
