---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Tvmaze Agentic Access
  operation_count: 72
  slug: tvmaze-agentic-access
  summary_line: 72 operations · 24 acting
api_count: 17
apis:
- description: The auth API from TVmaze — 3 operation(s) for auth.
  name: TVmaze auth API
  slug: tvmaze-auth-api
- description: Individual episode details including guest cast and crew.
  name: TVmaze Episodes API
  slug: tvmaze-episodes-api
- description: The followed networks API from TVmaze — 2 operation(s) for followed networks.
  name: TVmaze followed networks API
  slug: tvmaze-followed-networks-api
- description: The followed people API from TVmaze — 2 operation(s) for followed people.
  name: TVmaze followed people API
  slug: tvmaze-followed-people-api
- description: The followed shows API from TVmaze — 2 operation(s) for followed shows.
  name: TVmaze followed shows API
  slug: tvmaze-followed-shows-api
- description: The followed webchannels API from TVmaze — 2 operation(s) for followed webchannels.
  name: TVmaze followed webchannels API
  slug: tvmaze-followed-webchannels-api
- description: The marked episodes API from TVmaze — 2 operation(s) for marked episodes.
  name: TVmaze marked episodes API
  slug: tvmaze-marked-episodes-api
- description: Person profiles, cast credits, and crew credits.
  name: TVmaze People API
  slug: tvmaze-people-api
- description: Daily and rolling TV and web/streaming schedules.
  name: TVmaze Schedule API
  slug: tvmaze-schedule-api
- description: The scrobbling API from TVmaze — 4 operation(s) for scrobbling.
  name: TVmaze scrobbling API
  slug: tvmaze-scrobbling-api
- description: Free-text search and lookup endpoints for shows and people.
  name: TVmaze Search API
  slug: tvmaze-search-api
- description: Season-level metadata and episode listings.
  name: TVmaze Seasons API
  slug: tvmaze-seasons-api
- description: Show metadata, episodes, seasons, cast, crew, images, and aliases.
  name: TVmaze Shows API
  slug: tvmaze-shows-api
- description: The tagged shows API from TVmaze — 4 operation(s) for tagged shows.
  name: TVmaze tagged shows API
  slug: tvmaze-tagged-shows-api
- description: Bulk timestamps useful for incremental sync of shows and people.
  name: TVmaze Updates API
  slug: tvmaze-updates-api
- description: The voted episodes API from TVmaze — 2 operation(s) for voted episodes.
  name: TVmaze voted episodes API
  slug: tvmaze-voted-episodes-api
- description: The voted shows API from TVmaze — 2 operation(s) for voted shows.
  name: TVmaze voted shows API
  slug: tvmaze-voted-shows-api
artifact_total: 152
collections:
- collection_type: postman
  name: TVmaze Premium User auth API
  slug: postman-tvmaze-auth-api
- collection_type: postman
  name: TVmaze Premium User auth Episodes API
  slug: postman-tvmaze-episodes-api
- collection_type: postman
  name: TVmaze Premium User auth followed networks API
  slug: postman-tvmaze-followed-networks-api
- collection_type: postman
  name: TVmaze Premium User auth followed people API
  slug: postman-tvmaze-followed-people-api
- collection_type: postman
  name: TVmaze Premium User auth followed shows API
  slug: postman-tvmaze-followed-shows-api
- collection_type: postman
  name: TVmaze Premium User auth followed webchannels API
  slug: postman-tvmaze-followed-webchannels-api
- collection_type: postman
  name: TVmaze Premium User auth marked episodes API
  slug: postman-tvmaze-marked-episodes-api
- collection_type: postman
  name: TVmaze Premium User auth People API
  slug: postman-tvmaze-people-api
- collection_type: postman
  name: TVmaze Premium User auth Schedule API
  slug: postman-tvmaze-schedule-api
- collection_type: postman
  name: TVmaze Premium User auth scrobbling API
  slug: postman-tvmaze-scrobbling-api
