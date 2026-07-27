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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Finlight Agentic Access
  operation_count: 3
  slug: finlight-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 2
apis:
- description: Financial news articles with sentiment analysis and entity extraction
  name: Finlight Articles API
  slug: finlight-articles-api
- description: Available news sources and their configuration
  name: Finlight Sources API
  slug: finlight-sources-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finlight-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finlight-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finlight-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finlight.me/v2/
- group: commercial
  title: ''
  type: Pricing
  url: https://finlight.me/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.finlight.me
- group: company
  title: ''
  type: About
  url: https://finlight.me/about
- group: company
  title: ''
  type: x-twitter
  url: https://twitter.com/finlight_me
- group: operate
  title: ''
  type: x-discord
  url: https://discord.gg/XUs9JYZd24
- group: build
  title: ''
  type: x-npm
  url: https://www.npmjs.com/package/finlight-client
- group: other
  title: ''
  type: x-pypi
  url: https://pypi.org/project/finlight-client/
- group: operate
  title: ''
  type: Contact
  url: mailto:info@finlight.me
- group: company
  title: ''
  type: Blog
  url: https://finlight.me/blog/feed.xml
created: '2026-06-13'
description: Finlight is a real-time financial news API that aggregates market-moving news, earnings reports, analyst upgrades, and corporate announcements for equities, currencies, and commodities. The platform delivers AI-driven sentiment analysis, entity extraction, and sub-second latency streaming for developers and enterprises building financial applications.
examples:
- key_count: 2
  name: Get Article By Link Response
  slug: get-article-by-link-response
- key_count: 2
  name: List Sources Response
  slug: list-sources-response
- key_count: 2
  name: Search Articles Request
  slug: search-articles-request
- key_count: 2
  name: Search Articles Response
  slug: search-articles-response
- key_count: 3
  name: Webhook Payload
  slug: webhook-payload
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://finlight.me/favicon.ico
json_schemas:
- name: ArticleCategory
  property_count: 0
  slug: article-category
- name: Article
  property_count: 16
  slug: article
- name: Company
  property_count: 13
  slug: company
- name: Listing
  property_count: 3
  slug: listing
- name: Source
  property_count: 3
  slug: source
layout: provider
modified: '2026-06-13'
name: Finlight
nav: Providers
network: true
overview: 'Finlight publishes 2 APIs on the [APIs.io](https://apis.io/) network: Articles API and Sources API. Tagged areas include Financial News, Sentiment Analysis, Market Data, Equities, and Currencies.


  The Finlight catalog on APIs.io includes 1 Spectral governance ruleset.


  Finlight''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 37
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Finlight API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: finlight-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 21.7
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 0.0
  previous_composite: 45.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finlight/refs/heads/main/screenshots/finlight-2026-06-20T181218.png
security:
- kind: authentication
  name: Finlight Authentication
  slug: finlight-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Finlight Domain Security
  slug: finlight-domain-security
  summary_line: TLSv1.3 · DMARC
slug: finlight
tags:
- Financial News
- Sentiment Analysis
- Market Data
- Equities
- Currencies
- Commodities
- Real-Time
- Webhooks
- WebSocket
---
