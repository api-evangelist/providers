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
- acting_count: 31
  human_in_the_loop: 2
  name: Trakt Agentic Access
  operation_count: 89
  slug: trakt-agentic-access
  summary_line: 89 operations · 31 acting · 2 human-in-the-loop
api_count: 22
apis:
- description: Upcoming and recently aired schedules for shows, episodes, and movies.
  name: Trakt Calendars API
  slug: trakt-calendars-api
- description: Movie and show certification reference data.
  name: Trakt Certifications API
  slug: trakt-certifications-api
- description: Lightweight social "now watching" check-ins.
  name: Trakt Checkin API
  slug: trakt-checkin-api
- description: Comment threads, replies, likes, reactions.
  name: Trakt Comments API
  slug: trakt-comments-api
- description: Country reference data.
  name: Trakt Countries API
  slug: trakt-countries-api
- description: Episode metadata, ratings, comments, watching.
  name: Trakt Episodes API
  slug: trakt-episodes-api
- description: Genre reference data.
  name: Trakt Genres API
  slug: trakt-genres-api
- description: Language reference data.
  name: Trakt Languages API
  slug: trakt-languages-api
- description: Trending, popular, and personal lists.
  name: Trakt Lists API
  slug: trakt-lists-api
- description: Movie metadata, trending, watched, anticipated, popular, ratings, related, people.
  name: Trakt Movies API
  slug: trakt-movies-api
- description: Television network reference data.
  name: Trakt Networks API
  slug: trakt-networks-api
- description: Personal notes attached to media items.
  name: Trakt Notes API
  slug: trakt-notes-api
- description: Authorization Code and Device OAuth flows.
  name: Trakt OAuth API
  slug: trakt-oauth-api
- description: Person metadata, filmography, lists.
  name: Trakt People API
  slug: trakt-people-api
- description: Personalized recommendations for movies and shows.
  name: Trakt Recommendations API
  slug: trakt-recommendations-api
- description: Start, pause, and stop scrobbles for movies and episodes.
  name: Trakt Scrobble API
  slug: trakt-scrobble-api
- description: Text and ID lookup across movies, shows, episodes, people, lists.
  name: Trakt Search API
  slug: trakt-search-api
- description: Season-level metadata and episodes.
  name: Trakt Seasons API
  slug: trakt-seasons-api
- description: Show metadata, trending, watched, anticipated, popular, progress, seasons, episodes.
  name: Trakt Shows API
  slug: trakt-shows-api
- description: Studio reference data.
  name: Trakt Studios API
  slug: trakt-studios-api
- description: History, watchlist, ratings, favorites, collection, playback progress.
  name: Trakt Sync API
  slug: trakt-sync-api
- description: Profiles, settings, follows, friends, social activity, comments, watching.
  name: Trakt Users API
  slug: trakt-users-api
artifact_total: 99
collections:
- collection_type: postman
  name: Trakt Calendars API
  slug: postman-trakt-calendars-api
- collection_type: postman
  name: Trakt Calendars Certifications API
  slug: postman-trakt-certifications-api
- collection_type: postman
  name: Trakt Calendars Checkin API
  slug: postman-trakt-checkin-api
- collection_type: postman
  name: Trakt Calendars Comments API
  slug: postman-trakt-comments-api
- collection_type: postman
  name: Trakt Calendars Countries API
  slug: postman-trakt-countries-api
- collection_type: postman
  name: Trakt Calendars Episodes API
  slug: postman-trakt-episodes-api
- collection_type: postman
  name: Trakt Calendars Genres API
  slug: postman-trakt-genres-api
- collection_type: postman
  name: Trakt Calendars Languages API
  slug: postman-trakt-languages-api
- collection_type: postman
  name: Trakt Calendars Lists API
  slug: postman-trakt-lists-api
- collection_type: postman
  name: Trakt Calendars Movies API
  slug: postman-trakt-movies-api
- collection_type: postman
  name: Trakt Calendars Networks API
  slug: postman-trakt-networks-api
- collection_type: postman
  name: Trakt Calendars Notes API
  slug: postman-trakt-notes-api
- collection_type: postman
  name: Trakt Calendars OAuth API
  slug: postman-trakt-oauth-api
- collection_type: postman
  name: Trakt Calendars People API
  slug: postman-trakt-people-api
- collection_type: postman
  name: Trakt Calendars Recommendations API
  slug: postman-trakt-recommendations-api
- collection_type: postman
  name: Trakt Calendars Scrobble API
  slug: postman-trakt-scrobble-api
- collection_type: postman
  name: Trakt Calendars Search API
  slug: postman-trakt-search-api
- collection_type: postman
  name: Trakt Calendars Seasons API
  slug: postman-trakt-seasons-api
