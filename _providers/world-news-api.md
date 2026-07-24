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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: World News Api Agentic Access
  operation_count: 10
  slug: world-news-api-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 3
apis:
- description: The Geo API from World News API — 1 operation(s) for geo.
  name: World News API Geo API
  slug: world-news-api-geo-api
- description: The News API from World News API — 6 operation(s) for news.
  name: World News API News API
  slug: world-news-api-news-api
- description: The Sources API from World News API — 3 operation(s) for sources.
  name: World News API Sources API
  slug: world-news-api-sources-api
artifact_total: 10
collections:
- collection_type: open
  name: World News API
  slug: open-world-news-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/world-news-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/world-news-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/world-news-api-authentication.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://worldnewsapi.com/llms.txt
created: '2025-02-09'
description: The World News API gives you access to thousands of news sources in over 90 languages from over 228 countries. News are semantically tagged allowing for semantic news search like never before.
finops:
- name: World News Api Finops
  service_category: API
  slug: world-news-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/world-news-api.png
layout: provider
modified: '2026-05-19'
name: World News API
nav: Providers
network: true
overview: 'World News API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Geo API, News API, and Sources API.


  World News API''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: World News Api Plans Pricing
  plan_count: 3
  slug: world-news-api-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: World News Api Rate Limits
  slug: world-news-api-rate-limits
score:
  band: thin
  composite: 31.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.1
    developer_ergonomics: 10.9
    discoverability: 42.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/world-news-api/refs/heads/main/screenshots/world-news-api-2026-06-20T201617.png
security:
- kind: authentication
  name: World News Api Authentication
  slug: world-news-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: World News Api Domain Security
  slug: world-news-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: world-news-api
---
