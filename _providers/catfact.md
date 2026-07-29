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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Catfact Agentic Access
  operation_count: 3
  slug: catfact-agentic-access
  summary_line: 3 operations
api_count: 3
apis:
- description: The Breeds API from Cat Facts API — 1 operation(s) for breeds.
  name: Cat Facts API Breeds API
  slug: catfact-breeds-api
- description: The Fact API from Cat Facts API — 1 operation(s) for fact.
  name: Cat Facts API Fact API
  slug: catfact-fact-api
- description: The Facts API from Cat Facts API — 1 operation(s) for facts.
  name: Cat Facts API Facts API
  slug: catfact-facts-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/catfact-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/catfact-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catfact.ninja/
- group: docs
  title: ''
  type: Documentation
  url: https://catfact.ninja/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/alexwohlbruck/cat-facts
- group: commercial
  title: ''
  type: Plans
  url: plans/catfact-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/catfact-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/catfact-finops.yml
created: '2026-06-13'
description: Free REST API providing random cat facts, breed information, and cat-related trivia for developers building fun applications and learning APIs. No authentication required; CORS enabled for frontend use. Endpoints return paginated JSON data with configurable limits and max-length filters.
examples:
- key_count: 12
  name: Breeds List Response
  slug: breeds-list-response
- key_count: 2
  name: Fact Response
  slug: fact-response
- key_count: 12
  name: Facts List Response
  slug: facts-list-response
finops:
- name: Catfact Finops
  service_category: ''
  slug: catfact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/catfact.png
json_schemas:
- name: BreedList
  property_count: 12
  slug: breed-list
- name: Breed
  property_count: 5
  slug: breed
- name: FactList
  property_count: 12
  slug: fact-list
- name: Fact
  property_count: 2
  slug: fact
jsonld:
- class_count: 2
  name: context Context
  property_count: 19
  slug: context
layout: provider
modified: '2026-06-13'
name: Cat Facts API
nav: Providers
network: true
overview: 'Cat Facts API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Breeds API, Fact API, and Facts API. Tagged areas include Cat Facts, Trivia, Fun, Learning, and Free.


  The Cat Facts API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cat Facts API''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Catfact Plans Pricing
  plan_count: 1
  slug: catfact-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Catfact Rate Limits
  slug: catfact-rate-limits
rules:
- name: Cat Facts API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: catfact-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.6
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.8
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/catfact/refs/heads/main/screenshots/catfact-2026-06-20T174051.png
security:
- kind: domain-security
  name: Catfact Domain Security
  slug: catfact-domain-security
  summary_line: TLSv1.3
slug: catfact
tags:
- Cat Facts
- Trivia
- Fun
- Learning
- Free
website: https://catfact.ninja/
---
