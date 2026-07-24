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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Manticore Agentic Access
  operation_count: 20
  slug: manticore-agentic-access
  summary_line: 20 operations · 20 acting
api_count: 3
apis:
- description: Operations regarding adding, updating or deleting documents
  name: Manticore Search Index API
  slug: manticore-index-api
- description: Operations about performing searches over tables
  name: Manticore Search Search API
  slug: manticore-search-api
- description: The utils API from Manticore Search — 1 operation(s) for utils.
  name: Manticore Search utils API
  slug: manticore-utils-api
artifact_total: 65
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/manticore-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/manticore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://manticoresearch.com/
- group: docs
  title: ''
  type: Documentation
  url: https://manual.manticoresearch.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/manticoresoftware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/manticore-software
- group: company
  title: ''
  type: Blog
  url: https://manticoresearch.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://manticoresearch.com/services/
- group: other
  title: ''
  type: X
  url: https://twitter.com/manticoresearch
- group: commercial
  title: ''
  type: Plans
  url: plans/manticore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/manticore-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/manticore-finops.yml
created: '2026-06-13'
description: Open-source search engine with a REST API compatible with Elasticsearch and MySQL protocols for full-text search, filtering, aggregations, and AI vector search. Manticore Search is a high-performance alternative to Elasticsearch, offering up to 2.83x faster big data search and 10.09x faster log analytics, running efficiently on minimal resources.
examples:
- key_count: 6
  name: Autocomplete
  slug: autocomplete
- key_count: 5
  name: Bulk
  slug: bulk
- key_count: 6
  name: Delete
  slug: delete
- key_count: 6
  name: Insert
  slug: insert
- key_count: 5
  name: Partial_Replace
  slug: partial_replace
- key_count: 5
  name: Percolate
  slug: percolate
- key_count: 6
  name: Replace
  slug: replace
- key_count: 6
  name: Search
  slug: search
- key_count: 6
  name: Sql
  slug: sql
- key_count: 6
  name: Update
  slug: update
finops:
- name: Manticore Finops
  service_category: ''
  slug: manticore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/manticore.png
json_schemas:
- name: _match
  property_count: 3
  slug: _match
- name: aggComposite
  property_count: 2
  slug: aggComposite
- name: aggCompositeSource
  property_count: 1
  slug: aggCompositeSource
- name: aggCompositeTerm
  property_count: 1
  slug: aggCompositeTerm
- name: aggDateHistogram
  property_count: 4
  slug: aggDateHistogram
- name: aggHistogram
  property_count: 4
  slug: aggHistogram
- name: aggTerms
  property_count: 2
  slug: aggTerms
- name: aggregation
  property_count: 0
  slug: aggregation
- name: autocompleteRequest
  property_count: 3
  slug: autocompleteRequest
- name: boolFilter
  property_count: 3
  slug: boolFilter
- name: bulkResponse
  property_count: 5
  slug: bulkResponse
- name: deleteDocumentRequest
  property_count: 4
  slug: deleteDocumentRequest
- name: deleteResponse
  property_count: 5
  slug: deleteResponse
- name: errorResponse
  property_count: 2
  slug: errorResponse
- name: fulltextFilter
  property_count: 4
  slug: fulltextFilter
- name: geoDistance
  property_count: 4
  slug: geoDistance
- name: highlight
  property_count: 0
  slug: highlight
- name: highlightFieldOption
  property_count: 5
  slug: highlightFieldOption
- name: highlightFields
  property_count: 0
  slug: highlightFields
- name: hitsHits
  property_count: 8
  slug: hitsHits
- name: insertDocumentRequest
  property_count: 4
  slug: insertDocumentRequest
- name: join
  property_count: 0
  slug: join
- name: joinCond
  property_count: 4
  slug: joinCond
- name: joinOn
  property_count: 0
  slug: joinOn
- name: knn
  property_count: 7
  slug: knn
- name: match_all
  property_count: 1
  slug: match_all
- name: percolateRequest
  property_count: 1
  slug: percolateRequest
- name: queryFilter
  property_count: 0
  slug: queryFilter
- name: queryFilterAlias1
  property_count: 0
  slug: queryFilterAlias1
- name: queryFilterAlias2
  property_count: 0
  slug: queryFilterAlias2
- name: range
  property_count: 4
  slug: range
- name: replaceDocumentRequest
  property_count: 1
  slug: replaceDocumentRequest
- name: responseError
  property_count: 0
  slug: responseError
- name: responseErrorDetails
  property_count: 3
  slug: responseErrorDetails
- name: responseErrorText
  property_count: 0
  slug: responseErrorText
- name: searchQuery
  property_count: 0
  slug: searchQuery
- name: searchRequest
  property_count: 15
  slug: searchRequest
- name: searchResponse
  property_count: 7
  slug: searchResponse
- name: sourceRules
  property_count: 2
  slug: sourceRules
- name: sqlObjResponse
  property_count: 3
  slug: sqlObjResponse
- name: sqlRawResponse
  property_count: 0
  slug: sqlRawResponse
- name: sqlResponse
  property_count: 0
  slug: sqlResponse
- name: successResponse
  property_count: 6
  slug: successResponse
- name: updateDocumentRequest
  property_count: 5
  slug: updateDocumentRequest
- name: updateResponse
  property_count: 4
  slug: updateResponse
jsonld:
- class_count: 5
  name: Manticore Context
  property_count: 0
  slug: manticore
layout: provider
modified: '2026-06-13'
name: Manticore Search
nav: Providers
network: true
overview: 'Manticore Search publishes 3 APIs on the [APIs.io](https://apis.io/) network: Index API, Search API, and utils API. Tagged areas include Search, Full-Text Search, Vector Search, Elasticsearch Compatible, and Open Source.


  The Manticore Search catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Manticore Search''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Manticore Plans Pricing
  plan_count: 3
  slug: manticore-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 1
  name: Manticore Rate Limits
  slug: manticore-rate-limits
rules:
- name: Manticore Search API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: manticore-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.5
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 48.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/manticore/refs/heads/main/screenshots/manticore-2026-06-20T184929.png
security:
- kind: domain-security
  name: Manticore Domain Security
  slug: manticore-domain-security
  summary_line: TLSv1.3 · DMARC
slug: manticore
tags:
- Search
- Full-Text Search
- Vector Search
- Elasticsearch Compatible
- Open Source
- Database
website: https://manticoresearch.com/
---