- collection_type: postman
  name: Trakt Calendars Shows API
  slug: postman-trakt-shows-api
- collection_type: postman
  name: Trakt Calendars Studios API
  slug: postman-trakt-studios-api
- collection_type: postman
  name: Trakt Calendars Sync API
  slug: postman-trakt-sync-api
- collection_type: postman
  name: Trakt Calendars Users API
  slug: postman-trakt-users-api
- collection_type: open
  name: Trakt API
  slug: open-trakt
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/trakt/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trakt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trakt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trakt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trakt.tv
- group: start
  title: ''
  type: DeveloperPortal
  url: https://trakt.tv/oauth/applications
- group: docs
  title: ''
  type: Documentation
  url: https://trakt.docs.apiary.io/
- group: start
  title: ''
  type: Signup
  url: https://trakt.tv/auth/join
- group: commercial
  title: ''
  type: Pricing
  url: https://trakt.tv/vip
- group: commercial
  title: ''
  type: Plans
  url: plans/trakt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trakt-rate-limits.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trakt.tv/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trakt.tv/privacy
- group: operate
  title: ''
  type: Support
  url: https://forums.trakt.tv
- group: operate
  title: ''
  type: FAQ
  url: https://forums.trakt.tv/c/questions-help/8
- group: company
  title: ''
  type: Blog
  url: https://blog.trakt.tv
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trakt.tv
- group: operate
  title: ''
  type: ChangeLog
  url: https://forums.trakt.tv/c/announcements/3
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trakt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/trakt/trakt-api
- group: design
  title: ''
  type: SpectralRules
  url: rules/trakt-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trakt-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trakt-vocabulary.yml
- group: other
  title: ''
  type: Resources
  url: finops/trakt-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trakt/trakt-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/moogar0880/PyTrakt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trakt/nodeless-trakt
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Bogstag/oauth2-trakt
- group: build
  title: ''
  type: SDKs
  url: https://authjs.dev/reference/core/providers/trakt
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/trakt-android
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/trakt-apple
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/trakt-rippple
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/Plex-Trakt-Scrobbler
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/showly
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/trakt-web
- group: build
  title: ''
  type: Tools
  url: https://github.com/trakt/discord-presence
- group: build
  title: ''
  type: Tools
  url: https://github.com/kud/mcp-trakt
- group: build
  title: ''
  type: Tools
  url: https://github.com/kofort9/trakt-mcp-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/fab-codes/trakt-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/phhusson/trakt-mcp-server
- group: build
  title: ''
  type: Tools
  url: https://github.com/popcornemil/trakt-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/pipeworx-io/mcp-trakt
created: '2026-05-28'
description: Trakt is the personal media database for movies and TV. Its API v2 (api.trakt.tv) exposes ~150 endpoints across movies, shows, seasons, episodes, people, search, lists, calendars, recommendations, comments, notes, scrobble, checkin, and full per-user sync (history, watchlist, ratings, collection, favorites, playback progress). Authentication is OAuth 2.0 via Authorization Code or Device flows. The platform powers the Trakt website, official Android/iOS apps, and a large third-party ecosystem of media-center plugins and trackers.
examples:
- key_count: 3
  name: Trakt Addtohistory Example
  slug: trakt-addToHistory-example
- key_count: 3
  name: Trakt Generatedevicecode Example
  slug: trakt-generateDeviceCode-example
- key_count: 3
  name: Trakt Getmovie Example
  slug: trakt-getMovie-example
- key_count: 3
  name: Trakt Getshowwatchedprogress Example
  slug: trakt-getShowWatchedProgress-example
- key_count: 3
  name: Trakt Gettrendingmovies Example
  slug: trakt-getTrendingMovies-example
- key_count: 3
  name: Trakt Polldevicetoken Example
  slug: trakt-pollDeviceToken-example
- key_count: 3
  name: Trakt Scrobblestart Example
  slug: trakt-scrobbleStart-example
- key_count: 3
  name: Trakt Searchtext Example
  slug: trakt-searchText-example
features:
- description: Movies, shows, seasons, episodes, people, studios, networks, certifications — all keyed by trakt/imdb/tmdb/tvdb ids.
  name: Comprehensive media catalog
- description: history, watchlist, collection, favorites, ratings, and playback progress with /sync/last_activities delta detection.
  name: Per-user sync
- description: Start/pause/stop API with 80% completion semantics, dedupe, and resume-from-pause via /sync/playback.
  name: Scrobble lifecycle
- description: /recommendations/movies and /recommendations/shows return tailored suggestions per-user with hide/dismiss support.
  name: Personalized recommendations
- description: Public (all) and personal (my) calendars for shows, new shows, season premieres, finales, and movie releases.
  name: Calendars
- description: trending, popular, anticipated, hot, box office, streaming for both movies and shows.
  name: Discovery surfaces
