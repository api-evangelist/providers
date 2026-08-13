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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Opentripmap Agentic Access
  operation_count: 5
  slug: opentripmap-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Geographic coordinates of populated place API from OpenTripMap — 1 operation(s) for geographic coordinates of populated place.
  name: OpenTripMap Geographic coordinates of populated place API
  slug: opentripmap-geographic-coordinates-of-populated-place-api
- description: The Object properties API from OpenTripMap — 1 operation(s) for object properties.
  name: OpenTripMap Object properties API
  slug: opentripmap-object-properties-api
- description: The Objects list API from OpenTripMap — 3 operation(s) for objects list.
  name: OpenTripMap Objects list API
  slug: opentripmap-objects-list-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opentripmap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentripmap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opentripmap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://opentripmap.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.opentripmap.org/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/opentripmap
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opentripmap
- group: company
  title: ''
  type: Blog
  url: https://opentripmap.com/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://dev.opentripmap.org/price
- group: operate
  title: ''
  type: StatusPage
  url: https://dev.opentripmap.org/
- group: other
  title: ''
  type: X
  url: https://twitter.com/hashtag/opentripmap
- group: commercial
  title: ''
  type: Plans
  url: plans/opentripmap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/opentripmap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/opentripmap-finops.yml
created: '2026-06-13'
description: OpenTripMap provides a travel points of interest REST API with access to over 10 million POIs worldwide including attractions, restaurants, hotels, museums, and natural features. The API integrates data from OpenStreetMap, Wikidata, Wikipedia, and government cultural and environmental registries to deliver rich POI details with descriptions, coordinates, categorization, and Wikipedia links across more than 150 attraction types. Developers can query by bounding box, radius, name, category, and rating, with responses available in JSON and GeoJSON formats. Licensed under the Open Data Commons Open Database License (ODbL), which permits caching, indexing, and redistribution of data.
examples:
- key_count: 7
  name: Geoname Response
  slug: geoname-response
- key_count: 15
  name: Place Detail Response
  slug: place-detail-response
- key_count: 2
  name: Radius Geojson Response
  slug: radius-geojson-response
finops:
- name: Opentripmap Finops
  service_category: ''
  slug: opentripmap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opentripmap.png
json_schemas:
- name: Feature
  property_count: 4
  slug: feature
- name: FeatureCollection
  property_count: 2
  slug: featurecollection
- name: Geometry
  property_count: 2
  slug: geometry
- name: Geoname
  property_count: 7
  slug: geoname
- name: Places
  property_count: 17
  slug: places
- name: SimpleFeature
  property_count: 7
  slug: simplefeature
- name: SimpleSuggestFeature
  property_count: 8
  slug: simplesuggestfeature
jsonld:
- class_count: 22
  name: Opentripmap Context
  property_count: 5
  slug: opentripmap-context
layout: provider
modified: '2026-06-13'
name: OpenTripMap
nav: Providers
network: true
overview: 'OpenTripMap publishes 3 APIs on the [APIs.io](https://apis.io/) network: Geographic coordinates of populated place API, Object properties API, and Objects list API. Tagged areas include Travel, Points of Interest, POI, Tourism, and Maps.


  The OpenTripMap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenTripMap''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Opentripmap Plans Pricing
  plan_count: 4
  slug: opentripmap-plans-pricing
random_paper: 119
rate_limits:
- limit_count: 0
  name: Opentripmap Rate Limits
  slug: opentripmap-rate-limits
rules:
- name: OpenTripMap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: opentripmap-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentripmap/refs/heads/main/screenshots/opentripmap-2026-06-20T191049.png
security:
- kind: authentication
  name: Opentripmap Authentication
  slug: opentripmap-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Opentripmap Domain Security
  slug: opentripmap-domain-security
  summary_line: TLSv1.2
slug: opentripmap
tags:
- Travel
- Points of Interest
- POI
- Tourism
- Maps
- Geospatial
- OpenStreetMap
- Wikipedia
- Attractions
- Restaurants
- Hotels
- Museums
- REST API
website: https://opentripmap.com/en/
---
