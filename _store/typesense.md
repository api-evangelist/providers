---
name: Typesense
description: Typesense is a fast, typo-tolerant, open-source search engine designed for developer productivity. It provides instant search experiences with support for full-text search, faceting, filtering, sorting, geo-based search, vector search, and conversational AI search. Typesense is available as an open-source self-hosted solution or as a managed cloud service via Typesense Cloud.
image: https://typesense.org/favicon-32x32.png
url: https://typesense.org
created: '2026-05-03'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Full-Text Search
  - Open Source
  - Search Engine
  - Typo Tolerance
  - Vector Search
apis:
  - name: Typesense Search API
    description: The core Typesense REST API for managing collections, indexing documents, and performing full-text, faceted, filtered, sorted, geo-based, and multi-search queries. Supports synonym sets, curation sets, collection aliases, stopwords, presets, stemming dictionaries, API keys, and cluster operations.
    image: https://typesense.org/favicon-32x32.png
    humanURL: https://typesense.org/docs/
    baseURL: http://localhost:8108
    tags:
      - Collections
      - Documents
      - Full-Text Search
      - Search
    properties:
      - type: Documentation
        url: https://typesense.org/docs/
      - type: OpenAPI
        url: openapi/typesense-search-api-openapi.yml
      - type: Getting Started
        url: https://typesense.org/docs/guide/
      - type: API Reference
        url: https://typesense.org/docs/latest/api/
  - name: Typesense Vector Search API
    description: The Typesense Vector Search API extends the core search capabilities with vector and hybrid search. It supports indexing embedding fields, querying by vector proximity, and combining semantic vector search with keyword search for superior relevance.
    image: https://typesense.org/favicon-32x32.png
    humanURL: https://typesense.org/docs/guide/vector-search.html
    baseURL: http://localhost:8108
    tags:
      - Embeddings
      - Hybrid Search
      - Semantic Search
      - Vector Search
    properties:
      - type: Documentation
        url: https://typesense.org/docs/guide/vector-search.html
      - type: OpenAPI
        url: openapi/typesense-vector-search-api-openapi.yml
  - name: Typesense Conversational Search API
    description: The Typesense Conversational Search API enables AI-powered question answering over your search index. It supports conversation models (OpenAI, Cloudflare Workers AI), NL search models, and stateful multi-turn conversations over indexed data.
    image: https://typesense.org/favicon-32x32.png
    humanURL: https://typesense.org/docs/guide/conversational-search-rag.html
    baseURL: http://localhost:8108
    tags:
      - AI
      - Conversational Search
      - LLM
      - RAG
    properties:
      - type: Documentation
        url: https://typesense.org/docs/guide/conversational-search-rag.html
      - type: OpenAPI
        url: openapi/typesense-conversational-search-api-openapi.yml
  - name: Typesense Analytics API
    description: The Typesense Analytics API tracks search events and provides insights into search behavior, popular queries, no-result queries, and click analytics. Supports rule-based aggregation and analytics data exports.
    image: https://typesense.org/favicon-32x32.png
    humanURL: https://typesense.org/docs/guide/analytics-query-suggestions.html
    baseURL: http://localhost:8108
    tags:
      - Analytics
      - Events
      - Query Insights
      - Search Analytics
    properties:
      - type: Documentation
        url: https://typesense.org/docs/guide/analytics-query-suggestions.html
      - type: OpenAPI
        url: openapi/typesense-analytics-api-openapi.yml
  - name: Typesense Cloud Management API
    description: The Typesense Cloud Management API enables provisioning and managing Typesense Cloud clusters programmatically. Supports creating, updating, terminating clusters, scheduling configuration changes, managing server configuration parameters, and generating API keys.
    image: https://typesense.org/favicon-32x32.png
    humanURL: https://typesense.org/docs/cloud-management-api/v1/cluster-management.html
    baseURL: https://cloud.typesense.org/api/v1
    tags:
      - Cluster Management
      - Cloud
      - Infrastructure
      - Provisioning
    properties:
      - type: Documentation
        url: https://typesense.org/docs/cloud-management-api/v1/cluster-management.html
      - type: OpenAPI
        url: openapi/typesense-cloud-management-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://typesense.org
  - type: Documentation
    url: https://typesense.org/docs/
  - type: GitHub Organization
    url: https://github.com/typesense
  - type: Blog
    url: https://typesense.org/blog/
  - type: Slack Community
    url: https://join.slack.com/t/typesense-community/shared_invite/zt-2fetvh0pw-ft5y2YQlq4FS3fVDFTfWJA
  - type: Docker Hub
    url: https://hub.docker.com/r/typesense/typesense
  - type: npm
    url: https://www.npmjs.com/package/typesense
  - type: Pricing
    url: https://typesense.org/pricing/
  - type: Terms of Service
    url: https://typesense.org/terms/
  - type: Privacy Policy
    url: https://typesense.org/privacy/
  - type: JSON-LD
    url: json-ld/typesense-context.jsonld
  - type: JSONSchema
    url: json-schema/typesense-collection-schema.json
  - type: JSONSchema
    url: json-schema/typesense-search-result-schema.json
  - type: JSONSchema
    url: json-schema/typesense-analytics-event-schema.json
  - type: JSONStructure
    url: json-structure/typesense-collection-structure.json
  - type: JSONStructure
    url: json-structure/typesense-search-result-structure.json
  - type: Vocabulary
    url: vocabulary/typesense-vocabulary.yml
  - type: SpectralRules
    url: rules/typesense-rules.yml
  - type: NaftikoCapability
    url: capabilities/search-and-discovery.yaml
  - type: Features
    data:
      - 'Open Source: GPL v3 self-hosted, free at any scale'
      - Cloud Small from ~$0.045/hr (0.5 GB RAM, single node)
      - Cloud Medium from ~$0.18/hr (2 GB RAM, single node)
      - 'Cloud HA Multi-node: ~3x base for 3-node cluster'
      - 'Enterprise custom: dedicated support, self-hosted Enterprise license'
      - Typo-tolerant full-text search
      - Geosearch and faceted search
      - Vector search and hybrid search
      - Federated multi-collection search
      - REST API with scoped API keys
      - Configurable per-key rate limits
      - InstantSearch.js compatibility
      - Auto-suggestions and autocomplete
      - Synonyms, stop words, stemming
      - Curation rules for promoted results
      - Open-source SDKs for many languages
    sources:
      - https://typesense.org/cloud/
      - https://cloud.typesense.org/pricing
    updated: '2026-05-04'
---
