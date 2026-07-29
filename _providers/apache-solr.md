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
- acting_count: 10
  human_in_the_loop: 0
  name: Apache Solr Agentic Access
  operation_count: 21
  slug: apache-solr-agentic-access
  summary_line: 21 operations · 10 acting
api_count: 10
apis:
- description: The Solr Search API provides HTTP endpoints for full-text document search, including query parsers (Standard, DisMax, Extended DisMax), JSON Query DSL, faceting and JSON Facet API, spell checking, sug
  name: Apache Solr Search API
  slug: apache-solr-search-api
- description: The Solr Indexing API provides HTTP endpoints for adding, updating, and deleting documents from the search index. It supports JSON, XML, CSV, and binary Solr formats via the /update handler, atomic up
  name: Apache Solr Indexing API
  slug: apache-solr-indexing-api
- description: The Solr Schema API provides REST endpoints for managing the schema of a Solr collection, including field types, fields, dynamic fields, and copy fields. The Managed Schema approach allows runtime sch
  name: Apache Solr Schema API
  slug: apache-solr-schema-api
- description: The Solr Collections API provides REST endpoints for managing SolrCloud collections, shards, replicas, and aliases. It supports collection creation, deletion, modification, shard splitting, replica ma
  name: Apache Solr Collections API
  slug: apache-solr-collections-api
- description: The Solr Config API and Request Parameters API provide REST endpoints for managing Solr's solrconfig.xml settings at runtime without server restart, including request handler configuration, search com
  name: Apache Solr Config API
  slug: apache-solr-config-api
- description: Cluster status and properties
  name: Apache Solr Cluster API
  slug: apache-solr-cluster-api
- description: Manage SolrCloud collections, replicas, and nodes
  name: Apache Solr Collections API
  slug: apache-solr-collections-api
- description: Search a collection
  name: Apache Solr Query API
  slug: apache-solr-query-api
- description: Read and modify the schema of a collection
  name: Apache Solr Schema API
  slug: apache-solr-schema-api
- description: Index, update, and delete documents
  name: Apache Solr Update API
  slug: apache-solr-update-api
artifact_total: 39
collections:
- collection_type: open
  name: Apache Solr HTTP API
  slug: open-apache-solr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-solr-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-solr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-solr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-solr-authentication.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/solr
- group: docs
  title: ''
  type: Documentation
  url: https://solr.apache.org/guide/solr/latest/
- group: start
  title: ''
  type: Portal
  url: https://solr.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://solr.apache.org/guide/solr/latest/getting-started/introduction.html
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/solr/releases
- group: operate
  title: ''
  type: Support
  url: https://solr.apache.org/community.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: build
  title: SolrJ Java Client
  type: SDKs
  url: https://solr.apache.org/guide/solr/latest/deployment-guide/solrj.html
- group: build
  title: Solr Kubernetes Operator
  type: SDKs
  url: https://github.com/apache/solr-operator
- group: company
  title: ''
  type: Blog
  url: https://solr.apache.org/news.html
created: '2026-03-16'
description: Apache Solr is an open-source enterprise search platform built on Apache Lucene. It provides distributed indexing, replication, load-balanced querying, automated failover and recovery, and centralized configuration through SolrCloud. Solr exposes comprehensive REST/HTTP APIs for document indexing, full-text search with faceting and highlighting, schema management, collections management, and cluster operations. It is an Apache Software Foundation project used by major organizations for enterprise-scale search solutions.
features:
- description: Comprehensive full-text search with tokenization, stemming, synonyms, and relevance scoring.
  name: Full-Text Search
- description: Distributed search and indexing with automatic sharding, replication, and ZooKeeper coordination.
  name: SolrCloud
- description: Dynamic faceting including field facets, range facets, pivot facets, and JSON Facet API.
  name: Faceted Search
- description: SQL-like streaming expressions for distributed corpus analytics and aggregations.
  name: Streaming Expressions
- description: Approximate nearest neighbor (ANN) search for AI/ML vector embeddings using HNSW algorithm.
  name: Dense Vector Search
- description: Machine learning-based relevancy tuning with custom feature extraction and model training.
  name: Learning to Rank
- description: Near-real-time document retrieval before documents are committed to the index.
  name: Real-Time Get
- description: Geographic and spatial search with distance filtering and bounding box queries.
  name: Spatial Search
- description: SQL query language with JDBC support for analytics tools like Zeppelin and R.
  name: SQL Interface
finops:
- name: Apache Solr Finops
  service_category: API
  slug: apache-solr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-solr.png
integrations:
- description: Distributed coordination service for SolrCloud cluster management and configuration.
  name: Apache ZooKeeper
- description: Stream ingestion via Kafka connector for real-time document indexing.
  name: Apache Kafka
- description: Solr Kubernetes Operator for cloud-native deployment and management.
  name: Kubernetes
- description: Metrics integration via Prometheus exporter for Solr cluster monitoring.
  name: Grafana
- description: Document parsing for indexing rich content like PDFs, Word documents, and HTML.
  name: Apache Tika
- description: Data flow integration for automated document ingestion pipelines.
  name: Apache NiFi
- description: Natural language processing integration for text analysis and named entity recognition.
  name: OpenNLP
layout: provider
modified: '2026-04-19'
name: Apache Solr
nav: Providers
network: true
overview: 'Apache Solr publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Schema API, Collections API, Cluster API, and 4 more. Tagged areas include Enterprise Search, Full-Text Search, Lucene, Search, and SolrCloud.


  Apache Solr''s developer surface includes authentication, documentation, developer portal, getting-started guide, release notes, support, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Solr Plans Pricing
  plan_count: 3
  slug: apache-solr-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Apache Solr Rate Limits
  slug: apache-solr-rate-limits
score:
  band: developing
  composite: 44.7
  delta: -2.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 46.6
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-solr/refs/heads/main/screenshots/apache-solr-2026-06-20T172145.png
security:
- kind: authentication
  name: Apache Solr Authentication
  slug: apache-solr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Solr Domain Security
  slug: apache-solr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Solr Vulnerability Disclosure
  slug: apache-solr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-solr
tags:
- Enterprise Search
- Full-Text Search
- Lucene
- Search
- SolrCloud
- Open Source
- Java
use_cases:
- description: Unified enterprise search across documents, databases, web content, and file systems.
  name: Enterprise Search
- description: Product catalog search with faceting, filtering, and recommendation engines.
  name: E-Commerce Product Search
- description: Log ingestion and search for operational intelligence and security analysis.
  name: Log Analytics
- description: Semantic and similarity search using dense vector embeddings from AI models.
  name: AI/ML Vector Search
- description: Full-text search backend for CMS platforms and digital asset management systems.
  name: Content Management Search
website: https://solr.apache.org/
---
