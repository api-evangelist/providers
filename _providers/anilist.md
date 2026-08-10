---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Anilist Agentic Access
  operation_count: 4
  slug: anilist-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: The AniList GraphQL API v2 is the primary public developer interface for AniList.co. It exposes anime, manga, character, staff, studio, user, activity, review, recommendation, thread, comment, notific
  name: AniList GraphQL API v2
  slug: anilist-graphql-api-v2
- description: GraphQL query and mutation endpoint
  name: AniList GraphQL API
  slug: anilist-graphql-api
- description: OAuth2 authorization code and implicit grant endpoints
  name: AniList OAuth2 API
  slug: anilist-oauth2-api
artifact_total: 122
collections:
- collection_type: open
  name: AniList GraphQL API v2
  slug: open-anilist
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/anilist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anilist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anilist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anilist-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://anilist.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anilist.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.anilist.co/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anilist.co/guide/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anilist.co/guide/graphql/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.anilist.co/guide/auth/
- group: start
  title: ''
  type: Signup
  url: https://anilist.co/signup
- group: start
  title: ''
  type: Login
  url: https://anilist.co/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anilist.co/settings/developer
- group: start
  title: ''
  type: Console
  url: https://anilist.co/settings/developer
- group: start
  title: ''
  type: Sandbox
  url: https://studio.apollographql.com/sandbox/explorer?endpoint=https%3A%2F%2Fgraphql.anilist.co
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.anilist.co/guide/terms-of-use#commercial-usage
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.anilist.co/guide/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anilist.co/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AniList
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AniList/docs
- group: operate
  title: ''
  type: Support
  url: mailto:contact@anilist.co
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@anilist.co
- group: company
  title: ''
  type: Blog
  url: https://anistaff.medium.com/
- group: other
  title: ''
  type: X
  url: https://x.com/AniListco
- group: build
  title: ''
  type: SDKs
  url: https://github.com/topics/anilist
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/AniList/docs/tree/main/docs/guide/snippets
- group: build
  title: Community MCP Server (yuna0x0/anilist-mcp)
  type: Tools
  url: https://github.com/yuna0x0/anilist-mcp
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: AniList is an anime and manga database, tracking, and social platform serving over 500,000 anime and manga entries along with character, staff, studio, user, activity, review, recommendation, and forum thread data. The primary developer surface is a free public GraphQL API at https://graphql.anilist.co, with OAuth2 authentication (Authorization Code, Implicit, and Auth Pin flows) for read/write operations against user list and social data.
examples:
- key_count: 6
  name: Anilist Airingschedule Example
  slug: anilist-airingschedule-example
- key_count: 15
  name: Anilist Character Example
  slug: anilist-character-example
- key_count: 2
  name: Anilist Characterimage Example
  slug: anilist-characterimage-example
- key_count: 8
  name: Anilist Charactername Example
  slug: anilist-charactername-example
- key_count: 3
  name: Anilist Fuzzydate Example
  slug: anilist-fuzzydate-example
- key_count: 4
  name: Anilist Graphqlerror Example
  slug: anilist-graphqlerror-example
- key_count: 3
  name: Anilist Graphqlrequest Example
  slug: anilist-graphqlrequest-example
- key_count: 3
  name: Anilist Graphqlresponse Example
  slug: anilist-graphqlresponse-example
- key_count: 55
  name: Anilist Media Example
  slug: anilist-media-example
- key_count: 4
  name: Anilist Mediacoverimage Example
  slug: anilist-mediacoverimage-example
- key_count: 20
  name: Anilist Medialist Example
  slug: anilist-medialist-example
- key_count: 5
  name: Anilist Medialistcollection Example
  slug: anilist-medialistcollection-example
- key_count: 9
  name: Anilist Mediatag Example
  slug: anilist-mediatag-example
- key_count: 4
  name: Anilist Mediatitle Example
  slug: anilist-mediatitle-example
- key_count: 5
  name: Anilist Pageinfo Example
  slug: anilist-pageinfo-example
- key_count: 6
  name: Anilist Recommendation Example
  slug: anilist-recommendation-example
- key_count: 16
  name: Anilist Review Example
  slug: anilist-review-example
- key_count: 27
  name: Anilist Staff Example
  slug: anilist-staff-example
- key_count: 2
  name: Anilist Staffimage Example
  slug: anilist-staffimage-example
- key_count: 7
  name: Anilist Staffname Example
  slug: anilist-staffname-example
- key_count: 7
  name: Anilist Studio Example
  slug: anilist-studio-example
- key_count: 22
  name: Anilist Thread Example
  slug: anilist-thread-example
- key_count: 14
  name: Anilist Threadcomment Example
  slug: anilist-threadcomment-example
- key_count: 5
  name: Anilist Tokenrequest Example
  slug: anilist-tokenrequest-example
- key_count: 4
  name: Anilist Tokenresponse Example
  slug: anilist-tokenresponse-example
- key_count: 23
  name: Anilist User Example
  slug: anilist-user-example
- key_count: 2
  name: Anilist Useravatar Example
  slug: anilist-useravatar-example
- key_count: 10
  name: Anilist Useroptions Example
  slug: anilist-useroptions-example
