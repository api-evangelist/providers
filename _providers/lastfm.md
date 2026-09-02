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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Lastfm Agentic Access
  operation_count: 59
  slug: lastfm-agentic-access
  summary_line: 59 operations · 12 acting
api_count: 2
apis:
- description: Album metadata, tagging, and search.
  name: Last.fm Album API
  slug: lastfm-album-api
- description: Artist metadata, similarity, tagging, top albums/tracks, and search.
  name: Last.fm Artist API
  slug: lastfm-artist-api
- description: Token, session, and mobile session acquisition for authenticated calls.
  name: Last.fm Auth API
  slug: lastfm-auth-api
- description: Global top artists, tags, and tracks.
  name: Last.fm Chart API
  slug: lastfm-chart-api
- description: Country-level top artists and tracks.
  name: Last.fm Geo API
  slug: lastfm-geo-api
- description: A user's scrobbled artist library.
  name: Last.fm Library API
  slug: lastfm-library-api
- description: Tag metadata, similar tags, top albums/artists/tracks, and chart history.
  name: Last.fm Tag API
  slug: lastfm-tag-api
- description: Track metadata, scrobbling, love/unlove, tagging, search.
  name: Last.fm Track API
  slug: lastfm-track-api
- description: User profile, friends, listening history, top entities, and weekly charts.
  name: Last.fm User API
  slug: lastfm-user-api
arazzos:
- description: Search for an album, resolve its full info and tracklist, then surface the community tags that define its genre.
  name: Last.fm Album Genre Profile
  slug: lastfm-album-genre-profile-workflow
- description: Search for an artist by name, resolve full metadata, then surface their top tracks and similar artists.
  name: Last.fm Artist Discovery
  slug: lastfm-artist-discovery-workflow
- description: Take the
  name: Last.fm Chart To Album Deep Dive
  slug: lastfm-chart-to-album-workflow
- description: Take a genre tag's top artist, branch into similar artists, and pull that artist's top tracks.
  name: Last.fm Genre Artist Explorer
  slug: lastfm-genre-artist-explorer-workflow
- description: Find the top artist in a country, resolve their full profile, and list their top albums.
  name: Last.fm Geo Artist Spotlight
  slug: lastfm-geo-artist-spotlight-workflow
- description: Read a user's loved tracks, resolve the latest one's full info, and surface the community tags that describe it.
  name: Last.fm Loved Tracks Insight
  slug: lastfm-loved-tracks-insight-workflow
- description: Read a user's most recent track, resolve its full info, and surface the community tags that describe it.
  name: Last.fm Now Playing Context
  slug: lastfm-now-playing-context-workflow
- description: Resolve a tag's metadata, pull its top tracks, and fetch full info for the leading track.
  name: Last.fm Tag To Track Deep Dive
  slug: lastfm-tag-to-track-workflow
- description: Search for a track, resolve its full info, and build a similar-tracks radio seed — branching when no match is found.
  name: Last.fm Track Radio Seed
  slug: lastfm-track-radio-workflow
- description: Read a user's profile, find their top artist for a period, and surface that artist's top tracks.
  name: Last.fm User Taste Profile
  slug: lastfm-user-taste-profile-workflow
artifact_total: 74
collections:
- collection_type: postman
  name: Last.fm Album API
  slug: postman-lastfm-album-api
- collection_type: postman
  name: Last.fm Web Services API (2.0)
  slug: postman-lastfm-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Last.fm Web Services API (2.0) Album API
  slug: open-lastfm-album-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Artist API
  slug: open-lastfm-artist-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Auth API
  slug: open-lastfm-auth-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Chart API
  slug: open-lastfm-chart-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Geo API
  slug: open-lastfm-geo-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Library API
  slug: open-lastfm-library-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Tag API
  slug: open-lastfm-tag-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album Track API
  slug: open-lastfm-track-api
- collection_type: open
  name: Last.fm Web Services API (2.0) Album User API
  slug: open-lastfm-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lastfm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lastfm-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lastfm-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lastfm/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-album-genre-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-artist-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-chart-to-album-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-genre-artist-explorer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-geo-artist-spotlight-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-loved-tracks-insight-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-now-playing-context-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-tag-to-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-track-radio-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lastfm-user-taste-profile-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.last.fm
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.last.fm/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.last.fm/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.last.fm/api/intro
- group: docs
  title: ''
  type: APIReference
  url: https://www.last.fm/api/intro
- group: auth
  title: ''
  type: Authentication
  url: https://www.last.fm/api/authentication
