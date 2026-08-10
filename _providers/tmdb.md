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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The full TMDB REST API surface (v3). Covers movies, TV series, seasons, episodes, people, credits, images, collections, companies, networks, keywords, genres, reviews, lists, certifications, find, tre
  name: TMDB API
  slug: tmdb-api
artifact_total: 455
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tmdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.themoviedb.org
- group: docs
  title: ''
  type: Documentation
  url: https://developer.themoviedb.org/
- group: other
  title: ''
  type: APIOverview
  url: https://developer.themoviedb.org/docs/getting-started
- group: start
  title: ''
  type: Signup
  url: https://www.themoviedb.org/signup
- group: auth
  title: ''
  type: GetAPIKey
  url: https://www.themoviedb.org/settings/api
- group: auth
  title: ''
  type: Authentication
  url: https://developer.themoviedb.org/docs/authentication-application
- group: docs
  title: ''
  type: RateLimitingDocs
  url: https://developer.themoviedb.org/docs/rate-limiting
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.themoviedb.org/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.themoviedb.org/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.themoviedb.org/talk
- group: operate
  title: ''
  type: StatusPage
  url: https://status.themoviedb.org
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.themoviedb.org/llms.txt
- group: other
  title: ''
  type: Wrappers
  url: https://developer.themoviedb.org/docs/wrappers-and-libraries
- group: build
  title: ''
  type: SDKs
  url: https://github.com/celiao/tmdbsimple
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/tmdbsimple/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/grantholle/moviedb-promise
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/moviedb-promise
- group: build
  title: ''
  type: SDKs
  url: https://github.com/leandrowkz/tmdb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/blakejoy/tmdb-ts
- group: build
  title: ''
  type: SDKs
  url: https://github.com/LordMike/TMDbLib
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cyruzin/golang-tmdb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ryanbradynd05/go-tmdb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adamayoung/TMDb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wtfzdotnet/php-tmdb-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ahmetabdi/themoviedb
- group: build
  title: ''
  type: SDKs
  url: https://github.com/c-eg/themoviedbapi
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/leonardogilrodriguez/mcp-tmdb
- group: commercial
  title: ''
  type: Plans
  url: plans/tmdb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tmdb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tmdb-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/tmdb-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tmdb-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tmdb-context.jsonld
created: '2026-05-28'
description: The Movie Database (TMDB) is a community-built movie, TV, and people metadata catalog with a free REST API used by streaming apps, recommendation engines, second-screen experiences, fan sites, and AI/ML workflows. The TMDB API v3 exposes ~150 endpoints across movies, TV series, seasons, episodes, people, credits, images, collections, companies, networks, keywords, genres, reviews, lists, certifications, trending, discover/search, watch providers, account/lists, authentication, and configuration. A v4 surface adds OAuth-style user authentication and richer list management. Non-commercial use is free; commercial use requires a separate written agreement with TMDB.
examples:
- key_count: 2
  name: Tmdb Api Account Add Favorite Response Example
  slug: tmdb-api-account-add-favorite-response-example
- key_count: 2
  name: Tmdb Api Account Add To Watchlist Response Example
  slug: tmdb-api-account-add-to-watchlist-response-example
- key_count: 7
  name: Tmdb Api Account Details Response Example
  slug: tmdb-api-account-details-response-example
- key_count: 4
  name: Tmdb Api Account Favorite Tv Response Example
  slug: tmdb-api-account-favorite-tv-response-example
- key_count: 4
  name: Tmdb Api Account Get Favorites Response Example
  slug: tmdb-api-account-get-favorites-response-example
- key_count: 4
  name: Tmdb Api Account Lists Response Example
  slug: tmdb-api-account-lists-response-example
- key_count: 4
  name: Tmdb Api Account Rated Movies Response Example
  slug: tmdb-api-account-rated-movies-response-example
- key_count: 4
  name: Tmdb Api Account Rated Tv Episodes Response Example
  slug: tmdb-api-account-rated-tv-episodes-response-example
- key_count: 4
  name: Tmdb Api Account Rated Tv Response Example
  slug: tmdb-api-account-rated-tv-response-example
- key_count: 4
  name: Tmdb Api Account Watchlist Movies Response Example
  slug: tmdb-api-account-watchlist-movies-response-example
- key_count: 4
  name: Tmdb Api Account Watchlist Tv Response Example
  slug: tmdb-api-account-watchlist-tv-response-example
- key_count: 2
  name: Tmdb Api Alternative Names Copy Response Example
  slug: tmdb-api-alternative-names-copy-response-example
- key_count: 3
  name: Tmdb Api Authentication Create Guest Session Response Example
  slug: tmdb-api-authentication-create-guest-session-response-example
- key_count: 3
  name: Tmdb Api Authentication Create Request Token Response Example
  slug: tmdb-api-authentication-create-request-token-response-example
- key_count: 3
  name: Tmdb Api Authentication Create Session From Login Response Example
  slug: tmdb-api-authentication-create-session-from-login-response-example
- key_count: 2
  name: Tmdb Api Authentication Create Session From V4Token Response Example
  slug: tmdb-api-authentication-create-session-from-v4token-response-example
- key_count: 2
  name: Tmdb Api Authentication Create Session Response Example
  slug: tmdb-api-authentication-create-session-response-example
- key_count: 1
  name: Tmdb Api Authentication Delete Session Response Example
  slug: tmdb-api-authentication-delete-session-response-example
- key_count: 3
  name: Tmdb Api Authentication Validate Key Response Example
  slug: tmdb-api-authentication-validate-key-response-example
- key_count: 3
  name: Tmdb Api Authentication Validate Key401Response Example
  slug: tmdb-api-authentication-validate-key401response-example
- key_count: 1
  name: Tmdb Api Certification Movie List Response Example
  slug: tmdb-api-certification-movie-list-response-example
- key_count: 1
  name: Tmdb Api Certifications Tv List Response Example
  slug: tmdb-api-certifications-tv-list-response-example
- key_count: 4
  name: Tmdb Api Changes Movie List Response Example
  slug: tmdb-api-changes-movie-list-response-example
- key_count: 4
  name: Tmdb Api Changes People List Response Example
  slug: tmdb-api-changes-people-list-response-example
- key_count: 4
  name: Tmdb Api Changes Tv List Response Example
  slug: tmdb-api-changes-tv-list-response-example
- key_count: 8
  name: Tmdb Api Collection Details Response Example
  slug: tmdb-api-collection-details-response-example
- key_count: 3
  name: Tmdb Api Collection Images Response Example
  slug: tmdb-api-collection-images-response-example
- key_count: 2
  name: Tmdb Api Collection Translations Response Example
  slug: tmdb-api-collection-translations-response-example
- key_count: 2
  name: Tmdb Api Company Alternative Names Response Example
  slug: tmdb-api-company-alternative-names-response-example
- key_count: 8
  name: Tmdb Api Company Details Response Example
  slug: tmdb-api-company-details-response-example
- key_count: 2
  name: Tmdb Api Company Images Response Example
  slug: tmdb-api-company-images-response-example
- key_count: 2
  name: Tmdb Api Configuration Details Response Example
  slug: tmdb-api-configuration-details-response-example
- key_count: 7
  name: Tmdb Api Credit Details Response Example
  slug: tmdb-api-credit-details-response-example
- key_count: 2
  name: Tmdb Api Details Copy Response Example
  slug: tmdb-api-details-copy-response-example
- key_count: 4
  name: Tmdb Api Discover Movie Response Example
  slug: tmdb-api-discover-movie-response-example
- key_count: 4
  name: Tmdb Api Discover Tv Response Example
  slug: tmdb-api-discover-tv-response-example
