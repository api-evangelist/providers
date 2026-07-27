---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Solr Agentic Access
  operation_count: 14
  slug: solr-agentic-access
  summary_line: 14 operations · 10 acting
api_count: 8
apis:
- description: HTTP/REST API for Apache Solr providing endpoints for querying, indexing, schema management, collections administration, and core administration. The v2 API uses RESTful resource paths under /api whil
  name: Apache Solr REST API
  slug: rest-api
- description: Cluster-level collection management
  name: Apache Solr Collections API
  slug: solr-collections-api
- description: Legacy Collections admin handler endpoints
  name: Apache Solr CollectionsAdminHandler API
  slug: solr-collectionsadminhandler-api
- description: Per-collection configuration operations
  name: Apache Solr Config API
  slug: solr-config-api
- description: Node-level core administration
  name: Apache Solr Cores API
  slug: solr-cores-api
- description: Per-collection schema operations
  name: Apache Solr Schema API
  slug: solr-schema-api
- description: Shard management for collections
  name: Apache Solr Shards API
  slug: solr-shards-api
- description: Per-collection document update operations
  name: Apache Solr Update API
  slug: solr-update-api
artifact_total: 13
collections:
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
overview: 'Apache Solr publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Collections API, CollectionsAdminHandler API, Config API, and 4 more. Tagged areas include Search, Enterprise Search, Full-Text Search, Open Source, and Lucene.


  Apache Solr''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 6 more developer resources.'
random_paper: 40
score:
  band: emerging
  composite: 26.8
  delta: 2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 48.7
    developer_ergonomics: 26.1
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Open Source
- Lucene
- Indexing
website: https://solr.apache.org/
---
