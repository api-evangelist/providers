---
aid: apache-lucene
name: Apache Lucene
description: Apache Lucene is a high-performance, full-featured text search engine library written entirely in Java. It provides indexing and search technology, as well as spellchecking, hit highlighting, faceting, vector similarity search, and advanced analysis and tokenization capabilities. Lucene is the foundation for many popular search applications including Apache Solr.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Full-Text Search
  - Indexing
  - Java
  - Search
  - Text Analysis
  - Vector Search
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-lucene/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-lucene:apache-lucene
    name: Apache Lucene
    description: Lucene provides a comprehensive Java API for full-text indexing, searching, faceting, hit highlighting, spatial search, vector nearest-neighbor search, and text analysis with support for custom analyzers, query parsers, and pluggable ranking models including BM25 and Vector Space Model.
    humanURL: https://lucene.apache.org/core/
    tags:
      - Indexing
      - Java
      - Search
      - Vector Search
      - Text Analysis
    properties:
      - type: Documentation
        url: https://lucene.apache.org/core/
      - type: Documentation
        url: https://lucene.apache.org/core/10_4_0/index.html
      - type: GettingStarted
        url: https://lucene.apache.org/core/quickstart.html
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.lucene/lucene-core
        title: Maven Central (Java)
      - type: GitHubRepository
        url: https://github.com/apache/lucene
common:
  - type: Portal
    url: https://lucene.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/lucene
  - type: GitHubRepository
    url: https://github.com/apache/lucenenet
  - type: IssueTracker
    url: https://github.com/apache/lucene/issues
  - type: Blog
    url: https://lucene.apache.org/news.html
  - type: MailingList
    url: https://lists.apache.org/list.html?dev@lucene.apache.org
  - type: Slack
    url: https://the-asf.slack.com/messages/CE70MDPMF
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Full-Text Indexing
        description: High-performance full-text indexing with over 800GB/hour throughput on modern hardware with minimal RAM requirements.
      - name: Vector Nearest-Neighbor Search
        description: Native support for approximate and exact k-nearest-neighbor vector similarity search alongside traditional keyword search.
      - name: Advanced Query Types
        description: Supports phrase queries, wildcard, proximity, range, fuzzy, and fielded queries with pluggable query parsers.
      - name: Faceting and Grouping
        description: Built-in faceted search and result grouping capabilities for navigation and aggregation.
      - name: Hit Highlighting
        description: Highlights search keywords in result snippets using the Highlighter and UnifiedHighlighter modules.
      - name: Spell Checking and Suggestions
        description: Auto-suggest and spell-checking support via the Suggest module with multiple suggester implementations.
      - name: Pluggable Analyzers
        description: Extensive analyzer ecosystem supporting dozens of languages including ICU, Kuromoji (Japanese), Nori (Korean), OpenNLP, and more.
      - name: Pluggable Ranking Models
        description: Supports Vector Space Model, Okapi BM25, and custom pluggable similarity implementations.
      - name: Spatial Search
        description: Geospatial search capabilities via the Spatial and Spatial3D modules.
      - name: Replication Support
        description: Index replication support via the Replicator module for leader-follower architectures.
  - type: UseCases
    data:
      - name: Enterprise Search
        description: Power full-text search across enterprise documents, emails, databases, and file systems.
      - name: E-Commerce Product Search
        description: Implement fast, relevant product search with facets, autocomplete, and spell correction.
      - name: Log and Event Search
        description: Index and search structured and unstructured log data for observability and security analytics.
      - name: Semantic Search
        description: Combine keyword search with vector embeddings for hybrid semantic and lexical retrieval.
      - name: Knowledge Base Search
        description: Build searchable knowledge bases and documentation portals with rich query capabilities.
  - type: Integrations
    data:
      - name: Apache Solr
        description: Apache Solr is built on top of Lucene and adds distributed search, REST API, and enterprise features.
      - name: Elasticsearch/OpenSearch
        description: Elasticsearch and OpenSearch use Lucene as their underlying search engine.
      - name: Apache Hadoop
        description: Lucene integrates with Hadoop for large-scale distributed indexing pipelines.
      - name: Apache Tika
        description: Apache Tika extracts text from thousands of file formats for indexing into Lucene.
      - name: Apache OpenNLP
        description: OpenNLP provides NLP analysis capabilities integrated through Lucene analyzers.
      - name: Apache Nutch
        description: Apache Nutch is a web crawler that stores and indexes content via Lucene.
      - name: Lucene.NET
        description: Official .NET port of Apache Lucene, maintained in the apache/lucenenet repository.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
