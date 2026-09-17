---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Gracenote Agentic Access
  operation_count: 311
  slug: gracenote-agentic-access
  summary_line: 311 operations · 45 acting
api_count: 5
apis:
- description: The Gracenote OnConnect API delivers TV and video data including schedules, programs, celebrities, sports, images, and station lineups. Designed for mobile apps, connected TVs, EPGs, and streaming exp
  name: Gracenote OnConnect API
  slug: onconnect-api
- description: The Gracenote OnConnect Data API provides extended metadata for TV, movies, celebrities, and sports. It is designed for connected experiences and mobile applications that need rich entertainment data,
  name: Gracenote OnConnect Data API
  slug: onconnect-data-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Celebrities API from Gracenote — 2 operation(s) for celebrities.
  name: Gracenote Celebrities API
  slug: gracenote-celebrities-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Lineups API from Gracenote — 4 operation(s) for lineups.
  name: Gracenote Lineups API
  slug: gracenote-lineups-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Movies API from Gracenote — 2 operation(s) for movies.
  name: Gracenote Movies API
  slug: gracenote-movies-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Programs API from Gracenote — 2 operation(s) for programs.
  name: Gracenote Programs API
  slug: gracenote-programs-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Series API from Gracenote — 2 operation(s) for series.
  name: Gracenote Series API
  slug: gracenote-series-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Sports API from Gracenote — 2 operation(s) for sports.
  name: Gracenote Sports API
  slug: gracenote-sports-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Stations API from Gracenote — 3 operation(s) for stations.
  name: Gracenote Stations API
  slug: gracenote-stations-api
- description: A production remote Model Context Protocol server that grounds LLM responses in Gracenote's verified video metadata — more than 55 million titles plus continually updated viewing availability. Nine to
  name: Gracenote Video MCP Server
  slug: video-mcp-server