- key_count: 3
  name: Tmdb Api Error Response Example
  slug: tmdb-api-error-response-example
- key_count: 5
  name: Tmdb Api Find By Id Response Example
  slug: tmdb-api-find-by-id-response-example
- key_count: 1
  name: Tmdb Api Genre Movie List Response Example
  slug: tmdb-api-genre-movie-list-response-example
- key_count: 1
  name: Tmdb Api Genre Tv List Response Example
  slug: tmdb-api-genre-tv-list-response-example
- key_count: 4
  name: Tmdb Api Guest Session Rated Movies Response Example
  slug: tmdb-api-guest-session-rated-movies-response-example
- key_count: 4
  name: Tmdb Api Guest Session Rated Tv Episodes Response Example
  slug: tmdb-api-guest-session-rated-tv-episodes-response-example
- key_count: 4
  name: Tmdb Api Guest Session Rated Tv Response Example
  slug: tmdb-api-guest-session-rated-tv-response-example
- key_count: 2
  name: Tmdb Api Keyword Details Response Example
  slug: tmdb-api-keyword-details-response-example
- key_count: 5
  name: Tmdb Api Keyword Movies Response Example
  slug: tmdb-api-keyword-movies-response-example
- key_count: 2
  name: Tmdb Api List Add Movie Response Example
  slug: tmdb-api-list-add-movie-response-example
- key_count: 2
  name: Tmdb Api List Check Item Status Response Example
  slug: tmdb-api-list-check-item-status-response-example
- key_count: 2
  name: Tmdb Api List Clear Response Example
  slug: tmdb-api-list-clear-response-example
- key_count: 4
  name: Tmdb Api List Create Response Example
  slug: tmdb-api-list-create-response-example
- key_count: 2
  name: Tmdb Api List Delete Response Example
  slug: tmdb-api-list-delete-response-example
- key_count: 9
  name: Tmdb Api List Details Response Example
  slug: tmdb-api-list-details-response-example
- key_count: 2
  name: Tmdb Api List Remove Movie Response Example
  slug: tmdb-api-list-remove-movie-response-example
- key_count: 5
  name: Tmdb Api Lists Copy Response Example
  slug: tmdb-api-lists-copy-response-example
- key_count: 4
  name: Tmdb Api Movie Account States Response Example
  slug: tmdb-api-movie-account-states-response-example
- key_count: 2
  name: Tmdb Api Movie Add Rating Response Example
  slug: tmdb-api-movie-add-rating-response-example
- key_count: 2
  name: Tmdb Api Movie Alternative Titles Response Example
  slug: tmdb-api-movie-alternative-titles-response-example
- key_count: 1
  name: Tmdb Api Movie Changes Response Example
  slug: tmdb-api-movie-changes-response-example
- key_count: 3
  name: Tmdb Api Movie Credits Response Example
  slug: tmdb-api-movie-credits-response-example
- key_count: 2
  name: Tmdb Api Movie Delete Rating Response Example
  slug: tmdb-api-movie-delete-rating-response-example
- key_count: 26
  name: Tmdb Api Movie Details Response Example
  slug: tmdb-api-movie-details-response-example
- key_count: 6
  name: Tmdb Api Movie External Ids Response Example
  slug: tmdb-api-movie-external-ids-response-example
- key_count: 4
  name: Tmdb Api Movie Images Response Example
  slug: tmdb-api-movie-images-response-example
- key_count: 2
  name: Tmdb Api Movie Keywords Response Example
  slug: tmdb-api-movie-keywords-response-example
- key_count: 25
  name: Tmdb Api Movie Latest Id Response Example
  slug: tmdb-api-movie-latest-id-response-example
- key_count: 5
  name: Tmdb Api Movie Lists Response Example
  slug: tmdb-api-movie-lists-response-example
- key_count: 5
  name: Tmdb Api Movie Now Playing List Response Example
  slug: tmdb-api-movie-now-playing-list-response-example
- key_count: 4
  name: Tmdb Api Movie Popular List Response Example
  slug: tmdb-api-movie-popular-list-response-example
- key_count: 0
  name: Tmdb Api Movie Recommendations Response Example
  slug: tmdb-api-movie-recommendations-response-example
- key_count: 2
  name: Tmdb Api Movie Release Dates Response Example
  slug: tmdb-api-movie-release-dates-response-example
- key_count: 5
  name: Tmdb Api Movie Reviews Response Example
  slug: tmdb-api-movie-reviews-response-example
- key_count: 4
  name: Tmdb Api Movie Similar Response Example
  slug: tmdb-api-movie-similar-response-example
- key_count: 4
  name: Tmdb Api Movie Top Rated List Response Example
  slug: tmdb-api-movie-top-rated-list-response-example
- key_count: 2
  name: Tmdb Api Movie Translations Response Example
  slug: tmdb-api-movie-translations-response-example
- key_count: 5
  name: Tmdb Api Movie Upcoming List Response Example
  slug: tmdb-api-movie-upcoming-list-response-example
- key_count: 2
  name: Tmdb Api Movie Videos Response Example
  slug: tmdb-api-movie-videos-response-example
- key_count: 2
  name: Tmdb Api Movie Watch Providers Response Example
  slug: tmdb-api-movie-watch-providers-response-example
- key_count: 6
  name: Tmdb Api Network Details Response Example
  slug: tmdb-api-network-details-response-example
- key_count: 1
  name: Tmdb Api Person Changes Response Example
  slug: tmdb-api-person-changes-response-example
- key_count: 3
  name: Tmdb Api Person Combined Credits Response Example
  slug: tmdb-api-person-combined-credits-response-example
- key_count: 14
  name: Tmdb Api Person Details Response Example
  slug: tmdb-api-person-details-response-example
- key_count: 11
  name: Tmdb Api Person External Ids Response Example
  slug: tmdb-api-person-external-ids-response-example
- key_count: 2
  name: Tmdb Api Person Images Response Example
  slug: tmdb-api-person-images-response-example
- key_count: 14
  name: Tmdb Api Person Latest Id Response Example
  slug: tmdb-api-person-latest-id-response-example
- key_count: 3
  name: Tmdb Api Person Movie Credits Response Example
  slug: tmdb-api-person-movie-credits-response-example
- key_count: 4
  name: Tmdb Api Person Popular List Response Example
  slug: tmdb-api-person-popular-list-response-example
- key_count: 5
  name: Tmdb Api Person Tagged Images Response Example
  slug: tmdb-api-person-tagged-images-response-example
- key_count: 3
  name: Tmdb Api Person Tv Credits Response Example
  slug: tmdb-api-person-tv-credits-response-example
- key_count: 11
  name: Tmdb Api Review Details Response Example
  slug: tmdb-api-review-details-response-example
- key_count: 4
  name: Tmdb Api Search Collection Response Example
  slug: tmdb-api-search-collection-response-example
- key_count: 4
  name: Tmdb Api Search Company Response Example
  slug: tmdb-api-search-company-response-example
- key_count: 4
  name: Tmdb Api Search Keyword Response Example
  slug: tmdb-api-search-keyword-response-example
- key_count: 4
  name: Tmdb Api Search Movie Response Example
  slug: tmdb-api-search-movie-response-example
- key_count: 4
  name: Tmdb Api Search Multi Response Example
  slug: tmdb-api-search-multi-response-example
- key_count: 4
  name: Tmdb Api Search Person Response Example
  slug: tmdb-api-search-person-response-example
- key_count: 4
  name: Tmdb Api Search Tv Response Example
  slug: tmdb-api-search-tv-response-example
