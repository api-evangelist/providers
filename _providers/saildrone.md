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
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Key/secret exchange for bearer tokens and drone access discovery
  name: Saildrone Authentication API
  slug: saildrone-authentication-api
- description: Service health check
  name: Saildrone Health API
  slug: saildrone-health-api
- description: Mission time-series data across vehicle, atmospheric, oceanographic, and biogeochemical datasets
  name: Saildrone Time Series API
  slug: saildrone-time-series-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saildrone Mission Authentication API
  slug: open-saildrone-authentication-api
- collection_type: open
  name: Saildrone Mission Health API
  slug: open-saildrone-health-api
- collection_type: open
  name: Saildrone Mission Time Series API
  slug: open-saildrone-time-series-api
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
overview: 'Saildrone publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Health API, and Time Series API. Tagged areas include Maritime, Ocean Data, USV, Unmanned Surface Vehicle, and Autonomous Systems.


  The Saildrone catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Saildrone''s developer surface includes product news, GitHub presence, YouTube channel, engineering blog, and 24 more developer resources.'
plans:
- name: Saildrone Plans Pricing
  plan_count: 4
  slug: saildrone-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Saildrone Rate Limits
  slug: saildrone-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Saildrone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: saildrone-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Saildrone API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: saildrone-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 13
    catalog_gap: 28.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 28.5
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 31.6
  provenance:
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Anti-Submarine Warfare
- Defense
- Climate
- Oceanography
- Bathymetry
- Biogeochemical
website: https://www.saildrone.com
---
