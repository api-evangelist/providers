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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Currentsapi Agentic Access
  operation_count: 5
  slug: currentsapi-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Currents API Endpoint
  name: Currents API endpoint API
  slug: currentsapi-endpoint-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/currentsapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currentsapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/currentsapi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://currentsapi.services/en
- group: docs
  title: ''
  type: Documentation
  url: https://currentsapi.services/en/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/currentslab
- group: company
  title: ''
  type: Blog
  url: https://currentslab.github.io
- group: commercial
  title: ''
  type: Pricing
  url: https://currentsapi.services/en/product/price
- group: operate
  title: ''
  type: StatusPage
  url: https://currentsapi.services/en/status
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/currentsapi/refs/heads/main/plans/currentsapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/currentsapi/refs/heads/main/rate-limits/currentsapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/currentsapi/refs/heads/main/finops/currentsapi-finops.yml
created: '2026-06-13'
description: Latest news REST API aggregating real-time global news from 120,000+ sources worldwide with search, language filtering, category filtering, topic-based queries, and regional coverage across 70+ countries in 20+ languages.
examples:
- key_count: 3
  name: Available Categories
  slug: available-categories
- key_count: 3
  name: Available Languages
  slug: available-languages
- key_count: 2
  name: Latest News Response
  slug: latest-news-response
- key_count: 2
  name: Search Response
  slug: search-response
finops:
- name: Currentsapi Finops
  service_category: ''
  slug: currentsapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/currentsapi.png
json_schemas:
- name: News
  property_count: 9
  slug: news
- name: Results
  property_count: 2
  slug: results
layout: provider
modified: '2026-06-13'
name: Currents API
nav: Providers
network: true
overview: 'Currents API publishes 1 API on the [APIs.io](https://apis.io/) network: endpoint API. Tagged areas include News, Media, Search, REST, and Real-Time.


  The Currents API catalog on APIs.io includes 1 Spectral governance ruleset.


  Currents API''s developer surface includes authentication, documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Currentsapi Plans Pricing
  plan_count: 4
  slug: currentsapi-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 0
  name: Currentsapi Rate Limits
  slug: currentsapi-rate-limits
rules:
- name: Currents API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: currentsapi-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  delta: -5.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 32.3
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/currentsapi/refs/heads/main/screenshots/currentsapi-2026-06-20T175341.png
security:
- kind: authentication
  name: Currentsapi Authentication
  slug: currentsapi-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Currentsapi Domain Security
  slug: currentsapi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: currentsapi
tags:
- News
- Media
- Search
- REST
- Real-Time
website: https://currentsapi.services/en
---
