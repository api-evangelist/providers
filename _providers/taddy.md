---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 9
apis:
- description: Blazing-fast full-text `search` query across all 4M+ podcasts and 200M+ episodes, with filters for country, genre, language, publish date, and whether a transcript is available, and sortable by exactn
  name: Taddy Podcast Search API
  slug: taddy-podcast-search-api
- description: 'Look up podcast series and episodes via getPodcastSeries, getPodcastEpisode, getMultiplePodcastSeries, getMultiplePodcastEpisodes, and getLatestPodcastEpisodes, keyed by Taddy uuid, name, RSS URL, or '
  name: Taddy Podcast Series & Episodes API
  slug: taddy-podcast-series-episodes-api
- description: Retrieve episode transcripts with getEpisodeTranscript and the transcriptWithSpeakersAndTimecodes field, including per-line text, speaker names, and start/end timecodes, backed by Taddy's automatic tr
  name: Taddy Episode Transcripts API
  slug: taddy-transcripts-api
- description: Fetch chapter markers for an episode via getEpisodeChapters and the chapters field, returning chapter titles and start timecodes for chapterized podcasts.
  name: Taddy Episode Chapters API
  slug: taddy-episode-chapters-api
- description: Resolve Apple Podcasts / iTunes metadata for a podcast with getItunesInfo and the itunesInfo field, including iTunes ID, base artwork URL, categories, and content advisory.
  name: Taddy iTunes Info API
  slug: taddy-itunes-info-api
- description: Retrieve daily top charts and popular content with getTopChartsByCountry, getTopChartsByGenre, and getPopularContent, filterable by country, genre, and language.
  name: Taddy Top Charts & Popular API
  slug: taddy-top-charts-popular-api
- description: Access webcomic and creator data via getComicSeries, getComicIssue, getCreator, and getMultipleCreators, covering comic series, individual issues, and the artists, writers, and other creators behind t
  name: Taddy Comics & Creators API
  slug: taddy-comics-creators-api
- description: Real-time webhook notifications for new and updated content, delivering events such as podcast.created, podcast.updated, podcast.deleted, podcast.new_episodes, and matching creator/creatorcontent even
  name: Taddy Webhooks API
  slug: taddy-webhooks-api
- description: Monitor plan consumption with getApiRequestsRemaining (monthly API request quota) and getTranscriptCreditsRemaining (monthly transcript credit allocation).
  name: Taddy Account & Usage API
  slug: taddy-account-usage-api
artifact_total: 15
collections:
- collection_type: open
  name: Taddy GraphQL API
  slug: open-taddy
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taddy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/taddyorg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/taddy
- group: company
  title: ''
  type: Website
  url: https://taddy.org/
- group: docs
  title: ''
  type: Documentation
  url: https://taddy.org/developers
- group: commercial
  title: ''
  type: Plans
  url: plans/taddy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/taddy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/taddy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://taddy.org/blog
created: '2026-07-03'
description: Taddy is a GraphQL API for podcasts and comics, giving developers access to over 4 million podcasts and 200 million episodes, plus real-time full-text search, automatically generated episode transcripts, chapters, iTunes metadata, daily top charts, webcomic and creator data, and webhook notifications for new or updated content. All queries hit a single GraphQL endpoint at https://api.taddy.org authenticated with X-USER-ID and X-API-KEY headers.
finops:
- name: Taddy Finops
  service_category: Media and Content APIs
  slug: taddy-finops
graphqls:
- description: Taddy is a **native GraphQL API** for podcasts and comics. It gives developers
  name: Taddy GraphQL API
  slug: taddy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/taddy.png
layout: provider
modified: '2026-07-03'
name: Taddy
nav: Providers
network: true
overview: 'Taddy publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasts, Comics, GraphQL, Search, and Transcripts.


  Taddy''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Taddy Plans Pricing
  plan_count: 4
  slug: taddy-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Taddy Rate Limits
  slug: taddy-rate-limits
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 43.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Taddy Domain Security
  slug: taddy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: taddy
tags:
- Podcasts
- Comics
- GraphQL
- Search
- Transcripts
- Media
- Content
website: https://taddy.org/
---
