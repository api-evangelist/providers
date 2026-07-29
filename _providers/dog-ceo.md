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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Dog Ceo Agentic Access
  operation_count: 10
  slug: dog-ceo-agentic-access
  summary_line: 10 operations
api_count: 4
apis:
- description: Operations for fetching images from a specific breed
  name: Dog CEO Breed API
  slug: dog-ceo-breed-api
- description: Operations for listing all available dog breeds
  name: Dog CEO Breeds API
  slug: dog-ceo-breeds-api
- description: Operations for fetching random dog images across all breeds
  name: Dog CEO Random API
  slug: dog-ceo-random-api
- description: Operations for fetching images from a specific sub-breed
  name: Dog CEO Sub-Breed API
  slug: dog-ceo-sub-breed-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dog-ceo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dog-ceo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dog.ceo/dog-api/
- group: docs
  title: ''
  type: Documentation
  url: https://dog.ceo/dog-api/documentation/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ElliottLandsborough
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/ElliottLandsborough/dog-ceo-api
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/jigsawpieces/dog-api-images
- group: company
  title: ''
  type: Blog
  url: https://dog.ceo/dog-api/about
- group: commercial
  title: ''
  type: Pricing
  url: https://dog.ceo/dog-api/about
- group: other
  title: ''
  type: X
  url: https://x.com/dog__CEO
- group: commercial
  title: ''
  type: Plans
  url: plans/dog-ceo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dog-ceo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dog-ceo-finops.yml
created: '2026-06-13'
description: Free REST API providing random dog images organized by breed and sub-breed from 120+ breeds. Backed by the Stanford Dogs Dataset and community-contributed photos, Dog CEO is widely used for learning HTTP concepts, API integration practice, and building dog-related applications. No authentication or API key is required. All endpoints return JSON with image URLs served via Vultr CDN. Open-source under the MIT license and community-funded via voluntary donations.
examples:
- key_count: 2
  name: Breed Images
  slug: breed-images
- key_count: 2
  name: Breeds List All
  slug: breeds-list-all
- key_count: 2
  name: Random Image
  slug: random-image
- key_count: 2
  name: Random Images Multiple
  slug: random-images-multiple
- key_count: 2
  name: Sub Breeds List
  slug: sub-breeds-list
finops:
- name: Dog Ceo Finops
  service_category: ''
  slug: dog-ceo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dog-ceo.png
json_schemas:
- name: Dog CEO API Breeds List Response
  property_count: 2
  slug: breeds-list-response
- name: Dog CEO API Image Response
  property_count: 2
  slug: dog-image-response
- name: Dog CEO API Multiple Images Response
  property_count: 2
  slug: dog-images-list-response
jsonld:
- class_count: 5
  name: Dog Ceo Context
  property_count: 5
  slug: dog-ceo-context
layout: provider
modified: '2026-06-13'
name: Dog CEO
nav: Providers
network: true
overview: 'Dog CEO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Breed API, Breeds API, Random API, and 1 more. Tagged areas include Dogs, Images, Animals, Open Source, and Free API.


  The Dog CEO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dog CEO''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Dog Ceo Plans Pricing
  plan_count: 1
  slug: dog-ceo-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Dog Ceo Rate Limits
  slug: dog-ceo-rate-limits
rules:
- name: Dog CEO API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: dog-ceo-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.5
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dog-ceo/refs/heads/main/screenshots/dog-ceo-2026-06-20T180123.png
security:
- kind: domain-security
  name: Dog Ceo Domain Security
  slug: dog-ceo-domain-security
  summary_line: TLSv1.3
slug: dog-ceo
tags:
- Dogs
- Images
- Animals
- Open Source
- Free API
- Machine Learning
- Education
website: https://dog.ceo/dog-api/
---
