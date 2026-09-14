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
  try_now: false
api_count: 1
apis:
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: Entity statistics, trending entities, entity search, and entity metadata.
  name: MarketAux Entities API
  slug: marketaux-entities-api
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: Financial and market news feeds, similar-article lookup, and article retrieval by UUID.
  name: MarketAux News API
  slug: marketaux-news-api
- baseURL: https://api.marketaux.com/v1
  baseurl_source: declared
  description: News source metadata usable in news feed filters.
  name: MarketAux Sources API
  slug: marketaux-sources-api
artifact_total: 8
collections:
- collection_type: open
  name: Marketaux API
  slug: open-marketaux
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/marketaux-openapi-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/marketaux-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.marketaux.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.marketaux.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://www.marketaux.com/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.marketaux.com/documentation#introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marketaux.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.marketaux.com/register
- group: start
  title: ''
  type: Login
  url: https://www.marketaux.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.marketaux.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.marketaux.com/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marketaux.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marketaux.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketaux-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/marketaux-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketaux-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marketaux-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marketaux-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marketaux-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/marketaux-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marketaux-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/marketaux-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/marketaux-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marketaux-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketaux-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketaux-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Marketaux is a global financial and stock market news API that pairs every article with entity recognition and sentiment analysis. It aggregates 5,000+ news sources in 30+ languages, tracking 200,000+ entities — equities, indices, ETFs, mutual funds, currencies, and cryptocurrencies — across 80+ markets. Beyond filtered news feeds, it provides entity statistics time series, aggregations, and trending-entity endpoints for identifying the best and worst performing entities in the news, with a free self-serve tier.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketaux.png
layout: provider
modified: '2026-07-22'
name: MarketAux
nav: Providers
network: true
overview: 'MarketAux publishes 3 APIs on the [APIs.io](https://apis.io/) network: Entities API, News API, and Sources API. Tagged areas include News, Financial News, Stock Market, Sentiment Analysis, and Market Data.


  MarketAux''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, FAQ, and 21 more developer resources.'
plans:
- name: Marketaux Plans
  plan_count: 6
  slug: marketaux-plans
random_paper: 12
rate_limits:
- limit_count: 6
  name: Marketaux Rate Limits
  slug: marketaux-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/marketaux/refs/heads/main/screenshots/marketaux-2026-06-20T184952.png
security:
- kind: authentication
  name: Marketaux Authentication
  slug: marketaux-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Marketaux Domain Security
  slug: marketaux-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: marketaux
tags:
- News
- Financial News
- Stock Market
- Sentiment Analysis
- Market Data
- Entity Recognition
- Public APIs
website: https://www.marketaux.com/
---
