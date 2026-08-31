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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Airport Gap Agentic Access
  operation_count: 10
  slug: airport-gap-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
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
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airport Gap REST Airports API
  slug: open-airport-gap-airports-api
- collection_type: open
  name: Airport Gap REST Airports Distance API
  slug: open-airport-gap-distance-api
- collection_type: open
  name: Airport Gap REST Airports Favorites API
  slug: open-airport-gap-favorites-api
- collection_type: open
  name: Airport Gap REST Airports Tokens API
  slug: open-airport-gap-tokens-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dennmart/airport_gap/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/dennmart/airport_gap/blob/main/LICENSE
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


  Airport Gap''s developer surface includes authentication, documentation, signup flow, and 9 more developer resources.'
plans:
- name: Airport Gap Plans Pricing
  plan_count: 1
  slug: airport-gap-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Airport Gap Rate Limits
  slug: airport-gap-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Airport Gap API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: airport-gap-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 9.8
    contract_quality: 68.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
