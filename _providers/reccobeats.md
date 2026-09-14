---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Reccobeats Agentic Access
  operation_count: 14
  slug: reccobeats-agentic-access
  summary_line: 14 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Album metadata and tracklists.
  name: ReccoBeats Album API
  slug: reccobeats-album-api
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Artist metadata and discography.
  name: ReccoBeats Artist API
  slug: reccobeats-artist-api
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Extract audio features directly from an uploaded audio file.
  name: ReccoBeats Audio Analysis API
  slug: reccobeats-audio-analysis-api
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Spotify-style audio features for a catalog track.
  name: ReccoBeats Audio Features API
  slug: reccobeats-audio-features-api
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Track recommendations generated from seeds.
  name: ReccoBeats Recommendation API
  slug: reccobeats-recommendation-api
- baseURL: https://api.reccobeats.com/v1
  baseurl_source: declared
  description: Track metadata lookup by ReccoBeats or Spotify ID.
  name: ReccoBeats Track API
  slug: reccobeats-track-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ReccoBeats Album API
  slug: open-reccobeats-album-api
- collection_type: open
  name: ReccoBeats Album Artist API
  slug: open-reccobeats-artist-api
- collection_type: open
  name: ReccoBeats Album Audio Analysis API
  slug: open-reccobeats-audio-analysis-api
- collection_type: open
  name: ReccoBeats Album Audio Features API
  slug: open-reccobeats-audio-features-api
- collection_type: open
  name: ReccoBeats Album Recommendation API
  slug: open-reccobeats-recommendation-api
- collection_type: open
  name: ReccoBeats Album Track API
  slug: open-reccobeats-track-api
- collection_type: open
  name: ReccoBeats API
  slug: open-reccobeats
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/reccobeats-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reccobeats-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reccobeats-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://reccobeats.com/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://reccobeats.com
- group: docs
  title: ''
  type: Documentation
  url: https://reccobeats.com/docs/documentation/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/reccobeats-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reccobeats-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reccobeats-finops.yml
created: '2026-07-03'
description: ReccoBeats is a free music recommendation and database API service. It exposes a REST API over a database of millions of tracks, artists, and albums, and a machine-learning recommendation engine that suggests tracks from seed tracks, artists, or albums. ReccoBeats also extracts Spotify-style audio features - acousticness, danceability, energy, instrumentalness, liveness, loudness, speechiness, tempo, and valence - either for a catalog track by ID or directly from an uploaded audio file. Resources can be addressed by ReccoBeats UUID or by Spotify ID, and the API requires no API key or authentication.
finops:
- name: Reccobeats Finops
  service_category: Machine Learning and Media
  slug: reccobeats-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reccobeats.png
layout: provider
modified: '2026-07-03'
name: ReccoBeats
nav: Providers
network: true
overview: 'ReccoBeats publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Audio Analysis API, and 3 more. Tagged areas include Music, Recommendations, Audio Features, Audio Analysis, and Music Database.


  ReccoBeats'' developer surface includes engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Reccobeats Plans Pricing
  plan_count: 1
  slug: reccobeats-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Reccobeats Rate Limits
  slug: reccobeats-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/reccobeats/refs/heads/main/screenshots/reccobeats-2026-09-02T153043.png
security:
- kind: domain-security
  name: Reccobeats Domain Security
  slug: reccobeats-domain-security
  summary_line: TLSv1.3
slug: reccobeats
tags:
- Music
- Recommendations
- Audio Features
- Audio Analysis
- Music Database
- Spotify Alternative
website: https://reccobeats.com
---
