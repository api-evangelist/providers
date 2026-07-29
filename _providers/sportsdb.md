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
- acting_count: 0
  human_in_the_loop: 0
  name: Sportsdb Agentic Access
  operation_count: 22
  slug: sportsdb-agentic-access
  summary_line: 22 operations
api_count: 7
apis:
- description: The Events API from TheSportsDB — 5 operation(s) for events.
  name: TheSportsDB Events API
  slug: sportsdb-events-api
- description: The Leagues API from TheSportsDB — 5 operation(s) for leagues.
  name: TheSportsDB Leagues API
  slug: sportsdb-leagues-api
- description: The Livescores API from TheSportsDB — 1 operation(s) for livescores.
  name: TheSportsDB Livescores API
  slug: sportsdb-livescores-api
- description: The Lookup API from TheSportsDB — 5 operation(s) for lookup.
  name: TheSportsDB Lookup API
  slug: sportsdb-lookup-api
- description: The Players API from TheSportsDB — 1 operation(s) for players.
  name: TheSportsDB Players API
  slug: sportsdb-players-api
- description: The Search API from TheSportsDB — 4 operation(s) for search.
  name: TheSportsDB Search API
  slug: sportsdb-search-api
- description: The Teams API from TheSportsDB — 1 operation(s) for teams.
  name: TheSportsDB Teams API
  slug: sportsdb-teams-api
artifact_total: 14
collections:
- collection_type: open
  name: TheSportsDB API
  slug: open-sportsdb
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportsdb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportsdb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportsdb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thesportsdb
- group: company
  title: ''
  type: Website
  url: https://www.thesportsdb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.thesportsdb.com/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/sportsdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sportsdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sportsdb-finops.yml
created: '2026-06-25'
description: TheSportsDB is an open, crowd-sourced database of sports artwork and metadata with a free REST API in JSON. It provides data on leagues, teams, players, events, venues, schedules, and season standings across soccer, basketball, baseball, American football, hockey, tennis, and many other sports worldwide, with premium V2 livescores and video highlights for supporters.
finops:
- name: Sportsdb Finops
  service_category: Sports Data and Media
  slug: sportsdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportsdb.png
layout: provider
modified: '2026-06-25'
name: TheSportsDB
nav: Providers
network: true
overview: 'TheSportsDB publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Leagues API, Livescores API, and 4 more. Tagged areas include Sports, Sports Data, Teams, Players, and Events.


  TheSportsDB''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Sportsdb Plans Pricing
  plan_count: 3
  slug: sportsdb-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Sportsdb Rate Limits
  slug: sportsdb-rate-limits
score:
  band: thin
  composite: 35.8
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sportsdb Authentication
  slug: sportsdb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sportsdb Domain Security
  slug: sportsdb-domain-security
  summary_line: TLSv1.3
slug: sportsdb
tags:
- Sports
- Sports Data
- Teams
- Players
- Events
website: https://www.thesportsdb.com
---
