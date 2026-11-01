---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Realtimesportsapi Com Agentic Access
  operation_count: 100
  slug: realtimesportsapi-com-agentic-access
  summary_line: 100 operations · 12 acting
api_count: 1
apis:
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Athletes, search, game logs and availability history
  name: realtimesportsapi-com Athletes API
  slug: realtimesportsapi-com-athletes-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: 'Games: lists, live games, single game, box score, win probability, game rosters'
  name: realtimesportsapi-com Events API
  slug: realtimesportsapi-com-events-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Injury reports and normalized player availability
  name: realtimesportsapi-com Injuries & Availability API
  slug: realtimesportsapi-com-injuries-availability-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: League news and the news archive
  name: realtimesportsapi-com News API
  slug: realtimesportsapi-com-news-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Current betting lines and line history (single source book)
  name: realtimesportsapi-com Odds API
  slug: realtimesportsapi-com-odds-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Play-by-play and penalties
  name: realtimesportsapi-com Plays API
  slug: realtimesportsapi-com-plays-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Seasons, season types, groups, weeks, schedules and tournaments
  name: realtimesportsapi-com Seasons API
  slug: realtimesportsapi-com-seasons-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Sports and leagues
  name: realtimesportsapi-com Sports API
  slug: realtimesportsapi-com-sports-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Teams, rosters and depth charts
  name: realtimesportsapi-com Teams API
  slug: realtimesportsapi-com-teams-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Roster transactions
  name: realtimesportsapi-com Transactions API
  slug: realtimesportsapi-com-transactions-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Manage webhook subscriptions (paid plans). These management calls do not count toward your quota; deliveries do.
  name: realtimesportsapi-com Webhooks API
  slug: realtimesportsapi-com-webhooks-api
- baseURL: https://www.realtimesportsapi.com/api/v1
  baseurl_source: declared
  description: Get a short-lived token for the WebSocket push stream
  name: realtimesportsapi-com WebSocket API
  slug: realtimesportsapi-com-websocket-api
artifact_total: 27
asyncapis:
- description: ''
  name: Realtimesportsapi Com Webhooks
  slug: realtimesportsapi-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/realtimesportsapi-com/agentic-access/realtimesportsapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/realtimesportsapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/realtimesportsapi-com/plans/realtimesportsapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/realtimesportsapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/rules/realtimesportsapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/realtimesportsapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/json-ld/realtimesportsapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/realtimesportsapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/vocabulary/realtimesportsapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/realtimesportsapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/realtimesportsapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/asyncapi/realtimesportsapi-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/realtimesportsapi-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/data-model/realtimesportsapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/realtimesportsapi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/realtimesportsapi-com/changelog/realtimesportsapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/realtimesportsapi-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/errors/realtimesportsapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/realtimesportsapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/realtimesportsapi-com/conformance/realtimesportsapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/realtimesportsapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/realtimesportsapi-com/llms/realtimesportsapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/realtimesportsapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/realtimesportsapi-com/hosts/realtimesportsapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/realtimesportsapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/realtimesportsapi-com/vendors/realtimesportsapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/realtimesportsapi-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/realtimesportsapi-com/packages/realtimesportsapi-com-packages.yml
  title: ''
  type: SDKs
  url: packages/realtimesportsapi-com-packages.yml
- group: build
  href: https://artifacts.apis.io/realtimesportsapi-com/packages/realtimesportsapi-com-packages.yml
  title: ''
  type: Packages
  url: packages/realtimesportsapi-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.realtimesportsapi.com/apis/endpoints/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://www.realtimesportsapi.com/status
- group: company
  title: ''
  type: Newsroom
  url: https://www.realtimesportsapi.com/apis/endpoints/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.realtimesportsapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/realtimesportsapi-com/authentication/realtimesportsapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/realtimesportsapi-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/realtimesportsapi-com/security/realtimesportsapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/realtimesportsapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.realtimesportsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.realtimesportsapi.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.realtimesportsapi.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.realtimesportsapi.com/signup
- group: company
  title: ''
  type: Blog
  url: https://www.realtimesportsapi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.realtimesportsapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.realtimesportsapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.realtimesportsapi.com/privacy
created: '2026-10-31'
description: Realtime Sports API provides live sports data across major leagues including NBA, NFL, MLB, NHL, and soccer. It offers REST endpoints, WebSocket streams, and webhooks delivering scores, play‑by‑play, odds, and betting intel in near‑real‑time. Developers can access a free tier with 1,000 calls per month, no credit card required, and upgrade to paid plans for higher limits and advanced features. The service targets betting apps, fantasy platforms, and live scoreboards, emphasizing reliability, low latency, and comprehensive coverage of 29 leagues.
image: https://www.realtimesportsapi.com/og-image.png
json_schemas:
- name: Athlete
  property_count: 12
  slug: realtimesportsapi-com-athlete
- name: AvailabilityState
  property_count: 18
  slug: realtimesportsapi-com-availability-state
- name: Event
  property_count: 15
  slug: realtimesportsapi-com-event
- name: GameRoster
  property_count: 2
  slug: realtimesportsapi-com-game-roster
- name: Play
  property_count: 21
  slug: realtimesportsapi-com-play
- name: Team
  property_count: 18
  slug: realtimesportsapi-com-team
jsonld:
- class_count: 42
  name: Realtimesportsapi Com Context
  property_count: 170
  slug: realtimesportsapi-com-context
layout: provider
modified: '2026-10-31'
name: realtimesportsapi-com
nav: Providers
network: true
overview: 'realtimesportsapi-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Athletes API, Events API, Injuries & Availability API, and 9 more. Tagged areas include Company, Sports, API, Real-time, and Betting.


  The realtimesportsapi-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  realtimesportsapi-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
plans:
- name: Realtimesportsapi Com Plans Pricing
  plan_count: 5
  slug: realtimesportsapi-com-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: realtimesportsapi-com API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: realtimesportsapi-com-rules
scopes:
- name: Realtimesportsapi Com Scopes
  scope_count: 0
  slug: realtimesportsapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 70.1
    developer_ergonomics: 56.4
    discoverability: 67.9
    operational_transparency: 39.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Realtimesportsapi Com Authentication
  slug: realtimesportsapi-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Realtimesportsapi Com Domain Security
  slug: realtimesportsapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: realtimesportsapi-com-create-and-test-webhook
  slug: realtimesportsapi-com-create-and-test-webhook
slug: realtimesportsapi-com
tags:
- Company
- Sports
- API
- Real-time
- Betting
website: https://www.realtimesportsapi.com/
---
