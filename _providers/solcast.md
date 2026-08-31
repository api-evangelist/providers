---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Solcast Agentic Access
  operation_count: 25
  slug: solcast-agentic-access
  summary_line: 25 operations · 4 acting
api_count: 1
apis:
- description: Live and forecast aggregated generation data for grid collections and sub-aggregations.
  name: Solcast Aggregations API
  slug: solcast-aggregations-api
- description: Solar irradiance, PV power, and weather forecasts up to 14 days ahead.
  name: Solcast Forecast Data API
  slug: solcast-forecast-data-api
- description: Historical solar radiation and weather data from 2007-01-01 up to 7 days before present.
  name: Solcast Historic Data API
  slug: solcast-historic-data-api
- description: Real-time solar irradiance, PV power, and weather estimated actuals (last 7 days, updated every 5 minutes).
  name: Solcast Live Data API
  slug: solcast-live-data-api
- description: CRUD management of registered PV power sites for use with the advanced PV power model.
  name: Solcast PV Power Sites API
  slug: solcast-pv-power-sites-api
- description: Typical Meteorological Year data computed from 2007 to 2023 satellite observations.
  name: Solcast TMY Data API
  slug: solcast-tmy-data-api
artifact_total: 41
collections:
- collection_type: postman
  name: Solcast Aggregations API
  slug: postman-solcast-aggregations-api
- collection_type: postman
  name: Solcast Aggregations Forecast Data API
  slug: postman-solcast-forecast-data-api
- collection_type: postman
  name: Solcast Aggregations Historic Data API
  slug: postman-solcast-historic-data-api
- collection_type: postman
  name: Solcast Aggregations Live Data API
  slug: postman-solcast-live-data-api
- collection_type: postman
  name: Solcast Aggregations PV Power Sites API
  slug: postman-solcast-pv-power-sites-api
- collection_type: postman
  name: Solcast Aggregations TMY Data API
  slug: postman-solcast-tmy-data-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Solcast Aggregations API
  slug: open-solcast-aggregations-api
- collection_type: open
  name: Solcast Aggregations Forecast Data API
  slug: open-solcast-forecast-data-api
- collection_type: open
  name: Solcast Aggregations Historic Data API
  slug: open-solcast-historic-data-api
- collection_type: open
  name: Solcast Aggregations Live Data API
  slug: open-solcast-live-data-api
- collection_type: open
  name: Solcast Aggregations PV Power Sites API
  slug: open-solcast-pv-power-sites-api
- collection_type: open
  name: Solcast Aggregations TMY Data API
  slug: open-solcast-tmy-data-api
- collection_type: open
  name: Solcast API
  slug: open-solcast
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/dnv/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/solcast/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solcast-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solcast-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solcast-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://solcast.com
- group: start
  title: ''
  type: Portal
  url: https://solcast.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.solcast.com.au/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/solcast
- group: other
  title: ''
  type: X
  url: https://twitter.com/solcastapi
- group: company
  title: ''
  type: Blog
  url: https://solcast.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://solcast.com/pricing/irradiance-weather
- group: operate
  title: ''
  type: StatusPage
  url: https://status.solcast.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/solcast-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/solcast-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/solcast-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://solcast.com/sdk
- group: start
  title: ''
  type: Signup
  url: https://toolkit.solcast.com.au/register
- group: operate
  title: ''
  type: ChangeLog
  url: https://solcast.com/changelog
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Solcast
- group: build
  title: ''
  type: API Toolkit
  url: https://toolkit.solcast.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solcast.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solcast.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://solcast.com/contact
created: '2025-05-02'
description: Solcast is a solar and renewable energy data company, acquired by DNV in 2023, that provides high-resolution, satellite-derived solar irradiance, PV power, weather forecasting, and historical climate data via a developer API. Its data covers live, forecast, historical, and typical meteorological year (TMY) datasets for rooftop PV, advanced PV, grid aggregations, and soiling models globally.
examples:
- key_count: 2
  name: Solcast Create Pv Power Site Example
  slug: solcast-create-pv-power-site-example
- key_count: 2
  name: Solcast Get Forecast Radiation And Weather Example
  slug: solcast-get-forecast-radiation-and-weather-example
- key_count: 2
  name: Solcast Get Forecast Rooftop Pv Power Example
  slug: solcast-get-forecast-rooftop-pv-power-example
- key_count: 2
  name: Solcast Get Historic Radiation And Weather Example
  slug: solcast-get-historic-radiation-and-weather-example
- key_count: 2
  name: Solcast Get Live Radiation And Weather Example
  slug: solcast-get-live-radiation-and-weather-example
- key_count: 2
  name: Solcast List Pv Power Sites Example
  slug: solcast-list-pv-power-sites-example
finops:
- name: Solcast Finops
  service_category: API
  slug: solcast-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solcast.png
json_schemas:
- name: PV Power Estimated
  property_count: 7
  slug: solcast-pv-power
- name: PV Power Site
  property_count: 14
  slug: solcast-pv-power-site
- name: Radiation and Weather Estimated
  property_count: 25
  slug: solcast-radiation-and-weather
json_structures:
- name: Solcast Pv Power Site Structure
  property_count: 0
  slug: solcast-pv-power-site-structure
- name: Solcast Pv Power Structure
  property_count: 0
  slug: solcast-pv-power-structure
- name: Solcast Radiation And Weather Structure
  property_count: 0
  slug: solcast-radiation-and-weather-structure
jsonld:
- class_count: 0
  name: Solcast Context
  property_count: 56
  slug: solcast-context
layout: provider
modified: '2026-06-13'
name: Solcast
nav: Providers
network: true
overview: 'Solcast publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Aggregations API, Forecast Data API, Historic Data API, and 3 more. Tagged areas include Solar, Energy, Forecasting, Irradiance, and Weather.


  The Solcast catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Solcast''s developer surface includes authentication, developer portal, documentation, engineering blog, pricing, signup flow, changelog, and 17 more developer resources.'
plans:
- name: Solcast Plans Pricing
  plan_count: 5
  slug: solcast-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 6
  name: Solcast Rate Limits
  slug: solcast-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Solcast API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: solcast-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Solcast API Rules
  rule_count: 18
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 12
  slug: solcast-rules
score:
  band: strong
  composite: 56.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 41.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 76.9
    developer_ergonomics: 57.1
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 28.9
  previous_composite: 56.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solcast/refs/heads/main/screenshots/solcast-2026-06-20T194150.png
security:
- kind: authentication
  name: Solcast Authentication
  slug: solcast-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Solcast Domain Security
  slug: solcast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: solcast
tags:
- Solar
- Energy
- Forecasting
- Irradiance
- Weather
- Renewable Energy
- PV Power
website: https://solcast.com
---
