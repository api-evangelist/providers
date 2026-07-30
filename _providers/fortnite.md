---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Fortnite Agentic Access
  operation_count: 7
  slug: fortnite-agentic-access
  summary_line: 7 operations
api_count: 5
apis:
- description: Current Battle Pass weekly challenges.
  name: Fortnite Tracker Challenges API
  slug: fortnite-challenges-api
- description: Top-player leaderboards by platform and region.
  name: Fortnite Tracker Leaderboards API
  slug: fortnite-leaderboards-api
- description: Competitive Fortnite power rankings across professional events.
  name: Fortnite Tracker Power Rankings API
  slug: fortnite-power-rankings-api
- description: Per-player Fortnite lifetime and per-mode statistics.
  name: Fortnite Tracker Profile API
  slug: fortnite-profile-api
- description: Current Fortnite in-game store rotation.
  name: Fortnite Tracker Store API
  slug: fortnite-store-api
artifact_total: 44
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fortnite-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fortnite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fortnite-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://fortnitetracker.com/site-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TrackerNetwork
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tracker.gg/developers
- group: commercial
  title: ''
  type: Plans
  url: plans/fortnite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fortnite-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fortnite-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/fortnite-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/fortnite-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fortnite-tracker-context.jsonld
created: '2026-05-28'
description: Fortnite Tracker, by Tracker Network, exposes a small REST API surface (api.fortnitetracker.com/v1) covering player profile lifetime stats, regional leaderboards, competitive power rankings, the rotating in-game store, and the weekly challenges feed for Fortnite. Authentication is a single TRN-Api-Key header obtained from the Fortnite Tracker site. The service has reached a silent end-of-life in recent years (some endpoints are intermittently unavailable) but remains the canonical community profile of how Tracker Network packages Epic Games' Fortnite telemetry as a developer API.
examples:
- key_count: 8
  name: Fortnite Tracker Challenge Example
  slug: fortnite-tracker-challenge-example
- key_count: 6
  name: Fortnite Tracker Leaderboard Entry Example
  slug: fortnite-tracker-leaderboard-entry-example
- key_count: 14
  name: Fortnite Tracker Match Summary Example
  slug: fortnite-tracker-match-summary-example
- key_count: 8
  name: Fortnite Tracker Player Profile Example
  slug: fortnite-tracker-player-profile-example
- key_count: 9
  name: Fortnite Tracker Power Ranking Detail Example
  slug: fortnite-tracker-power-ranking-detail-example
- key_count: 8
  name: Fortnite Tracker Power Ranking Entry Example
  slug: fortnite-tracker-power-ranking-entry-example
- key_count: 11
  name: Fortnite Tracker Stat Block Example
  slug: fortnite-tracker-stat-block-example
- key_count: 2
  name: Fortnite Tracker Stat Line Example
  slug: fortnite-tracker-stat-line-example
- key_count: 8
  name: Fortnite Tracker Stat Value Example
  slug: fortnite-tracker-stat-value-example
- key_count: 6
  name: Fortnite Tracker Store Item Example
  slug: fortnite-tracker-store-item-example
finops:
- name: Fortnite Finops
  service_category: Games And Comics
  slug: fortnite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fortnite.png
json_schemas:
- name: Challenge
  property_count: 8
  slug: fortnite-tracker-challenge
- name: LeaderboardEntry
  property_count: 6
  slug: fortnite-tracker-leaderboard-entry
- name: MatchSummary
  property_count: 14
  slug: fortnite-tracker-match-summary
- name: PlayerProfile
  property_count: 8
  slug: fortnite-tracker-player-profile
- name: PowerRankingDetail
  property_count: 0
  slug: fortnite-tracker-power-ranking-detail
- name: PowerRankingEntry
  property_count: 8
  slug: fortnite-tracker-power-ranking-entry
- name: StatBlock
  property_count: 11
  slug: fortnite-tracker-stat-block
- name: StatLine
  property_count: 2
  slug: fortnite-tracker-stat-line
- name: StatValue
  property_count: 8
  slug: fortnite-tracker-stat-value
- name: StoreItem
  property_count: 6
  slug: fortnite-tracker-store-item
json_structures:
- name: Fortnite Tracker Challenge Structure
  property_count: 8
  slug: fortnite-tracker-challenge-structure
- name: Fortnite Tracker Leaderboard Entry Structure
  property_count: 6
  slug: fortnite-tracker-leaderboard-entry-structure
- name: Fortnite Tracker Match Summary Structure
  property_count: 14
  slug: fortnite-tracker-match-summary-structure
- name: Fortnite Tracker Player Profile Structure
  property_count: 8
  slug: fortnite-tracker-player-profile-structure
- name: Fortnite Tracker Power Ranking Detail Structure
  property_count: 0
  slug: fortnite-tracker-power-ranking-detail-structure
- name: Fortnite Tracker Power Ranking Entry Structure
  property_count: 8
  slug: fortnite-tracker-power-ranking-entry-structure
- name: Fortnite Tracker Stat Block Structure
  property_count: 11
  slug: fortnite-tracker-stat-block-structure
- name: Fortnite Tracker Stat Line Structure
  property_count: 2
  slug: fortnite-tracker-stat-line-structure
- name: Fortnite Tracker Stat Value Structure
  property_count: 8
  slug: fortnite-tracker-stat-value-structure
- name: Fortnite Tracker Store Item Structure
  property_count: 6
  slug: fortnite-tracker-store-item-structure
jsonld:
- class_count: 9
  name: Fortnite Tracker Context
  property_count: 56
  slug: fortnite-tracker-context
layout: provider
modified: '2026-05-30'
name: Fortnite Tracker
nav: Providers
network: true
overview: 'Fortnite Tracker publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Challenges API, Leaderboards API, Power Rankings API, and 2 more. Tagged areas include Games And Comics, Public APIs, Fortnite, Player Statistics, and Esports.


  The Fortnite Tracker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Fortnite Tracker''s developer surface includes authentication and 12 more developer resources.'
plans:
- name: Fortnite Plans Pricing
  plan_count: 2
  slug: fortnite-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Fortnite Rate Limits
  slug: fortnite-rate-limits
rules:
- name: Fortnite Tracker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fortnite-jsonschema-spectral-rules
- name: Fortnite Tracker API Rules
  rule_count: 48
  severity_counts:
    error: 20
    hint: 0
    info: 4
    warn: 24
  slug: fortnite-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: -6.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Fortnite Authentication
  slug: fortnite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fortnite Domain Security
  slug: fortnite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fortnite
tags:
- Games And Comics
- Public APIs
- Fortnite
- Player Statistics
- Esports
- Tracker Network
website: https://fortnitetracker.com/site-api
---
