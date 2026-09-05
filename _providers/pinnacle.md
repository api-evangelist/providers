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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Pinnacle Agentic Access
  operation_count: 18
  slug: pinnacle-agentic-access
  summary_line: 18 operations · 2 acting
api_count: 12
apis:
- description: Pinnacle is an online gaming website that was founded in 1998. Since its inception, Pinnacle has become a medium-sized, fully licensed, online sportsbook.
  name: Pinnacle Bets API
  slug: pinnacle-bets-api
- description: Pinnacle is an online gaming website that was founded in 1998. Since its inception, Pinnacle has become a medium-sized, fully licensed, online sportsbook.
  name: Pinnacle Lines API
  slug: pinnacle-lines-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Cancellationreasons API from Pinnacle Sports Betting — 1 operation(s) for cancellationreasons.
  name: ' Pinnacle Sports Betting Cancellationreasons API'
  slug: pinnacle-cancellationreasons-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Currencies API from Pinnacle Sports Betting — 1 operation(s) for currencies.
  name: ' Pinnacle Sports Betting Currencies API'
  slug: pinnacle-currencies-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Fixtures API from Pinnacle Sports Betting — 4 operation(s) for fixtures.
  name: ' Pinnacle Sports Betting Fixtures API'
  slug: pinnacle-fixtures-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Inrunning API from Pinnacle Sports Betting — 1 operation(s) for inrunning.
  name: ' Pinnacle Sports Betting Inrunning API'
  slug: pinnacle-inrunning-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Leagues API from Pinnacle Sports Betting — 1 operation(s) for leagues.
  name: ' Pinnacle Sports Betting Leagues API'
  slug: pinnacle-leagues-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Line API from Pinnacle Sports Betting — 4 operation(s) for line.
  name: ' Pinnacle Sports Betting Line API'
  slug: pinnacle-line-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Odds API from Pinnacle Sports Betting — 3 operation(s) for odds.
  name: ' Pinnacle Sports Betting Odds API'
  slug: pinnacle-odds-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Periods API from Pinnacle Sports Betting — 1 operation(s) for periods.
  name: ' Pinnacle Sports Betting Periods API'
  slug: pinnacle-periods-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Sports API from Pinnacle Sports Betting — 1 operation(s) for sports.
  name: ' Pinnacle Sports Betting Sports API'
  slug: pinnacle-sports-api
- baseURL: https://api.pinnacle.com
  baseurl_source: spec
  description: The Teaser API from Pinnacle Sports Betting — 1 operation(s) for teaser.
  name: ' Pinnacle Sports Betting Teaser API'
  slug: pinnacle-teaser-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pinnacle Lines API - Long-Poll Surface
  slug: open-pinnacle-asyncapi
- collection_type: open
  name: Pinnacle Lines Cancellationreasons API
  slug: open-pinnacle-cancellationreasons-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Currencies API
  slug: open-pinnacle-currencies-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Fixtures API
  slug: open-pinnacle-fixtures-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Inrunning API
  slug: open-pinnacle-inrunning-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Leagues API
  slug: open-pinnacle-leagues-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Line API
  slug: open-pinnacle-line-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Odds API
  slug: open-pinnacle-odds-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Periods API
  slug: open-pinnacle-periods-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Sports API
  slug: open-pinnacle-sports-api
- collection_type: open
  name: Pinnacle Lines Cancellationreasons Teaser API
  slug: open-pinnacle-teaser-api
- collection_type: open
  name: Pinnacle Lines API
  slug: open-pinnacle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinnacle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinnacle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinnacle-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinnacle-sports
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pinnacleapi
created: '2024-11-07T00:00:00.000Z'
description: Pinnacle is an online gaming website that was founded in 1998. Since its inception, Pinnacle has become a medium-sized, fully licensed, online sportsbook.
finops:
- name: Pinnacle Finops
  service_category: API
  slug: pinnacle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pinnacle.png
layout: provider
modified: '2026-05-30'
name: Pinnacle Sports Betting
nav: Providers
network: true
overview: 'Pinnacle Sports Betting publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Pinnacle Lines API, g Cancellationreasons API, g Currencies API, and 8 more. Tagged areas include Gambling and Sports Betting.


  Pinnacle Sports Betting''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Pinnacle Plans Pricing
  plan_count: 3
  slug: pinnacle-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Pinnacle Rate Limits
  slug: pinnacle-rate-limits
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 21.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 91.7
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinnacle/refs/heads/main/screenshots/pinnacle-2026-06-20T191716.png
security:
- kind: authentication
  name: Pinnacle Authentication
  slug: pinnacle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pinnacle Domain Security
  slug: pinnacle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pinnacle
tags:
- Gambling
- Sports Betting
---
