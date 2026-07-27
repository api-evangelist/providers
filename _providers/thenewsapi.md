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
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Thenewsapi Agentic Access
  operation_count: 6
  slug: thenewsapi-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: News article retrieval and search
  name: TheNewsAPI news API
  slug: thenewsapi-news-api
- description: News source discovery
  name: TheNewsAPI sources API
  slug: thenewsapi-sources-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thenewsapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thenewsapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thenewsapi-authentication.yml
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: other
  title: ''
  type: BaseURL
  url: ''
- group: design
  title: ''
  type: Versioning
  url: ''
- group: other
  title: ''
  type: DataFormats
  url: ''
- group: design
  title: ''
  type: ErrorCodes
  url: ''
created: '2026-06-13'
description: Global news aggregation REST API providing real-time and historical news articles from thousands of sources with filtering by category, language, country, and search. Indexes over 1 million new articles per week from 40,000+ sources across 50+ countries and 35+ languages.
examples:
- key_count: 4
  name: Get All News
  slug: get-all-news
- key_count: 4
  name: Get Sources
  slug: get-sources
- key_count: 4
  name: Get Top Stories
  slug: get-top-stories
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.thenewsapi.com/img/logo.png
json_schemas:
- name: ArticleListResponse
  property_count: 2
  slug: article-list-response
- name: Article
  property_count: 14
  slug: article
- name: Source
  property_count: 5
  slug: source
layout: provider
modified: '2026-06-13'
name: TheNewsAPI
nav: Providers
network: true
overview: 'TheNewsAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: news API and sources API. Tagged areas include news, articles, headlines, media, and aggregation.


  The TheNewsAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  TheNewsAPI''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 60
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: TheNewsAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thenewsapi-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 10.9
    discoverability: 85.0
    governance: 73.7
    operational_transparency: 15.8
  previous_composite: 45.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thenewsapi/refs/heads/main/screenshots/thenewsapi-2026-06-20T195250.png
security:
- kind: authentication
  name: Thenewsapi Authentication
  slug: thenewsapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Thenewsapi Domain Security
  slug: thenewsapi-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: thenewsapi
tags:
- news
- articles
- headlines
- media
- aggregation
- real-time
website: https://www.thenewsapi.com
---
