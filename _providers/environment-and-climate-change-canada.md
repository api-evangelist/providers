---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
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
  composite: 5.9
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
slug: environment-and-climate-change-canada
tags:
- Geospatial
- OGC
- WMS
- GIS
- Empty Surface
website: https://geo.ec.gc.ca/
---
