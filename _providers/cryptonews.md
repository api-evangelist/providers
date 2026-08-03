---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cryptonews Agentic Access
  operation_count: 11
  slug: cryptonews-agentic-access
  summary_line: 11 operations
api_count: 8
apis:
- description: Account and reference data
  name: CryptoNews API Account API
  slug: cryptonews-account-api
- description: News by category or sector
  name: CryptoNews API Categories API
  slug: cryptonews-categories-api
- description: Curated digest endpoints
  name: CryptoNews API Digest API
  slug: cryptonews-digest-api
- description: Cryptocurrency news articles aggregated from 50+ sources
  name: CryptoNews API News API
  slug: cryptonews-news-api
- description: Delayed cryptocurrency pricing data
  name: CryptoNews API Prices API
  slug: cryptonews-prices-api
- description: Sentiment analysis and statistical summaries
  name: CryptoNews API Sentiment & Stats API
  slug: cryptonews-sentiment-stats-api
- description: Trending headlines and top mentions
  name: CryptoNews API Trending API
  slug: cryptonews-trending-api
- description: Large on-chain whale transaction tracking
  name: CryptoNews API Whale Transactions API
  slug: cryptonews-whale-transactions-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cryptonews-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cryptonews-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cryptonews-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://cryptonews-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptonews-api.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptonews-api.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://cryptonews-api.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://cryptonews-api.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptonews-api.com/termsandconditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptonews-api.com/privacypolicy
- group: other
  title: ''
  type: X
  url: https://x.com/cryptonewsapi
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/cryptonews/refs/heads/main/plans/cryptonews-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/cryptonews/refs/heads/main/rate-limits/cryptonews-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/cryptonews/refs/heads/main/finops/cryptonews-finops.yml
created: 2026-06-13
description: REST API aggregating cryptocurrency news, Bitcoin sentiment analysis, and crypto market news from 50+ sources with filtering by currency and time range. Provides AI-powered sentiment analysis, delayed pricing for 600+ coins, whale transaction tracking, and historical data from December 2020.
examples:
- key_count: 3
  name: Get Crypto News
  slug: get-crypto-news
- key_count: 1
  name: Get Ticker Price
  slug: get-ticker-price
- key_count: 2
  name: Get Whale Transactions
  slug: get-whale-transactions
finops:
- name: Cryptonews Finops
  service_category: ''
  slug: cryptonews-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cryptonews.png
json_schemas:
- name: CryptoNews Article
  property_count: 10
  slug: news-article
- name: Ticker Price
  property_count: 5
  slug: ticker-price
- name: Whale Transaction
  property_count: 9
  slug: whale-transaction
jsonld:
- class_count: 44
  name: Cryptonews Context
  property_count: 5
  slug: cryptonews-context
layout: provider
modified: 2026-06-13
name: CryptoNews API
nav: Providers
network: true
overview: 'CryptoNews API publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Categories API, Digest API, and 5 more. Tagged areas include Cryptocurrency, News, Sentiment Analysis, Bitcoin, and Market Data.


  The CryptoNews API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CryptoNews API''s developer surface includes authentication, documentation, pricing, engineering blog, FAQ, and 9 more developer resources.'
plans:
- name: Cryptonews Plans Pricing
  plan_count: 4
  slug: cryptonews-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Cryptonews Rate Limits
  slug: cryptonews-rate-limits
rules:
- name: CryptoNews API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cryptonews-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.6
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 67.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cryptonews/refs/heads/main/screenshots/cryptonews-2026-06-20T175312.png
security:
- kind: authentication
  name: Cryptonews Authentication
  slug: cryptonews-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cryptonews Domain Security
  slug: cryptonews-domain-security
  summary_line: TLSv1.2
slug: cryptonews
tags:
- Cryptocurrency
- News
- Sentiment Analysis
- Bitcoin
- Market Data
- Whale Transactions
- Crypto Prices
website: https://cryptonews-api.com/
---
