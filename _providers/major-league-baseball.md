---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Major League Baseball Agentic Access
  operation_count: 186
  slug: major-league-baseball-agentic-access
  summary_line: 186 operations · 8 acting
api_count: 1
apis:
- description: The MLB Stats API is the modern statistics and game-data service operated by Major League Baseball. It powers official scoreboards, gameday feeds, and downstream applications with endpoints for schedu
  name: MLB Stats API
  slug: mlb-stats-api
- description: The MLB Data Lookup Service is the legacy public data service exposing player search and details, hitting and pitching statistics, projections, team lists and rosters, game type information, date rang
  name: MLB Data Lookup Service API
  slug: mlb-data-lookup-service
- description: Baseball Savant is MLB's public Statcast platform, surfacing pitch- and tracking-level data captured by Statcast cameras and radar in every MLB ballpark. It exposes leaderboards, search tools, visuali
  name: MLB Statcast (Baseball Savant)
  slug: mlb-statcast-baseball-savant
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to field tracking and analytics.
  name: Major League Baseball Analytics API
  slug: major-league-baseball-analytics-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The attendance endpoints handle game and season attendance and openings numbers by team.
  name: Major League Baseball Attendance API
  slug: major-league-baseball-attendance-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The awards endpoints allow users to lookup award information and recipients.
  name: Major League Baseball Awards API
  slug: major-league-baseball-awards-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to bat tracking data
  name: Major League Baseball Bat Tracking API
  slug: major-league-baseball-bat-tracking-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to biomechanical data
  name: Major League Baseball Biomechanics API
  slug: major-league-baseball-biomechanics-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The broadcast endpoints return information pertaining to broadcasters.
  name: Major League Baseball Broadcast API
  slug: major-league-baseball-broadcast-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The conference endpoint returns data specific to the PCL (Pacific Coast League) which was historically divided into separate conferences.
  name: Major League Baseball Conference API
  slug: major-league-baseball-conference-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Config elements
  name: Major League Baseball Config API
  slug: major-league-baseball-config-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to divisions
  name: Major League Baseball Division API
  slug: major-league-baseball-division-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to MLB BaseballDraft
  name: Major League Baseball Draft API
  slug: major-league-baseball-draft-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to games
  name: Major League Baseball Game API
  slug: major-league-baseball-game-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The Game Pace API from Major League Baseball — 1 operation(s) for game pace.
  name: Major League Baseball Game Pace API
  slug: major-league-baseball-game-pace-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to high/low stats
  name: Major League Baseball High/Low API
  slug: major-league-baseball-high-low-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to home run derby
  name: Major League Baseball Homerun Derby API
  slug: major-league-baseball-homerun-derby-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to jobs
  name: Major League Baseball Job API
  slug: major-league-baseball-job-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to leagues
  name: Major League Baseball League API
  slug: major-league-baseball-league-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to milestones
  name: Major League Baseball Milestones API
  slug: major-league-baseball-milestones-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to players
  name: Major League Baseball Person API
  slug: major-league-baseball-person-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The Predictions API from Major League Baseball — 2 operation(s) for predictions.
  name: Major League Baseball Predictions API
  slug: major-league-baseball-predictions-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The Reviews API from Major League Baseball — 1 operation(s) for reviews.
  name: Major League Baseball Reviews API
  slug: major-league-baseball-reviews-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to schedules
  name: Major League Baseball Schedule API
  slug: major-league-baseball-schedule-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to seasons
  name: Major League Baseball Season API
  slug: major-league-baseball-season-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to skeletal data
  name: Major League Baseball Skeletal API
  slug: major-league-baseball-skeletal-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to sports
  name: Major League Baseball Sports API
  slug: major-league-baseball-sports-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to teams
  name: Major League Baseball Standings API
  slug: major-league-baseball-standings-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to stats
  name: Major League Baseball Stats API
  slug: major-league-baseball-stats-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Endpoints for stats streaks
  name: Major League Baseball Streaks API
  slug: major-league-baseball-streaks-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to teams
  name: Major League Baseball Teams API
  slug: major-league-baseball-teams-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to transactions
  name: Major League Baseball Transactions API
  slug: major-league-baseball-transactions-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: Operations pertaining to venues
  name: Major League Baseball Venues API
  slug: major-league-baseball-venues-api
- baseURL: https://statsapi.mlb.com
  baseurl_source: spec
  description: The Weather API from Major League Baseball — 4 operation(s) for weather.
  name: Major League Baseball Weather API
  slug: major-league-baseball-weather-api
artifact_total: 69
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stats API Documentation Analytics API
  slug: open-major-league-baseball-analytics-api
- collection_type: open
  name: Stats API Documentation Analytics Attendance API
  slug: open-major-league-baseball-attendance-api
- collection_type: open
  name: Stats API Documentation Analytics Awards API
  slug: open-major-league-baseball-awards-api
- collection_type: open
  name: Stats API Documentation Analytics Bat Tracking API
  slug: open-major-league-baseball-bat-tracking-api
- collection_type: open
  name: Stats API Documentation Analytics Biomechanics API
  slug: open-major-league-baseball-biomechanics-api
