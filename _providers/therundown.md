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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Therundown Agentic Access
  operation_count: 60
  slug: therundown-agentic-access
  summary_line: 60 operations
api_count: 14
apis:
- description: Delta/change feeds (V1 legacy)
  name: The Rundown V1 Delta API
  slug: therundown-v1-delta-api
- description: Events with line-based odds (V1 legacy)
  name: The Rundown V1 Events API
  slug: therundown-v1-events-api
- description: Moneyline, spread, total, best-line endpoints (V1 legacy)
  name: The Rundown V1 Lines API
  slug: therundown-v1-lines-api
- description: Reference data (V1 legacy)
  name: The Rundown V1 Reference API
  slug: therundown-v1-reference-api
- description: Sport listings, dates, events, schedules (V1 legacy)
  name: The Rundown V1 Sports API
  slug: therundown-v1-sports-api
- description: Real-time streaming via WebSocket (V1 legacy)
  name: The Rundown V1 WebSocket API
  slug: therundown-v1-websocket-api
- description: Events with market-based odds (V2)
  name: The Rundown V2 Events API
  slug: therundown-v2-events-api
- description: Market definitions, odds, deltas, and history (V2)
  name: The Rundown V2 Markets API
  slug: therundown-v2-markets-api
- description: Player data (V2)
  name: The Rundown V2 Players API
  slug: therundown-v2-players-api
- description: Reference data — affiliates, sportsbooks, season types (V2)
  name: The Rundown V2 Reference API
  slug: therundown-v2-reference-api
- description: Sport listings, dates, and teams (V2)
  name: The Rundown V2 Sports API
  slug: therundown-v2-sports-api
- description: Team and player statistics (V2)
  name: The Rundown V2 Stats API
  slug: therundown-v2-stats-api
- description: Team data, players, and stats (V2)
  name: The Rundown V2 Teams API
  slug: therundown-v2-teams-api
- description: Real-time streaming via WebSocket (V2)
  name: The Rundown V2 WebSocket API
  slug: therundown-v2-websocket-api
artifact_total: 87
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/therundown-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/therundown-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/therundown-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://therundown.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.therundown.io/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/TheRundown
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/therundowninc
- group: company
  title: ''
  type: Blog
  url: https://blog.therundown.io
- group: commercial
  title: ''
  type: Pricing
  url: https://therundown.io/pricing/api
- group: operate
  title: ''
  type: StatusPage
  url: https://therundown.instatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/therundownio
- group: commercial
  title: ''
  type: Plans
  url: plans/therundown-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/therundown-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/therundown-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/therundown-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/therundown-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: The Rundown is a sports betting data API platform providing real-time odds, lines, scores, and results across 30+ sports leagues including NFL, NBA, MLB, NHL, WNBA, MLS, college football and basketball, and international soccer, tennis, cricket, and Formula 1. The API aggregates data from 16+ sportsbooks including DraftKings, FanDuel, BetMGM, and Pinnacle, as well as prediction markets like Kalshi and Polymarket, normalizing everything into a single unified schema with 600+ market types covering moneylines, spreads, totals, player props, team totals, futures, and live in-play odds. Developers can access data via REST endpoints or WebSocket streaming for sub-second real-time updates, with historical odds data and line movement tracking available on higher tiers.
examples:
- key_count: 4
  name: Therundown Get Best Line Example
  slug: therundown-get-best-line-example
- key_count: 4
  name: Therundown Get Delta Example
  slug: therundown-get-delta-example
- key_count: 4
  name: Therundown Get Events By Date Example
  slug: therundown-get-events-by-date-example
- key_count: 4
  name: Therundown Get Market Odds Example
  slug: therundown-get-market-odds-example
- key_count: 4
  name: Therundown List Sports Example
  slug: therundown-list-sports-example
finops:
- name: Therundown Finops
  service_category: ''
  slug: therundown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/therundown.png
json_schemas:
- name: Affiliate
  property_count: 4
  slug: therundown-affiliate
- name: AffiliatesResponse
  property_count: 1
  slug: therundown-affiliatesresponse
- name: BestAffiliateInfo
  property_count: 3
  slug: therundown-bestaffiliateinfo
- name: BestLineResponse
  property_count: 5
  slug: therundown-bestlineresponse
- name: BestMoneyline
  property_count: 6
  slug: therundown-bestmoneyline
- name: BestSpread
  property_count: 6
  slug: therundown-bestspread
- name: BestTotal
  property_count: 6
  slug: therundown-besttotal
- name: ChartResponse
  property_count: 2
  slug: therundown-chartresponse
- name: ChartSeries
  property_count: 2
  slug: therundown-chartseries
- name: Conference
  property_count: 3
  slug: therundown-conference
- name: ConferencesResponse
  property_count: 1
  slug: therundown-conferencesresponse
- name: DeltasResponse
  property_count: 2
  slug: therundown-deltasresponse
- name: Division
  property_count: 4
  slug: therundown-division
- name: DivisionsResponse
  property_count: 1
  slug: therundown-divisionsresponse
