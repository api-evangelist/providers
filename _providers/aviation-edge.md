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
- acting_count: 0
  human_in_the_loop: 0
  name: Aviation Edge Agentic Access
  operation_count: 13
  slug: aviation-edge-agentic-access
  summary_line: 13 operations
api_count: 5
apis:
- description: Aviation Edge API provides comprehensive aviation data including real-time flight tracking, airport information, airline schedules, aircraft data, and satellite tracking for global aviation intelligen
  name: Aviation Edge
  slug: aviation-edge
- description: Real-time and live flight tracking
  name: Aviation Edge Real-Time API
  slug: aviation-edge-real-time-api
- description: Static reference data
  name: Aviation Edge Reference API
  slug: aviation-edge-reference-api
- description: Satellite tracking data
  name: Aviation Edge Satellites API
  slug: aviation-edge-satellites-api
- description: Airport schedules and flight timetables
  name: Aviation Edge Schedules API
  slug: aviation-edge-schedules-api
artifact_total: 12
collections:
- collection_type: open
  name: Aviation Edge API
  slug: open-aviation-edge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aviation-edge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aviation-edge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aviation-edge-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aviation-edge.com/developers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aviation-edge
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aviation-edge/
- group: company
  title: ''
  type: Blog
  url: https://aviation-edge.com/feed/
created: '2025-02-06'
description: Aviation Edge is a leading provider of aviation data and technology solutions for the global aviation industry. The company offers comprehensive and accurate data sets that cover everything from flight schedules and airline information to airport details and aircraft data.
finops:
- name: Aviation Edge Finops
  service_category: API
  slug: aviation-edge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aviation-edge.png
layout: provider
modified: '2026-04-19'
name: Aviation Edge
nav: Providers
network: true
overview: 'Aviation Edge publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Real-Time API, Reference API, Satellites API, and 1 more. Tagged areas include Airlines, Airports, Aviation, Flight Data, and Real-Time.


  Aviation Edge''s developer surface includes authentication, developer portal, engineering blog, and 4 more developer resources.'
plans:
- name: Aviation Edge Plans Pricing
  plan_count: 3
  slug: aviation-edge-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Aviation Edge Rate Limits
  slug: aviation-edge-rate-limits
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aviation-edge/refs/heads/main/screenshots/aviation-edge-2026-06-20T172729.png
security:
- kind: authentication
  name: Aviation Edge Authentication
  slug: aviation-edge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aviation Edge Domain Security
  slug: aviation-edge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aviation-edge
tags:
- Airlines
- Airports
- Aviation
- Flight Data
- Real-Time
website: https://aviation-edge.com/developers/
---
