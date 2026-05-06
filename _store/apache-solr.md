---
aid: apache-solr
name: Apache Solr
description: Apache Solr is an open-source enterprise search platform built on Apache Lucene. It provides distributed indexing, replication, load-balanced querying, automated failover and recovery, and centralized configuration through SolrCloud. Solr exposes comprehensive REST/HTTP APIs for document indexing, full-text search with faceting and highlighting, schema management, collections management, and cluster operations. It is an Apache Software Foundation project used by major organizations for enterprise-scale search solutions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Search
  - Full-Text Search
  - Lucene
  - Search
  - SolrCloud
  - Open Source
  - Java
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-solr/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-solr:apache-solr-search-api
    name: Apache Solr Search API
    description: The Solr Search API provides HTTP endpoints for full-text document search, including query parsers (Standard, DisMax, Extended DisMax), JSON Query DSL, faceting and JSON Facet API, spell checking, suggestions, MoreLikeThis, spatial search, dense vector search, result grouping, highlighting, and result clustering. Queries are submitted to the /select handler and support complex relevancy scoring with Learning to Rank.
    humanURL: https://solr.apache.org/guide/solr/latest/query-guide/query-syntax-and-parsers.html
    tags:
      - Search
      - Faceting
      - Full-Text Search
      - REST
      - Indexing
    properties:
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/query-guide/query-syntax-and-parsers.html
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/query-guide/json-request-api.html
  - aid: apache-solr:apache-solr-indexing-api
    name: Apache Solr Indexing API
    description: The Solr Indexing API provides HTTP endpoints for adding, updating, and deleting documents from the search index. It supports JSON, XML, CSV, and binary Solr formats via the /update handler, atomic updates, optimistic concurrency, document routing in SolrCloud, and the DataImportHandler for bulk loading from databases and file systems.
    humanURL: https://solr.apache.org/guide/solr/latest/indexing-guide/indexing-with-update-handlers.html
    tags:
      - Indexing
      - Documents
      - REST
      - Updates
    properties:
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/indexing-guide/indexing-with-update-handlers.html
  - aid: apache-solr:apache-solr-schema-api
    name: Apache Solr Schema API
    description: The Solr Schema API provides REST endpoints for managing the schema of a Solr collection, including field types, fields, dynamic fields, and copy fields. The Managed Schema approach allows runtime schema modifications without server restart via the /schema endpoint.
    humanURL: https://solr.apache.org/guide/solr/latest/indexing-guide/schema-api.html
    tags:
      - Schema
      - REST
      - Management
    properties:
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/indexing-guide/schema-api.html
  - aid: apache-solr:apache-solr-collections-api
    name: Apache Solr Collections API
    description: The Solr Collections API provides REST endpoints for managing SolrCloud collections, shards, replicas, and aliases. It supports collection creation, deletion, modification, shard splitting, replica management, collection backup/restore, alias management, and cross-datacenter replication (CDCR) configuration.
    humanURL: https://solr.apache.org/guide/solr/latest/deployment-guide/cluster-node-management.html
    tags:
      - Collections
      - SolrCloud
      - Cluster
      - Management
    properties:
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/deployment-guide/cluster-node-management.html
  - aid: apache-solr:apache-solr-config-api
    name: Apache Solr Config API
    description: The Solr Config API and Request Parameters API provide REST endpoints for managing Solr's solrconfig.xml settings at runtime without server restart, including request handler configuration, search component configuration, query settings, and configset management. The v2 API provides a modern JSON-based interface for all configuration operations.
    humanURL: https://solr.apache.org/guide/solr/latest/configuration-guide/config-api.html
    tags:
      - Configuration
      - REST
      - Management
    properties:
      - type: Documentation
        url: https://solr.apache.org/guide/solr/latest/configuration-guide/config-api.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/solr
  - type: Documentation
    url: https://solr.apache.org/guide/solr/latest/
  - type: Portal
    url: https://solr.apache.org/
  - type: GettingStarted
    url: https://solr.apache.org/guide/solr/latest/getting-started/introduction.html
  - type: ReleaseNotes
    url: https://github.com/apache/solr/releases
  - type: Support
    url: https://solr.apache.org/community.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://solr.apache.org/guide/solr/latest/deployment-guide/solrj.html
    title: SolrJ Java Client
  - type: SDK
    url: https://github.com/apache/solr-operator
    title: Solr Kubernetes Operator
  - type: Features
    data:
      - name: Full-Text Search
        description: Comprehensive full-text search with tokenization, stemming, synonyms, and relevance scoring.
      - name: SolrCloud
        description: Distributed search and indexing with automatic sharding, replication, and ZooKeeper coordination.
      - name: Faceted Search
        description: Dynamic faceting including field facets, range facets, pivot facets, and JSON Facet API.
      - name: Streaming Expressions
        description: SQL-like streaming expressions for distributed corpus analytics and aggregations.
      - name: Dense Vector Search
        description: Approximate nearest neighbor (ANN) search for AI/ML vector embeddings using HNSW algorithm.
      - name: Learning to Rank
        description: Machine learning-based relevancy tuning with custom feature extraction and model training.
      - name: Real-Time Get
        description: Near-real-time document retrieval before documents are committed to the index.
      - name: Spatial Search
        description: Geographic and spatial search with distance filtering and bounding box queries.
      - name: SQL Interface
        description: SQL query language with JDBC support for analytics tools like Zeppelin and R.
  - type: UseCases
    data:
      - name: Enterprise Search
        description: Unified enterprise search across documents, databases, web content, and file systems.
      - name: E-Commerce Product Search
        description: Product catalog search with faceting, filtering, and recommendation engines.
      - name: Log Analytics
        description: Log ingestion and search for operational intelligence and security analysis.
      - name: AI/ML Vector Search
        description: Semantic and similarity search using dense vector embeddings from AI models.
      - name: Content Management Search
        description: Full-text search backend for CMS platforms and digital asset management systems.
  - type: Integrations
    data:
      - name: Apache ZooKeeper
        description: Distributed coordination service for SolrCloud cluster management and configuration.
      - name: Apache Kafka
        description: Stream ingestion via Kafka connector for real-time document indexing.
      - name: Kubernetes
        description: Solr Kubernetes Operator for cloud-native deployment and management.
      - name: Grafana
        description: Metrics integration via Prometheus exporter for Solr cluster monitoring.
      - name: Apache Tika
        description: Document parsing for indexing rich content like PDFs, Word documents, and HTML.
      - name: Apache NiFi
        description: Data flow integration for automated document ingestion pipelines.
      - name: OpenNLP
        description: Natural language processing integration for text analysis and named entity recognition.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