- key_count: 2
  name: Tmdb Api Translations Response Example
  slug: tmdb-api-translations-response-example
- key_count: 4
  name: Tmdb Api Trending All Response Example
  slug: tmdb-api-trending-all-response-example
- key_count: 4
  name: Tmdb Api Trending Movies Response Example
  slug: tmdb-api-trending-movies-response-example
- key_count: 4
  name: Tmdb Api Trending People Response Example
  slug: tmdb-api-trending-people-response-example
- key_count: 4
  name: Tmdb Api Trending Tv Response Example
  slug: tmdb-api-trending-tv-response-example
- key_count: 4
  name: Tmdb Api Tv Episode Account States Response Example
  slug: tmdb-api-tv-episode-account-states-response-example
- key_count: 2
  name: Tmdb Api Tv Episode Add Rating Response Example
  slug: tmdb-api-tv-episode-add-rating-response-example
- key_count: 1
  name: Tmdb Api Tv Episode Changes By Id Response Example
  slug: tmdb-api-tv-episode-changes-by-id-response-example
- key_count: 4
  name: Tmdb Api Tv Episode Credits Response Example
  slug: tmdb-api-tv-episode-credits-response-example
- key_count: 2
  name: Tmdb Api Tv Episode Delete Rating Response Example
  slug: tmdb-api-tv-episode-delete-rating-response-example
- key_count: 13
  name: Tmdb Api Tv Episode Details Response Example
  slug: tmdb-api-tv-episode-details-response-example
- key_count: 7
  name: Tmdb Api Tv Episode External Ids Response Example
  slug: tmdb-api-tv-episode-external-ids-response-example
- key_count: 8
  name: Tmdb Api Tv Episode Group Details Response Example
  slug: tmdb-api-tv-episode-group-details-response-example
- key_count: 2
  name: Tmdb Api Tv Episode Images Response Example
  slug: tmdb-api-tv-episode-images-response-example
- key_count: 2
  name: Tmdb Api Tv Episode Translations Response Example
  slug: tmdb-api-tv-episode-translations-response-example
- key_count: 2
  name: Tmdb Api Tv Episode Videos Response Example
  slug: tmdb-api-tv-episode-videos-response-example
- key_count: 2
  name: Tmdb Api Tv Season Account States Response Example
  slug: tmdb-api-tv-season-account-states-response-example
- key_count: 3
  name: Tmdb Api Tv Season Aggregate Credits Response Example
  slug: tmdb-api-tv-season-aggregate-credits-response-example
- key_count: 1
  name: Tmdb Api Tv Season Changes By Id Response Example
  slug: tmdb-api-tv-season-changes-by-id-response-example
- key_count: 3
  name: Tmdb Api Tv Season Credits Response Example
  slug: tmdb-api-tv-season-credits-response-example
- key_count: 10
  name: Tmdb Api Tv Season Details Response Example
  slug: tmdb-api-tv-season-details-response-example
- key_count: 6
  name: Tmdb Api Tv Season External Ids Response Example
  slug: tmdb-api-tv-season-external-ids-response-example
- key_count: 2
  name: Tmdb Api Tv Season Images Response Example
  slug: tmdb-api-tv-season-images-response-example
- key_count: 2
  name: Tmdb Api Tv Season Translations Response Example
  slug: tmdb-api-tv-season-translations-response-example
- key_count: 2
  name: Tmdb Api Tv Season Videos Response Example
  slug: tmdb-api-tv-season-videos-response-example
- key_count: 2
  name: Tmdb Api Tv Season Watch Providers Response Example
  slug: tmdb-api-tv-season-watch-providers-response-example
- key_count: 4
  name: Tmdb Api Tv Series Account States Response Example
  slug: tmdb-api-tv-series-account-states-response-example
- key_count: 2
  name: Tmdb Api Tv Series Add Rating Response Example
  slug: tmdb-api-tv-series-add-rating-response-example
- key_count: 3
  name: Tmdb Api Tv Series Aggregate Credits Response Example
  slug: tmdb-api-tv-series-aggregate-credits-response-example
- key_count: 4
  name: Tmdb Api Tv Series Airing Today List Response Example
  slug: tmdb-api-tv-series-airing-today-list-response-example
- key_count: 2
  name: Tmdb Api Tv Series Alternative Titles Response Example
  slug: tmdb-api-tv-series-alternative-titles-response-example
- key_count: 1
  name: Tmdb Api Tv Series Changes Response Example
  slug: tmdb-api-tv-series-changes-response-example
- key_count: 2
  name: Tmdb Api Tv Series Content Ratings Response Example
  slug: tmdb-api-tv-series-content-ratings-response-example
- key_count: 3
  name: Tmdb Api Tv Series Credits Response Example
  slug: tmdb-api-tv-series-credits-response-example
- key_count: 2
  name: Tmdb Api Tv Series Delete Rating Response Example
  slug: tmdb-api-tv-series-delete-rating-response-example
- key_count: 32
  name: Tmdb Api Tv Series Details Response Example
  slug: tmdb-api-tv-series-details-response-example
- key_count: 2
  name: Tmdb Api Tv Series Episode Groups Response Example
  slug: tmdb-api-tv-series-episode-groups-response-example
- key_count: 10
  name: Tmdb Api Tv Series External Ids Response Example
  slug: tmdb-api-tv-series-external-ids-response-example
- key_count: 4
  name: Tmdb Api Tv Series Images Response Example
  slug: tmdb-api-tv-series-images-response-example
- key_count: 2
  name: Tmdb Api Tv Series Keywords Response Example
  slug: tmdb-api-tv-series-keywords-response-example
- key_count: 32
  name: Tmdb Api Tv Series Latest Id Response Example
  slug: tmdb-api-tv-series-latest-id-response-example
- key_count: 4
  name: Tmdb Api Tv Series On The Air List Response Example
  slug: tmdb-api-tv-series-on-the-air-list-response-example
- key_count: 4
  name: Tmdb Api Tv Series Popular List Response Example
  slug: tmdb-api-tv-series-popular-list-response-example
- key_count: 4
  name: Tmdb Api Tv Series Recommendations Response Example
  slug: tmdb-api-tv-series-recommendations-response-example
- key_count: 5
  name: Tmdb Api Tv Series Reviews Response Example
  slug: tmdb-api-tv-series-reviews-response-example
- key_count: 2
  name: Tmdb Api Tv Series Screened Theatrically Response Example
  slug: tmdb-api-tv-series-screened-theatrically-response-example
- key_count: 4
  name: Tmdb Api Tv Series Similar Response Example
  slug: tmdb-api-tv-series-similar-response-example
- key_count: 4
  name: Tmdb Api Tv Series Top Rated List Response Example
  slug: tmdb-api-tv-series-top-rated-list-response-example
- key_count: 2
  name: Tmdb Api Tv Series Translations Response Example
  slug: tmdb-api-tv-series-translations-response-example
- key_count: 2
  name: Tmdb Api Tv Series Videos Response Example
  slug: tmdb-api-tv-series-videos-response-example
- key_count: 2
  name: Tmdb Api Tv Series Watch Providers Response Example
  slug: tmdb-api-tv-series-watch-providers-response-example
- key_count: 1
  name: Tmdb Api Watch Provider Tv List Response Example
  slug: tmdb-api-watch-provider-tv-list-response-example
- key_count: 1
  name: Tmdb Api Watch Providers Available Regions Response Example
  slug: tmdb-api-watch-providers-available-regions-response-example
- key_count: 1
  name: Tmdb Api Watch Providers Movie List Response Example
  slug: tmdb-api-watch-providers-movie-list-response-example
