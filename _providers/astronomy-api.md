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
  name: Astronomy Api Agentic Access
  operation_count: 7
  slug: astronomy-api-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 5
apis:
- description: The Astronomy API provides access to astronomical data including celestial body positions, moon phases, planet positions, star charts, astronomical events, and deep space object search for any locatio
  name: Astronomy API
  slug: astronomy-api
- description: Celestial body information and positions
  name: Astronomy API Bodies API
  slug: astronomy-api-bodies-api
- description: Astronomical events for a given location and date range
  name: Astronomy API Events API
  slug: astronomy-api-events-api
- description: Search for stars and deep space objects
  name: Astronomy API Search API
  slug: astronomy-api-search-api
- description: Generated imagery (moon phase and star charts)
  name: Astronomy API Studio API
  slug: astronomy-api-studio-api
artifact_total: 22
collections:
- collection_type: open
  name: Astronomy API
  slug: open-astronomy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/astronomy-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astronomy-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/astronomy-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AstronomyAPI
- group: start
  title: Astronomy API Website
  type: Portal
  url: https://astronomyapi.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://docs.astronomyapi.com/
- group: start
  title: Sign Up
  type: Signup
  url: https://astronomyapi.com/auth/signup
- group: commercial
  title: Pricing
  type: Pricing
  url: https://astronomyapi.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://astronomyapi.com/llms.txt
created: '2024-03-30'
description: AstronomyAPI is a web API for retrieving astronomical information including data about celestial bodies, moon phases, planet positions, star charts, and astronomical events for a given location and time. The API provides developers with access to celestial body positions, astronomical event data, star chart generation, moon phase imagery, and deep space object search capabilities for any geographic location and date/time combination.
features:
- description: Retrieve real-time and historical positions of celestial bodies including planets, moons, and other astronomical objects for any geographic location and date/time.
  name: Celestial Body Positions
- description: Access data on celestial events such as eclipses, conjunctions, and other notable astronomical occurrences for a given body and date range.
  name: Astronomical Events
- description: Generate customizable star charts as images for any sky position, date, and observer location for use in applications and publications.
  name: Star Chart Generation
- description: Generate moon phase images showing the illumination and appearance of the moon for any given date and location.
  name: Moon Phase Imagery
- description: Search for stars and deep space objects by name or catalog designation to retrieve positional and descriptive data.
  name: Deep Space Object Search
finops:
- name: Astronomy Api Finops
  service_category: API
  slug: astronomy-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/astronomy-api.png
integrations:
- description: Mobile applications integrate the Astronomy API to provide real-time sky data and star chart overlays for stargazing experiences.
  name: Mobile Astronomy Apps
- description: Planetarium and sky simulation software integrates celestial body position data from the Astronomy API for accurate sky rendering.
  name: Planetarium Software
layout: provider
modified: '2026-04-19'
name: Astronomy API
nav: Providers
network: true
overview: 'Astronomy API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Bodies API, Events API, Search API, and 1 more. Tagged areas include Astronomy, Celestial Data, Space, Moon Phases, and Star Charts.


  Astronomy API''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, and 4 more developer resources.'
plans:
- name: Astronomy Api Plans Pricing
  plan_count: 3
  slug: astronomy-api-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Astronomy Api Rate Limits
  slug: astronomy-api-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -2.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astronomy-api/refs/heads/main/screenshots/astronomy-api-2026-06-20T172510.png
security:
- kind: authentication
  name: Astronomy Api Authentication
  slug: astronomy-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Astronomy Api Domain Security
  slug: astronomy-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: astronomy-api
tags:
- Astronomy
- Celestial Data
- Space
- Moon Phases
- Star Charts
use_cases:
- description: Developers build educational astronomy applications that display real-time planet positions, star charts, and moon phases for learners and enthusiasts.
  name: Astronomy Education Apps
- description: Amateur astronomers use the API to plan observing sessions by retrieving celestial body positions and upcoming astronomical events for their location.
  name: Observation Planning Tools
- description: Astrology apps integrate the Astronomy API for accurate planetary position data to power birth chart calculations and transit predictions.
  name: Astrology and Horoscope Applications
website: https://astronomyapi.com/
---
