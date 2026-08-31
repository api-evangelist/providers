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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Radar Agentic Access
  operation_count: 25
  slug: radar-agentic-access
  summary_line: 25 operations · 6 acting
api_count: 1
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
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Radar Events API
  slug: open-radar-events-api
- collection_type: open
  name: Radar Events Geocoding API
  slug: open-radar-geocoding-api
- collection_type: open
  name: Radar Events Geofences API
  slug: open-radar-geofences-api
- collection_type: open
  name: Radar Events Routing API
  slug: open-radar-routing-api
- collection_type: open
  name: Radar Events Search API
  slug: open-radar-search-api
- collection_type: open
  name: Radar Events Track API
  slug: open-radar-track-api
- collection_type: open
  name: Radar Events Users API
  slug: open-radar-users-api
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
random_paper: 18
rate_limits:
- limit_count: 5
  name: Radar Rate Limits
  slug: radar-rate-limits
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
