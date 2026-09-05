---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Solr Agentic Access
  operation_count: 14
  slug: solr-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 1
apis:
- description: HTTP/REST API for Apache Solr providing endpoints for querying, indexing, schema management, collections administration, and core administration. The v2 API uses RESTful resource paths under /api whil
  name: Apache Solr REST API
  slug: rest-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Cluster-level collection management
  name: Apache Solr Collections API
  slug: solr-collections-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Legacy Collections admin handler endpoints
  name: Apache Solr CollectionsAdminHandler API
  slug: solr-collectionsadminhandler-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Per-collection configuration operations
  name: Apache Solr Config API
  slug: solr-config-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Node-level core administration
  name: Apache Solr Cores API
  slug: solr-cores-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Per-collection schema operations
  name: Apache Solr Schema API
  slug: solr-schema-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Shard management for collections
  name: Apache Solr Shards API
  slug: solr-shards-api
- baseURL: http://localhost:8983/api
  baseurl_source: declared
  description: Per-collection document update operations
  name: Apache Solr Update API
  slug: solr-update-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Solr REST Collections API
  slug: open-solr-collections-api
- collection_type: open
  name: Apache Solr REST Collections CollectionsAdminHandler API
  slug: open-solr-collectionsadminhandler-api
- collection_type: open
  name: Apache Solr REST Collections Config API
  slug: open-solr-config-api
- collection_type: open
  name: Apache Solr REST Collections Cores API
  slug: open-solr-cores-api
- collection_type: open
  name: Apache Solr REST Collections Schema API
  slug: open-solr-schema-api
- collection_type: open
  name: Apache Solr REST Collections Shards API
  slug: open-solr-shards-api
- collection_type: open
  name: Apache Solr REST Collections Update API
  slug: open-solr-update-api
- collection_type: open
  name: Apache Solr REST API
  slug: open-solr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/solr-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/solr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solr-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://solr.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://solr.apache.org/guide/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/apache/solr
- group: other
  title: ''
  type: Downloads
  url: https://solr.apache.org/downloads.html
- group: operate
  title: ''
  type: Community
  url: https://solr.apache.org/community.html
- group: company
  title: ''
  type: Blog
  url: https://solr.apache.org/feeds/solr/news.atom.xml
created: '2026-05-11'
description: Apache Solr is a popular, open source enterprise search platform built on Apache Lucene that provides full-text search, hit highlighting, faceted search, dynamic clustering, database integration, and rich document handling. Solr powers the search and navigation features of many of the world's largest internet sites and is highly scalable and reliable. Solr exposes a comprehensive HTTP/REST API (v1 and v2) for indexing, querying, and managing cores, collections, and configurations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solr.png
layout: provider
modified: '2026-05-11'
name: Apache Solr
nav: Providers
network: true
overview: 'Apache Solr publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Collections API, CollectionsAdminHandler API, Config API, and 4 more. Tagged areas include Search, Enterprise Search, Full-Text Search, Open-Source, and Lucene.


  Apache Solr''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 6 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 23.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 44.9
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solr/refs/heads/main/screenshots/solr-2026-06-20T194151.png
security:
- kind: authentication
  name: Solr Authentication
  slug: solr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Solr Domain Security
  slug: solr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Solr Vulnerability Disclosure
  slug: solr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: solr
tags:
- Search
- Enterprise Search
- Full-Text Search
- Open-Source
- Lucene
- Indexing
website: https://solr.apache.org/
---
