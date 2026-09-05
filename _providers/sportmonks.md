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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sportmonks Agentic Access
  operation_count: 17
  slug: sportmonks-agentic-access
  summary_line: 17 operations
api_count: 1
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
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Scheduled and historical match fixtures.
  name: Sportmonks Fixtures API
  slug: sportmonks-fixtures-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Competition metadata across countries and seasons.
  name: Sportmonks Leagues API
  slug: sportmonks-leagues-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Real-time score and match-state feeds.
  name: Sportmonks Livescores API
  slug: sportmonks-livescores-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Pre-match and in-play betting odds.
  name: Sportmonks Odds API
  slug: sportmonks-odds-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Player profiles, attributes, and career data.
  name: Sportmonks Players API
  slug: sportmonks-players-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Probabilities and predicted outcomes for upcoming fixtures.
  name: Sportmonks Predictions API
  slug: sportmonks-predictions-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Round and stage schedules per season.
  name: Sportmonks Schedules API
  slug: sportmonks-schedules-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Season records and per-season fixture lists.
  name: Sportmonks Seasons API
  slug: sportmonks-seasons-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: League tables and group standings.
  name: Sportmonks Standings API
  slug: sportmonks-standings-api
- baseURL: https://api.sportmonks.com/v3/football
  baseurl_source: declared
  description: Team profiles, squads, and metadata.
  name: Sportmonks Teams API
  slug: sportmonks-teams-api
artifact_total: 71
collections:
- collection_type: postman
  name: Sportmonks Football Fixtures API
  slug: postman-sportmonks-fixtures-api
- collection_type: postman
  name: Sportmonks Football Fixtures Leagues API
  slug: postman-sportmonks-leagues-api
- collection_type: postman
  name: Sportmonks Football Fixtures Livescores API
  slug: postman-sportmonks-livescores-api
- collection_type: postman
  name: Sportmonks Football Fixtures Odds API
  slug: postman-sportmonks-odds-api
- collection_type: postman
  name: Sportmonks Football Fixtures Players API
  slug: postman-sportmonks-players-api
- collection_type: postman
  name: Sportmonks Football Fixtures Predictions API
  slug: postman-sportmonks-predictions-api
- collection_type: postman
  name: Sportmonks Football Fixtures Schedules API
  slug: postman-sportmonks-schedules-api
- collection_type: postman
  name: Sportmonks Football Fixtures Seasons API
  slug: postman-sportmonks-seasons-api
- collection_type: postman
  name: Sportmonks Football Fixtures Standings API
  slug: postman-sportmonks-standings-api
- collection_type: postman
  name: Sportmonks Football Fixtures Teams API
  slug: postman-sportmonks-teams-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sportmonks Football Fixtures API
  slug: open-sportmonks-fixtures-api
- collection_type: open
  name: Sportmonks Football API
  slug: open-sportmonks-football
- collection_type: open
  name: Sportmonks Football Fixtures Leagues API
  slug: open-sportmonks-leagues-api
- collection_type: open
  name: Sportmonks Football Fixtures Livescores API
  slug: open-sportmonks-livescores-api
- collection_type: open
  name: Sportmonks Football Fixtures Odds API
  slug: open-sportmonks-odds-api
- collection_type: open
  name: Sportmonks Football Fixtures Players API
  slug: open-sportmonks-players-api
- collection_type: open
  name: Sportmonks Football Fixtures Predictions API
  slug: open-sportmonks-predictions-api
- collection_type: open
  name: Sportmonks Football Fixtures Schedules API
  slug: open-sportmonks-schedules-api
- collection_type: open
  name: Sportmonks Football Fixtures Seasons API
  slug: open-sportmonks-seasons-api
- collection_type: open
  name: Sportmonks Football Fixtures Standings API
  slug: open-sportmonks-standings-api
- collection_type: open
  name: Sportmonks Football Fixtures Teams API
  slug: open-sportmonks-teams-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sportmonks/overview
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


  Sportmonks'' developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Sportmonks Plans Pricing
  plan_count: 6
  slug: sportmonks-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Sportmonks Rate Limits
  slug: sportmonks-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sportmonks API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sportmonks-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Sportmonks API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 6
  slug: sportmonks-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 76.5
    catalog_earned_first_party: 0.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 28.8
    contract_quality: 60.3
    developer_ergonomics: 50.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 65.8
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sportmonks/refs/heads/main/screenshots/sportmonks-2026-08-17T125430.png
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
- Live Scores
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
