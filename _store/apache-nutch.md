---
aid: apache-nutch
name: Apache Nutch
description: Apache Nutch is a highly extensible and scalable open-source web crawler software project built on Apache Hadoop data structures for batch processing. It provides a pluggable architecture supporting custom parse filters, scoring filters, index writers, and protocol implementations. Nutch integrates with Apache Solr and Elasticsearch for full-text search and exposes a REST API for managing crawl jobs, configurations, seed lists, and database queries. Governed by the Apache Software Foundation under the Apache License 2.0.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Web Crawler
  - Indexing
  - Search
  - Apache
  - Java
  - Hadoop
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-nutch:apache-nutch-rest-api
    name: Apache Nutch REST API
    description: REST API for managing Apache Nutch crawl jobs, configurations, seed URL lists, database queries (CrawlDB and FetchDB), and data readers. Supports full crawl lifecycle management including inject, generate, fetch, parse, updatedb, and index operations. Secured via HTTP Basic Authentication.
    humanURL: https://cwiki.apache.org/confluence/display/NUTCH/Nutch+1.X+REST+API
    baseURL: http://localhost:8081
    tags:
      - REST
      - Crawl Management
      - Job Management
      - Configuration
    properties:
      - type: Documentation
        url: https://cwiki.apache.org/confluence/display/NUTCH/Nutch+1.X+REST+API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/openapi/apache-nutch-openapi.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-nutch-config-schema.json
        title: Nutch Config Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-job-config-schema.json
        title: Job Config Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-job-info-schema.json
        title: Job Info Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-nutch-server-info-schema.json
        title: Server Info Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-seed-list-schema.json
        title: Seed List Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-schema/apache-nutch-db-query-schema.json
        title: DB Query Schema
common:
  - type: GitHubRepository
    url: https://github.com/apache/nutch
    title: Apache Nutch GitHub Repository
  - type: GitHubOrganization
    url: https://github.com/apache
    title: Apache Software Foundation GitHub
  - type: Documentation
    url: https://nutch.apache.org/documentation/
    title: Apache Nutch Documentation
  - type: GettingStarted
    url: https://cwiki.apache.org/confluence/display/NUTCH/NutchTutorial
    title: Nutch Tutorial
  - type: Tutorials
    url: https://nutch.apache.org/documentation/tutorials/
    title: Apache Nutch Tutorials
  - type: FAQ
    url: https://nutch.apache.org/documentation/faqs/
    title: Apache Nutch FAQs
  - type: ReleaseNotes
    url: https://github.com/apache/nutch/blob/master/CHANGES.md
    title: Nutch Release Notes
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
    title: Apache License 2.0
  - type: Support
    url: https://nutch.apache.org/community/mailing-lists/
    title: Mailing Lists
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/nutch
    title: Nutch on Stack Overflow
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/rules/apache-nutch-spectral-rules.yml
    title: Apache Nutch Spectral Rules
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/capabilities/apache-nutch-crawl-management.yaml
    title: Apache Nutch Crawl Management
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/vocabulary/apache-nutch-vocabulary.yaml
    title: Apache Nutch Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/apache-nutch/refs/heads/main/json-ld/apache-nutch-context.jsonld
    title: Apache Nutch JSON-LD Context
  - type: Features
    data:
      - name: Scalable Batch Crawling
        description: Leverages Apache Hadoop data structures for distributed, large-scale web crawling batch processing.
      - name: Pluggable Architecture
        description: Extensible plugin system supporting custom parse filters, scoring filters, index writers, protocol plugins, and URL filters.
      - name: REST API for Crawl Management
        description: Full REST API for managing crawl jobs, configurations, seed lists, CrawlDB/FetchDB queries, and sequence file readers.
      - name: Full-Text Search Integration
        description: Built-in index writers for Apache Solr and Elasticsearch to enable full-text search over crawled content.
      - name: Apache Tika Parsing
        description: Uses Apache Tika for parsing a wide variety of document formats during the crawl pipeline.
      - name: Duplicate Detection
        description: Built-in deduplication support to identify and remove duplicate content from the crawl database and search index.
      - name: Configurable URL Filtering
        description: Regex-based and custom URL filter plugins to control crawl scope and exclusions.
      - name: Incremental Crawling
        description: Supports multi-round incremental crawling workflows to keep the crawl database fresh.
      - name: CommonCrawl Export
        description: Service operations for exporting crawl data in CommonCrawl-compatible formats.
      - name: HTTP Authentication Support
        description: Configurable HTTP authentication schemes for crawling password-protected sites.
  - type: UseCases
    data:
      - name: Enterprise Search
        description: Build enterprise search engines over internal or external web content using Nutch as the crawler and Solr/Elasticsearch as the search backend.
      - name: Research Data Collection
        description: Academic and research teams use Nutch for large-scale systematic web data collection and indexing.
      - name: Intranet Document Search
        description: Crawl and index intranet sites, wikis, and document repositories for internal enterprise search.
      - name: Web Archive Creation
        description: Create structured web archives compatible with CommonCrawl format for long-term data preservation.
      - name: SEO and Content Monitoring
        description: Monitor web content changes, track competitor sites, and analyze web structure at scale.
      - name: Custom Data Extraction Pipelines
        description: Build custom extraction pipelines using Nutch plugin architecture for targeted data acquisition tasks.
  - type: Integrations
    data:
      - name: Apache Solr
        description: Native index writer plugin for indexing crawled content into Apache Solr for full-text search.
      - name: Elasticsearch
        description: Index writer plugin for sending crawled content to Elasticsearch clusters.
      - name: Apache Hadoop
        description: Core dependency providing distributed storage and processing via HDFS and MapReduce.
      - name: Apache Tika
        description: Used for content detection and extraction from a wide range of document formats during parsing.
      - name: SolrCloud
        description: Support for SolrCloud distributed search clusters for scalable indexing.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
