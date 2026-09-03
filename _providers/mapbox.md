---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Mapbox Agentic Access
  operation_count: 23
  slug: mapbox-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 12
apis:
- description: The Mapbox Vector Tiles API serves vector tiles from Mapbox-hosted vector tilesets.
  name: Mapbox Vector Tiles API
  slug: vector-tiles-api
- description: The Mapbox Raster Tiles API serves raster tiles generated from satellite imagery tilesets and tilesets generated from raster data uploaded to Mapbox.com.
  name: Mapbox Raster Tiles API
  slug: mapbox-raster-tiles-api
- description: The Mapbox Static Images API serves standalone, static map images generated from Mapbox Studio styles. These images can be displayed on web and mobile devices without the aid of a mapping library or A
  name: Mapbox Static Images API
  slug: mapbox-static-images-api
- description: The Mapbox Static Tiles API serves raster tiles generated from Mapbox Studio styles. Raster tiles can be used in traditional web mapping libraries like Mapbox.js, Leaflet, OpenLayers, and others to cr
  name: Mapbox Static Tiles API
  slug: mapbox-static-tiles-api
- description: The Mapbox Styles API lets you read and change map styles, fonts, and images. This API is the basis for Mapbox Studio.
  name: Mapbox Styles API
  slug: mapbox-styles-api
- description: The Mapbox Tilequery API allows you to retrieve data about specific features from a vector tileset, based on a given latitude and longitude. The Tilequery API makes it possible to query for features w
  name: Mapbox Tilequery API
  slug: mapbox-tilequery-api
- description: The Mapbox Uploads API transforms geographic data into tilesets that can be used with maps and geographic applications. Given a wide variety of geospatial formats, it normalizes projections and genera
  name: Mapbox Uploads API
  slug: mapbox-uploads-api
- description: The Mapbox Datasets API supports reading, creating, updating, and removing features from a dataset. Datasets contain one or more collections of GeoJSON features.
  name: Mapbox Datasets API
  slug: mapbox-datasets-api
- description: 'The Mapbox Fonts API accepts fonts as raw binary data, allows those fonts to be deleted, and generates encoded letters for map renderers. Two types of fonts are supported: TrueType fonts (.ttf) and Op'
  name: Mapbox Fonts API
  slug: mapbox-fonts-api
- baseURL: https://api.mapbox.com
  baseurl_source: declared
  description: The Activity API from Mapbox — 1 operation(s) for activity.
  name: Mapbox Activity API
  slug: mapbox-activity-api
- baseURL: https://api.mapbox.com
  baseurl_source: declared
  description: The Mapbox Tiling Service API API from Mapbox — 1 operation(s) for mapbox tiling service api.
  name: Mapbox Mapbox Tiling Service API API
  slug: mapbox-mapbox-tiling-service-api-api
- baseURL: https://api.mapbox.com
  baseurl_source: declared
  description: The Tilesets API from Mapbox — 13 operation(s) for tilesets.
  name: Mapbox Tilesets API
  slug: mapbox-tilesets-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Mapbox Tiling Service Activity API
  slug: open-mapbox-activity-api
- collection_type: open
  name: Mapbox Tiling Service Activity Mapbox Tiling Service API API
  slug: open-mapbox-mapbox-tiling-service-api-api
- collection_type: open
  name: Mapbox Tiling Service Activity Tilesets API
  slug: open-mapbox-tilesets-api
- collection_type: open
  name: Mapbox Tiling Service API
  slug: open-mapbox
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mapbox-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mapbox-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mapbox-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mapbox
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mapbox
- group: operate
  title: ''
  type: Support
  url: https://docs.mapbox.com/help/
- group: build
  title: ''
  type: SDKs
  url: https://docs.mapbox.com/api/overview/#sdk-and-library-support
- group: auth
  title: ''
  type: Authentication
  url: https://docs.mapbox.com/api/overview/#access-tokens-and-token-scopes
- group: design
  title: ''
  type: Versioning
  url: https://docs.mapbox.com/api/overview/#api-versioning
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.mapbox.com/api/overview/#rate-limits
- group: other
  title: ''
  type: CORS
  url: https://docs.mapbox.com/api/overview/#https-and-cors
- group: design
  title: ''
  type: Pagination
  url: https://docs.mapbox.com/api/overview/#pagination
- group: start
  title: ''
  type: Login
  url: https://account.mapbox.com/auth/signin/
- group: start
  title: ''
  type: Signup
  url: https://account.mapbox.com/auth/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mapbox.com/tos/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.mapbox.com/privacy/
- group: auth
  title: ''
  type: Security
  url: https://www.mapbox.com/platform/security/
- group: other
  title: ''
  type: Cheatsheet
  url: https://labs.mapbox.com/developer-cheatsheet/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mapbox.com/help/getting-started
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.mapbox.com/help/tutorials
- group: learn
  title: ''
  type: Videos
  url: https://docs.mapbox.com/help/how-to-videos
- group: other
  title: ''
  type: Troubleshooting
  url: https://docs.mapbox.com/help/troubleshooting
- group: other
  title: ''
  type: Glossary
  url: https://docs.mapbox.com/help/glossary
- group: company
  title: ''
  type: Website
  url: https://www.mapbox.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.mapbox.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.mapbox.com/blog
created: '2023-11-22'
description: Mapbox is a leading mapping and location data platform that provides tools and services to help developers and businesses create custom maps, visualize geospatial data, and build location-aware applications. Their platform offers a wide range of mapping technologies, from interactive maps and map design tools to geocoding and routing services.
features:
- Maps SDKs for iOS and Android (free up to 25k MAU, then $4/1k MAU)
- Mapbox GL JS for web map loads (free up to 50k loads, then $5/1k)
- Static Images API (free up to 50k req, then $1/1k)
- Directions API for driving/walking/cycling routes (free up to 100k req, then $2/1k)
- Temporary Geocoding API ($0.75/1k above 100k free)
- Search Box API session-based pricing ($3/1k sessions)
- Address Autofill ($12.50/1k sessions above 1k free)
- Navigation SDK v3 metered ($0.30/MAU + $0.08/trip) or unlimited (custom)
- Per-token, per-endpoint rate limits (60-1,250 req/min defaults)
- Volume discounts at higher usage levels
- Statistics API for usage reporting
- Vector and raster tile services
- Mapbox Studio for custom map design
- Tilequery API for spatial point-in-polygon queries
- Map Matching API to snap GPS traces to road networks
finops:
- name: Mapbox Finops
  service_category: Location Services
  slug: mapbox-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mapbox.png
layout: provider
modified: '2026-05-30'
name: Mapbox
nav: Providers
network: true
overview: 'Mapbox publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activity API, Mapbox Tiling Service API API, and Tilesets API. Tagged areas include Mapping, Maps, Geospatial, and Location.


  Mapbox''s developer surface includes support, authentication, signup flow, privacy policy, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Mapbox Plans Pricing
  plan_count: 8
  slug: mapbox-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Mapbox Rate Limits
  slug: mapbox-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 51.3
    commercial_clarity: 51.3
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 47.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mapbox/refs/heads/main/screenshots/mapbox-2026-06-20T184931.png
security:
- kind: domain-security
  name: Mapbox Domain Security
  slug: mapbox-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Mapbox Trust Center
  slug: mapbox-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR, CSA STAR
slug: mapbox
tags:
- Mapping
- Maps
- Geospatial
- Location
website: https://www.mapbox.com/
---
