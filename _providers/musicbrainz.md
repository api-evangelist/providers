---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 6
  human_in_the_loop: 0
  name: Musicbrainz Agentic Access
  operation_count: 36
  slug: musicbrainz-agentic-access
  summary_line: 36 operations · 6 acting
api_count: 16
apis:
- description: Lookup, browse, and search for geographic areas (countries, cities, etc.).
  name: MusicBrainz Areas API
  slug: musicbrainz-areas-api
- description: Lookup, browse, and search for artists (people, bands, orchestras).
  name: MusicBrainz Artists API
  slug: musicbrainz-artists-api
- description: Authenticated user collections of entities.
  name: MusicBrainz Collections API
  slug: musicbrainz-collections-api
- description: Lookup, browse, and search for music events (concerts, festivals, etc.).
  name: MusicBrainz Events API
  slug: musicbrainz-events-api
- description: List the curated genre taxonomy.
  name: MusicBrainz Genres API
  slug: musicbrainz-genres-api
- description: Non-MBID lookups by ISRC, ISWC, and DiscID.
  name: MusicBrainz Identifiers API
  slug: musicbrainz-identifiers-api
- description: Lookup and search for instruments used in recordings.
  name: MusicBrainz Instruments API
  slug: musicbrainz-instruments-api
- description: Lookup, browse, and search for record labels.
  name: MusicBrainz Labels API
  slug: musicbrainz-labels-api
- description: Lookup, browse, and search for places (venues, studios, etc.).
  name: MusicBrainz Places API
  slug: musicbrainz-places-api
- description: Lookup, browse, and search for recordings (distinct audio captures of a performance).
  name: MusicBrainz Recordings API
  slug: musicbrainz-recordings-api
- description: Lookup, browse, and search for release groups (logical grouping of releases).
  name: MusicBrainz Release Groups API
  slug: musicbrainz-release-groups-api
- description: Lookup, browse, and search for releases (specific issues of an album).
  name: MusicBrainz Releases API
  slug: musicbrainz-releases-api
- description: Lookup, browse, and search for series (ordered groups of entities).
  name: MusicBrainz Series API
  slug: musicbrainz-series-api
- description: Authenticated submission of tags, ratings, barcodes, and ISRCs.
  name: MusicBrainz Submission API
  slug: musicbrainz-submission-api
- description: Lookup URLs linked to other MusicBrainz entities.
  name: MusicBrainz URLs API
  slug: musicbrainz-urls-api
- description: Lookup, browse, and search for musical works (abstract compositions).
  name: MusicBrainz Works API
  slug: musicbrainz-works-api
artifact_total: 36
collections:
- collection_type: open
  name: MusicBrainz Web Service v2
  slug: open-musicbrainz-web-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/musicbrainz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/musicbrainz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/musicbrainz-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/musicbrainz-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://musicbrainz.org/
- group: other
  title: ''
  type: Foundation
  url: https://metabrainz.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metabrainz
- group: docs
  title: ''
  type: Documentation
  url: https://musicbrainz.org/doc/MusicBrainz_API
- group: other
  title: ''
  type: Developer
  url: https://musicbrainz.org/doc/Developer_Resources
- group: operate
  title: ''
  type: Forums
  url: https://community.metabrainz.org/
- group: other
  title: ''
  type: IRC
  url: ircs://irc.libera.chat/#musicbrainz
- group: company
  title: ''
  type: Blog
  url: https://blog.metabrainz.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metabrainz.org/social-contract
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metabrainz.org/privacy
- group: commercial
  title: ''
  type: License
  url: https://musicbrainz.org/doc/About/Data_License
- group: other
  title: ''
  type: Donate
  url: https://metabrainz.org/donate
- group: other
  title: ''
  type: Database
  url: https://musicbrainz.org/doc/MusicBrainz_Database
- group: docs
  title: ''
  type: Schema
  url: https://musicbrainz.org/doc/MusicBrainz_Database/Schema
- group: other
  title: ''
  type: Download
  url: https://musicbrainz.org/doc/MusicBrainz_Database/Download
- group: other
  title: ''
  type: Replication
  url: https://musicbrainz.org/doc/Replication_Mechanics
- group: other
  title: ''
  type: Mirror
  url: https://musicbrainz.org/doc/MusicBrainz_Database/Mirror
- group: other
  title: ''
  type: Identifiers
  url: https://musicbrainz.org/doc/MusicBrainz_Identifier
- group: docs
  title: ''
  type: StyleGuide
  url: https://musicbrainz.org/doc/Style
- group: other
  title: ''
  type: API
  url: https://musicbrainz.org/doc/MusicBrainz_API
- group: operate
  title: ''
  type: RateLimits
  url: https://musicbrainz.org/doc/MusicBrainz_API/Rate_Limiting
- group: auth
  title: ''
  type: Authentication
  url: https://musicbrainz.org/doc/MusicBrainz_API/Authentication
- group: build
  title: MusicBrainz Server (canonical implementation)
  type: GitHubRepository
  url: https://github.com/metabrainz/musicbrainz-server
- group: build
  title: MusicBrainz Docker (self-hosted replica)
  type: GitHubRepository
  url: https://github.com/metabrainz/musicbrainz-docker
