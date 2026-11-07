---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
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
  description: Location lookup endpoints.
  name: MeteoSource Air Quality Data API Locations API
  slug: meteosource-air-quality-data-api-locations-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: Current and forecasted weather endpoints.
  name: MeteoSource Air Quality Data API Weather API
  slug: meteosource-air-quality-data-api-weather-api
- baseURL: https://www.meteosource.com/api/v1
  baseurl_source: declared
  description: PNG map images of weather variables (e.g. temperature, precipitation, cloud cover) for a given area and time, plus the base map tileset used to render them as an interactive map.
  name: MeteoSource Air Quality Data API Weather maps API
  slug: meteosource-air-quality-data-api-weather-maps-api
artifact_total: 16
collections:
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
- group: commercial
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/plans/meteosource-air-quality-data-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meteosource-air-quality-data-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/rate-limits/meteosource-air-quality-data-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meteosource-air-quality-data-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/finops/meteosource-air-quality-data-api-finops.yml
  title: ''
  type: FinOps
  url: finops/meteosource-air-quality-data-api-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.meteosource.com/
- group: agent
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/agentic-access/meteosource-air-quality-data-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meteosource-air-quality-data-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/security/meteosource-air-quality-data-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meteosource-air-quality-data-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/meteosource-air-quality-data-api/authentication/meteosource-air-quality-data-api-authentication.yml
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
- has_sources: false
  method: generated
  name: Meteosource Air Quality Data Api Finops
  primary_unit: request
  service_category: API
  slug: meteosource-air-quality-data-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meteosource-air-quality-data-api.png
layout: provider
modified: '2026-05-19'
name: MeteoSource Air Quality Data API
nav: Providers
network: true
overview: 'MeteoSource Air Quality Data API publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Locations API, Weather API, and Weather maps API. Tagged areas include Air Quality, Environmental Data, Forecasting, and Weather.


  The MeteoSource Air Quality Data API catalog on APIs.io includes 1 Spectral governance ruleset.


  MeteoSource Air Quality Data API''s developer surface includes authentication, developer portal, pricing, signup flow, engineering blog, and 7 more developer resources.'
plans:
- name: Meteosource Air Quality Data Api Plans Pricing
  plan_count: 3
  slug: meteosource-air-quality-data-api-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Meteosource Air Quality Data Api Rate Limits
  slug: meteosource-air-quality-data-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: MeteoSource Air Quality Data API API Rules
  rule_count: 57
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 3
  slug: meteosource-air-quality-data-api-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 10.5
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 33.3
      total: 9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/meteosource-air-quality-data-api/meteosource-air-quality-data-api-2026-06-20T185257.png
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
