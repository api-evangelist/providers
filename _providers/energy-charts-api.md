---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 25.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Energy Charts Api Agentic Access
  operation_count: 17
  slug: energy-charts-api-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Import/export values
  name: Energy Charts API Import Export API
  slug: energy-charts-api-import-export-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Query power values
  name: Energy Charts API Power API
  slug: energy-charts-api-power-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Query price values
  name: Energy Charts API Prices API
  slug: energy-charts-api-prices-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Renewable shares
  name: Energy Charts API Ren Share API
  slug: energy-charts-api-ren-share-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: The Energy Charts API API from Energy Charts API — 1 operation(s) for energy charts api.
  name: Energy Charts API Energy Charts API
  slug: energy-charts-api-energy-charts-api-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Import/export values in the uniform, machine-readable v2 envelope
  name: Energy Charts API import_export v2 API
  slug: energy-charts-api-import-export-v2-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Power values in the uniform, machine-readable v2 envelope
  name: Energy Charts API power v2 API
  slug: energy-charts-api-power-v2-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Price values in the uniform, machine-readable v2 envelope
  name: Energy Charts API prices v2 API
  slug: energy-charts-api-prices-v2-api
- baseURL: https://api.energy-charts.info
  baseurl_source: declared
  description: Renewable shares in the uniform, machine-readable v2 envelope
  name: Energy Charts API ren_share v2 API
  slug: energy-charts-api-ren-share-v2-api
artifact_total: 20
collections:
- collection_type: open
  name: Energy-Charts import_export API
  slug: open-energy-charts-api-import-export-api
- collection_type: open
  name: Energy-Charts import_export power API
  slug: open-energy-charts-api-power-api
- collection_type: open
  name: Energy-Charts import_export prices API
  slug: open-energy-charts-api-prices-api
- collection_type: open
  name: Energy-Charts import_export ren_share API
  slug: open-energy-charts-api-ren-share-api
- collection_type: open
  name: Energy-Charts API
  slug: open-energy-charts-api
common:
- group: commercial
  href: https://artifacts.apis.io/energy-charts-api/plans/energy-charts-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/energy-charts-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/energy-charts-api/rate-limits/energy-charts-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/energy-charts-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/energy-charts-api/finops/energy-charts-api-finops.yml
  title: ''
  type: FinOps
  url: finops/energy-charts-api-finops.yml
- group: agent
  href: https://artifacts.apis.io/energy-charts-api/agentic-access/energy-charts-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/energy-charts-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/energy-charts-api/security/energy-charts-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/energy-charts-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.energy-charts.info/
- group: other
  title: ''
  type: Provider
  url: https://www.ise.fraunhofer.de/
created: '2025-05-02'
description: The Energy-Charts API, provided by Fraunhofer ISE, delivers European energy data including electricity production by source, day-ahead spot market prices, cross-border electricity trading and physical flows, grid frequency, installed capacity, and renewable energy share forecasts. It covers more than 40 European countries and bidding zones, supports ISO 8601, daily, and UNIX timestamp formats, and is largely licensed under CC BY 4.0.
finops:
- has_sources: false
  method: generated
  name: Energy Charts Api Finops
  primary_unit: request
  service_category: API
  slug: energy-charts-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/energy-charts-api.png
layout: provider
modified: '2026-05-19'
name: Energy Charts API
nav: Providers
network: true
overview: 'Energy Charts API publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Import Export API, Power API, Prices API, and 6 more. Tagged areas include Energy, Electricity, Renewables, Grid, and Europe.


  The Energy Charts API catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Energy Charts Api Plans Pricing
  plan_count: 3
  slug: energy-charts-api-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Energy Charts Api Rate Limits
  slug: energy-charts-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Energy Charts API API Rules
  rule_count: 59
  severity_counts:
    error: 51
    hint: 0
    info: 2
    warn: 6
  slug: energy-charts-api-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 46.3
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 22.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 64.3
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/energy-charts-api/energy-charts-api-2026-06-20T180710.png
security:
- kind: domain-security
  name: Energy Charts Api Domain Security
  slug: energy-charts-api-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: energy-charts-api
tags:
- Energy
- Electricity
- Renewables
- Grid
- Europe
- Power
- Pricing
- Forecast
website: https://www.energy-charts.info/
---
