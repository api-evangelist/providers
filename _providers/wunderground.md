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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wunderground Agentic Access
  operation_count: 8
  slug: wunderground-agentic-access
  summary_line: 8 operations
api_count: 4
apis:
- description: Weather forecasts based on PWS location
  name: Weather Underground Forecast API
  slug: wunderground-forecast-api
- description: Historical PWS observations and daily summaries
  name: Weather Underground Historical API
  slug: wunderground-historical-api
- description: PWS station location lookup
  name: Weather Underground Location API
  slug: wunderground-location-api
- description: Current and real-time PWS observations
  name: Weather Underground Observations API
  slug: wunderground-observations-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Weather Underground PWS Forecast API
  slug: open-wunderground-forecast-api
- collection_type: open
  name: Weather Underground PWS Forecast Historical API
  slug: open-wunderground-historical-api
- collection_type: open
  name: Weather Underground PWS Forecast Location API
  slug: open-wunderground-location-api
- collection_type: open
  name: Weather Underground PWS Forecast Observations API
  slug: open-wunderground-observations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wunderground-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wunderground-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wunderground-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wunderground-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wunderground.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.wunderground.com/member/api-keys
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/wunderground-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wunderground-llc
- group: company
  title: ''
  type: Blog
  url: https://www.wunderground.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wunderground.com/member/api-keys
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.com/wunderground.com
- group: other
  title: ''
  type: X
  url: https://x.com/wunderground
- group: commercial
  title: ''
  type: Plans
  url: plans/wunderground-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wunderground-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wunderground-finops.yml
created: '2026-06-13'
description: Weather Underground operates a personal weather station network of 250,000+ stations worldwide, providing hyperlocal weather data via a REST API. The PWS API (hosted at api.weather.com) offers authenticated access to current conditions, historical observations, 5-day forecasts, and location lookup for registered station contributors. API keys are free for PWS owners who upload data to the network.
examples:
- key_count: 17
  name: 5 Day Forecast
  slug: 5-day-forecast
- key_count: 1
  name: Current Observations
  slug: current-observations
- key_count: 1
  name: Daily Summary
  slug: daily-summary
finops:
- name: Wunderground Finops
  service_category: ''
  slug: wunderground-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wunderground.png
json_schemas:
- name: PWS Observation
  property_count: 20
  slug: observation
jsonld:
- class_count: 0
  name: Wunderground Context
  property_count: 66
  slug: wunderground-context
layout: provider
modified: '2026-06-13'
name: Weather Underground
nav: Providers
network: true
overview: 'Weather Underground publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Forecast API, Historical API, Location API, and 1 more. Tagged areas include Weather, Personal Weather Stations, Hyperlocal, Observations, and Forecasts.


  The Weather Underground catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Weather Underground''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Wunderground Plans Pricing
  plan_count: 1
  slug: wunderground-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Wunderground Rate Limits
  slug: wunderground-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Weather Underground API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: wunderground-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.3
  delta: -6.1
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 42.1
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wunderground/refs/heads/main/screenshots/wunderground-2026-06-20T201644.png
security:
- kind: authentication
  name: Wunderground Authentication
  slug: wunderground-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wunderground Domain Security
  slug: wunderground-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Wunderground Vulnerability Disclosure
  slug: wunderground-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wunderground
tags:
- Weather
- Personal Weather Stations
- Hyperlocal
- Observations
- Forecasts
- Historical Data
- REST API
website: https://www.wunderground.com
---
