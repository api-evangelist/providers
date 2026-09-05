---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Yr No Agentic Access
  operation_count: 38
  slug: yr-no-agentic-access
  summary_line: 38 operations
api_count: 5
apis:
- description: REST API for historical meteorological observation data from weather stations worldwide, maintained by MET Norway. Access time-series temperature, precipitation, wind, and other observations.
  name: Frost API
  slug: frost-api
- description: Forecasts of air quality for locations in Norway, including concentrations of PM2.5, PM10, NO2, and ozone, with daily and hourly granularity.
  name: Air Quality Forecast API
  slug: air-quality-forecast-api
- baseURL: https://api.met.no/weatherapi/locationforecast/2.0/
  baseurl_source: declared
  description: Weather alert endpoints
  name: Yr alerts API
  slug: yr-no-alerts-api
- baseURL: https://api.met.no/weatherapi/locationforecast/2.0/
  baseurl_source: declared
  description: Forecast data endpoints
  name: Yr data API
  slug: yr-no-data-api
- baseURL: https://api.met.no/weatherapi/locationforecast/2.0/
  baseurl_source: declared
  description: Service metadata endpoints
  name: Yr metadata API
  slug: yr-no-metadata-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Locationforecast alerts API
  slug: open-yr-no-alerts-api
- collection_type: open
  name: Locationforecast alerts data API
  slug: open-yr-no-data-api
- collection_type: open
  name: Locationforecast alerts metadata API
  slug: open-yr-no-metadata-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/yr-no-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yr-no-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yr-no-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.yr.no/en
- group: docs
  title: ''
  type: Documentation
  url: https://developer.yr.no/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/YR
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/metno
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/met-norway/
- group: company
  title: ''
  type: Blog
  url: https://developer.yr.no/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.yr.no/doc/TermsOfService/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.yr.no/doc/TermsOfService/
- group: commercial
  title: ''
  type: License
  url: https://developer.yr.no/doc/License/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.met.no/en/About-us/privacy
- group: other
  title: ''
  type: X
  url: https://twitter.com/meteorologene
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/yrno-22652235447/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.yr.no/doc/GettingStarted/
- group: commercial
  title: ''
  type: Plans
  url: plans/yr-no-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/yr-no-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/yr-no-finops.yml
created: '2026-06-13'
description: Yr is a weather service from the Norwegian Meteorological Institute (MET Norway) and the Norwegian Broadcasting Corporation (NRK), providing free, high-quality weather forecasts for locations worldwide via a simple REST interface. The MET Weather API offers a comprehensive suite of products including location-based forecasts, weather alerts, nowcasts, ocean forecasts, aviation weather, sunrise and sun event calculations, radar imagery, and historical meteorological observation data. All data is open under CC BY 4.0 and requires only a User-Agent identification header — no API key or account is needed.
examples:
- key_count: 3
  name: Yr No Compact Forecast Example
  slug: yr-no-compact-forecast-example
- key_count: 2
  name: Yr No Metalert Example
  slug: yr-no-metalert-example
- key_count: 3
  name: Yr No Oceanforecast Example
  slug: yr-no-oceanforecast-example
- key_count: 2
  name: Yr No Sunrise Example
  slug: yr-no-sunrise-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yr-no.png
json_schemas:
- name: MET Norway MetAlerts GeoJSON Schema
  property_count: 2
  slug: yr-no-alert
- name: MET Norway Forecast Response Schema
  property_count: 3
  slug: yr-no-forecast
jsonld:
- class_count: 21
  name: Yr No Context
  property_count: 48
  slug: yr-no-context
layout: provider
modified: '2026-06-13'
name: Yr
nav: Providers
network: true
overview: 'Yr publishes 3 APIs on the [APIs.io](https://apis.io/) network: alerts API, data API, and metadata API. Tagged areas include Weather, Forecast, Meteorology, Climate, and Norway.


  The Yr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Yr''s developer surface includes documentation, engineering blog, pricing, getting-started guide, and 15 more developer resources.'
plans:
- name: Yr No Plans Pricing
  plan_count: 1
  slug: yr-no-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Yr No Rate Limits
  slug: yr-no-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Yr API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: yr-no-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.3
    catalog_earned_first_party: 0.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 9.8
    contract_quality: 58.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 42.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yr-no/refs/heads/main/screenshots/yr-no-2026-06-20T201749.png
security:
- kind: domain-security
  name: Yr No Domain Security
  slug: yr-no-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Yr No Vulnerability Disclosure
  slug: yr-no-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yr-no
tags:
- Weather
- Forecast
- Meteorology
- Climate
- Norway
- Nordic
- Open Data
- Aviation Weather
- Marine Weather
- Alerts
website: https://www.yr.no/en
---
