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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 84
  human_in_the_loop: 4
  name: Lichess Agentic Access
  operation_count: 185
  slug: lichess-agentic-access
  summary_line: 185 operations · 84 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Read and write account information and preferences. <https://lichess.org/account/preferences/game-display>
  name: Lichess Account API
  slug: lichess-account-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access Lichess cloud evaluations database. <https://lichess.org/analysis>
  name: Lichess Analysis API
  slug: lichess-analysis-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: 'Play on Lichess with physical boards and third-party clients. Works with normal Lichess accounts. Engine play or assistance is [forbidden](https://lichess.org/page/fair-play). ### Features - [Stream i'
  name: Lichess Board API
  slug: lichess-board-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Play on Lichess as a bot. Allows engine play. Read the [blog post announcement of lichess bots](https://lichess.org/blog/WvDNticAAMu_mHKP/welcome-lichess-bots). Only works with [Bot accounts](#tag/bot
  name: Lichess Bot API
  slug: lichess-bot-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: 'Relay chess events on Lichess. [Official broadcasts](https://lichess.org/broadcast) are maintained by Lichess, but you can [create your own broadcasts](https://lichess.org/broadcast/new) to cover any '
  name: Lichess Broadcasts API
  slug: lichess-broadcasts-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Create many games for other players. These endpoints are intended for tournament organisers.
  name: Lichess Bulk pairings API
  slug: lichess-bulk-pairings-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Send and receive challenges to play. To create a lot of challenges, consider [bulk pairing](#tag/bulk-pairings/POST/api/bulk-pairing) instead.
  name: Lichess Challenges API
  slug: lichess-challenges-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: '**This API is in alpha and subject to change.** Use or provide external engine analysis. External engines can provide analysis on pages like the [analysis board](https://lichess.org/analysis), running'
  name: Lichess External engine API
  slug: lichess-external-engine-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: FIDE players and federations from [their public download](https://ratings.fide.com/download_lists.phtml). <https://lichess.org/fide>
  name: Lichess FIDE API
  slug: lichess-fide-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access games played on Lichess. <https://lichess.org/games>
  name: Lichess Games API
  slug: lichess-games-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Private messages with other players. <https://lichess.org/inbox>
  name: Lichess Messaging API
  slug: lichess-messaging-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Obtaining and revoking OAuth tokens. [Read about the Lichess API authentication methods and code examples](https://github.com/lichess-org/api/blob/master/example/README.md).
  name: Lichess OAuth API
  slug: lichess-oauth-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Lookup positions from the [Lichess opening explorer](https://lichess.org/analysis#explorer). Runs <https://github.com/lichess-org/lila-openingexplorer>. > [!important] > The hostname for these endpoin
  name: Lichess Opening Explorer API
  slug: lichess-opening-explorer-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Fetch and solve [puzzles](https://lichess.org/training), view your puzzle history and dashboard. Our collection of puzzles is in the public domain, you can [download it here](https://database.lichess.
  name: Lichess Puzzles API
  slug: lichess-puzzles-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access relations between users.
  name: Lichess Relations API
  slug: lichess-relations-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access simuls played on Lichess. <https://lichess.org/simul>
  name: Lichess Simuls API
  slug: lichess-simuls-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access Lichess studies. <https://lichess.org/study>
  name: Lichess Studies API
  slug: lichess-studies-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Lookup positions from the [Lichess tablebase server](https://lichess.org/blog/W3WeMyQAACQAdfAL/7-piece-syzygy-tablebases-are-complete). > [!important] > The hostname for these endpoints is `tablebase.
  name: Lichess Tablebase API
  slug: lichess-tablebase-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access and manage Lichess teams and their members. <https://lichess.org/team>
  name: Lichess Teams API
  slug: lichess-teams-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access Arena tournaments played on Lichess. [Official Arena tournaments](https://lichess.org/tournament) are maintained by Lichess, but you can [create your own Arena tournaments](https://lichess.org/
  name: Lichess Tournaments (Arena) API
  slug: lichess-tournaments-arena-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access Swiss tournaments played on Lichess. [Read more about Swiss tournaments.](https://lichess.org/swiss).
  name: Lichess Tournaments (Swiss) API
  slug: lichess-tournaments-swiss-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: Access Lichess TV channels and games. <https://lichess.org/tv> & <https://lichess.org/games>
  name: Lichess TV API
  slug: lichess-tv-api
- baseURL: https://lichess.org
  baseurl_source: declared
  description: 'Access registered users on Lichess. <https://lichess.org/player> - Each user blog exposes an atom (RSS) feed, like <https://lichess.org/@/thibault/blog.atom> - User blogs mashup feed: https://lichess.'
  name: Lichess Users API
  slug: lichess-users-api
artifact_total: 111
asyncapis:
- description: AsyncAPI description of Lichess's streaming surface. Lichess does NOT expose its public real-time API over WebSocket; instead, streams are delivered over plain HTTPS using chunked transfer encoding, w
  name: Lichess Streaming API
  slug: lichess-asyncapi
collections:
- collection_type: postman
  name: Lichess.org API reference Account API
  slug: postman-lichess-account-api
- collection_type: postman
  name: Lichess.org API reference Account Analysis API
  slug: postman-lichess-analysis-api
- collection_type: postman
  name: Lichess.org API reference Account Board API
  slug: postman-lichess-board-api
- collection_type: postman
  name: Lichess.org API reference Account Bot API
  slug: postman-lichess-bot-api
- collection_type: postman
  name: Lichess.org API reference Account Broadcasts API
  slug: postman-lichess-broadcasts-api
- collection_type: postman
  name: Lichess.org API reference Account Bulk pairings API
  slug: postman-lichess-bulk-pairings-api
- collection_type: postman
  name: Lichess.org API reference Account Challenges API
  slug: postman-lichess-challenges-api
- collection_type: postman
  name: Lichess.org API reference Account External engine API
  slug: postman-lichess-external-engine-api
- collection_type: postman
  name: Lichess.org API reference Account FIDE API
  slug: postman-lichess-fide-api
- collection_type: postman
  name: Lichess.org API reference Account Games API
  slug: postman-lichess-games-api
- collection_type: postman
  name: Lichess.org API reference Account Messaging API
  slug: postman-lichess-messaging-api
- collection_type: postman
  name: Lichess.org API reference Account OAuth API
  slug: postman-lichess-oauth-api
- collection_type: postman
  name: Lichess.org API reference Account Opening Explorer API
  slug: postman-lichess-opening-explorer-api
- collection_type: postman
  name: Lichess.org API reference Account Puzzles API
  slug: postman-lichess-puzzles-api
- collection_type: postman
  name: Lichess.org API reference Account Relations API
  slug: postman-lichess-relations-api
- collection_type: postman
  name: Lichess.org API reference Account Simuls API
  slug: postman-lichess-simuls-api
- collection_type: postman
  name: Lichess.org API reference Account Studies API
  slug: postman-lichess-studies-api
- collection_type: postman
  name: Lichess.org API reference Account Tablebase API
  slug: postman-lichess-tablebase-api
- collection_type: postman
  name: Lichess.org API reference Account Teams API
  slug: postman-lichess-teams-api
- collection_type: postman
  name: Lichess.org API reference Account Tournaments (Arena) API
  slug: postman-lichess-tournaments-arena-api
- collection_type: postman
  name: Lichess.org API reference Account Tournaments (Swiss) API
  slug: postman-lichess-tournaments-swiss-api
- collection_type: postman
  name: Lichess.org API reference Account TV API
  slug: postman-lichess-tv-api
- collection_type: postman
  name: Lichess.org API reference Account Users API
  slug: postman-lichess-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lichess.org API reference Account API
  slug: open-lichess-account-api
- collection_type: open
  name: Lichess.org API reference Account Analysis API
  slug: open-lichess-analysis-api
- collection_type: open
  name: Lichess.org API reference Account Board API
  slug: open-lichess-board-api
- collection_type: open
  name: Lichess.org API reference Account Bot API
  slug: open-lichess-bot-api
- collection_type: open
  name: Lichess.org API reference Account Broadcasts API
  slug: open-lichess-broadcasts-api
- collection_type: open
  name: Lichess.org API reference Account Bulk pairings API
  slug: open-lichess-bulk-pairings-api
- collection_type: open
  name: Lichess.org API reference Account Challenges API
  slug: open-lichess-challenges-api
- collection_type: open
  name: Lichess.org API reference Account External engine API
  slug: open-lichess-external-engine-api
- collection_type: open
  name: Lichess.org API reference Account FIDE API
  slug: open-lichess-fide-api
- collection_type: open
  name: Lichess.org API reference Account Games API
  slug: open-lichess-games-api
- collection_type: open
  name: Lichess.org API reference Account Messaging API
  slug: open-lichess-messaging-api
- collection_type: open
  name: Lichess.org API reference Account OAuth API
  slug: open-lichess-oauth-api
- collection_type: open
  name: Lichess.org API reference Account Opening Explorer API
  slug: open-lichess-opening-explorer-api
- collection_type: open
  name: Lichess.org API reference Account Puzzles API
  slug: open-lichess-puzzles-api
- collection_type: open
  name: Lichess.org API reference Account Relations API
  slug: open-lichess-relations-api
- collection_type: open
  name: Lichess.org API reference Account Simuls API
  slug: open-lichess-simuls-api
- collection_type: open
  name: Lichess.org API reference Account Studies API
  slug: open-lichess-studies-api
- collection_type: open
  name: Lichess.org API reference Account Tablebase API
  slug: open-lichess-tablebase-api
- collection_type: open
  name: Lichess.org API reference Account Teams API
  slug: open-lichess-teams-api
- collection_type: open
  name: Lichess.org API reference Account Tournaments (Arena) API
  slug: open-lichess-tournaments-arena-api
- collection_type: open
  name: Lichess.org API reference Account Tournaments (Swiss) API
  slug: open-lichess-tournaments-swiss-api
- collection_type: open
  name: Lichess.org API reference Account TV API
  slug: open-lichess-tv-api
- collection_type: open
  name: Lichess.org API reference Account Users API
  slug: open-lichess-users-api
- collection_type: open
  name: Lichess.org API reference
  slug: open-lichess
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lichess/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lichess-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lichess-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lichess-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lichess-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lichess-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://lichess.org
- group: docs
  title: ''
  type: Documentation
  url: https://lichess.org/api
- group: start
  title: ''
  type: Sandbox
  url: https://lichess.org/api/ui
- group: start
  title: ''
  type: Sandbox
  url: https://lichess-org.github.io/api-demo/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lichess-org
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/api
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/lila
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/scalachess
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/chessground
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/pgn-viewer
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lichess-org/mobile
- group: build
  title: ''
  type: SDKs
  url: https://github.com/lichess-org/berserk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tors42/chariot
- group: build
  title: ''
  type: SDKs
  url: https://github.com/devjiwonchoi/equine
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Rabergsel/LichessNET
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Dblike/LichessSharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mkomon/uberserk
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/async-lichess-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-bot-devs/lichess-bot
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-org/fishnet
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-org/external-engine
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-org/broadcaster
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-org/pgn-mule
- group: build
  title: ''
  type: Tools
  url: https://github.com/lichess-org/api-ui
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/lichess-org/api/tree/master/example
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/lichess
- group: operate
  title: ''
  type: Forums
  url: https://lichess.org/forum
- group: other
  title: ''
  type: BulkDataDownload
  url: https://database.lichess.org/
- group: auth
  title: ''
  type: Authentication
  url: https://lichess.org/account/oauth/token
- group: docs
  title: ''
  type: Documentation
  url: https://lichess.org/developers
- group: auth
  title: ''
  type: Authentication
  url: https://lichess.org/account/oauth/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lichess.org/page/fair-play
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lichess.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lichess.org/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://lichess.org/source
- group: other
  title: ''
  type: Donate
  url: https://lichess.org/patron
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lichess.org/
- group: company
  title: ''
  type: Blog
  url: https://lichess.org/blog
- group: operate
  title: ''
  type: RateLimits
  url: https://lichess.org/api#section/Introduction/Rate-limiting
- group: auth
  title: ''
  type: Authentication
  url: https://lichess.org/api#tag/OAuth
- group: commercial
  title: ''
  type: License
  url: https://www.gnu.org/licenses/agpl-3.0.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/lichess-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lichess-rate-limits.yml
created: '2026-05-25T00:00:00.000Z'
description: Lichess is a free, ad-free, open-source online chess server operated by a French nonprofit and powered entirely by volunteers and donations. It serves millions of games per day with live play, tournaments, puzzles, studies, broadcasts, analysis, and a public API. The server (lila), engine library (scalachess), mobile app, board UI (chessground), and distributed Stockfish analysis network (fishnet) are all open source under AGPL-3.0, MIT, and GPL-3.0 licenses. The Lichess API provides 185 documented operations across 23 functional areas including Account, Users, Games, Puzzles, Teams, Board, Bot, Challenges, Arena and Swiss Tournaments, Simuls, Studies, Broadcasts, Messaging, OAuth, FIDE, Opening Explorer, Tablebase, External Engine, and Cloud Analysis, with comprehensive ND-JSON streaming support.
features:
- Free, ad-free, open-source online chess server operated by a French nonprofit, funded by donations
- Full OpenAPI 3.1 specification with 185 operations across 23 tags published at github.com/lichess-org/api
- Account, users, relations, and messaging endpoints for managing players and social graph
- Games REST and ND-JSON streaming endpoints for current and historical games, including PGN export
- TV channels and current best games for live broadcast and embedding
- Daily puzzle, puzzle by ID, puzzle activity, and puzzle dashboard endpoints
- Teams API for creating, joining, listing, and managing chess teams
- Board API for playing real-time games with physical boards and third-party clients using regular accounts
- Bot API for programmatic play by accounts upgraded to bot status, with streaming game state
- Challenges API for issuing, accepting, declining, and listing challenges including AI and open challenges
- Bulk pairings for programmatically creating many games at once
- Arena and Swiss tournament APIs including create, update, terminate, join, withdraw, and result export
- Simuls endpoint for current and upcoming simultaneous exhibitions
- Studies API for exporting and importing study chapters in PGN
- Broadcasts API for creating tournaments, rounds, and pushing PGN updates for live event coverage
- FIDE endpoints exposing FIDE player and federation data
- Opening Explorer with Masters database, Lichess database, and player database lookups
- Tablebase endpoint for 7-piece Syzygy endgame results
- External Engine API enabling user-hosted engines to power analysis on lichess.org/analysis
- Cloud evaluation lookup for previously evaluated positions
- OAuth 2.0 Authorization Code Flow with PKCE plus personal access tokens, long-lived (one year typical)
- Newline-delimited JSON (ND-JSON) streaming for events, games, and TV feeds
- Distributed Stockfish analysis network (fishnet) and open client-side Stockfish WASM builds
- Public dataset exports of all rated games, puzzles, and computer evaluations at database.lichess.org
- Official community SDKs in Python (berserk), Java (chariot), JavaScript/TypeScript (equine), .NET, and more
- AGPL-3.0 licensed server (lila), with MIT scalachess engine library and GPL-3.0 mobile and tooling code
image: https://lichess1.org/assets/logo/lichess-pad12.svg
json_schemas:
- name: Lichess Game
  property_count: 20
  slug: lichess-game
- name: Lichess User
  property_count: 16
  slug: lichess-user
jsonld:
- class_count: 55
  name: Lichess Context
  property_count: 16
  slug: lichess-context
layout: provider
modified: '2026-05-25'
name: Lichess
nav: Providers
network: true
overview: 'Lichess publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account API, Analysis API, Board API, and 20 more. Tagged areas include Chess, Games, Open-Source, Non-Profit, and Tournaments.


  The Lichess catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Lichess'' developer surface includes authentication, developer portal, documentation, sandbox, tooling, code examples, engineering blog, and 42 more developer resources.'
plans:
- name: Lichess Plans Pricing
  plan_count: 2
  slug: lichess-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 16
  name: Lichess Rate Limits
  slug: lichess-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Lichess API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: lichess-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Lichess API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lichess-jsonschema-spectral-rules
- effective_rule_count: 11
  extends: []
  name: Lichess API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 6
  slug: lichess-rules
scopes:
- name: Lichess Scopes
  scope_count: 23
  slug: lichess-scopes
  summary_line: 23 scopes · authorizationCode
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 80.9
    developer_ergonomics: 66.7
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 52.6
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lichess/refs/heads/main/screenshots/lichess-2026-06-20T184507.png
security:
- kind: authentication
  name: Lichess Authentication
  slug: lichess-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Lichess Domain Security
  slug: lichess-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lichess Vulnerability Disclosure
  slug: lichess-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lichess
tags:
- Chess
- Games
- Open-Source
- Non-Profit
- Tournaments
- Puzzles
- Bots
- Streaming
- ND-JSON
- Authentication
website: https://lichess.org
---
