---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Firms Agentic Access
  operation_count: 6
  slug: nasa-firms-agentic-access
  summary_line: 6 operations
api_count: 4
apis:
- description: Active fire hotspot detections within a bounding box area
  name: NASA FIRMS Area Fire Detections API
  slug: nasa-firms-area-fire-detections-api
- description: Check which dates have Standard Processing or Near Real-Time data
  name: NASA FIRMS Data Availability API
  slug: nasa-firms-data-availability-api
- description: KMZ files containing color-coded fire footprint polygons by region
  name: NASA FIRMS KML Fire Footprints API
  slug: nasa-firms-kml-fire-footprints-api
- description: Identify dates with absent satellite fire detection data
  name: NASA FIRMS Missing Data API
  slug: nasa-firms-missing-data-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-firms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-firms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firms.modaps.eosdis.nasa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://firms.modaps.eosdis.nasa.gov/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://firms.modaps.eosdis.nasa.gov/api/area/
- group: auth
  title: ''
  type: Authentication
  url: https://firms.modaps.eosdis.nasa.gov/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nasa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.earthdata.nasa.gov/engage/open-data-services-and-software/data-and-information-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://firms.modaps.eosdis.nasa.gov/api/
- group: company
  title: ''
  type: Blog
  url: https://earthdata.nasa.gov/
- group: operate
  title: ''
  type: Contact
  url: https://firms.modaps.eosdis.nasa.gov/contact/
- group: commercial
  title: ''
  type: Plans
  url: plans/nasa-firms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasa-firms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nasa-firms-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nasa-firms-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/nasa-firms-context.jsonld
created: '2026-06-13'
description: NASA Fire Information for Resource Management System (FIRMS) REST API providing near-real-time satellite fire detections globally from MODIS (Terra/Aqua), VIIRS (S-NPP, NOAA-20, NOAA-21), and LANDSAT instruments. Data is available within 3 hours of satellite observation worldwide, with Ultra Real-Time detections available within 60 seconds for the US and Canada. Supports area-based bounding box queries, KML fire footprints by region, data availability checks, and missing data identification. Free MAP_KEY registration required.
examples:
- key_count: 5
  name: Area Fire Detections Request
  slug: area-fire-detections-request
- key_count: 5
  name: Data Availability Request
  slug: data-availability-request
- key_count: 5
  name: Kml Fire Footprints Request
  slug: kml-fire-footprints-request
finops:
- name: Nasa Firms Finops
  service_category: ''
  slug: nasa-firms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-firms.png
json_schemas:
- name: Data Availability Record
  property_count: 4
  slug: data-availability
- name: Fire Detection Record
  property_count: 13
  slug: fire-detection
jsonld:
- class_count: 0
  name: Nasa Firms Context
  property_count: 3
  slug: nasa-firms-context
layout: provider
modified: '2026-06-13'
name: NASA FIRMS
nav: Providers
network: true
overview: 'NASA FIRMS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Area Fire Detections API, Data Availability API, KML Fire Footprints API, and 1 more. Tagged areas include NASA, Fire Detection, Satellite, MODIS, and VIIRS.


  The NASA FIRMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA FIRMS''s developer surface includes documentation, getting-started guide, authentication, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Nasa Firms Plans Pricing
  plan_count: 2
  slug: nasa-firms-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Nasa Firms Rate Limits
  slug: nasa-firms-rate-limits
rules:
- name: NASA FIRMS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nasa-firms-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.8
  delta: -5.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.1
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-firms/refs/heads/main/screenshots/nasa-firms-2026-06-20T185947.png
security:
- kind: domain-security
  name: Nasa Firms Domain Security
  slug: nasa-firms-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: nasa-firms
tags:
- NASA
- Fire Detection
- Satellite
- MODIS
- VIIRS
- Remote Sensing
- Open Data
- Environmental
- Geospatial
- Science
website: https://firms.modaps.eosdis.nasa.gov/
---
