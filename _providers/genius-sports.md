---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 66
  human_in_the_loop: 0
  name: Genius Sports Agentic Access
  operation_count: 227
  slug: genius-sports-agentic-access
  summary_line: 227 operations · 66 acting
api_count: 31
apis:
- description: Query information regarding matches, players, statistics etc. both past and future. Covers basketball, 3x3, football (soccer), volleyball, American football, and ice hockey.
  name: Genius Sports REST API
  slug: rest-api
- description: Delivers event-by-event data and aggregated statistics for matches in progress, supporting live consumption of sporting event data.
  name: Genius Sports Streaming API
  slug: streaming-api
- description: Enables publishing of real-time event data from sporting events into the Genius Sports warehouse and statistics engine.
  name: Genius Sports Publish API
  slug: publish-api
- description: Live venue data delivered for TV production and consumers covering basketball, football (soccer), and volleyball.
  name: Genius Sports LiveStats In-Arena Feed
  slug: livestats-in-arena-feed
- description: Retrieves matches and options from the Genius Sports licensing server.
  name: Genius Sports Licensing API
  slug: licensing-api
- description: The Competitions API from Genius Sports — 2 operation(s) for competitions.
  name: Genius Sports Competitions API
  slug: genius-sports-competitions-api
- description: The Competitors API from Genius Sports — 21 operation(s) for competitors.
  name: Genius Sports Competitors API
  slug: genius-sports-competitors-api
- description: Groups the operations related to competitors of type Double partnership. When creating a double partnership the competitors must be of the same sport, and the sport should allow creation of double par
  name: Genius Sports competitors/doubles API
  slug: genius-sports-competitors-doubles-api
- description: Groups the operations related to competitors of type Horse
  name: Genius Sports competitors/horses API
  slug: genius-sports-competitors-horses-api
- description: Groups the operations related to competitors of type Player
  name: Genius Sports competitors/players API
  slug: genius-sports-competitors-players-api
- description: Groups the operations related to to-be-determined competitors.
  name: Genius Sports competitors/tbds API
  slug: genius-sports-competitors-tbds-api
- description: Groups the operations related to competitors of type Team
  name: Genius Sports competitors/teams API
  slug: genius-sports-competitors-teams-api
- description: The Contracts API from Genius Sports — 10 operation(s) for contracts.
  name: Genius Sports Contracts API
  slug: genius-sports-contracts-api
- description: The Fixtures API from Genius Sports — 7 operation(s) for fixtures.
  name: Genius Sports Fixtures API
  slug: genius-sports-fixtures-api
- description: The Groups API from Genius Sports — 2 operation(s) for groups.
  name: Genius Sports Groups API
  slug: genius-sports-groups-api
- description: The Ingestion API from Genius Sports — 12 operation(s) for ingestion.
  name: Genius Sports Ingestion API
  slug: genius-sports-ingestion-api
- description: The Localities API from Genius Sports — 2 operation(s) for localities.
  name: Genius Sports Localities API
  slug: genius-sports-localities-api
- description: Match data and broadcasts
  name: Genius Sports Matches API
  slug: genius-sports-matches-api
- description: Leagues, competitions, clubs, teams
  name: Genius Sports Organization API
  slug: genius-sports-organization-api
- description: The Organizations API from Genius Sports — 2 operation(s) for organizations.
  name: Genius Sports Organizations API
  slug: genius-sports-organizations-api
- description: The Pending requests API from Genius Sports — 1 operation(s) for pending requests.
  name: Genius Sports Pending requests API
  slug: genius-sports-pending-requests-api
- description: Players, officials, staff
  name: Genius Sports People API
  slug: genius-sports-people-api
- description: The Persons API from Genius Sports — 5 operation(s) for persons.
  name: Genius Sports Persons API
  slug: genius-sports-persons-api
- description: The results from the this kind of matching are always probabilistic. However we consider matches that have above 90% match score as viable results.
  name: Genius Sports Probabilistic matching API
  slug: genius-sports-probabilistic-matching-api
- description: The Rounds API from Genius Sports — 5 operation(s) for rounds.
  name: Genius Sports Rounds API
  slug: genius-sports-rounds-api
- description: The Seasons API from Genius Sports — 4 operation(s) for seasons.
  name: Genius Sports Seasons API
  slug: genius-sports-seasons-api
- description: The Sourcerequests API from Genius Sports — 1 operation(s) for sourcerequests.
  name: Genius Sports Sourcerequests API
  slug: genius-sports-sourcerequests-api
- description: The Sports API from Genius Sports — 2 operation(s) for sports.
  name: Genius Sports Sports API
  slug: genius-sports-sports-api
- description: Competition standings
  name: Genius Sports Standings API
  slug: genius-sports-standings-api
- description: Team and player statistics
  name: Genius Sports Statistics API
  slug: genius-sports-statistics-api
- description: The Venues API from Genius Sports — 3 operation(s) for venues.
  name: Genius Sports Venues API
  slug: genius-sports-venues-api
artifact_total: 40
collections:
- collection_type: open
  name: Fixtures-v2
  slug: open-genius-sports-fixtures-v2
- collection_type: open
  name: fixtures-matching-v2
  slug: open-genius-sports-matching-v2
- collection_type: open
  name: Genius Sports Data Warehouse REST API
  slug: open-genius-sports
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/genius-sports-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/genius-sports-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/genius-sports-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geniussportsgroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/geniussports
- group: company
  title: ''
  type: Website
  url: https://geniussports.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.geniussports.com/
created: '2025-03-01'
description: Genius Sports provides APIs to query information regarding matches, players, statistics etc. both past and future across multiple sports including basketball, football (soccer), volleyball, American football, and ice hockey.
finops:
- name: Genius Sports Finops
  service_category: API
  slug: genius-sports-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genius-sports.png
layout: provider
modified: '2026-05-30'
name: Genius Sports
nav: Providers
network: true
overview: 'Genius Sports publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Competitions API, Competitors API, competitors/doubles API, and 23 more. Tagged areas include Sports, Statistics, Live Data, and Fixtures.


  Genius Sports'' developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: Genius Sports Plans Pricing
  plan_count: 3
  slug: genius-sports-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Genius Sports Rate Limits
  slug: genius-sports-rate-limits
score:
  band: thin
  composite: 30.2
  delta: -3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 19.6
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/genius-sports/refs/heads/main/screenshots/genius-sports-2026-06-20T181734.png
security:
- kind: authentication
  name: Genius Sports Authentication
  slug: genius-sports-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Genius Sports Domain Security
  slug: genius-sports-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: genius-sports
tags:
- Sports
- Statistics
- Live Data
- Fixtures
website: https://geniussports.com/
---
