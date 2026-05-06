---
aid: meilisearch
name: Meilisearch
description: Meilisearch is an open source, lightning-fast search engine API that brings AI-powered hybrid search to sites and applications. It provides a RESTful API for indexing, searching, and managing documents, with SDKs available for all major languages and frameworks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Search
  - Full-Text Search
  - Hybrid Search
  - Open Source
  - Search
url: https://raw.githubusercontent.com/api-evangelist/meilisearch/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: meilisearch:meilisearch-api
    name: Meilisearch API
    description: The Meilisearch RESTful API provides endpoints for creating and managing indexes, adding and searching documents, configuring search settings, managing API keys, and monitoring tasks and health status.
    humanURL: https://www.meilisearch.com/docs
    baseURL: https://localhost:7700
    tags:
      - Documents
      - Indexing
      - Search
    properties:
      - type: Documentation
        url: https://www.meilisearch.com/docs
      - type: Reference
        url: https://www.meilisearch.com/docs/reference/api/overview
      - type: Getting Started
        url: https://www.meilisearch.com/docs/learn/getting_started/installation
      - type: Authentication
        url: https://www.meilisearch.com/docs/learn/security/basic_security
      - type: SDKs
        url: https://www.meilisearch.com/docs/learn/what_is_meilisearch/sdks
common:
  - type: Portal
    url: https://www.meilisearch.com/
  - type: Documentation
    url: https://www.meilisearch.com/docs
  - type: GitHub Organization
    url: https://github.com/meilisearch
  - type: Community
    url: https://discord.gg/meilisearch
  - type: Sign Up
    url: https://cloud.meilisearch.com/register
  - type: Login
    url: https://cloud.meilisearch.com/
  - type: Pricing
    url: https://www.meilisearch.com/pricing
  - type: Blog
    url: https://www.meilisearch.com/blog
  - type: Change Log
    url: https://github.com/meilisearch/meilisearch/releases
  - type: Features
    data:
      - 'Open Source: free self-hosted'
      - 'Cloud Usage-Based from $30/mo: pay per search + documents'
      - 'Cloud Resource-Based from $23/mo: pay by CPU/RAM/storage'
      - 'Enterprise: custom self-hosting + premier support'
      - Typo-tolerant full-text search
      - Vector search for semantic + RAG use cases
      - Faceted search and filtering
      - Multi-tenancy via tenant tokens
      - Federated search across multiple indexes
      - REST API with master and tenant keys
      - 'Concurrent indexing tasks: 4 default'
      - Embedders integration (OpenAI, HuggingFace, etc.)
      - Synonyms, stop words, ranking rules
      - InstantSearch UI libraries (JS, React, Vue)
      - Webhooks via task notifications
      - EU + US data residency
    sources:
      - https://www.meilisearch.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
