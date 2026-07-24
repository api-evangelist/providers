---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sportmonks Agentic Access
  operation_count: 17
  slug: sportmonks-agentic-access
  summary_line: 17 operations
api_count: 13
apis:
- description: REST API for cricket data covering 130+ leagues including IPL, international fixtures, and T20 competitions. Provides ball-by-ball commentary, live scoreboards, fixtures, teams, players, venues, offic
  name: Sportmonks Cricket API
  slug: cricket-api
- description: REST API for motorsport data including Formula 1 race results, qualifying, driver and constructor standings, lap times, season schedules, and circuit information. Replaces the deprecated Formula One v
  name: Sportmonks Motorsport API
  slug: motorsport-api
- description: Embeddable JavaScript widgets that render Sportmonks football data as ready-to-use UI components for livescores, league tables, fixtures, and match details. Designed for media sites and football publi
  name: Sportmonks Football Widgets
  slug: football-widgets
- description: Scheduled and historical match fixtures.
  name: Sportmonks Fixtures API
  slug: sportmonks-fixtures-api
- description: Competition metadata across countries and seasons.
  name: Sportmonks Leagues API
  slug: sportmonks-leagues-api
- description: Real-time score and match-state feeds.
  name: Sportmonks Livescores API
  slug: sportmonks-livescores-api
- description: Pre-match and in-play betting odds.
  name: Sportmonks Odds API
  slug: sportmonks-odds-api
- description: Player profiles, attributes, and career data.
  name: Sportmonks Players API
  slug: sportmonks-players-api
- description: Probabilities and predicted outcomes for upcoming fixtures.
  name: Sportmonks Predictions API
  slug: sportmonks-predictions-api
- description: Round and stage schedules per season.
  name: Sportmonks Schedules API
  slug: sportmonks-schedules-api
- description: Season records and per-season fixture lists.
  name: Sportmonks Seasons API
  slug: sportmonks-seasons-api
- description: League tables and group standings.
  name: Sportmonks Standings API
  slug: sportmonks-standings-api
- description: Team profiles, squads, and metadata.
  name: Sportmonks Teams API
  slug: sportmonks-teams-api
artifact_total: 50
collections:
- collection_type: open
  name: Sportmonks Football API
  slug: open-sportmonks-football
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sportmonks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sportmonks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sportmonks-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.sportmonks.com/
- group: start
  title: ''
  type: Portal
  url: https://my.sportmonks.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sportmonks.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sportmonks.com/football/welcome/introduction
- group: start
  title: ''
  type: Signup
  url: https://my.sportmonks.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sportmonks.com/football-api/
- group: company
  title: ''
  type: Blog
  url: https://www.sportmonks.com/blogs/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sportmonks.com/api-status/
- group: operate
  title: ''
  type: Support
  url: mailto:support@sportmonks.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sportmonks.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sportmonks.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sportmonks/
- group: company
  title: ''
  type: XTwitter
  url: https://twitter.com/Sportmonks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sportmonks
- group: build
  title: ''
  type: PostmanCollection
  url: https://cricket-postman.sportmonks.com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportmonks-fixture-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportmonks-team-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportmonks-player-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportmonks-livescore-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sportmonks-league-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sportmonks-fixture-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sportmonks-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/sportmonks-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sportmonks-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sportmonks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sportmonks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sportmonks-finops.yml
created: '2026-05-25'
description: Sportmonks is a Dutch sports data provider (Deventer, Netherlands) delivering developer-friendly REST APIs for football/soccer, cricket, and motorsport (Formula 1). The platform serves 30,000+ active users and 20,000+ developers building livescore portals, fantasy games, betting platforms, sports media products, and analytics tools. Sportmonks emphasizes fast real-time updates (<15 seconds), 99.9% uptime, transparent per-league pricing, and a forever-free tier covering selected leagues. APIs use JSON over REST with API token authentication via either an Authorization header or an `api_token` query parameter, and support fine-grained response shaping through filters, includes, and field selection.
examples:
- key_count: 4
  name: Sportmonks Fixture Example
  slug: sportmonks-fixture-example
- key_count: 2
  name: Sportmonks Livescore Example
  slug: sportmonks-livescore-example
