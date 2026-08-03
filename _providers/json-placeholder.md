---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Json Placeholder Agentic Access
  operation_count: 5
  slug: json-placeholder-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Posts API from JSONPlaceholder — 2 operation(s) for posts.
  name: JSONPlaceholder Posts API
  slug: json-placeholder-posts-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/json-placeholder-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/json-placeholder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jsonplaceholder.typicode.com
- group: docs
  title: ''
  type: Documentation
  url: https://jsonplaceholder.typicode.com/guide/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/typicode
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/typicode/jsonplaceholder
- group: company
  title: ''
  type: Blog
  url: https://blog.typicode.com
- group: commercial
  title: ''
  type: Pricing
  url: https://jsonplaceholder.typicode.com
- group: other
  title: ''
  type: X
  url: https://x.com/typicode
- group: commercial
  title: ''
  type: Plans
  url: plans/json-placeholder-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/json-placeholder-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/json-placeholder-finops.yml
created: '2026-06-13'
description: Free fake REST API for testing and prototyping providing mock data for posts, comments, albums, photos, todos, and users without any setup. Handles approximately 3 billion requests per month and supports all standard HTTP methods with CORS and JSONP support.
examples:
- key_count: 3
  name: Create Post Request
  slug: create-post-request
- key_count: 4
  name: Create Post Response
  slug: create-post-response
finops:
- name: Json Placeholder Finops
  service_category: ''
  slug: json-placeholder-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/json-placeholder.png
json_schemas:
- name: Post
  property_count: 4
  slug: post
jsonld:
- class_count: 1
  name: context Context
  property_count: 4
  slug: context
layout: provider
modified: '2026-06-13'
name: JSONPlaceholder
nav: Providers
network: true
overview: 'JSONPlaceholder publishes 1 API on the [APIs.io](https://apis.io/) network: Posts API. Tagged areas include Fake API, Testing, Prototyping, Mock Data, and REST.


  The JSONPlaceholder catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JSONPlaceholder''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Json Placeholder Plans Pricing
  plan_count: 1
  slug: json-placeholder-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 0
  name: Json Placeholder Rate Limits
  slug: json-placeholder-rate-limits
rules:
- name: JSONPlaceholder API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: json-placeholder-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/json-placeholder/refs/heads/main/screenshots/json-placeholder-2026-06-20T183815.png
security:
- kind: domain-security
  name: Json Placeholder Domain Security
  slug: json-placeholder-domain-security
  summary_line: TLSv1.3
slug: json-placeholder
tags:
- Fake API
- Testing
- Prototyping
- Mock Data
- REST
- Open Source
website: https://jsonplaceholder.typicode.com
---
