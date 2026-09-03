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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meteosource Air Quality Data Api Agentic Access
  operation_count: 8
  slug: meteosource-air-quality-data-api-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Air quality and pollution forecasts.
  name: MeteoSource Air Quality Data API Air Quality API
  slug: meteosource-air-quality-data-api-air-quality-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Historical Time Machine data.
  name: MeteoSource Air Quality Data API History API
  slug: meteosource-air-quality-data-api-history-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Location lookup endpoints.
  name: MeteoSource Air Quality Data API Locations API
  slug: meteosource-air-quality-data-api-locations-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Tile-based weather and pollution maps.
  name: MeteoSource Air Quality Data API Maps API
  slug: meteosource-air-quality-data-api-maps-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Current and forecasted weather endpoints.
  name: MeteoSource Air Quality Data API Weather API
  slug: meteosource-air-quality-data-api-weather-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MeteoSource Data Air Quality API
  slug: open-meteosource-air-quality-data-api-air-quality-api
- collection_type: open
  name: MeteoSource Data Air Quality History API
  slug: open-meteosource-air-quality-data-api-history-api
- collection_type: open
  name: MeteoSource Data Air Quality Locations API
  slug: open-meteosource-air-quality-data-api-locations-api
- collection_type: open
  name: MeteoSource Data Air Quality Maps API
  slug: open-meteosource-air-quality-data-api-maps-api
- collection_type: open
  name: MeteoSource Data Air Quality Weather API
  slug: open-meteosource-air-quality-data-api-weather-api
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
random_paper: 0
rate_limits:
- limit_count: 5
  name: Meteosource Air Quality Data Api Rate Limits
  slug: meteosource-air-quality-data-api-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
