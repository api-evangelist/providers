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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spacetrack Agentic Access
  operation_count: 22
  slug: spacetrack-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 7
apis:
- description: Launch sites, boxscore, announcements, and other reference data
  name: Space-Track Ancillary API
  slug: spacetrack-ancillary-api
- description: Session-based authentication via cookie
  name: Space-Track Authentication API
  slug: spacetrack-authentication-api
- description: Spaceflight safety conjunction data messages (CDM)
  name: Space-Track Conjunction Data API
  slug: spacetrack-conjunction-data-api
- description: Satellite reentry and decay predictions
  name: Space-Track Decay Predictions API
  slug: spacetrack-decay-predictions-api
- description: Current and historical SGP4 keplerian element sets (TLE/OMM)
  name: Space-Track General Perturbations API
  slug: spacetrack-general-perturbations-api
- description: Catalog metadata for all tracked Earth-orbiting objects
  name: Space-Track Satellite Catalog API
  slug: spacetrack-satellite-catalog-api
- description: Reentry tracking and impact prediction messages (TIP)
  name: Space-Track Tracking and Impact Prediction API
  slug: spacetrack-tracking-and-impact-prediction-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacetrack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacetrack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spacetrack-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.space-track.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.space-track.org/documentation
- group: start
  title: ''
  type: Login
  url: https://www.space-track.org/auth/login
- group: other
  title: ''
  type: Registration
  url: https://www.space-track.org/auth/createAccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.space-track.org/documentation#user-agreement
- group: operate
  title: ''
  type: Contact
  url: https://www.space-track.org/contactus/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/finops/finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/openapi/openapi.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/json-ld/context.jsonld
created: '2026-06-13'
description: US military space surveillance REST API providing Two-Line Element (TLE) sets, conjunction data messages, orbital element sets, satellite catalog data, and decay predictions for tracked satellites and debris operated by the 18th Space Control Squadron.
examples:
- key_count: 4
  name: Cdm Query
  slug: cdm-query
- key_count: 3
  name: Gp Iss
  slug: gp-iss
- key_count: 4
  name: Login
  slug: login
- key_count: 3
  name: Satcat Query
  slug: satcat-query
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.space-track.org/favicon.ico
json_schemas:
- name: GP Record
  property_count: 33
  slug: gp-record
- name: SATCAT Record
  property_count: 24
  slug: satcat-record
jsonld:
- class_count: 0
  name: context Context
  property_count: 43
  slug: context
layout: provider
modified: '2026-06-13'
name: Space-Track
nav: Providers
network: true
overview: 'Space-Track publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ancillary API, Authentication API, Conjunction Data API, and 4 more. Tagged areas include Space, Satellites, TLE, Orbital Data, and Space Surveillance.


  The Space-Track catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Space-Track''s developer surface includes authentication, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 40
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Space-Track API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spacetrack-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 78.3
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/screenshots/spacetrack-2026-06-20T194237.png
security:
- kind: authentication
  name: Spacetrack Authentication
  slug: spacetrack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spacetrack Domain Security
  slug: spacetrack-domain-security
  summary_line: TLSv1.3
slug: spacetrack
tags:
- Space
- Satellites
- TLE
- Orbital Data
- Space Surveillance
- Debris Tracking
- Conjunction Data
- US Military
website: https://www.space-track.org
---
