---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Isbndb Agentic Access
  operation_count: 16
  slug: isbndb-agentic-access
  summary_line: 16 operations · 1 acting
api_count: 8
apis:
- description: Author endpoints
  name: ISBNdb Author API
  slug: isbndb-author-api
- description: Book endpoints
  name: ISBNdb Books API
  slug: isbndb-books-api
- description: Feed endpoints for incremental sync
  name: ISBNdb Feed API
  slug: isbndb-feed-api
- description: API key management
  name: ISBNdb Key API
  slug: isbndb-key-api
- description: Publisher endpoints
  name: ISBNdb Publisher API
  slug: isbndb-publisher-api
- description: Legacy search endpoints (deprecated)
  name: ISBNdb Search API
  slug: isbndb-search-api
- description: Database statistics
  name: ISBNdb Stats API
  slug: isbndb-stats-api
- description: Subject endpoints
  name: ISBNdb Subject API
  slug: isbndb-subject-api
artifact_total: 21
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/isbndb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/isbndb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/isbndb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://isbndb.com
- group: docs
  title: ''
  type: Documentation
  url: https://isbndb.com/api-documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://isbndb.com/isbn-database
- group: company
  title: ''
  type: Blog
  url: https://isbndb.com/blog/
- group: other
  title: ''
  type: X
  url: https://x.com/ISBNdb_com
- group: commercial
  title: ''
  type: Plans
  url: plans/isbndb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/isbndb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/isbndb-finops.yml
created: '2026-06-13'
description: ISBNdb is the world's largest book database REST API providing access to metadata for over 110 million books and publications. Search by ISBN (ISBN-10 or ISBN-13), title, author, publisher, or subject to retrieve up to 19 data points per book including cover images, publication dates, descriptions, and real-time pricing. The API supports bulk lookups of up to 1,000 ISBNs per request on eligible plans.
examples:
- key_count: 6
  name: Author Details Response
  slug: author-details-response
- key_count: 1
  name: Book Get Response
  slug: book-get-response
- key_count: 1
  name: Books Bulk Request
  slug: books-bulk-request
- key_count: 3
  name: Books Search Response
  slug: books-search-response
finops:
- name: Isbndb Finops
  service_category: ''
  slug: isbndb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/isbndb.png
json_schemas:
- name: Book
  property_count: 26
  slug: book
jsonld:
- class_count: 2
  name: Isbndb Context
  property_count: 33
  slug: isbndb-context
layout: provider
modified: '2026-06-13'
name: ISBNdb
nav: Providers
network: true
overview: 'ISBNdb publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Author API, Books API, Feed API, and 5 more. Tagged areas include Books, ISBN, Publishing, Metadata, and Library.


  The ISBNdb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ISBNdb''s developer surface includes authentication, documentation, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Isbndb Plans Pricing
  plan_count: 5
  slug: isbndb-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 10
  name: Isbndb Rate Limits
  slug: isbndb-rate-limits
rules:
- name: ISBNdb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: isbndb-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/isbndb/refs/heads/main/screenshots/isbndb-2026-06-20T183614.png
security:
- kind: authentication
  name: Isbndb Authentication
  slug: isbndb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Isbndb Domain Security
  slug: isbndb-domain-security
  summary_line: TLSv1.3 · DMARC
slug: isbndb
tags:
- Books
- ISBN
- Publishing
- Metadata
- Library
- Bibliography
website: https://isbndb.com
---