- name: EventsV2Response
  property_count: 2
  slug: therundown-eventsv2response
- name: EventV2
  property_count: 12
  slug: therundown-eventv2
- name: Market
  property_count: 9
  slug: therundown-market
- name: MarketDeltaEntry
  property_count: 15
  slug: therundown-marketdeltaentry
- name: MarketDeltaResponse
  property_count: 2
  slug: therundown-marketdeltaresponse
- name: MarketHistoryResponse
  property_count: 2
  slug: therundown-markethistoryresponse
- name: MarketLinePriceHistory
  property_count: 13
  slug: therundown-marketlinepricehistory
- name: MarketLinePriceResponse
  property_count: 6
  slug: therundown-marketlinepriceresponse
- name: MarketLinesResponse
  property_count: 5
  slug: therundown-marketlinesresponse
- name: MarketParticipant
  property_count: 6
  slug: therundown-marketparticipant
- name: MarketParticipantResponse
  property_count: 4
  slug: therundown-marketparticipantresponse
- name: MarketParticipantsResponse
  property_count: 1
  slug: therundown-marketparticipantsresponse
- name: MarketResponse
  property_count: 6
  slug: therundown-marketresponse
- name: Meta
  property_count: 1
  slug: therundown-meta
- name: OpeningPricesResponse
  property_count: 2
  slug: therundown-openingpricesresponse
- name: Pitcher
  property_count: 6
  slug: therundown-pitcher
- name: PlayerGameStatResponse
  property_count: 3
  slug: therundown-playergamestatresponse
- name: PlayerGameStats
  property_count: 7
  slug: therundown-playergamestats
- name: PlayerNormalized
  property_count: 25
  slug: therundown-playernormalized
- name: PlayersResponse
  property_count: 1
  slug: therundown-playersresponse
- name: PlayerStatResponse
  property_count: 2
  slug: therundown-playerstatresponse
- name: PlayerStats
  property_count: 14
  slug: therundown-playerstats
- name: Region
  property_count: 2
  slug: therundown-region
- name: Schedule
  property_count: 11
  slug: therundown-schedule
- name: ScheduledEvent
  property_count: 22
  slug: therundown-scheduledevent
- name: ScheduleResponse
  property_count: 1
  slug: therundown-scheduleresponse
- name: Score
  property_count: 18
  slug: therundown-score
- name: SeasonTypeSport
  property_count: 4
  slug: therundown-seasontypesport
- name: SeasonTypesResponse
  property_count: 1
  slug: therundown-seasontypesresponse
- name: Sport
  property_count: 2
  slug: therundown-sport
- name: SportsResponse
  property_count: 1
  slug: therundown-sportsresponse
- name: StatDefinition
  property_count: 7
  slug: therundown-statdefinition
- name: StatsMeta
  property_count: 1
  slug: therundown-statsmeta
- name: Team
  property_count: 8
  slug: therundown-team
- name: TeamGameStatResponse
  property_count: 3
  slug: therundown-teamgamestatresponse
- name: TeamGameStats
  property_count: 6
  slug: therundown-teamgamestats
- name: TeamNormalized
  property_count: 10
  slug: therundown-teamnormalized
- name: TeamsResponse
  property_count: 1
  slug: therundown-teamsresponse
- name: TeamStats
  property_count: 13
  slug: therundown-teamstats
- name: V1Event
  property_count: 14
  slug: therundown-v1event
- name: V1EventsResponse
  property_count: 2
  slug: therundown-v1eventsresponse
- name: V1Line
  property_count: 8
  slug: therundown-v1line
- name: V1LinePeriods
  property_count: 14
  slug: therundown-v1lineperiods
- name: V1Moneyline
  property_count: 8
  slug: therundown-v1moneyline
- name: V1Spread
  property_count: 11
  slug: therundown-v1spread
- name: V1Total
  property_count: 11
  slug: therundown-v1total
jsonld:
- class_count: 4
  name: Therundown Context
  property_count: 49
  slug: therundown-context
layout: provider
modified: '2026-06-12'
name: The Rundown
nav: Providers
network: true
overview: 'The Rundown publishes 14 APIs on the [APIs.io](https://apis.io/) network, including V1 Delta API, V1 Events API, V1 Lines API, and 11 more. Tagged areas include Sports, Betting, Odds, NFL, and NBA.


  The The Rundown catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Rundown''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Therundown Plans Pricing
  plan_count: 8
  slug: therundown-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 0
  name: Therundown Rate Limits
  slug: therundown-rate-limits
rules:
- name: The Rundown API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: therundown-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/therundown/refs/heads/main/screenshots/therundown-2026-06-20T195255.png
security:
- kind: authentication
  name: Therundown Authentication
  slug: therundown-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Therundown Domain Security
  slug: therundown-domain-security
  summary_line: TLSv1.3 · DMARC
slug: therundown
tags:
- Sports
- Betting
- Odds
- NFL
- NBA
- MLB
- NHL
- Soccer
- Real-Time
- Sports Data
- Sportsbook
website: https://therundown.io
---
