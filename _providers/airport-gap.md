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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Airport Gap Agentic Access
  operation_count: 10
  slug: airport-gap-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 4
apis:
- description: Retrieve airport information by IATA code or browse the full database.
  name: Airport Gap Airports API
  slug: airport-gap-airports-api
- description: Calculate great-circle distances between two airports.
  name: Airport Gap Distance API
  slug: airport-gap-distance-api
- description: Manage saved favorite airports (authenticated users only).
  name: Airport Gap Favorites API
  slug: airport-gap-favorites-api
- description: Generate Bearer tokens for authenticated access.
  name: Airport Gap Tokens API
  slug: airport-gap-tokens-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airport-gap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airport-gap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airport-gap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://airportgap.com
- group: docs
  title: ''
  type: Documentation
  url: https://airportgap.com/docs
- group: start
  title: ''
  type: Signup
  url: https://airportgap.com/tokens/new
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dennmart/airport_gap
- group: commercial
  title: ''
  type: Plans
  url: plans/airport-gap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airport-gap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airport-gap-finops.yml
created: '2026-06-13'
description: Airport Gap is a RESTful API designed to help developers practice API automation testing. It provides access to a database of worldwide airports including ICAO/IATA codes, location coordinates, elevation, and country information. The API also supports calculating distances between airports in miles, kilometers, and nautical miles, and allows authenticated users to save and manage favorite airports. Data is sourced from OpenFlights.org under the Open Database License (ODbL 1.0).
examples:
- key_count: 3
  name: Delete Favorites Clear All
  slug: delete-favorites-clear-all
- key_count: 3
  name: Get Airport Jfk
  slug: get-airport-jfk
- key_count: 3
  name: Post Airports Distance
  slug: post-airports-distance
- key_count: 3
  name: Post Favorites
  slug: post-favorites
- key_count: 3
  name: Post Tokens
  slug: post-tokens
finops:
- name: Airport Gap Finops
  service_category: Developer Tools
  slug: airport-gap-finops
image: https://airportgap.com/favicon.ico
json_schemas:
- name: Airport
  property_count: 3
  slug: airport
- name: AirportDistance
  property_count: 3
  slug: distance
- name: Favorite
  property_count: 3
  slug: favorite
jsonld:
- class_count: 2
  name: Airport Gap Context
  property_count: 17
  slug: airport-gap-context
layout: provider
modified: '2026-06-13'
name: Airport Gap
nav: Providers
network: true
overview: 'Airport Gap publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Airports API, Distance API, Favorites API, and 1 more. Tagged areas include Airports, Aviation, Transportation, IATA, and ICAO.


  The Airport Gap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Airport Gap''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Airport Gap Plans Pricing
  plan_count: 1
  slug: airport-gap-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Airport Gap Rate Limits
  slug: airport-gap-rate-limits
rules:
- name: Airport Gap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airport-gap-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.8
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 48.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airport-gap/refs/heads/main/screenshots/airport-gap-2026-06-20T171424.png
security:
- kind: authentication
  name: Airport Gap Authentication
  slug: airport-gap-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airport Gap Domain Security
  slug: airport-gap-domain-security
  summary_line: TLSv1.3 · HSTS
slug: airport-gap
tags:
- Airports
- Aviation
- Transportation
- IATA
- ICAO
- Distance Calculation
- Geolocation
website: https://airportgap.com
---
