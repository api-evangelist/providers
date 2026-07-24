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
  trial: true
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
  name: Goalserve Agentic Access
  operation_count: 7
  slug: goalserve-agentic-access
  summary_line: 7 operations
api_count: 6
apis:
- description: The Commentaries API from GoalServe — 1 operation(s) for commentaries.
  name: GoalServe Commentaries API
  slug: goalserve-commentaries-api
- description: The Fixtures API from GoalServe — 1 operation(s) for fixtures.
  name: GoalServe Fixtures API
  slug: goalserve-fixtures-api
- description: The Live Scores API from GoalServe — 2 operation(s) for live scores.
  name: GoalServe Live Scores API
  slug: goalserve-live-scores-api
- description: The Player Data API from GoalServe — 1 operation(s) for player data.
  name: GoalServe Player Data API
  slug: goalserve-player-data-api
- description: The Standings API from GoalServe — 1 operation(s) for standings.
  name: GoalServe Standings API
  slug: goalserve-standings-api
- description: The Team Data API from GoalServe — 1 operation(s) for team data.
  name: GoalServe Team Data API
  slug: goalserve-team-data-api
artifact_total: 13
collections:
- collection_type: open
  name: GoalServe Sports Data Feeds API
  slug: open-goalserve
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goalserve-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goalserve-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/goalserve-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goalserve-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/goalserve-finops.yml
created: '2026-06-25'
description: GoalServe is a live sports data feeds provider founded in 2005, delivering live scores, fixtures, standings, odds, commentaries, and team/player data across 20+ sports and 500+ soccer leagues. Feeds are served as XML or JSON over HTTP GET with a unique API access key carried in the request path.
finops:
- name: Goalserve Finops
  service_category: Analytics and Data
  slug: goalserve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goalserve.png
layout: provider
modified: '2026-06-25'
name: GoalServe
nav: Providers
network: true
overview: 'GoalServe publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Commentaries API, Fixtures API, Live Scores API, and 3 more. Tagged areas include Sports Data, Live Scores, Odds, Fixtures, and Soccer.


  GoalServe''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Goalserve Plans Pricing
  plan_count: 4
  slug: goalserve-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Goalserve Rate Limits
  slug: goalserve-rate-limits
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
