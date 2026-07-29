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
- acting_count: 1
  human_in_the_loop: 0
  name: Depositphotos Agentic Access
  operation_count: 1
  slug: depositphotos-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 3
apis:
- description: The Enterprise API provides organizations with full content licensing workflows including searching 331M+ assets, licensing items, invoice management, license transfer, complimentary downloads, and AI
  name: Depositphotos Enterprise API
  slug: depositphotos-enterprise-api
- description: The Depositphotos Suite API bundles a graphic design editor, access to the 331M+ stock library, and generative AI tools (AI Assistant, AI Image Generator) into a single integration point for embedding
  name: Depositphotos Suite API
  slug: depositphotos-suite-api
- description: The Authentication API from Depositphotos — 1 operation(s) for authentication.
  name: Depositphotos Authentication API
  slug: depositphotos-authentication-api
artifact_total: 17
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/depositphotos-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/depositphotos-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/depositphotos-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://depositphotos.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.depositphotos.com/doc/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/depositphotos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/depositphotos
- group: company
  title: ''
  type: Blog
  url: https://blog.depositphotos.com
- group: commercial
  title: ''
  type: Pricing
  url: https://depositphotos.com/api-plans.html
- group: operate
  title: ''
  type: StatusPage
  url: https://depositphotos.com/status
- group: other
  title: ''
  type: X
  url: https://x.com/depositphotos
- group: commercial
  title: ''
  type: Plans
  url: plans/depositphotos-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/depositphotos-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/depositphotos-finops.yml
created: '2026-06-13'
description: Depositphotos is a stock photo, vector, and video marketplace offering a REST API for searching and downloading images, managing subscriptions, lightboxes, and contributor portfolios. The API supports Partner and Reseller programs, an Enterprise solution with advanced licensing and invoicing, and an AI Suite for generative image creation and graphic editing. All API calls use HTTP GET/POST requests with JSON responses and session-based authentication.
examples:
- key_count: 4
  name: License Item Enterprise
  slug: license-item-enterprise
- key_count: 4
  name: Login Request
  slug: login-request
- key_count: 4
  name: Search Request
  slug: search-request
finops:
- name: Depositphotos Finops
  service_category: ''
  slug: depositphotos-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/depositphotos.png
json_schemas:
- name: APIResponse
  property_count: 6
  slug: api-response
- name: MediaItem
  property_count: 22
  slug: media-item
- name: SearchRequest
  property_count: 25
  slug: search-request
jsonld:
- class_count: 0
  name: Depositphotos Context
  property_count: 0
  slug: depositphotos
layout: provider
modified: '2026-06-13'
name: Depositphotos
nav: Providers
network: true
overview: 'Depositphotos publishes 1 API on the [APIs.io](https://apis.io/) network: Authentication API. Tagged areas include Stock Photos, Images, Videos, Vectors, and Media.


  The Depositphotos catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Depositphotos'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Depositphotos Plans Pricing
  plan_count: 6
  slug: depositphotos-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 6
  name: Depositphotos Rate Limits
  slug: depositphotos-rate-limits
rules:
- name: Depositphotos API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: depositphotos-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.6
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/depositphotos/refs/heads/main/screenshots/depositphotos-2026-06-20T175928.png
security:
- kind: authentication
  name: Depositphotos Authentication
  slug: depositphotos-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Depositphotos Domain Security
  slug: depositphotos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: depositphotos
tags:
- Stock Photos
- Images
- Videos
- Vectors
- Media
- Creative Assets
- Generative AI
website: https://depositphotos.com
---