- description: A production remote Model Context Protocol server for live, upcoming and recent sports — eleven tools covering entity resolution, event discovery, match info, recaps, lineups, where-to-watch, team and
  name: Gracenote Sports MCP Server
  slug: sports-mcp-server
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The AlbumEditions API from Gracenote — 4 operation(s) for albumeditions.
  name: Gracenote Album Editions API
  slug: gracenote-albumeditions-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: An Album Master groups all known Album Editions for a given logical release and provides a single, canonical view across those editions. Think of it as a "parent" that holds together the remastered ve
  name: Gracenote Album Masters API
  slug: gracenote-albummasters-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Artists API from Gracenote — 4 operation(s) for artists.
  name: Gracenote Artists API
  slug: gracenote-artists-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Availability Day API from Gracenote — 1 operation(s) for availability day.
  name: Gracenote Availability Day API
  slug: gracenote-availability-day-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Availability Day Manifest API from Gracenote — 1 operation(s) for availability day manifest.
  name: Gracenote Availability Day Manifest API
  slug: gracenote-availability-day-manifest-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The bulk API from Gracenote — 4 operation(s) for bulk.
  name: Gracenote Bulk API
  slug: gracenote-bulk-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The catalog API from Gracenote — 3 operation(s) for catalog.
  name: Gracenote Catalog API
  slug: gracenote-catalog-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Catalog Item API from Gracenote — 1 operation(s) for catalog item.
  name: Gracenote Catalog Item API
  slug: gracenote-catalog-item-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Catalog Manifest API from Gracenote — 1 operation(s) for catalog manifest.
  name: Gracenote Catalog Manifest API
  slug: gracenote-catalog-manifest-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Classification Endpoints API from Gracenote — 2 operation(s) for classification endpoints.
  name: Gracenote Classification Endpoints API
  slug: gracenote-classification-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to curated content collections.
  name: Gracenote Collections API
  slug: gracenote-collections-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Contributor API from Gracenote — 1 operation(s) for contributor.
  name: Gracenote Contributor API
  slug: gracenote-contributor-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Controlled Vocabulary API from Gracenote — 1 operation(s) for controlled vocabulary.
  name: Gracenote Controlled Vocabulary API
  slug: gracenote-controlled-vocabulary-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Core On APIs API from Gracenote — 11 operation(s) for core on apis.
  name: Gracenote Core On APIs API
  slug: gracenote-core-on-apis-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Country API from Gracenote — 1 operation(s) for country.
  name: Gracenote Country API
  slug: gracenote-country-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Default API from Gracenote — 1 operation(s) for default.
  name: Gracenote Default API
  slug: gracenote-default-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints to be removed in a future release.
  name: Gracenote Deprecated API
  slug: gracenote-deprecated-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The descriptor correlation request enables the computation of Artist and Recording similarity by providing numerical values representing similarity or dissimilarity. These values can be used to inform
  name: Gracenote Descriptor Correlations API
  slug: gracenote-descriptorcorrelations-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: Descriptor hierarchies provide structured access to Gracenote's comprehensive taxonomies of musical descriptors including GENRES, LANGUAGES, ORIGINS, ERAS, ARTISTTYPES, MOODS, STYLES, and TEMPOS. Each
  name: Gracenote Descriptor Hierarchies API
  slug: gracenote-descriptorhierarchies-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Descriptors API from Gracenote — 1 operation(s) for descriptors.
  name: Gracenote Descriptors API
  slug: gracenote-descriptors-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: Entitlements represent authorization levels, determining the specific data access granted to a user based on their API key. All valid API keys are provisioned with the 'base' package at least. API key
  name: Gracenote Entitlements API
  slug: gracenote-entitlements-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to forthcoming features.
  name: Gracenote Experimental API
  slug: gracenote-experimental-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The export API from Gracenote — 3 operation(s) for export.
  name: Gracenote Export API
  slug: gracenote-export-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The General Endpoints API from Gracenote — 4 operation(s) for general endpoints.
  name: Gracenote General Endpoints API
  slug: gracenote-general-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The images API from Gracenote — 3 operation(s) for images.
  name: Gracenote Images API
  slug: gracenote-images-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Intermediate Endpoints API from Gracenote — 2 operation(s) for intermediate endpoints.
  name: Gracenote Intermediate Endpoints API
  slug: gracenote-intermediate-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The League Endpoints API from Gracenote — 12 operation(s) for league endpoints.
  name: Gracenote League Endpoints API
  slug: gracenote-league-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The League Season Endpoints API from Gracenote — 9 operation(s) for league season endpoints.
  name: Gracenote League Season Endpoints API
  slug: gracenote-league-season-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Match Endpoints API from Gracenote — 7 operation(s) for match endpoints.
  name: Gracenote Match Endpoints API
  slug: gracenote-match-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Media API from Gracenote — 1 operation(s) for media.
  name: Gracenote Media API
  slug: gracenote-media-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The movie-presentation API from Gracenote — 5 operation(s) for movie-presentation.
  name: Gracenote Movie Presentation API
  slug: gracenote-movie-presentation-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The movie-root API from Gracenote — 2 operation(s) for movie-root.
  name: Gracenote Movie Root API
  slug: gracenote-movie-root-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The movie-version API from Gracenote — 3 operation(s) for movie-version.
  name: Gracenote Movie Version API
  slug: gracenote-movie-version-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Movies in Theatres API from Gracenote — 6 operation(s) for movies in theatres.
  name: Gracenote Movies in Theatres API
  slug: gracenote-movies-in-theatres-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Movies on TV API from Gracenote — 3 operation(s) for movies on tv.
  name: Gracenote Movies on TV API
  slug: gracenote-movies-on-tv-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to music content.
  name: Gracenote Music API
  slug: gracenote-music-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: Retrieve social media links for movies and TV series.
  name: Gracenote Online Social API
  slug: gracenote-online-social-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: Retrieve online video availability and metadata for episodes, series, movies, and specials.
  name: Gracenote Online Video API
  slug: gracenote-online-video-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Overall Endpoints API from Gracenote — 4 operation(s) for overall endpoints.
  name: Gracenote Overall Endpoints API
  slug: gracenote-overall-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Person Endpoints API from Gracenote — 1 operation(s) for person endpoints.
  name: Gracenote Person Endpoints API
  slug: gracenote-person-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Phase Endpoints API from Gracenote — 4 operation(s) for phase endpoints.
  name: Gracenote Phase Endpoints API
  slug: gracenote-phase-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to podcast metadata.
  name: Gracenote Podcasts API
  slug: gracenote-podcasts-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The program-summaries API from Gracenote — 1 operation(s) for program-summaries.
  name: Gracenote Program Summaries API
  slug: gracenote-program-summaries-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The publish API from Gracenote — 2 operation(s) for publish.
  name: Gracenote Publish API
  slug: gracenote-publish-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Recordings API from Gracenote — 4 operation(s) for recordings.
  name: Gracenote Recordings API
  slug: gracenote-recordings-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to content search.
  name: Gracenote Search API
  slug: gracenote-search-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Series Endpoints API from Gracenote — 3 operation(s) for series endpoints.
  name: Gracenote Series Endpoints API
  slug: gracenote-series-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Series Season Endpoints API from Gracenote — 2 operation(s) for series season endpoints.
  name: Gracenote Series Season Endpoints API
  slug: gracenote-series-season-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The show-episode API from Gracenote — 3 operation(s) for show-episode.
  name: Gracenote Show Episode API
  slug: gracenote-show-episode-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The show-presentation API from Gracenote — 5 operation(s) for show-presentation.
  name: Gracenote Show Presentation API
  slug: gracenote-show-presentation-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The show-root API from Gracenote — 2 operation(s) for show-root.
  name: Gracenote Show Root API
  slug: gracenote-show-root-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The show-season API from Gracenote — 3 operation(s) for show-season.
  name: Gracenote Show Season API
  slug: gracenote-show-season-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The show-version API from Gracenote — 3 operation(s) for show-version.
  name: Gracenote Show Version API
  slug: gracenote-show-version-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The SourcePrograms APIs API from Gracenote — 1 operation(s) for sourceprograms apis.
  name: Gracenote SourcePrograms APIs API
  slug: gracenote-sourceprograms-apis-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Sources API from Gracenote — 1 operation(s) for sources.
  name: Gracenote Sources API
  slug: gracenote-sources-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Sport Endpoints API from Gracenote — 4 operation(s) for sport endpoints.
  name: Gracenote Sport Endpoints API
  slug: gracenote-sport-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Sports APIs API from Gracenote — 7 operation(s) for sports apis.
  name: Gracenote Sports APIs API
  slug: gracenote-sports-apis-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Team Endpoints API from Gracenote — 4 operation(s) for team endpoints.
  name: Gracenote Team Endpoints API
  slug: gracenote-team-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Tier, Conference and Division Endpoints API from Gracenote — 14 operation(s) for tier, conference and division endpoints.
  name: Gracenote Tier, Conference and Division Endpoints API
  slug: gracenote-tier-conference-and-division-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Tracks API from Gracenote — 1 operation(s) for tracks.
  name: Gracenote Tracks API
  slug: gracenote-tracks-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Update Endpoints API from Gracenote — 13 operation(s) for update endpoints.
  name: Gracenote Update Endpoints API
  slug: gracenote-update-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Venue Endpoints API from Gracenote — 1 operation(s) for venue endpoints.
  name: Gracenote Venue Endpoints API
  slug: gracenote-venue-endpoints-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to video program content.
  name: Gracenote Video API
  slug: gracenote-video-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Video Descriptors Taxonomy Items API from Gracenote — 1 operation(s) for video descriptors taxonomy items.
  name: Gracenote Video Descriptors Taxonomy Items API
  slug: gracenote-video-descriptors-taxonomy-items-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Video Popularity API from Gracenote — 1 operation(s) for video popularity.
  name: Gracenote Video Popularity API
  slug: gracenote-video-popularity-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The vocabulary API from Gracenote — 1 operation(s) for vocabulary.
  name: Gracenote Vocabulary API
  slug: gracenote-vocabulary-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: API endpoints related to radio station metadata.
  name: Gracenote Radio Stations API
  slug: gracenote-radio-stations-api