features:
- description: Sub-15-second push of score and match-event updates across covered competitions.
  name: Real-Time Livescores
- description: Per-request response shaping to keep payloads small and queries expressive without server-side bespoke endpoints.
  name: Filters, Includes, Field Selection
- description: Permanent free access to selected leagues (Danish Superliga, Scottish Premiership) for evaluation and hobby use.
  name: Forever-Free Tier
- description: Plans gate the number of leagues a customer can pick rather than charging per-call, making cost predictable for niche regional products.
  name: Per-League Pricing
- description: Published reliability target backed by a public status page.
  name: 99.9% Uptime SLA
- description: 24/7 human-in-the-loop data processing layered on top of automated feeds.
  name: Human Data Verification
- description: First-party Postman collections and embeddable football widgets reduce time-to-first-render.
  name: Postman & Widgets
finops:
- name: Sportmonks Finops
  service_category: Sports Data Subscription
  slug: sportmonks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sportmonks.png
integrations:
- description: Official Sportmonks Cricket Postman collection at cricket-postman.sportmonks.com.
  name: Postman
- description: 20+ community-maintained client libraries on GitHub across Python, PHP/Laravel, TypeScript, Go, Java, R, and Ruby.
  name: Community SDKs
json_schemas:
- name: Sportmonks Fixture
  property_count: 20
  slug: sportmonks-fixture
- name: Sportmonks League
  property_count: 12
  slug: sportmonks-league
- name: Sportmonks Livescore
  property_count: 8
  slug: sportmonks-livescore
- name: Sportmonks Player
  property_count: 18
  slug: sportmonks-player
- name: Sportmonks Team
  property_count: 12
  slug: sportmonks-team
json_structures:
- name: Sportmonks Fixture Structure
  property_count: 0
  slug: sportmonks-fixture-structure
jsonld:
- class_count: 12
  name: Sportmonks Context
  property_count: 9
  slug: sportmonks-context
layout: provider
modified: '2026-05-25'
name: Sportmonks
nav: Providers
network: true
overview: 'Sportmonks publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cricket API, Fixtures API, Leagues API, and 8 more. Tagged areas include Cricket, Data, Developer-Friendly, Football, and Formula 1.


  The Sportmonks catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sportmonks'' developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Sportmonks Plans Pricing
  plan_count: 6
  slug: sportmonks-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Sportmonks Rate Limits
  slug: sportmonks-rate-limits
rules:
- name: Sportmonks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sportmonks-jsonschema-spectral-rules
- name: Sportmonks API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 6
  slug: sportmonks-rules
score:
  band: strong
  composite: 63.7
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.9
    developer_ergonomics: 50.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 63.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportmonks/refs/heads/main/screenshots/sportmonks-2026-06-20T194341.png
security:
- kind: authentication
  name: Sportmonks Authentication
  slug: sportmonks-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Sportmonks Domain Security
  slug: sportmonks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportmonks
solutions:
- description: Core soccer data API covering 2,300+ leagues with tiered league-count pricing.
  name: Football API
- description: Cricket data API with ball-by-ball detail across 130+ leagues.
  name: Cricket API
- description: F1 and broader motorsport data API (v3 successor to the deprecated Formula One v1 API).
  name: Motorsport API
- description: Drop-in embeddable widgets for media and publisher sites.
  name: Football Widgets
tags:
- Cricket
- Data
- Developer-Friendly
- Football
- Formula 1
- Livescores
- Motorsport
- Real-Time
- Soccer
- Sports
- Sports Data
- Statistics
use_cases:
- description: Public livescore sites consuming fixtures, livescores, and event feeds.
  name: Livescore Portals
- description: Fantasy game backends consuming player stats, lineups, and event data.
  name: Fantasy Football
- description: Sportsbook and trading platforms consuming pre-match and in-play odds.
  name: Sports Betting
- description: Editorial sites embedding widgets and pulling structured match data.
  name: Sports Media
- description: Clubs and analysts pulling player and team statistics for performance review.
  name: Football Clubs & Scouting
- description: Fantasy, prediction, and casual gaming products powered by live sports state.
  name: iGaming
website: https://www.sportmonks.com/
---
