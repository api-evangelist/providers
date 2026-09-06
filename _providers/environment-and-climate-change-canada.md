---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: 'An OGC-standard GeoServer at geo.ec.gc.ca. Probed anonymously on 2026-08-20: the WMS 1.3.0 GetCapabilities request returned HTTP 200 with a valid WMS_Capabilities document titled "ECCC Web Map Service'
  name: Environment and Climate Change Canada OGC Web Services (WMS / WFS)
  slug: ogc-web-services
- description: 'A GeoServer-provided OGC API - Features endpoint on the same host. Probed anonymously on 2026-08-20: /collections?f=json returned HTTP 200 with a well-formed OGC API response containing ZERO collectio'
  name: Environment and Climate Change Canada OGC API - Features
  slug: ogc-api-features
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://geo.ec.gc.ca/
created: '2026-08-20'
description: Environment and Climate Change Canada (ECCC) is the federal department responsible for weather, climate, water and environmental protection in Canada, and operates the Meteorological Service of Canada. It runs an OGC-standard GeoServer at geo.ec.gc.ca which responds correctly to WMS, WFS and OGC API - Features requests but, when probed on 2026-08-20, published no layers, no feature types and no collections through it.
layout: provider
modified: '2026-08-20'
name: Environment and Climate Change Canada
nav: Providers
network: true
overview: Environment and Climate Change Canada publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, OGC, WMS, GIS, and Empty Surface.
random_paper: 8
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 2
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 7.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/environment-and-climate-change-canada/refs/heads/main/screenshots/environment-and-climate-change-canada-2026-09-02T145404.png
slug: environment-and-climate-change-canada
tags:
- Geospatial
- OGC
- WMS
- GIS
- Empty Surface
website: https://geo.ec.gc.ca/
---