- collection_type: postman
  name: TVmaze Premium User auth Search API
  slug: postman-tvmaze-search-api
- collection_type: postman
  name: TVmaze Premium User auth Seasons API
  slug: postman-tvmaze-seasons-api
- collection_type: postman
  name: TVmaze Premium User auth Shows API
  slug: postman-tvmaze-shows-api
- collection_type: postman
  name: TVmaze Premium User auth tagged shows API
  slug: postman-tvmaze-tagged-shows-api
- collection_type: postman
  name: TVmaze Premium User auth Updates API
  slug: postman-tvmaze-updates-api
- collection_type: postman
  name: TVmaze Premium User auth voted episodes API
  slug: postman-tvmaze-voted-episodes-api
- collection_type: postman
  name: TVmaze Premium User auth voted shows API
  slug: postman-tvmaze-voted-shows-api
- collection_type: open
  name: TVmaze Premium User API
  slug: open-tvmaze-premium
- collection_type: open
  name: TVmaze Public API
  slug: open-tvmaze-public
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tvmaze/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tvmaze-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tvmaze-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tvmaze-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tvmaze.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.tvmaze.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://static.tvmaze.com/apidoc/
- group: start
  title: ''
  type: Signup
  url: https://www.tvmaze.com/account/register
- group: start
  title: ''
  type: Login
  url: https://www.tvmaze.com/account/login
- group: start
  title: ''
  type: Console
  url: https://www.tvmaze.com/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tvmaze.com/premium
- group: commercial
  title: ''
  type: Plans
  url: plans/tvmaze-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tvmaze-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tvmaze-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://www.tvmaze.com/request/create
- group: operate
  title: ''
  type: FAQ
  url: https://www.tvmaze.com/faqs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tvmaze.com/threads/4/api-changelog
- group: company
  title: ''
  type: Blog
  url: https://www.tvmaze.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tvmaze.com/site/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tvmaze.com/site/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://www.tvmaze.com/site/copyright
- group: commercial
  title: ''
  type: DataPrivacy
  url: https://www.tvmaze.com/faqs/9/data-policies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tvmaze
- group: build
  title: Python TVmaze SDK (community, maintained by the TVmaze GitHub org)
  type: SDKs
  url: https://github.com/tvmaze/tvmaze
- group: design
  title: ''
  type: SpectralRules
  url: rules/tvmaze-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tvmaze-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tvmaze-context.jsonld
- group: build
  title: ''
  type: Tools
  url: ''
created: '2026-05-28'
description: TVmaze is a community-driven TV show database that publishes a free RESTful API for TV show, episode, season, cast, crew, and broadcast/streaming schedule data. The public API is anonymous, CORS-enabled, and licensed under CC BY-SA 4.0. A paid Premium subscription unlocks a separate user-scoped API for managing follows, votes, marks, tags, and scrobbling.
examples:
- key_count: 14
  name: Public Get Episode Example
  slug: public-get-episode-example
- key_count: 10
  name: Public Get Person Example
  slug: public-get-person-example
- key_count: 12
  name: Public Get Season Example
  slug: public-get-season-example
- key_count: 23
  name: Public Get Show Example
  slug: public-get-show-example
- key_count: 5
  name: Public Get Show Updates Example
  slug: public-get-show-updates-example
- key_count: 4
  name: Tvmaze Public Castcredit Example
  slug: tvmaze-public-castcredit-example
- key_count: 3
  name: Tvmaze Public Country Example
  slug: tvmaze-public-country-example
- key_count: 14
  name: Tvmaze Public Episode Example
  slug: tvmaze-public-episode-example
- key_count: 3
  name: Tvmaze Public Externals Example
  slug: tvmaze-public-externals-example
- key_count: 2
  name: Tvmaze Public Image Example
  slug: tvmaze-public-image-example
- key_count: 4
  name: Tvmaze Public Network Example
  slug: tvmaze-public-network-example
