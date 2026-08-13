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
- acting_count: 6
  human_in_the_loop: 0
  name: Radar Agentic Access
  operation_count: 25
  slug: radar-agentic-access
  summary_line: 25 operations · 6 acting
api_count: 7
apis:
- description: Query location events
  name: Radar Events API
  slug: radar-events-api
- description: Forward, reverse, and IP geocoding
  name: Radar Geocoding API
  slug: radar-geocoding-api
- description: Manage geographic boundaries
  name: Radar Geofences API
  slug: radar-geofences-api
- description: Distance, matrix, match, directions, and route optimization
  name: Radar Routing API
  slug: radar-routing-api
- description: Autocomplete, search users, geofences, places, and validate addresses
  name: Radar Search API
  slug: radar-search-api
- description: Update user locations and generate events
  name: Radar Track API
  slug: radar-track-api
- description: Manage user records
  name: Radar Users API
  slug: radar-users-api
artifact_total: 14
collections:
- collection_type: open
  name: Radar API
  slug: open-radar
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/radar-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/radarlabs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radarlabs
- group: company
  title: ''
  type: Blog
  url: https://radar.com/blog
created: '2025-02-06'
description: Use Radar APIs as building blocks for location-based products and services like pickup and delivery tracking, location-triggered notifications, location verification, store locators, address autocomplete, and more. Or, use Radar APIs to manage your Radar data, including users, geofences, and events.
finops:
- name: Radar Finops
  service_category: API
  slug: radar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radar.png
layout: provider
modified: '2026-05-19'
name: Radar
nav: Providers
network: true
overview: 'Radar publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Geocoding API, Geofences API, and 4 more. Tagged areas include Location, Geocoding, Geofencing, Routing, and Maps.


  Radar''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Radar Plans Pricing
  plan_count: 3
  slug: radar-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Radar Rate Limits
  slug: radar-rate-limits
score:
  band: emerging
  composite: 27.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 50.7
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radar/refs/heads/main/screenshots/radar-2026-06-20T192516.png
security:
- kind: authentication
  name: Radar Authentication
  slug: radar-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Radar Domain Security
  slug: radar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: radar
tags:
- Location
- Geocoding
- Geofencing
- Routing
- Maps
---
