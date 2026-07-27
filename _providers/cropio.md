---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: Create, list, get, update, and delete fields, field groups, field shapes (boundaries in multiple geo formats), and land parcels. Fields carry calculated/legal/tillable area, administrative location, a
  name: Cropio Fields API
  slug: cropio-fields-api
- description: Manage crops (name, season type, base crop, color scheme), seasons (year, start/end date), production cycles, and growth stage / growth scale tracking used to plan and record what is planted on a fiel
  name: Cropio Crops API
  slug: cropio-crops-api
- description: Read-only access to per-field and per-field-group satellite images - capture date, source satellite, cloud/cirrus/data coverage, and min/max/mean NDVI values - plus NDVI grid data for zoning and veget
  name: Cropio Satellite Imagery API
  slug: cropio-satellite-imagery-api
- description: Read-only weather station data (real and virtual stations) keyed by geoposition, including a rolling 24-hour hourly current_weather array (precipitation, air temperature, and related measurements) and
  name: Cropio Weather API
  slug: cropio-weather-api
- description: Create and manage scouting tasks and manual tasks assigned to a field and a responsible user, plus the field scout reports, scout report points, and plant threat findings recorded against them, and ag
  name: Cropio Scouting & Tasks API
  slug: cropio-scouting-and-tasks-api
- description: Manage machines, implements, and machine tasks (driver, work type, field, start/end time), plus GPS logger data - raw and hourly-aggregated positions, speed, and distance per machine - polled over HTT
  name: Cropio Machinery & Telematics API
  slug: cropio-machinery-telematics-api
- description: 'Read and write yield maps (per-field moisture/yield/applied property maps tied to a field work result), harvest weighings and transportations, and productivity/yield estimates and their history, used '
  name: Cropio Yield & Harvest API
  slug: cropio-yield-and-harvest-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cropio-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cropio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cropio
- group: company
  title: ''
  type: Website
  url: https://operations.cropwise.com
- group: docs
  title: ''
  type: Documentation
  url: https://cropwiseoperations.docs.apiary.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/cropio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cropio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cropio-finops.yml
created: '2026-07-03'
description: Cropio was an independent Eastern European farm management and precision agriculture platform (fields, satellite/NDVI imagery, weather, scouting, machinery telematics, and yield) founded in 2013. Syngenta acquired Cropio in September 2019 and folded it into its Cropwise digital agriculture portfolio; the product now operates as Cropwise Operations, and cropio.com redirects to operations.cropwise.com. The original Cropio API v3 was not shut down - it continues to run as the documented Cropwise Operations Platform API v3, reachable at operations.cropwise.com/api/v3 (the legacy cropio.com/api/v3 host has redirected there since April 1, 2022). It is a per-account HTTP JSON REST API (not a self-serve developer marketplace) - a Cropwise Operations login is required to obtain a USER_API_TOKEN, and there is no published self-signup API key flow or API-specific price list. Syngenta separately launched a broader "Cropwise Open Platform" for partners in 2025, which is a distinct, newer
  developer program outside the scope of this entry.
finops:
- name: Cropio Finops
  service_category: Agriculture Technology and Farm Management
  slug: cropio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cropio.png
layout: provider
modified: '2026-07-03'
name: Cropio
nav: Providers
network: true
overview: 'Cropio publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture, AgTech, Precision Agriculture, Farm Management, and Satellite Imagery.


  Cropio''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Cropio Plans Pricing
  plan_count: 3
  slug: cropio-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Cropio Rate Limits
  slug: cropio-rate-limits
score:
  band: emerging
  composite: 24.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 24.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cropio/refs/heads/main/screenshots/cropio-2026-07-25T210746.png
security:
- kind: domain-security
  name: Cropio Domain Security
  slug: cropio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cropio
tags:
- Agriculture
- AgTech
- Precision Agriculture
- Farm Management
- Satellite Imagery
- NDVI
- Weather
- Telematics
- Syngenta
- Cropwise
website: https://operations.cropwise.com
---
