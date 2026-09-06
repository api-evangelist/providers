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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Tesla Energy Agentic Access
  operation_count: 10
  slug: tesla-energy-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Backup reserve threshold for Powerwall sites
  name: Tesla Energy Backup API
  slug: tesla-energy-backup-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Historical energy production, consumption, and battery flow
  name: Tesla Energy History API
  slug: tesla-energy-history-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Real-time power, state-of-charge, and grid status for an energy site
  name: Tesla Energy Live Status API
  slug: tesla-energy-live-status-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Reserve threshold for EV charging when the site is islanded from the grid
  name: Tesla Energy Off Grid Charging API
  slug: tesla-energy-off-grid-charging-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Operation mode — self_consumption, backup, or autonomous
  name: Tesla Energy Operation API
  slug: tesla-energy-operation-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Discover energy_sites and other products owned by the authenticated account
  name: Tesla Energy Products API
  slug: tesla-energy-products-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Virtual power plant and grid-services program participation
  name: Tesla Energy Programs API
  slug: tesla-energy-programs-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Static configuration of an energy site (components, address, time zone)
  name: Tesla Energy Site Info API
  slug: tesla-energy-site-info-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Pre-charge Powerwall to 100% ahead of severe weather alerts
  name: Tesla Energy Storm Mode API
  slug: tesla-energy-storm-mode-api
- baseURL: https://fleet-api.prd.na.vn.cloud.tesla.com/api/1
  baseurl_source: declared
  description: Tariff schedule, peak/off-peak rate plans, and TOU optimization
  name: Tesla Energy Time Of Use API
  slug: tesla-energy-time-of-use-api
artifact_total: 65
collections:
- collection_type: postman
  name: Tesla Fleet Energy Backup API
  slug: postman-tesla-energy-backup-api
- collection_type: postman
  name: Tesla Fleet Energy Backup History API
  slug: postman-tesla-energy-history-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Live Status API
  slug: postman-tesla-energy-live-status-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Off Grid Charging API
  slug: postman-tesla-energy-off-grid-charging-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Operation API
  slug: postman-tesla-energy-operation-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Products API
  slug: postman-tesla-energy-products-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Programs API
  slug: postman-tesla-energy-programs-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Site Info API
  slug: postman-tesla-energy-site-info-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Storm Mode API
  slug: postman-tesla-energy-storm-mode-api
- collection_type: postman
  name: Tesla Fleet Energy Backup Time Of Use API
  slug: postman-tesla-energy-time-of-use-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tesla Fleet Energy Backup API
  slug: open-tesla-energy-backup-api
- collection_type: open
  name: Tesla Fleet Energy API
  slug: open-tesla-energy-fleet-api
- collection_type: open
  name: Tesla Fleet Energy Backup History API
  slug: open-tesla-energy-history-api
- collection_type: open
  name: Tesla Fleet Energy Backup Live Status API
  slug: open-tesla-energy-live-status-api
- collection_type: open
  name: Tesla Fleet Energy Backup Off Grid Charging API
  slug: open-tesla-energy-off-grid-charging-api
- collection_type: open
  name: Tesla Fleet Energy Backup Operation API
  slug: open-tesla-energy-operation-api
- collection_type: open
  name: Tesla Fleet Energy Backup Products API
  slug: open-tesla-energy-products-api
- collection_type: open
  name: Tesla Fleet Energy Backup Programs API
  slug: open-tesla-energy-programs-api
- collection_type: open
  name: Tesla Fleet Energy Backup Site Info API
  slug: open-tesla-energy-site-info-api
- collection_type: open
  name: Tesla Fleet Energy Backup Storm Mode API
  slug: open-tesla-energy-storm-mode-api
- collection_type: open
  name: Tesla Fleet Energy Backup Time Of Use API
  slug: open-tesla-energy-time-of-use-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tesla-energy/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tesla-energy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesla-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tesla-energy-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tesla-energy-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.tesla.com/energy
- group: start
  title: ''
  type: Portal
  url: https://developer.tesla.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tesla.com/docs/fleet-api
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tesla.com/docs/fleet-api/endpoints/energy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tesla.com/docs/fleet-api/products/energy-products
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tesla.com/docs/fleet-api/authentication/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developer.tesla.com/docs/fleet-api/authentication/third-party-tokens
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.tesla.com/docs/fleet-api/billing-and-limits
- group: commercial
  title: ''
  type: Billing
  url: https://developer.tesla.com/docs/fleet-api/billing-and-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.tesla.com/docs/fleet-api/announcements
- group: operate
  title: ''
  type: FAQ
  url: https://developer.tesla.com/docs/fleet-api/support/faq
