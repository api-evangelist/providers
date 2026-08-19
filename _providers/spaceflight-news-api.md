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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
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
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Spaceflight News Api Agentic Access
  operation_count: 7
  slug: spaceflight-news-api-agentic-access
  summary_line: 7 operations
api_count: 4
apis:
- description: Space news article operations
  name: Spaceflight News API Articles API
  slug: spaceflight-news-api-articles-api
- description: Space blog post operations
  name: Spaceflight News API Blogs API
  slug: spaceflight-news-api-blogs-api
- description: API metadata operations
  name: Spaceflight News API Info API
  slug: spaceflight-news-api-info-api
- description: Space mission report operations
  name: Spaceflight News API Reports API
  slug: spaceflight-news-api-reports-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spaceflight News Articles API
  slug: open-spaceflight-news-api-articles-api
- collection_type: open
  name: Spaceflight News Articles Blogs API
  slug: open-spaceflight-news-api-blogs-api
- collection_type: open
  name: Spaceflight News Articles Info API
  slug: open-spaceflight-news-api-info-api
- collection_type: open
  name: Spaceflight News Articles Reports API
  slug: open-spaceflight-news-api-reports-api
- collection_type: open
  name: Spaceflight News API
  slug: open-spaceflight-news-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spaceflight-news-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spaceflight-news-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.spaceflightnewsapi.net
- group: docs
  title: ''
  type: Documentation
  url: https://api.spaceflightnewsapi.net/v4/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thespacedevs/spaceflightnewsapi
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/thespacedevs
created: '2024-11-07'
description: The Spaceflight News API (SNAPI) is a free, open REST API that aggregates space-related news, blogs, and reports from over 43 sources including NASA, SpaceX, Reuters, NASASpaceflight, and Spaceflight Now. It provides paginated access to articles, blogs, and reports with integration to Launch Library 2 for linking news to specific launches and events.
examples:
- key_count: 4
  name: Spaceflight News Api List Articles Example
  slug: spaceflight-news-api-list-articles-example
finops:
- name: Spaceflight News Api Finops
  service_category: API
  slug: spaceflight-news-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spaceflight-news-api.png
json_schemas:
- name: Spaceflight News API Article
  property_count: 12
  slug: spaceflight-news-api-article
json_structures:
- name: Spaceflight News Api Article Structure
  property_count: 0
  slug: spaceflight-news-api-article-structure
jsonld:
- class_count: 14
  name: Spaceflight News Api Context
  property_count: 11
  slug: spaceflight-news-api-context
layout: provider
modified: '2026-05-19'
name: Spaceflight News API
nav: Providers
network: true
overview: 'Spaceflight News API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Blogs API, Info API, and 1 more. Tagged areas include News, Space, Spaceflight, and Media.


  The Spaceflight News API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spaceflight News API''s developer surface includes documentation, GitHub presence, support, and 3 more developer resources.'
plans:
- name: Spaceflight News Api Plans Pricing
  plan_count: 3
  slug: spaceflight-news-api-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 5
  name: Spaceflight News Api Rate Limits
  slug: spaceflight-news-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spaceflight News API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spaceflight-news-api-jsonschema-spectral-rules
- effective_rule_count: 9
  extends: []
  name: Spaceflight News API API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 3
    warn: 5
  slug: spaceflight-news-api-rules
score:
  band: thin
  composite: 27.4
  delta: -10.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 64.7
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/spaceflight-news-api/refs/heads/main/screenshots/spaceflight-news-api-2026-06-20T194235.png
security:
- kind: domain-security
  name: Spaceflight News Api Domain Security
  slug: spaceflight-news-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spaceflight-news-api
tags:
- News
- Space
- Spaceflight
- Media
website: https://www.spaceflightnewsapi.net
---
