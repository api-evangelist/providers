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
