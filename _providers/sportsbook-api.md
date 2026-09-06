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
  name: Sportsbook Api Agentic Access
  operation_count: 7
  slug: sportsbook-api-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://api.sportsbookapi.com
  baseurl_source: declared
  description: The Betting Analysis API from Sportsbook API — 3 operation(s) for betting analysis.
  name: Sportsbook API Betting Analysis API
  slug: sportsbook-api-betting-analysis-api
- baseURL: https://api.sportsbookapi.com
  baseurl_source: declared
  description: The Odds API from Sportsbook API — 2 operation(s) for odds.
  name: Sportsbook API Odds API
  slug: sportsbook-api-odds-api
- baseURL: https://api.sportsbookapi.com
  baseurl_source: declared
  description: The Reference API from Sportsbook API — 2 operation(s) for reference.
  name: Sportsbook API Reference API
  slug: sportsbook-api-reference-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sportsbook Betting Analysis API
  slug: open-sportsbook-api-betting-analysis-api
- collection_type: open
  name: Sportsbook Betting Analysis Odds API
  slug: open-sportsbook-api-odds-api
- collection_type: open
  name: Sportsbook Betting Analysis Reference API
  slug: open-sportsbook-api-reference-api
- collection_type: open
  name: Sportsbook API
  slug: open-sportsbook-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportsbook-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportsbook-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportsbook-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sportsbookapi.com/
- group: start
  title: ''
  type: Portal
  url: https://sportsbookapi.com/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://sportsbookapi.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://sportsbookapi.com/feed/
created: '2026-03-16'
description: Sportsbook API provides real-time sports betting odds data from major US sportsbooks including FanDuel, DraftKings, BetMGM, Kalshi, theScore, Fanatics, BetRivers, Polymarket, Bovada, and BetOnline. The API aggregates spreads, moneylines, totals, halves, quarters, player props, and futures for NFL, NBA, MLB, NHL, NCAA football, NCAA basketball, and soccer leagues. Includes tools to identify positive expected value (+EV) bets, arbitrage opportunities, and middling situations. Odds update once per minute, with live odds available during games.
examples:
- key_count: 4
  name: Sportsbook Api Get Arbitrage Example
  slug: sportsbook-api-get-arbitrage-example
- key_count: 4
  name: Sportsbook Api Get Odds Example
  slug: sportsbook-api-get-odds-example
finops:
- name: Sportsbook Api Finops
  service_category: API
  slug: sportsbook-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportsbook-api.png
json_schemas:
- name: Sportsbook API Arbitrage Opportunity
  property_count: 14
  slug: sportsbook-api-arbitrage
- name: Sportsbook API Odds Response
  property_count: 3
  slug: sportsbook-api-odds
json_structures:
- name: Sportsbook Api Odds Structure
  property_count: 0
  slug: sportsbook-api-odds-structure
jsonld:
- class_count: 29
  name: Sportsbook Api Context
  property_count: 5
  slug: sportsbook-api-context
layout: provider
modified: '2026-05-19'
name: Sportsbook API
nav: Providers
network: true
overview: 'Sportsbook API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Betting Analysis API, Odds API, and Reference API. Tagged areas include Sports Betting, Odds, Sports Data, and Gambling.


  The Sportsbook API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sportsbook API''s developer surface includes authentication, developer portal, pricing, engineering blog, and 3 more developer resources.'
plans:
- name: Sportsbook Api Plans Pricing
  plan_count: 3
  slug: sportsbook-api-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Sportsbook Api Rate Limits
  slug: sportsbook-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sportsbook API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sportsbook-api-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Sportsbook API API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: sportsbook-api-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 53.5
    catalog_earned_first_party: 0.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 60.8
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportsbook-api/refs/heads/main/screenshots/sportsbook-api-2026-06-20T194345.png
security:
- kind: authentication
  name: Sportsbook Api Authentication
  slug: sportsbook-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sportsbook Api Domain Security
  slug: sportsbook-api-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: sportsbook-api
tags:
- Sports Betting
- Odds
- Sports Data
- Gambling
website: https://sportsbookapi.com/
---
