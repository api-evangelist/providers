---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
  name: Geocode Earth Agentic Access
  operation_count: 5
  slug: geocode-earth-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Forward API from Geocode Earth — 3 operation(s) for forward.
  name: Geocode Earth Forward API
  slug: geocode-earth-forward-api
- description: The Place API from Geocode Earth — 1 operation(s) for place.
  name: Geocode Earth Place API
  slug: geocode-earth-place-api
- description: The Reverse API from Geocode Earth — 1 operation(s) for reverse.
  name: Geocode Earth Reverse API
  slug: geocode-earth-reverse-api
artifact_total: 10
collections:
- collection_type: open
  name: Geocode Earth API
  slug: open-geocode-earth
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/geocode-earth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/geocode-earth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/geocode-earth-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pelias
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geocode-earth
- group: company
  title: ''
  type: Website
  url: https://geocode.earth/
- group: docs
  title: ''
  type: Documentation
  url: https://geocode.earth/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/geocode-earth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/geocode-earth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/geocode-earth-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://geocode.earth/feed.xml
created: '2026-06-21'
description: Geocode Earth is a hosted geocoding and address autocomplete API built by the team that maintains Pelias, the open-source geocoder. It provides forward (search), autocomplete, reverse, and structured geocoding plus place lookup over fully open data (OpenStreetMap, OpenAddresses, Who's on First, and Geonames), with results that can be stored without restrictive licensing.
finops:
- name: Geocode Earth Finops
  service_category: Maps and Location Services
  slug: geocode-earth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/geocode-earth.png
layout: provider
modified: '2026-06-21'
name: Geocode Earth
nav: Providers
network: true
overview: 'Geocode Earth publishes 3 APIs on the [APIs.io](https://apis.io/) network: Forward API, Place API, and Reverse API. Tagged areas include Geocoding, Address Autocomplete, Reverse Geocoding, Mapping, and Pelias.


  Geocode Earth''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Geocode Earth Plans Pricing
  plan_count: 5
  slug: geocode-earth-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 4
  name: Geocode Earth Rate Limits
  slug: geocode-earth-rate-limits
score:
  band: thin
  composite: 37.6
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/geocode-earth/refs/heads/main/screenshots/geocode-earth-2026-07-25T215637.png
security:
- kind: authentication
  name: Geocode Earth Authentication
  slug: geocode-earth-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Geocode Earth Domain Security
  slug: geocode-earth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: geocode-earth
tags:
- Geocoding
- Address Autocomplete
- Reverse Geocoding
- Mapping
- Pelias
- Open Data
website: https://geocode.earth/
---