- group: operate
  title: ''
  type: Support
  url: https://developer.tesla.com/docs/fleet-api/support/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teslamotors
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teslamotors/vehicle-command
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tdorssers/TeslaPy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/timdorr/tesla-api
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/781424/2s9YRCWB4f
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/powerwall
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/megapack
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/solarpanels
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/solarroof
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/electric
- group: company
  title: ''
  type: Website
  url: https://www.tesla.com/autobidder
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tesla-motors
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tesla.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tesla.com/legal/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/tesla-energy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tesla-energy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tesla-energy-finops.yml
created: '2026-05-25'
description: Tesla Energy is Tesla's solar generation and battery storage business unit, encompassing residential Powerwall, utility-scale Megapack, retrofit solar panels, and the Solar Roof. The Fleet API exposes energy_sites endpoints that let partners and owners read live power, calendar history, and site info, and write backup reserve, operation mode (self_consumption, backup, autonomous), storm mode, time-of-use settings, and off-grid vehicle charging reserve — the same control surface that powers the Tesla app and integrators like Autobidder, Tesla Electric (virtual power plant), and third-party home energy dashboards.
examples:
- key_count: 1
  name: Tesla Energy Live Status Example
  slug: tesla-energy-live-status-example
- key_count: 1
  name: Tesla Energy Site Info Example
  slug: tesla-energy-site-info-example
features:
- Powerwall residential battery — 13.5 kWh per unit, stackable up to 10 units, with integrated inverter and gateway in Powerwall+
- Megapack utility-scale battery — up to 3.9 MWh per unit, containerized DC architecture for grid storage and frequency regulation
- Solar Roof — integrated solar shingles for new and retrofit residential roofs
- Retrofit solar panels — private-label panels paired with Tesla Solar Inverter (cellular-connected, OTA updates)
- Autobidder — real-time energy trading and dispatch platform for utility-scale storage
- Tesla Electric — virtual utility / retail electricity provider in Texas with Powerwall participation
- Fleet API energy_sites endpoints for partner read/write access to site state and operation
- Backup reserve control — set the % state-of-charge Powerwall holds in reserve for outages
- Operation mode control — self_consumption, backup-only, autonomous (algorithmic)
- Storm Mode — automatically charges Powerwall to 100% ahead of severe weather alerts
- Time-of-Use settings — tariff schedule and peak/off-peak rate plan management
- Off-Grid Vehicle Charging Reserve — separate reserve threshold for EV charging during outages
- Calendar history — historical energy production, consumption, grid import/export, battery flow
- Live Status — real-time site power, state-of-charge, grid status, and load breakdown
- Programs — virtual power plant and grid services participation status
- Tesla app — single-pane control for Powerwall, Solar, and vehicles (consumer surface above the API)
- Lathrop, CA Megapack factory (operational since 2022) — 40 GWh/year capacity
- Shanghai Megafactory — Tesla's second Megapack factory, online 2025
- Energy revenue $10.1B in 2024 (+67% YoY); 31.4 GWh battery deployments in 2023 (+113% YoY)
finops:
- name: Tesla Energy Finops
  service_category: Energy / Storage / API
  slug: tesla-energy-finops
json_schemas:
- name: Tesla Energy Site Live Status
  property_count: 13
  slug: tesla-energy-live-status
- name: Tesla Energy Site
  property_count: 13
  slug: tesla-energy-site
jsonld:
- class_count: 11
  name: Tesla Energy Context
  property_count: 25
  slug: tesla-energy-context
layout: provider
modified: '2026-05-25'
name: Tesla Energy
nav: Providers
network: true
overview: 'Tesla Energy publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Backup API, History API, Live Status API, and 7 more. Tagged areas include Energy, Clean Energy, Solar, Battery Storage, and Powerwall.


  The Tesla Energy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tesla Energy''s developer surface includes authentication, developer portal, documentation, changelog, FAQ, support, and 29 more developer resources.'
plans:
- name: Tesla Energy Plans Pricing
  plan_count: 5
  slug: tesla-energy-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Tesla Energy Rate Limits
  slug: tesla-energy-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tesla Energy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tesla-energy-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tesla Energy API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: tesla-energy-rules
scopes:
- name: Tesla Energy Scopes
  scope_count: 3
  slug: tesla-energy-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 87.5
    catalog_earned_first_party: 0.0
    catalog_gap: 27.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 74.8
    developer_ergonomics: 57.1
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 50.0
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tesla-energy/refs/heads/main/screenshots/tesla-energy-2026-08-17T125758.png
security:
- kind: authentication
  name: Tesla Energy Authentication
  slug: tesla-energy-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Tesla Energy Domain Security
  slug: tesla-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tesla-energy
tags:
- Energy
- Clean Energy
- Solar
- Battery Storage
- Powerwall
- Megapack
- Solar Roof
- Virtual Power Plant
- IoT
- Grid Services
- Home Energy
- Utility Scale
website: https://www.tesla.com
---
