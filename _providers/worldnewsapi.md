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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Worldnewsapi Agentic Access
  operation_count: 8
  slug: worldnewsapi-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: Extract article content and links from arbitrary news URLs.
  name: World News API Extract News API
  slug: worldnewsapi-extract-news-api
- description: Retrieve newspaper front-page images by country and date.
  name: World News API Front Pages API
  slug: worldnewsapi-front-pages-api
- description: Resolve a place name to latitude/longitude for local news search.
  name: World News API Geo Coordinates API
  slug: worldnewsapi-geo-coordinates-api
- description: Discover and inspect available news sources.
  name: World News API News Sources API
  slug: worldnewsapi-news-sources-api
- description: Retrieve full article records by id.
  name: World News API Retrieve News API
  slug: worldnewsapi-retrieve-news-api
- description: Full-text, semantic, and geo/local news search.
  name: World News API Search News API
  slug: worldnewsapi-search-news-api
- description: Country-level top news clustered by coverage.
  name: World News API Top News API
  slug: worldnewsapi-top-news-api
artifact_total: 14
collections:
- collection_type: open
  name: World News API
  slug: open-worldnewsapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/worldnewsapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/worldnewsapi-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldnewsapi-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ddsky
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-news-api
- group: company
  title: ''
  type: Website
  url: https://worldnewsapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://worldnewsapi.com/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/worldnewsapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/worldnewsapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/worldnewsapi-finops.yml
created: '2026-07-11'
description: World News API is a real-time and historical news data API covering thousands of sources across 210+ countries and 86+ languages. It provides full-text and semantic news search, geo-targeted local news search (a radius filter around a latitude/longitude point), article content and link extraction from arbitrary URLs, country-level top news clustering, newspaper front-page images, and news-source discovery. Local news search is a first-class feature - resolve a place name to coordinates with the Geo Coordinates endpoint, then pass those coordinates to Search News via the location-filter parameter to find news published or mentioned near that place. Requests are authenticated with an API key (api-key query parameter or x-api-key header) and metered in points against a daily plan allowance.
finops:
- name: Worldnewsapi Finops
  service_category: News and Media Data
  slug: worldnewsapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldnewsapi.png
layout: provider
modified: '2026-07-11'
name: World News API
nav: Providers
network: true
overview: 'World News API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Extract News API, Front Pages API, Geo Coordinates API, and 4 more. Tagged areas include News, Local News, News Search, Media Monitoring, and Geo Search.


  World News API''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Worldnewsapi Plans Pricing
  plan_count: 4
  slug: worldnewsapi-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 6
  name: Worldnewsapi Rate Limits
  slug: worldnewsapi-rate-limits
score:
  band: thin
  composite: 39.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Worldnewsapi Authentication
  slug: worldnewsapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Worldnewsapi Domain Security
  slug: worldnewsapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: worldnewsapi
tags:
- News
- Local News
- News Search
- Media Monitoring
- Geo Search
- News Data
- Sentiment Analysis
- Content Extraction
website: https://worldnewsapi.com
---
