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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Vatsim Agentic Access
  operation_count: 34
  slug: vatsim-agentic-access
  summary_line: 34 operations · 2 acting
api_count: 18
apis:
- description: Delivers information about upcoming events on the VATSIM network, including dates, times, organizers, airports, routes, and banner images. Publicly accessible without authentication and provides listi
  name: VATSIM Events API
  slug: vatsim-events-api
- description: Grants access to real-time METAR weather information for airports around the world. Accepts single or comma-delimited ICAO airport codes, supports a special "all" value for bulk retrieval, and returns
  name: VATSIM METAR API
  slug: vatsim-metar-api
- description: OAuth 2.0 single sign-on authentication service for VATSIM members. Enables third-party applications and VATSIM organizations to authenticate users and access authorized profile data including full na
  name: VATSIM Connect API
  slug: vatsim-connect-api
- description: Provides real-time connection information for individual VATSIM users, delivering live session data for a given VATSIM member. Publicly accessible without authentication.
  name: VATSIM Slurper API
  slug: vatsim-slurper-api
- description: The Airport info API from VATSIM — 2 operation(s) for airport info.
  name: VATSIM Airport info API
  slug: vatsim-airport-info-api
- description: The atc API from VATSIM — 2 operation(s) for atc.
  name: VATSIM atc API
  slug: vatsim-atc-api
- description: The Audio API from VATSIM — 2 operation(s) for audio.
  name: VATSIM Audio API
  slug: vatsim-audio-api
- description: The community API from VATSIM — 1 operation(s) for community.
  name: VATSIM community API
  slug: vatsim-community-api
- description: The Data feed API from VATSIM — 1 operation(s) for data feed.
  name: VATSIM Data feed API
  slug: vatsim-data-feed-api
- description: The Event info API from VATSIM — 6 operation(s) for event info.
  name: VATSIM Event info API
  slug: vatsim-event-info-api
- description: The Events API from VATSIM — 2 operation(s) for events.
  name: VATSIM Events API
  slug: vatsim-events-api
- description: The members API from VATSIM — 7 operation(s) for members.
  name: VATSIM members API
  slug: vatsim-members-api
- description: The METAR API from VATSIM — 1 operation(s) for metar.
  name: VATSIM METAR API
  slug: vatsim-metar-api
- description: The OAuth2 API from VATSIM — 2 operation(s) for oauth2.
  name: VATSIM OAuth2 API
  slug: vatsim-oauth2-api
- description: The orgs API from VATSIM — 2 operation(s) for orgs.
  name: VATSIM orgs API
  slug: vatsim-orgs-api
- description: The Servers API from VATSIM — 3 operation(s) for servers.
  name: VATSIM Servers API
  slug: vatsim-servers-api
- description: The User API from VATSIM — 1 operation(s) for user.
  name: VATSIM User API
  slug: vatsim-user-api
- description: The Users API from VATSIM — 1 operation(s) for users.
  name: VATSIM Users API
  slug: vatsim-users-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: VATSIM AIP Airport info API
  slug: open-vatsim-airport-info-api
- collection_type: open
  name: VATSIM AIP Airport info atc API
  slug: open-vatsim-atc-api
- collection_type: open
  name: VATSIM AIP Airport info Audio API
  slug: open-vatsim-audio-api
- collection_type: open
  name: VATSIM AIP Airport info community API
  slug: open-vatsim-community-api
- collection_type: open
  name: VATSIM AIP Airport info Data feed API
  slug: open-vatsim-data-feed-api
- collection_type: open
  name: VATSIM AIP Airport info Event info API
  slug: open-vatsim-event-info-api
- collection_type: open
  name: VATSIM AIP Airport info Events API
  slug: open-vatsim-events-api
- collection_type: open
  name: VATSIM AIP Airport info members API
  slug: open-vatsim-members-api
- collection_type: open
  name: VATSIM AIP Airport info METAR API
  slug: open-vatsim-metar-api
- collection_type: open
  name: VATSIM AIP Airport info OAuth2 API
  slug: open-vatsim-oauth2-api
- collection_type: open
  name: VATSIM AIP Airport info orgs API
  slug: open-vatsim-orgs-api
- collection_type: open
  name: VATSIM AIP Airport info Servers API
  slug: open-vatsim-servers-api
- collection_type: open
  name: VATSIM AIP Airport info User API
  slug: open-vatsim-user-api
- collection_type: open
  name: VATSIM AIP Airport info Users API
  slug: open-vatsim-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vatsim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vatsim-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vatsim-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vatsim-scopes.yml
description: VATSIM (Virtual Air Traffic Simulation Network) is a global online flight simulation network providing real-time data about pilots, controllers, flight plans, and ATC positions. The VATSIM REST APIs allow developers to access live network data, member statistics, aviation weather, upcoming events, and authentication services for the simulation community.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://vatsim.net/favicon.ico
layout: provider
modified: 2026-06-13
name: VATSIM
nav: Providers
network: true
overview: 'VATSIM publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Events API, METAR API, Airport info API, and 13 more. Tagged areas include Aviation, Flight Simulation, Air Traffic Control, Real-Time Data, and Community.


  VATSIM''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 64
rate_limits:
- limit_count: 1
  name: Rate Limits
  slug: rate-limits
scopes:
- name: Vatsim Scopes
  scope_count: 4
  slug: vatsim-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 32.4
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vatsim/refs/heads/main/screenshots/vatsim-2026-06-20T200846.png
security:
- kind: authentication
  name: Vatsim Authentication
  slug: vatsim-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Vatsim Domain Security
  slug: vatsim-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: vatsim
tags:
- Aviation
- Flight Simulation
- Air Traffic Control
- Real-Time Data
- Community
website: https://vatsim.dev/services/apis/
---