artifact_total: 95
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities API
  slug: open-gracenote-celebrities-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Lineups API
  slug: open-gracenote-lineups-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Movies API
  slug: open-gracenote-movies-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Programs API
  slug: open-gracenote-programs-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Series API
  slug: open-gracenote-series-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Sports API
  slug: open-gracenote-sports-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Stations API
  slug: open-gracenote-stations-api
- collection_type: open
  name: Gracenote OnConnect TMS API
  slug: open-gracenote
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-on-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-on-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-onconnect-lookup-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-onconnect-lookup-apis-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/skills/gracenote-tv-listings-with-onconnect.md
  title: ''
  type: AgentSkill
  url: skills/gracenote-tv-listings-with-onconnect.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-gvd-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-gvd-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-gn-ids-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-gn-ids-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/skills/gracenote-publish-a-movie-to-gn-ids.md
  title: ''
  type: AgentSkill
  url: skills/gracenote-publish-a-movie-to-gn-ids.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-gmd-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-gmd-api-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-gmd-api-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-gmd-api-v3-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-nexus-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-nexus-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-global-sports-data-lookup-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-global-sports-data-lookup-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/skills/gracenote-sports-schedule-and-standings.md
  title: ''
  type: AgentSkill
  url: skills/gracenote-sports-schedule-and-standings.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-global-sports-data-update-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-global-sports-data-update-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/overlays/gracenote-online-video-social-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gracenote-online-video-social-apis-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/capabilities/gracenote-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gracenote-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/agentic-access/gracenote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gracenote-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/security/gracenote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gracenote-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/authentication/gracenote-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gracenote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gracenote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gracenote
