---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meteosource Air Quality Data Api Agentic Access
  operation_count: 8
  slug: meteosource-air-quality-data-api-agentic-access
  summary_line: 8 operations
api_count: 5
apis:
- description: Air quality and pollution forecasts.
  name: MeteoSource Air Quality Data API Air Quality API
  slug: meteosource-air-quality-data-api-air-quality-api
- description: Historical Time Machine data.
  name: MeteoSource Air Quality Data API History API
  slug: meteosource-air-quality-data-api-history-api
- description: Location lookup endpoints.
  name: MeteoSource Air Quality Data API Locations API
  slug: meteosource-air-quality-data-api-locations-api
- description: Tile-based weather and pollution maps.
  name: MeteoSource Air Quality Data API Maps API
  slug: meteosource-air-quality-data-api-maps-api
- description: Current and forecasted weather endpoints.
  name: MeteoSource Air Quality Data API Weather API
  slug: meteosource-air-quality-data-api-weather-api
artifact_total: 12
collections:
- collection_type: open
  name: MeteoSource Air Quality Data API
  slug: open-meteosource-air-quality-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meteosource-air-quality-data-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meteosource-air-quality-data-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meteosource-air-quality-data-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Meteosource
- group: start
  title: ''
  type: Portal
  url: https://www.meteosource.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meteosource.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.meteosource.com/client/register
- group: company
  title: ''
  type: Blog
  url: https://www.meteosource.com/blog
created: '2024-11-07'
description: MeteoSource provides an Air Quality API delivering hour-by-hour pollution data for any location on Earth, with forecasts up to 5 days ahead. The API also offers weather forecast data from multiple meteorological models.
finops:
- name: Meteosource Air Quality Data Api Finops
  service_category: API
  slug: meteosource-air-quality-data-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meteosource-air-quality-data-api.png
layout: provider
modified: '2026-05-19'
name: MeteoSource Air Quality Data API
nav: Providers
network: true
overview: 'MeteoSource Air Quality Data API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Air Quality API, History API, Locations API, and 2 more. Tagged areas include Air Quality, Environmental Data, Forecasting, and Weather.


  MeteoSource Air Quality Data API''s developer surface includes authentication, developer portal, pricing, signup flow, engineering blog, and 3 more developer resources.'
plans:
- name: Meteosource Air Quality Data Api Plans Pricing
  plan_count: 3
  slug: meteosource-air-quality-data-api-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Meteosource Air Quality Data Api Rate Limits
  slug: meteosource-air-quality-data-api-rate-limits
score:
  band: thin
  composite: 34.8
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/meteosource-air-quality-data-api/refs/heads/main/screenshots/meteosource-air-quality-data-api-2026-06-20T185257.png
security:
- kind: authentication
  name: Meteosource Air Quality Data Api Authentication
  slug: meteosource-air-quality-data-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Meteosource Air Quality Data Api Domain Security
  slug: meteosource-air-quality-data-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meteosource-air-quality-data-api
tags:
- Air Quality
- Environmental Data
- Forecasting
- Weather
website: https://www.meteosource.com/
---