- description: Follow/unfollow, friends, social activity feeds, comments, replies, likes, reactions, sentiments.
  name: Social graph
- description: Trending and popular lists plus full CRUD for personal lists with sorting and item-level notes.
  name: Lists
- description: Attach private notes to movies, shows, seasons, episodes, people, or history items.
  name: Notes (VIP)
- description: Lightweight social "now watching" status that auto-expires after the runtime.
  name: Checkin
- description: Authorization Code flow for web/server apps and Device Code flow for TV/console/CLI apps.
  name: OAuth 2.0
finops:
- name: Trakt Finops
  service_category: ''
  slug: trakt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trakt.png
integrations:
- description: Trakt cross-references TMDB IDs and recommends TMDB as the upstream metadata source for media reports.
  name: TMDB
- description: All movies and many shows include their IMDB ID for downstream lookup.
  name: IMDB
- description: Shows and episodes include TVDB IDs for legacy media-center compatibility.
  name: TVDB
- description: /movies/{id}/watchnow/justwatch_links/{country} returns deep links into JustWatch for streaming availability.
  name: JustWatch
- description: Official Plex-Trakt-Scrobbler bridges Plex playback events to /scrobble.
  name: Plex
- description: Scrobble + checkin requests accept a sharing object that crossposts the activity.
  name: Twitter / Mastodon / Tumblr
- description: Official trakt/discord-presence project surfaces Trakt activity as Discord rich presence.
  name: Discord
json_schemas:
- name: Trakt Episode
  property_count: 9
  slug: trakt-episode
- name: Trakt Movie
  property_count: 20
  slug: trakt-movie
- name: Trakt Scrobble Event
  property_count: 9
  slug: trakt-scrobble
- name: Trakt Show
  property_count: 19
  slug: trakt-show
- name: Trakt User Profile
  property_count: 13
  slug: trakt-user
json_structures:
- name: Trakt History Structure
  property_count: 0
  slug: trakt-history-structure
- name: Trakt Movie Structure
  property_count: 0
  slug: trakt-movie-structure
- name: Trakt Show Structure
  property_count: 0
  slug: trakt-show-structure
jsonld:
- class_count: 35
  name: Trakt Context
  property_count: 1
  slug: trakt-context
layout: provider
modified: '2026-05-30'
name: Trakt
nav: Providers
network: true
overview: 'Trakt publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Calendars API, Certifications API, Checkin API, and 19 more. Tagged areas include Video, Movies, Television, Media Tracking, and Scrobble.


  The Trakt catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trakt''s developer surface includes authentication, documentation, signup flow, pricing, support, FAQ, engineering blog, and 35 more developer resources.'
plans:
- name: Trakt Plans Pricing
  plan_count: 3
  slug: trakt-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 0
  name: Trakt Rate Limits
  slug: trakt-rate-limits
rules:
- name: Trakt API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trakt-jsonschema-spectral-rules
- name: Trakt API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: trakt-rules
score:
  band: strong
  composite: 63.2
  delta: -2.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 69.8
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trakt/refs/heads/main/screenshots/trakt-2026-06-20T195545.png
security:
- kind: authentication
  name: Trakt Authentication
  slug: trakt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trakt Domain Security
  slug: trakt-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: trakt
solutions:
- description: Personal use with the 2026 limits — 250 watchlist items, 5 personal lists, 100k history items, 10k ratings, 100 notes.
  name: Free
- description: $30 first year, $60 renewal — 5000 watchlist items, 100 personal lists, watchlist notes, year-in-review reports, no ads.
  name: Trakt VIP
- description: $1500 lifetime support tier.
  name: Trakt VIP EP
- description: Approval-required for apps that monetize Trakt data or generate significant traffic — contact support via the Trakt forums.
  name: Commercial use
tags:
- Video
- Movies
- Television
- Media Tracking
- Scrobble
- Recommendations
- Social
- OAuth2
- Public APIs
use_cases:
- description: Plex, Kodi, Jellyfin, and custom media centers report playback to /scrobble so a user's watch history stays accurate across devices.
  name: Media center scrobbling
- description: Mobile and web apps showing what a user has watched, what's next, and what's anticipated.
  name: Personal media tracker
- description: Apps that combine Trakt history with their own ranking to suggest the next thing to watch.
  name: Recommendation engines
- description: Cross-device watchlist with VIP-only note attachments per item.
  name: Watchlist management
- description: Subscribe to per-user calendars and surface upcoming episodes in third-party calendars or notifications.
  name: Calendar integrations
- description: Browse trending lists, follow other users, and comment on shows.
  name: Social discovery
- description: Multiple community MCP servers expose Trakt to LLM agents for "what should I watch next" workflows.
  name: AI agents / MCP
website: https://trakt.tv
---
