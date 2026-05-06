---
aid: chroma
name: Chroma
x-type: company
description: Chroma (Chroma DB) is an open-source AI-native embedding database designed to make it easy to build LLM applications by providing storage, retrieval, and management for vector embeddings, full-text search, regex search, and multi-modal retrieval (text, image, audio). Distributed under the Apache 2.0 license, Chroma can be self-hosted (single-node Python or distributed Rust-based deployment) or consumed via Chroma Cloud, a managed serverless vector database service offering usage-based pricing. Chroma is the open-source data infrastructure for AI agents and RAG (Retrieval-Augmented Generation) applications, with first-party SDKs for Python and JavaScript/TypeScript and integrations with leading embedding providers (OpenAI, Cohere, Hugging Face, sentence-transformers).
url: https://raw.githubusercontent.com/api-evangelist/chroma/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - AI Native
  - Apache 2.0
  - Cloud
  - Embeddings
  - Hybrid Search
  - JavaScript
  - LLM
  - Machine Learning
  - Multi-Modal
  - Open Source
  - Python
  - RAG
  - Retrieval
  - SDK
  - Search
  - Serverless
  - TypeScript
  - Vector Database
created: '2025-03-07'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chroma:server-api
    name: Chroma Server API
    description: The Chroma Server API is a REST API that provides access to the Chroma open-source vector database. It enables developers to create and manage collections of embeddings, add documents with automatic tokenization and embedding, and perform vector similarity searches. The API supports metadata filtering, full-text search, and collection management operations. An OpenAPI specification is available at the server endpoint for client generation in various programming languages.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trychroma.com
    humanURL: https://docs.trychroma.com/reference/chroma-reference
    tags:
      - AI
      - Embeddings
      - Machine Learning
      - Search
      - Vector Database
    properties:
      - type: Documentation
        url: https://docs.trychroma.com/reference/chroma-reference
      - type: OpenAPI
        url: openapi/chroma-server-api-openapi.yml
  - aid: chroma:cloud-api
    name: Chroma Cloud API
    description: Chroma Cloud is a managed, serverless vector database service that provides fast and scalable vector, full-text, and metadata search across terabytes of data. It is backed by Chroma's Apache 2.0 distributed database and offers usage-based pricing with starter and team plans. Developers can connect to Chroma Cloud using the Python or JavaScript client SDKs without needing to manage infrastructure.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.trychroma.com
    humanURL: https://docs.trychroma.com/cloud/pricing
    tags:
      - AI
      - Cloud
      - Embeddings
      - Serverless
      - Vector Database
    properties:
      - type: Documentation
        url: https://docs.trychroma.com/cloud/sync/overview
      - type: OpenAPI
        url: openapi/chroma-cloud-api-openapi.yml
  - aid: chroma:python-client
    name: Chroma Python Client
    description: The Chroma Python Client is a first-party SDK for interacting with both self-hosted Chroma servers and Chroma Cloud. It provides a simple, developer-friendly interface with a core API of just four functions for managing collections, adding documents, and querying embeddings. The client handles automatic tokenization, embedding, and indexing of documents, making it straightforward to build AI applications that require vector similarity search.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.trychroma.com/reference/python/client
    tags:
      - Embeddings
      - Python
      - SDK
      - Vector Database
    properties:
      - type: Documentation
        url: https://docs.trychroma.com/reference/python/client
      - type: SourceCode
        url: https://github.com/chroma-core/chroma
  - aid: chroma:javascript-client
    name: Chroma JavaScript Client
    description: The Chroma JavaScript and TypeScript Client is a first-party SDK for interacting with Chroma from JavaScript or TypeScript applications. The v3 rewrite focused on reducing bundle size and improving developer experience, making it well-suited for deployment on serverless platforms like Vercel. It supports both self-hosted Chroma instances and Chroma Cloud via the CloudClient class, providing collection management, document ingestion, and vector similarity search capabilities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.trychroma.com/reference/js/client
    tags:
      - Embeddings
      - JavaScript
      - SDK
      - TypeScript
      - Vector Database
    properties:
      - type: Documentation
        url: https://docs.trychroma.com/reference/js/client
      - type: SourceCode
        url: https://github.com/chroma-core/chroma-js
common:
  - type: Website
    url: https://www.trychroma.com/
  - type: Documentation
    url: https://docs.trychroma.com/docs/overview/introduction
  - type: Portal
    url: https://docs.trychroma.com/
  - type: Login
    url: https://cloud.trychroma.com/
  - type: Pricing
    url: https://docs.trychroma.com/cloud/pricing
  - type: Blog
    url: https://www.trychroma.com/blog
  - type: GitHubOrg
    url: https://github.com/chroma-core
  - type: SourceCode
    url: https://github.com/chroma-core/chroma
  - type: Discord
    url: https://discord.gg/MMeYNTmh3x
  - type: Twitter
    url: https://twitter.com/trychroma
  - type: License
    name: Apache License 2.0
    url: https://github.com/chroma-core/chroma/blob/main/LICENSE
  - type: TermsOfService
    url: https://www.trychroma.com/tos
  - type: PrivacyPolicy
    url: https://www.trychroma.com/privacy
  - type: JSONLDContext
    url: json-ld/chroma-context.jsonld
  - type: JSONSchema
    url: json-schema/chroma-collection-schema.json
  - type: JSONSchema
    url: json-schema/chroma-record-schema.json
  - type: Spectral
    url: spectral/chroma-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/chroma-capabilities.yml
  - name: Features
    type: Features
    data:
      - name: Document and Metadata Storage
      - name: Vector Similarity Search (Dense, Sparse, Hybrid)
      - name: Full-Text and Regex Search
      - name: Metadata Filtering
      - name: Multi-Modal Retrieval (Text, Image, Audio)
      - name: Automatic Tokenization and Embedding
      - name: Collection Management
      - name: Embedding Function Plugins
      - name: Self-Hosted and Cloud Deployments
      - name: Apache 2.0 Open Source License
  - name: EmbeddingProviders
    type: EmbeddingProviders
    data:
      - name: OpenAI
      - name: Cohere
      - name: Hugging Face
      - name: sentence-transformers
      - name: Google Vertex AI
      - name: Ollama
  - name: UseCases
    type: UseCases
    data:
      - name: RAG (Retrieval Augmented Generation)
      - name: Semantic Search
      - name: AI Agent Memory
      - name: Code Search (AST-Aware Chunking)
      - name: Recommendation Systems
      - name: Multi-Modal Search (Text + Images)
      - name: Question Answering Systems
      - name: Knowledge Base Querying
  - name: Standards
    type: Standards
    data:
      - name: OpenAPI Specification
      - name: REST/HTTP
      - name: Apache License 2.0
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