- group: start
  title: ''
  type: Signup
  url: https://www.last.fm/api/account/create
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.last.fm/api/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.last.fm/legal/privacy
- group: design
  title: ''
  type: ErrorCodes
  url: https://www.last.fm/api/errorcodes
- group: operate
  title: ''
  type: Support
  url: https://support.last.fm
- group: operate
  title: ''
  type: Contact
  url: mailto:partners@last.fm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lastfm
- group: commercial
  title: ''
  type: Pricing
  url: plans/lastfm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lastfm-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/lastfm-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lastfm-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/lastfm-context.jsonld
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  title: Inflatable.Lastfm (.NET / NuGet) — portable C# client
  type: SDKs
  url: https://github.com/inflatablefriends/lastfm
- group: build
  title: feross/last-fm (JavaScript) — simple public-data client
  type: SDKs
  url: https://github.com/feross/last-fm
- group: build
  title: dandelionmood/php-lastfm (PHP) — dead-simple wrapper
  type: SDKs
  url: https://github.com/dandelionmood/php-lastfm
- group: build
  title: barryvanveen/lastfm (PHP + Laravel service provider)
  type: SDKs
  url: https://github.com/barryvanveen/lastfm
- group: build
  title: gordonbisnor/lastfm (Ruby) — Rails plugin
  type: SDKs
  url: https://github.com/gordonbisnor/lastfm
- group: build
  title: codegram/lastfm (Ruby) — broad method coverage
  type: SDKs
  url: https://github.com/codegram/lastfm
- group: build
  title: theorangewill/pylastfmapi (Python)
  type: SDKs
  url: https://github.com/theorangewill/pylastfmapi
- group: build
  title: jrichocean/Elixirfm (Elixir)
  type: SDKs
  url: https://github.com/jrichocean/Elixirfm
- group: build
  title: mihaiolteanu/lastfm (Common Lisp)
  type: SDKs
  url: https://github.com/mihaiolteanu/lastfm
- group: build
  title: supki/liblastfm (Haskell)
  type: SDKs
  url: https://github.com/supki/liblastfm
- group: build
  title: Nebulino/Scrobblenaut (Dart)
  type: SDKs
  url: https://github.com/Nebulino/Scrobblenaut
