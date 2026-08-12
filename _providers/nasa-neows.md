---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Neows Agentic Access
  operation_count: 3
  slug: nasa-neows-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Browse API from NASA NeoWs — 1 operation(s) for browse.
  name: NASA NeoWs Browse API
  slug: nasa-neows-browse-api
- description: The Feed API from NASA NeoWs — 1 operation(s) for feed.
  name: NASA NeoWs Feed API
  slug: nasa-neows-feed-api
- description: The Lookup API from NASA NeoWs — 1 operation(s) for lookup.
  name: NASA NeoWs Lookup API
  slug: nasa-neows-lookup-api
artifact_total: 17
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nasa/api-docs/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/nasa/api-docs/blob/gh-pages/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-neows-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-neows-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasa-neows-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://api.nasa.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://api.nasa.gov/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nasa
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/nasa/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://api.nasa.gov/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.api.nasa.gov/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usa.gov/developer-apis
- group: start
  title: ''
  type: Signup
  url: https://api.nasa.gov/#signUp
- group: commercial
  title: ''
  type: Plans
  url: plans/nasa-neows-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasa-neows-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nasa-neows-finops.yml
created: '2026-06-13'
description: NASA Near Earth Object Web Service (NeoWs) REST API for searching and browsing near Earth asteroid information. Users can search for asteroids based on their closest approach date to Earth, look up a specific asteroid by NASA JPL small body (SPK-ID), and browse the overall dataset. Data originates from the NASA JPL Asteroid team and is maintained by the SpaceRocks Team.
examples:
- key_count: 3
  name: Browse Asteroids
  slug: browse-asteroids
- key_count: 3
  name: Get Asteroid Feed
  slug: get-asteroid-feed
- key_count: 3
  name: Lookup Asteroid
  slug: lookup-asteroid
finops:
- name: Nasa Neows Finops
  service_category: ''
  slug: nasa-neows-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa-neows.png
json_schemas:
- name: AsteroidBrowseResponse
  property_count: 3
  slug: asteroid-browse-response
- name: AsteroidFeedResponse
  property_count: 3
  slug: asteroid-feed-response
- name: NearEarthObject
  property_count: 12
  slug: near-earth-object
jsonld:
- class_count: 8
  name: Nasa Neows Context
  property_count: 53
  slug: nasa-neows-context
layout: provider
modified: '2026-06-13'
name: NASA NeoWs
nav: Providers
network: true
overview: 'NASA NeoWs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Browse API, Feed API, and Lookup API. Tagged areas include NASA, Asteroids, Near Earth Objects, Space, and Science.


  The NASA NeoWs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA NeoWs'' developer surface includes authentication, documentation, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Nasa Neows Plans Pricing
  plan_count: 3
  slug: nasa-neows-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 3
  name: Nasa Neows Rate Limits
  slug: nasa-neows-rate-limits
rules:
- name: NASA NeoWs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: nasa-neows-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.0
  delta: 1.7
  facets:
    commercial_clarity: 73.7
    contract_quality: 67.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 52.3
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
    score: 38.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa-neows/refs/heads/main/screenshots/nasa-neows-2026-06-20T185953.png
security:
- kind: authentication
  name: Nasa Neows Authentication
  slug: nasa-neows-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nasa Neows Domain Security
  slug: nasa-neows-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nasa-neows
tags:
- NASA
- Asteroids
- Near Earth Objects
- Space
- Science
- Open Data
- Planetary Defense
website: https://api.nasa.gov/
---