finops:
- name: Tmdb Finops
  service_category: Media + Entertainment Catalog
  slug: tmdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tmdb.png
json_schemas:
- name: AccountAddFavoriteResponse
  property_count: 2
  slug: tmdb-api-account-add-favorite-response
- name: AccountAddToWatchlistResponse
  property_count: 2
  slug: tmdb-api-account-add-to-watchlist-response
- name: AccountDetailsResponse
  property_count: 7
  slug: tmdb-api-account-details-response
- name: AccountFavoriteTvResponse
  property_count: 4
  slug: tmdb-api-account-favorite-tv-response
- name: AccountGetFavoritesResponse
  property_count: 4
  slug: tmdb-api-account-get-favorites-response
- name: AccountListsResponse
  property_count: 4
  slug: tmdb-api-account-lists-response
- name: AccountRatedMoviesResponse
  property_count: 4
  slug: tmdb-api-account-rated-movies-response
- name: AccountRatedTvEpisodesResponse
  property_count: 4
  slug: tmdb-api-account-rated-tv-episodes-response
- name: AccountRatedTvResponse
  property_count: 4
  slug: tmdb-api-account-rated-tv-response
- name: AccountWatchlistMoviesResponse
  property_count: 4
  slug: tmdb-api-account-watchlist-movies-response
- name: AccountWatchlistTvResponse
  property_count: 4
  slug: tmdb-api-account-watchlist-tv-response
- name: AlternativeNamesCopyResponse
  property_count: 2
  slug: tmdb-api-alternative-names-copy-response
- name: AuthenticationCreateGuestSessionResponse
  property_count: 3
  slug: tmdb-api-authentication-create-guest-session-response
- name: AuthenticationCreateRequestTokenResponse
  property_count: 3
  slug: tmdb-api-authentication-create-request-token-response
- name: AuthenticationCreateSessionFromLoginResponse
  property_count: 3
  slug: tmdb-api-authentication-create-session-from-login-response
- name: AuthenticationCreateSessionFromV4TokenResponse
  property_count: 2
  slug: tmdb-api-authentication-create-session-from-v4token-response
- name: AuthenticationCreateSessionResponse
  property_count: 2
  slug: tmdb-api-authentication-create-session-response
- name: AuthenticationDeleteSessionResponse
  property_count: 1
  slug: tmdb-api-authentication-delete-session-response
- name: AuthenticationValidateKeyResponse
  property_count: 3
  slug: tmdb-api-authentication-validate-key-response
- name: AuthenticationValidateKey401Response
  property_count: 3
  slug: tmdb-api-authentication-validate-key401response
- name: CertificationMovieListResponse
  property_count: 1
  slug: tmdb-api-certification-movie-list-response
- name: CertificationsTvListResponse
  property_count: 1
  slug: tmdb-api-certifications-tv-list-response
- name: ChangesMovieListResponse
  property_count: 4
  slug: tmdb-api-changes-movie-list-response
- name: ChangesPeopleListResponse
  property_count: 4
  slug: tmdb-api-changes-people-list-response
- name: ChangesTvListResponse
  property_count: 4
  slug: tmdb-api-changes-tv-list-response
- name: CollectionDetailsResponse
  property_count: 8
  slug: tmdb-api-collection-details-response
- name: CollectionImagesResponse
  property_count: 3
  slug: tmdb-api-collection-images-response
- name: CollectionTranslationsResponse
  property_count: 2
  slug: tmdb-api-collection-translations-response
- name: CompanyAlternativeNamesResponse
  property_count: 2
  slug: tmdb-api-company-alternative-names-response
- name: CompanyDetailsResponse
  property_count: 8
  slug: tmdb-api-company-details-response
- name: CompanyImagesResponse
  property_count: 2
  slug: tmdb-api-company-images-response
- name: ConfigurationDetailsResponse
  property_count: 2
  slug: tmdb-api-configuration-details-response
- name: CreditDetailsResponse
  property_count: 7
  slug: tmdb-api-credit-details-response
- name: DetailsCopyResponse
  property_count: 2
  slug: tmdb-api-details-copy-response
- name: DiscoverMovieResponse
  property_count: 4
  slug: tmdb-api-discover-movie-response
- name: DiscoverTvResponse
  property_count: 4
  slug: tmdb-api-discover-tv-response
- name: ErrorResponse
  property_count: 3
  slug: tmdb-api-error-response
- name: FindByIdResponse
  property_count: 5
  slug: tmdb-api-find-by-id-response
- name: GenreMovieListResponse
  property_count: 1
  slug: tmdb-api-genre-movie-list-response
- name: GenreTvListResponse
  property_count: 1
  slug: tmdb-api-genre-tv-list-response
- name: GuestSessionRatedMoviesResponse
  property_count: 4
  slug: tmdb-api-guest-session-rated-movies-response
- name: GuestSessionRatedTvEpisodesResponse
  property_count: 4
  slug: tmdb-api-guest-session-rated-tv-episodes-response
- name: GuestSessionRatedTvResponse
  property_count: 4
  slug: tmdb-api-guest-session-rated-tv-response
- name: KeywordDetailsResponse
  property_count: 2
  slug: tmdb-api-keyword-details-response
- name: KeywordMoviesResponse
  property_count: 5
  slug: tmdb-api-keyword-movies-response
- name: ListAddMovieResponse
  property_count: 2
  slug: tmdb-api-list-add-movie-response
- name: ListCheckItemStatusResponse
  property_count: 2
  slug: tmdb-api-list-check-item-status-response
- name: ListClearResponse
  property_count: 2
  slug: tmdb-api-list-clear-response
- name: ListCreateResponse
  property_count: 4
  slug: tmdb-api-list-create-response
- name: ListDeleteResponse
  property_count: 2
  slug: tmdb-api-list-delete-response
- name: ListDetailsResponse
  property_count: 9
  slug: tmdb-api-list-details-response
- name: ListRemoveMovieResponse
  property_count: 2
  slug: tmdb-api-list-remove-movie-response
- name: ListsCopyResponse
  property_count: 5
  slug: tmdb-api-lists-copy-response
- name: MovieAccountStatesResponse
  property_count: 4
  slug: tmdb-api-movie-account-states-response
- name: MovieAddRatingResponse
  property_count: 2
  slug: tmdb-api-movie-add-rating-response
- name: MovieAlternativeTitlesResponse
  property_count: 2
  slug: tmdb-api-movie-alternative-titles-response
- name: MovieChangesResponse
  property_count: 1
  slug: tmdb-api-movie-changes-response
- name: MovieCreditsResponse
  property_count: 3
  slug: tmdb-api-movie-credits-response
- name: MovieDeleteRatingResponse
  property_count: 2
  slug: tmdb-api-movie-delete-rating-response
- name: MovieDetailsResponse
  property_count: 26
  slug: tmdb-api-movie-details-response
- name: MovieExternalIdsResponse
  property_count: 6
  slug: tmdb-api-movie-external-ids-response
- name: MovieImagesResponse
  property_count: 4
  slug: tmdb-api-movie-images-response
- name: MovieKeywordsResponse
  property_count: 2
  slug: tmdb-api-movie-keywords-response
- name: MovieLatestIdResponse
  property_count: 25
  slug: tmdb-api-movie-latest-id-response
- name: MovieListsResponse
  property_count: 5
  slug: tmdb-api-movie-lists-response
- name: MovieNowPlayingListResponse
  property_count: 5
  slug: tmdb-api-movie-now-playing-list-response
- name: MoviePopularListResponse
  property_count: 4
  slug: tmdb-api-movie-popular-list-response
- name: MovieRecommendationsResponse
  property_count: 0
  slug: tmdb-api-movie-recommendations-response
