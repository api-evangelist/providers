---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Geoinsight Agentic Access
  operation_count: 14
  slug: geoinsight-agentic-access
  summary_line: 14 operations
api_count: 2
apis:
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Collection ID API from GeoInsight — 1 operation(s) for collection id.
  name: GeoInsight Collection ID API
  slug: geoinsight-collection-id-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Collections API from GeoInsight — 1 operation(s) for collections.
  name: GeoInsight Collections API
  slug: geoinsight-collections-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Data API from GeoInsight — 1 operation(s) for data.
  name: GeoInsight Data API
  slug: geoinsight-data-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The DGGRS ID API from GeoInsight — 2 operation(s) for dggrs id.
  name: GeoInsight DGGRS ID API
  slug: geoinsight-dggrs-id-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The DGGS API from GeoInsight — 2 operation(s) for dggs.
  name: GeoInsight DGGS API
  slug: geoinsight-dggs-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Items API from GeoInsight — 2 operation(s) for items.
  name: GeoInsight Items API
  slug: geoinsight-items-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The root API from GeoInsight — 1 operation(s) for root.
  name: GeoInsight Root API
  slug: geoinsight-root-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Zone ID API from GeoInsight — 2 operation(s) for zone id.
  name: GeoInsight Zone ID API
  slug: geoinsight-zone-id-api
- baseURL: https://api.geoinsight.ai
  baseurl_source: declared
  description: The Zones API from GeoInsight — 2 operation(s) for zones.
  name: GeoInsight Zones API
  slug: geoinsight-zones-api
artifact_total: 14
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
overview: 'GeoInsight publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Collection ID API, Collections API, Data API, and 6 more. Tagged areas include Geospatial, DGGS, Discrete Global Grid System, Earth Observation, and Remote Sensing.


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
  composite: 28.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geoinsight/refs/heads/main/screenshots/geoinsight-2026-09-02T145559.png
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