- group: build
  title: SHOEGAZEssb/Shoegaze.LastFM (modern C#)
  type: SDKs
  url: https://github.com/SHOEGAZEssb/Shoegaze.LastFM
- group: build
  title: mannuelf/lastfm-nodejs-client (TypeScript / Node.js)
  type: SDKs
  url: https://github.com/mannuelf/lastfm-nodejs-client
- group: build
  title: michaellavelle/spring-social-lastfm (Java / Spring Social)
  type: SDKs
  url: https://github.com/michaellavelle/spring-social-lastfm
- group: build
  title: ScrobblerContext — Last.fm MCP server (Swift, stdio MCP transport, search/library/scrobble)
  type: Tools
  url: https://github.com/tfmart/ScrobblerContext
- group: build
  title: lastfm-mcp — Cloudflare Workers MCP server with OAuth 2.0 for AI access to Last.fm listening data
  type: Tools
  url: https://github.com/rianvdm/lastfm-mcp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/last-fm
- group: company
  title: ''
  type: Blog
  url: https://www.last.fm/blog
- group: other
  title: ''
  type: X
  url: https://x.com/lastfm
- group: operate
  title: ''
  type: StatusPage
  url: https://x.com/lastfmstatus
- group: commercial
  title: ''
  type: Plans
  url: plans/lastfm-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lastfm-finops.yml
created: '2026-05-28'
description: Last.fm is the long-running music recommendation, scrobbling, and music-data service operated by CBS Interactive. Its Web Services 2.0 API (the AudioScrobbler API at ws.audioscrobbler.com/2.0/) exposes catalog data (artists, albums, tracks, tags), charts, geo-listening data, user listening history (recent tracks, top tracks/albums/artists, weekly charts), and the Scrobbling 2.0 write surface (track.scrobble, track.updateNowPlaying, track.love). Every operation is dispatched through a single endpoint via the `method` parameter (e.g. `method=user.getRecentTracks`). Authentication uses an API key for reads and a signed (`api_sig`) session-key flow for writes. The API is free for non-commercial use; commercial use requires a separate agreement via partners@last.fm.
examples:
- key_count: 1
  name: Artist Getinfo Response
  slug: artist-getInfo-response
- key_count: 1
  name: Lastfm Album Getinfo Example
  slug: lastfm-album-getinfo-example
- key_count: 1
  name: Lastfm Artist Getinfo Example
  slug: lastfm-artist-getinfo-example
- key_count: 1
  name: Lastfm Chart Gettopartists Example
  slug: lastfm-chart-gettopartists-example
- key_count: 1
  name: Lastfm Track Getinfo Example
  slug: lastfm-track-getinfo-example
- key_count: 1
  name: Lastfm Track Scrobble Example
  slug: lastfm-track-scrobble-example
- key_count: 1
  name: Lastfm User Getrecenttracks Example
  slug: lastfm-user-getrecenttracks-example
- key_count: 14
  name: Track Scrobble Request
  slug: track-scrobble-request
- key_count: 1
  name: User Getrecenttracks Response
  slug: user-getRecentTracks-response
features:
- description: Comprehensive metadata for artists, albums, and tracks including biographies, images, tags, and similar items
  name: Music Metadata
- description: Track submission API (Scrobbling 2.0) for recording listening history from any client or device
  name: Scrobbling
- description: Access recent tracks, loved tracks, top artists, albums, and tracks for any user
  name: User Listening History
- description: Global and geographic top artists and tracks, plus tag-based and weekly user charts
  name: Music Charts
- description: Similar artist and track recommendations powered by Last.fm's social listening data
  name: Music Discovery
- description: Full-text search across the Last.fm music catalog for artists, albums, and tracks
  name: Artist and Track Search
- description: Browse music by community-applied tags to discover themed playlists and artists
  name: Tag Exploration
- description: Access user friends, listening comparisons, and shared music taste data
  name: User Social Data
finops:
- name: Lastfm Finops
  service_category: ''
  slug: lastfm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lastfm.png
json_schemas:
- name: Artist
  property_count: 10
  slug: artist
- name: Last.fm Album
  property_count: 11
  slug: lastfm-album
- name: Last.fm Artist
  property_count: 10
  slug: lastfm-artist
- name: Last.fm Tag
  property_count: 6
  slug: lastfm-tag
- name: Last.fm Track
  property_count: 15
  slug: lastfm-track
- name: Last.fm User
  property_count: 12
  slug: lastfm-user
- name: Scrobble
  property_count: 10
  slug: scrobble
- name: Track
  property_count: 13
  slug: track
json_structures:
- name: Lastfm Album Structure
  property_count: 11
  slug: lastfm-album-structure
- name: Lastfm Artist Structure
  property_count: 8
  slug: lastfm-artist-structure
- name: Lastfm Track Structure
  property_count: 12
  slug: lastfm-track-structure
jsonld:
- class_count: 27
  name: Lastfm Context
  property_count: 8
  slug: lastfm-context
layout: provider
modified: '2026-08-08'
name: Last.fm
nav: Providers
network: true
overview: 'Last.fm publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Auth API, and 6 more. Tagged areas include Music, Audio, Scrobbling, Recommendations, and Charts.


  The Last.fm catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Last.fm''s developer surface includes authentication, documentation, getting-started guide, API reference, signup flow, support, pricing, and 48 more developer resources.'
plans:
- name: Lastfm Plans Pricing
  plan_count: 2
  slug: lastfm-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Lastfm Rate Limits
  slug: lastfm-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Last.fm API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lastfm-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Last.fm API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 4
  slug: lastfm-rules
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 27.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 68.8
    developer_ergonomics: 76.2
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 64.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lastfm/refs/heads/main/screenshots/lastfm-2026-06-20T184325.png
security:
- kind: authentication
  name: Lastfm Authentication
  slug: lastfm-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lastfm Domain Security
  slug: lastfm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lastfm
tags:
- Music
- Audio
- Scrobbling
- Recommendations
- Charts
- Public APIs
- AudioScrobbler
use_cases:
- description: Record tracks played in music apps to Last.fm user profiles for history and recommendations
  name: Music Player Scrobbling
- description: Augment music catalogs with artist bios, album art, tags, and similar artist data
  name: Music Metadata Enrichment
- description: Display weekly, monthly, or all-time listening charts for users in applications
  name: Personalized Charts
- description: Power recommendation engines with similar artist and track data from Last.fm
  name: Music Discovery Features
- description: Show what friends are listening to and compare music tastes between users
  name: Social Listening
- description: Display top artists and tracks by country or region for localized music features
  name: Geographic Music Trends
website: https://www.last.fm
---
