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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mediastack Agentic Access
  operation_count: 2
  slug: mediastack-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Live and historical news articles from global publishers.
  name: Mediastack News API
  slug: mediastack-news-api
- description: Discovery of supported news sources, publishers, and blogs.
  name: Mediastack Sources API
  slug: mediastack-sources-api
artifact_total: 47
collections:
- collection_type: postman
  name: Mediastack News API
  slug: postman-mediastack-news-api
- collection_type: postman
  name: Mediastack News Sources API
  slug: postman-mediastack-sources-api
- collection_type: open
  name: Mediastack News API
  slug: open-mediastack
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apilayer/mediastack/issues
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mediastack/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mediastack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mediastack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mediastack-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mediastack.com
- group: start
  title: ''
  type: Portal
  url: https://mediastack.com/dashboard
- group: start
  title: ''
  type: Signup
  url: https://mediastack.com/signup/free
- group: commercial
  title: ''
  type: Pricing
  url: https://mediastack.com/product
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mediastack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mediastack.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://mediastack.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://mediastack.com/documentation#faq
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apilayer/mediastack
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mediastack-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/mediastack-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mediastack-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mediastack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mediastack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mediastack-finops.yml
created: '2026-05-28'
description: Mediastack is a free and paid REST API by apilayer for live, historical, and blog news articles aggregated from more than 7,500 publishers across 50+ countries and 13 languages. It exposes a /v1/news endpoint for keyword-, source-, country-, language-, category-, and date-filtered search, and a /v1/sources endpoint for browsing the underlying publisher catalog.
examples:
- key_count: 3
  name: Mediastack Historical News Example
  slug: mediastack-historical-news-example
- key_count: 2
  name: Mediastack List Sources Example
  slug: mediastack-list-sources-example
- key_count: 2
  name: Mediastack Search News Example
  slug: mediastack-search-news-example
features:
- description: Real-time aggregation of articles from 7,500+ global news publishers.
  name: Live News Data
- description: Date-bounded lookups of past articles via the date query parameter (paid plans).
  name: Historical News
- description: Articles indexed across 13 languages including English, German, Spanish, French, Chinese, and Arabic.
  name: Multi-Language Coverage
- description: Filter by 50+ country codes using ISO 3166-1 alpha-2.
  name: Multi-Country Coverage
- description: Restrict to general, business, entertainment, health, science, sports, or technology.
  name: Category Filtering
- description: Include/exclude lists of specific publishers via comma-separated IDs.
  name: Source Filtering
- description: Full-text search across article title, description, and body.
  name: Keyword Search
- description: Browse the /sources catalog by country, language, or category.
  name: Publisher Catalog
- description: Encrypted transport on Standard plan and above.
  name: HTTPS Encryption
- description: Permitted on Standard plan and above.
  name: Commercial Use License
finops:
- name: Mediastack Finops
  service_category: News & Media Data
  slug: mediastack-finops
image: https://mediastack.com/site_images/mediastack_logo_dark.svg
integrations:
- description: Mediastack is one of several APIs in the apilayer marketplace alongside marketstack, currencylayer, weatherstack, and ipapi.
  name: apilayer Marketplace
- description: Standard HTTPS+JSON makes it trivial to integrate with any HTTP client library.
  name: REST + JSON
- description: Manual import of the OpenAPI spec into common API clients.
  name: Postman / Insomnia
json_schemas:
- name: Error
  property_count: 2
  slug: mediastack-error
- name: NewsArticle
  property_count: 10
  slug: mediastack-news-article
- name: Pagination
  property_count: 4
  slug: mediastack-pagination
- name: Source
  property_count: 6
  slug: mediastack-source
json_structures:
- name: Mediastack News Article Structure
  property_count: 0
  slug: mediastack-news-article-structure
- name: Mediastack Source Structure
  property_count: 0
  slug: mediastack-source-structure
jsonld:
- class_count: 13
  name: Mediastack Context
  property_count: 6
  slug: mediastack-context
layout: provider
modified: '2026-05-30'
name: Mediastack
nav: Providers
network: true
overview: 'Mediastack publishes 2 APIs on the [APIs.io](https://apis.io/) network: News API and Sources API. Tagged areas include News, News Aggregation, Media, Apilayer, and Public APIs.


  The Mediastack catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mediastack''s developer surface includes authentication, developer portal, signup flow, pricing, support, FAQ, and 15 more developer resources.'
plans:
- name: Mediastack Plans Pricing
  plan_count: 5
  slug: mediastack-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Mediastack Rate Limits
  slug: mediastack-rate-limits
rules:
- name: Mediastack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mediastack-jsonschema-spectral-rules
- name: Mediastack API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 4
  slug: mediastack-rules
score:
  band: strong
  composite: 60.9
  delta: 1.9
  facets:
    commercial_clarity: 84.2
    contract_quality: 73.9
    developer_ergonomics: 28.3
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mediastack/refs/heads/main/screenshots/mediastack-2026-06-20T185116.png
security:
- kind: authentication
  name: Mediastack Authentication
  slug: mediastack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mediastack Domain Security
  slug: mediastack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mediastack
solutions:
- description: Evaluation tier, 100 requests/month, HTTP only, no historical data, no commercial use.
  name: Free Plan
- description: $24.99/month, 10k requests, HTTPS, historical data, commercial use.
  name: Standard Plan
- description: $99.99/month, 50k requests, lower overage rate.
  name: Professional Plan
- description: $249.99/month, 250k requests, lowest published overage rate.
  name: Business Plan
- description: Custom volume, platinum support, custom solutions.
  name: Enterprise Plan
tags:
- News
- News Aggregation
- Media
- Apilayer
- Public APIs
use_cases:
- description: Power consumer-facing news readers with category- and language-filtered feeds.
  name: News Aggregator Apps
- description: Track brand, executive, product, or competitor mentions across global press.
  name: Media Monitoring
- description: Stream business-tagged headlines into trading dashboards.
  name: Investor Research
- description: Sample current-events text for fine-tuning and retrieval-augmented generation.
  name: AI Training Corpora
- description: Tally publication volume and sentiment around recurring keywords.
  name: Trend Analysis
- description: Auto-generate daily digests by country, language, or topic.
  name: Newsletter Curation
website: https://mediastack.com
---
