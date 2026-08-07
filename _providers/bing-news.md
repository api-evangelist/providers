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
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bing News Agentic Access
  operation_count: 3
  slug: bing-news-agentic-access
  summary_line: 3 operations
api_count: 5
apis:
- description: Returns top news articles filtered by category (e.g., Business, Entertainment, Sports, Health, ScienceAndTechnology, Politics, World). Supports multiple markets with locale-specific category taxonomie
  name: Bing News Category API
  slug: news-category
- description: Returns news topics that are currently trending on social networks. Supports filtering by Unix epoch timestamp (since parameter) to retrieve topics discovered after a specific point in time. Results i
  name: Bing Trending News Topics API
  slug: trending-topics
- description: Get top news articles by category
  name: Bing News Search News Category API
  slug: bing-news-news-category-api
- description: Search for news articles by keyword query
  name: Bing News Search News Search API
  slug: bing-news-news-search-api
- description: Get currently trending news topics from social networks
  name: Bing News Search Trending Topics API
  slug: bing-news-trending-topics-api
artifact_total: 20
collections:
- collection_type: postman
  name: Bing News Search API v7 News Category API
  slug: postman-bing-news-news-category-api
- collection_type: postman
  name: Bing API v7 News Category News Search API
  slug: postman-bing-news-news-search-api
- collection_type: postman
  name: Bing News Search API v7 News Category Trending Topics API
  slug: postman-bing-news-trending-topics-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bing-news-search/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bing-news-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bing-news-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bing-news-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bing.com/news
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/previous-versions/bing/search-apis/bing-news-search/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/previous-versions/bing/search-apis/bing-news-search/reference/endpoints
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/create-bing-search-service-resource
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/bing/apis/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/bing/apis/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/previous-versions/bing/search-apis/bing-news-search/quickstarts/quickstarts
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/previous-versions/azure/cognitive-services/Bing-News-Search/quickstarts/client-libraries
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/tags/142/bing-category-bing-search-apis-azure-bing-news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
created: '2026-06-13'
description: Microsoft Bing News Search REST API enables developers to retrieve relevant news articles, trending topics, and category-filtered news with image thumbnails and publisher metadata. The API provides search queries against Bing's news index, returning results with titles, descriptions, URLs, publication dates, and related media content.
examples:
- key_count: 3
  name: News Category Response
  slug: news-category-response
- key_count: 6
  name: News Search Response
  slug: news-search-response
- key_count: 2
  name: Trending Topics Response
  slug: trending-topics-response
finops:
- name: Bing News Finops
  service_category: API
  slug: bing-news-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bing-news.png
json_schemas:
- name: NewsArticle
  property_count: 13
  slug: news-article
- name: TrendingTopic
  property_count: 6
  slug: trending-topic
layout: provider
modified: '2026-06-13'
name: Bing News Search
nav: Providers
network: true
overview: 'Bing News Search publishes 3 APIs on the [APIs.io](https://apis.io/) network: News Category API, News Search API, and Trending Topics API. Tagged areas include News, Search, Microsoft, Bing, and Media.


  The Bing News Search catalog on APIs.io includes 1 Spectral governance ruleset.


  Bing News Search''s developer surface includes authentication, developer portal, documentation, API reference, pricing, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Bing News Plans Pricing
  plan_count: 2
  slug: bing-news-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Bing News Rate Limits
  slug: bing-news-rate-limits
rules:
- name: Bing News Search API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bing-news-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.6
    developer_ergonomics: 60.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bing-news/refs/heads/main/screenshots/bing-news-2026-06-20T173246.png
security:
- kind: authentication
  name: Bing News Authentication
  slug: bing-news-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bing News Domain Security
  slug: bing-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bing-news
tags:
- News
- Search
- Microsoft
- Bing
- Media
- Headlines
- Trending Topics
website: https://www.bing.com/news
---
