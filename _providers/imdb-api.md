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
  name: Imdb Api Agentic Access
  operation_count: 37
  slug: imdb-api-agentic-access
  summary_line: 37 operations
api_count: 6
apis:
- description: Wikipedia, external sites, reviews, FAQ and other ancillary data.
  name: IMDb-API External API
  slug: imdb-api-external-api
- description: Curated and aggregated lists (Top 250, Most Popular, In Theaters, Coming Soon, Box Office).
  name: IMDb-API Lists API
  slug: imdb-api-lists-api
- description: People (actors, directors, writers) information and awards.
  name: IMDb-API Name API
  slug: imdb-api-name-api
- description: Free-text and faceted search across titles, names, companies and keywords.
  name: IMDb-API Search API
  slug: imdb-api-search-api
- description: Movie and series metadata, posters, images, trailers, cast, ratings.
  name: IMDb-API Title API
  slug: imdb-api-title-api
- description: Image utilities and account usage.
  name: IMDb-API Tools API
  slug: imdb-api-tools-api
artifact_total: 58
collections:
- collection_type: open
  name: IMDb-API (TV-API)
  slug: open-imdb-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imdb-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imdb-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imdb-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://tv-api.com/
- group: company
  title: ''
  type: LegacyWebsite
  url: https://imdb-api.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tv-api.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://tv-api.com/Identity/Account/Register
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IMDb-API
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/IMDb-API/IMDbApiLib
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/IMDb-API/IMDbApiClient
- group: build
  title: ''
  type: SDKs
  url: https://github.com/IMDb-API/IMDbApiLib
- group: build
  title: ''
  type: Client
  url: https://github.com/IMDb-API/IMDbApiClient
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: SpectralRules
  url: rules/imdb-api-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/imdb-api-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/imdb-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imdb-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imdb-api-finops.yml
- group: build
  title: ''
  type: Tools
  url: ''