features:
- description: 500,000+ anime and manga entries with rich metadata including titles, formats, statuses, episodes, chapters, durations, genres, tags, scores, popularity, trends, external links, and relations.
  name: Comprehensive Media Catalog
- description: Searchable directories of characters and staff with relationships, voice actors, role credits, and birthday filters.
  name: Character & Staff Database
- description: Catalog of anime studios with associated media production credits.
  name: Studio Directory
- description: MediaList / MediaListCollection queries and mutations let apps read and write a user's anime/manga lists, custom lists, follows, favourites, likes, and activity feed.
  name: User Lists & Social Graph
- description: Read and write social activity (text/message/list), reviews, recommendations, forum threads, and thread comments.
  name: Activity, Reviews, Recommendations, Threads
- description: Per-user notification stream with type filtering and unread-count reset.
  name: Notifications
- description: AiringSchedule queries for upcoming episode airings; MediaTrend queries for time-series popularity and score trends.
  name: Airing Schedule & Trends
- description: Aggregate site statistics across users, anime, and manga.
  name: Site Statistics
- description: AniChartUser settings and highlights for the AniChart seasonal anime chart.
  name: AniChart Integration
- description: All list-returning queries are wrapped in a Page object with pageInfo (currentPage, lastPage, total, hasNextPage) for cursor-less pagination.
  name: Pagination via Page Type
- description: Markdown query converts AniList-flavored markdown to HTML (auth required).
  name: Server-side Markdown Rendering
graphqls:
- description: The AniList GraphQL API v2 is the primary public developer interface for AniList.co. It exposes anime, manga, character, staff, studio, user, activity, review, recommendation, thread, comment, notific
  name: AniList GraphQL API
  slug: anilist-graphql
image: https://anilist.co/img/icons/icon.svg
integrations:
- description: Media entries carry an `idMal` field cross-referencing MyAnimeList's canonical ID.
  name: MyAnimeList
- description: ExternalLinkSourceCollection exposes streaming, reading, social, and information sites linked from media entries (Crunchyroll, Funimation, Netflix, Hulu, VIZ, Comixology, Wikipedia, official sites, etc.).
  name: External Link Sources
- description: AniChart.net seasonal anime chart is powered by the same API; AniChartUser settings are mutable through the API.
  name: AniChart
- description: Official AniList Discord server provides API status and community support; the AniList org publishes a Discord search bot.
  name: Discord
- description: AniList exposes its schema through Apollo Studio's hosted sandbox explorer for interactive query authoring.
  name: Apollo Studio
json_schemas:
- name: AiringSchedule
  property_count: 6
  slug: anilist-airingschedule
- name: Character
  property_count: 15
  slug: anilist-character
- name: CharacterImage
  property_count: 2
  slug: anilist-characterimage
- name: CharacterName
  property_count: 8
  slug: anilist-charactername
- name: FuzzyDate
  property_count: 3
  slug: anilist-fuzzydate
- name: GraphQLError
  property_count: 4
  slug: anilist-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: anilist-graphqlrequest
- name: GraphQLResponse
  property_count: 3
  slug: anilist-graphqlresponse
- name: Media
  property_count: 55
  slug: anilist-media
- name: MediaCoverImage
  property_count: 4
  slug: anilist-mediacoverimage
- name: MediaList
  property_count: 20
  slug: anilist-medialist
- name: MediaListCollection
  property_count: 5
  slug: anilist-medialistcollection
- name: MediaTag
  property_count: 9
  slug: anilist-mediatag
- name: MediaTitle
  property_count: 4
  slug: anilist-mediatitle
- name: PageInfo
  property_count: 5
  slug: anilist-pageinfo
- name: Recommendation
  property_count: 6
  slug: anilist-recommendation
- name: Review
  property_count: 16
  slug: anilist-review
- name: Staff
  property_count: 27
  slug: anilist-staff
- name: StaffImage
  property_count: 2
  slug: anilist-staffimage
- name: StaffName
  property_count: 7
  slug: anilist-staffname
- name: Studio
  property_count: 7
  slug: anilist-studio
- name: Thread
  property_count: 22
  slug: anilist-thread
- name: ThreadComment
  property_count: 14
  slug: anilist-threadcomment
- name: TokenRequest
  property_count: 5
  slug: anilist-tokenrequest
- name: TokenResponse
  property_count: 4
  slug: anilist-tokenresponse
- name: User
  property_count: 23
  slug: anilist-user
- name: UserAvatar
  property_count: 2
  slug: anilist-useravatar
- name: UserOptions
  property_count: 10
  slug: anilist-useroptions
json_structures:
- name: Anilist Airingschedule Structure
  property_count: 6
  slug: anilist-airingschedule-structure
- name: Anilist Character Structure
  property_count: 15
  slug: anilist-character-structure
- name: Anilist Characterimage Structure
  property_count: 2
  slug: anilist-characterimage-structure
- name: Anilist Charactername Structure
  property_count: 8
  slug: anilist-charactername-structure
- name: Anilist Fuzzydate Structure
  property_count: 3
  slug: anilist-fuzzydate-structure
