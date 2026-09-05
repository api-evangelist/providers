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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Entitysport Agentic Access
  operation_count: 15
  slug: entitysport-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
apis:
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Access token generation.
  name: Entity Sport Authentication API
  slug: entitysport-authentication-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Competitions, seasons, and standings.
  name: Entity Sport Competitions API
  slug: entitysport-competitions-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Fantasy points and squads.
  name: Entity Sport Fantasy API
  slug: entitysport-fantasy-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Match listing, info, and live scoring.
  name: Entity Sport Matches API
  slug: entitysport-matches-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Cricket Exchange live odds.
  name: Entity Sport Odds API
  slug: entitysport-odds-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Player profiles and statistics.
  name: Entity Sport Players API
  slug: entitysport-players-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Match scorecards and innings detail.
  name: Entity Sport Scorecards API
  slug: entitysport-scorecards-api
- baseURL: https://restapi.entitysport.com/v2
  baseurl_source: declared
  description: Team profiles and rosters.
  name: Entity Sport Teams API
  slug: entitysport-teams-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication API
  slug: open-entitysport-authentication-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Competitions API
  slug: open-entitysport-competitions-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Fantasy API
  slug: open-entitysport-fantasy-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Matches API
  slug: open-entitysport-matches-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Odds API
  slug: open-entitysport-odds-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Players API
  slug: open-entitysport-players-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Scorecards API
  slug: open-entitysport-scorecards-api
- collection_type: open
  name: Entity Sport Cricket API V2 Authentication Teams API
  slug: open-entitysport-teams-api
- collection_type: open
  name: Entity Sport Cricket API V2
  slug: open-entitysport
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/entitysport-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/entitysport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/entitysport-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/entitysport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/entitysport
- group: company
  title: ''
  type: Website
  url: https://www.entitysport.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.doc.entitysport.com
- group: commercial
  title: ''
  type: Plans
  url: plans/entitysport-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/entitysport-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/entitysport-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.entitysport.com/feed/
created: '2026-06-25'
description: Entity Sport (Entity Digital Sports) provides real-time sports data APIs, with cricket as its flagship product. The Cricket API V2 delivers competitions and seasons, fixtures and results, ball-by-ball live scoring, detailed scorecards, fantasy points, player and team profiles, standings, and betting odds over a token-authenticated REST interface.
finops:
- name: Entitysport Finops
  service_category: Sports Data and Analytics
  slug: entitysport-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/entitysport.png
layout: provider
modified: '2026-06-25'
name: Entity Sport
nav: Providers
network: true
overview: 'Entity Sport publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Competitions API, Fantasy API, and 5 more. Tagged areas include Sports Data, Cricket, Live Scores, Fantasy, and Odds.


  Entity Sport''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Entitysport Plans Pricing
  plan_count: 8
  slug: entitysport-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Entitysport Rate Limits
  slug: entitysport-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.4
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/entitysport/refs/heads/main/screenshots/entitysport-2026-07-25T213432.png
security:
- kind: authentication
  name: Entitysport Authentication
  slug: entitysport-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Entitysport Domain Security
  slug: entitysport-domain-security
  summary_line: TLSv1.3 · DMARC
slug: entitysport
tags:
- Sports Data
- Cricket
- Live Scores
- Fantasy
- Odds
website: https://www.entitysport.com
---