- name: MovieReleaseDatesResponse
  property_count: 2
  slug: tmdb-api-movie-release-dates-response
- name: MovieReviewsResponse
  property_count: 5
  slug: tmdb-api-movie-reviews-response
- name: MovieSimilarResponse
  property_count: 4
  slug: tmdb-api-movie-similar-response
- name: MovieTopRatedListResponse
  property_count: 4
  slug: tmdb-api-movie-top-rated-list-response
- name: MovieTranslationsResponse
  property_count: 2
  slug: tmdb-api-movie-translations-response
- name: MovieUpcomingListResponse
  property_count: 5
  slug: tmdb-api-movie-upcoming-list-response
- name: MovieVideosResponse
  property_count: 2
  slug: tmdb-api-movie-videos-response
- name: MovieWatchProvidersResponse
  property_count: 2
  slug: tmdb-api-movie-watch-providers-response
- name: NetworkDetailsResponse
  property_count: 6
  slug: tmdb-api-network-details-response
- name: PersonChangesResponse
  property_count: 1
  slug: tmdb-api-person-changes-response
- name: PersonCombinedCreditsResponse
  property_count: 3
  slug: tmdb-api-person-combined-credits-response
- name: PersonDetailsResponse
  property_count: 14
  slug: tmdb-api-person-details-response
- name: PersonExternalIdsResponse
  property_count: 11
  slug: tmdb-api-person-external-ids-response
- name: PersonImagesResponse
  property_count: 2
  slug: tmdb-api-person-images-response
- name: PersonLatestIdResponse
  property_count: 14
  slug: tmdb-api-person-latest-id-response
- name: PersonMovieCreditsResponse
  property_count: 3
  slug: tmdb-api-person-movie-credits-response
- name: PersonPopularListResponse
  property_count: 4
  slug: tmdb-api-person-popular-list-response
- name: PersonTaggedImagesResponse
  property_count: 5
  slug: tmdb-api-person-tagged-images-response
- name: PersonTvCreditsResponse
  property_count: 3
  slug: tmdb-api-person-tv-credits-response
- name: ReviewDetailsResponse
  property_count: 11
  slug: tmdb-api-review-details-response
- name: SearchCollectionResponse
  property_count: 4
  slug: tmdb-api-search-collection-response
- name: SearchCompanyResponse
  property_count: 4
  slug: tmdb-api-search-company-response
- name: SearchKeywordResponse
  property_count: 4
  slug: tmdb-api-search-keyword-response
- name: SearchMovieResponse
  property_count: 4
  slug: tmdb-api-search-movie-response
- name: SearchMultiResponse
  property_count: 4
  slug: tmdb-api-search-multi-response
- name: SearchPersonResponse
  property_count: 4
  slug: tmdb-api-search-person-response
- name: SearchTvResponse
  property_count: 4
  slug: tmdb-api-search-tv-response
- name: TranslationsResponse
  property_count: 2
  slug: tmdb-api-translations-response
- name: TrendingAllResponse
  property_count: 4
  slug: tmdb-api-trending-all-response
- name: TrendingMoviesResponse
  property_count: 4
  slug: tmdb-api-trending-movies-response
- name: TrendingPeopleResponse
  property_count: 4
  slug: tmdb-api-trending-people-response
- name: TrendingTvResponse
  property_count: 4
  slug: tmdb-api-trending-tv-response
- name: TvEpisodeAccountStatesResponse
  property_count: 4
  slug: tmdb-api-tv-episode-account-states-response
- name: TvEpisodeAddRatingResponse
  property_count: 2
  slug: tmdb-api-tv-episode-add-rating-response
- name: TvEpisodeChangesByIdResponse
  property_count: 1
  slug: tmdb-api-tv-episode-changes-by-id-response
- name: TvEpisodeCreditsResponse
  property_count: 4
  slug: tmdb-api-tv-episode-credits-response
- name: TvEpisodeDeleteRatingResponse
  property_count: 2
  slug: tmdb-api-tv-episode-delete-rating-response
- name: TvEpisodeDetailsResponse
  property_count: 13
  slug: tmdb-api-tv-episode-details-response
- name: TvEpisodeExternalIdsResponse
  property_count: 7
  slug: tmdb-api-tv-episode-external-ids-response
- name: TvEpisodeGroupDetailsResponse
  property_count: 8
  slug: tmdb-api-tv-episode-group-details-response
- name: TvEpisodeImagesResponse
  property_count: 2
  slug: tmdb-api-tv-episode-images-response
- name: TvEpisodeTranslationsResponse
  property_count: 2
  slug: tmdb-api-tv-episode-translations-response
- name: TvEpisodeVideosResponse
  property_count: 2
  slug: tmdb-api-tv-episode-videos-response
- name: TvSeasonAccountStatesResponse
  property_count: 2
  slug: tmdb-api-tv-season-account-states-response
- name: TvSeasonAggregateCreditsResponse
  property_count: 3
  slug: tmdb-api-tv-season-aggregate-credits-response
- name: TvSeasonChangesByIdResponse
  property_count: 1
  slug: tmdb-api-tv-season-changes-by-id-response
- name: TvSeasonCreditsResponse
  property_count: 3
  slug: tmdb-api-tv-season-credits-response
- name: TvSeasonDetailsResponse
  property_count: 10
  slug: tmdb-api-tv-season-details-response
- name: TvSeasonExternalIdsResponse
  property_count: 6
  slug: tmdb-api-tv-season-external-ids-response
- name: TvSeasonImagesResponse
  property_count: 2
  slug: tmdb-api-tv-season-images-response
- name: TvSeasonTranslationsResponse
  property_count: 2
  slug: tmdb-api-tv-season-translations-response
- name: TvSeasonVideosResponse
  property_count: 2
  slug: tmdb-api-tv-season-videos-response
- name: TvSeasonWatchProvidersResponse
  property_count: 2
  slug: tmdb-api-tv-season-watch-providers-response
- name: TvSeriesAccountStatesResponse
  property_count: 4
  slug: tmdb-api-tv-series-account-states-response
- name: TvSeriesAddRatingResponse
  property_count: 2
  slug: tmdb-api-tv-series-add-rating-response
- name: TvSeriesAggregateCreditsResponse
  property_count: 3
  slug: tmdb-api-tv-series-aggregate-credits-response
- name: TvSeriesAiringTodayListResponse
  property_count: 4
  slug: tmdb-api-tv-series-airing-today-list-response
- name: TvSeriesAlternativeTitlesResponse
  property_count: 2
  slug: tmdb-api-tv-series-alternative-titles-response
- name: TvSeriesChangesResponse
  property_count: 1
  slug: tmdb-api-tv-series-changes-response
- name: TvSeriesContentRatingsResponse
  property_count: 2
  slug: tmdb-api-tv-series-content-ratings-response
- name: TvSeriesCreditsResponse
  property_count: 3
  slug: tmdb-api-tv-series-credits-response
- name: TvSeriesDeleteRatingResponse
  property_count: 2
  slug: tmdb-api-tv-series-delete-rating-response
- name: TvSeriesDetailsResponse
  property_count: 32
  slug: tmdb-api-tv-series-details-response
- name: TvSeriesEpisodeGroupsResponse
  property_count: 2
  slug: tmdb-api-tv-series-episode-groups-response
- name: TvSeriesExternalIdsResponse
  property_count: 10
  slug: tmdb-api-tv-series-external-ids-response
- name: TvSeriesImagesResponse
  property_count: 4
  slug: tmdb-api-tv-series-images-response
