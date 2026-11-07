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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Forecast Solar Agentic Access
  operation_count: 56
  slug: forecast-solar-agentic-access
  summary_line: 56 operations
api_count: 1
apis:
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Chart widget (registered users)
  name: Forecast.Solar Chart API
  slug: forecast-solar-chart-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Solar production for clear sky condition (registered users)
  name: Forecast.Solar Clear sky API
  slug: forecast-solar-clear-sky-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Solar production forecast
  name: Forecast.Solar Forecast API
  slug: forecast-solar-forecast-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Historic average solar production (registered users)
  name: Forecast.Solar History API
  slug: forecast-solar-history-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Miscellaneous functions
  name: Forecast.Solar Misc API
  slug: forecast-solar-misc-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Functions for Professional account holders
  name: Forecast.Solar Professional API
  slug: forecast-solar-professional-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Public functions
  name: Forecast.Solar Public API
  slug: forecast-solar-public-api
- baseURL: https://api.forecast.solar
  baseurl_source: declared
  description: Weather forecast (registered users)
  name: Forecast.Solar Weather API
  slug: forecast-solar-weather-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/forecast-solar/agentic-access/forecast-solar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/forecast-solar-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/forecast-solar/rules/forecast-solar-rules.yml
  title: ''
  type: Spectral
  url: rules/forecast-solar-rules.yml
- group: design
  href: https://artifacts.apis.io/forecast-solar/vocabulary/forecast-solar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/forecast-solar-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/forecast-solar/data-model/forecast-solar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/forecast-solar-data-model.yml
- group: design
  href: https://artifacts.apis.io/forecast-solar/errors/forecast-solar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/forecast-solar-problem-types.yml
- group: design
  href: https://artifacts.apis.io/forecast-solar/conformance/forecast-solar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/forecast-solar-conformance.yml
- group: other
  href: https://artifacts.apis.io/forecast-solar/hosts/forecast-solar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/forecast-solar-hosts.yml
- group: build
  href: https://artifacts.apis.io/forecast-solar/packages/forecast-solar-packages.yml
  title: ''
  type: SDKs
  url: packages/forecast-solar-packages.yml
- group: build
  href: https://artifacts.apis.io/forecast-solar/packages/forecast-solar-packages.yml
  title: ''
  type: Packages
  url: packages/forecast-solar-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forecast.solar/
- group: auth
  href: https://artifacts.apis.io/forecast-solar/security/forecast-solar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/forecast-solar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forecast.solar/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.forecast.solar/
- group: docs
  title: ''
  type: APIReference
  url: https://api.forecast.solar/swagger.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.forecast.solar/doku.php?id=start
- group: operate
  title: ''
  type: Support
  url: https://support.knutkohl.consulting/
created: '2026-10-28'
description: Forecast.Solar provides a RESTful API delivering solar production forecasts and weather data for photovoltaic installations worldwide. Leveraging PVGIS irradiation data and multiple weather services, the service offers hourly to 15‑minute resolution forecasts, historic averages, and clear‑sky estimates. It supports professional accounts with advanced features such as time‑window calculations and chart generation, enabling developers and energy managers to integrate solar forecasting into applications and automation workflows.
image: https://forecast.solar/images/og_image.jpg
layout: provider
modified: '2026-10-28'
name: Forecast.Solar
nav: Providers
network: true
overview: 'Forecast.Solar publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chart API, Clear sky API, Forecast API, and 5 more. Tagged areas include Company, Solar, Forecast, and Renewable Energy.


  The Forecast.Solar catalog on APIs.io includes 1 Spectral governance ruleset.


  Forecast.Solar''s developer surface includes documentation, API reference, getting-started guide, support, and 12 more developer resources.'
plans:
- name: Forecast Solar Plans Pricing
  plan_count: 6
  slug: forecast-solar-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Forecast Solar Rate Limits
  slug: forecast-solar-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Forecast.Solar API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: forecast-solar-rules
scopes:
- name: Forecast Solar Scopes
  scope_count: 0
  slug: forecast-solar-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 57.8
    catalog_earned_first_party: 20.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 35.1
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 28.9
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/forecast-solar/forecast-solar-2026-11-03T132235.png
security:
- kind: authentication
  name: Forecast Solar Authentication
  slug: forecast-solar-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Forecast Solar Domain Security
  slug: forecast-solar-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: weather-forecast
  slug: forecast-solar-weather-forecast
slug: forecast-solar
tags:
- Company
- Solar
- Forecast
- Renewable Energy
website: https://forecast.solar/
---
