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
- acting_count: 0
  human_in_the_loop: 0
  name: Pandascore Agentic Access
  operation_count: 19
  slug: pandascore-agentic-access
  summary_line: 19 operations
api_count: 14
apis:
- description: Unified REST API for esports fixtures, matches, tournaments, leagues, series, teams, players, and historical statistics across all supported videogames. Bearer-token authenticated, paginated, and game
  name: PandaScore REST API
  slug: rest-api
- description: Esports betting odds and markets including pre-match and live odds, player props, BetBuilder, and Kill Maker markets across 308+ unique markets for supported titles. Delivered through the same REST su
  name: PandaScore Odds API
  slug: odds-api
- description: Real-time in-game state, frames, and event timelines streamed over WebSocket for supported esports titles. Used for live score apps, live trading, and second-screen experiences.
  name: PandaScore Live Data API
  slug: live-data-api
- description: The Changes API from PandaScore — 3 operation(s) for changes.
  name: PandaScore Changes API
  slug: pandascore-changes-api
- description: The Game - CS:GO API from PandaScore — 1 operation(s) for game - cs:go.
  name: PandaScore Game - CS:GO API
  slug: pandascore-game-cs-go-api
- description: The Game - Dota 2 API from PandaScore — 1 operation(s) for game - dota 2.
  name: PandaScore Game - Dota 2 API
  slug: pandascore-game-dota-2-api
- description: The Game - League of Legends API from PandaScore — 1 operation(s) for game - league of legends.
  name: PandaScore Game - League of Legends API
  slug: pandascore-game-league-of-legends-api
- description: The Game - Valorant API from PandaScore — 1 operation(s) for game - valorant.
  name: PandaScore Game - Valorant API
  slug: pandascore-game-valorant-api
- description: The Leagues API from PandaScore — 2 operation(s) for leagues.
  name: PandaScore Leagues API
  slug: pandascore-leagues-api
- description: The Matches API from PandaScore — 5 operation(s) for matches.
  name: PandaScore Matches API
  slug: pandascore-matches-api
- description: The Players API from PandaScore — 1 operation(s) for players.
  name: PandaScore Players API
  slug: pandascore-players-api
- description: The Series API from PandaScore — 1 operation(s) for series.
  name: PandaScore Series API
  slug: pandascore-series-api
- description: The Teams API from PandaScore — 1 operation(s) for teams.
  name: PandaScore Teams API
  slug: pandascore-teams-api
- description: The Tournaments API from PandaScore — 2 operation(s) for tournaments.
  name: PandaScore Tournaments API
  slug: pandascore-tournaments-api
artifact_total: 21
collections:
- collection_type: open
  name: PandaScore API
  slug: open-pandascore
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pandascore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pandascore-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pandascore-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pandascore.co/
- group: start
  title: ''
  type: Portal
  url: https://app.pandascore.co/dashboard/main
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pandascore.co/docs
- group: start
  title: ''
  type: Signup
  url: https://app.pandascore.co/signup
- group: company
  title: ''
  type: Blog
  url: https://pandascore.co/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pandascore
- group: company
  title: ''
  type: Careers
  url: https://www.welcometothejungle.com/fr/companies/pandascore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pandascore.co/terms-and-condition
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pandascore.co/privacy
- group: operate
  title: ''
  type: Contact
  url: mailto:sales@pandascore.co
created: '2026-05-23'
description: PandaScore is a Paris-based esports data and odds provider supplying real-time fixtures, live statistics, historical data, and betting markets across 13+ esports titles including League of Legends, Counter-Strike 2, Dota 2, Valorant, Rainbow Six Siege, Overwatch, Call of Duty, Rocket League, EA Sports FC, King of Glory, Wild Rift, StarCraft, and Mobile Legends Bang Bang. The PandaScore REST API at api.pandascore.co plus WebSocket feeds power fantasy platforms, media outlets, predictive analytics, live score apps, and regulated sportsbooks.
finops:
- name: Pandascore Finops
  service_category: API
  slug: pandascore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pandascore.png
layout: provider
modified: '2026-05-23'
name: PandaScore
nav: Providers
network: true
overview: 'PandaScore publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Changes API, Game - CS:GO API, Game - Dota 2 API, and 8 more. Tagged areas include Esports, Odds, Betting, Live Data, and Stats.


  PandaScore''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Pandascore Plans Pricing
  plan_count: 1
  slug: pandascore-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Pandascore Rate Limits
  slug: pandascore-rate-limits
score:
  band: thin
  composite: 39.6
  delta: -2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 53.4
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pandascore/refs/heads/main/screenshots/pandascore-2026-06-20T191336.png
security:
- kind: authentication
  name: Pandascore Authentication
  slug: pandascore-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pandascore Domain Security
  slug: pandascore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pandascore
tags:
- Esports
- Odds
- Betting
- Live Data
- Stats
- Fantasy
- WebSocket
- REST
website: https://pandascore.co/
---
