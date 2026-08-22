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
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: News Api Agentic Access
  operation_count: 3
  slug: news-api-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Articles API from News API — 1 operation(s) for articles.
  name: News API Articles API
  slug: news-api-articles-api
- description: The Headlines API from News API — 1 operation(s) for headlines.
  name: News API Headlines API
  slug: news-api-headlines-api
- description: The Sources API from News API — 1 operation(s) for sources.
  name: News API Sources API
  slug: news-api-sources-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: News Articles API
  slug: open-news-api-articles-api
- collection_type: open
  name: News Articles Headlines API
  slug: open-news-api-headlines-api
- collection_type: open
  name: News Articles Sources API
  slug: open-news-api-sources-api
- collection_type: open
  name: News API
  slug: open-news-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/news-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/news-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/news-api-authentication.yml
created: '2025-02-09'
description: Locate articles and breaking news headlines from news sources and blogs across the web with our JSON API.
finops:
- name: News Api Finops
  service_category: API
  slug: news-api-finops
graphqls:
- description: Conceptual GraphQL schema for the [NewsAPI](https://newsapi.org/) news aggregation REST API. NewsAPI provides access to breaking headlines and a searchable index of articles from thousands of news sou
  name: NewsAPI GraphQL Schema
  slug: news-api-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/news-api.png
layout: provider
modified: '2026-05-19'
name: News API
nav: Providers
network: true
overview: 'News API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Articles API, Headlines API, and Sources API. Tagged areas include News, Articles, Headlines, and Search.


  News API''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: News Api Plans Pricing
  plan_count: 3
  slug: news-api-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: News Api Rate Limits
  slug: news-api-rate-limits
score:
  band: thin
  composite: 26.6
  delta: -0.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 58.0
    developer_ergonomics: 11.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/news-api/refs/heads/main/screenshots/news-api-2026-06-20T190244.png
security:
- kind: authentication
  name: News Api Authentication
  slug: news-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: News Api Domain Security
  slug: news-api-domain-security
  summary_line: TLSv1.3
slug: news-api
tags:
- News
- Articles
- Headlines
- Search
---
