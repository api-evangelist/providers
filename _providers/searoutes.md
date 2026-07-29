---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Searoutes Agentic Access
  operation_count: 32
  slug: searoutes-agentic-access
  summary_line: 32 operations · 2 acting
api_count: 6
apis:
- description: Multimodal CO2e emission calculations (sea, road, rail, air, inland water).
  name: Searoutes CO2 Emissions API
  slug: searoutes-co2-emissions-api
- description: Ports, airports, places, areas, postal codes, and nearest points.
  name: Searoutes Geocoding API
  slug: searoutes-geocoding-api
- description: Sea routes, distances, durations, and voyage plans.
  name: Searoutes Ocean Routing API
  slug: searoutes-ocean-routing-api
- description: Carrier and liner-service lookup.
  name: Searoutes Search API
  slug: searoutes-search-api
- description: AIS vessel positions, ETAs, arrivals, traces, and time series.
  name: Searoutes Vessel API
  slug: searoutes-vessel-api
- description: Historical, real-time, and forecasted weather.
  name: Searoutes Weather API
  slug: searoutes-weather-api
artifact_total: 13
collections:
- collection_type: open
  name: Searoutes API
  slug: open-searoutes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/searoutes-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/searoutes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/searoutes-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/searoutes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/searoutes
- group: company
  title: ''
  type: Website
  url: https://searoutes.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.searoutes.com/reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/searoutes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/searoutes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/searoutes-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://searoutes.com/blog/feed/
created: '2026-07-03'
description: Searoutes is a maritime routing and carbon-emissions API platform for logistics, freight forwarding, and supply-chain teams. Its REST APIs compute point-to-point, port-to-point, and port-to-port sea routes with distances and durations (including SECA, HRA, and ice-area avoidance), geocode ports, airports, and places, calculate multimodal CO2e emissions (sea, road, rail, air, inland waterway) using a GLEC-accredited methodology, track vessels via AIS (positions, ETAs, traces, arrivals), look up carriers and services, and return historical, real-time, and forecasted weather along routes. All APIs are served from https://api.searoutes.com and authenticated with an x-api-key header.
finops:
- name: Searoutes Finops
  service_category: Maritime and Logistics
  slug: searoutes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/searoutes.png
layout: provider
modified: '2026-07-03'
name: Searoutes
nav: Providers
network: true
overview: 'Searoutes publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CO2 Emissions API, Geocoding API, Ocean Routing API, and 3 more. Tagged areas include Maritime, Sea Routing, Ocean Freight, CO2 Emissions, and Carbon Accounting.


  Searoutes'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Searoutes Plans Pricing
  plan_count: 5
  slug: searoutes-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Searoutes Rate Limits
  slug: searoutes-rate-limits
score:
  band: thin
  composite: 38.4
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Searoutes Authentication
  slug: searoutes-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Searoutes Domain Security
  slug: searoutes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: searoutes
tags:
- Maritime
- Sea Routing
- Ocean Freight
- CO2 Emissions
- Carbon Accounting
- Vessel Tracking
- AIS
- Geocoding
- Logistics
- Supply Chain
website: https://searoutes.com
---
