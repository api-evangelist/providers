---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zenplanner Agentic Access
  operation_count: 10
  slug: zenplanner-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 7
apis:
- description: The Classes API from Zen Planner — 3 operation(s) for classes.
  name: Zen Planner Classes API
  slug: zenplanner-classes-api
- description: The Groups API from Zen Planner — 1 operation(s) for groups.
  name: Zen Planner Groups API
  slug: zenplanner-groups-api
- description: The Locations API from Zen Planner — 1 operation(s) for locations.
  name: Zen Planner Locations API
  slug: zenplanner-locations-api
- description: The Memberships API from Zen Planner — 1 operation(s) for memberships.
  name: Zen Planner Memberships API
  slug: zenplanner-memberships-api
- description: The People API from Zen Planner — 2 operation(s) for people.
  name: Zen Planner People API
  slug: zenplanner-people-api
- description: The Programs API from Zen Planner — 1 operation(s) for programs.
  name: Zen Planner Programs API
  slug: zenplanner-programs-api
- description: The Prospects API from Zen Planner — 1 operation(s) for prospects.
  name: Zen Planner Prospects API
  slug: zenplanner-prospects-api
artifact_total: 12
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenplanner-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenplanner-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenplanner-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zenplanner-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zenplanner
- group: company
  title: ''
  type: Website
  url: https://zenplanner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.partners.daxko.com/openapi/ZenPlanner/v1/
- group: commercial
  title: ''
  type: Plans
  url: plans/zenplanner-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://zenplanner.com/feed/
created: '2026-07-04'
description: Zen Planner is gym, martial arts, yoga, affiliate, and fitness studio management software covering membership management, billing and payments, class scheduling, attendance and check-ins, skills and belt tracking, and a member app. Zen Planner is owned by Daxko, and its developer API is published on the shared Daxko Partners platform as the Zen Planner API. The API is partner-gated - access is requested through a Daxko sales representative - but the API reference is publicly documented via Daxko's Redocly-hosted docs. It exposes REST endpoints for People, Memberships, Classes (schedules, reservations, attendances), Locations, Programs, Prospects, and Groups, authenticated with OAuth 2.0 against the Daxko Partners token service.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenplanner.png
layout: provider
modified: '2026-07-04'
name: Zen Planner
nav: Providers
network: true
overview: 'Zen Planner publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Classes API, Groups API, Locations API, and 4 more. Tagged areas include Fitness, Gym Management, Studio Management, Martial Arts, and Membership.


  Zen Planner''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Zenplanner Plans Pricing
  plan_count: 4
  slug: zenplanner-plans-pricing
random_paper: 65
scopes:
- name: Zenplanner Scopes
  scope_count: 0
  slug: zenplanner-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 54.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Zenplanner Authentication
  slug: zenplanner-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zenplanner Domain Security
  slug: zenplanner-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenplanner
tags:
- Fitness
- Gym Management
- Studio Management
- Martial Arts
- Membership
- Scheduling
- Class Booking
- Daxko
website: https://zenplanner.com/
---
