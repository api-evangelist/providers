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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 31.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Hockey League Agentic Access
  operation_count: 15
  slug: national-hockey-league-agentic-access
  summary_line: 15 operations
api_count: 9
apis:
- description: Public but undocumented JSON API that powers NHL.com and the league's first-party web and mobile apps. Surfaces schedules, scores, play-by-play, standings, teams, players, draft, prospects, season sta
  name: NHL Web API
  slug: nhl-web-api
- description: 'Legacy statistics endpoint at api.nhle.com (and the older statsapi.web.nhl.com) used by community projects and analytics tools. Hosts deeper historical records, play-by-play, and shift data. Like the '
  name: NHL Stats API (Legacy)
  slug: nhl-stats-api
- description: The Game Center API from National Hockey League — 2 operation(s) for game center.
  name: National Hockey League Game Center API
  slug: national-hockey-league-game-center-api
- description: The Players API from National Hockey League — 2 operation(s) for players.
  name: National Hockey League Players API
  slug: national-hockey-league-players-api
- description: The Schedule API from National Hockey League — 1 operation(s) for schedule.
  name: National Hockey League Schedule API
  slug: national-hockey-league-schedule-api
- description: The Scores API from National Hockey League — 2 operation(s) for scores.
  name: National Hockey League Scores API
  slug: national-hockey-league-scores-api
- description: The Standings API from National Hockey League — 2 operation(s) for standings.
  name: National Hockey League Standings API
  slug: national-hockey-league-standings-api
- description: The Stats API from National Hockey League — 2 operation(s) for stats.
  name: National Hockey League Stats API
  slug: national-hockey-league-stats-api
- description: The Teams API from National Hockey League — 4 operation(s) for teams.
  name: National Hockey League Teams API
  slug: national-hockey-league-teams-api
artifact_total: 12
collections:
- collection_type: open
  name: NHL Web API
  slug: open-national-hockey-league
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-hockey-league-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-hockey-league-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-hockey-league
- group: company
  title: ''
  type: Website
  url: https://www.nhl.com/
- group: other
  title: ''
  type: Stats
  url: https://www.nhl.com/stats/
- group: other
  title: ''
  type: NHLEdge
  url: https://edge.nhl.com/
created: '2026-05-05'
description: The National Hockey League (NHL) is the premier professional ice hockey league in North America, comprised of 32 franchises across the United States and Canada. The NHL produces the Stanley Cup playoffs and is one of the major North American professional sports leagues. The NHL does not publish an officially documented developer portal; the league operates undocumented JSON endpoints used by its first-party web and mobile apps (api-web.nhle.com) and provides advanced statistics through NHL EDGE. Commercial data feeds are licensed through SMT, Sportradar, and other approved partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-hockey-league.png
layout: provider
modified: '2026-05-23'
name: National Hockey League
nav: Providers
network: true
overview: National Hockey League publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Game Center API, Players API, Schedule API, and 4 more. Tagged areas include Sports, Hockey, Entertainment, and Professional League.
random_paper: 21
score:
  band: emerging
  composite: 17.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 46.6
    developer_ergonomics: 0.0
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-hockey-league/refs/heads/main/screenshots/national-hockey-league-2026-06-20T190023.png
security:
- kind: domain-security
  name: National Hockey League Domain Security
  slug: national-hockey-league-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: national-hockey-league
tags:
- Sports
- Hockey
- Entertainment
- Professional League
website: https://www.nhl.com/
---