created: '2026-05-28'
description: Community web service (operated under the IMDb-API / TV-API brand) providing movie, TV series and cast information in JSON. Aggregates data from IMDb, TheMovieDb, Wikipedia, Rotten Tomatoes, Metacritic, TheTVDB, FilmAffinity and YouTube. Originally hosted at imdb-api.com and migrated to tv-api.com. Operated by the IMDb-API GitHub user (open source C# client library and Windows client app). NOT an official IMDb / Amazon product — IMDb itself does not expose a public API; community scrapers such as this one (alongside OMDb, TMDB and Apify's IMDb scraper) fill the gap.
examples:
- key_count: 3
  name: Imdb Api Fullcast Example
  slug: imdb-api-fullcast-example
- key_count: 3
  name: Imdb Api Ratings Example
  slug: imdb-api-ratings-example
- key_count: 3
  name: Imdb Api Search Example
  slug: imdb-api-search-example
- key_count: 3
  name: Imdb Api Title Example
  slug: imdb-api-title-example
- key_count: 3
  name: Imdb Api Top250Movies Example
  slug: imdb-api-top250movies-example
- key_count: 3
  name: Imdb Api Usage Example
  slug: imdb-api-usage-example
features:
- description: Full movie / series / episode metadata by IMDb tt-id.
  name: Title metadata
- description: IMDb, Metacritic, Rotten Tomatoes, TMDB and FilmAffinity scores in a single response.
  name: Aggregated ratings
- description: Directors, writers, actors and other crew with IMDb nm-ids.
  name: Full cast and crew
- description: Title, movie, series, name, episode, company and keyword search; plus faceted advanced search.
  name: Search
- description: Top 250 movies and TV, Most Popular, In Theaters, Coming Soon, Weekend & All-Time Box Office.
  name: Curated lists
- description: Posters, image galleries, trailers and YouTube trailer URLs.
  name: Media assets
- description: Cross-platform identifiers (Netflix, FilmAffinity, TheTVDB) and Wikipedia plot summaries.
  name: External links
- description: User reviews and Metacritic critic reviews.
  name: Reviews
- description: Server-side resize for arbitrary URLs and preset-token poster resizing.
  name: Image utilities
- description: Per-key daily quota consumption via /API/Usage.
  name: Usage telemetry
finops:
- name: Imdb Api Finops
  service_category: ''
  slug: imdb-api-finops
image: https://tv-api.com/images/original/Apple-TV-Plus-Logo.png
integrations:
- description: Primary source of title and name ids.
  name: IMDb
- description: Source of secondary ratings and additional metadata.
  name: TheMovieDb (TMDB)
- description: Critic and audience scores.
  name: Rotten Tomatoes
- description: Metascore and critic reviews.
  name: Metacritic
- description: Community ratings.
  name: FilmAffinity
- description: External TV id linkage.
  name: TheTVDB
- description: Plot summaries and PlotLocal in multiple languages.
  name: Wikipedia
- description: Trailer video resolution.
  name: YouTube
- description: Alternative IMDb data path documented in the broader ecosystem.
  name: Apify
- description: Adjacent community IMDb wrapper consumers often compare.
  name: OMDb API
json_schemas:
- name: Name
  property_count: 11
  slug: imdb-api-name
- name: Rating
  property_count: 11
  slug: imdb-api-rating
- name: SearchResult
  property_count: 5
  slug: imdb-api-search-result
- name: Title
  property_count: 22
  slug: imdb-api-title
- name: Usage
  property_count: 3
  slug: imdb-api-usage
json_structures:
- name: Imdb Api Name Structure
  property_count: 0
  slug: imdb-api-name-structure
- name: Imdb Api Rating Structure
  property_count: 0
  slug: imdb-api-rating-structure
- name: Imdb Api Title Structure
  property_count: 0
  slug: imdb-api-title-structure
jsonld:
- class_count: 41
  name: Imdb Api Context
  property_count: 0
  slug: imdb-api-context
layout: provider
modified: '2026-05-30'
name: IMDb-API
nav: Providers
network: true
overview: 'IMDb-API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including External API, Lists API, Name API, and 3 more. Tagged areas include Video, Movies, TV, Entertainment, and Metadata.


  The IMDb-API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IMDb-API''s developer surface includes authentication, pricing, signup flow, tooling, and 14 more developer resources.'
plans:
- name: Imdb Api Plans Pricing
  plan_count: 4
  slug: imdb-api-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Imdb Api Rate Limits
  slug: imdb-api-rate-limits
rules:
- name: IMDb-API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: imdb-api-jsonschema-spectral-rules
- name: IMDb-API API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: imdb-api-rules
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 17.4
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 47.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imdb-api/refs/heads/main/screenshots/imdb-api-2026-06-20T183246.png
security:
- kind: authentication
  name: Imdb Api Authentication
  slug: imdb-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Imdb Api Domain Security
  slug: imdb-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imdb-api
solutions:
- description: 100 requests/day for hobbyists and prototypes.
  name: Free tier
- description: Small-to-growing applications (5k-10k requests/day).
  name: Standard / Plus
- description: Production applications (30k-999k requests/day, unlimited IP authorizations).
  name: Premium
tags:
- Video
- Movies
- TV
- Entertainment
- Metadata
- Ratings
- Public APIs
use_cases:
- description: Hydrate an in-house movie or TV catalog with posters, plots, cast and ratings.
  name: Media catalog enrichment
- description: Drive what-to-watch suggestions from Top 250, Most Popular and similar-titles signals.
  name: Recommendation systems
- description: Surface IMDb, Metacritic and Rotten Tomatoes scores in a single UI.
  name: Review aggregation
- description: Track weekend and all-time box office performance.
  name: Box office dashboards
- description: Answer movie and cast questions from a conversational agent.
  name: Entertainment chatbots
website: https://tv-api.com/
---
