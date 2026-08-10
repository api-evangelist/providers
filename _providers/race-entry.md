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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Race Entry Agentic Access
  operation_count: 20
  slug: race-entry-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 16
apis:
- description: The Event API from Race Entry — 3 operation(s) for event.
  name: Race Entry Event API
  slug: race-entry-event-api
- description: The Get Category Teams API from Race Entry — 1 operation(s) for get category teams.
  name: Race Entry Get Category Teams API
  slug: race-entry-get-category-teams-api
- description: The Get Event Categories API from Race Entry — 1 operation(s) for get event categories.
  name: Race Entry Get Event Categories API
  slug: race-entry-get-event-categories-api
- description: The Get Event Participants API from Race Entry — 1 operation(s) for get event participants.
  name: Race Entry Get Event Participants API
  slug: race-entry-get-event-participants-api
- description: The Get Event Pin API from Race Entry — 1 operation(s) for get event pin.
  name: Race Entry Get Event Pin API
  slug: race-entry-get-event-pin-api
- description: The Get Event Questions API from Race Entry — 1 operation(s) for get event questions.
  name: Race Entry Get Event Questions API
  slug: race-entry-get-event-questions-api
- description: The Get Event Teams API from Race Entry — 1 operation(s) for get event teams.
  name: Race Entry Get Event Teams API
  slug: race-entry-get-event-teams-api
- description: The Get Events API from Race Entry — 1 operation(s) for get events.
  name: Race Entry Get Events API
  slug: race-entry-get-events-api
- description: The Login API from Race Entry — 1 operation(s) for login.
  name: Race Entry Login API
  slug: race-entry-login-api
- description: The Memberships API from Race Entry — 2 operation(s) for memberships.
  name: Race Entry Memberships API
  slug: race-entry-memberships-api
- description: The Result API from Race Entry — 2 operation(s) for result.
  name: Race Entry Result API
  slug: race-entry-result-api
- description: The Set Event App Access API from Race Entry — 1 operation(s) for set event app access.
  name: Race Entry Set Event App Access API
  slug: race-entry-set-event-app-access-api
- description: The Set Event Pin API from Race Entry — 1 operation(s) for set event pin.
  name: Race Entry Set Event Pin API
  slug: race-entry-set-event-pin-api
- description: The Update Event Participant API from Race Entry — 1 operation(s) for update event participant.
  name: Race Entry Update Event Participant API
  slug: race-entry-update-event-participant-api
- description: The Upload API from Race Entry — 1 operation(s) for upload.
  name: Race Entry Upload API
  slug: race-entry-upload-api
- description: The User API from Race Entry — 1 operation(s) for user.
  name: Race Entry User API
  slug: race-entry-user-api
artifact_total: 23
collections:
- collection_type: open
  name: Race Entry Software API
  slug: open-race-entry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/race-entry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/race-entry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/race-entry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/raceentry-com
created: '2025-02-06'
description: This API was designed specifically for the Director software to allow certain timers and directors integration into our Race Entry data with the Director. It provides programmatic access to events, registrations, participants, teams, results, check-in PINs, and club memberships, with temporary key/secret authentication issued via a login endpoint.
finops:
- name: Race Entry Finops
  service_category: API
  slug: race-entry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/race-entry.png
layout: provider
modified: '2026-05-19'
name: Race Entry
nav: Providers
network: true
overview: 'Race Entry publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Event API, Get Category Teams API, Get Event Categories API, and 13 more. Tagged areas include Race Timing, Race Registration, Event Management, Race Results, and Sports.


  Race Entry''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Race Entry Plans Pricing
  plan_count: 3
  slug: race-entry-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Race Entry Rate Limits
  slug: race-entry-rate-limits
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/race-entry/refs/heads/main/screenshots/race-entry-2026-06-20T192506.png
security:
- kind: authentication
  name: Race Entry Authentication
  slug: race-entry-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Race Entry Domain Security
  slug: race-entry-domain-security
  summary_line: TLSv1.3 · HSTS
slug: race-entry
tags:
- Race Timing
- Race Registration
- Event Management
- Race Results
- Sports
---
