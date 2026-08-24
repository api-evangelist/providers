---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Geoinsight Agentic Access
  operation_count: 14
  slug: geoinsight-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- description: 'Standards-compliant OGC API - Discrete Global Grid Systems endpoint exposing the GeoInsight Spatial Token store for zone-based queries. Fourteen read operations across four resource families: a landin'
  name: OGC API - DGGS
  slug: ogc-api-dggs
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geoinsight-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://geoinsight.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dggs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.geoinsight.ai/api?f=html
- group: docs
  title: ''
  type: APIReference
  url: https://api.geoinsight.ai/api?f=html
- group: start
  title: ''
  type: Sandbox
  url: https://dggs.io/api-tester
- group: commercial
  title: ''
  type: TermsOfService
  url: https://geoinsight.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://geoinsight.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:info@geoinsight.ai
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/geoinsight-ogc-api-dggs-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geoinsight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/geoinsight-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/geoinsight-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/geoinsight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/geoinsight-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/geoinsight-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/geoinsight-ogc-api-dggs-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/geoinsight-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/geoinsight-packages.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/geoinsight-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/geoinsight-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/geoinsight-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geoinsight-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geoinsight-domain-security.yml
created: '2026-08-20'
description: GeoInsight GmbH is a German geospatial-AI company running a Data-as-a-Service platform built on a Discrete Global Grid System (DGGS). It converts Earth-observation and vector data into AI-ready hierarchical hexagonal "Spatial Tokens" so that models can reason about geography the way language models reason about text. The platform is exposed through a standards-compliant OGC API - DGGS endpoint that answers zone-based queries across multiple DGGRS (H3, ISEA3H, IGEO7, IVEA3H), serving Sentinel-2 and Landsat imagery from the Copernicus and USGS archives, RADARSAT Constellation backscatter, Overture administrative boundaries, AIS vessel positions, building footprints and elevation models. Queries return GeoJSON, DGGS-JSON, GeoParquet or HTML, with CQL2 filtering, COG raster statistics and STAC search strategies. Target markets are OSINT and maritime intelligence, climate and environment, agriculture and food security, infrastructure and urban planning, disaster response, and finance
  and risk. The company is an NVIDIA Inception member and participates in the OGC AI-DGGS pilot programme.
image: https://geoinsight.ai/og-image.png
layout: provider
modified: '2026-08-20'
name: GeoInsight
nav: Providers
network: true
overview: 'GeoInsight publishes 1 API on the [APIs.io](https://apis.io/) network: OGC API - DGGS. Tagged areas include Geospatial, DGGS, Discrete Global Grid System, Earth Observation, and Remote Sensing.


  GeoInsight''s developer surface includes documentation, API reference, sandbox, support, authentication, and 20 more developer resources.'
plans:
- name: Geoinsight Plans Pricing
  plan_count: 0
  slug: geoinsight-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Geoinsight Rate Limits
  slug: geoinsight-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 35.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Geoinsight Authentication
  slug: geoinsight-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Geoinsight Domain Security
  slug: geoinsight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: geoinsight
tags:
- Geospatial
- DGGS
- Discrete Global Grid System
- Earth Observation
- Remote Sensing
- Spatial Data
- GIS
- Artificial Intelligence
- Machine-Learning
- Analysis-ready data
- Spatial Tokens
- Sentinel-2
- Copernicus
- OGC
- STAC
- GeoParquet
- H3
website: https://geoinsight.ai/
---