- key_count: 10
  name: Tvmaze Public Person Example
  slug: tvmaze-public-person-example
- key_count: 1
  name: Tvmaze Public Rating Example
  slug: tvmaze-public-rating-example
- key_count: 2
  name: Tvmaze Public Schedule Example
  slug: tvmaze-public-schedule-example
- key_count: 12
  name: Tvmaze Public Season Example
  slug: tvmaze-public-season-example
- key_count: 23
  name: Tvmaze Public Show Example
  slug: tvmaze-public-show-example
features:
- description: No API key required for read access to shows, episodes, schedules, cast, crew, people.
  name: Free Public API
- description: HTTP-Basic authenticated user-scoped API for follows, marks, votes, tags, and scrobbling.
  name: Premium User API
- description: /v1/auth/start + /v1/auth/poll flow lets third-party apps obtain a user's API key without prompting for the password.
  name: Device Auth Pairing
- description: Resolve a show by TVRage, TheTVDB, or IMDb identifier.
  name: External ID Lookup
- description: Use ?embed= to fold cast, episodes, seasons, nextepisode, or previousepisode into a single show response.
  name: Embedded Related Resources
- description: /updates/shows and /updates/people return timestamp maps for efficient catch-up jobs.
  name: Incremental Sync
- description: /schedule and /schedule/web accept an ISO country code and date to produce localized listings.
  name: Country-Aware Schedules
- description: /schedule/full returns every known future episode for bulk ingestion (cached 24h).
  name: Full Future Schedule
- description: Submit batches of viewing events through /v1/scrobble/episodes — available to free users too.
  name: Bulk Scrobbling
- description: Data is freely usable with attribution to tvmaze.com.
  name: CC BY-SA Licensed Data
finops:
- name: Tvmaze Finops
  service_category: ''
  slug: tvmaze-finops
image: https://static.tvmaze.com/images/api/tvm_api.png
integrations:
- description: Many Trakt-style workflows mirror TVmaze IDs and metadata.
  name: Trakt.tv
- description: Media-center plugins read TVmaze metadata for show artwork, episode info, and airdates.
  name: Plex / Kodi / Emby
- description: Stremio addons (e.g. tvmaze-addon) surface TVmaze schedules in the catalog UI.
  name: Stremio
- description: Several PVR ecosystems consume TVmaze as a fallback metadata provider.
  name: Sonarr / Radarr family
- description: Community MCP servers (mcp-tvmaze, tvmaze-mcp-server, 3cat-tvmaze-mcp) expose TVmaze as agent tools.
  name: Model Context Protocol (MCP)
- description: Apify hosts a TVmaze scraper actor with its own OpenAPI definition.
  name: Apify TVmaze Scraper
json_schemas:
- name: BulkResponse
  property_count: 0
  slug: tvmaze-premium-bulkresponse
- name: Episode
  property_count: 0
  slug: tvmaze-premium-episode
- name: EpisodeVote
  property_count: 3
  slug: tvmaze-premium-episodevote
- name: MarkedEpisode
  property_count: 4
  slug: tvmaze-premium-markedepisode
- name: MarkType
  property_count: 0
  slug: tvmaze-premium-marktype
- name: Network
  property_count: 0
  slug: tvmaze-premium-network
- name: NetworkFollow
  property_count: 2
  slug: tvmaze-premium-networkfollow
- name: Person
  property_count: 0
  slug: tvmaze-premium-person
- name: PersonFollow
  property_count: 2
  slug: tvmaze-premium-personfollow
- name: Show
  property_count: 0
  slug: tvmaze-premium-show
- name: ShowFollow
  property_count: 2
  slug: tvmaze-premium-showfollow
- name: ShowVote
  property_count: 3
  slug: tvmaze-premium-showvote
- name: Tag
  property_count: 2
  slug: tvmaze-premium-tag
- name: TagInstance
  property_count: 2
  slug: tvmaze-premium-taginstance
- name: Webchannel
  property_count: 0
  slug: tvmaze-premium-webchannel
