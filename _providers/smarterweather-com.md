---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Smarterweather Com Agentic Access
  operation_count: 78
  slug: smarterweather-com-agentic-access
  summary_line: 78 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Agriculture-derived indices (Growing Degree Units / GDD) computed on read from stored daily temperature extremes.
  name: smarterweather-com Agriculture API
  slug: smarterweather-com-agriculture-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: NWS weather alert lookups.
  name: smarterweather-com Alerts API
  slug: smarterweather-com-alerts-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: 'Climatology: long-period day-of-year statistics describing what is typical at a location, as distinct from what is forecast.'
  name: smarterweather-com Climate API
  slug: smarterweather-com-climate-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Forward, reverse, and typeahead geocoding for locations within the 50 US states and DC. Forward and typeahead results omit places outside it (Puerto Rico, Guam and the other territories); reverse geoc
  name: smarterweather-com Geocode API
  slug: smarterweather-com-geocode-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: 'Forecaster guidance products (SPC mesoscale discussions, WPC precipitation discussions, area forecast discussions, hazardous weather outlooks, short-term NOW). GeoJSON overlays under `/v1/guidance/*` '
  name: smarterweather-com Guidance API
  slug: smarterweather-com-guidance-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Service health.
  name: smarterweather-com Health API
  slug: smarterweather-com-health-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: 'Cross-cutting platform endpoints: the data catalog, platform status, deprecations.'
  name: smarterweather-com Meta API
  slug: smarterweather-com-meta-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Surface observations and upper-air soundings sampled at or nearest to a point.
  name: smarterweather-com Observations API
  slug: smarterweather-com-observations-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Gridded / vector weather products and derived summaries, such as risk-zone population exposure.
  name: smarterweather-com Products API
  slug: smarterweather-com-products-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Severe-weather tracking products (storm tracks, storm reports, record events).
  name: smarterweather-com Storms API
  slug: smarterweather-com-storms-api
- baseURL: https://api.smarterweather.com
  baseurl_source: declared
  description: Public weather data endpoints.
  name: smarterweather-com Weather API
  slug: smarterweather-com-weather-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/smarterweather-com/agentic-access/smarterweather-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smarterweather-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/smarterweather-com/rate-limits/smarterweather-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smarterweather-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smarterweather-com/plans/smarterweather-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smarterweather-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/rules/smarterweather-com-rules.yml
  title: ''
  type: Spectral
  url: rules/smarterweather-com-rules.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/json-ld/smarterweather-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/smarterweather-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/smarterweather-com/vocabulary/smarterweather-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/smarterweather-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/smarterweather-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/data-model/smarterweather-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/smarterweather-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/conventions/smarterweather-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/smarterweather-com-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://developers.smarterweather.com/authentication/leaked-keys/
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/authentication/smarterweather-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smarterweather-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/smarterweather-com/lifecycle/smarterweather-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/smarterweather-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/lifecycle/smarterweather-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/smarterweather-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/errors/smarterweather-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/smarterweather-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/smarterweather-com/conformance/smarterweather-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/smarterweather-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/smarterweather-com/llms/smarterweather-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/smarterweather-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/smarterweather-com/mcp/smarterweather-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/smarterweather-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/well-known/smarterweather-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smarterweather-com-security.txt
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/well-known/smarterweather-com-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smarterweather-com-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/well-known/smarterweather-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/smarterweather-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/smarterweather-com/well-known/smarterweather-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/smarterweather-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/smarterweather-com/hosts/smarterweather-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smarterweather-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/smarterweather-com/vendors/smarterweather-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smarterweather-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/smarterweather-com/packages/smarterweather-com-packages.yml
  title: ''
  type: SDKs
  url: packages/smarterweather-com-packages.yml
- group: build
  href: https://artifacts.apis.io/smarterweather-com/packages/smarterweather-com-packages.yml
  title: ''
  type: Packages
  url: packages/smarterweather-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://smarterweather.com/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://developers.smarterweather.com/api/reference
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/security/smarterweather-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/smarterweather-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/smarterweather-com/security/smarterweather-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smarterweather-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smarterweather.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.smarterweather.com/overview/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.smarterweather.com/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.smarterweather.com/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://smarterweather.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://smarterweather.com/app-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smarterweather.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smarterweather.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smarterweather.com/privacy/
created: '2026-10-30'
description: Smarter Weather LLC provides weather data and forecasting services built on NOAA and National Weather Service observations. Their mission is to understand the impact of weather on every person and organization, delivering proactive, personalized, and trusted guidance. They turn raw weather data into clear, actionable insights through products such as a weather app, a meteorologist agent, and a developer platform offering APIs for agents. Based in Chicago, Illinois, they also publish forecast accuracy scores and operate a status page.
image: https://smarterweather.com/logo.svg
json_schemas:
- name: AlertDetail
  property_count: 30
  slug: smarterweather-com-alert-detail
- name: OutlookDetail
  property_count: 6
  slug: smarterweather-com-outlook-detail
- name: PointValue
  property_count: 9
  slug: smarterweather-com-point-value
- name: RouteWeatherResponse
  property_count: 5
  slug: smarterweather-com-route-weather-response
- name: WeatherBatchRequest
  property_count: 9
  slug: smarterweather-com-weather-batch-request
- name: Weather
  property_count: 17
  slug: smarterweather-com-weather
jsonld:
- class_count: 120
  name: Smarterweather Com Context
  property_count: 481
  slug: smarterweather-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.smarterweather.com.
  name: smarterweather-com MCP Server
  slug: smarterweather-com-mcp-yml
modified: '2026-10-30'
name: smarterweather-com
nav: Providers
network: true
overview: 'smarterweather-com publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agriculture API, Alerts API, Climate API, and 8 more. Tagged areas include Company, Weather, Data, Forecasting, and Climate.


  The smarterweather-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  smarterweather-com''s developer surface includes authentication, changelog, API reference, documentation, getting-started guide, support, pricing, and 31 more developer resources.'
plans:
- name: Smarterweather Com Plans Pricing
  plan_count: 5
  slug: smarterweather-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 6
  name: Smarterweather Com Rate Limits
  slug: smarterweather-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: smarterweather-com API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 1
  slug: smarterweather-com-rules
scopes:
- name: Smarterweather Com Scopes
  scope_count: 0
  slug: smarterweather-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 68.1
    developer_ergonomics: 46.9
    discoverability: 75.0
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/smarterweather-com/smarterweather-com-2026-11-03T143340.png
security:
- kind: authentication
  name: Smarterweather Com Authentication
  slug: smarterweather-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Smarterweather Com Domain Security
  slug: smarterweather-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smarterweather Com Vulnerability Disclosure
  slug: smarterweather-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: smarterweather-api
  slug: smarterweather-com-smarterweather-api
- name: smarterweather-mcp
  slug: smarterweather-com-smarterweather-mcp
- name: smarterweather-onboarding
  slug: smarterweather-com-smarterweather-onboarding
slug: smarterweather-com
tags:
- Company
- Weather
- Data
- Forecasting
- Climate
website: https://smarterweather.com/
---
