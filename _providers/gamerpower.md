---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gamerpower Agentic Access
  operation_count: 4
  slug: gamerpower-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Multi-value platform and type filtering using dot-separated values.
  name: GamerPower Filter API
  slug: gamerpower-filter-api
- description: List and look up live game giveaways, beta keys, DLC drops, and loot offers.
  name: GamerPower Giveaways API
  slug: gamerpower-giveaways-api
- description: Aggregate live giveaway counts and USD value estimation.
  name: GamerPower Worth API
  slug: gamerpower-worth-api
artifact_total: 24
collections:
- collection_type: open
  name: GamerPower API
  slug: open-gamerpower
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gamerpower-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gamerpower-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gamerpower.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.gamerpower.com/api-read
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: other
  title: RapidAPI Listing
  type: Marketplace
  url: https://rapidapi.com/digiwalls/api/gamerpower
- group: build
  title: Game_Grabber (Community Client)
  type: CodeExamples
  url: https://github.com/LuckyLuke00/Game_Grabber
- group: build
  title: api-gamerpower (HTML/JS Client)
  type: CodeExamples
  url: https://github.com/suvayan-m/api-gamerpower
- group: build
  title: gamehub (Flutter Client)
  type: CodeExamples
  url: https://github.com/AnggaPutraa/gamehub
created: '2026-05-28'
description: GamerPower is a free, no-authentication REST API that aggregates live game giveaways across PC, console, mobile, VR, and DRM-free platforms — tracking free games, beta keys, DLC drops, and in-game loot offers from Steam, Epic Games Store, GOG, Ubisoft Connect, EA Origin, itch.io, Battle.net, PlayStation, Xbox, Switch, Android, iOS, and VR storefronts. Multi-value platform/type filtering, date/value/popularity sorting, and aggregate USD worth estimation are exposed.
examples:
- key_count: 16
  name: Gamerpower Giveaway Example
  slug: gamerpower-giveaway-example
- key_count: 2
  name: Gamerpower Status Envelope Example
  slug: gamerpower-status-envelope-example
- key_count: 2
  name: Gamerpower Worth Estimation Example
  slug: gamerpower-worth-estimation-example
- key_count: 2
  name: Get Worth
  slug: get-worth
finops:
- name: Gamerpower Finops
  service_category: API
  slug: gamerpower-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gamerpower.png
json_schemas:
- name: GiveawayList
  property_count: 0
  slug: gamerpower-giveaway-list
- name: Giveaway
  property_count: 16
  slug: gamerpower-giveaway
- name: StatusEnvelope
  property_count: 2
  slug: gamerpower-status-envelope
- name: WorthEstimation
  property_count: 2
  slug: gamerpower-worth-estimation
json_structures:
- name: Gamerpower Giveaway Structure
  property_count: 16
  slug: gamerpower-giveaway-structure
- name: Gamerpower Status Envelope Structure
  property_count: 2
  slug: gamerpower-status-envelope-structure
- name: Gamerpower Worth Estimation Structure
  property_count: 2
  slug: gamerpower-worth-estimation-structure
jsonld:
- class_count: 13
  name: Gamerpower Context
  property_count: 9
  slug: gamerpower-context
- class_count: 0
  name: Gamerpower Context
  property_count: 0
  slug: gamerpower
layout: provider
modified: '2026-05-30'
name: GamerPower
nav: Providers
network: true
overview: 'GamerPower publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filter API, Giveaways API, and Worth API. Tagged areas include Games And Comics, Giveaways, Free Games, and Public APIs.


  The GamerPower catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  GamerPower''s developer surface includes documentation, code examples, and 7 more developer resources.'
plans:
- name: Gamerpower Plans Pricing
  plan_count: 2
  slug: gamerpower-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Gamerpower Rate Limits
  slug: gamerpower-rate-limits
rules:
- name: GamerPower API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gamerpower-jsonschema-spectral-rules
- name: GamerPower API Rules
  rule_count: 35
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 17
  slug: gamerpower-rules
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 28.0
    developer_ergonomics: 8.7
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gamerpower/refs/heads/main/screenshots/gamerpower-2026-06-20T181638.png
security:
- kind: domain-security
  name: Gamerpower Domain Security
  slug: gamerpower-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gamerpower
tags:
- Games And Comics
- Giveaways
- Free Games
- Public APIs
website: https://www.gamerpower.com
---
