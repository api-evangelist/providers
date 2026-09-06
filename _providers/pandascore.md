---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pandascore Agentic Access
  operation_count: 19
  slug: pandascore-agentic-access
  summary_line: 19 operations
api_count: 1
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
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Changes API from PandaScore — 3 operation(s) for changes.
  name: PandaScore Changes API
  slug: pandascore-changes-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Game - CS:GO API from PandaScore — 1 operation(s) for game - cs:go.
  name: PandaScore Game - CS:GO API
  slug: pandascore-game-cs-go-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Game - Dota 2 API from PandaScore — 1 operation(s) for game - dota 2.
  name: PandaScore Game - Dota 2 API
  slug: pandascore-game-dota-2-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Game - League of Legends API from PandaScore — 1 operation(s) for game - league of legends.
  name: PandaScore Game - League of Legends API
  slug: pandascore-game-league-of-legends-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Game - Valorant API from PandaScore — 1 operation(s) for game - valorant.
  name: PandaScore Game - Valorant API
  slug: pandascore-game-valorant-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Leagues API from PandaScore — 2 operation(s) for leagues.
  name: PandaScore Leagues API
  slug: pandascore-leagues-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Matches API from PandaScore — 5 operation(s) for matches.
  name: PandaScore Matches API
  slug: pandascore-matches-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Players API from PandaScore — 1 operation(s) for players.
  name: PandaScore Players API
  slug: pandascore-players-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Series API from PandaScore — 1 operation(s) for series.
  name: PandaScore Series API
  slug: pandascore-series-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Teams API from PandaScore — 1 operation(s) for teams.
  name: PandaScore Teams API
  slug: pandascore-teams-api
- baseURL: https://api.pandascore.co
  baseurl_source: declared
  description: The Tournaments API from PandaScore — 2 operation(s) for tournaments.
  name: PandaScore Tournaments API
  slug: pandascore-tournaments-api
artifact_total: 33
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PandaScore Changes API
  slug: open-pandascore-changes-api
- collection_type: open
  name: PandaScore Changes Game - CS:GO API
  slug: open-pandascore-game-cs-go-api
- collection_type: open
  name: PandaScore Changes Game - Dota 2 API
  slug: open-pandascore-game-dota-2-api
- collection_type: open
  name: PandaScore Changes Game - League of Legends API
  slug: open-pandascore-game-league-of-legends-api
- collection_type: open
  name: PandaScore Changes Game - Valorant API
  slug: open-pandascore-game-valorant-api
- collection_type: open
  name: PandaScore Changes Leagues API
  slug: open-pandascore-leagues-api
- collection_type: open
  name: PandaScore Changes Matches API
  slug: open-pandascore-matches-api
- collection_type: open
  name: PandaScore Changes Players API
  slug: open-pandascore-players-api
- collection_type: open
  name: PandaScore Changes Series API
  slug: open-pandascore-series-api
- collection_type: open
  name: PandaScore Changes Teams API
  slug: open-pandascore-teams-api
- collection_type: open
  name: PandaScore Changes Tournaments API
  slug: open-pandascore-tournaments-api
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
random_paper: 6
rate_limits:
- limit_count: 2
  name: Pandascore Rate Limits
  slug: pandascore-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pandascore/refs/heads/main/screenshots/pandascore-2026-08-17T083019.png
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
