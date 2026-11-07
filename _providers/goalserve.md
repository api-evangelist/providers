---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Goalserve Agentic Access
  operation_count: 7
  slug: goalserve-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Commentaries API from GoalServe — 1 operation(s) for commentaries.
  name: GoalServe Commentaries API
  slug: goalserve-commentaries-api
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Fixtures API from GoalServe — 1 operation(s) for fixtures.
  name: GoalServe Fixtures API
  slug: goalserve-fixtures-api
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Player Data API from GoalServe — 1 operation(s) for player data.
  name: GoalServe Player Data API
  slug: goalserve-player-data-api
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Standings API from GoalServe — 1 operation(s) for standings.
  name: GoalServe Standings API
  slug: goalserve-standings-api
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Team Data API from GoalServe — 1 operation(s) for team data.
  name: GoalServe Team Data API
  slug: goalserve-team-data-api
- baseURL: https://www.goalserve.com/getfeed
  baseurl_source: declared
  description: The Livescores API from GoalServe — 2 operation(s) for livescores.
  name: GoalServe Livescores API
  slug: goalserve-livescores-api
artifact_total: 20
collections:
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries API
  slug: open-goalserve-commentaries-api
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries Fixtures API
  slug: open-goalserve-fixtures-api
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries Live Scores API
  slug: open-goalserve-live-scores-api
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries Player Data API
  slug: open-goalserve-player-data-api
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries Standings API
  slug: open-goalserve-standings-api
- collection_type: open
  name: GoalServe Sports Data Feeds Commentaries Team Data API
  slug: open-goalserve-team-data-api
- collection_type: open
  name: GoalServe Sports Data Feeds API
  slug: open-goalserve
common:
- group: company
  title: ''
  type: Blog
  url: https://www.goalserve.com/en/blog
- group: agent
  href: https://artifacts.apis.io/goalserve/agentic-access/goalserve-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/goalserve-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/goalserve/security/goalserve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goalserve-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/goalserve/authentication/goalserve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goalserve-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goalserve-api
- group: company
  title: ''
  type: Website
  url: https://www.goalserve.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.goalserve.com/v1/
- group: commercial
  href: https://artifacts.apis.io/goalserve/plans/goalserve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goalserve-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/goalserve/rate-limits/goalserve-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/goalserve-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/goalserve/finops/goalserve-finops.yml
  title: ''
  type: FinOps
  url: finops/goalserve-finops.yml
created: '2026-06-25'
description: GoalServe is a live sports data feeds provider founded in 2005, delivering live scores, fixtures, standings, odds, commentaries, and team/player data across 20+ sports and 500+ soccer leagues. Feeds are served as XML or JSON over HTTP GET with a unique API access key carried in the request path.
finops:
- has_sources: true
  method: generated
  name: Goalserve Finops
  primary_unit: ''
  service_category: Analytics and Data
  slug: goalserve-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goalserve.png
layout: provider
modified: '2026-10-06'
name: GoalServe
nav: Providers
network: true
overview: 'GoalServe publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Commentaries API, Fixtures API, Player Data API, and 3 more. Tagged areas include Sports Data, Live Scores, Odds, Fixtures, and Soccer.


  The GoalServe catalog on APIs.io includes 1 Spectral governance ruleset.


  GoalServe''s developer surface includes engineering blog, authentication, documentation, and 7 more developer resources.'
plans:
- name: Goalserve Plans Pricing
  plan_count: 4
  slug: goalserve-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Goalserve Rate Limits
  slug: goalserve-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: GoalServe API Rules
  rule_count: 58
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 1
  slug: goalserve-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 47.8
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/goalserve/goalserve-2026-07-25T215959.png
security:
- kind: authentication
  name: Goalserve Authentication
  slug: goalserve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Goalserve Domain Security
  slug: goalserve-domain-security
  summary_line: TLSv1.2 · HSTS
slug: goalserve
tags:
- Sports Data
- Live Scores
- Odds
- Fixtures
- Soccer
website: https://www.goalserve.com
---