- name: TvSeriesKeywordsResponse
  property_count: 2
  slug: tmdb-api-tv-series-keywords-response
- name: TvSeriesLatestIdResponse
  property_count: 32
  slug: tmdb-api-tv-series-latest-id-response
- name: TvSeriesOnTheAirListResponse
  property_count: 4
  slug: tmdb-api-tv-series-on-the-air-list-response
- name: TvSeriesPopularListResponse
  property_count: 4
  slug: tmdb-api-tv-series-popular-list-response
- name: TvSeriesRecommendationsResponse
  property_count: 4
  slug: tmdb-api-tv-series-recommendations-response
- name: TvSeriesReviewsResponse
  property_count: 5
  slug: tmdb-api-tv-series-reviews-response
- name: TvSeriesScreenedTheatricallyResponse
  property_count: 2
  slug: tmdb-api-tv-series-screened-theatrically-response
- name: TvSeriesSimilarResponse
  property_count: 4
  slug: tmdb-api-tv-series-similar-response
- name: TvSeriesTopRatedListResponse
  property_count: 4
  slug: tmdb-api-tv-series-top-rated-list-response
- name: TvSeriesTranslationsResponse
  property_count: 2
  slug: tmdb-api-tv-series-translations-response
- name: TvSeriesVideosResponse
  property_count: 2
  slug: tmdb-api-tv-series-videos-response
- name: TvSeriesWatchProvidersResponse
  property_count: 2
  slug: tmdb-api-tv-series-watch-providers-response
- name: WatchProviderTvListResponse
  property_count: 1
  slug: tmdb-api-watch-provider-tv-list-response
- name: WatchProvidersAvailableRegionsResponse
  property_count: 1
  slug: tmdb-api-watch-providers-available-regions-response
- name: WatchProvidersMovieListResponse
  property_count: 1
  slug: tmdb-api-watch-providers-movie-list-response
json_structures:
- name: Tmdb Api Account Add Favorite Response Structure
  property_count: 2
  slug: tmdb-api-account-add-favorite-response-structure
- name: Tmdb Api Account Add To Watchlist Response Structure
  property_count: 2
  slug: tmdb-api-account-add-to-watchlist-response-structure
- name: Tmdb Api Account Details Response Structure
  property_count: 7
  slug: tmdb-api-account-details-response-structure
- name: Tmdb Api Account Favorite Tv Response Structure
  property_count: 4
  slug: tmdb-api-account-favorite-tv-response-structure
- name: Tmdb Api Account Get Favorites Response Structure
  property_count: 4
  slug: tmdb-api-account-get-favorites-response-structure
- name: Tmdb Api Account Lists Response Structure
  property_count: 4
  slug: tmdb-api-account-lists-response-structure
- name: Tmdb Api Account Rated Movies Response Structure
  property_count: 4
  slug: tmdb-api-account-rated-movies-response-structure
- name: Tmdb Api Account Rated Tv Episodes Response Structure
  property_count: 4
  slug: tmdb-api-account-rated-tv-episodes-response-structure
- name: Tmdb Api Account Rated Tv Response Structure
  property_count: 4
  slug: tmdb-api-account-rated-tv-response-structure
- name: Tmdb Api Account Watchlist Movies Response Structure
  property_count: 4
  slug: tmdb-api-account-watchlist-movies-response-structure
- name: Tmdb Api Account Watchlist Tv Response Structure
  property_count: 4
  slug: tmdb-api-account-watchlist-tv-response-structure
- name: Tmdb Api Alternative Names Copy Response Structure
  property_count: 2
  slug: tmdb-api-alternative-names-copy-response-structure
- name: Tmdb Api Authentication Create Guest Session Response Structure
  property_count: 3
  slug: tmdb-api-authentication-create-guest-session-response-structure
- name: Tmdb Api Authentication Create Request Token Response Structure
  property_count: 3
  slug: tmdb-api-authentication-create-request-token-response-structure
- name: Tmdb Api Authentication Create Session From Login Response Structure
  property_count: 3
  slug: tmdb-api-authentication-create-session-from-login-response-structure
- name: Tmdb Api Authentication Create Session From V4Token Response Structure
  property_count: 2
  slug: tmdb-api-authentication-create-session-from-v4token-response-structure
- name: Tmdb Api Authentication Create Session Response Structure
  property_count: 2
  slug: tmdb-api-authentication-create-session-response-structure
- name: Tmdb Api Authentication Delete Session Response Structure
  property_count: 1
  slug: tmdb-api-authentication-delete-session-response-structure
- name: Tmdb Api Authentication Validate Key Response Structure
  property_count: 3
  slug: tmdb-api-authentication-validate-key-response-structure
- name: Tmdb Api Authentication Validate Key401Response Structure
  property_count: 3
  slug: tmdb-api-authentication-validate-key401response-structure
- name: Tmdb Api Certification Movie List Response Structure
  property_count: 1
  slug: tmdb-api-certification-movie-list-response-structure
- name: Tmdb Api Certifications Tv List Response Structure
  property_count: 1
  slug: tmdb-api-certifications-tv-list-response-structure
- name: Tmdb Api Changes Movie List Response Structure
  property_count: 4
  slug: tmdb-api-changes-movie-list-response-structure
- name: Tmdb Api Changes People List Response Structure
  property_count: 4
  slug: tmdb-api-changes-people-list-response-structure
- name: Tmdb Api Changes Tv List Response Structure
  property_count: 4
  slug: tmdb-api-changes-tv-list-response-structure
- name: Tmdb Api Collection Details Response Structure
  property_count: 8
  slug: tmdb-api-collection-details-response-structure
- name: Tmdb Api Collection Images Response Structure
  property_count: 3
  slug: tmdb-api-collection-images-response-structure
- name: Tmdb Api Collection Translations Response Structure
  property_count: 2
  slug: tmdb-api-collection-translations-response-structure
- name: Tmdb Api Company Alternative Names Response Structure
  property_count: 2
  slug: tmdb-api-company-alternative-names-response-structure
- name: Tmdb Api Company Details Response Structure
  property_count: 8
  slug: tmdb-api-company-details-response-structure
- name: Tmdb Api Company Images Response Structure
  property_count: 2
  slug: tmdb-api-company-images-response-structure
- name: Tmdb Api Configuration Details Response Structure
  property_count: 2
  slug: tmdb-api-configuration-details-response-structure
- name: Tmdb Api Credit Details Response Structure
  property_count: 7
  slug: tmdb-api-credit-details-response-structure
- name: Tmdb Api Details Copy Response Structure
  property_count: 2
  slug: tmdb-api-details-copy-response-structure
- name: Tmdb Api Discover Movie Response Structure
  property_count: 4
  slug: tmdb-api-discover-movie-response-structure
- name: Tmdb Api Discover Tv Response Structure
  property_count: 4
  slug: tmdb-api-discover-tv-response-structure
- name: Tmdb Api Error Response Structure
  property_count: 3
  slug: tmdb-api-error-response-structure
- name: Tmdb Api Find By Id Response Structure
  property_count: 5
  slug: tmdb-api-find-by-id-response-structure
- name: Tmdb Api Genre Movie List Response Structure
  property_count: 1
  slug: tmdb-api-genre-movie-list-response-structure
- name: Tmdb Api Genre Tv List Response Structure
  property_count: 1
  slug: tmdb-api-genre-tv-list-response-structure
- name: Tmdb Api Guest Session Rated Movies Response Structure
  property_count: 4
  slug: tmdb-api-guest-session-rated-movies-response-structure
- name: Tmdb Api Guest Session Rated Tv Episodes Response Structure
  property_count: 4
  slug: tmdb-api-guest-session-rated-tv-episodes-response-structure