- group: company
  title: ''
  type: Website
  url: https://www.gracenote.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.tmsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devportal.gracenote.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tmsapi.com/Getting_Started
- group: operate
  title: ''
  type: Support
  url: https://www.gracenote.com/support/
- group: other
  title: ''
  type: Products
  url: https://www.gracenote.com/products/
- group: other
  title: ''
  type: Parent
  url: https://www.nielsen.com/
- group: company
  title: ''
  type: Blog
  url: https://gracenote.com/insights/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/mcp/gracenote-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gracenote-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/mcp/gracenote-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gracenote-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/well-known/gracenote-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gracenote-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/llms/gracenote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gracenote-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/conventions/gracenote-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gracenote-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/errors/gracenote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gracenote-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/lifecycle/gracenote-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gracenote-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/lifecycle/gracenote-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gracenote-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/changelog/gracenote-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gracenote-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/conformance/gracenote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gracenote-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/data-model/gracenote-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gracenote-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/packages/gracenote-packages.yml
  title: ''
  type: Packages
  url: packages/gracenote-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/packages/gracenote-packages.yml
  title: ''
  type: SDKs
  url: packages/gracenote-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/sandbox/gracenote-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gracenote-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/plans/gracenote-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gracenote-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/rate-limits/gracenote-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gracenote-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/finops/gracenote-finops.yml
  title: ''
  type: FinOps
  url: finops/gracenote-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/security/gracenote-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gracenote-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.gracenote.com/
- group: docs
  title: ''
  type: APIReference
  url: https://devportal.gracenote.com/catalog
- group: start
  title: ''
  type: SignUp
  url: https://devportal.gracenote.com/register
- group: start
  title: ''
  type: Login
  url: https://devportal.gracenote.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gracenote.com/gracenote-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gracenote.com/gracenote-website-privacy-notice/
created: '2026-03-16'
description: Gracenote, a Nielsen company, provides entertainment metadata, content recognition technology, and developer APIs for the TV, video, music, sports and automotive industries, powering content discovery, search and personalization across linear and streaming services worldwide. It publishes ten first-party OpenAPI 3.1.1 definitions covering 298 operations — TV schedules and program data (On API, OnConnect, GVD), the GN IDS content-submission API, global music data (GMD v2 and v3 Beta), automotive in-car entertainment (Nexus) and global sports data — plus two production Model Context Protocol servers for video and sports that ground LLM answers in Gracenote's verified metadata. Access is licensed through sales rather than self-serve.
finops:
- name: Gracenote Finops
  service_category: API
  slug: gracenote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gracenote.png
layout: provider
mcp_servers:
- description: Gracenote publishes two production, hosted Model Context Protocol servers — a Video MCP Server and a Sports MCP Server — that ground LLM responses in Gracenote's verified entertainment and sports meta
  name: Gracenote MCP Servers
  slug: gracenote-mcp-servers
modified: '2026-09-12'
name: Gracenote
nav: Providers
network: true
overview: 'Gracenote publishes 74 APIs on the [APIs.io](https://apis.io/) network, including Celebrities API, Lineups API, Movies API, and 71 more. Tagged areas include Artificial Intelligence, Automotive, Content Metadata, Entertainment, and MCP.


  Gracenote''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, changelog, sandbox, and 45 more developer resources.'
plans:
- name: Gracenote Plans Pricing
  plan_count: 0
  slug: gracenote-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Gracenote Rate Limits
  slug: gracenote-rate-limits
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 50.7
    developer_ergonomics: 66.1
    discoverability: 68.5
    operational_transparency: 10.5
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 18.9
      derived: 0
      marker_coverage: 0.0
      total: 74
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/screenshots/gracenote-2026-06-20T182312.png
security:
- kind: authentication
  name: Gracenote Authentication
  slug: gracenote-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Gracenote Domain Security
  slug: gracenote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gracenote Vulnerability Disclosure
  slug: gracenote-vulnerability-disclosure
  summary_line: Hackerone
slug: gracenote
tags:
- Artificial Intelligence
- Automotive
- Content Metadata
- Entertainment
- MCP
- Music
- Nielsen
- Sports
- Sports Data
- Streaming
- Television
- Video
- Video Metadata
website: https://www.gracenote.com/
---
