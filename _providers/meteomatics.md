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
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Meteomatics Agentic Access
  operation_count: 7
  slug: meteomatics-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Obtain OAuth2 bearer tokens
  name: Meteomatics Authentication API
  slug: meteomatics-authentication-api
- description: Account usage statistics
  name: Meteomatics User API
  slug: meteomatics-user-api
- description: Query weather parameters for point, grid, multi-location, and route requests
  name: Meteomatics Weather Data API
  slug: meteomatics-weather-data-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meteomatics Weather Authentication API
  slug: open-meteomatics-authentication-api
- collection_type: open
  name: Meteomatics Weather Authentication User API
  slug: open-meteomatics-user-api
- collection_type: open
  name: Meteomatics Weather Authentication Weather Data API
  slug: open-meteomatics-weather-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meteomatics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meteomatics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meteomatics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.meteomatics.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.meteomatics.com/en/api/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/meteomatics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meteomatics
- group: company
  title: ''
  type: Blog
  url: https://www.meteomatics.com/en/tech-blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meteomatics.com/en/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://sanes.co
- group: other
  title: ''
  type: X
  url: https://twitter.com/meteomatics
- group: commercial
  title: ''
  type: Plans
  url: plans/meteomatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meteomatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/meteomatics-finops.yml
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.meteomatics.com/en/service-level-agreement/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/meteomatics-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/meteomatics-context.jsonld
created: '2026-06-12'
description: Meteomatics is a Swiss weather technology company offering a REST and WebSocket Weather API that provides hyperlocal forecasts, historical weather data back to 1940, climate scenarios to 2100, marine conditions, and environmental parameters at up to 1km native resolution. The API exposes over 1,800 weather parameters across global, regional, oceanic, and AI-based models, supporting point, multi-location, route, and polygon queries with output in JSON, CSV, XML, PNG, GeoTIFF, and NetCDF formats.
examples:
- key_count: 3
  name: Meteomatics Point Query Example
  slug: meteomatics-point-query-example
finops:
- name: Meteomatics Finops
  service_category: ''
  slug: meteomatics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meteomatics.png
json_schemas:
- name: Meteomatics Weather API Response
  property_count: 5
  slug: meteomatics-weather-response
jsonld:
- class_count: 16
  name: Meteomatics Context
  property_count: 25
  slug: meteomatics-context
layout: provider
modified: '2026-06-12'
name: Meteomatics
nav: Providers
network: true
overview: 'Meteomatics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, User API, and Weather Data API. Tagged areas include Weather, Forecast, Climate, Historical Weather, and Marine.


  The Meteomatics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Meteomatics'' developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Meteomatics Plans Pricing
  plan_count: 4
  slug: meteomatics-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Meteomatics Rate Limits
  slug: meteomatics-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Meteomatics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: meteomatics-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 37.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 71.4
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meteomatics/refs/heads/main/screenshots/meteomatics-2026-06-20T185254.png
security:
- kind: authentication
  name: Meteomatics Authentication
  slug: meteomatics-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Meteomatics Domain Security
  slug: meteomatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meteomatics
tags:
- Weather
- Forecast
- Climate
- Historical Weather
- Marine
- Environmental Data
- Hyperlocal
- Meteorology
- Time Series
- Geospatial
website: https://www.meteomatics.com
---