- collection_type: open
  name: Stats API Documentation Analytics Broadcast API
  slug: open-major-league-baseball-broadcast-api
- collection_type: open
  name: Stats API Documentation Analytics Conference API
  slug: open-major-league-baseball-conference-api
- collection_type: open
  name: Stats API Documentation Analytics Config API
  slug: open-major-league-baseball-config-api
- collection_type: open
  name: Stats API Documentation Analytics Division API
  slug: open-major-league-baseball-division-api
- collection_type: open
  name: Stats API Documentation Analytics Draft API
  slug: open-major-league-baseball-draft-api
- collection_type: open
  name: Stats API Documentation Analytics Game API
  slug: open-major-league-baseball-game-api
- collection_type: open
  name: Stats API Documentation Analytics Game Pace API
  slug: open-major-league-baseball-game-pace-api
- collection_type: open
  name: Stats API Documentation Analytics High/Low API
  slug: open-major-league-baseball-high-low-api
- collection_type: open
  name: Stats API Documentation Analytics Homerun Derby API
  slug: open-major-league-baseball-homerun-derby-api
- collection_type: open
  name: Stats API Documentation Analytics Job API
  slug: open-major-league-baseball-job-api
- collection_type: open
  name: Stats API Documentation Analytics League API
  slug: open-major-league-baseball-league-api
- collection_type: open
  name: Stats API Documentation Analytics Milestones API
  slug: open-major-league-baseball-milestones-api
- collection_type: open
  name: Stats API Documentation Analytics Person API
  slug: open-major-league-baseball-person-api
- collection_type: open
  name: Stats API Documentation Analytics Predictions API
  slug: open-major-league-baseball-predictions-api
- collection_type: open
  name: Stats API Documentation Analytics Schedule API
  slug: open-major-league-baseball-schedule-api
- collection_type: open
  name: Stats API Documentation Analytics Season API
  slug: open-major-league-baseball-season-api
- collection_type: open
  name: Stats API Documentation Analytics Skeletal API
  slug: open-major-league-baseball-skeletal-api
- collection_type: open
  name: Stats API Documentation Analytics Sports API
  slug: open-major-league-baseball-sports-api
- collection_type: open
  name: Stats API Documentation Analytics Standings API
  slug: open-major-league-baseball-standings-api
- collection_type: open
  name: API Documentation Analytics Stats API
  slug: open-major-league-baseball-stats-api
- collection_type: open
  name: Stats API Documentation Analytics Streaks API
  slug: open-major-league-baseball-streaks-api
- collection_type: open
  name: Stats API Documentation Analytics Teams API
  slug: open-major-league-baseball-teams-api
- collection_type: open
  name: Stats API Documentation Analytics Transactions API
  slug: open-major-league-baseball-transactions-api
- collection_type: open
  name: Stats API Documentation Analytics Venues API
  slug: open-major-league-baseball-venues-api
- collection_type: open
  name: Stats API Documentation Analytics Weather API
  slug: open-major-league-baseball-weather-api
- collection_type: open
  name: Stats API Documentation
  slug: open-major-league-baseball
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/major-league-baseball-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/major-league-baseball-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/major-league-baseball-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/major-league-baseball
- group: company
  title: ''
  type: Website
  url: https://www.mlb.com/
- group: company
  title: ''
  type: News
  url: https://www.mlb.com/news
- group: other
  title: ''
  type: Stats
  url: https://www.mlb.com/stats
- group: other
  title: ''
  type: Standings
  url: https://www.mlb.com/standings
- group: other
  title: ''
  type: Schedule
  url: https://www.mlb.com/schedule
- group: other
  title: ''
  type: Teams
  url: https://www.mlb.com/team
- group: other
  title: ''
  type: Players
  url: https://www.mlb.com/players
- group: company
  title: ''
  type: Careers
  url: https://www.mlb.com/careers
- group: company
  title: ''
  type: Press
  url: https://www.mlb.com/press
- group: company
  title: ''
  type: Blog
  url: https://www.mlb.com/feeds/news/rss.xml
created: '2026-05-05'
description: Major League Baseball (MLB) is the professional baseball organization of the United States and Canada, operating the National League and American League with 30 teams. MLB Advanced Media (now part of MLB) provides public stats and game data through the MLB Stats API and the legacy MLB Data (lookup service) API, used by teams, broadcasters, analysts, and a wide community of developers building stats sites, fantasy applications, and analytical tools. MLB also exposes Statcast data through Baseball Savant. There is no general-purpose self-service developer portal with terms or signup; the APIs are widely consumed but are formally intended for partner use.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/major-league-baseball.png
layout: provider
modified: '2026-05-16'
name: Major League Baseball
nav: Providers
network: true
overview: 'Major League Baseball publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Attendance API, Awards API, and 28 more. Tagged areas include Analytics, Baseball, Entertainment, Media, and Sports.


  Major League Baseball''s developer surface includes product news, engineering blog, and 12 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Major League Baseball Domain Security
  slug: major-league-baseball-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Major League Baseball Vulnerability Disclosure
  slug: major-league-baseball-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: major-league-baseball
tags:
- Analytics
- Baseball
- Entertainment
- Media
- Sports
- Sports Data
- Statistics
website: https://www.mlb.com/
---
