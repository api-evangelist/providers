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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openf1 Agentic Access
  operation_count: 13
  slug: openf1-agentic-access
  summary_line: 13 operations
api_count: 11
apis:
- description: The Drivers API from OpenF1 — 1 operation(s) for drivers.
  name: OpenF1 Drivers API
  slug: openf1-drivers-api
- description: The Laps API from OpenF1 — 1 operation(s) for laps.
  name: OpenF1 Laps API
  slug: openf1-laps-api
- description: The Meetings API from OpenF1 — 1 operation(s) for meetings.
  name: OpenF1 Meetings API
  slug: openf1-meetings-api
- description: The Pit API from OpenF1 — 1 operation(s) for pit.
  name: OpenF1 Pit API
  slug: openf1-pit-api
- description: The Position API from OpenF1 — 2 operation(s) for position.
  name: OpenF1 Position API
  slug: openf1-position-api
- description: The RaceControl API from OpenF1 — 1 operation(s) for racecontrol.
  name: OpenF1 RaceControl API
  slug: openf1-racecontrol-api
- description: The Sessions API from OpenF1 — 1 operation(s) for sessions.
  name: OpenF1 Sessions API
  slug: openf1-sessions-api
- description: The Stints API from OpenF1 — 1 operation(s) for stints.
  name: OpenF1 Stints API
  slug: openf1-stints-api
- description: The TeamRadio API from OpenF1 — 1 operation(s) for teamradio.
  name: OpenF1 TeamRadio API
  slug: openf1-teamradio-api
- description: The Telemetry API from OpenF1 — 2 operation(s) for telemetry.
  name: OpenF1 Telemetry API
  slug: openf1-telemetry-api
- description: The Weather API from OpenF1 — 1 operation(s) for weather.
  name: OpenF1 Weather API
  slug: openf1-weather-api
artifact_total: 23
collections:
- collection_type: open
  name: OpenF1 API
  slug: open-openf1
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openf1-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openf1-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://openf1.org/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/br-g/openf1
created: '2025-02-06'
description: OpenF1 is a free and open-source API providing real-time and historical Formula 1 data including car telemetry, lap timings, race control messages, weather, pit stops, team radio, and championship standings.
finops:
- name: Openf1 Finops
  service_category: API
  slug: openf1-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openf1.png
json_schemas:
- name: OpenF1 Car Telemetry
  property_count: 10
  slug: openf1-cardata
- name: OpenF1 Driver
  property_count: 12
  slug: openf1-driver
- name: OpenF1 Lap
  property_count: 13
  slug: openf1-lap
- name: OpenF1 Session
  property_count: 15
  slug: openf1-session
jsonld:
- class_count: 0
  name: Openf1 Context
  property_count: 5
  slug: openf1-context
layout: provider
modified: '2026-05-19'
name: OpenF1
nav: Providers
network: true
overview: 'OpenF1 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Drivers API, Laps API, Meetings API, and 8 more. Tagged areas include Formula 1, Motorsport, Telemetry, Real-Time, and Sports.


  The OpenF1 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenF1''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Openf1 Plans Pricing
  plan_count: 3
  slug: openf1-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Openf1 Rate Limits
  slug: openf1-rate-limits
rules:
- name: OpenF1 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openf1-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.0
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openf1/refs/heads/main/screenshots/openf1-2026-06-20T190958.png
security:
- kind: domain-security
  name: Openf1 Domain Security
  slug: openf1-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: openf1
tags:
- Formula 1
- Motorsport
- Telemetry
- Real-Time
- Sports
---
