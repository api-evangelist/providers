---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Serper Agentic Access
  operation_count: 10
  slug: serper-agentic-access
  summary_line: 10 operations · 10 acting
api_count: 10
apis:
- description: Search autocomplete suggestions
  name: Serper Autocomplete API
  slug: serper-autocomplete-api
- description: Image search results
  name: Serper Images API
  slug: serper-images-api
- description: Maps and location search
  name: Serper Maps API
  slug: serper-maps-api
- description: News search results
  name: Serper News API
  slug: serper-news-api
- description: Patent search results
  name: Serper Patents API
  slug: serper-patents-api
- description: Local business and place search
  name: Serper Places API
  slug: serper-places-api
- description: Academic publication search
  name: Serper Scholar API
  slug: serper-scholar-api
- description: Web search results
  name: Serper Search API
  slug: serper-search-api
- description: Product and shopping search results
  name: Serper Shopping API
  slug: serper-shopping-api
- description: Video search results
  name: Serper Videos API
  slug: serper-videos-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/serper-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/serper-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/serper-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://serper.dev
- group: docs
  title: ''
  type: Documentation
  url: https://serper.dev
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Serper-API
- group: other
  title: ''
  type: X
  url: https://x.com/serperapi
- group: commercial
  title: ''
  type: Pricing
  url: https://serper.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/serper-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/serper-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/serper-finops.yml
created: '2026-06-13'
description: Serper is the world's fastest and most affordable Google Search API, delivering real-time SERP data in 1-2 seconds via a simple REST interface. It supports web search, images, news, maps, places, videos, shopping, scholar, patents, and autocomplete — all returned as structured JSON. Widely used in AI agents, LLM pipelines, and SEO tooling, Serper uses a credit-based model with 2,500 free queries and volume pricing down to $0.30 per 1,000 requests.
examples:
- key_count: 2
  name: Serper Autocomplete Example
  slug: serper-autocomplete-example
- key_count: 2
  name: Serper Image Search Example
  slug: serper-image-search-example
- key_count: 2
  name: Serper News Search Example
  slug: serper-news-search-example
- key_count: 2
  name: Serper Scholar Search Example
  slug: serper-scholar-search-example
- key_count: 2
  name: Serper Shopping Search Example
  slug: serper-shopping-search-example
- key_count: 2
  name: Serper Web Search Example
  slug: serper-web-search-example
finops:
- name: Serper Finops
  service_category: ''
  slug: serper-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/serper.png
json_schemas:
- name: Serper Search Request
  property_count: 8
  slug: serper-search-request
- name: Serper Search Response
  property_count: 6
  slug: serper-search-response
jsonld:
- class_count: 53
  name: Serper Context
  property_count: 30
  slug: serper-context
layout: provider
modified: '2026-06-13'
name: Serper
nav: Providers
network: true
overview: 'Serper publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Images API, Maps API, and 7 more. Tagged areas include Search, SERP, Google Search, AI, and LLM.


  The Serper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Serper''s developer surface includes authentication, documentation, pricing, and 8 more developer resources.'
plans:
- name: Serper Plans Pricing
  plan_count: 5
  slug: serper-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 0
  name: Serper Rate Limits
  slug: serper-rate-limits
rules:
- name: Serper API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: serper-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.2
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/serper/refs/heads/main/screenshots/serper-2026-06-20T193723.png
security:
- kind: authentication
  name: Serper Authentication
  slug: serper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Serper Domain Security
  slug: serper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: serper
tags:
- Search
- SERP
- Google Search
- AI
- LLM
- SEO
- Images
- News
- Maps
- Shopping
website: https://serper.dev
---
