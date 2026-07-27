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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Army Agentic Access
  operation_count: 4
  slug: us-army-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: The US Army provides open data resources through data.gov and maintains open source projects through the US Army Research Laboratory GitHub organization. Army data includes geospatial datasets, resear
  name: US Army Open Data
  slug: us-army-open-data
- description: The Articles API from US Army — 2 operation(s) for articles.
  name: US Army Articles API
  slug: us-army-articles-api
- description: The Events API from US Army — 1 operation(s) for events.
  name: US Army Events API
  slug: us-army-events-api
- description: The News API from US Army — 1 operation(s) for news.
  name: US Army News API
  slug: us-army-news-api
artifact_total: 16
collections:
- collection_type: open
  name: US Army Public API
  slug: open-us-army-public
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-army-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-army-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-army
created: '2024-11-21'
description: The US Army is the largest branch of the United States military and is responsible for conducting ground combat operations. Its mission is to defend the nation and support humanitarian, peacekeeping, and training missions worldwide. The Army maintains a public API at api.army.mil providing access to news articles, events, and official content using OpenAPI 3 specification.
examples:
- key_count: 2
  name: Us Army Public Get Article By Id Example
  slug: us-army-public-get-article-by-id-example
finops:
- name: Us Army Finops
  service_category: API
  slug: us-army-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-army.png
json_schemas:
- name: US Army Article
  property_count: 11
  slug: us-army-article
json_structures:
- name: Us Army Article Structure
  property_count: 0
  slug: us-army-article-structure
jsonld:
- class_count: 20
  name: Us Army Context
  property_count: 7
  slug: us-army-context
layout: provider
modified: '2026-05-19'
name: US Army
nav: Providers
network: true
overview: 'US Army publishes 3 APIs on the [APIs.io](https://apis.io/) network: Articles API, Events API, and News API. Tagged areas include Army, Federal Government, Military, Defense, and Open Data.


  The US Army catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Us Army Plans Pricing
  plan_count: 3
  slug: us-army-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Us Army Rate Limits
  slug: us-army-rate-limits
rules:
- name: US Army API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-army-jsonschema-spectral-rules
- name: US Army API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 4
  slug: us-army-public-rules
score:
  band: thin
  composite: 42.0
  delta: 2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.2
    developer_ergonomics: 0.0
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 39.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-army/refs/heads/main/screenshots/us-army-2026-06-20T200556.png
security:
- kind: domain-security
  name: Us Army Domain Security
  slug: us-army-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: us-army
tags:
- Army
- Federal Government
- Military
- Defense
- Open Data
- News
---
