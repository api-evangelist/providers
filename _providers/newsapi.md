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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Newsapi Agentic Access
  operation_count: 3
  slug: newsapi-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: Search all articles from all sources
  name: NewsAPI Everything API
  slug: newsapi-everything-api
- description: Get available news sources
  name: NewsAPI Sources API
  slug: newsapi-sources-api
- description: Get live top and breaking headlines
  name: NewsAPI Top Headlines API
  slug: newsapi-top-headlines-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: News Everything API
  slug: open-newsapi-everything-api
- collection_type: open
  name: News Everything Sources API
  slug: open-newsapi-sources-api
- collection_type: open
  name: News Everything Top Headlines API
  slug: open-newsapi-top-headlines-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/newsapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newsapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/newsapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://newsapi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://newsapi.org/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/News-API-gh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newsapi
- group: company
  title: ''
  type: Blog
  url: https://newsapi.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://newsapi.org/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://newsapi.org/status
- group: other
  title: ''
  type: X
  url: https://x.com/newsapi
- group: commercial
  title: ''
  type: Plans
  url: plans/newsapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/newsapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/newsapi-finops.yml
created: '2026-06-12'
description: NewsAPI is a simple, easy-to-use REST API that returns JSON metadata for news articles and breaking headlines published by over 80,000 worldwide sources and blogs. The API supports full-text keyword search across hundreds of millions of articles, filtering by source domain, language, date range, and sorting by relevance or publication date. A dedicated top-headlines endpoint delivers live breaking news by country and category — covering business, entertainment, general, health, science, sports, and technology. Developers authenticate via an API key passed as a query parameter or HTTP header, and all responses are returned as standard JSON.
examples:
- key_count: 2
  name: Newsapi Everything Example
  slug: newsapi-everything-example
- key_count: 2
  name: Newsapi Sources Example
  slug: newsapi-sources-example
- key_count: 2
  name: Newsapi Top Headlines Example
  slug: newsapi-top-headlines-example
finops:
- name: Newsapi Finops
  service_category: News Data API
  slug: newsapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newsapi.png
json_schemas:
- name: Article
  property_count: 8
  slug: newsapi-article
- name: ErrorResponse
  property_count: 3
  slug: newsapi-error
- name: NewsSource
  property_count: 7
  slug: newsapi-source
jsonld:
- class_count: 2
  name: Newsapi Context
  property_count: 29
  slug: newsapi-context
layout: provider
modified: '2026-06-12'
name: NewsAPI
nav: Providers
network: true
overview: 'NewsAPI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Everything API, Sources API, and Top Headlines API. Tagged areas include News, Headlines, Articles, Search, and Media.


  The NewsAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NewsAPI''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Newsapi Plans Pricing
  plan_count: 4
  slug: newsapi-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Newsapi Rate Limits
  slug: newsapi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: NewsAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: newsapi-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: -8.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 70.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/newsapi/refs/heads/main/screenshots/newsapi-2026-06-20T190246.png
security:
- kind: authentication
  name: Newsapi Authentication
  slug: newsapi-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Newsapi Domain Security
  slug: newsapi-domain-security
  summary_line: TLSv1.3
slug: newsapi
tags:
- News
- Headlines
- Articles
- Search
- Media
- Content
- REST
- JSON
website: https://newsapi.org/
---
