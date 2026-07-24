---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Saildrone Public Mission API (BETA). Provides authenticated access via a key/secret bearer flow to per-mission time-series telemetry across the four canonical Saildrone datasets — vehicle, atmospheric
  name: Saildrone Mission API
  slug: saildrone-mission-api
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saildrone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.saildrone.com
- group: company
  title: ''
  type: About
  url: https://www.saildrone.com/about
- group: other
  title: ''
  type: API
  url: https://www.saildrone.com/data-delivery/api
- group: docs
  title: ''
  type: SwaggerUI
  url: https://developer-mission.saildrone.com/api-docs
- group: start
  title: ''
  type: MissionPortal
  url: https://www.saildrone.com/data-delivery/mission-portal
- group: other
  title: ''
  type: DataProducts
  url: https://www.saildrone.com/technology/data
- group: other
  title: ''
  type: Platform
  url: https://www.saildrone.com/platform/spectre
- group: other
  title: ''
  type: Platform
  url: https://www.saildrone.com/platform/surveyor
- group: other
  title: ''
  type: Platform
  url: https://www.saildrone.com/platform/voyager
- group: other
  title: ''
  type: Platform
  url: https://www.saildrone.com/platform/explorer
- group: other
  title: ''
  type: Services
  url: https://www.saildrone.com/service-model/fully-managed
- group: other
  title: ''
  type: Capability
  url: https://www.saildrone.com/capabilities/metocean-survey
- group: company
  title: ''
  type: News
  url: https://www.saildrone.com/news
- group: company
  title: ''
  type: Press
  url: https://www.saildrone.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.saildrone.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.saildrone.com/contact
- group: company
  title: ''
  type: PartnerOpenData
  url: https://www.pmel.noaa.gov/ocs/saildrone/data-access
- group: company
  title: ''
  type: PartnerOpenData
  url: https://data.pmel.noaa.gov/generic/erddap/tabledap/saildrone_gts.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Saildrone
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/saildrone
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/saildrone
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@saildrone
- group: commercial
  title: ''
  type: Plans
  url: plans/saildrone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/saildrone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/saildrone-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/saildrone-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.saildrone.com/news
created: '2026-05-24'
description: Saildrone is an Alameda, California maritime autonomy company that designs, manufactures, and operates a global fleet of wind/solar-powered autonomous surface vehicles (USVs) for ocean science, maritime domain awareness, and defense applications. Founded in 2012 by Richard Jenkins, the company runs four USV classes — Explorer (23ft, environmental sensing), Voyager (33ft, MDA and counter-narcotics), Surveyor (65ft, deep-ocean bathymetric mapping), and the newer Spectre (ISR / anti-submarine warfare / kinetic payloads). Saildrone has logged over 2.5M nautical miles and 65,000 days at sea across customers including NOAA PMEL, NOAA SWFSC, the US Navy (Task Force 59), NASA, EUMETSAT, BOEM, and Lockheed Martin (which invested $50M in October 2025). Saildrone delivers data through two product surfaces — the Saildrone Mission Portal (secure web app for tasking and live multi-INT visualization) and the Saildrone Public Mission API (BETA) at developer-mission.saildrone.com, which exposes
  key/secret authenticated endpoints for health, drone access discovery, and time-series retrieval across vehicle, atmospheric, oceanographic, and biogeochemical datasets. Open ocean data from past missions is published via NOAA PMEL ERDDAP and NCEI under open-data terms.
examples:
- key_count: 2
  name: Saildrone Authenticate Example
  slug: saildrone-authenticate-example
- key_count: 2
  name: Saildrone Get Time Series Example
  slug: saildrone-get-time-series-example
- key_count: 2
  name: Saildrone List Access Example
  slug: saildrone-list-access-example
finops:
- name: Saildrone Finops
  service_category: ''
  slug: saildrone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saildrone.png
json_schemas:
- name: Saildrone Mission Access
  property_count: 4
  slug: saildrone-mission-access
- name: Saildrone Mission Time Series Record
  property_count: 22
  slug: saildrone-mission-time-series-record
jsonld:
- class_count: 24
  name: Saildrone Context
  property_count: 8
  slug: saildrone-context
layout: provider
modified: '2026-05-24'
name: Saildrone
nav: Providers
network: true
overview: 'Saildrone publishes 1 API on the [APIs.io](https://apis.io/) network: Mission API. Tagged areas include Maritime, Ocean Data, USV, Unmanned Surface Vehicle, and Autonomous Systems.


  The Saildrone catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Saildrone''s developer surface includes product news, GitHub presence, YouTube channel, engineering blog, and 24 more developer resources.'
plans:
- name: Saildrone Plans Pricing
  plan_count: 4
  slug: saildrone-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 0
  name: Saildrone Rate Limits
  slug: saildrone-rate-limits
rules:
- name: Saildrone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: saildrone-jsonschema-spectral-rules
- name: Saildrone API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: saildrone-rules
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 71.7
    developer_ergonomics: 2.2
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 45.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saildrone/refs/heads/main/screenshots/saildrone-2026-06-20T193333.png
security:
- kind: domain-security
  name: Saildrone Domain Security
  slug: saildrone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saildrone
tags:
- Maritime
- Ocean Data
- USV
- Unmanned Surface Vehicle
- Autonomous Systems
- METOC
- Maritime Domain Awareness
- Anti Submarine Warfare
- Defense
- Climate
- Oceanography
- Bathymetry
- Biogeochemical
website: https://www.saildrone.com
---
