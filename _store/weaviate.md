---
aid: weaviate
name: Weaviate
description: Weaviate is an open-source, AI-native vector database that enables developers to build semantic search and AI-powered applications. It stores data as vector embeddings alongside structured properties, enabling lightning-fast similarity search using HNSW or flat indexes. Weaviate supports multi-tenancy, automatic vectorization via configurable modules, GraphQL and REST APIs, and enterprise features including authentication, authorization, backups, and replication.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Vector Database
  - AI
  - Machine Learning
  - Semantic Search
  - Open Source
  - GraphQL
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/weaviate/refs/heads/main/apis.yml
created: '2024-06-18'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: weaviate:weaviate-rest-api
    name: Weaviate REST API
    description: The Weaviate REST API provides full programmatic access to vector database operations including object CRUD, schema management, GraphQL vector search, multi-tenancy, backups, authentication, authorization, and cluster management.
    humanURL: https://weaviate.io/developers/weaviate/api/rest
    tags:
      - Vector Database
      - Objects
      - Schema
      - GraphQL
      - Search
      - AI
    properties:
      - url: openapi/weaviate-openapi.yml
        type: OpenAPI
      - url: https://weaviate.io/developers/weaviate/api/rest
        type: Documentation
      - url: https://weaviate.io/developers/weaviate/quickstart
        type: GettingStarted
common:
  - url: https://weaviate.io/developers/weaviate/api/rest
    type: Documentation
  - url: https://github.com/weaviate/weaviate
    type: GitHubRepository
  - url: https://github.com/weaviate
    type: GitHubOrganization
  - url: https://weaviate.io/developers/weaviate/quickstart
    type: GettingStarted
  - url: https://weaviate.io/developers/academy
    type: Learn
  - url: https://weaviate.io/blog
    type: Blog
  - url: https://weaviate.io/community
    type: Community
  - url: https://forum.weaviate.io/
    type: Forum
  - url: https://weaviate.io/slack
    type: Slack
  - url: https://weaviate.io/pricing
    type: Pricing
  - url: https://weaviate.io/podcast
    type: Podcast
  - url: https://newsletter.weaviate.io/
    type: Newsletter
  - url: https://weaviate.io/community/events
    type: Events
  - url: https://github.com/weaviate/weaviate/blob/master/LICENSE
    type: TermsOfService
  - url: https://weaviate.io/security
    type: Security
  - url: https://github.com/weaviate/weaviate/blob/master/CHANGELOG.md
    type: ChangeLog
  - url: https://github.com/weaviate/weaviate/issues
    type: Support
  - type: SpectralRules
    url: rules/weaviate-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/vector-database.yaml
    title: Vector Database Capability
  - type: Vocabulary
    url: vocabulary/weaviate-vocabulary.yml
  - type: Features
    data:
      - Free Trial 14 days then pay-as-you-go
      - 'Flex from $45/mo: $0.255/GiB storage, $0.0264/GiB backup'
      - 'Premium from $400/mo: $0.31875/GiB storage, $0.033/GiB backup'
      - Hybrid search (vector + BM25)
      - Dynamic index, compression, multi-tenancy
      - REST, GraphQL, and gRPC APIs
      - Throughput scales with cluster size
      - Batch import recommended at 100 objects/request
      - Built-in modules for OpenAI, Cohere, HuggingFace embeddings
      - Generative search modules (RAG-style)
      - Multi-tenancy with strict isolation
      - Bring Your Own Vectors (BYOV)
      - RBAC baseline security
      - 99.5% SLA Flex, up to 99.95% Premium
      - Available on AWS, GCP, Azure
      - Open-source self-hosted alternative
    sources:
      - https://weaviate.io/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Semantic Search
        description: Build semantic and hybrid search applications using vector similarity and BM25 keyword search combined.
      - name: RAG Applications
        description: Power Retrieval Augmented Generation (RAG) pipelines by storing and retrieving relevant context for large language model prompts.
      - name: Multi-Modal Search
        description: Search across text, images, and other modalities using unified vector representations.
      - name: AI-Powered Recommendations
        description: Build recommendation engines using object similarity search to find related items based on vector proximity.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
