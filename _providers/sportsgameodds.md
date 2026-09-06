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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sportsgameodds Agentic Access
  operation_count: 11
  slug: sportsgameodds-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Account API from SportsGameOdds — 1 operation(s) for account.
  name: SportsGameOdds Account API
  slug: sportsgameodds-account-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Events API from SportsGameOdds — 2 operation(s) for events.
  name: SportsGameOdds Events API
  slug: sportsgameodds-events-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Leagues API from SportsGameOdds — 1 operation(s) for leagues.
  name: SportsGameOdds Leagues API
  slug: sportsgameodds-leagues-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Markets API from SportsGameOdds — 1 operation(s) for markets.
  name: SportsGameOdds Markets API
  slug: sportsgameodds-markets-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Players API from SportsGameOdds — 2 operation(s) for players.
  name: SportsGameOdds Players API
  slug: sportsgameodds-players-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Sports API from SportsGameOdds — 1 operation(s) for sports.
  name: SportsGameOdds Sports API
  slug: sportsgameodds-sports-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Stats API from SportsGameOdds — 1 operation(s) for stats.
  name: SportsGameOdds Stats API
  slug: sportsgameodds-stats-api
- baseURL: https://api.sportsgameodds.com/v1
  baseurl_source: declared
  description: The Teams API from SportsGameOdds — 2 operation(s) for teams.
  name: SportsGameOdds Teams API
  slug: sportsgameodds-teams-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SportsGameOdds Account API
  slug: open-sportsgameodds-account-api
- collection_type: open
  name: SportsGameOdds Account Events API
  slug: open-sportsgameodds-events-api
- collection_type: open
  name: SportsGameOdds Account Leagues API
  slug: open-sportsgameodds-leagues-api
- collection_type: open
  name: SportsGameOdds Account Markets API
  slug: open-sportsgameodds-markets-api
- collection_type: open
  name: SportsGameOdds Account Players API
  slug: open-sportsgameodds-players-api
- collection_type: open
  name: SportsGameOdds Account Sports API
  slug: open-sportsgameodds-sports-api
- collection_type: open
  name: SportsGameOdds Account Stats API
  slug: open-sportsgameodds-stats-api
- collection_type: open
  name: SportsGameOdds Account Teams API
  slug: open-sportsgameodds-teams-api
- collection_type: open
  name: SportsGameOdds API
  slug: open-sportsgameodds
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportsgameodds-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportsgameodds-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportsgameodds-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sportsgameodds.com/
- group: start
  title: ''
  type: Portal
  url: https://sportsgameodds.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://sportsgameodds.com/docs/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://sportsgameodds.com/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/SportsGameOdds
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SportsGameOdds/sports-odds-api-ruby
- group: agent
  title: ''
  type: LlmsText
  url: https://sportsgameodds.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://sportsgameodds.com/blog
created: '2025-02-08'
description: SportsGameOdds API provides real-time sports betting odds data from 80+ sportsbooks across 50+ leagues. The API delivers live and pre-match odds across 3,000+ markets including moneylines, spreads, over/unders, team props, and player props for NFL, NBA, MLB, NHL, NCAAF, NCAAB, EPL, UCL, UFC, PGA, ATP and more. Features include consensus odds calculations, streaming for live data, an interactive data explorer, and official SDKs for JavaScript/TypeScript and Python.
examples:
- key_count: 4
  name: Sportsgameodds List Events Example
  slug: sportsgameodds-list-events-example
- key_count: 4
  name: Sportsgameodds List Markets Example
  slug: sportsgameodds-list-markets-example
finops:
- name: Sportsgameodds Finops
  service_category: API
  slug: sportsgameodds-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportsgameodds.png
json_schemas:
- name: SportsGameOdds Event
  property_count: 8
  slug: sportsgameodds-event
- name: SportsGameOdds Market
  property_count: 7
  slug: sportsgameodds-market
json_structures:
- name: Sportsgameodds Event Structure
  property_count: 0
  slug: sportsgameodds-event-structure
jsonld:
- class_count: 36
  name: Sportsgameodds Context
  property_count: 5
  slug: sportsgameodds-context
layout: provider
modified: '2026-05-19'
name: SportsGameOdds
nav: Providers
network: true
overview: 'SportsGameOdds publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Events API, Leagues API, and 5 more. Tagged areas include Sports Betting, Odds, Sports Data, Fantasy Sports, and Gambling.


  The SportsGameOdds catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SportsGameOdds'' developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Sportsgameodds Plans Pricing
  plan_count: 3
  slug: sportsgameodds-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Sportsgameodds Rate Limits
  slug: sportsgameodds-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SportsGameOdds API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sportsgameodds-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: SportsGameOdds API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: sportsgameodds-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 61.2
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportsgameodds/refs/heads/main/screenshots/sportsgameodds-2026-06-20T194349.png
security:
- kind: authentication
  name: Sportsgameodds Authentication
  slug: sportsgameodds-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sportsgameodds Domain Security
  slug: sportsgameodds-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportsgameodds
tags:
- Sports Betting
- Odds
- Sports Data
- Fantasy Sports
- Gambling
website: https://sportsgameodds.com/
---
