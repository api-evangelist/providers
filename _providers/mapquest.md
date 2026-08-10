---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Mapquest Agentic Access
  operation_count: 11
  slug: mapquest-agentic-access
  summary_line: 11 operations · 5 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: The MapQuest Geocoding API converts addresses into geographic coordinates and vice versa, supporting both single and batch geocoding requests.
  name: MapQuest Geocoding API
  slug: mapquest-geocoding-api
- description: The MapQuest Static Map API returns a map image based on specified parameters including center, zoom, size, and map type.
  name: MapQuest Static Map API
  slug: mapquest-static-map-api
- description: The MapQuest Traffic API returns traffic incidents for a specified bounding box in JSON or XML formats, including road construction and collisions.
  name: MapQuest Traffic API
  slug: mapquest-traffic-api
- description: The MapQuest Search API supports radius, rectangle, polygon, and corridor searches against MapQuest hosted data tables, returning matching points of interest with attributes.
  name: MapQuest Search API
  slug: mapquest-search-api
- description: The MapQuest Place Search API returns places matching a search query, with support for category, location, and bounding-box filtering.
  name: MapQuest Place Search API
  slug: mapquest-place-search-api
- description: The MapQuest Search Ahead API delivers prediction-based search suggestions as users type, supporting addresses, places, categories, and admin areas.
  name: MapQuest Search Ahead API
  slug: mapquest-search-ahead-api
- description: The MapQuest Geolocation API returns the approximate location of a device based on cell tower and Wi-Fi access point information.
  name: MapQuest Geolocation API
  slug: mapquest-geolocation-api
- description: The MapQuest Icons API serves customizable map marker icons for use with MapQuest static and interactive maps.
  name: MapQuest Icons API
  slug: mapquest-icons-api
- description: The MapQuest Data Manager API allows developers to upload, manage, and query custom hosted data tables for use with MapQuest search and mapping services.
  name: MapQuest Data Manager API
  slug: mapquest-data-manager-api
- description: The Directions API from MapQuest — 8 operation(s) for directions.
  name: MapQuest Directions API
  slug: mapquest-directions-api
artifact_total: 16
collections:
- collection_type: open
  name: MapQuest Directions API
  slug: open-mapquest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mapquest-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mapquest-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MapQuest
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mapquest
- group: start
  title: ''
  type: Portal
  url: https://developer.mapquest.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mapquest.com/documentation/
- group: start
  title: ''
  type: Signup
  url: https://developer.mapquest.com/plan_purchase/steps/business_edition/business_edition_free/register
- group: start
  title: ''
  type: Login
  url: https://developer.mapquest.com/user/login
- group: operate
  title: ''
  type: Support
  url: https://developer.mapquest.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hello.mapquest.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hello.mapquest.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://developer.mapquest.com/blog/archive/
created: '2025-01-07'
description: MapQuest provides mapping, geocoding, routing, and traffic data APIs for developers to build location-aware applications. The developer portal offers free API keys and documentation for directions, static maps, geocoding, and traffic incident services.
finops:
- name: Mapquest Finops
  service_category: API
  slug: mapquest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mapquest.png
layout: provider
modified: '2026-05-19'
name: MapQuest
nav: Providers
network: true
overview: 'MapQuest publishes 1 API on the [APIs.io](https://apis.io/) network: Directions API. Tagged areas include Geocoding, Mapping, Maps, Navigation, and Routing.


  MapQuest''s developer surface includes developer portal, getting-started guide, signup flow, support, engineering blog, and 7 more developer resources.'
plans:
- name: Mapquest Plans Pricing
  plan_count: 3
  slug: mapquest-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Mapquest Rate Limits
  slug: mapquest-rate-limits
score:
  band: developing
  composite: 44.4
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 48.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mapquest/refs/heads/main/screenshots/mapquest-2026-06-20T184933.png
security:
- kind: domain-security
  name: Mapquest Domain Security
  slug: mapquest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mapquest
tags:
- Geocoding
- Mapping
- Maps
- Navigation
- Routing
- Traffic
website: https://developer.mapquest.com/
---
