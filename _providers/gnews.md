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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gnews Agentic Access
  operation_count: 2
  slug: gnews-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: The Headlines API from GNews — 1 operation(s) for headlines.
  name: GNews Headlines API
  slug: gnews-headlines-api
- description: The Search API from GNews — 1 operation(s) for search.
  name: GNews Search API
  slug: gnews-search-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GNews Headlines API
  slug: open-gnews-headlines-api
- collection_type: open
  name: GNews Headlines Search API
  slug: open-gnews-search-api
- collection_type: open
  name: GNews API
  slug: open-gnews
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gnews-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gnews-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gnews-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gnews
- group: company
  title: ''
  type: Website
  url: https://gnews.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gnews.io/
- group: start
  title: ''
  type: Signup
  url: https://gnews.io/#register
- group: commercial
  title: ''
  type: Pricing
  url: https://gnews.io/#pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://gnews.io/llms.txt
created: '2025-02-09'
description: A REST News API to search current and historical articles and retrieve trending news in over 22 languages across 30 countries from 60,000+ sources.
finops:
- name: Gnews Finops
  service_category: API
  slug: gnews-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gnews.png
layout: provider
modified: '2026-05-19'
name: GNews
nav: Providers
network: true
overview: 'GNews publishes 2 APIs on the [APIs.io](https://apis.io/) network: Headlines API and Search API. Tagged areas include Articles, Headlines, News, and Search.


  GNews'' developer surface includes authentication, documentation, signup flow, pricing, and 5 more developer resources.'
plans:
- name: Gnews Plans Pricing
  plan_count: 3
  slug: gnews-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Gnews Rate Limits
  slug: gnews-rate-limits
score:
  band: thin
  composite: 34.8
  delta: 2.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 33.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gnews/refs/heads/main/screenshots/gnews-2026-06-20T181935.png
security:
- kind: authentication
  name: Gnews Authentication
  slug: gnews-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gnews Domain Security
  slug: gnews-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gnews
tags:
- Articles
- Headlines
- News
- Search
website: https://gnews.io/
---
