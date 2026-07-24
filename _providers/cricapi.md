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
  name: Cricapi Agentic Access
  operation_count: 11
  slug: cricapi-agentic-access
  summary_line: 11 operations
api_count: 6
apis:
- description: Fantasy cricket squad, scorecard, and points
  name: CricAPI Fantasy API
  slug: cricapi-fantasy-api
- description: Generic helper data (countries, flags)
  name: CricAPI Generic API
  slug: cricapi-generic-api
- description: Detailed info endpoints for series, matches, and players
  name: CricAPI Info API
  slug: cricapi-info-api
- description: All matches and current live matches
  name: CricAPI Matches API
  slug: cricapi-matches-api
- description: Player listing and search
  name: CricAPI Players API
  slug: cricapi-players-api
- description: Cricket series list and search
  name: CricAPI Series API
  slug: cricapi-series-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cricapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cricapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cricapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cricapi.com/
- group: company
  title: ''
  type: Website
  url: https://cricketdata.org/
- group: docs
  title: ''
  type: Documentation
  url: https://cricketdata.org/how-to-use-cricket-data-api.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://cricketdata.org/pricing/
- group: company
  title: ''
  type: Blog
  url: https://cricketdata.org/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/PpnXLf0Mpm
- group: other
  title: ''
  type: X
  url: https://twitter.com/cricapi
- group: operate
  title: ''
  type: Contact
  url: https://cricketdata.org/contact/
- group: operate
  title: ''
  type: Forums
  url: https://cricketdata.org/forum/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/plans/cricapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/rate-limits/cricapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/finops/cricapi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/json-ld/cricapi-context.jsonld
created: '2026-06-12'
description: CricAPI (now operating as CricketData.org) is a cricket data API platform that has provided free, high-performance cricket data since September 2015. The API delivers live scores, ball-by-ball updates, match details, player statistics, team rankings, schedules, and fantasy cricket scorecard data for international and domestic tournaments including ICC, IPL, T20, BBL, and PSL. Developers can access historical match data going back to 2000, widgets for website integration, and a fantasy cricket API designed for league operators. The platform is ISO 9001:2015 certified and uses its own AI engine with human data entry rather than scraping third-party sources.
examples:
- key_count: 3
  name: Cricapi Match Example
  slug: cricapi-match-example
- key_count: 3
  name: Cricapi Player Example
  slug: cricapi-player-example
- key_count: 3
  name: Cricapi Series Example
  slug: cricapi-series-example
finops:
- name: Cricapi Finops
  service_category: ''
  slug: cricapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cricapi.png
json_schemas:
- name: CricAPI Match
  property_count: 11
  slug: cricapi-match
- name: CricAPI Player
  property_count: 8
  slug: cricapi-player
- name: CricAPI Series
  property_count: 9
  slug: cricapi-series
jsonld:
- class_count: 35
  name: Cricapi Context
  property_count: 7
  slug: cricapi-context
layout: provider
modified: '2026-06-12'
name: CricAPI
nav: Providers
network: true
overview: 'CricAPI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Fantasy API, Generic API, Info API, and 3 more. Tagged areas include Cricket, Sports, Live Scores, Player Statistics, and Match Data.


  The CricAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CricAPI''s developer surface includes authentication, documentation, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Cricapi Plans Pricing
  plan_count: 5
  slug: cricapi-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Cricapi Rate Limits
  slug: cricapi-rate-limits
rules:
- name: CricAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cricapi-jsonschema-spectral-rules
score:
  band: developing
  composite: 58.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 77.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 47.4
  previous_composite: 58.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cricapi/refs/heads/main/screenshots/cricapi-2026-06-20T175236.png
security:
- kind: authentication
  name: Cricapi Authentication
  slug: cricapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cricapi Domain Security
  slug: cricapi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: cricapi
tags:
- Cricket
- Sports
- Live Scores
- Player Statistics
- Match Data
- Fantasy Cricket
- Ball-by-Ball
- Team Rankings
- Schedules
- Sports Data
website: https://www.cricapi.com/
---
