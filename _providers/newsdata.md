---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: NewsData.io API for retrieving live breaking news and historical news data from over 82,000 sources, with search, filtering, and multi-language support.
  name: NewsData
  slug: newsdata
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/newsdata-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/newsdataapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/newsdata
- group: docs
  title: ''
  type: Documentation
  url: https://newsdata.io/documentation
- group: start
  title: ''
  type: Signup
  url: https://newsdata.io/register
- group: commercial
  title: ''
  type: Pricing
  url: https://newsdata.io/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://newsdata.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://newsdata.io/blog/feed/
created: '2025-02-09'
description: NewsData.io provides live breaking news and historical news data going back to January 2018, sourced from over 82,000 sources worldwide. The API supports searching, filtering by source, language, country, and category, and returns results in JSON format suitable for analytics, monitoring, and AI training.
finops:
- name: Newsdata Finops
  service_category: API
  slug: newsdata-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/newsdata.png
layout: provider
modified: '2026-04-28'
name: NewsData
nav: Providers
network: true
overview: 'NewsData publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News, Media, Search, and Content.


  NewsData''s developer surface includes documentation, signup flow, pricing, engineering blog, and 4 more developer resources.'
plans:
- name: Newsdata Plans Pricing
  plan_count: 3
  slug: newsdata-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Newsdata Rate Limits
  slug: newsdata-rate-limits
score:
  band: emerging
  composite: 23.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/newsdata/refs/heads/main/screenshots/newsdata-2026-06-20T190303.png
security:
- kind: domain-security
  name: Newsdata Domain Security
  slug: newsdata-domain-security
  summary_line: TLSv1.3 · DMARC
slug: newsdata
tags:
- News
- Media
- Search
- Content
---
