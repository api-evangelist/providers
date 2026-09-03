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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fueleconomy Agentic Access
  operation_count: 12
  slug: fueleconomy-agentic-access
  summary_line: 12 operations
api_count: 1
apis:
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: EPA tailpipe emissions data per vehicle
  name: FuelEconomy.gov Emissions API
  slug: fueleconomy-emissions-api
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: Current US fuel prices used by the FuelEconomy.gov platform
  name: FuelEconomy.gov Fuel Prices API
  slug: fueleconomy-fuel-prices-api
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: Navigation menus for year/make/model vehicle lookup
  name: FuelEconomy.gov Menus API
  slug: fueleconomy-menus-api
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: Community-contributed real-world MPG data
  name: FuelEconomy.gov User MPG API
  slug: fueleconomy-user-mpg-api
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: Navigation menus for community MPG data lookup
  name: FuelEconomy.gov User MPG Menus API
  slug: fueleconomy-user-mpg-menus-api
- baseURL: https://www.fueleconomy.gov/ws/rest
  baseurl_source: declared
  description: Retrieve EPA fuel economy and specifications for specific vehicles
  name: FuelEconomy.gov Vehicles API
  slug: fueleconomy-vehicles-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fuel Economy Web Services Emissions API
  slug: open-fueleconomy-emissions-api
- collection_type: open
  name: Fuel Economy Web Services Emissions Fuel Prices API
  slug: open-fueleconomy-fuel-prices-api
- collection_type: open
  name: Fuel Economy Web Services Emissions Menus API
  slug: open-fueleconomy-menus-api
- collection_type: open
  name: Fuel Economy Web Services Emissions User MPG API
  slug: open-fueleconomy-user-mpg-api
- collection_type: open
  name: Fuel Economy Web Services Emissions User MPG Menus API
  slug: open-fueleconomy-user-mpg-menus-api
- collection_type: open
  name: Fuel Economy Web Services Emissions Vehicles API
  slug: open-fueleconomy-vehicles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/fueleconomy-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fueleconomy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fueleconomy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fueleconomy.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fueleconomy.gov/feg/ws/index.shtml
- group: other
  title: ''
  type: DataDownload
  url: https://www.fueleconomy.gov/feg/download.shtml
- group: other
  title: ''
  type: Widgets
  url: https://www.fueleconomy.gov/widgets/
- group: company
  title: ''
  type: Newsletter
  url: mailto:FuelEconomyNews-join@elist.ornl.gov
- group: commercial
  title: ''
  type: Plans
  url: plans/fueleconomy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fueleconomy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fueleconomy-finops.yml
created: '2026-06-13'
description: US Department of Energy REST API providing official EPA fuel economy ratings, vehicle specifications, CO2 emissions data, and energy cost comparisons for all model years from 1984 to present. Administered by Oak Ridge National Laboratory for the DOE and EPA, the API offers free, unauthenticated access to vehicle lookup menus, per-vehicle MPG records, emissions data, current fuel prices, and community-contributed real-world fuel economy data.
finops:
- name: Fueleconomy Finops
  service_category: ''
  slug: fueleconomy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fueleconomy.png
json_schemas:
- name: FuelPrices
  property_count: 8
  slug: fuel-prices
- name: MenuItems
  property_count: 1
  slug: menu-items
- name: Vehicle
  property_count: 65
  slug: vehicle
- name: YmpgVehicle
  property_count: 7
  slug: ympg-vehicle
jsonld:
- class_count: 7
  name: Fueleconomy Context
  property_count: 75
  slug: fueleconomy-context
layout: provider
modified: '2026-06-13'
name: FuelEconomy.gov
nav: Providers
network: true
overview: 'FuelEconomy.gov publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Emissions API, Fuel Prices API, Menus API, and 3 more. Tagged areas include Fuel Economy, EPA, DOE, Energy, and Vehicles.


  The FuelEconomy.gov catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FuelEconomy.gov''s developer surface includes documentation and 10 more developer resources.'
plans:
- name: Fueleconomy Plans Pricing
  plan_count: 1
  slug: fueleconomy-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Fueleconomy Rate Limits
  slug: fueleconomy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: FuelEconomy.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fueleconomy-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 52.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 59.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 0.0
  previous_composite: 30.3
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
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fueleconomy/refs/heads/main/screenshots/fueleconomy-2026-06-20T181604.png
security:
- kind: domain-security
  name: Fueleconomy Domain Security
  slug: fueleconomy-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: fueleconomy
tags:
- Fuel Economy
- EPA
- DOE
- Energy
- Vehicles
- Emissions
- CO2
- MPG
- Automotive
- Government
- Open Data
website: https://www.fueleconomy.gov/
---
