---
access_model:
  confidence: high
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Valueserp Agentic Access
  operation_count: 6
  slug: valueserp-agentic-access
  summary_line: 6 operations
api_count: 6
apis:
- description: Google Image search results.
  name: ValueSERP Images API
  slug: valueserp-images-api
- description: Google News article results.
  name: ValueSERP News API
  slug: valueserp-news-api
- description: Google Maps and local places search results.
  name: ValueSERP Places API
  slug: valueserp-places-api
- description: Google product knowledge panel data (deprecated).
  name: ValueSERP Product API
  slug: valueserp-product-api
- description: Google organic web search results.
  name: ValueSERP Search API
  slug: valueserp-search-api
- description: Google Shopping product results.
  name: ValueSERP Shopping API
  slug: valueserp-shopping-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/valueserp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/valueserp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/valueserp-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trajectdata.com/serp/value-serp-api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trajectdata.com/valueserp
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/joejoinerr/python-valueserp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traject-data/
- group: company
  title: ''
  type: Blog
  url: https://trajectdata.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://trajectdata.com/serp/value-serp-api/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://valueserp.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/valueserp
- group: commercial
  title: ''
  type: Plans
  url: plans/valueserp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/valueserp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/valueserp-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/vocabulary/valueserp-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/json-ld/valueserp-context.jsonld
created: 2026-06-13
description: ValueSERP is a real-time Google Search API providing SERP results, image search, news search, shopping results, places, and local pack data via a simple REST interface with JSON output. Operated by Traject Data, it offers low-cost, high-reliability SERP data with no queues, batch processing capabilities, and pay-as-you-go or subscription pricing starting at $50/month for 25,000 searches.
examples:
- key_count: 4
  name: Valueserp News Search Example
  slug: valueserp-news-search-example
- key_count: 4
  name: Valueserp Organic Search Example
  slug: valueserp-organic-search-example
- key_count: 4
  name: Valueserp Places Search Example
  slug: valueserp-places-search-example
- key_count: 4
  name: Valueserp Shopping Search Example
  slug: valueserp-shopping-search-example
finops:
- name: Valueserp Finops
  service_category: ''
  slug: valueserp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/valueserp.png
json_schemas:
- name: ValueSERP Search Request
  property_count: 46
  slug: valueserp-search-request
- name: ValueSERP Search Response
  property_count: 16
  slug: valueserp-search-response
jsonld:
- class_count: 0
  name: Valueserp Context
  property_count: 120
  slug: valueserp-context
layout: provider
modified: 2026-06-13
name: ValueSERP
nav: Providers
network: true
overview: 'ValueSERP publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Images API, News API, Places API, and 3 more. Tagged areas include SERP, Search Engine Results, Google Search, Search API, and SEO.


  The ValueSERP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ValueSERP''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Valueserp Plans Pricing
  plan_count: 12
  slug: valueserp-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 11
  name: Valueserp Rate Limits
  slug: valueserp-rate-limits
rules:
- name: ValueSERP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: valueserp-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 75.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/valueserp/refs/heads/main/screenshots/valueserp-2026-06-20T200802.png
security:
- kind: authentication
  name: Valueserp Authentication
  slug: valueserp-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Valueserp Domain Security
  slug: valueserp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: valueserp
tags:
- SERP
- Search Engine Results
- Google Search
- Search API
- SEO
- Web Scraping
- Shopping Results
- News Search
- Image Search
- Local Search
- Places
- Data API
website: https://trajectdata.com/serp/value-serp-api/
---