- name: WebchannelFollow
  property_count: 2
  slug: tvmaze-premium-webchannelfollow
- name: Aka
  property_count: 2
  slug: tvmaze-public-aka
- name: CastCredit
  property_count: 4
  slug: tvmaze-public-castcredit
- name: Character
  property_count: 5
  slug: tvmaze-public-character
- name: Country
  property_count: 3
  slug: tvmaze-public-country
- name: CrewCredit
  property_count: 2
  slug: tvmaze-public-crewcredit
- name: Episode
  property_count: 14
  slug: tvmaze-public-episode
- name: Externals
  property_count: 3
  slug: tvmaze-public-externals
- name: Image
  property_count: 2
  slug: tvmaze-public-image
- name: Links
  property_count: 0
  slug: tvmaze-public-links
- name: Network
  property_count: 4
  slug: tvmaze-public-network
- name: Person
  property_count: 10
  slug: tvmaze-public-person
- name: Rating
  property_count: 1
  slug: tvmaze-public-rating
- name: Schedule
  property_count: 2
  slug: tvmaze-public-schedule
- name: Season
  property_count: 12
  slug: tvmaze-public-season
- name: Show
  property_count: 23
  slug: tvmaze-public-show
- name: WebChannel
  property_count: 0
  slug: tvmaze-public-webchannel
json_structures:
- name: Tvmaze Premium Bulkresponse Structure
  property_count: 0
  slug: tvmaze-premium-bulkresponse-structure
- name: Tvmaze Premium Episode Structure
  property_count: 0
  slug: tvmaze-premium-episode-structure
- name: Tvmaze Premium Episodevote Structure
  property_count: 0
  slug: tvmaze-premium-episodevote-structure
- name: Tvmaze Premium Markedepisode Structure
  property_count: 0
  slug: tvmaze-premium-markedepisode-structure
- name: Tvmaze Premium Marktype Structure
  property_count: 0
  slug: tvmaze-premium-marktype-structure
- name: Tvmaze Premium Network Structure
  property_count: 0
  slug: tvmaze-premium-network-structure
- name: Tvmaze Premium Networkfollow Structure
  property_count: 0
  slug: tvmaze-premium-networkfollow-structure
- name: Tvmaze Premium Person Structure
  property_count: 0
  slug: tvmaze-premium-person-structure
- name: Tvmaze Premium Personfollow Structure
  property_count: 0
  slug: tvmaze-premium-personfollow-structure
- name: Tvmaze Premium Show Structure
  property_count: 0
  slug: tvmaze-premium-show-structure
- name: Tvmaze Premium Showfollow Structure
  property_count: 0
  slug: tvmaze-premium-showfollow-structure
- name: Tvmaze Premium Showvote Structure
  property_count: 0
  slug: tvmaze-premium-showvote-structure
- name: Tvmaze Premium Tag Structure
  property_count: 0
  slug: tvmaze-premium-tag-structure
- name: Tvmaze Premium Taginstance Structure
  property_count: 0
  slug: tvmaze-premium-taginstance-structure
- name: Tvmaze Premium Webchannel Structure
  property_count: 0
  slug: tvmaze-premium-webchannel-structure
- name: Tvmaze Premium Webchannelfollow Structure
  property_count: 0
  slug: tvmaze-premium-webchannelfollow-structure
- name: Tvmaze Public Aka Structure
  property_count: 0
  slug: tvmaze-public-aka-structure
- name: Tvmaze Public Castcredit Structure
  property_count: 0
  slug: tvmaze-public-castcredit-structure
- name: Tvmaze Public Character Structure
  property_count: 0
  slug: tvmaze-public-character-structure
- name: Tvmaze Public Country Structure
  property_count: 0
  slug: tvmaze-public-country-structure
- name: Tvmaze Public Crewcredit Structure
  property_count: 0
  slug: tvmaze-public-crewcredit-structure
