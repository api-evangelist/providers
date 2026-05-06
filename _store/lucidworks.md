---
aid: lucidworks
name: Lucidworks
url: https://raw.githubusercontent.com/api-evangelist/lucidworks/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
position: Consumer
access: 3rd-Party
tags:
  - Search
  - Artificial Intelligence
  - Enterprise Search
  - Vector Search
  - RAG
  - Commerce
created: '2025-01-07'
modified: '2026-04-28'
specificationVersion: '0.19'
description: Lucidworks builds AI-powered search, discovery, and agent platforms used by enterprise commerce, support, and workplace teams. The Lucidworks AI Platform, Fusion, Neural Hybrid Search, Agent Studio, Commerce Studio, and Analytics Studio expose REST APIs for prediction, embedding, classification, signals capture, query rewriting, custom rule management, content chunking, and model deployment.
apis:
  - aid: lucidworks:ai-platform
    name: Lucidworks AI Platform API
    description: The Lucidworks AI Platform API exposes prediction endpoints for FAQ enrichment, keyword extraction, named entity recognition, retrieval augmented generation (RAG), summarization, passthrough LLM calls, and query rewriting. Developers can invoke pre-built use cases or chain custom predictions, then fetch results asynchronously by prediction ID.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference
    baseURL: https://api.lucidworks.ai
    tags:
      - Artificial Intelligence
      - Predictions
      - RAG
      - Summarization
      - NER
      - LLM
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference
      - type: Authentication
        url: https://doc.lucidworks.com/api-reference/request-access-token/request-access-token
      - type: OpenAPI
        url: openapi/lucidworks-ai-platform-openapi.yml
  - aid: lucidworks:embeddings
    name: Lucidworks Embeddings and Classification API
    description: The Embeddings and Classification API generates 768-dimensional vector encodings using the English Language Model text encoder, returns ranked classification labels, exposes custom model predictions, and tokenizes inputs by model ID for use in vector search and downstream ML pipelines.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference
    baseURL: https://api.lucidworks.ai
    tags:
      - Embeddings
      - Vector Search
      - Classification
      - Tokenization
      - Machine Learning
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/get-predictions/english-language-model-text-encoder
      - type: OpenAPI
        url: openapi/lucidworks-embeddings-openapi.yml
  - aid: lucidworks:signals
    name: Lucidworks Signals API
    description: The Signals API captures and retrieves user behavior signals for click, query, cart-add, and purchase-complete events. Signals power relevance tuning, recommendations, and analytics across Commerce Studio and the Analytics Studio.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference
    baseURL: https://api.lucidworks.ai
    tags:
      - Signals
      - Analytics
      - Click Tracking
      - Commerce
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/get-signals/click-signals
      - type: OpenAPI
        url: openapi/lucidworks-signals-openapi.yml
  - aid: lucidworks:rules
    name: Lucidworks Rules and Query Rewrites API
    description: The Rules and Query Rewrites API allows commerce and search teams to create, read, update, and delete custom business rules and query rewrites. Rules drive boost, bury, pin, redirect, and synonym behaviors that personalize search results without code changes.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference/rule-management/list-rules
    baseURL: https://api.lucidworks.ai
    tags:
      - Business Rules
      - Query Rewrites
      - Search Tuning
      - Commerce
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/rule-management/list-rules
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/query-rewrite-management/list-query-rewrites
      - type: OpenAPI
        url: openapi/lucidworks-rules-openapi.yml
  - aid: lucidworks:chunking
    name: Lucidworks Content Chunking API
    description: The Content Chunking API splits long-form content into retrieval-ready passages using dynamic-sentence chunkers, semantic chunkers, and regex splitters. Chunked output feeds vector indexing and RAG pipelines.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference/split-content-into-chunks/chunk-text-using-the-specified-chunker
    baseURL: https://api.lucidworks.ai
    tags:
      - Chunking
      - Content Processing
      - RAG
      - Indexing
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/split-content-into-chunks/chunk-text-using-the-specified-chunker
      - type: OpenAPI
        url: openapi/lucidworks-chunking-openapi.yml
  - aid: lucidworks:models
    name: Lucidworks Model Management API
    description: The Model Management API lets teams create, get, list, deploy, and delete models used by Lucidworks AI. Custom models can be registered and deployed alongside the default catalog for inference at query and indexing time.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/api-reference/manage-models/list-all-models
    baseURL: https://api.lucidworks.ai
    tags:
      - Model Management
      - MLOps
      - Deployment
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/api-reference/manage-models/list-all-models
      - type: OpenAPI
        url: openapi/lucidworks-models-openapi.yml
  - aid: lucidworks:fusion
    name: Lucidworks Fusion REST API
    description: Fusion REST APIs administer collections, indexing pipelines, query pipelines, connectors, and search apps inside the Lucidworks Fusion platform. The legacy Custom Rules API for Fusion 5.7 is part of this family of administrative endpoints.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://doc.lucidworks.com/docs/5/fusion/dev-portal/rest-apis
    tags:
      - Fusion
      - Enterprise Search
      - Indexing
      - Pipelines
      - Connectors
    properties:
      - type: Documentation
        url: https://doc.lucidworks.com/docs/5/fusion/dev-portal/rest-apis
      - type: Documentation
        url: https://legacydoc.lucidworks.com/fusion/5.7/331/custom-rules-api
common:
  - type: Website
    url: https://lucidworks.com
  - type: Documentation
    url: https://doc.lucidworks.com
  - type: APIReference
    url: https://doc.lucidworks.com/api-reference
  - type: Authentication
    url: https://doc.lucidworks.com/api-reference/request-access-token/request-access-token
  - type: SDK
    url: https://doc.lucidworks.com/docs/5/fusion/dev-portal/connectors-sdk/overview
  - type: Blog
    url: https://lucidworks.com/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
