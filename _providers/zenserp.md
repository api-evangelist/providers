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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Zenserp Agentic Access
  operation_count: 6
  slug: zenserp-agentic-access
  summary_line: 6 operations · 1 acting
api_count: 3
apis:
- description: Batch processing for multiple simultaneous queries.
  name: Zenserp Batch API
  slug: zenserp-batch-api
- description: Reference list endpoints for supported languages, countries, locations, and engines.
  name: Zenserp Lists API
  slug: zenserp-lists-api
- description: Core search endpoints supporting all search types and engines.
  name: Zenserp Search API
  slug: zenserp-search-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenserp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenserp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenserp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zenserp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.zenserp.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://zenserp.com/pricing-plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://zenserp.freshstatus.io
- group: company
  title: ''
  type: Blog
  url: https://zenserp.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zenserp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apilayer/
- group: other
  title: ''
  type: X
  url: https://twitter.com/apilayer
- group: commercial
  title: ''
  type: Plans
  url: plans/zenserp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenserp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zenserp-finops.yml
created: '2026-06-13'
description: Zenserp is a Google SERP API that enables developers to fetch live, structured search engine results in real time without interruption. The API supports web, image, video, news, shopping, maps, YouTube, Bing, Yandex, DuckDuckGo, reverse image, and trends search types across 200+ countries, returning clean JSON responses. It offers geolocation-based queries, batch endpoints, keyword search volume and CPC data, and a bulk index checker tool, with a 99.9% uptime SLA.
examples:
- key_count: 2
  name: Zenserp Batch Search Example
  slug: zenserp-batch-search-example
- key_count: 3
  name: Zenserp Image Search Example
  slug: zenserp-image-search-example
- key_count: 6
  name: Zenserp Web Search Example
  slug: zenserp-web-search-example
finops:
- name: Zenserp Finops
  service_category: ''
  slug: zenserp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenserp.png
json_schemas:
- name: Zenserp Search Response
  property_count: 14
  slug: zenserp-search-response
jsonld:
- class_count: 17
  name: Zenserp Context
  property_count: 59
  slug: zenserp-context
layout: provider
modified: '2026-06-13'
name: Zenserp
nav: Providers
network: true
overview: 'Zenserp publishes 3 APIs on the [APIs.io](https://apis.io/) network: Batch API, Lists API, and Search API. Tagged areas include SERP, Search Engine Results, Google Search, Web Scraping, and SEO.


  The Zenserp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zenserp''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Zenserp Plans Pricing
  plan_count: 6
  slug: zenserp-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 7
  name: Zenserp Rate Limits
  slug: zenserp-rate-limits
rules:
- name: Zenserp API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenserp-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.7
  delta: -0.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenserp/refs/heads/main/screenshots/zenserp-2026-06-20T201820.png
security:
- kind: authentication
  name: Zenserp Authentication
  slug: zenserp-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Zenserp Domain Security
  slug: zenserp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zenserp
tags:
- SERP
- Search Engine Results
- Google Search
- Web Scraping
- SEO
- Image Search
- News Search
- Shopping Search
- Maps
- YouTube Search
- Bing
- Yandex
- DuckDuckGo
- Geolocation
- Keyword Research
website: https://zenserp.com/
---
