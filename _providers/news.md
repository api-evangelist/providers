---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Headlines currently published on a range of news sources and blogs
  name: News
  slug: news
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://newsapi.org/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Headlines currently published on a range of news sources and blogs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/news.png
layout: provider
modified: '2026-05-28'
name: News
nav: Providers
network: true
overview: News publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Public APIs, and Fortune 500.
random_paper: 97
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/news/refs/heads/main/screenshots/news-2026-06-20T190244.png
security:
- kind: domain-security
  name: News Domain Security
  slug: news-domain-security
  summary_line: TLSv1.3
slug: news
tags:
- News
- Public APIs
- Fortune 500
website: https://newsapi.org/
---
