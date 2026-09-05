---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sportsdb Agentic Access
  operation_count: 22
  slug: sportsdb-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Events API from TheSportsDB — 5 operation(s) for events.
  name: TheSportsDB Events API
  slug: sportsdb-events-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Leagues API from TheSportsDB — 5 operation(s) for leagues.
  name: TheSportsDB Leagues API
  slug: sportsdb-leagues-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Livescores API from TheSportsDB — 1 operation(s) for livescores.
  name: TheSportsDB Livescores API
  slug: sportsdb-livescores-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Lookup API from TheSportsDB — 5 operation(s) for lookup.
  name: TheSportsDB Lookup API
  slug: sportsdb-lookup-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Players API from TheSportsDB — 1 operation(s) for players.
  name: TheSportsDB Players API
  slug: sportsdb-players-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Search API from TheSportsDB — 4 operation(s) for search.
  name: TheSportsDB Search API
  slug: sportsdb-search-api
- baseURL: https://www.thesportsdb.com/api/v1/json
  baseurl_source: declared
  description: The Teams API from TheSportsDB — 1 operation(s) for teams.
  name: TheSportsDB Teams API
  slug: sportsdb-teams-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TheSportsDB Events API
  slug: open-sportsdb-events-api
- collection_type: open
  name: TheSportsDB Events Leagues API
  slug: open-sportsdb-leagues-api
- collection_type: open
  name: TheSportsDB Events Livescores API
  slug: open-sportsdb-livescores-api
- collection_type: open
  name: TheSportsDB Events Lookup API
  slug: open-sportsdb-lookup-api
- collection_type: open
  name: TheSportsDB Events Players API
  slug: open-sportsdb-players-api
- collection_type: open
  name: TheSportsDB Events Search API
  slug: open-sportsdb-search-api
- collection_type: open
  name: TheSportsDB Events Teams API
  slug: open-sportsdb-teams-api
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
overview: 'TheSportsDB publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Events API, Leagues API, Livescores API, and 4 more. Tagged areas include Sports, Sports Data, Team, Players, and Event.


  TheSportsDB''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Sportsdb Plans Pricing
  plan_count: 3
  slug: sportsdb-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Sportsdb Rate Limits
  slug: sportsdb-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 22.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportsdb/refs/heads/main/screenshots/sportsdb-2026-09-02T160548.png
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
- Team
- Players
- Event
website: https://www.thesportsdb.com
---