- name: Tmdb Api Guest Session Rated Tv Response Structure
  property_count: 4
  slug: tmdb-api-guest-session-rated-tv-response-structure
- name: Tmdb Api Keyword Details Response Structure
  property_count: 2
  slug: tmdb-api-keyword-details-response-structure
- name: Tmdb Api Keyword Movies Response Structure
  property_count: 5
  slug: tmdb-api-keyword-movies-response-structure
- name: Tmdb Api List Add Movie Response Structure
  property_count: 2
  slug: tmdb-api-list-add-movie-response-structure
- name: Tmdb Api List Check Item Status Response Structure
  property_count: 2
  slug: tmdb-api-list-check-item-status-response-structure
- name: Tmdb Api List Clear Response Structure
  property_count: 2
  slug: tmdb-api-list-clear-response-structure
- name: Tmdb Api List Create Response Structure
  property_count: 4
  slug: tmdb-api-list-create-response-structure
- name: Tmdb Api List Delete Response Structure
  property_count: 2
  slug: tmdb-api-list-delete-response-structure
- name: Tmdb Api List Details Response Structure
  property_count: 9
  slug: tmdb-api-list-details-response-structure
- name: Tmdb Api List Remove Movie Response Structure
  property_count: 2
  slug: tmdb-api-list-remove-movie-response-structure
- name: Tmdb Api Lists Copy Response Structure
  property_count: 5
  slug: tmdb-api-lists-copy-response-structure
- name: Tmdb Api Movie Account States Response Structure
  property_count: 4
  slug: tmdb-api-movie-account-states-response-structure
- name: Tmdb Api Movie Add Rating Response Structure
  property_count: 2
  slug: tmdb-api-movie-add-rating-response-structure
- name: Tmdb Api Movie Alternative Titles Response Structure
  property_count: 2
  slug: tmdb-api-movie-alternative-titles-response-structure
- name: Tmdb Api Movie Changes Response Structure
  property_count: 1
  slug: tmdb-api-movie-changes-response-structure
- name: Tmdb Api Movie Credits Response Structure
  property_count: 3
  slug: tmdb-api-movie-credits-response-structure
- name: Tmdb Api Movie Delete Rating Response Structure
  property_count: 2
  slug: tmdb-api-movie-delete-rating-response-structure
- name: Tmdb Api Movie Details Response Structure
  property_count: 26
  slug: tmdb-api-movie-details-response-structure
- name: Tmdb Api Movie External Ids Response Structure
  property_count: 6
  slug: tmdb-api-movie-external-ids-response-structure
- name: Tmdb Api Movie Images Response Structure
  property_count: 4
  slug: tmdb-api-movie-images-response-structure
- name: Tmdb Api Movie Keywords Response Structure
  property_count: 2
  slug: tmdb-api-movie-keywords-response-structure
- name: Tmdb Api Movie Latest Id Response Structure
  property_count: 25
  slug: tmdb-api-movie-latest-id-response-structure
- name: Tmdb Api Movie Lists Response Structure
  property_count: 5
  slug: tmdb-api-movie-lists-response-structure
- name: Tmdb Api Movie Now Playing List Response Structure
  property_count: 5
  slug: tmdb-api-movie-now-playing-list-response-structure
- name: Tmdb Api Movie Popular List Response Structure
  property_count: 4
  slug: tmdb-api-movie-popular-list-response-structure
- name: Tmdb Api Movie Recommendations Response Structure
  property_count: 0
  slug: tmdb-api-movie-recommendations-response-structure
- name: Tmdb Api Movie Release Dates Response Structure
  property_count: 2
  slug: tmdb-api-movie-release-dates-response-structure
- name: Tmdb Api Movie Reviews Response Structure
  property_count: 5
  slug: tmdb-api-movie-reviews-response-structure
- name: Tmdb Api Movie Similar Response Structure
  property_count: 4
  slug: tmdb-api-movie-similar-response-structure
- name: Tmdb Api Movie Top Rated List Response Structure
  property_count: 4
  slug: tmdb-api-movie-top-rated-list-response-structure
- name: Tmdb Api Movie Translations Response Structure
  property_count: 2
  slug: tmdb-api-movie-translations-response-structure
- name: Tmdb Api Movie Upcoming List Response Structure
  property_count: 5
  slug: tmdb-api-movie-upcoming-list-response-structure
- name: Tmdb Api Movie Videos Response Structure
  property_count: 2
  slug: tmdb-api-movie-videos-response-structure
- name: Tmdb Api Movie Watch Providers Response Structure
  property_count: 2
  slug: tmdb-api-movie-watch-providers-response-structure
- name: Tmdb Api Network Details Response Structure
  property_count: 6
  slug: tmdb-api-network-details-response-structure
- name: Tmdb Api Person Changes Response Structure
  property_count: 1
  slug: tmdb-api-person-changes-response-structure
- name: Tmdb Api Person Combined Credits Response Structure
  property_count: 3
  slug: tmdb-api-person-combined-credits-response-structure
- name: Tmdb Api Person Details Response Structure
  property_count: 14
  slug: tmdb-api-person-details-response-structure
- name: Tmdb Api Person External Ids Response Structure
  property_count: 11
  slug: tmdb-api-person-external-ids-response-structure
- name: Tmdb Api Person Images Response Structure
  property_count: 2
  slug: tmdb-api-person-images-response-structure
- name: Tmdb Api Person Latest Id Response Structure
  property_count: 14
  slug: tmdb-api-person-latest-id-response-structure
- name: Tmdb Api Person Movie Credits Response Structure
  property_count: 3
  slug: tmdb-api-person-movie-credits-response-structure
- name: Tmdb Api Person Popular List Response Structure
  property_count: 4
  slug: tmdb-api-person-popular-list-response-structure
- name: Tmdb Api Person Tagged Images Response Structure
  property_count: 5
  slug: tmdb-api-person-tagged-images-response-structure
- name: Tmdb Api Person Tv Credits Response Structure
  property_count: 3
  slug: tmdb-api-person-tv-credits-response-structure
- name: Tmdb Api Review Details Response Structure
  property_count: 11
  slug: tmdb-api-review-details-response-structure
- name: Tmdb Api Search Collection Response Structure
  property_count: 4
  slug: tmdb-api-search-collection-response-structure
- name: Tmdb Api Search Company Response Structure
  property_count: 4
  slug: tmdb-api-search-company-response-structure
- name: Tmdb Api Search Keyword Response Structure
  property_count: 4
  slug: tmdb-api-search-keyword-response-structure
- name: Tmdb Api Search Movie Response Structure
  property_count: 4
  slug: tmdb-api-search-movie-response-structure
- name: Tmdb Api Search Multi Response Structure
  property_count: 4
  slug: tmdb-api-search-multi-response-structure
- name: Tmdb Api Search Person Response Structure
  property_count: 4
  slug: tmdb-api-search-person-response-structure
- name: Tmdb Api Search Tv Response Structure
  property_count: 4
  slug: tmdb-api-search-tv-response-structure
- name: Tmdb Api Translations Response Structure
  property_count: 2
  slug: tmdb-api-translations-response-structure
- name: Tmdb Api Trending All Response Structure
  property_count: 4
  slug: tmdb-api-trending-all-response-structure
- name: Tmdb Api Trending Movies Response Structure
  property_count: 4
  slug: tmdb-api-trending-movies-response-structure
- name: Tmdb Api Trending People Response Structure
  property_count: 4
  slug: tmdb-api-trending-people-response-structure
- name: Tmdb Api Trending Tv Response Structure
  property_count: 4
  slug: tmdb-api-trending-tv-response-structure