- name: Tvmaze Public Episode Structure
  property_count: 0
  slug: tvmaze-public-episode-structure
- name: Tvmaze Public Externals Structure
  property_count: 0
  slug: tvmaze-public-externals-structure
- name: Tvmaze Public Image Structure
  property_count: 0
  slug: tvmaze-public-image-structure
- name: Tvmaze Public Links Structure
  property_count: 0
  slug: tvmaze-public-links-structure
- name: Tvmaze Public Network Structure
  property_count: 0
  slug: tvmaze-public-network-structure
- name: Tvmaze Public Person Structure
  property_count: 0
  slug: tvmaze-public-person-structure
- name: Tvmaze Public Rating Structure
  property_count: 0
  slug: tvmaze-public-rating-structure
- name: Tvmaze Public Schedule Structure
  property_count: 0
  slug: tvmaze-public-schedule-structure
- name: Tvmaze Public Season Structure
  property_count: 0
  slug: tvmaze-public-season-structure
- name: Tvmaze Public Show Structure
  property_count: 0
  slug: tvmaze-public-show-structure
- name: Tvmaze Public Webchannel Structure
  property_count: 0
  slug: tvmaze-public-webchannel-structure
jsonld:
- class_count: 44
  name: Tvmaze Context
  property_count: 13
  slug: tvmaze-context
layout: provider
modified: '2026-05-30'
name: TVmaze
nav: Providers
network: true
overview: 'TVmaze publishes 17 APIs on the [APIs.io](https://apis.io/) network, including auth API, Episodes API, followed networks API, and 14 more. Tagged areas include Video, Television, Streaming, Schedule, and Metadata.


  The TVmaze catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  TVmaze''s developer surface includes authentication, documentation, API reference, signup flow, developer console, pricing, support, and 20 more developer resources.'
plans:
- name: Tvmaze Plans Pricing
  plan_count: 5
  slug: tvmaze-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Tvmaze Rate Limits
  slug: tvmaze-rate-limits
rules:
- name: TVmaze API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tvmaze-jsonschema-spectral-rules
- name: TVmaze API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 3
    warn: 7
  slug: tvmaze-rules
score:
  band: strong
  composite: 63.7
  delta: -2.8
  facets:
    commercial_clarity: 84.2
    contract_quality: 72.9
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 66.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tvmaze/refs/heads/main/screenshots/tvmaze-2026-06-20T195842.png
security:
- kind: authentication
  name: Tvmaze Authentication
  slug: tvmaze-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tvmaze Domain Security
  slug: tvmaze-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tvmaze
solutions:
- description: Anonymous public API for hobby projects, dashboards, and personal calendars.
  name: Free Personal Use
- description: Entry-tier subscription unlocking the user API and tracking features.
  name: Premium Bronze
- description: Adds custom iCal and RSS calendar feeds.
  name: Premium Silver
- description: Tops the tier with influence over feature development.
  name: Premium Gold
- description: Custom commercial licensing for high-volume or redistributive use beyond CC BY-SA personal use.
  name: Enterprise / Commercial
tags:
- Video
- Television
- Streaming
- Schedule
- Metadata
- Entertainment
- Public APIs
use_cases:
- description: Build a personal TV calendar driven by /schedule and Premium /v1/user/follows/shows.
  name: TV Calendar Apps
- description: Power show search and recommendation flows with /search/shows and ?embed= calls.
  name: Streaming Discovery
- description: Sync show, episode, and image metadata into Plex, Kodi, Emby, Jellyfin, or Stremio plugins.
  name: Media Center Integrations
- description: Use /v1/scrobble/episodes to record viewing history from media players.
  name: Trakt-Style Scrobblers
- description: Front the public API through MCP servers (e.g. mcp-tvmaze) to give LLM agents structured TV knowledge.
  name: AI Agents and Chatbots
- description: Bulk-ingest /shows, /people, and /schedule/full pages for analytics and ML training.
  name: Data Science / Research
website: https://www.tvmaze.com
---
