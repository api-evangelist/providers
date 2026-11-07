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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: The BMW Vehicle Identification API allows users to access detailed information about BMW vehicles by inputting their unique vehicle identification number (VIN). Provides essential data about a vehicle
  name: BMW Vehicle Identification API
  slug: vehicle-identification-api
- description: The BMW Repair and Maintenance API provides access to maintenance schedules, diagnostic information, and technical specifications for BMW vehicles. Enables automotive technicians and repair shops to a
  name: BMW Repair and Maintenance API
  slug: repair-and-maintenance-api
- description: The BMW Technical Campaign and Map Status API provides real-time data on the status of technical campaigns and software map updates related to BMW vehicles, including campaign progress, completion tim
  name: BMW Technical Campaign and Map Status API
  slug: technical-campaign-and-map-status-api
- description: The BMW Flat Rates API provides access to a database of fixed prices for specific services and repairs on BMW vehicles, enabling transparent and standardized pricing for vehicle maintenance and repair
  name: BMW Flat Rates API
  slug: flat-rates-api
- description: The BMW Smart Maintenance API provides real-time vehicle health and maintenance need information by connecting to the vehicle's onboard diagnostic system, monitoring engine performance, tire pressure,
  name: BMW Smart Maintenance API
  slug: smart-maintenance-api
- description: The BMW Open Data Platform provides developers, researchers, and innovators with access to vehicle data including performance metrics, sensor data, and diagnostic information. The platform supports de
  name: BMW Open Data Platform
  slug: bmw-open-data-platform
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/bmw/plans/bmw-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bmw-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bmw/rate-limits/bmw-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bmw-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bmw/finops/bmw-finops.yml
  title: ''
  type: FinOps
  url: finops/bmw-finops.yml
- group: auth
  href: https://artifacts.apis.io/bmw/security/bmw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmw-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmwgroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bmw-group
- group: company
  title: ''
  type: Website
  url: https://www.bmw.com
- group: start
  title: ''
  type: Portal
  url: https://aos.bmwgroup.com/bmw-api
- group: start
  title: ''
  type: GettingStarted
  url: https://aos.bmwgroup.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://aos.bmwgroup.com/help/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://aos.bmwgroup.com/price-list
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aos.bmwgroup.com/conditions-of-use
- group: company
  title: ''
  type: Blog
  url: https://www.press.bmwgroup.com/global/rss
created: '2025-02-08'
description: BMW is a German multinational company specializing in manufacturing luxury vehicles and motorcycles. BMW provides automotive data APIs through the Aftersales Online System (AOS) portal and the BMW Open Data Platform, enabling dealers, repair shops, and developers to access vehicle identification, maintenance, technical campaign, pricing, and diagnostic data.
finops:
- has_sources: false
  method: generated
  name: Bmw Finops
  primary_unit: request
  service_category: API
  slug: bmw-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bmw.png
layout: provider
modified: '2026-04-21'
name: BMW
nav: Providers
network: true
overview: 'BMW is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Cars, Vehicles, Automotive, and Connected Vehicles.


  BMW''s developer surface includes developer portal, getting-started guide, support, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Bmw Plans Pricing
  plan_count: 3
  slug: bmw-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Bmw Rate Limits
  slug: bmw-rate-limits
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 62.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 20.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bmw/bmw-2026-06-20T173545.png
security:
- kind: domain-security
  name: Bmw Domain Security
  slug: bmw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bmw
tags:
- Automobiles
- Cars
- Vehicles
- Automotive
- Connected Vehicles
website: https://www.bmw.com
---