- name: Anilist Graphqlerror Structure
  property_count: 4
  slug: anilist-graphqlerror-structure
- name: Anilist Graphqlrequest Structure
  property_count: 3
  slug: anilist-graphqlrequest-structure
- name: Anilist Graphqlresponse Structure
  property_count: 3
  slug: anilist-graphqlresponse-structure
- name: Anilist Media Structure
  property_count: 55
  slug: anilist-media-structure
- name: Anilist Mediacoverimage Structure
  property_count: 4
  slug: anilist-mediacoverimage-structure
- name: Anilist Medialist Structure
  property_count: 20
  slug: anilist-medialist-structure
- name: Anilist Medialistcollection Structure
  property_count: 5
  slug: anilist-medialistcollection-structure
- name: Anilist Mediatag Structure
  property_count: 9
  slug: anilist-mediatag-structure
- name: Anilist Mediatitle Structure
  property_count: 4
  slug: anilist-mediatitle-structure
- name: Anilist Pageinfo Structure
  property_count: 5
  slug: anilist-pageinfo-structure
- name: Anilist Recommendation Structure
  property_count: 6
  slug: anilist-recommendation-structure
- name: Anilist Review Structure
  property_count: 16
  slug: anilist-review-structure
- name: Anilist Staff Structure
  property_count: 27
  slug: anilist-staff-structure
- name: Anilist Staffimage Structure
  property_count: 2
  slug: anilist-staffimage-structure
- name: Anilist Staffname Structure
  property_count: 7
  slug: anilist-staffname-structure
- name: Anilist Studio Structure
  property_count: 7
  slug: anilist-studio-structure
- name: Anilist Thread Structure
  property_count: 22
  slug: anilist-thread-structure
- name: Anilist Threadcomment Structure
  property_count: 14
  slug: anilist-threadcomment-structure
- name: Anilist Tokenrequest Structure
  property_count: 5
  slug: anilist-tokenrequest-structure
- name: Anilist Tokenresponse Structure
  property_count: 4
  slug: anilist-tokenresponse-structure
- name: Anilist User Structure
  property_count: 23
  slug: anilist-user-structure
- name: Anilist Useravatar Structure
  property_count: 2
  slug: anilist-useravatar-structure
- name: Anilist Useroptions Structure
  property_count: 10
  slug: anilist-useroptions-structure
jsonld:
- class_count: 25
  name: Anilist Context
  property_count: 99
  slug: anilist-context
layout: provider
modified: '2026-05-30'
name: AniList
nav: Providers
network: true
overview: 'AniList publishes 2 APIs on the [APIs.io](https://apis.io/) network: GraphQL API and OAuth2 API. Tagged areas include Anime, Manga, Entertainment, Media, and Social.


  The AniList catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AniList''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, developer console, sandbox, and 21 more developer resources.'
random_paper: 60
rules:
- name: AniList API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: anilist-jsonschema-spectral-rules
- name: AniList API Rules
  rule_count: 49
  severity_counts:
    error: 18
    hint: 0
    info: 9
    warn: 22
  slug: anilist-rules
scopes:
- name: Anilist Scopes
  scope_count: 0
  slug: anilist-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 29.6
    developer_ergonomics: 65.2
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anilist/refs/heads/main/screenshots/anilist-2026-06-20T172003.png
security:
- kind: authentication
  name: Anilist Authentication
  slug: anilist-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Anilist Domain Security
  slug: anilist-domain-security
  summary_line: TLSv1.3 · DMARC
slug: anilist
solutions:
- description: Free use, subject to terms (no data hoarding, no backup/storage abuse, no competing tracker without sustained AniList sync).
  name: Non-commercial / Hobby
- description: Free for commercial applications generating less than $150 in monthly revenue, no permission required.
  name: Commercial under $150/mo
- description: Requires a commercial license arranged via contact@anilist.co.
  name: Commercial over $150/mo
tags:
- Anime
- Manga
- Entertainment
- Media
- Social
- Database
- GraphQL
- OAuth2
- Public APIs
use_cases:
- description: Browse and search the catalog by season, format, genre, tag, popularity, score, source, country of origin, and free-text query.
  name: Anime/Manga Discovery Apps
- description: Authenticated apps can read and write a user's watching/reading/completed/paused/dropped/planning lists, custom lists, scores, and progress.
  name: Personal Tracker & List Sync
- description: Discord, Telegram, and web bots that surface upcoming episode airings, season schedules, and per-user notifications.
  name: Airing Calendar / Notification Bots
- description: Alternative frontends that render activity feeds, reviews, recommendations, and forum threads.
  name: Social & Community Frontends
- description: Build recommendation systems using user list data, scoring, genres, tags, and the built-in Recommendation graph.
  name: Recommendation Engines
- description: Trend dashboards, AniChart-style seasonal charts, and statistics visualizations built on MediaTrend and SiteStatistics queries.
  name: Data Visualization & Analytics
- description: Generate strongly typed clients in TypeScript, Rust, Kotlin, Swift, Dart, and others against the public schema for editor-completion and compile-time safety.
  name: GraphQL Codegen / Typed Clients
website: https://anilist.co/
---
