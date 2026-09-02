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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Isbndb Agentic Access
  operation_count: 16
  slug: isbndb-agentic-access
  summary_line: 16 operations · 1 acting
api_count: 2
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
artifact_total: 29
collections:
- collection_type: open
  name: ISBNdb API v2 Author API
  slug: open-isbndb-author-api
- collection_type: open
  name: ISBNdb API v2 Books API
  slug: open-isbndb-books-api
- collection_type: open
  name: ISBNdb API v2 Feed API
  slug: open-isbndb-feed-api
- collection_type: open
  name: ISBNdb API v2 Key API
  slug: open-isbndb-key-api
- collection_type: open
  name: ISBNdb API v2 Publisher API
  slug: open-isbndb-publisher-api
- collection_type: open
  name: ISBNdb API v2 Search API
  slug: open-isbndb-search-api
- collection_type: open
  name: ISBNdb API v2 Stats API
  slug: open-isbndb-stats-api
- collection_type: open
  name: ISBNdb API v2 Subject API
  slug: open-isbndb-subject-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/isbndb-capability-edges.yml
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/api-evangelist/isbndb/collection/86oo60r/isbndb-api
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/isbndb
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
  property_count: 25
  slug: book
jsonld:
- class_count: 2
  name: Isbndb Context
  property_count: 32
  slug: isbndb-context
layout: provider
modified: '2026-06-13'
name: ISBNdb
nav: Providers
network: true
overview: 'ISBNdb publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Author API, Books API, Feed API, and 5 more. Tagged areas include Books, ISBN, Publishing, Metadata, and Library.


  The ISBNdb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ISBNdb''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Isbndb Plans Pricing
  plan_count: 5
  slug: isbndb-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 10
  name: Isbndb Rate Limits
  slug: isbndb-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ISBNdb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: isbndb-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 39.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 55.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 31.6
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
