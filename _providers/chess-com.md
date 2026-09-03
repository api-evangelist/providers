---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
  score: 20.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chess Com Agentic Access
  operation_count: 29
  slug: chess-com-agentic-access
  summary_line: 29 operations
api_count: 1
apis:
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Club profiles, members, and team matches
  name: Chess.com Clubs API
  slug: chess-com-clubs-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Country profiles, players, and clubs
  name: Chess.com Countries API
  slug: chess-com-countries-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Daily, live, and archived games (JSON and PGN)
  name: Chess.com Games API
  slug: chess-com-games-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Live leaderboards across time controls and variants
  name: Chess.com Leaderboards API
  slug: chess-com-leaderboards-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Daily and live team match details
  name: Chess.com Matches API
  slug: chess-com-matches-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Profiles, stats, online state, archives, clubs, matches, tournaments
  name: Chess.com Players API
  slug: chess-com-players-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Daily and random puzzles
  name: Chess.com Puzzles API
  slug: chess-com-puzzles-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Chess.com streamers
  name: Chess.com Streamers API
  slug: chess-com-streamers-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Lists of titled players by FIDE title
  name: Chess.com Titled Players API
  slug: chess-com-titled-players-api
- baseURL: https://api.chess.com/pub/
  baseurl_source: declared
  description: Tournament details, rounds, and groups
  name: Chess.com Tournaments API
  slug: chess-com-tournaments-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Chess.com Published Data Clubs API
  slug: open-chess-com-clubs-api
- collection_type: open
  name: Chess.com Published Data Clubs Countries API
  slug: open-chess-com-countries-api
- collection_type: open
  name: Chess.com Published Data Clubs Games API
  slug: open-chess-com-games-api
- collection_type: open
  name: Chess.com Published Data Clubs Leaderboards API
  slug: open-chess-com-leaderboards-api
- collection_type: open
  name: Chess.com Published Data Clubs Matches API
  slug: open-chess-com-matches-api
- collection_type: open
  name: Chess.com Published Data Clubs Players API
  slug: open-chess-com-players-api
- collection_type: open
  name: Chess.com Published Data API
  slug: open-chess-com-published-data-api
- collection_type: open
  name: Chess.com Published Data Clubs Puzzles API
  slug: open-chess-com-puzzles-api
- collection_type: open
  name: Chess.com Published Data Clubs Streamers API
  slug: open-chess-com-streamers-api
- collection_type: open
  name: Chess.com Published Data Clubs Titled Players API
  slug: open-chess-com-titled-players-api
- collection_type: open
  name: Chess.com Published Data Clubs Tournaments API
  slug: open-chess-com-tournaments-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chess-com-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chess-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chess-com-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.chess.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.chess.com/news/view/published-data-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.chess.com/en/articles/9650547-published-data-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chess.com/membership
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.chess.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.chess.com/legal
- group: company
  title: ''
  type: AboutUs
  url: https://www.chess.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.chess.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.chess.com/article
- group: operate
  title: ''
  type: Forums
  url: https://www.chess.com/forum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chess-com
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/chesscom
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/chess
- group: other
  title: ''
  type: Twitch
  url: https://www.twitch.tv/chess
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chess
- group: operate
  title: ''
  type: Support
  url: https://www.chess.com/coaches
- group: docs
  title: ''
  type: Documentation
  url: https://www.chess.com/streamers
- group: docs
  title: ''
  type: Documentation
  url: https://www.chess.com/leaderboard
- group: build
  title: ''
  type: SDKs
  url: https://github.com/andyruwruw/chess-web-api
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/chess-web-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sarartur/chess.com
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Stupidoodle/chess-com-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sornerol/chess-com-pubapi-java-wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/chrismaltais/chess-pub-api-client
- group: commercial
  title: ''
  type: Plans
  url: plans/chess-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chess-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chess-com-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/chess-com-vocabulary.yml
created: '2026-05-25'
examples:
- key_count: 2
  name: Chess Com Get Daily Puzzle Example
  slug: chess-com-get-daily-puzzle-example
- key_count: 2
  name: Chess Com Get Monthly Archive Example
  slug: chess-com-get-monthly-archive-example
- key_count: 2
  name: Chess Com Get Player Profile Example
  slug: chess-com-get-player-profile-example
finops:
- name: Chess Com Finops
  service_category: ''
  slug: chess-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chess-com.png
json_schemas:
- name: Chess.com Club
  property_count: 14
  slug: chess-com-club
- name: Chess.com Game
  property_count: 16
  slug: chess-com-game
- name: Chess.com Player
  property_count: 17
  slug: chess-com-player
json_structures:
- name: Chess Com Player Structure
  property_count: 0
  slug: chess-com-player-structure
jsonld:
- class_count: 0
  name: Chess Com Context
  property_count: 7
  slug: chess-com-context
layout: provider
modified: '2026-05-25'
name: Chess.com
nav: Providers
network: true
overview: 'Chess.com publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Clubs API, Countries API, Games API, and 7 more. Tagged areas include Chess, Gaming, Online Games, Sports, and Community.


  The Chess.com catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Chess.com''s developer surface includes developer portal, documentation, pricing, engineering blog, YouTube channel, support, and 25 more developer resources.'
plans:
- name: Chess Com Plans Pricing
  plan_count: 5
  slug: chess-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Chess Com Rate Limits
  slug: chess-com-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Chess.com API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: chess-com-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Chess.com API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: chess-com-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 28.8
    contract_quality: 56.0
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chess-com/refs/heads/main/screenshots/chess-com-2026-06-20T174300.png
security:
- kind: domain-security
  name: Chess Com Domain Security
  slug: chess-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chess Com Vulnerability Disclosure
  slug: chess-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chess-com
tags:
- Chess
- Gaming
- Online Games
- Sports
- Community
- Education
website: https://www.chess.com
---