- name: Tmdb Api Tv Episode Account States Response Structure
  property_count: 4
  slug: tmdb-api-tv-episode-account-states-response-structure
- name: Tmdb Api Tv Episode Add Rating Response Structure
  property_count: 2
  slug: tmdb-api-tv-episode-add-rating-response-structure
- name: Tmdb Api Tv Episode Changes By Id Response Structure
  property_count: 1
  slug: tmdb-api-tv-episode-changes-by-id-response-structure
- name: Tmdb Api Tv Episode Credits Response Structure
  property_count: 4
  slug: tmdb-api-tv-episode-credits-response-structure
- name: Tmdb Api Tv Episode Delete Rating Response Structure
  property_count: 2
  slug: tmdb-api-tv-episode-delete-rating-response-structure
- name: Tmdb Api Tv Episode Details Response Structure
  property_count: 13
  slug: tmdb-api-tv-episode-details-response-structure
- name: Tmdb Api Tv Episode External Ids Response Structure
  property_count: 7
  slug: tmdb-api-tv-episode-external-ids-response-structure
- name: Tmdb Api Tv Episode Group Details Response Structure
  property_count: 8
  slug: tmdb-api-tv-episode-group-details-response-structure
- name: Tmdb Api Tv Episode Images Response Structure
  property_count: 2
  slug: tmdb-api-tv-episode-images-response-structure
- name: Tmdb Api Tv Episode Translations Response Structure
  property_count: 2
  slug: tmdb-api-tv-episode-translations-response-structure
- name: Tmdb Api Tv Episode Videos Response Structure
  property_count: 2
  slug: tmdb-api-tv-episode-videos-response-structure
- name: Tmdb Api Tv Season Account States Response Structure
  property_count: 2
  slug: tmdb-api-tv-season-account-states-response-structure
- name: Tmdb Api Tv Season Aggregate Credits Response Structure
  property_count: 3
  slug: tmdb-api-tv-season-aggregate-credits-response-structure
- name: Tmdb Api Tv Season Changes By Id Response Structure
  property_count: 1
  slug: tmdb-api-tv-season-changes-by-id-response-structure
- name: Tmdb Api Tv Season Credits Response Structure
  property_count: 3
  slug: tmdb-api-tv-season-credits-response-structure
- name: Tmdb Api Tv Season Details Response Structure
  property_count: 10
  slug: tmdb-api-tv-season-details-response-structure
- name: Tmdb Api Tv Season External Ids Response Structure
  property_count: 6
  slug: tmdb-api-tv-season-external-ids-response-structure
- name: Tmdb Api Tv Season Images Response Structure
  property_count: 2
  slug: tmdb-api-tv-season-images-response-structure
- name: Tmdb Api Tv Season Translations Response Structure
  property_count: 2
  slug: tmdb-api-tv-season-translations-response-structure
- name: Tmdb Api Tv Season Videos Response Structure
  property_count: 2
  slug: tmdb-api-tv-season-videos-response-structure
- name: Tmdb Api Tv Season Watch Providers Response Structure
  property_count: 2
  slug: tmdb-api-tv-season-watch-providers-response-structure
- name: Tmdb Api Tv Series Account States Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-account-states-response-structure
- name: Tmdb Api Tv Series Add Rating Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-add-rating-response-structure
- name: Tmdb Api Tv Series Aggregate Credits Response Structure
  property_count: 3
  slug: tmdb-api-tv-series-aggregate-credits-response-structure
- name: Tmdb Api Tv Series Airing Today List Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-airing-today-list-response-structure
- name: Tmdb Api Tv Series Alternative Titles Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-alternative-titles-response-structure
- name: Tmdb Api Tv Series Changes Response Structure
  property_count: 1
  slug: tmdb-api-tv-series-changes-response-structure
- name: Tmdb Api Tv Series Content Ratings Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-content-ratings-response-structure
- name: Tmdb Api Tv Series Credits Response Structure
  property_count: 3
  slug: tmdb-api-tv-series-credits-response-structure
- name: Tmdb Api Tv Series Delete Rating Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-delete-rating-response-structure
- name: Tmdb Api Tv Series Details Response Structure
  property_count: 32
  slug: tmdb-api-tv-series-details-response-structure
- name: Tmdb Api Tv Series Episode Groups Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-episode-groups-response-structure
- name: Tmdb Api Tv Series External Ids Response Structure
  property_count: 10
  slug: tmdb-api-tv-series-external-ids-response-structure
- name: Tmdb Api Tv Series Images Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-images-response-structure
- name: Tmdb Api Tv Series Keywords Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-keywords-response-structure
- name: Tmdb Api Tv Series Latest Id Response Structure
  property_count: 32
  slug: tmdb-api-tv-series-latest-id-response-structure
- name: Tmdb Api Tv Series On The Air List Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-on-the-air-list-response-structure
- name: Tmdb Api Tv Series Popular List Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-popular-list-response-structure
- name: Tmdb Api Tv Series Recommendations Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-recommendations-response-structure
- name: Tmdb Api Tv Series Reviews Response Structure
  property_count: 5
  slug: tmdb-api-tv-series-reviews-response-structure
- name: Tmdb Api Tv Series Screened Theatrically Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-screened-theatrically-response-structure
- name: Tmdb Api Tv Series Similar Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-similar-response-structure
- name: Tmdb Api Tv Series Top Rated List Response Structure
  property_count: 4
  slug: tmdb-api-tv-series-top-rated-list-response-structure
- name: Tmdb Api Tv Series Translations Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-translations-response-structure
- name: Tmdb Api Tv Series Videos Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-videos-response-structure
- name: Tmdb Api Tv Series Watch Providers Response Structure
  property_count: 2
  slug: tmdb-api-tv-series-watch-providers-response-structure
- name: Tmdb Api Watch Provider Tv List Response Structure
  property_count: 1
  slug: tmdb-api-watch-provider-tv-list-response-structure
- name: Tmdb Api Watch Providers Available Regions Response Structure
  property_count: 1
  slug: tmdb-api-watch-providers-available-regions-response-structure
- name: Tmdb Api Watch Providers Movie List Response Structure
  property_count: 1
  slug: tmdb-api-watch-providers-movie-list-response-structure
jsonld:
- class_count: 149
  name: Tmdb Context
  property_count: 324
  slug: tmdb-context
layout: provider
modified: '2026-05-30'
name: The Movie Database
nav: Providers
network: true
overview: 'The Movie Database publishes 1 API on the [APIs.io](https://apis.io/) network: TMDB API. Tagged areas include Catalog, Discovery, Entertainment, Images, and Media.


  The The Movie Database catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  The Movie Database''s developer surface includes documentation, signup flow, authentication, support, tooling, and 29 more developer resources.'
plans:
- name: Tmdb Plans Pricing
  plan_count: 2
  slug: tmdb-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 3
  name: Tmdb Rate Limits
  slug: tmdb-rate-limits
rules:
- name: The Movie Database API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: tmdb-jsonschema-spectral-rules
- name: The Movie Database API Rules
  rule_count: 42
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 22
  slug: tmdb-rules
score:
  band: strong
  composite: 56.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.5
    developer_ergonomics: 39.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 56.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tmdb/refs/heads/main/screenshots/tmdb-2026-06-20T195425.png
security:
- kind: domain-security
  name: Tmdb Domain Security
  slug: tmdb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tmdb
tags:
- Catalog
- Discovery
- Entertainment
- Images
- Media
- Metadata
- Movies
- People
- Recommendations
- Reviews
- Search
- Streaming
- Trending
- TV
- Video
- Watch Providers
website: https://www.themoviedb.org
---
