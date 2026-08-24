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
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-24'
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
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TheNews news API
  slug: open-thenewsapi-news-api
- collection_type: open
  name: TheNews news sources API
  slug: open-thenewsapi-sources-api
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
overview: 'TheNewsAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network: news API and sources API. Tagged areas include News, Articles, Headlines, Media, and Aggregation.


  The TheNewsAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  TheNewsAPI''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Plans
  plan_count: 5
  slug: plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: TheNewsAPI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thenewsapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 58.0
    developer_ergonomics: 11.9
    discoverability: 70.4
    governance: 9.8
    operational_transparency: 15.8
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
- News
- Articles
- Headlines
- Media
- Aggregation
- Real-Time
website: https://www.thenewsapi.com
---
