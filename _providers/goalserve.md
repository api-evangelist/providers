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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Goalserve Agentic Access
  operation_count: 7
  slug: goalserve-agentic-access
  summary_line: 7 operations
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
random_paper: 2
rate_limits:
- limit_count: 5
  name: Goalserve Rate Limits
  slug: goalserve-rate-limits
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goalserve/refs/heads/main/screenshots/goalserve-2026-07-25T215959.png
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
