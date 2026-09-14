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
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wager Api Agentic Access
  operation_count: 9
  slug: wager-api-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://api.wagerapi.com
  baseurl_source: declared
  description: Season and championship futures markets
  name: Wager API Futures API
  slug: wager-api-futures-api
- baseURL: https://api.wagerapi.com
  baseurl_source: declared
  description: Game schedules, results, and team information
  name: Wager API Games API
  slug: wager-api-games-api
- baseURL: https://api.wagerapi.com
  baseurl_source: declared
  description: Real-time game odds including spreads, moneylines, and totals
  name: Wager API Odds API
  slug: wager-api-odds-api
- baseURL: https://api.wagerapi.com
  baseurl_source: declared
  description: Player statistics, projections, and injury information
  name: Wager API Players API
  slug: wager-api-players-api
- baseURL: https://api.wagerapi.com
  baseurl_source: declared
  description: Player proposition odds
  name: Wager API Props API
  slug: wager-api-props-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wager Futures API
  slug: open-wager-api-futures-api
- collection_type: open
  name: Wager Futures Games API
  slug: open-wager-api-games-api
- collection_type: open
  name: Wager Futures Odds API
  slug: open-wager-api-odds-api
- collection_type: open
  name: Wager Futures Players API
  slug: open-wager-api-players-api
- collection_type: open
  name: Wager Futures Props API
  slug: open-wager-api-props-api
- collection_type: open
  name: Wager API
  slug: open-wager-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wager-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wager-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wager-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wagerapi.com/
- group: operate
  title: ''
  type: Contact
  url: https://wagerapi.com/#contact
created: '2025-02-08'
description: Wager API is a modern sports betting data platform that enables developers to build sports betting applications, bots, and predictive models with a single API. The platform provides real-time sports odds including spreads, moneylines, totals, player props, and futures markets across NFL, NCAA, NBA, MLB, NHL, soccer, tennis, and golf. Wager API also delivers player statistics, projections, fantasy data, injury reports, lineup updates, game schedules, and depth charts, making it a comprehensive data source for sports betting and fantasy sports applications.
examples:
- key_count: 2
  name: Wager Api Get Game Odds Example
  slug: wager-api-get-game-odds-example
- key_count: 2
  name: Wager Api Get Player Props Example
  slug: wager-api-get-player-props-example
finops:
- name: Wager Api Finops
  service_category: API
  slug: wager-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wager-api.png
json_schemas:
- name: Wager API Game Odds
  property_count: 8
  slug: wager-api-game-odds
json_structures:
- name: Wager Api Game Odds Structure
  property_count: 0
  slug: wager-api-game-odds-structure
jsonld:
- class_count: 34
  name: Wager Api Context
  property_count: 4
  slug: wager-api-context
layout: provider
modified: '2026-05-19'
name: Wager API
nav: Providers
network: true
overview: 'Wager API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Futures API, Games API, Odds API, and 2 more. Tagged areas include Sports Betting, Sports Odds, Fantasy Sports, Sports Data, and NFL.


  The Wager API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wager API''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Wager Api Plans Pricing
  plan_count: 3
  slug: wager-api-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Wager Api Rate Limits
  slug: wager-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Wager API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wager-api-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Wager API API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: wager-api-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/wager-api/refs/heads/main/screenshots/wager-api-2026-06-20T201159.png
security:
- kind: authentication
  name: Wager Api Authentication
  slug: wager-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wager Api Domain Security
  slug: wager-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: wager-api
tags:
- Sports Betting
- Sports Odds
- Fantasy Sports
- Sports Data
- NFL
- NBA
- MLB
- NHL
- NCAA
website: https://wagerapi.com/
---