- group: build
  title: MusicBrainz Documentation Source
  type: GitHubRepository
  url: https://github.com/metabrainz/musicbrainz-docs
- group: build
  title: MMD RELAX NG Schema
  type: GitHubRepository
  url: https://github.com/metabrainz/mmd-schema
- group: build
  title: libdiscid (DiscID computation)
  type: CLI
  url: https://github.com/metabrainz/libdiscid
- group: build
  title: MusicBrainz Picard (Tagger)
  type: Tools
  url: https://picard.musicbrainz.org/
- group: build
  title: MCP Server (community)
  type: Tools
  url: https://github.com/usercourses63/musicbrainz-mcp-server
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/metabrainz/musicbrainz-server
- group: other
  title: MusicBrainz Android
  type: Mobile
  url: https://github.com/metabrainz/musicbrainz-android
- group: other
  title: MusicBrainz iOS
  type: Mobile
  url: https://github.com/metabrainz/musicbrainz-ios
- group: other
  title: ListenBrainz
  type: SisterProject
  url: https://listenbrainz.org/
- group: other
  title: Cover Art Archive
  type: SisterProject
  url: https://coverartarchive.org/
- group: other
  title: CritiqueBrainz
  type: SisterProject
  url: https://critiquebrainz.org/
- group: other
  title: BookBrainz
  type: SisterProject
  url: https://bookbrainz.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: MusicBrainz is an open-source, community-maintained music encyclopedia operated by the MetaBrainz Foundation, a US 501(c)(3) non-profit. It collects metadata about artists, releases, recordings, works, labels, places, areas, events, instruments, series, URLs, and the relationships between them, then exposes the catalog through a free public REST web service at https://musicbrainz.org/ws/2/. The dataset itself is released under CC0 (core data) and CC-BY-NC-SA (supplemental tables), the schema is open, and full database dumps and a live replication feed are available. The web service is read-mostly with authenticated submission endpoints for tags, ratings, collections, barcodes, and ISRCs, and is rate-limited to one request per IP per second with a mandatory descriptive User-Agent header.
examples:
- key_count: 3
  name: Musicbrainz Lookup Artist Example
  slug: musicbrainz-lookup-artist-example
- key_count: 3
  name: Musicbrainz Lookup Discid Example
  slug: musicbrainz-lookup-discid-example
- key_count: 3
  name: Musicbrainz Lookup Isrc Example
  slug: musicbrainz-lookup-isrc-example
- key_count: 3
  name: Musicbrainz Search Recordings Example
  slug: musicbrainz-search-recordings-example
graphqls:
- description: MusicBrainz is an open music encyclopedia. The API covers artist lookups, recording metadata, releases and release groups, labels, works, places, events, instruments, series, and relation data between
  name: MusicBrainz GraphQL API
  slug: musicbrainz-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/musicbrainz.png
json_schemas:
- name: MusicBrainz Artist
  property_count: 19
  slug: musicbrainz-artist
- name: MusicBrainz Recording
  property_count: 12
  slug: musicbrainz-recording
- name: MusicBrainz Release
  property_count: 20
  slug: musicbrainz-release
- name: MusicBrainz Work
  property_count: 12
  slug: musicbrainz-work
json_structures:
- name: Musicbrainz Artist Structure
  property_count: 0
  slug: musicbrainz-artist-structure
jsonld:
- class_count: 88
  name: Musicbrainz Context
  property_count: 7
  slug: musicbrainz-context
layout: provider
modified: '2026-05-29'
name: MusicBrainz
nav: Providers
network: true
overview: 'MusicBrainz publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Areas API, Artists API, Collections API, and 13 more. Tagged areas include Music, Metadata, Encyclopedia, Open Data, and Catalog.


  The MusicBrainz catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MusicBrainz''s developer surface includes authentication, documentation, engineering blog, CLI, tooling, and 36 more developer resources.'
plans:
- name: Musicbrainz Plans Pricing
  plan_count: 3
  slug: musicbrainz-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 4
  name: Musicbrainz Rate Limits
  slug: musicbrainz-rate-limits
rules:
- name: MusicBrainz API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: musicbrainz-jsonschema-spectral-rules
- name: MusicBrainz API Rules
  rule_count: 22
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 9
  slug: musicbrainz-rules
scopes:
- name: Musicbrainz Scopes
  scope_count: 7
  slug: musicbrainz-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 56.7
  delta: 3.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 66.7
    developer_ergonomics: 28.3
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 53.2
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/musicbrainz/refs/heads/main/screenshots/musicbrainz-2026-06-20T185906.png
security:
- kind: authentication
  name: Musicbrainz Authentication
  slug: musicbrainz-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Musicbrainz Domain Security
  slug: musicbrainz-domain-security
  summary_line: TLSv1.3 · DMARC
slug: musicbrainz
tags:
- Music
- Metadata
- Encyclopedia
- Open Data
- Catalog
- Identifiers
- ISRC
- ISWC
- MBID
- DiscID
- Artists
- Releases
- Recordings
- Works
- Labels
- Cover Art
- Open Source
- Non Profit
website: https://musicbrainz.org/
---
